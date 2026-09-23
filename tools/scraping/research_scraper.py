"""Bounded, provenance-first web collection for research workflows.

This module intentionally stays below a crawler framework. It provides the
smallest useful research collector: robots-aware fetching, raw-response
caching, same-host link discovery, structured-data-first extraction, durable
JSONL output, and a machine-readable run manifest. It never follows links
outside the operator-provided host scope and never bypasses blocks.
"""
from __future__ import annotations

import json
import time
from collections import deque
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Optional
from urllib.parse import urlparse

from .cache import CachedResponse, DiskCache
from .cleaning import canonicalize_url, clean_text
from .extractors.jsonld import extract_jsonld
from .extractors.opengraph import extract_opengraph
from .extractors.soup import extract_links, parse_html
from .http_client import FetchResult, fetch
from .throttle import AdaptiveThrottle


@dataclass(slots=True)
class ScrapeRecord:
    """One page result, including enough provenance for later verification."""

    url: str
    referrer: Optional[str]
    final_url: str
    fetched_at: str
    status: int
    source_host: str
    content_sha256: str
    title: Optional[str]
    text: str
    jsonld: list[dict[str, Any]]
    opengraph: dict[str, str]
    links: list[str]
    from_cache: bool = False
    elapsed_seconds: Optional[float] = None
    error: Optional[str] = None


@dataclass(slots=True)
class ScrapeRun:
    """Run-level evidence and operational outcomes."""

    started_at: str
    finished_at: Optional[str] = None
    requested_urls: list[str] = field(default_factory=list)
    pages_seen: int = 0
    pages_succeeded: int = 0
    pages_failed: int = 0
    errors: list[dict[str, str]] = field(default_factory=list)
    selector_version: str = "research-scraper-v1"
    robots_respected: bool = True
    same_host_only: bool = True


FetchCallable = Callable[..., FetchResult]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha256(body: bytes) -> str:
    import hashlib

    return hashlib.sha256(body).hexdigest()


def _title_and_text(html: str) -> tuple[Optional[str], str]:
    soup = parse_html(html)
    title = clean_text(soup.title.get_text(" ", strip=True)) if soup.title else None
    for node in soup.select("script, style, noscript, template, svg"):
        node.decompose()
    text = clean_text(soup.get_text(" ", strip=True))
    return title or None, text


class ResearchScraper:
    """Collect a bounded set of public pages for research.

    ``fetch_fn`` is injectable so parser and crawl behavior can be tested
    offline. The default uses the engine's robots-aware HTTP client.
    """

    def __init__(
        self,
        output_dir: str | Path,
        *,
        user_agent: str,
        delay: float = 1.0,
        max_pages: int = 25,
        same_host_only: bool = True,
        respect_robots: bool = True,
        cache_ttl_seconds: int = 30 * 24 * 3600,
        fetch_fn: FetchCallable = fetch,
    ) -> None:
        if max_pages < 1:
            raise ValueError("max_pages must be positive")
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.cache = DiskCache(self.output_dir / "raw-cache", ttl_seconds=cache_ttl_seconds)
        self.user_agent = user_agent
        self.max_pages = max_pages
        self.same_host_only = same_host_only
        self.respect_robots = respect_robots
        self.fetch_fn = fetch_fn
        self.throttle = AdaptiveThrottle(base_delay=max(0.0, delay))

    def run(self, urls: Iterable[str]) -> ScrapeRun:
        seeds = [canonicalize_url(u) for u in urls if urlparse(u).scheme in {"http", "https"}]
        run = ScrapeRun(started_at=_now(), requested_urls=seeds, robots_respected=self.respect_robots,
                        same_host_only=self.same_host_only)
        queue: deque[tuple[str, Optional[str]]] = deque((u, None) for u in seeds)
        visited: set[str] = set()
        hosts = {urlparse(u).netloc for u in seeds}
        records_path = self.output_dir / "records.jsonl"

        with records_path.open("w", encoding="utf-8") as records:
            while queue and run.pages_seen < self.max_pages:
                url, referrer = queue.popleft()
                url = canonicalize_url(url)
                if url in visited:
                    continue
                if self.same_host_only and urlparse(url).netloc not in hosts:
                    continue
                visited.add(url)
                run.pages_seen += 1
                try:
                    record = self._scrape_one(url, referrer)
                    records.write(json.dumps(asdict(record), ensure_ascii=False, sort_keys=True) + "\n")
                    records.flush()
                    run.pages_succeeded += 1
                    for link in record.links:
                        if link not in visited:
                            queue.append((link, url))
                except Exception as exc:  # isolate one bad page from the run
                    run.pages_failed += 1
                    run.errors.append({"url": url, "error_type": type(exc).__name__, "message": str(exc)})

        run.finished_at = _now()
        (self.output_dir / "manifest.json").write_text(
            json.dumps(asdict(run), indent=2, ensure_ascii=False, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return run

    def _scrape_one(self, url: str, referrer: Optional[str]) -> ScrapeRecord:
        cached = self.cache.get(url)
        from_cache = cached is not None
        if cached is not None:
            body = cached.body
            result = FetchResult(url=url, status=cached.status, headers=cached.headers,
                                 text=body.decode("utf-8", errors="replace"), content=body,
                                 final_url=url, elapsed_seconds=0.0)
        else:
            started = time.monotonic()
            result = self.fetch_fn(url, user_agent=self.user_agent,
                                   respect_robots=self.respect_robots, throttle=self.throttle)
            self.throttle.observe(url, result.elapsed_seconds or (time.monotonic() - started))
            self.cache.put(url, CachedResponse(url=result.final_url, status=result.status,
                                               headers=result.headers, body=result.content,
                                               fetched_at=time.time()))
        title, text = _title_and_text(result.text)
        jsonld = extract_jsonld(result.text)
        opengraph = extract_opengraph(result.text)
        links = sorted({canonicalize_url(link, base=result.final_url)
                        for link in extract_links(parse_html(result.text), result.final_url)
                        if urlparse(link).scheme in {"http", "https"}})
        return ScrapeRecord(url=url, referrer=referrer, final_url=result.final_url, fetched_at=_now(), status=result.status,
                            source_host=urlparse(result.final_url).netloc, content_sha256=_sha256(result.content),
                            title=title, text=text, jsonld=jsonld, opengraph=opengraph, links=links,
                            from_cache=from_cache, elapsed_seconds=result.elapsed_seconds,
                            error=None)


def scrape_urls(urls: Iterable[str], output_dir: str | Path, **kwargs: Any) -> ScrapeRun:
    """Convenience entry point for notebooks and small research scripts."""
    return ResearchScraper(output_dir, **kwargs).run(urls)


__all__ = ["ResearchScraper", "ScrapeRecord", "ScrapeRun", "scrape_urls"]
