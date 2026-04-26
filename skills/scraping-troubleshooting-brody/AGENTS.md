# Codex / generic-agent — scraping-troubleshooting-brody

```yaml
scraper_audit:
  user_agent_set: bool
  full_browser_headers: bool
  uses_session_only_if_login_required: bool
  csrf_tokens_handled: bool
  robots_txt_parsed: bool
  crawl_delay_honored: bool
  default_sleep_seconds: [<float min>, <float max>]
  concurrency_per_host: <int>
  retry_policy:
    backoff: exponential
    cap_retries: <int>
    respects_retry_after: bool
  missing_field_handling: normalize_to_none
  resumable_checkpoint: bool
  xhr_first_html_fallback: bool
```

See `SKILL.md`.
