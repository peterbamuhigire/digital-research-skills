---
name: scraping-engineering-python
description: Use when scaling a Python scraper beyond a single-file requests script — encodes Lawson's *Web Scraping with Python* engineering layer (caching to disk and MongoDB, concurrent downloading, dynamic content via WebKit/Selenium/Playwright, form interaction, CAPTCHA strategies, Scrapy framework selection).
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Scraping Engineering — Python (Lawson)

Encodes Richard Lawson's *Web Scraping with Python* (Packt) as the engine's engineering layer for production-grade Python scrapers. Pair with `scraping-troubleshooting-brody` (etiquette and debugging) and `web-scraping-foundations` (basics). For non-Python pipelines, the patterns transfer; the libraries change.

## 1. When to scale up

A single-file `requests` script is fine for one-off scrapes. Move to the patterns in this skill when any of the following holds:

- Crawl size > 1,000 URLs.
- The crawl will run more than once (you'll re-download wastefully).
- The site uses JavaScript to render content.
- The site requires multi-step form interaction or CAPTCHA solving.
- You need >5 concurrent in-flight requests.
- You need resumability after failure.

## 2. Caching downloads (Chapter 3)

**Why:** development iterations should re-parse cached responses, not re-fetch them. Caching also enables resumable crawls.

### 2a. Disk cache

URL → safe filename mapping. Critical filesystem rules:

| OS | FS | Invalid chars | Max filename |
|---|---|---|---|
| Linux | Ext3/4 | `/`, `\0` | 255 bytes |
| macOS | HFS+/APFS | `:`, `\0` | 255 UTF-16 units |
| Windows | NTFS | `\ / ? : * " > < |` | 255 chars |

```python
import re, os, gzip, pickle
from urllib.parse import urlsplit

class DiskCache:
    def __init__(self, cache_dir="cache"):
        self.cache_dir = cache_dir

    def url_to_path(self, url):
        components = urlsplit(url)
        path = components.path
        if not path or path.endswith("/"):
            path += "index.html"
        filename = components.netloc + path + components.query
        filename = re.sub(r'[^/0-9a-zA-Z\-.,;_ ]', '_', filename)
        # cap each segment at 255 chars
        filename = '/'.join(seg[:255] for seg in filename.split('/'))
        return os.path.join(self.cache_dir, filename)

    def __getitem__(self, url):
        path = self.url_to_path(url)
        if os.path.exists(path):
            with gzip.open(path, "rb") as f:
                return pickle.load(f)
        raise KeyError(url)

    def __setitem__(self, url, result):
        path = self.url_to_path(url)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with gzip.open(path, "wb") as f:
            pickle.dump(result, f)
```

### 2b. MongoDB cache

When the disk-cache file count is the bottleneck (>1 M URLs), or you need cross-machine sharing, switch to MongoDB with the URL as `_id` and `upsert=True`:

```python
from pymongo import MongoClient
from datetime import datetime, timedelta

class MongoCache:
    def __init__(self, client=None, expires=timedelta(days=30)):
        self.client = client or MongoClient("localhost", 27017)
        self.db = self.client.cache
        self.expires = expires

    def __getitem__(self, url):
        rec = self.db.webpage.find_one({"_id": url})
        if rec is None:
            raise KeyError(url)
        if datetime.utcnow() - rec["timestamp"] > self.expires:
            raise KeyError(f"{url} expired")
        return rec["result"]

    def __setitem__(self, url, result):
        record = {"result": result, "timestamp": datetime.utcnow()}
        self.db.webpage.update_one({"_id": url}, {"$set": record}, upsert=True)
```

**Rules:** every cache entry stores a timestamp; every read enforces TTL; expired entries trigger re-fetch (do not silently serve stale).

## 3. Concurrent downloading (Chapter 4)

**Three concurrency models, ranked by typical fit for scraping:**

1. **Threading (`concurrent.futures.ThreadPoolExecutor`)** — best for I/O-bound HTTP; simple; default choice.
2. **Asyncio (`httpx.AsyncClient`, `aiohttp`)** — highest throughput; steeper learning curve; required for >100 in-flight.
3. **Multiprocessing** — only when CPU-bound parsing is the bottleneck; adds IPC complexity.

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch(session, url):
    return url, session.get(url, headers=HEADERS, timeout=30)

with ThreadPoolExecutor(max_workers=10) as ex:
    futures = [ex.submit(fetch, session, u) for u in urls]
    for f in as_completed(futures):
        url, response = f.result()
        # process
```

**Concurrency budget per host (Brody's etiquette still applies):**

| Site posture | Workers per host |
|---|---|
| Public API or sitemap-blessed | 5–10 |
| Standard public site | 2–3 |
| Restrictive `Crawl-delay` | 1 (sequential) |
| You have written permission | per agreement |

Concurrency-per-host ≠ concurrency total. A pool of 50 hitting one host is rude; 50 hitting 50 distinct hosts is fine.

## 4. Dynamic content (Chapter 5)

The page renders correctly in a browser but the HTML you fetch is empty. Options, ranked by efficiency:

1. **Reverse-engineer the JSON XHR endpoint.** Open dev tools → Network → XHR. Almost every dynamic page calls a JSON API; hitting it directly is 10–100× faster and more stable than headless rendering.
2. **Inspect inline JSON.** Some pages embed the data as a JSON blob in a `<script>` tag (`__NEXT_DATA__`, `window.__INITIAL_STATE__`). Extract it via regex or BeautifulSoup, parse it.
3. **Headless browser** — last resort. Choices:

| Tool | Strengths | Weaknesses |
|---|---|---|
| **Playwright** | Modern, fast, async, multi-browser, built-in network interception | Requires browser binaries |
| **Selenium** | Mature, language coverage | Slower; flakier; older API |
| **PyQt WebKit** (Lawson's choice) | Embedded in Python | Old; less maintained |
| **Splash** | HTTP API to Lua-driven browser | Extra service to run |

**Playwright minimal example:**

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(user_agent=REAL_UA)
    page.goto(url, wait_until="networkidle")
    page.wait_for_selector("#result")
    html = page.content()
    browser.close()
```

**Cost rule:** a headless browser uses 100–500 MB and 1–3 s per page. Reserve for the pages that genuinely need it; never headless-render an entire crawl by reflex.

## 5. Form interaction (Chapter 6)

**Three form-handling levels:**

| Approach | When |
|---|---|
| Build the request manually | Static form, all fields in HTML, no JS validation |
| `mechanicalsoup` / `requests` + `BeautifulSoup` | Form has hidden CSRF fields and standard HTML inputs |
| Browser automation (Playwright) | Form requires JS-driven clicks, AJAX submission, dynamic field reveal |

Always:
1. GET the form page with a Session.
2. Extract every hidden input's name + value.
3. POST to the form's `action` URL with all hidden fields plus your own.
4. Validate the response — don't assume HTTP 200 means success; many forms re-render the page with an error message.

## 6. CAPTCHA strategies (Chapter 7)

Ranked by what to try first:

1. **Avoid triggering it.** CAPTCHAs are usually rate-limit / fingerprint responses. Slow down; rotate IPs; mirror real-browser headers; use a logged-in session if appropriate.
2. **Negotiate access.** For research/commercial use, contact the site owner. A signed agreement beats every technical workaround.
3. **OCR for simple image CAPTCHAs.** Tesseract or open-source models handle low-quality CAPTCHAs that some long-tail sites still use.
4. **Third-party solving services** (2Captcha, AntiCaptcha, DeathByCaptcha) — paid, ToS-grey, sometimes used in commercial scraping. Engine default: **do not use** unless explicitly authorised.
5. **Human-in-the-loop** — a small UI that pings a human when a CAPTCHA fires. Practical for low-volume jobs.

**reCAPTCHA v3 / hCaptcha:** practically un-bypassable without paid services or browser automation with a real session. If a target uses these, prefer official API access or written permission over technical defeat.

## 7. Scrapy — when the framework wins (Chapter 8)

Scrapy is a full crawling framework. Choose it when the project has:

- Multi-spider, multi-domain crawls.
- Persistent queues, deduplication, retry middleware.
- Pipelines for cleaning, validation, storage.
- Distributed scaling needs (with `scrapy-redis`).

Stick with `requests` + your own loop when the project is a single spider for a single site with simple output.

**Minimal Scrapy spider:**

```python
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://example.com/list"]
    custom_settings = {
        "DOWNLOAD_DELAY": 1.5,
        "AUTOTHROTTLE_ENABLED": True,
        "USER_AGENT": REAL_UA,
        "ROBOTSTXT_OBEY": True,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2,
    }

    def parse(self, response):
        for href in response.css("a.detail::attr(href)").getall():
            yield response.follow(href, self.parse_detail)
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_detail(self, response):
        yield {
            "title": response.css("h1::text").get(),
            "price": response.css(".price::text").get(),
            "url": response.url,
        }
```

**Scrapy settings to always set:**

- `ROBOTSTXT_OBEY = True`
- `AUTOTHROTTLE_ENABLED = True` with conservative `AUTOTHROTTLE_TARGET_CONCURRENCY`
- `DOWNLOAD_DELAY` ≥ 1.0
- `RETRY_ENABLED = True`, `RETRY_TIMES = 3`
- `HTTPCACHE_ENABLED = True` during development
- `USER_AGENT` set to a real browser string
- `CONCURRENT_REQUESTS_PER_DOMAIN = 2`

## 8. Storage layer

| Output | Right format |
|---|---|
| <100 k rows, mostly read by humans | CSV |
| Tabular, repeated reads, mixed types | Parquet (columnar, typed, compressed) |
| Document/nested data | JSONL (one JSON per line; streamable) |
| Many appends, search needed | SQLite for single-user, PostgreSQL for multi-user |
| Page caches keyed by URL | MongoDB with TTL index, or filesystem |

**Engine convention:** scraped artefacts land as Parquet + JSONL alongside a manifest (`source`, `fetched_at`, `headers`, `selector_versions`, `n_rows`, `n_errors`). Pair with `data-quality-assessment` to score each batch.

## 9. Resumability and checkpointing

- Persist a frontier queue (URLs to fetch) and a seen set (URLs done).
- Cache responses by URL so a crash + restart re-uses fetched bytes.
- Periodically (every N URLs or M seconds) flush state to disk.
- On restart: load seen, load frontier, dedupe, continue.

For Scrapy: enable `JOBDIR` (`scrapy crawl example -s JOBDIR=jobs/example`) — it persists the request queue and dupefilter to disk.

## 10. Anti-patterns

- Re-fetching the same URL on every dev iteration (no cache).
- Using a headless browser when a JSON XHR exists.
- Threadpool with 50 workers all hitting one host.
- No timeouts on `requests.get` (hangs forever on slow servers).
- Ignoring `Retry-After` from 429 responses.
- Fragile selectors keyed on auto-generated CSS classes that change between deploys.
- Crashing the whole crawl on a single failed URL.
- Pickling raw HTML into ever-growing files without TTL.
- Scrapy with `ROBOTSTXT_OBEY = False` and no `DOWNLOAD_DELAY`.
- Storing scraped data only in CSV when a Parquet would be 5–20× smaller.
- Solving CAPTCHAs as the first move when slowing down would have prevented them.

## 11. Pipeline ship gate

- [ ] Cache layer in place (disk or Mongo); TTL enforced.
- [ ] Concurrency capped per host within etiquette.
- [ ] All requests have timeouts.
- [ ] Retry middleware with exponential backoff and Retry-After respect.
- [ ] Dynamic content: XHR endpoint preferred; headless only where needed.
- [ ] Form pages fetched fresh; hidden fields propagated.
- [ ] CAPTCHA strategy declared (avoid > negotiate > OCR > paid > human).
- [ ] Output format chosen (Parquet / JSONL / SQLite / Postgres) with manifest.
- [ ] Resumable: frontier and seen set persisted; cached responses survive restart.
- [ ] Selectors verified across ≥3 records; tolerate missing fields.
- [ ] Logging: per-URL status, per-batch summary, no spammy stack traces.

## See also

- `scraping-troubleshooting-brody` — etiquette and debugging
- `web-scraping-foundations` — HTTP/HTML basics
- `scraping-politeness-and-ratelimiting` — politeness layer
- `data-quality-assessment` — score scraped batches
- `merge-discipline` — joining scraped data with reference data
