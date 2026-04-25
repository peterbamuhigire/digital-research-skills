"""Citation-density audit.

Per academic norms: each substantive paragraph should carry at least one
citation; assertion-heavy paragraphs need 2-3. Paragraphs with NO citations
are either (a) the writer's own argument (acceptable in conclusion / discussion)
or (b) plagiarism risk (claims as if original).

This tool counts inline citations per paragraph and flags paragraphs that
look thin.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Literal


# Common citation patterns across major styles.
_CITATION_PATTERNS = [
    # APA / Harvard: (Author, 2024) or (Author 2024) or (Author, 2024, p. 12)
    re.compile(r"\(\s*[A-Z][\w'-]+(?:\s+(?:and|&|et al\.?))?\s*,?\s+(?:19|20)\d{2}[a-z]?(?:\s*,\s*p+\.\s*\d+(?:\s*-\s*\d+)?)?\s*\)"),
    # APA narrative: Author (2024)
    re.compile(r"[A-Z][\w'-]+(?:\s+(?:and|&|et al\.?))?\s*\(\s*(?:19|20)\d{2}[a-z]?\s*\)"),
    # Chicago notes: footnote markers — count as citations
    re.compile(r"\[\d+\]"),
    # Vancouver: numeric superscript — appear as [1] or (1) in plain text
    re.compile(r"\(\d{1,3}(?:\s*[,\-]\s*\d{1,3})*\)"),
    # MLA: (Author 12) — page only
    re.compile(r"\(\s*[A-Z][\w'-]+\s+\d+\s*\)"),
]


@dataclass(slots=True)
class ParagraphAudit:
    paragraph_index: int
    word_count: int
    citation_count: int
    severity: Literal["ok", "thin", "uncited", "over-cited"]
    text_preview: str


@dataclass(slots=True)
class CitationDensityReport:
    paragraphs: list[ParagraphAudit]
    total_paragraphs: int
    total_citations: int
    citations_per_1000_words: float
    thin_paragraphs: list[int] = field(default_factory=list)
    uncited_paragraphs: list[int] = field(default_factory=list)


def citation_density(
    text: str, *,
    min_words_for_audit: int = 50,
    min_citations_per_substantive_paragraph: int = 1,
    over_cite_threshold_per_100_words: float = 5.0,
    exempt_paragraphs: tuple[str, ...] = ("introduction", "conclusion", "abstract"),
) -> CitationDensityReport:
    """Audit a draft's citation density.

    exempt_paragraphs: paragraphs starting with these section names are
    expected to carry the author's own argument; they're flagged as "ok"
    even with no citations.
    """
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    audits: list[ParagraphAudit] = []
    total_citations = 0
    total_words = 0

    for i, p in enumerate(paragraphs):
        words = len(re.findall(r"\b\w+\b", p))
        total_words += words
        cites = _count_citations(p)
        total_citations += cites

        is_exempt = any(p.lower().lstrip("# ").startswith(s) for s in exempt_paragraphs)

        if words < min_words_for_audit:
            severity: Literal["ok", "thin", "uncited", "over-cited"] = "ok"
        elif is_exempt:
            severity = "ok"
        elif cites == 0:
            severity = "uncited"
        elif cites < min_citations_per_substantive_paragraph:
            severity = "thin"
        elif cites > (words / 100) * over_cite_threshold_per_100_words:
            severity = "over-cited"
        else:
            severity = "ok"

        audits.append(ParagraphAudit(
            paragraph_index=i,
            word_count=words,
            citation_count=cites,
            severity=severity,
            text_preview=p[:120] + ("…" if len(p) > 120 else ""),
        ))

    thin = [a.paragraph_index for a in audits if a.severity == "thin"]
    uncited = [a.paragraph_index for a in audits if a.severity == "uncited"]

    return CitationDensityReport(
        paragraphs=audits,
        total_paragraphs=len(audits),
        total_citations=total_citations,
        citations_per_1000_words=(total_citations * 1000 / total_words) if total_words else 0.0,
        thin_paragraphs=thin,
        uncited_paragraphs=uncited,
    )


def _count_citations(text: str) -> int:
    n = 0
    for pat in _CITATION_PATTERNS:
        n += len(pat.findall(text))
    return n
