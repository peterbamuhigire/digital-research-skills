"""Pagination iterators.

Four canonical patterns per Lawson + Brody + Oxylabs synthesis:
  1. paginate_offset    — ?page=N or ?offset=N
  2. paginate_cursor    — server returns next-cursor in body
  3. paginate_xhr       — hidden JSON API endpoint
  4. (next-link)        — caller follows rel=next; not a generator pattern
"""
from __future__ import annotations

from typing import Any, AsyncIterator, Callable, Iterator, Optional
from urllib.parse import urlencode, urlparse, parse_qs, urlunparse


def paginate_offset(
    base_url: str,
    *,
    page_param: str = "page",
    start: int = 1,
    step: int = 1,
    max_pages: int = 1000,
) -> Iterator[str]:
    """Yield URL with incrementing page param.

    Caller is responsible for stopping (empty result, 404, terminator).
    """
    p = urlparse(base_url)
    q = parse_qs(p.query, keep_blank_values=True)
    page = start
    for _ in range(max_pages):
        q[page_param] = [str(page)]
        new_q = urlencode({k: v[-1] for k, v in q.items()})
        yield urlunparse(p._replace(query=new_q))
        page += step


def paginate_cursor(
    initial_url: str,
    *,
    fetch: Callable[[str], dict[str, Any]],
    next_path: str = "next",
    max_pages: int = 1000,
) -> Iterator[dict[str, Any]]:
    """Generic cursor-based pagination.

    fetch(url) -> JSON dict. We extract dict[next_path] for the next URL.
    """
    url: Optional[str] = initial_url
    seen = 0
    while url and seen < max_pages:
        body = fetch(url)
        yield body
        url = body.get(next_path) if isinstance(body, dict) else None
        seen += 1


async def paginate_xhr(
    template_url: str,
    *,
    fetch_async: Callable[[str], Any],
    page_param: str = "page",
    start: int = 1,
    terminator: Optional[Callable[[Any], bool]] = None,
    max_pages: int = 1000,
) -> AsyncIterator[Any]:
    """Async generator over an XHR API.

    template_url should NOT contain the page param yet — we add it.
    terminator(response) returns True when no more pages.
    Default terminator: empty response.
    """
    p = urlparse(template_url)
    q = parse_qs(p.query, keep_blank_values=True)
    page = start
    for _ in range(max_pages):
        q[page_param] = [str(page)]
        new_q = urlencode({k: v[-1] for k, v in q.items()})
        url = urlunparse(p._replace(query=new_q))
        body = await fetch_async(url)
        yield body
        if terminator is not None and terminator(body):
            return
        # Default terminator: empty list / dict
        if isinstance(body, (list, dict)) and not body:
            return
        page += 1
