---
name: scraping-politeness-and-ratelimiting
description: Use on every scrape — robots.txt parsing, per-host throttling, exponential backoff, identification headers, off-hours scheduling. The discipline layer that keeps scrapers ethical AND lawful AND unblocked. Backed by tools/scraping/.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Scraping politeness and rate limiting

A polite scraper is rarely blocked. Rude scrapers get rate-limited, IP-banned, or sued. Lawson, Brody, Oxylabs, and Hands-On all converge on the same discipline.

## Default rules (always on unless explicit override)

1. **Respect robots.txt.** `tools.scraping.is_robots_allowed(url)` runs before every fetch.
2. **Throttle per host.** Default 1 second/host with 0.3s jitter (`tools.scraping.Throttle`).
3. **Exponential backoff on 5xx + connection errors.** 2s, 4s, 8s, 16s. Cap retries at 3.
4. **Never retry 4xx.** Surface — don't bury.
5. **Identify yourself.** User-Agent: `digital-research-engine/0.1 (+https://github.com/peterbamuhigire/digital-research-skills)` by default.
6. **Honor Crawl-delay** if specified in robots.txt.

## When to be MORE polite (slow down)

- Small / regional / community sites — they may not have CDN
- Government sites — rate-limit thresholds often low and quietly enforced
- Sites with explicit Crawl-delay
- After a 429 response — back off and stay slow
- During business hours in target's timezone — Brody recommends 2am local

## When stealth is justified vs not

| Justified | Not justified |
|---|---|
| TLS fingerprint blocks legitimate research traffic | Bypassing explicit "no bots" signal |
| Custom UA blocked because of generic Python | Solving CAPTCHA on a site that uses CAPTCHA as anti-scraping |
| You have a legitimate account and 2FA breaks `requests` | Rotating residential proxies to defeat per-IP rate limits the operator chose |

## The robots.txt protocol

robots.txt is **a request, not a technical control**. Disregarding it isn't illegal in itself, but is the strongest evidence of bad faith in litigation. Honour by default; override only with explicit operator authorisation and a defensible reason.

```python
from tools.scraping.robots import is_robots_allowed, crawl_delay, sitemaps_for

if not is_robots_allowed(url, "MyBot"):
    raise RobotsBlocked(url)

delay = crawl_delay(url, "MyBot")
if delay:
    throttle = Throttle(delay=delay)

# Sitemap URLs from robots.txt — efficient enumeration
for sm in sitemaps_for("https://example.com"):
    ...
```

## Rate-limit math

Reasonable defaults:
- **Single-process scrape:** ≤ 1 req/sec/host
- **Distributed crawl:** Sum across all workers ≤ 1 req/sec/host
- **Polite limit:** 1 req every 5 sec/host for small sites
- **Aggressive (with permission):** 5 req/sec/host max
- **Unbounded (with explicit API contract):** as documented

Use `AdaptiveThrottle` to back off when servers slow down — Throttle that observes response time and dilates accordingly.

## Identification

Every scrape carries:

```
User-Agent: <bot-name>/<version> (+<contact-url-or-email>)
```

Per Brody: the contact URL is your shield. When a sysadmin sees your scrapes and wants to reach out, they should be able to — and may grant you a higher rate-limit instead of blocking.

## Off-hours scheduling

Brody recommends running scrapes at **2am local time in the target's timezone**. Reduces collision with real users and gets you under the radar of basic per-second rate limiters.

## Anti-patterns

- Hammering with no delay
- `verify=False` to defeat self-signed-cert blocks (only acceptable in dev)
- Disregarding robots.txt while the site is actively blocking your IP
- User-Agent spoofing + proxy rotation + CAPTCHA solving in combination — the rude trinity
- Treating a 429 as a transient error rather than a "stop"
- No backoff after 5xx — same frequency as before the error

## Block-detection signals (treat as "stop")

- HTTP 429
- HTTP 403 with body containing "Cloudflare" / "blocked" / "are you a robot"
- HTTP 503 with body containing CAPTCHA challenge
- HTTP 200 with body containing CAPTCHA / interstitial → `SoftBlock` (the engine's classifier flags this)
- Sudden response-time 10× normal
- Response body unexpectedly tiny (<5 KB when normally >50 KB)

When any of these fires: **STOP**. Don't retry harder. Reduce footprint, contact the site if appropriate, or escalate to the operator.

## See also

- `tools/scraping/robots.py`, `throttle.py`, `retry.py`, `http_client.py` — implementation
- `web-scraping-foundations` — decision tree
- `scraping-legal-and-ethical-bounds` (roadmap) — when to refuse a scrape
- `evidence-discipline` — overrides apply
