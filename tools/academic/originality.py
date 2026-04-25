"""N-gram overlap detector against a source corpus.

Plagiarism detectors (Turnitin, iThenticate, Grammarly Premium, Copyleaks,
SafeAssign, Quetext) primarily flag overlapping n-grams of length 5–15.
Most flag 7+ word verbatim matches as suspicious.

This tool runs the same check locally so we can audit a draft BEFORE it
ships to a human reviewer / submission.

Strategy:
- Tokenise both source and draft
- Slide an N-gram window across both
- Report any source N-gram that appears in the draft
- Caller decides what to do (rewrite, cite, quote)
"""
from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


# Tokeniser tuned for academic prose: keeps hyphenated words; drops punctuation.
_TOKEN = re.compile(r"\b[\w'-]+\b")


@dataclass(slots=True)
class NGramHit:
    text: str
    length: int            # number of words
    draft_position: int    # token index in draft
    source_id: str         # which source file matched
    source_position: int   # token index in source


@dataclass(slots=True)
class OverlapReport:
    draft_token_count: int
    sources_checked: int
    n_gram_lengths: list[int]
    hits: list[NGramHit] = field(default_factory=list)

    @property
    def total_overlapping_tokens(self) -> int:
        """Approximate count of draft tokens covered by hits.
        Note: overlapping windows can double-count; this is upper-bound."""
        if not self.hits:
            return 0
        return sum(h.length for h in self.hits)

    @property
    def overlap_rate(self) -> float:
        if not self.draft_token_count:
            return 0.0
        # Use unique-position covered count, not raw sum
        covered: set[int] = set()
        for h in self.hits:
            for i in range(h.draft_position, h.draft_position + h.length):
                covered.add(i)
        return len(covered) / self.draft_token_count

    def by_severity(self) -> dict[str, list[NGramHit]]:
        """Group hits by severity:
            critical: 12+ word verbatim match (almost always plagiarism)
            high: 7-11 word match (typically flagged)
            medium: 5-6 word match (often flagged for academic prose)
        """
        out: dict[str, list[NGramHit]] = {"critical": [], "high": [], "medium": []}
        for h in self.hits:
            if h.length >= 12:
                out["critical"].append(h)
            elif h.length >= 7:
                out["high"].append(h)
            else:
                out["medium"].append(h)
        return out


def detect_overlap(
    draft_text: str,
    sources: dict[str, str],   # source_id -> source text
    *,
    n_gram_lengths: tuple[int, ...] = (5, 7, 10, 15),
) -> OverlapReport:
    """Find verbatim overlaps between draft and sources.

    Reports n-gram matches at multiple lengths so caller can prioritise
    long matches first (more severe plagiarism signal).
    """
    draft_tokens = _tokens(draft_text)
    source_tokens: dict[str, list[str]] = {sid: _tokens(s) for sid, s in sources.items()}

    hits: list[NGramHit] = []
    for n in sorted(n_gram_lengths, reverse=True):
        # Build source N-gram index
        source_index: dict[str, list[tuple[str, int]]] = {}
        for sid, toks in source_tokens.items():
            for i in range(len(toks) - n + 1):
                gram = " ".join(toks[i:i + n]).lower()
                source_index.setdefault(gram, []).append((sid, i))

        # Slide draft window
        for i in range(len(draft_tokens) - n + 1):
            gram = " ".join(draft_tokens[i:i + n]).lower()
            if gram in source_index:
                # Take the first source match
                sid, sp = source_index[gram][0]
                hits.append(NGramHit(
                    text=" ".join(draft_tokens[i:i + n]),
                    length=n,
                    draft_position=i,
                    source_id=sid,
                    source_position=sp,
                ))

    # Deduplicate: if a 15-gram hits at position X, the contained 10/7/5-grams
    # at positions X..X+5 are subsumed. Keep only the longest non-subsumed match
    # per draft start position.
    hits.sort(key=lambda h: (h.draft_position, -h.length))
    seen: set[int] = set()
    unique: list[NGramHit] = []
    for h in hits:
        if h.draft_position in seen:
            continue
        # Mark all positions covered by this hit
        for p in range(h.draft_position, h.draft_position + h.length):
            seen.add(p)
        unique.append(h)

    return OverlapReport(
        draft_token_count=len(draft_tokens),
        sources_checked=len(sources),
        n_gram_lengths=list(n_gram_lengths),
        hits=unique,
    )


def detect_overlap_from_files(
    draft_path: str | Path,
    source_paths: Iterable[str | Path],
    **kwargs,
) -> OverlapReport:
    """Convenience wrapper that loads draft + sources from disk."""
    draft = Path(draft_path).read_text(encoding="utf-8", errors="ignore")
    sources = {}
    for sp in source_paths:
        sp = Path(sp)
        sources[sp.name] = sp.read_text(encoding="utf-8", errors="ignore")
    return detect_overlap(draft, sources, **kwargs)


def _tokens(text: str) -> list[str]:
    return _TOKEN.findall(text)
