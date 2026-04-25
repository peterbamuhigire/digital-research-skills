"""BeautifulSoup wrappers with safe defaults.

Per Lawson: lxml parser by default for speed (~6x faster than html.parser).
Per Brody: never index by visual position; always use semantic selectors.
"""
from __future__ import annotations

from typing import Any, Optional
from urllib.parse import urljoin


def parse_html(html: str, *, parser: str = "lxml") -> Any:
    """Return a BeautifulSoup object. Lazy-imports BeautifulSoup."""
    from bs4 import BeautifulSoup
    return BeautifulSoup(html, parser)


def select(soup: Any, css: str, *, default: Optional[str] = None) -> Optional[str]:
    """First match's stripped text, or default."""
    el = soup.select_one(css)
    if el is None:
        return default
    return el.get_text(strip=True)


def select_all(soup: Any, css: str) -> list[str]:
    """All matches as stripped text."""
    return [el.get_text(strip=True) for el in soup.select(css)]


def extract_text(soup_or_node: Any, *, separator: str = " ", strip: bool = True) -> str:
    """Clean text extraction."""
    return soup_or_node.get_text(separator=separator, strip=strip)


def extract_links(soup: Any, base_url: str) -> list[str]:
    """All <a href=> values resolved to absolute URLs."""
    out: list[str] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith(("javascript:", "mailto:", "#")):
            continue
        out.append(urljoin(base_url, href))
    return out


def safe_attr(soup: Any, css: str, attr: str, *, default: Optional[str] = None) -> Optional[str]:
    """Safely fetch an attribute on the first match."""
    el = soup.select_one(css)
    if el is None:
        return default
    return el.get(attr, default)
