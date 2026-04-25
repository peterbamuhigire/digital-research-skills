---
name: web-scraping-foundations
description: Use as the entry point for any web-scraping task. Covers the requests/httpx/Playwright decision tree, parser choice, JS reverse-engineering vs headless rendering, structured-data shortcuts (JSON-LD, OG, sitemaps, RSS), and error taxonomy. Backed by tools/scraping/. Adapted from Lawson, Brody, Oxylabs, and the Hands-On Scraping books.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Web scraping foundations

The four scraping books we studied converge on the same decision tree. Memorise it.

## The decision tree

1. **Can the data be obtained from a published API or dataset?** If yes, use it instead. Skip scraping. (`dataset-discovery-and-analysis`)
2. **View source. Is the data in the HTML?** If yes → `requests` / `httpx` + BeautifulSoup. Done.
3. **Open DevTools → Network → XHR. Is there a JSON endpoint?** If yes → call it directly. Often easier and faster than HTML.
4. **Is the data only available after JS interaction?** Only then → Playwright (`tools/scraping/headless.py`).
5. **Is this a multi-domain crawl with politeness, dedup, pause/resume?** Use Scrapy. (See `scrapy-distributed-crawling` — roadmap.)

**Don't skip steps.** Brody: *"View Source → Cmd-F for a known datum"* is the cheapest diagnostic.

## Stack choices

| Layer | Default | When to switch |
|---|---|---|
| HTTP | `httpx` (async) or `requests` (sync) | `curl-cffi` if TLS-fingerprint blocks |
| Parser | `BeautifulSoup(html, "lxml")` | `selectolax` for >1k pages/sec |
| Selectors | CSS via `.select()` | XPath only when CSS can't (axis nav, position) |
| Headless | Playwright | Selenium only when migrating legacy scripts |
| Crawler | Scrapy | Hand-rolled `requests` loop only for one-domain pulls |
| Storage | SQLite for ad-hoc; Postgres for prod | CSV for share with non-engineers |
| Rate limit | `tools.scraping.Throttle` | `AdaptiveThrottle` for unknown servers |

## Always check structured-data shortcuts FIRST

Many sites publish clean structured data for crawlers. Use it:

- **JSON-LD** in `<script type="application/ld+json">` — Schema.org Product, Article, Organization, BreadcrumbList. **Always check this before parsing the DOM.** (`tools.scraping.extract_jsonld`)
- **Open Graph + Twitter Cards** — `og:title`, `og:image`, `og:description`. (`tools.scraping.extract_opengraph`)
- **RSS / Atom feeds** — `feedparser`. (`tools.scraping.extractors.feeds.parse_feed`)
- **`/sitemap.xml`** — enumeration without link-following. (`tools.scraping.extractors.feeds.parse_sitemap`)
- **`/robots.txt`** — Sitemap declarations + Disallow rules. (`tools.scraping.sitemaps_for`)

A scraper that ignores these layers wastes effort.

## Pagination patterns

Four canonical types:

1. **Query-string offset** — `?page=N`. Use `paginate_offset()`.
2. **Cursor-based** — server returns next-cursor in body. Use `paginate_cursor()`.
3. **Infinite scroll / Load More** — XHR backed. Find the endpoint via DevTools, use `paginate_xhr()`.
4. **Hash-based** (`#page=2`) — client-side only; needs Playwright OR find underlying API.

**Edge-case probe:** try `page_size=1000` first. Servers often don't validate against UI options.

## Error taxonomy (from `tools.scraping.http_client`)

| Class | When | Caller action |
|---|---|---|
| `RobotsBlocked` | robots.txt disallows | Stop. Don't override without authorisation. |
| `RateLimited` (429) | Server says slow down | Back off; reduce concurrency. |
| `ScrapeError` (4xx) | Auth / not found | Don't retry. Surface to operator. |
| `ScrapeError` (5xx) | Server fault | Exponential-backoff retry (3 max). |
| `SoftBlock` | 200 but body is CAPTCHA / interstitial | Stop. Reduce footprint. Don't escalate. |

**Anti-pattern:** silent retry on 4xx. Surface, don't bury.

## Parser performance

Lawson's benchmark for 1000 iterations on the same page:
- regex: 5.5s
- lxml: 7.0s
- BeautifulSoup (Python parser): 42.8s

**Decision:** default to `BeautifulSoup(html, "lxml")` (fast + ergonomic). Only profile for `selectolax` (~10× faster than lxml on huge pages) when the parser is the actual bottleneck (rare — network usually dominates).

## Caching raw HTML

Lawson's central discipline: **store raw HTML, not just parsed records**. Re-extraction is free; re-crawling is expensive. Use `tools.scraping.DiskCache` or `SQLiteCache` for any non-trivial crawl.

## Anti-patterns

- `time.sleep()` as a wait strategy — use Playwright's `wait_for_selector`
- `verify=False` as a habit — only for self-signed dev hosts
- Indexing by visual position (`soup.find_all('div')[3]`) — semantic selectors only
- Single giant try/except wrapping the whole crawl — swallows real bugs
- Re-crawling on every run — cache raw HTML
- Hard-coded selectors with no graceful "MISSING DATA" fallback
- Parsing HTML with regex (parser preferred; regex only on extracted text)
- Hammering a server with no delay — use `Throttle`

## See also

- `tools/scraping/` — actual implementation
- `browser-automation-playwright` — when headless is needed
- `scraping-politeness-and-ratelimiting` — robots, throttle, backoff
- `scraping-pattern-discovery` — Brody's diagnostic workflow
- `scraped-data-validation` — pydantic + parquet (roadmap)
- `scraping-legal-and-ethical-bounds` — what's lawful (roadmap)
