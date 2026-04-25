"""HTTP client wrapper — synchronous + async — with retry, throttling, classified errors.

Decision tree (per `skills/web-scraping-foundations/SKILL.md`):
- Use `fetch` for low-volume sync work or scripts.
- Use `fetch_async` for >50 concurrent requests.
- Both respect robots.txt by default; override with `respect_robots=False` per call.
- Both attach identification headers by default; override with `user_agent=...`.

Errors are classified to support skill-level decision rules (don't silent-retry
4xx; surface CAPTCHAs as SoftBlock not as success).
"""
from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Optional

DEFAULT_USER_AGENT = (
    "digital-research-engine/0.1 "
    "(+https://github.com/peterbamuhigire/digital-research-skills)"
)
DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 3


class ScrapeError(Exception):
    """Base scrape error."""


class RobotsBlocked(ScrapeError):
    """robots.txt disallows this URL for the configured user agent."""


class RateLimited(ScrapeError):
    """Server returned 429 or equivalent. Caller should back off."""


class SoftBlock(ScrapeError):
    """200 OK with a body that is a CAPTCHA / interstitial / block page.
    Detected by content heuristics, not status code."""


@dataclass(slots=True)
class FetchResult:
    """Return shape for fetch() / fetch_async()."""

    url: str
    status: int
    headers: dict[str, str]
    text: str
    content: bytes
    final_url: str               # after redirects
    elapsed_seconds: float


def fetch(
    url: str,
    *,
    method: str = "GET",
    headers: Optional[dict[str, str]] = None,
    params: Optional[dict[str, Any]] = None,
    data: Optional[Any] = None,
    json: Optional[Any] = None,
    timeout: float = DEFAULT_TIMEOUT,
    max_retries: int = DEFAULT_MAX_RETRIES,
    user_agent: str = DEFAULT_USER_AGENT,
    respect_robots: bool = True,
    impersonate: Optional[str] = None,
    proxy: Optional[str] = None,
    throttle: Optional["Throttle"] = None,
) -> FetchResult:
    """Synchronous fetch.

    impersonate: if set (e.g. "chrome120"), routes via curl-cffi to match
        Chrome's TLS/JA3 fingerprint. Defeats fingerprint-based blocks that
        reject standard `requests`.
    proxy: e.g. "http://user:pass@host:port".
    throttle: optional per-host rate limiter.
    """
    from .robots import is_robots_allowed
    from .retry import retry_request

    if respect_robots and not is_robots_allowed(url, user_agent):
        raise RobotsBlocked(f"robots.txt disallows {url} for {user_agent!r}")

    if throttle is not None:
        throttle.wait(url)

    if impersonate is not None:
        # Lazy-import only when needed.
        from curl_cffi import requests as cffi_requests  # type: ignore

        def _do() -> FetchResult:
            r = cffi_requests.request(
                method, url, headers={**(headers or {}), "User-Agent": user_agent},
                params=params, data=data, json=json, timeout=timeout,
                impersonate=impersonate, proxies={"https": proxy, "http": proxy} if proxy else None,
            )
            return _classify(url, r.status_code, dict(r.headers), r.text, r.content, str(r.url), 0.0)
    else:
        import requests

        sess = requests.Session()
        sess.headers["User-Agent"] = user_agent

        def _do() -> FetchResult:
            t0 = time.monotonic()
            r = sess.request(
                method, url, headers=headers, params=params, data=data, json=json,
                timeout=timeout, proxies={"https": proxy, "http": proxy} if proxy else None,
            )
            return _classify(url, r.status_code, dict(r.headers), r.text, r.content, r.url, time.monotonic() - t0)

    return retry_request(_do, retries=max_retries)


async def fetch_async(
    url: str,
    *,
    method: str = "GET",
    headers: Optional[dict[str, str]] = None,
    params: Optional[dict[str, Any]] = None,
    data: Optional[Any] = None,
    json: Optional[Any] = None,
    timeout: float = DEFAULT_TIMEOUT,
    max_retries: int = DEFAULT_MAX_RETRIES,
    user_agent: str = DEFAULT_USER_AGENT,
    respect_robots: bool = True,
    proxy: Optional[str] = None,
    client: Optional[Any] = None,
) -> FetchResult:
    """Async fetch via httpx. Pass an existing `httpx.AsyncClient` to share connection pool."""
    from .robots import is_robots_allowed

    if respect_robots and not is_robots_allowed(url, user_agent):
        raise RobotsBlocked(f"robots.txt disallows {url} for {user_agent!r}")

    import httpx

    own_client = client is None
    if own_client:
        client = httpx.AsyncClient(
            timeout=timeout,
            headers={"User-Agent": user_agent},
            proxies=proxy,
            follow_redirects=True,
        )

    try:
        last_err: Optional[BaseException] = None
        for attempt in range(max_retries + 1):
            t0 = time.monotonic()
            try:
                r = await client.request(method, url, headers=headers, params=params, data=data, json=json)
                return _classify(url, r.status_code, dict(r.headers), r.text, r.content, str(r.url), time.monotonic() - t0)
            except (httpx.TimeoutException, httpx.ConnectError) as e:
                last_err = e
                # Exponential backoff between attempts
                await _async_sleep(2 ** attempt)
        assert last_err is not None
        raise ScrapeError(f"async fetch failed after {max_retries + 1} attempts: {last_err}")
    finally:
        if own_client:
            await client.aclose()


async def _async_sleep(seconds: float) -> None:
    import asyncio
    await asyncio.sleep(seconds)


_SOFT_BLOCK_HINTS = (
    "captcha", "are you a robot", "verify you are human",
    "cloudflare", "access denied", "bot detection",
)


def _classify(url: str, status: int, hdrs: dict[str, str], text: str, content: bytes, final_url: str, elapsed: float) -> FetchResult:
    """Classify the response — raise SoftBlock / RateLimited if the body / status look adversarial."""
    if status == 429:
        raise RateLimited(f"429 from {url}")
    if status in (401, 403):
        # Don't retry — caller decides escalation.
        raise ScrapeError(f"{status} from {url}: authentication or block")
    if status >= 500:
        raise ScrapeError(f"{status} from {url}: server error (retryable)")

    if status == 200 and len(content) < 50_000:
        body_lower = text.lower()
        if any(hint in body_lower for hint in _SOFT_BLOCK_HINTS):
            raise SoftBlock(f"200 OK from {url} but body looks like a block / CAPTCHA page")

    return FetchResult(url=url, status=status, headers=hdrs, text=text, content=content,
                       final_url=final_url, elapsed_seconds=elapsed)
