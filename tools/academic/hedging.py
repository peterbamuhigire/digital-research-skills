"""Hedging / modality auditor.

Academic prose is hedged. Strong unqualified claims (e.g., "this is the
cause of X") are often overclaims. The discipline is to qualify.

This tool counts hedge markers and warns when assertion-density is too
absolute.
"""
from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field


HEDGING_MARKERS: dict[str, list[str]] = {
    "modal_verbs": [
        "may", "might", "could", "would", "can", "should",
    ],
    "epistemic_adverbs": [
        "perhaps", "possibly", "probably", "presumably", "apparently",
        "seemingly", "arguably", "supposedly",
    ],
    "approximators": [
        "approximately", "roughly", "around", "about", "some", "several",
        "a number of", "many",
    ],
    "softening_phrases": [
        "it is possible that", "it appears that", "it seems that",
        "this suggests", "this implies", "to some extent", "in part",
        "in some respects", "broadly speaking",
    ],
    "evidentials": [
        "according to", "based on", "the evidence suggests",
        "research indicates", "studies show",
    ],
    "qualifiers": [
        "tend to", "tends to", "tendency", "frequently", "often", "usually",
        "in most cases", "in many cases", "in general",
    ],
}

OVERCLAIM_RED_FLAGS = [
    # Absolute claims that should usually be qualified
    "always", "never", "all", "none", "every", "no one", "everyone",
    "proves", "definitely", "undoubtedly", "certainly", "without doubt",
    "obviously", "clearly", "absolutely",
]


@dataclass(slots=True)
class HedgingReport:
    word_count: int
    hedge_count: int
    overclaim_count: int
    hedge_rate_per_1000_words: float
    overclaim_rate_per_1000_words: float
    counts_by_category: dict[str, int] = field(default_factory=dict)
    overclaims_found: list[str] = field(default_factory=list)
    verdict: str = ""


def hedging_audit(
    text: str, *,
    target_hedge_rate: float = 8.0,    # hedges per 1000 words for academic prose
    max_overclaim_rate: float = 1.0,
) -> HedgingReport:
    """Audit hedging discipline in academic prose.

    target_hedge_rate: typical academic prose carries 6-12 hedges / 1000 words.
    Below 4 = under-hedged (sounds dogmatic).
    Above 15 = over-hedged (sounds wishy-washy).
    """
    words = re.findall(r"\b\w+\b", text)
    word_count = len(words)
    text_lower = text.lower()

    by_cat: Counter = Counter()
    for cat, markers in HEDGING_MARKERS.items():
        for m in markers:
            pattern = r"\b" + re.escape(m) + r"\b"
            n = len(re.findall(pattern, text_lower))
            if n:
                by_cat[cat] += n

    overclaims_found: list[str] = []
    for oc in OVERCLAIM_RED_FLAGS:
        pattern = r"\b" + re.escape(oc) + r"\b"
        if re.search(pattern, text_lower):
            overclaims_found.append(oc)

    hedge_count = sum(by_cat.values())
    overclaim_count = len(overclaims_found)

    hedge_rate = (hedge_count * 1000 / word_count) if word_count else 0.0
    overclaim_rate = (overclaim_count * 1000 / word_count) if word_count else 0.0

    if word_count < 300:
        verdict = "Too short to audit hedging meaningfully."
    elif hedge_rate < 4 and overclaim_rate > max_overclaim_rate:
        verdict = "UNDER-HEDGED. Sounds dogmatic. Add modal verbs / approximators."
    elif hedge_rate > 15:
        verdict = "OVER-HEDGED. Sounds wishy-washy. Drop some qualifiers."
    elif hedge_rate < target_hedge_rate * 0.5:
        verdict = "Hedging below academic norm. Consider qualifying strong claims."
    else:
        verdict = "Hedging within academic norm."

    return HedgingReport(
        word_count=word_count,
        hedge_count=hedge_count,
        overclaim_count=overclaim_count,
        hedge_rate_per_1000_words=hedge_rate,
        overclaim_rate_per_1000_words=overclaim_rate,
        counts_by_category=dict(by_cat),
        overclaims_found=overclaims_found,
        verdict=verdict,
    )
