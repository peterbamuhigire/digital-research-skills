"""Banned-phrase scanner — Bailey's cliché list + AI-template tells.

Hard-fails any draft containing these. The discipline is to write around them,
not just remove them — usually the underlying sentence needs a more specific
claim, not a stylistic fix.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field


# Bailey's documented anti-patterns + AI-template phrases (post-2023 LLM tells).
BANNED_PHRASES: dict[str, list[str]] = {
    "vague_hedge_openers": [
        "currently these days",
        "in the modern world",
        "in today's fast-paced world",
        "in today's digital age",
        "in today's society",
        "throughout history",
        "since the dawn of time",
        "since the beginning of time",
        "since time immemorial",
        "in this day and age",
    ],
    "redundant_pairs": [
        "true facts",
        "end result",
        "advance planning",
        "brief summary",
        "global problem in the whole world",
        "first of all and above all",
        "free gift",
        "future plans",
        "past history",
        "completely finished",
    ],
    "idiomatic_pad": [
        "at the end of the day",
        "last but not least",
        "first and foremost",
        "in conclusion to conclude",
        "needless to say",
        "it goes without saying",
        "let's face it",
        "it's high time",
    ],
    "ai_template_signals": [
        "delve into",
        "delve deeper",
        "intricate tapestry",
        "rich tapestry",
        "navigate the complexities of",
        "navigate the intricate",
        "stands as a testament to",
        "play a crucial role",
        "the realm of",
        "in the realm of",
        "myriad of",
        "at its core",
        "at the core of",
        "ever-evolving",
        "ever-changing",
        "in a world where",
        "it is important to note that",
        "it is worth noting that",
        "it is essential to",
        "let us explore",
        "let us delve",
        "let us examine",
        "this essay will explore",
        "this essay will discuss",
        "in this essay i will",
        "in this paper, we will",
    ],
    "essay_scaffolding": [
        "this essay will discuss the advantages and disadvantages",
        "there are many advantages and disadvantages",
        "in conclusion",         # only banned in body text; allowed in conclusion section
        "to conclude",
        "let us now turn to",
    ],
    "personal_attitude_adverbs": [
        "luckily,", "surprisingly,", "remarkably,", "fortunately,",
        "sadly,", "hopefully,", "unfortunately,", "amazingly,",
        "astonishingly,",
    ],
    "vague_quantifiers": [
        "lots of",
        "a lot of",
        "tons of",
        "loads of",
        "hundreds of years ago",
        "thousands of years ago",
        "many many",
        "very many",
    ],
    "informal_register": [
        "kids",
        "boss",
        "thing",
        "stuff",
        "ok,", "okay,",
        "nowadays",
        "wanna", "gonna", "gotta",
    ],
    "absolute_overclaims": [
        # Words that should usually be qualified — but they appear in legitimate
        # contexts too (e.g., "every nation has a flag"), so we flag rather than ban
        "always",
        "never",
        "all",
        "none",
        "every",
        "no one",
        "everyone",
        "proves",
        "definitely",
        "undoubtedly",
        "certainly",
        "obviously",
        "clearly",
        "absolutely",
    ],
}


@dataclass(slots=True)
class BannedPhraseHit:
    phrase: str
    category: str
    position: int
    context: str   # 50 chars surrounding


@dataclass(slots=True)
class BannedPhraseReport:
    hits: list[BannedPhraseHit] = field(default_factory=list)
    total_hits: int = 0
    hard_fail: bool = False           # True if any non-flag-only category hit
    flag_only_hits: int = 0           # absolute_overclaims (warn, don't fail)


# Categories that hard-fail (vs flag-only)
HARD_FAIL_CATEGORIES = {
    "vague_hedge_openers", "redundant_pairs", "idiomatic_pad",
    "ai_template_signals", "essay_scaffolding", "personal_attitude_adverbs",
    "vague_quantifiers", "informal_register",
}


def scan_banned_phrases(text: str, *, in_conclusion_section: bool = False) -> BannedPhraseReport:
    """Find banned phrases in a draft.

    in_conclusion_section: if True, allows "in conclusion" / "to conclude"
    (which are banned only in body text).
    """
    report = BannedPhraseReport()
    text_lower = text.lower()

    for category, phrases in BANNED_PHRASES.items():
        for phrase in phrases:
            # Skip "in conclusion" if we ARE in the conclusion section
            if in_conclusion_section and phrase in ("in conclusion", "to conclude"):
                continue

            pattern = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
            for m in pattern.finditer(text_lower):
                start = max(0, m.start() - 25)
                end = min(len(text), m.end() + 25)
                report.hits.append(BannedPhraseHit(
                    phrase=phrase,
                    category=category,
                    position=m.start(),
                    context=text[start:end],
                ))
                if category in HARD_FAIL_CATEGORIES:
                    report.hard_fail = True
                else:
                    report.flag_only_hits += 1

    report.total_hits = len(report.hits)
    return report


def list_alternatives(phrase: str) -> list[str]:
    """Suggest alternatives for common banned phrases."""
    suggestions: dict[str, list[str]] = {
        "in conclusion": ["overall", "in sum", "to summarise"],
        "throughout history": ["historically", "across centuries", "in past eras"],
        "in today's world": ["currently", "in the present period", "at present"],
        "delve into": ["examine", "investigate", "explore"],
        "navigate": ["address", "manage", "work through"],
        "play a crucial role": ["are central", "matter substantially", "shape"],
        "at its core": ["fundamentally", "in essence", "at base"],
        "myriad of": ["many", "numerous", "various"],
        "lots of": ["a number of", "several", "many"],
        "kids": ["children", "young people"],
        "boss": ["manager", "supervisor"],
        "thing": ["factor", "issue", "element"],
        "luckily": ["", "[remove — bias signal]"],
    }
    return suggestions.get(phrase.lower(), [])
