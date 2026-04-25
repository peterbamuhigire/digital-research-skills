# `tools/` — runtime utilities for the engine

Real Python code (not just skill documentation). The skills tell agents *what* to do; these tools are *how* they do it.

## Layout

```
tools/
├── scraping/         core scraping infrastructure (Layer 0)
│   ├── http_client.py        requests / httpx / curl-cffi wrapper with retries + throttling
│   ├── throttle.py           per-host rate limiting
│   ├── robots.py             robots.txt + sitemap parsing
│   ├── retry.py              exponential-backoff retry decorator
│   ├── cache.py              raw-HTML cache (disk / S3 / SQLite)
│   ├── pagination.py         offset / cursor / XHR pagination iterators
│   ├── auth.py               session + CSRF + browser-cookie import
│   ├── headless.py           Playwright fetcher with XHR capture
│   ├── storage.py            CSV / SQLite / Postgres / S3 sinks
│   ├── cleaning.py           text / money / URL canonicalisation
│   ├── dedup.py              URL + content-hash dedup
│   ├── ethics.py              robots-allow + identification headers
│   ├── monitoring.py         success-rate per source, block-rate signal
│   └── extractors/
│       ├── soup.py           BeautifulSoup safe extraction helpers
│       ├── jsonld.py         Schema.org JSON-LD extraction
│       ├── opengraph.py      OG / Twitter Card meta extraction
│       └── feeds.py          RSS / Atom / sitemap parsing
│
├── google/           Google power-search utilities (Brown)
│   ├── search_api.py         Custom Search JSON + SerpAPI fan-out
│   ├── stakeholder.py        Stakeholder-first SERP recon
│   └── tld_atlas.py          TLD / state-domain / county-domain matrix
│
└── verification/     Investigative verification utilities (Silverman)
    ├── exif.py               EXIF + GPS extraction; metadata-stripped detector
    ├── reverse_image.py      TinEye + Google Images + Yandex + Bing fan-out
    ├── shadow_time.py        Solar-position-from-shadow time inference
    ├── provenance.py         Earliest-known-timestamp tracer
    ├── whois_cluster.py      Whois cluster + shared-infrastructure detector
    └── archive.py            Wayback / archive.today resurrector
```

## Dependency baseline

Optional dependencies are imported *inside functions*, not at module top, so importing `tools.scraping` doesn't require Playwright unless you call a Playwright function.

Suggested `requirements.txt`:

```
# core
httpx>=0.27
requests>=2.31
beautifulsoup4>=4.12
lxml>=5.0
selectolax>=0.3
tenacity>=8.2
python-dateutil>=2.8
charset-normalizer>=3.3
ftfy>=6.1

# headless / async (optional)
playwright>=1.45
curl-cffi>=0.7
aiohttp>=3.9

# crawler (optional)
scrapy>=2.11
scrapy-playwright>=0.0.34

# extraction
extruct>=0.16
feedparser>=6.0

# storage
pyarrow>=15.0
pydantic>=2.6
boto3>=1.34
psycopg[binary]>=3.1

# google
google-api-python-client>=2.120

# verification
exifread>=3.0
piexif>=1.1
ephem>=4.1            # solar position
python-whois>=0.9
waybackpy>=3.0
```

## Engineering principles

1. **Lazy imports.** Heavy deps (Playwright, Scrapy, Selenium) imported inside functions.
2. **Type hints everywhere.** PEP 695 syntax preferred (`def f(x: str) -> str:`).
3. **Async by default for I/O.** `httpx.AsyncClient`, `asyncio.gather`, `aiolimiter`.
4. **Fail loudly with classified errors.** `ScrapeError`, `RobotsBlocked`, `RateLimited`, `SoftBlock` (CAPTCHA/200-with-block-page).
5. **No silent retries on 4xx** — only 5xx and connection errors.
6. **Identification header by default** — `User-Agent: digital-research-engine/0.1 (+https://github.com/peterbamuhigire/digital-research-skills)` unless explicitly overridden.
7. **Robots.txt respected by default** — must explicitly opt out per call.
8. **Tests are first-class.** Each module ships with a `__tests__/test_<module>.py`.

## Anti-patterns

- `time.sleep()` as a wait strategy — use `WebDriverWait` / Playwright `wait_for_*`
- `verify=False` as a habit — only for self-signed dev hosts
- Hard-coded selectors with no graceful fallback
- Silent retries on 403/429
- Bypassing CAPTCHA on third-party sites
- Storing personal data without lawful basis (GDPR / Uganda DPPA)

See `skills/web-scraping-foundations/SKILL.md`, `skills/scraping-politeness-and-ratelimiting/SKILL.md`, and `skills/scraping-legal-and-ethical-bounds/SKILL.md` for full discipline.
