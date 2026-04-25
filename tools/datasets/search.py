"""Federated dataset search across registered hosts.

Most government open-data portals are CKAN-based and expose `/api/3/action/package_search`.
Others (Socrata, custom) need per-host adapters — implemented incrementally.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, Optional

from .registry import DATASET_REGISTRY, DatasetHost


@dataclass(slots=True)
class DatasetSearchResult:
    title: str
    description: str
    url: str
    host: str
    formats: list[str]   # e.g. ["CSV", "JSON", "XLSX"]
    last_modified: Optional[str] = None
    license: Optional[str] = None
    tags: list[str] | None = None


def search_datasets(
    query: str, *,
    hosts: Optional[list[DatasetHost]] = None,
    per_host: int = 10,
    coverage_filter: Optional[str] = None,
) -> Iterator[DatasetSearchResult]:
    """Federated search — yields results across all configured hosts."""
    targets = hosts or DATASET_REGISTRY
    if coverage_filter:
        targets = [h for h in targets if coverage_filter.lower() in h.coverage.lower()]
    for host in targets:
        try:
            yield from _search_host(host, query, per_host)
        except Exception:
            # Don't let one host's failure stop the others.
            continue


def _search_host(host: DatasetHost, query: str, limit: int) -> Iterator[DatasetSearchResult]:
    if host.type == "ckan":
        yield from _search_ckan(host, query, limit)
    elif host.type == "huggingface":
        yield from _search_huggingface(host, query, limit)
    elif host.type == "zenodo":
        yield from _search_zenodo(host, query, limit)
    # Other types: implement on demand — explicit gap rather than silent failure.


def _search_ckan(host: DatasetHost, query: str, limit: int) -> Iterator[DatasetSearchResult]:
    import httpx
    api = f"{host.base_url.rstrip('/')}/api/3/action/package_search"
    r = httpx.get(api, params={"q": query, "rows": limit}, timeout=30.0)
    r.raise_for_status()
    data = r.json()
    for pkg in data.get("result", {}).get("results", []):
        yield DatasetSearchResult(
            title=pkg.get("title", ""),
            description=pkg.get("notes", "") or "",
            url=f"{host.base_url.rstrip('/')}/dataset/{pkg.get('name', '')}",
            host=host.name,
            formats=[r.get("format", "").upper() for r in pkg.get("resources", []) if r.get("format")],
            last_modified=pkg.get("metadata_modified"),
            license=pkg.get("license_title"),
            tags=[t.get("name") for t in pkg.get("tags", []) if t.get("name")],
        )


def _search_huggingface(host: DatasetHost, query: str, limit: int) -> Iterator[DatasetSearchResult]:
    import httpx
    r = httpx.get(host.base_url, params={"search": query, "limit": limit}, timeout=30.0)
    r.raise_for_status()
    for ds in r.json()[:limit]:
        if not isinstance(ds, dict):
            continue
        yield DatasetSearchResult(
            title=ds.get("id", ""),
            description=(ds.get("description") or "")[:500],
            url=f"https://huggingface.co/datasets/{ds.get('id', '')}",
            host=host.name,
            formats=["parquet" if "parquet" in str(ds).lower() else "json"],
            last_modified=ds.get("lastModified"),
            tags=ds.get("tags") or [],
        )


def _search_zenodo(host: DatasetHost, query: str, limit: int) -> Iterator[DatasetSearchResult]:
    import httpx
    api = f"{host.base_url.rstrip('/')}/records"
    r = httpx.get(api, params={"q": query, "size": limit, "type": "dataset"}, timeout=30.0)
    r.raise_for_status()
    for rec in r.json().get("hits", {}).get("hits", []):
        meta = rec.get("metadata", {}) or {}
        yield DatasetSearchResult(
            title=meta.get("title", ""),
            description=(meta.get("description") or "")[:500],
            url=rec.get("links", {}).get("self_html", ""),
            host=host.name,
            formats=[(f.get("filename", "").rsplit(".", 1)[-1] or "").upper()
                     for f in rec.get("files", []) if f.get("filename")],
            last_modified=meta.get("publication_date"),
            license=(meta.get("license") or {}).get("id"),
            tags=meta.get("keywords") or [],
        )
