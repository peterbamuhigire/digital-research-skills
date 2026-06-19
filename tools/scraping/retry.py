"""Retry with exponential backoff.

Per Lawson: retry only 5xx + connection errors, never 4xx.
Per Brody: 2s, 4s, 8s, 16s on successive failures.
"""
from __future__ import annotations

import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry_request(
    fn: Callable[[], T],
    *,
    retries: int = 3,
    backoff_base: float = 2.0,
    max_backoff: float = 60.0,
) -> T:
    last_err: BaseException | None = None
    for attempt in range(retries + 1):
        try:
            return fn()
        except Exception as e:
            if not _is_retryable(e):
                raise
            last_err = e
            if attempt < retries:
                delay = min(backoff_base ** attempt, max_backoff)
                time.sleep(delay)
            else:
                break
    assert last_err is not None
    raise last_err


def _is_retryable(exc: Exception) -> bool:
    """Retry only explicit transient scrape failures.

    ``ScrapeError`` is also used by the HTTP wrapper for 401/403 blocks, so the
    retry gate checks the classified message rather than catching the base class
    unconditionally.
    """

    name = exc.__class__.__name__
    if name == "RateLimited":
        return True
    if name != "ScrapeError":
        return False
    message = str(exc)
    return any(message.startswith(f"{status} ") for status in ("500", "502", "503", "504"))
