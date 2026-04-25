"""Sanctions list registry + refresh.

Free public sources; no paid vendor required for the baseline coverage.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(slots=True)
class ListSpec:
    name: str
    url: str
    format: str           # "xml" | "csv" | "json" | "ftm"
    refresh_cadence: str  # "daily" | "weekly" | "irregular"
    issuer: str           # e.g. "US Treasury OFAC"
    coverage: str
    free: bool = True


LIST_REGISTRY: list[ListSpec] = [
    ListSpec(
        name="OFAC SDN",
        url="https://www.treasury.gov/ofac/downloads/sdn.xml",
        format="xml",
        refresh_cadence="daily",
        issuer="US Treasury OFAC",
        coverage="US blocked persons + entities",
    ),
    ListSpec(
        name="OFAC Consolidated Sanctions",
        url="https://www.treasury.gov/ofac/downloads/consolidated/consolidated.xml",
        format="xml",
        refresh_cadence="daily",
        issuer="US Treasury OFAC",
        coverage="US sectoral + non-SDN sanctions",
    ),
    ListSpec(
        name="EU Consolidated Financial Sanctions",
        url="https://webgate.ec.europa.eu/fsd/fsf/public/files/xmlFullSanctionsList_1_1/content?token=dG9rZW4tMjAxNw",
        format="xml",
        refresh_cadence="daily",
        issuer="European External Action Service",
        coverage="EU + member-state",
    ),
    ListSpec(
        name="UN Security Council Consolidated",
        url="https://scsanctions.un.org/resources/xml/en/consolidated.xml",
        format="xml",
        refresh_cadence="irregular",
        issuer="United Nations Security Council",
        coverage="UN-wide",
    ),
    ListSpec(
        name="UK HMT Financial Sanctions",
        url="https://ofsistorage.blob.core.windows.net/publishlive/2022format/ConList.xml",
        format="xml",
        refresh_cadence="daily",
        issuer="HM Treasury Office of Financial Sanctions Implementation",
        coverage="UK",
    ),
    ListSpec(
        name="OpenSanctions Default",
        url="https://data.opensanctions.org/datasets/latest/default/entities.ftm.json",
        format="ftm",
        refresh_cadence="daily",
        issuer="OpenSanctions.org",
        coverage="Cross-jurisdictional consolidated + PEP + sanctions",
    ),
    ListSpec(
        name="OpenSanctions PEPs",
        url="https://data.opensanctions.org/datasets/latest/peps/entities.ftm.json",
        format="ftm",
        refresh_cadence="daily",
        issuer="OpenSanctions.org",
        coverage="Politically Exposed Persons (global)",
    ),
    ListSpec(
        name="ICIJ Offshore Leaks",
        url="https://offshoreleaks.icij.org/",
        format="csv",
        refresh_cadence="irregular",
        issuer="ICIJ",
        coverage="Offshore registries (Panama / Paradise / Pandora / Bahamas / OffshoreLeaks)",
    ),
]


def refresh_lists(
    *, dest_dir: str | Path = "./data/sanctions",
    only: Optional[list[str]] = None,
) -> dict[str, Path]:
    """Pull each registered list into local cache; return name → path map."""
    from ..scraping.http_client import fetch
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    out: dict[str, Path] = {}
    for spec in LIST_REGISTRY:
        if only is not None and spec.name not in only:
            continue
        ext = spec.format if spec.format != "ftm" else "json"
        local = dest_dir / f"{spec.name.replace(' ', '_').lower()}.{ext}"
        try:
            r = fetch(spec.url, respect_robots=False, max_retries=2)
            local.write_bytes(r.content)
            out[spec.name] = local
        except Exception:
            # Don't stop the whole refresh on one failure.
            continue
    return out
