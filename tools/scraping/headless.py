"""Playwright-first headless browser fetcher.

Per Brody's diagnostic: only use a headless browser when (a) View Source
shows the data isn't there and (b) you can't find the underlying XHR endpoint.
Otherwise use the plain HTTP path — it's an order of magnitude faster.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable, Optional


@dataclass(slots=True)
class CapturedRequest:
    method: str
    url: str
    headers: dict[str, str]
    body: Optional[str]
    response_status: int
    response_body: Optional[str]


@dataclass(slots=True)
class RenderResult:
    url: str
    final_url: str
    html: str
    captured_xhr: list[CapturedRequest] = field(default_factory=list)
    screenshot_path: Optional[str] = None


async def render(
    url: str,
    *,
    wait_for_selector: Optional[str] = None,
    wait_for_url: Optional[str] = None,
    storage_state: Optional[str] = None,
    block_resources: tuple[str, ...] = ("image", "font", "media"),
    capture_xhr: bool = False,
    screenshot_path: Optional[str] = None,
    user_agent: Optional[str] = None,
    timeout_ms: int = 30_000,
    stealth: bool = True,
) -> RenderResult:
    """Render a URL with Playwright. Lazy-imports playwright."""
    from playwright.async_api import async_playwright

    captured: list[CapturedRequest] = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=user_agent,
            storage_state=storage_state,
        )
        if stealth:
            await _apply_stealth(context)

        # Block heavy resources for speed
        if block_resources:
            await context.route(
                "**/*",
                lambda route: route.abort() if route.request.resource_type in block_resources else route.continue_(),
            )

        page = await context.new_page()

        if capture_xhr:
            async def _on_response(response: Any) -> None:
                req = response.request
                if req.resource_type in ("xhr", "fetch"):
                    try:
                        body = await response.text()
                    except Exception:
                        body = None
                    captured.append(CapturedRequest(
                        method=req.method, url=req.url, headers=dict(req.headers),
                        body=req.post_data, response_status=response.status, response_body=body,
                    ))

            page.on("response", _on_response)

        await page.goto(url, timeout=timeout_ms, wait_until="networkidle")
        if wait_for_selector:
            await page.wait_for_selector(wait_for_selector, timeout=timeout_ms)
        if wait_for_url:
            await page.wait_for_url(wait_for_url, timeout=timeout_ms)

        html = await page.content()
        final_url = page.url
        if screenshot_path:
            await page.screenshot(path=screenshot_path, full_page=True)

        await browser.close()

    return RenderResult(url=url, final_url=final_url, html=html,
                        captured_xhr=captured, screenshot_path=screenshot_path)


async def _apply_stealth(context: Any) -> None:
    """Light-touch stealth: hide webdriver flag.
    For full stealth, install the `playwright-stealth` package and use it instead.
    """
    await context.add_init_script(
        """
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        """
    )


async def login_and_save_state(
    login_url: str,
    *,
    fill: dict[str, str],
    submit_selector: str,
    out_path: str,
    success_selector: Optional[str] = None,
    timeout_ms: int = 30_000,
) -> None:
    """Drive a login form and save browser state for replay.

    fill: {selector: value} pairs
    """
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(login_url, timeout=timeout_ms)
        for selector, value in fill.items():
            await page.fill(selector, value)
        await page.click(submit_selector)
        if success_selector:
            await page.wait_for_selector(success_selector, timeout=timeout_ms)
        await context.storage_state(path=out_path)
        await browser.close()
