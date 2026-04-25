"""RSS / Atom / sitemap parsers."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator
from xml.etree import ElementTree as ET


@dataclass(slots=True)
class FeedItem:
    title: str
    link: str
    published: str | None
    summary: str | None


def parse_feed(url_or_xml: str) -> list[FeedItem]:
    """Parse RSS or Atom. Pass URL or raw XML.

    Lazy-imports feedparser.
    """
    import feedparser
    parsed = feedparser.parse(url_or_xml)
    return [
        FeedItem(
            title=str(getattr(e, "title", "")),
            link=str(getattr(e, "link", "")),
            published=str(getattr(e, "published", None) or "") or None,
            summary=str(getattr(e, "summary", None) or "") or None,
        )
        for e in parsed.entries
    ]


def parse_sitemap(xml: str) -> Iterator[str]:
    """Yield URLs from a sitemap.xml or a sitemap-index. No deps beyond stdlib."""
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        return
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    # Sitemap index → recurse
    for sm in root.findall("sm:sitemap/sm:loc", ns):
        if sm.text:
            yield sm.text
    # URL set → emit URLs
    for u in root.findall("sm:url/sm:loc", ns):
        if u.text:
            yield u.text
