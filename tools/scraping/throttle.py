"""Per-host rate limiter.

Per Lawson + Brody discipline: every scrape respects a per-domain delay
keyed by `urlparse(url).netloc`. Default 1s/host with jitter.
"""
from __future__ import annotations

import random
import threading
import time
from typing import Optional
from urllib.parse import urlparse


class Throttle:
    """Per-host rate limiter.

    Usage:
        t = Throttle(delay=1.0, jitter=0.3)
        t.wait("https://example.com/page1")  # may sleep
    """

    def __init__(self, delay: float = 1.0, jitter: float = 0.3) -> None:
        self.delay = delay
        self.jitter = jitter
        self._last: dict[str, float] = {}
        self._lock = threading.Lock()

    def wait(self, url: str) -> None:
        host = urlparse(url).netloc
        with self._lock:
            last = self._last.get(host)
            now = time.monotonic()
            if last is not None:
                elapsed = now - last
                wait_for = max(0.0, self.delay + random.uniform(0, self.jitter) - elapsed)
                if wait_for > 0:
                    time.sleep(wait_for)
            self._last[host] = time.monotonic()


class AdaptiveThrottle(Throttle):
    """Adapts delay per-host based on observed response time.
    Slow servers get more delay; fast servers less."""

    def __init__(self, base_delay: float = 1.0, min_delay: float = 0.2, max_delay: float = 30.0, target_latency: float = 0.5) -> None:
        super().__init__(delay=base_delay, jitter=base_delay * 0.2)
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.target_latency = target_latency
        self._per_host_delay: dict[str, float] = {}

    def observe(self, url: str, response_seconds: float) -> None:
        host = urlparse(url).netloc
        with self._lock:
            current = self._per_host_delay.get(host, self.delay)
            if response_seconds > self.target_latency * 2:
                new = min(current * 1.5, self.max_delay)
            elif response_seconds < self.target_latency:
                new = max(current * 0.9, self.min_delay)
            else:
                new = current
            self._per_host_delay[host] = new

    def wait(self, url: str) -> None:
        host = urlparse(url).netloc
        with self._lock:
            self.delay = self._per_host_delay.get(host, self.delay)
        super().wait(url)
