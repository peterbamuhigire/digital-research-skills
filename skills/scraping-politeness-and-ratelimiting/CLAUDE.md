# Claude-specific — scraping-politeness-and-ratelimiting

- Defaults: respect robots, throttle 1s/host, identify with engine's UA + contact URL.
- Block detection (`SoftBlock` from `http_client`): treat as "stop", not "retry harder".
- Off-hours scheduling for any heavy crawl.

See `SKILL.md`.
