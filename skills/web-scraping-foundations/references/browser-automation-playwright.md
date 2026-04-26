# Browser automation — Playwright

Playwright supersedes Selenium for new work. Auto-waiting, browser contexts, network interception, codegen.

## When to use Playwright (vs plain HTTP)

Use a headless browser ONLY when:
1. View Source confirms the data isn't in the HTML, AND
2. DevTools Network XHR scan finds no usable JSON endpoint, AND
3. The data requires JS interaction (click, scroll, multi-step form).

If any of those is false, use plain HTTP. Playwright is 10–100× slower than `httpx` per page.

## Standard recipe

```python
from tools.scraping.headless import render

result = await render(
    "https://example.com/dynamic",
    wait_for_selector=".product-card",
    block_resources=("image", "font", "media"),  # speed up
    capture_xhr=True,                            # also collect XHR responses
    screenshot_path="debug.png",
    stealth=True,                                # hide webdriver flag
)
print(result.html[:1000])
for xhr in result.captured_xhr:
    print(xhr.method, xhr.url, xhr.response_status)
```

## Wait strategies — never use `time.sleep`

| Wait | When |
|---|---|
| `page.wait_for_selector(sel)` | Element must appear |
| `page.wait_for_load_state("networkidle")` | All network quiet |
| `page.wait_for_response(lambda r: "/api/" in r.url)` | Capture specific XHR |
| `page.wait_for_url("**/dashboard")` | Navigation to specific URL |

`time.sleep()` is the canonical anti-pattern.

## Login + replay (storage_state)

```python
from tools.scraping.headless import login_and_save_state

await login_and_save_state(
    "https://example.com/login",
    fill={"#email": "u@x.com", "#password": "..."},
    submit_selector="button[type=submit]",
    out_path="auth.json",
    success_selector=".user-menu",
)

# Later — replay without re-logging in
result = await render(url, storage_state="auth.json")
```

## Network interception for blocking analytics / images

```python
await context.route(
    "**/*",
    lambda route: route.abort()
        if route.request.resource_type in ("image", "font", "media")
        else route.continue_(),
)
```

Halves page-load time; doesn't affect data extraction.

## Codegen — record interactions

```bash
playwright codegen https://example.com
```

Opens a browser; record clicks/typing; outputs Python script. Useful for one-off complex flows.

## Stealth

For light stealth, the engine's `tools/scraping/headless.render(stealth=True)` patches `navigator.webdriver`. For full stealth (canvas / WebGL / plugin lists / fonts):

```bash
pip install playwright-stealth
```

```python
from playwright_stealth import stealth_async
await stealth_async(page)
```

**Ethics:** stealth is for cases where the site's TLS / fingerprint detection breaks legitimate research access. Don't use stealth + proxy + CAPTCHA-solver to defeat a site that has explicitly blocked you.

## Anti-patterns

- `time.sleep` instead of `wait_for_*`
- Headless when plain HTTP would work
- Forgetting to `await browser.close()` (leaks Chrome processes)
- Not blocking images on data-only pages (3× slowdown)
- Stealth + proxy + CAPTCHA solver chain to defeat clear "no" signals

## See also

- `tools/scraping/headless.py` — implementation
- `web-scraping-foundations` — decision tree (start there)
- `scraping-politeness-and-ratelimiting` — even with Playwright, throttle
- `scraping-pattern-discovery` — finding the underlying XHR is usually faster
