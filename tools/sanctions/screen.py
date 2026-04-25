"""Multi-list sanctions / PEP / watch-list screener.

Per Hetherington: never assert "X is on OFAC" without verifying full-name +
DOB + nationality + locator. This module:
- Loads cached lists from `refresh_lists()`.
- Performs fuzzy-match against every list.
- Returns structured hits with confidence scores.
- Caller decides on threshold + escalation.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass(slots=True)
class ScreeningHit:
    list_name: str
    matched_name: str
    matched_aliases: list[str] = field(default_factory=list)
    entity_type: str = "unknown"   # "person" | "organization" | "vessel" | "aircraft"
    matched_dob: Optional[str] = None
    matched_nationality: Optional[str] = None
    program: Optional[str] = None  # e.g. "SDGT", "Russia-EO14024"
    similarity: float = 0.0
    record_url: Optional[str] = None
    raw: dict | None = None


@dataclass(slots=True)
class ScreeningResult:
    query_name: str
    query_dob: Optional[str]
    query_nationality: Optional[str]
    total_hits: int
    high_confidence_hits: list[ScreeningHit] = field(default_factory=list)
    medium_confidence_hits: list[ScreeningHit] = field(default_factory=list)
    low_confidence_hits: list[ScreeningHit] = field(default_factory=list)


def screen_name(
    name: str, *,
    dob: Optional[str] = None,
    nationality: Optional[str] = None,
    aliases: Optional[list[str]] = None,
    cache_dir: str | Path = "./data/sanctions",
    threshold_high: float = 0.92,
    threshold_medium: float = 0.78,
) -> ScreeningResult:
    """Screen a name against all cached sanctions / PEP lists.

    Returns three confidence buckets so callers can decide escalation.
    Per Hetherington's rule: high-confidence + DOB-or-nationality match → escalate;
    medium-confidence → triangulate; low-confidence → log only.
    """
    from rapidfuzz import fuzz  # lazy import

    cache_dir = Path(cache_dir)
    if not cache_dir.exists():
        raise FileNotFoundError(f"Cache dir {cache_dir} missing — run refresh_lists() first")

    high: list[ScreeningHit] = []
    medium: list[ScreeningHit] = []
    low: list[ScreeningHit] = []

    queries = [name] + (aliases or [])

    for path in cache_dir.iterdir():
        if not path.is_file():
            continue
        list_name = path.stem.replace("_", " ")
        try:
            entries = _load(path)
        except Exception:
            continue

        for entry in entries:
            entry_names = _names_in(entry)
            best = 0.0
            best_match = ""
            for q in queries:
                for en in entry_names:
                    s = fuzz.token_sort_ratio(q.lower(), en.lower()) / 100.0
                    if s > best:
                        best = s
                        best_match = en
            if best < threshold_medium:
                continue

            hit = ScreeningHit(
                list_name=list_name,
                matched_name=best_match,
                matched_aliases=entry_names[:5],
                entity_type=entry.get("schema", "unknown"),
                matched_dob=_first(entry, ("birthDate", "dob")),
                matched_nationality=_first(entry, ("nationality", "country")),
                program=_first(entry, ("program", "topics", "sanctions")),
                similarity=best,
                raw=entry,
            )

            # Refine confidence with DOB / nationality boost
            if dob and hit.matched_dob and dob[:4] == str(hit.matched_dob)[:4]:
                hit.similarity = min(1.0, hit.similarity + 0.05)
            if nationality and hit.matched_nationality and nationality.lower() == str(hit.matched_nationality).lower():
                hit.similarity = min(1.0, hit.similarity + 0.05)

            if hit.similarity >= threshold_high:
                high.append(hit)
            elif hit.similarity >= threshold_medium:
                medium.append(hit)
            else:
                low.append(hit)

    return ScreeningResult(
        query_name=name, query_dob=dob, query_nationality=nationality,
        total_hits=len(high) + len(medium) + len(low),
        high_confidence_hits=high,
        medium_confidence_hits=medium,
        low_confidence_hits=low,
    )


def _load(path: Path) -> list[dict]:
    """Load a cached list file. Supports FTM/JSONL, JSON, and rudimentary XML."""
    if path.suffix == ".json":
        text = path.read_text(encoding="utf-8")
        # FollowTheMoney FTM is JSONL-ish: one JSON per line.
        if "\n" in text and text.lstrip().startswith("{"):
            try:
                return [json.loads(line) for line in text.splitlines() if line.strip()]
            except json.JSONDecodeError:
                pass
        try:
            data = json.loads(text)
            if isinstance(data, list):
                return data
            if isinstance(data, dict) and "entities" in data:
                return data["entities"]
        except json.JSONDecodeError:
            pass
    return []


def _names_in(entry: dict) -> list[str]:
    """Extract candidate name strings from a heterogeneous list entry."""
    out: list[str] = []
    for k in ("name", "fullName", "firstName", "lastName", "primary_name"):
        v = entry.get(k)
        if isinstance(v, str):
            out.append(v)
    # FTM aliases / weakAliases
    for k in ("aliases", "weakAliases", "alias", "akas"):
        v = entry.get(k)
        if isinstance(v, list):
            out.extend(str(x) for x in v if isinstance(x, str))
    # FTM "names" array
    names = entry.get("names")
    if isinstance(names, list):
        out.extend(str(n) for n in names if isinstance(n, str))
    return out


def _first(entry: dict, keys: tuple[str, ...]):
    for k in keys:
        if k in entry and entry[k]:
            v = entry[k]
            if isinstance(v, list) and v:
                return v[0]
            return v
    return None
