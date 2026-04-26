# Codex / generic-agent — scraping-engineering-python

```yaml
scraper_pipeline:
  cache: {backend: disk | mongo, ttl_days: <int>}
  concurrency:
    model: threading | asyncio | multiprocessing
    workers_total: <int>
    workers_per_host: <int>
  dynamic_content:
    strategy: xhr_endpoint | inline_json | headless_browser
    headless_tool: playwright | selenium | webkit | splash
  forms:
    handler: requests_session | mechanicalsoup | playwright
    csrf_propagated: bool
  captcha:
    strategy: avoid | negotiate | ocr | paid_service | human_in_loop
  storage: {format: parquet | jsonl | sqlite | postgres, manifest: bool}
  resumability:
    frontier_persisted: bool
    seen_set_persisted: bool
    response_cache_keyed_by_url: bool
  scrapy_settings:
    robotstxt_obey: true
    autothrottle: true
    download_delay: <float>
    concurrent_requests_per_domain: <int>
    retry_times: <int>
    httpcache_enabled: bool
```

See `SKILL.md`.
