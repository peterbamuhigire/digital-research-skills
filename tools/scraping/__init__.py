"""Core scraping infrastructure.

Public API:
    fetch                      — synchronous HTTP fetch with retries + throttling
    fetch_async                — async equivalent via httpx
    parse_html                 — BeautifulSoup wrapper with parser auto-selection
    select / select_all        — CSS selector helpers with safe defaults
    is_robots_allowed          — robots.txt check
    Throttle                   — per-host rate limiter
    DiskCache / SQLiteCache    — raw-HTML caches
    paginate_offset / paginate_cursor / paginate_xhr — pagination iterators
    PlaywrightFetcher          — headless renderer (lazy-imported)

All optional heavy deps (playwright, curl-cffi, scrapy) are lazy-imported
inside the functions that use them, so `import tools.scraping` is cheap.
"""
from __future__ import annotations

# Light-weight re-exports
from .http_client import fetch, fetch_async, ScrapeError, RobotsBlocked, RateLimited, SoftBlock
from .throttle import Throttle, AdaptiveThrottle
from .retry import retry_request
from .robots import is_robots_allowed, crawl_delay, sitemaps_for
from .cache import DiskCache, SQLiteCache
from .pagination import paginate_offset, paginate_cursor, paginate_xhr
from .extractors.soup import parse_html, select, select_all, extract_text, extract_links
from .extractors.jsonld import extract_jsonld
from .extractors.opengraph import extract_opengraph
from .cleaning import clean_text, parse_money, canonicalize_url

__all__ = [
    "fetch", "fetch_async",
    "ScrapeError", "RobotsBlocked", "RateLimited", "SoftBlock",
    "Throttle", "AdaptiveThrottle",
    "retry_request",
    "is_robots_allowed", "crawl_delay", "sitemaps_for",
    "DiskCache", "SQLiteCache",
    "paginate_offset", "paginate_cursor", "paginate_xhr",
    "parse_html", "select", "select_all", "extract_text", "extract_links",
    "extract_jsonld", "extract_opengraph",
    "clean_text", "parse_money", "canonicalize_url",
]
