"""Direct-quote formatting + attribution helpers.

Per Bailey: quote sparingly (typically <5% of total words). Use direct
quotation only when:
1. The exact phrasing is essential (technical / legal / historical)
2. The quote is itself the object of analysis
3. Paraphrase would distort the meaning

For everything else, paraphrase + cite.
"""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(slots=True)
class FormattedQuote:
    formatted: str
    is_block_quote: bool
    word_count: int


def canonicalize_quote(
    quote_text: str, *,
    author: str,
    year: int | str,
    page: int | str | None = None,
    style: str = "apa",            # "apa" | "harvard" | "chicago_ad" | "mla"
    block_quote_threshold: int = 40,
) -> FormattedQuote:
    """Format a direct quote with citation, choosing inline vs block quote
    based on length.

    block_quote_threshold: quotes >= this many words become block quotes
    (most styles use 40 for APA, 4 lines for MLA).
    """
    words = quote_text.split()
    n_words = len(words)
    is_block = n_words >= block_quote_threshold

    citation = _format_citation(author, year, page, style)

    if is_block:
        # Block quote: indented, no quotation marks (in most styles)
        formatted = f"\n\n    {quote_text.strip()} {citation}\n\n"
    else:
        formatted = f'"{quote_text.strip()}" {citation}'

    return FormattedQuote(
        formatted=formatted,
        is_block_quote=is_block,
        word_count=n_words,
    )


def _format_citation(author: str, year, page, style: str) -> str:
    if style in ("apa", "harvard"):
        if page is not None:
            return f"({author}, {year}, p. {page})"
        return f"({author}, {year})"
    if style == "chicago_ad":
        if page is not None:
            return f"({author} {year}, {page})"
        return f"({author} {year})"
    if style == "mla":
        if page is not None:
            return f"({author} {page})"
        return f"({author})"
    # Default
    return f"({author}, {year})"


def format_block_quote(
    quote_text: str, *,
    author: str,
    year: int | str,
    page: int | str | None = None,
    style: str = "apa",
) -> FormattedQuote:
    """Force block quote regardless of length."""
    return canonicalize_quote(
        quote_text, author=author, year=year, page=page, style=style,
        block_quote_threshold=0,
    )


def detect_quote_density(text: str) -> float:
    """Estimate proportion of text that is direct quotation.

    Returns 0-1 ratio of quoted-token-count to total-token-count.
    """
    quoted_pattern = re.compile(r'"([^"]+)"')
    quotes = quoted_pattern.findall(text)
    quoted_words = sum(len(q.split()) for q in quotes)
    total_words = len(re.findall(r"\b\w+\b", text))
    if not total_words:
        return 0.0
    return quoted_words / total_words
