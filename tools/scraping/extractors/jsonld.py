"""Schema.org JSON-LD extraction.

Per the synthesis: a scraper should ALWAYS check JSON-LD before parsing
the DOM. Sites publish clean structured data specifically for crawlers.
"""
from __future__ import annotations

import json
from typing import Any


def extract_jsonld(html: str) -> list[dict[str, Any]]:
    """Return all parsed JSON-LD blocks from the document.

    Common @types: Product, Article, NewsArticle, Organization, Person,
    BreadcrumbList, FAQPage, Recipe, Event.
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    out: list[dict[str, Any]] = []
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            obj = json.loads(script.string or "")
        except (json.JSONDecodeError, TypeError):
            continue
        if isinstance(obj, list):
            out.extend(o for o in obj if isinstance(o, dict))
        elif isinstance(obj, dict):
            # Some sites wrap in @graph
            graph = obj.get("@graph")
            if isinstance(graph, list):
                out.extend(g for g in graph if isinstance(g, dict))
            else:
                out.append(obj)
    return out


def find_type(blocks: list[dict[str, Any]], type_name: str) -> list[dict[str, Any]]:
    """Filter blocks by Schema.org @type."""
    return [b for b in blocks if _matches_type(b.get("@type"), type_name)]


def _matches_type(t: Any, target: str) -> bool:
    if isinstance(t, str):
        return t == target
    if isinstance(t, list):
        return target in t
    return False
