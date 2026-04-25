"""Wayback Machine + archive.today resurrection.

Per Silverman + Brown: dead-link recovery is a primary investigative move.
Always try Wayback before declaring a URL gone.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class ArchiveSnapshot:
    archive_url: str
    captured_at: str  # ISO8601
    archive_name: str  # "wayback" | "archive_today"
    original_url: str


def wayback_resurrect(url: str, *, timestamp: Optional[str] = None) -> Optional[ArchiveSnapshot]:
    """Retrieve the closest Wayback snapshot to `timestamp` (or latest if None).

    timestamp: YYYYMMDD or YYYY-MM-DD (or full YYYYMMDDhhmmss).
    """
    import httpx
    api = "https://archive.org/wayback/available"
    params = {"url": url}
    if timestamp:
        params["timestamp"] = timestamp.replace("-", "")
    try:
        r = httpx.get(api, params=params, timeout=30.0)
        r.raise_for_status()
        data = r.json()
        snap = data.get("archived_snapshots", {}).get("closest")
        if not snap:
            return None
        return ArchiveSnapshot(
            archive_url=snap["url"],
            captured_at=snap["timestamp"],
            archive_name="wayback",
            original_url=url,
        )
    except (httpx.HTTPError, KeyError):
        return None


def archive_today_snapshot(url: str) -> Optional[ArchiveSnapshot]:
    """archive.today / archive.ph lookup. Best-effort — there's no formal API.
    Returns most recent snapshot URL if discoverable.
    """
    # archive.today exposes a `https://archive.ph/<url>` redirect-or-list page.
    # Without an official API we issue a HEAD and let caller decide.
    import httpx
    try:
        r = httpx.head(f"https://archive.ph/{url}", timeout=30.0, follow_redirects=True)
        if r.status_code == 200:
            return ArchiveSnapshot(
                archive_url=str(r.url),
                captured_at="unknown",
                archive_name="archive_today",
                original_url=url,
            )
        return None
    except httpx.HTTPError:
        return None


def all_snapshots(url: str) -> list[ArchiveSnapshot]:
    """Return all known snapshots from Wayback + archive.today (best-effort)."""
    out: list[ArchiveSnapshot] = []
    s = wayback_resurrect(url)
    if s:
        out.append(s)
    s = archive_today_snapshot(url)
    if s:
        out.append(s)
    return out
