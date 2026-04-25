# Codex / generic-agent — web-scraping-foundations

Per scrape:

```yaml
target_url: "..."
data_path: api | xhr_json | html | headless
parser: lxml | selectolax | html5lib
structured_data_checked: [json_ld, opengraph, sitemap, rss]
pagination_pattern: offset | cursor | xhr | hash
rate_limit: <req/sec/host>
robots_check: passed | failed
error_class_observed: none | ScrapeError | RateLimited | RobotsBlocked | SoftBlock
```

See `SKILL.md`.
