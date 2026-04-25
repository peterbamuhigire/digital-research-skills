"""Reporting-verb variety auditor.

Academic prose uses verbs to attribute claims to their authors. Repetitive
use of "says" / "states" / "argues" flags weak voice. The Bailey / Trzeciak
discipline: rotate across the verb categories below.

Each category carries a different epistemic stance. Choosing the right verb
is itself an analytical move.
"""
from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field


REPORTING_VERBS: dict[str, list[str]] = {
    "neutral_assertion": [
        "states", "writes", "notes", "observes", "describes", "reports",
        "remarks", "comments",
    ],
    "argumentative": [
        "argues", "contends", "maintains", "asserts", "insists", "claims",
        "posits", "advances", "holds",
    ],
    "tentative": [
        "suggests", "proposes", "implies", "speculates", "conjectures",
        "hypothesises", "indicates",
    ],
    "evaluative_positive": [
        "demonstrates", "shows", "establishes", "confirms", "corroborates",
        "verifies", "substantiates", "evidences",
    ],
    "evaluative_critical": [
        "challenges", "disputes", "questions", "refutes", "contests",
        "rejects", "problematises", "complicates",
    ],
    "agreement": [
        "concurs", "agrees", "endorses", "supports", "corroborates",
    ],
    "discovery": [
        "finds", "discovers", "identifies", "recognises", "uncovers",
        "reveals", "exposes",
    ],
    "interpretation": [
        "interprets", "reads", "understands", "construes", "frames",
        "characterises", "represents",
    ],
    "comparison": [
        "compares", "contrasts", "distinguishes", "differentiates",
        "parallels", "echoes",
    ],
    "highlighting": [
        "highlights", "emphasises", "stresses", "underscores", "foregrounds",
        "draws attention to",
    ],
}


@dataclass(slots=True)
class ReportingVerbReport:
    total_reporting_instances: int
    counts_by_verb: dict[str, int] = field(default_factory=dict)
    counts_by_category: dict[str, int] = field(default_factory=dict)
    overused: list[tuple[str, int]] = field(default_factory=list)
    underused_categories: list[str] = field(default_factory=list)
    suggested_substitutions: dict[str, list[str]] = field(default_factory=dict)


def reporting_verb_variety(
    text: str, *,
    overuse_threshold: int = 5,
) -> ReportingVerbReport:
    """Audit reporting-verb usage in a draft.

    overuse_threshold: a single verb appearing more than this many times in
    the draft is flagged for substitution.
    """
    counts: Counter = Counter()
    by_category: Counter = Counter()
    verb_to_category: dict[str, str] = {
        v: cat for cat, vs in REPORTING_VERBS.items() for v in vs
    }

    # Match verb forms with simple suffix variation
    text_lower = text.lower()
    for verb, category in verb_to_category.items():
        # Match the verb stem with optional suffixes
        stem = verb.rstrip("s") if verb.endswith("s") else verb
        pattern = r"\b" + re.escape(stem) + r"(?:s|ed|ing|d)?\b"
        matches = re.findall(pattern, text_lower)
        if matches:
            counts[verb] += len(matches)
            by_category[category] += len(matches)

    overused = [(v, n) for v, n in counts.items() if n > overuse_threshold]
    overused.sort(key=lambda x: -x[1])

    used_categories = set(by_category.keys())
    all_categories = set(REPORTING_VERBS.keys())
    underused = sorted(all_categories - used_categories)

    suggestions: dict[str, list[str]] = {}
    for v, _ in overused:
        cat = verb_to_category.get(v)
        if cat:
            suggestions[v] = [x for x in REPORTING_VERBS[cat] if x != v]

    return ReportingVerbReport(
        total_reporting_instances=sum(counts.values()),
        counts_by_verb=dict(counts),
        counts_by_category=dict(by_category),
        overused=overused,
        underused_categories=underused,
        suggested_substitutions=suggestions,
    )
