"""Stakeholder-first reconnaissance.

Brown's Chapter 4 codified: before searching, ask *who cares about this
topic enough to publish on it?* — then build a `site:` query bundle for
each likely publisher.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .tld_atlas import US_STATE_DOMAINS, FOREIGN_GOV_DOMAINS, IGO_DOMAINS


@dataclass(slots=True)
class Stakeholder:
    name: str
    domain: str
    category: str  # "igo" | "foreign_gov" | "us_federal" | "us_state" | "ngo" | "academic" | "trade" | "media"
    relevance: float = 1.0  # 0.0–1.0, set by caller


def enumerate_stakeholders(
    *, topic: str,
    country_focus: list[str] | None = None,
    include_us_states: bool = False,
    include_igos: bool = True,
    extra_ngos: list[str] | None = None,
    extra_academic: list[str] | None = None,
) -> list[Stakeholder]:
    """Build the candidate stakeholder list for a topic.

    Caller refines by relevance after enumeration.
    """
    out: list[Stakeholder] = []

    if include_igos:
        for d in IGO_DOMAINS:
            out.append(Stakeholder(name=d.split(".")[0].upper(), domain=d, category="igo"))

    if country_focus:
        for iso2 in country_focus:
            d = FOREIGN_GOV_DOMAINS.get(iso2.upper())
            if d:
                out.append(Stakeholder(name=f"{iso2} government", domain=d, category="foreign_gov"))

    if include_us_states:
        for state, domains in US_STATE_DOMAINS.items():
            for d in domains:
                out.append(Stakeholder(name=f"{state} government", domain=d, category="us_state"))

    out.append(Stakeholder(name="US federal", domain=".gov", category="us_federal"))
    out.append(Stakeholder(name="US military", domain=".mil", category="us_federal"))
    out.append(Stakeholder(name="US academic", domain=".edu", category="academic"))

    for n in extra_ngos or []:
        out.append(Stakeholder(name=n, domain=n, category="ngo"))
    for a in extra_academic or []:
        out.append(Stakeholder(name=a, domain=a, category="academic"))

    return out


def stakeholder_query_bundle(
    topic: str,
    stakeholders: Iterable[Stakeholder],
    *,
    file_types: list[str] | None = None,
    quote_topic: bool = True,
) -> list[str]:
    """Generate ready-to-issue Google queries for each stakeholder.

    file_types: ['pdf', 'xlsx'] etc.
    quote_topic: wrap topic in "" for phrase precision.
    """
    q_topic = f'"{topic}"' if quote_topic else topic
    queries: list[str] = []
    for s in stakeholders:
        base = f"{q_topic} site:{s.domain}"
        if file_types:
            for ft in file_types:
                queries.append(f"{base} filetype:{ft}")
        else:
            queries.append(base)
    return queries
