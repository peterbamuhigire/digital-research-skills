"""Raw-HTML caches.

Lawson's central insight: store raw HTML in addition to extracted fields.
Re-extraction is free; re-crawling is expensive. Caches let you experiment
with selectors without re-fetching.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
import time
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Protocol


@dataclass(slots=True)
class CachedResponse:
    url: str
    status: int
    headers: dict[str, str]
    body: bytes
    fetched_at: float


class CacheBackend(Protocol):
    def get(self, url: str) -> Optional[CachedResponse]: ...
    def put(self, url: str, response: CachedResponse) -> None: ...
    def delete(self, url: str) -> None: ...


def _key(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()


class DiskCache:
    """Compressed pickle cache on disk, keyed by URL hash."""

    def __init__(self, root: str | Path, ttl_seconds: int = 30 * 24 * 3600) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.ttl_seconds = ttl_seconds

    def _path(self, url: str) -> Path:
        h = _key(url)
        sub = self.root / h[:2]
        sub.mkdir(parents=True, exist_ok=True)
        return sub / f"{h}.bin"

    def get(self, url: str) -> Optional[CachedResponse]:
        p = self._path(url)
        if not p.exists():
            return None
        try:
            raw = zlib.decompress(p.read_bytes())
            obj = json.loads(raw[: raw.index(b"\n")])
            body = raw[raw.index(b"\n") + 1 :]
            cr = CachedResponse(url=obj["url"], status=obj["status"], headers=obj["headers"],
                                body=body, fetched_at=obj["fetched_at"])
            if (time.time() - cr.fetched_at) > self.ttl_seconds:
                return None
            return cr
        except Exception:
            return None

    def put(self, url: str, response: CachedResponse) -> None:
        p = self._path(url)
        meta = json.dumps({
            "url": response.url,
            "status": response.status,
            "headers": response.headers,
            "fetched_at": response.fetched_at,
        }).encode("utf-8")
        blob = meta + b"\n" + response.body
        p.write_bytes(zlib.compress(blob, level=6))

    def delete(self, url: str) -> None:
        p = self._path(url)
        if p.exists():
            p.unlink()


class SQLiteCache:
    """Single-file SQLite cache, indexed by URL hash."""

    def __init__(self, path: str | Path, ttl_seconds: int = 30 * 24 * 3600) -> None:
        self.path = str(path)
        self.ttl_seconds = ttl_seconds
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """CREATE TABLE IF NOT EXISTS cache (
                       key TEXT PRIMARY KEY,
                       url TEXT NOT NULL,
                       status INTEGER NOT NULL,
                       headers_json TEXT NOT NULL,
                       body BLOB NOT NULL,
                       fetched_at REAL NOT NULL
                   )"""
            )

    def get(self, url: str) -> Optional[CachedResponse]:
        with sqlite3.connect(self.path) as conn:
            row = conn.execute("SELECT url, status, headers_json, body, fetched_at FROM cache WHERE key=?",
                               (_key(url),)).fetchone()
            if row is None:
                return None
            cr = CachedResponse(url=row[0], status=row[1], headers=json.loads(row[2]),
                                body=row[3], fetched_at=row[4])
            if (time.time() - cr.fetched_at) > self.ttl_seconds:
                return None
            return cr

    def put(self, url: str, response: CachedResponse) -> None:
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO cache(key, url, status, headers_json, body, fetched_at) VALUES (?,?,?,?,?,?)",
                (_key(url), response.url, response.status, json.dumps(response.headers),
                 response.body, response.fetched_at),
            )

    def delete(self, url: str) -> None:
        with sqlite3.connect(self.path) as conn:
            conn.execute("DELETE FROM cache WHERE key=?", (_key(url),))
