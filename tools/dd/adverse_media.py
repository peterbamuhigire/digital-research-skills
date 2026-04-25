"""Adverse-media (negative-news) search with disambiguation guard.

Hetherington's multi-source rule: combine multiple search engines + GDELT +
foreign-press where relevant. Filter by subject identifiers (DOB, employer,
location) to reduce common-name false positives.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator, Optional


@dataclass(slots=True)
class AdverseMediaHit:
    title: str
    url: str
    snippet: str
    source: str            # outlet
    published: Optional[str] = None
    language: str = "en"
    risk_terms: list[str] = field(default_factory=list)  # which negative terms hit
    subject_identifiers_matched: list[str] = field(default_factory=list)
    confidence: str = "low"  # "high" | "medium" | "low"
    engine: str = ""       # which search engine surfaced this


# Curated negative-news term sets. Caller can extend.
RISK_TERMS_EN: dict[str, list[str]] = {
    "financial_crime": [
        "fraud", "embezzlement", "money laundering", "ponzi", "tax evasion",
        "insider trading", "bribery", "kickback", "corrupt", "racketeer",
    ],
    "regulatory": [
        "sanctions", "fined", "penalty", "consent decree", "cease and desist",
        "debarred", "disqualified", "censure", "revoked",
    ],
    "criminal": [
        "indicted", "convicted", "arrested", "charged", "sentenced",
        "guilty plea", "felony", "criminal complaint",
    ],
    "litigation": [
        "lawsuit", "sued", "class action", "settlement", "judgment against",
    ],
    "reputational": [
        "scandal", "investigation", "probe", "exposé", "allegation",
    ],
}


def search_adverse_media(
    subject_name: str, *,
    aliases: Optional[list[str]] = None,
    subject_identifiers: Optional[list[str]] = None,  # e.g. ["1965", "Acme Corp", "Nairobi"]
    engines: Optional[list[str]] = None,  # ["google_cse", "serpapi", "brave"]
    risk_categories: Optional[list[str]] = None,
    languages: tuple[str, ...] = ("en",),
    per_query_limit: int = 10,
) -> Iterator[AdverseMediaHit]:
    """Run multi-engine, multi-term adverse-media search.

    Combines subject name × risk terms across engines. Filter results by
    subject identifiers to reduce false positives (Hetherington's anti-
    defamation rule).
    """
    from ..google.search_api import GoogleSearchClient, SerpAPIClient

    risk_categories = risk_categories or list(RISK_TERMS_EN.keys())
    queries = [subject_name] + (aliases or [])
    engines = engines or ["google_cse"]

    for engine in engines:
        client = _make_client(engine)
        if client is None:
            continue
        for q_subject in queries:
            for cat in risk_categories:
                for term in RISK_TERMS_EN.get(cat, []):
                    q = f'"{q_subject}" "{term}"'
                    try:
                        for r in client.search(q, num=per_query_limit):
                            ident_matched = _identifiers_in(r.snippet, subject_identifiers or [])
                            confidence = _confidence(ident_matched, len(subject_identifiers or []))
                            yield AdverseMediaHit(
                                title=r.title, url=r.url, snippet=r.snippet,
                                source=_outlet_from_url(r.url),
                                risk_terms=[term],
                                subject_identifiers_matched=ident_matched,
                                confidence=confidence,
                                engine=engine,
                            )
                    except Exception:
                        continue


def _make_client(engine: str):
    from ..google.search_api import GoogleSearchClient, SerpAPIClient
    try:
        if engine == "google_cse":
            return GoogleSearchClient()
        if engine == "serpapi":
            return SerpAPIClient()
    except RuntimeError:
        return None
    return None


def _identifiers_in(text: str, identifiers: list[str]) -> list[str]:
    text_l = text.lower()
    return [i for i in identifiers if i.lower() in text_l]


def _confidence(matched: list[str], total: int) -> str:
    if total == 0:
        return "low"
    ratio = len(matched) / total
    if ratio >= 0.5:
        return "high"
    if ratio > 0:
        return "medium"
    return "low"


def _outlet_from_url(url: str) -> str:
    from urllib.parse import urlparse
    return urlparse(url).netloc
