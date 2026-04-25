"""Anti-defamation identity triangulator.

Per Hetherington: never attribute a derogatory hit without ≥3 vendors agreeing.
Common-name confusion is the #1 defamation-risk vector in DD work.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(slots=True)
class IdentityCandidate:
    source: str            # "Accurint" | "TLO" | "CLEAR" | "Companies House" | "OpenCorporates" | ...
    name: str
    aliases: list[str] = field(default_factory=list)
    dob: Optional[str] = None
    address: Optional[str] = None
    employer: Optional[str] = None
    nationality: Optional[str] = None
    identifier: Optional[str] = None  # passport / SSN-last-4 / DUNS / etc.
    raw: dict | None = None


@dataclass(slots=True)
class IdentityVerdict:
    name: str
    dob: Optional[str]
    confidence: str   # "confirmed" | "probable" | "unconfirmed"
    confirmed_attributes: dict[str, list[str]]  # attr → list of sources confirming
    conflicting_attributes: dict[str, list[tuple[str, str]]]  # attr → [(value, source)]
    sources_consulted: list[str]
    triangulation_passed: bool   # ≥3 sources agree on at least one identifier


def triangulate_identity(
    name: str, candidates: list[IdentityCandidate], *,
    min_sources: int = 3,
) -> IdentityVerdict:
    """Resolve an identity across N source candidates. Hetherington's discipline.

    A finding is "confirmed" when at least `min_sources` (default 3) candidates
    agree on at least one strong identifier (DOB OR address OR identifier).
    """
    confirmed: dict[str, list[str]] = {}
    conflicting: dict[str, list[tuple[str, str]]] = {}

    def _record(attr: str, value: Optional[str], source: str) -> None:
        if not value:
            return
        if attr not in confirmed:
            confirmed[attr] = []
        if value not in [v for v, _ in confirmed.get(attr + "_values", [])]:
            confirmed.setdefault(attr + "_values", []).append((value, source))
        else:
            confirmed[attr].append(source)

    # Gather attribute-value pairs
    by_attr: dict[str, dict[str, list[str]]] = {}
    for c in candidates:
        for attr, val in (("dob", c.dob), ("address", c.address),
                          ("employer", c.employer), ("nationality", c.nationality),
                          ("identifier", c.identifier)):
            if val:
                by_attr.setdefault(attr, {}).setdefault(val, []).append(c.source)

    triangulated_attrs: dict[str, list[str]] = {}
    for attr, val_to_sources in by_attr.items():
        for val, sources in val_to_sources.items():
            if len(set(sources)) >= min_sources:
                triangulated_attrs.setdefault(attr, []).extend(sources)
        # Conflicts: same attr with different values across sources
        if len(val_to_sources) > 1:
            conflicting[attr] = [(v, s) for v, ss in val_to_sources.items() for s in ss]

    triangulation_passed = bool(triangulated_attrs)

    if triangulation_passed and len(triangulated_attrs.get("identifier", [])) >= min_sources:
        confidence = "confirmed"
    elif triangulation_passed:
        confidence = "probable"
    else:
        confidence = "unconfirmed"

    # Pick the most-supported DOB to put on the verdict
    dob = None
    if "dob" in by_attr:
        dob = max(by_attr["dob"].keys(), key=lambda v: len(by_attr["dob"][v]))

    return IdentityVerdict(
        name=name, dob=dob, confidence=confidence,
        confirmed_attributes=triangulated_attrs,
        conflicting_attributes=conflicting,
        sources_consulted=list({c.source for c in candidates}),
        triangulation_passed=triangulation_passed,
    )
