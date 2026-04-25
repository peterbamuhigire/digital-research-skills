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
        except _RetryableError as e:  # type: ignore[name-defined]
            last_err = e
            if attempt < retries:
                delay = min(backoff_base ** attempt, max_backoff)
                time.sleep(delay)
            else:
                break
    assert last_err is not None
    raise last_err


# Local alias so we can extend without circular import. The http_client module
# raises ScrapeError for retryable 5xx; this is intentionally narrower than
# generic Exception — silent broad retry is the anti-pattern Lawson warns against.
class _RetryableError(Exception):
    pass


# At import time, register http_client's retryable errors. Lazy because they
# import this module too.
try:
    from .http_client import ScrapeError, RateLimited
    _RetryableError.register(ScrapeError)  # type: ignore[arg-type]
    _RetryableError.register(RateLimited)  # type: ignore[arg-type]
except ImportError:
    pass
