"""Open Graph + Twitter Card meta extraction."""
from __future__ import annotations


def extract_opengraph(html: str) -> dict[str, str]:
    """Return all og:* and twitter:* meta tags as a flat dict."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    out: dict[str, str] = {}
    for m in soup.find_all("meta"):
        prop = m.get("property") or m.get("name")
        content = m.get("content")
        if prop and content and (prop.startswith("og:") or prop.startswith("twitter:")):
            out[prop] = content
    return out
