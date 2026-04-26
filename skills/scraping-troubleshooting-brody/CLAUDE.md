# Claude-specific — scraping-troubleshooting-brody

- Always set a realistic User-Agent and a full header dict on outbound HTTP.
- When content differs from browser, diff request headers first; check XHR endpoints second; reach for headless browser last.
- For login-required scraping, use Sessions; otherwise omit cookies.
- For POST forms with hidden inputs, fetch the form page first and resubmit all hidden fields.
- Parse robots.txt; honour `Crawl-delay`; default to 1–3 s jittered sleeps.
- Never `[0]` a parsed result without an emptiness check.

See `SKILL.md`.
