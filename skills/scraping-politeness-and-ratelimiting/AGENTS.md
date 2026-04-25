# Codex / generic-agent — scraping-politeness-and-ratelimiting

```yaml
robots_check: required
throttle:
  base_delay_s: 1.0
  jitter_s: 0.3
  adaptive: true | false
backoff:
  base_s: 2.0
  max_retries: 3
  retry_on: [500, 502, 503, 504, 408, 429]
identification:
  user_agent: "<bot>/<ver> (+contact-url)"
block_signals:
  on_429: stop_and_backoff
  on_403_captcha: stop_and_escalate
  on_softblock: stop_and_escalate
schedule:
  off_hours: true
```

See `SKILL.md`.
