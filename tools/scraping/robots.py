"""robots.txt compliance helpers.

Default behaviour throughout the engine: respect robots.txt unless the
operator explicitly opts out per call. Lawson, Brody, and Bell all converge
on this as the lawful + ethical default.
"""
from __future__ import annotations

import urllib.robotparser
from functools import lru_cache
from typing import Optional
from urllib.parse import urljoin, urlparse


@lru_cache(maxsize=512)
def _parser_for(host_base: str) -> urllib.robotparser.RobotFileParser:
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(host_base, "/robots.txt"))
    try:
        rp.read()
    except Exception:
        # If robots.txt is unreachable, treat as permissive but log
        pass
    return rp


def _host_base(url: str) -> str:
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}"


def is_robots_allowed(url: str, user_agent: str = "*") -> bool:
    rp = _parser_for(_host_base(url))
    try:
        return rp.can_fetch(user_agent, url)
    except Exception:
        return True  # Permissive default if parser raises


def crawl_delay(url: str, user_agent: str = "*") -> Optional[float]:
    rp = _parser_for(_host_base(url))
    try:
        d = rp.crawl_delay(user_agent)
        return float(d) if d is not None else None
    except Exception:
        return None


def sitemaps_for(host_or_url: str) -> list[str]:
    """Return Sitemap: URLs declared in robots.txt for the given host."""
    rp = _parser_for(_host_base(host_or_url))
    try:
        sm = rp.site_maps()
        return list(sm) if sm else []
    except Exception:
        return []
