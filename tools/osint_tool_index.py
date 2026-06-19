"""Candidate OSINT tool/source index extraction.

This module turns public toolkit pages into low-confidence candidate records.
It does not verify that a linked tool is authoritative, lawful to use, current,
or suitable for a project. Verification stays in the registry workflow.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import yaml


@dataclass(frozen=True)
class OSINTToolLead:
    id: str
    name: str
    url: str
    category: str
    geography: str
    source_ids: list[str]
    access_model: str
    legal_notes: str
    verification: str
    confidence: str
    status: str
    last_checked: str


@dataclass(frozen=True)
class IndexResult:
    source_added: bool
    tools_added: int
    tools_seen: int


def fetch_source_html(url: str, *, respect_robots: bool = True) -> tuple[str, str]:
    """Fetch source HTML through the engine scraping wrapper."""
    from tools.scraping.http_client import fetch

    result = fetch(url, respect_robots=respect_robots)
    return result.text, result.final_url


def build_source_record(url: str, *, title: str | None = None, source_id: str | None = None) -> dict[str, Any]:
    today = _today()
    return {
        "id": source_id or _stable_id("SRC-OSINT", url),
        "title": title or url,
        "ref": url,
        "tier": "5",
        "accessed": today,
        "verification": "candidate-osint-toolkit-source; source-evaluation required before use",
        "confidence": "low",
    }


def extract_tool_leads(
    html: str,
    *,
    base_url: str,
    source_id: str,
    geography: str = "global",
    limit: int | None = None,
) -> list[OSINTToolLead]:
    parser = _ToolkitHTMLParser(base_url=base_url, source_id=source_id, geography=geography)
    parser.feed(html)
    leads = parser.leads
    return leads[:limit] if limit is not None else leads


def append_tool_index_records(project_root: Path, source_record: dict[str, Any], leads: list[OSINTToolLead]) -> IndexResult:
    registry_dir = project_root / "_registry"
    registry_dir.mkdir(parents=True, exist_ok=True)

    source_added = _append_source_if_missing(registry_dir / "sources.yaml", source_record)
    tools_added = _append_tools_if_missing(registry_dir / "osint-tool-index.yaml", leads)
    return IndexResult(source_added=source_added, tools_added=tools_added, tools_seen=len(leads))


class _ToolkitHTMLParser(HTMLParser):
    def __init__(self, *, base_url: str, source_id: str, geography: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.source_netloc = urlparse(base_url).netloc.lower()
        self.source_id = source_id
        self.geography = geography
        self.category = ""
        self._heading_tag: str | None = None
        self._heading_text: list[str] = []
        self._anchor_href: str | None = None
        self._anchor_text: list[str] = []
        self._seen_urls: set[str] = set()
        self.leads: list[OSINTToolLead] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"h2", "h3", "h4", "h5"}:
            self._heading_tag = tag
            self._heading_text = []
            return

        if tag != "a":
            return
        attr_map = {name.lower(): value for name, value in attrs}
        href = attr_map.get("href")
        if href:
            self._anchor_href = href
            self._anchor_text = []

    def handle_data(self, data: str) -> None:
        if self._heading_tag:
            self._heading_text.append(data)
        if self._anchor_href:
            self._anchor_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == self._heading_tag:
            heading = _clean_text(" ".join(self._heading_text))
            if heading and heading.lower() not in {"subscribe", "share"}:
                self.category = heading
            self._heading_tag = None
            self._heading_text = []
            return

        if tag != "a" or not self._anchor_href:
            return

        href = urljoin(self.base_url, self._anchor_href)
        name = _clean_text(" ".join(self._anchor_text))
        self._anchor_href = None
        self._anchor_text = []

        if not _is_indexable_link(href, name, self.source_netloc):
            return
        if href in self._seen_urls:
            return

        self._seen_urls.add(href)
        category = self.category or "uncategorized"
        self.leads.append(_lead_from_link(name=name, href=href, category=category, source_id=self.source_id, geography=self.geography))


def _lead_from_link(*, name: str, href: str, category: str, source_id: str, geography: str) -> OSINTToolLead:
    return OSINTToolLead(
        id=_stable_id("OSINT", href),
        name=name,
        url=href,
        category=category,
        geography=geography,
        source_ids=[source_id],
        access_model="unverified",
        legal_notes="Verify robots.txt, terms of service, jurisdiction, and lawful purpose before use.",
        verification=f"candidate lead from {source_id}; primary-site verification pending",
        confidence="low",
        status="candidate",
        last_checked=_today(),
    )


def _append_source_if_missing(path: Path, source_record: dict[str, Any]) -> bool:
    data = _load_registry(path, "sources")
    rows = data["sources"]
    if any(row.get("id") == source_record["id"] or row.get("ref") == source_record["ref"] for row in rows):
        return False
    rows.append(source_record)
    _write_registry(path, data)
    return True


def _append_tools_if_missing(path: Path, leads: list[OSINTToolLead]) -> int:
    data = _load_registry(path, "osint_tools")
    rows = data["osint_tools"]
    existing_by_url = {row.get("url"): row for row in rows}
    added = 0

    for lead in leads:
        record = asdict(lead)
        existing = existing_by_url.get(lead.url)
        if existing:
            existing_sources = existing.get("source_ids") or []
            if isinstance(existing_sources, list):
                merged_sources = sorted({*map(str, existing_sources), *lead.source_ids})
                existing["source_ids"] = merged_sources
            if existing.get("access_model") == "unknown":
                existing["access_model"] = "unverified"
            continue
        rows.append(record)
        existing_by_url[lead.url] = record
        added += 1

    _write_registry(path, data)
    return added


def _load_registry(path: Path, root_key: str) -> dict[str, list[dict[str, Any]]]:
    if not path.exists():
        return {root_key: []}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rows = data.get(root_key)
    if not isinstance(rows, list):
        rows = []
    return {root_key: rows}


def _write_registry(path: Path, data: dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False), encoding="utf-8")


def _is_indexable_link(href: str, name: str, source_netloc: str) -> bool:
    parsed = urlparse(href)
    if parsed.scheme not in {"http", "https"}:
        return False
    if parsed.netloc.lower() == source_netloc:
        return False
    if not name or name.lower() in {"share", "subscribe", "sign in"}:
        return False
    return True


def _stable_id(prefix: str, value: str) -> str:
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:10].upper()
    return f"{prefix}-{digest}"


def _clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _today() -> str:
    return datetime.now(timezone.utc).date().isoformat()
