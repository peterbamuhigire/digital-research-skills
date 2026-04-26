# Claude-specific — scraping-engineering-python

- Add a cache layer (disk or Mongo) before iterating; never re-fetch in dev.
- Always set `timeout=` on every HTTP call.
- For dynamic content, prefer reverse-engineered JSON XHR before Playwright.
- Cap concurrency per host (≤2–3 for standard sites); concurrency total ≠ per-host.
- For Scrapy projects, enable `ROBOTSTXT_OBEY`, `AUTOTHROTTLE_ENABLED`, `DOWNLOAD_DELAY` ≥ 1, `RETRY_ENABLED`.
- Default storage: Parquet + JSONL with manifest; CSV only for small human-facing outputs.
- CAPTCHAs: try avoidance and rate-limit reduction first; never use paid solving services without explicit authorization.

See `SKILL.md`.
