# Claude-specific — browser-automation-playwright

- Use `tools.scraping.headless.render` not raw Playwright.
- Always block image/font/media resources on data-only pages.
- `wait_for_selector` not `time.sleep`.
- `storage_state` for replay after login.

See `SKILL.md`.
