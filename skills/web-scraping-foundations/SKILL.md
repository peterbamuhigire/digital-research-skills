---
name: web-scraping-foundations
description: Use as the single entry point for any web-scraping task. Carries the decision tree (API → JSON XHR → HTML → headless), structured-data shortcuts, parser/HTTP stack choices, error taxonomy, and orchestration rules across politeness, troubleshooting, and browser-automation references. Backed by tools/scraping/.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Web Scraping Foundations

The single entry skill for web scraping. Encodes the decision tree, stack choices, and orchestration rules. Detailed sub-disciplines live in `references/` and are loaded only when the situation demands them.

## Companion skill

- `scraping-engineering-python` — kept separate because it is the Python-specific scaling layer (caching, concurrency, dynamic content, Scrapy framework selection). Load it when the crawl exceeds ~1,000 URLs, requires resumability, or needs concurrent downloading.

## Reference index

When the situation matches the trigger, load the named reference verbatim. Do not load all references by default.

| Reference | Load when |
|---|---|
| `references/politeness-and-ratelimiting.md` | Every non-trivial scrape — robots.txt, throttle, backoff, identification headers, block-detection signals |
| `references/troubleshooting-brody.md` | Scraper returns empty/different content, gets blocked, or needs to behave like a real browser (header spoofing, session cookies, hidden CSRF tokens, missing-element resilience, debugging workflow) |
| `references/browser-automation-playwright.md` | Decision tree below has eliminated plain-HTTP options and JS rendering is required — Playwright recipes, wait strategies, login replay, network interception, stealth |

## 1. The decision tree (memorise — never skip)

Run in this order on every job. Stop at the first step that succeeds.

1. **Is the data available from a published API or open dataset?** Use it. Skip scraping. (See `dataset-discovery-and-analysis`.)
2. **View Source. Is the data in the response HTML?** Yes → `requests`/`httpx` + BeautifulSoup. Done.
3. **DevTools → Network → XHR. Is there a JSON endpoint?** Yes → call it directly. Faster and more stable than HTML parsing.
4. **Inline JSON in `<script>` tags?** (`__NEXT_DATA__`, `window.__INITIAL_STATE__`.) Extract and parse before considering a browser.
5. **Does the page require JS interaction (click, scroll, multi-step form)?** Only now → load `references/browser-automation-playwright.md`.
6. **Multi-domain crawl with politeness, dedup, pause/resume needs?** Load `scraping-engineering-python` for Scrapy.

> Brody's cheapest diagnostic: *"View Source → Cmd-F for a known datum."* If the datum is visible there, no JS is needed.

## 2. Always check structured-data shortcuts FIRST

Many sites publish clean structured data:

- **JSON-LD** in `<script type="application/ld+json">` — Schema.org Product/Article/Organization (`tools.scraping.extract_jsonld`).
- **Open Graph + Twitter Cards** — `og:title`, `og:image`, `og:description` (`tools.scraping.extract_opengraph`).
- **RSS / Atom feeds** — `feedparser` (`tools.scraping.extractors.feeds.parse_feed`).
- **`/sitemap.xml`** — server-blessed enumeration without link-following.
- **`/robots.txt`** — Sitemap declarations + Disallow rules.

A scraper that ignores these layers wastes effort.

## 3. Stack choices

| Layer | Default | Switch when |
|---|---|---|
| HTTP | `httpx` (async) or `requests` (sync) | TLS-fingerprint blocks → `curl-cffi` |
| Parser | `BeautifulSoup(html, "lxml")` | >1k pages/sec → `selectolax` |
| Selectors | CSS `.select()` | CSS can't (axis nav, position) → XPath |
| Headless | Playwright | Migrating legacy → Selenium |
| Crawler | Hand-rolled `requests` loop | Multi-domain or resumable → Scrapy (load `scraping-engineering-python`) |
| Storage | SQLite ad-hoc; Postgres prod; **Parquet + JSONL** for scraped artefacts | CSV only for human share |
| Rate limit | `tools.scraping.Throttle` | Unknown server behaviour → `AdaptiveThrottle` |

## 4. Pagination patterns

| Pattern | Recognise by | Strategy |
|---|---|---|
| Query-string offset | `?page=N` | `paginate_offset()` |
| Cursor-based | server returns `next` token | `paginate_cursor()` |
| Infinite scroll / Load More | XHR-backed | DevTools → find endpoint → `paginate_xhr()` |
| Hash-based (`#page=2`) | client-side only | Find underlying API or use Playwright |

**Edge-case probe:** try `page_size=1000` first — servers often don't validate against UI options.

## 5. Error taxonomy

| Class | When | Action |
|---|---|---|
| `RobotsBlocked` | robots.txt disallows | Stop. Don't override without authorisation. |
| `RateLimited` (429) | Server says slow down | Honour `Retry-After`; reduce concurrency; lengthen delay floor |
| `ScrapeError` (4xx) | Auth / not found | Don't retry. Surface to operator. |
| `ScrapeError` (5xx) | Server fault | Exponential-backoff retry, max 3 |
| `SoftBlock` | 200 but body is CAPTCHA / interstitial | Stop. Reduce footprint. |

**Anti-pattern:** silent retry on 4xx. Surface, don't bury.

## 6. Orchestration — what to load and when

```
new scraping task
├─ load this SKILL.md
├─ ALWAYS load references/politeness-and-ratelimiting.md before issuing requests
├─ Step 2 fails (content differs from browser, or empty)
│   └─ load references/troubleshooting-brody.md
├─ Step 5 fires (JS interaction required)
│   └─ load references/browser-automation-playwright.md
└─ Crawl exceeds 1,000 URLs / needs resumability / multi-domain
    └─ load scraping-engineering-python skill
```

## 7. Caching raw HTML

Lawson's central discipline: **store raw HTML, not just parsed records.** Re-extraction is free; re-crawling is expensive. Use `tools.scraping.DiskCache` or `SQLiteCache` for any non-trivial crawl. Detail in `scraping-engineering-python`.

## 8. Parser-performance baseline

Lawson's 1000-iteration benchmark on the same page: regex 5.5 s · lxml 7.0 s · BeautifulSoup pure-Python 42.8 s. Default to `BeautifulSoup(html, "lxml")` (fast + ergonomic). Only profile for `selectolax` (~10× faster than lxml on huge pages) when the parser is the actual bottleneck — network usually dominates.

## 9. Universal anti-patterns

- `time.sleep()` as a wait strategy in browser code — use `wait_for_selector`.
- `verify=False` as a habit — only for self-signed dev hosts.
- Indexing by visual position (`soup.find_all('div')[3]`) — use semantic selectors.
- Single giant try/except wrapping the whole crawl — swallows real bugs.
- Re-crawling on every run — cache raw HTML.
- Hard-coded selectors with no graceful "MISSING DATA" fallback.
- Parsing HTML with regex (parser preferred; regex only on extracted text).
- Hammering a server with no delay — use `Throttle`.
- Running a headless browser when a JSON XHR exists.

## 10. Ship gate (universal)

- [ ] Decision tree run; the chosen approach is the cheapest one that works.
- [ ] Structured-data shortcuts checked before HTML parsing.
- [ ] `references/politeness-and-ratelimiting.md` rules applied (robots.txt, throttle, identification, backoff).
- [ ] Selectors verified against ≥3 records.
- [ ] Missing fields normalised to `None`; one bad record does not crash the crawl.
- [ ] Errors surfaced by class (4xx vs 5xx vs 429 vs SoftBlock).
- [ ] Raw HTML cached for non-trivial crawls.
- [ ] Output stored as Parquet + JSONL with manifest (`source`, `fetched_at`, `headers`, `selector_versions`, `n_rows`, `n_errors`).
- [ ] If headless was used, the trigger from Step 5 is documented.

## See also

- `scraping-engineering-python` — caching, concurrency, dynamic content, Scrapy
- `dataset-discovery-and-analysis` — try this before scraping
- `data-quality-assessment` — score scraped batches on the four-axis model
- `evidence-discipline` — when scraping for OSINT/DD, evidence rules override defaults
