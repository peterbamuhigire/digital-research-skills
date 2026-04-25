"""Programmatic Google search via Custom Search JSON API or SerpAPI.

Closes the biggest gap in Brown's *Harnessing the Power of Google*: he gives
a richly worked manual methodology but no API surface. This module exposes
his recipes as automatable functions.

Usage:
    client = GoogleSearchClient(api_key=..., cse_id=...)
    for result in client.search('"deposit theft" site:.go.ke', num=20):
        print(result.url)

Or fan-out across an explicit list of sites:
    for r in search_sites('"hostel pain"', sites=['monitor.co.ug', 'nation.africa'], client=client):
        ...
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Iterator, Optional


@dataclass(slots=True)
class SearchResult:
    title: str
    url: str
    snippet: str
    source: str  # "google_cse" | "serpapi"


class GoogleSearchClient:
    """Google Custom Search JSON API client.

    Get an API key at https://developers.google.com/custom-search/v1/overview
    Get a CSE id at https://programmablesearchengine.google.com/
    """

    def __init__(self, api_key: Optional[str] = None, cse_id: Optional[str] = None) -> None:
        self.api_key = api_key or os.environ.get("GOOGLE_API_KEY")
        self.cse_id = cse_id or os.environ.get("GOOGLE_CSE_ID")
        if not self.api_key or not self.cse_id:
            raise RuntimeError("GOOGLE_API_KEY and GOOGLE_CSE_ID required")

    def search(
        self, query: str, *, num: int = 10, start: int = 1,
        site_search: Optional[str] = None, file_type: Optional[str] = None,
        date_restrict: Optional[str] = None,
    ) -> Iterator[SearchResult]:
        """Iterate up to `num` results.

        date_restrict: e.g. 'd7' (last 7 days), 'm1', 'y1'.
        Limit per request is 10; we paginate up to `num`.
        """
        from googleapiclient.discovery import build  # type: ignore
        svc = build("customsearch", "v1", developerKey=self.api_key)

        emitted = 0
        cursor = start
        while emitted < num:
            page_size = min(10, num - emitted)
            params: dict = dict(q=query, cx=self.cse_id, num=page_size, start=cursor)
            if site_search:
                params["siteSearch"] = site_search
            if file_type:
                params["fileType"] = file_type
            if date_restrict:
                params["dateRestrict"] = date_restrict

            resp = svc.cse().list(**params).execute()
            items = resp.get("items", [])
            if not items:
                return
            for item in items:
                yield SearchResult(
                    title=item.get("title", ""),
                    url=item.get("link", ""),
                    snippet=item.get("snippet", ""),
                    source="google_cse",
                )
            emitted += len(items)
            cursor += len(items)


class SerpAPIClient:
    """SerpAPI client — alternative to Google CSE with broader engine support
    (Google, Bing, Brave, Yandex, etc.).

    Get a key at https://serpapi.com/
    """

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or os.environ.get("SERPAPI_KEY")
        if not self.api_key:
            raise RuntimeError("SERPAPI_KEY required")

    def search(
        self, query: str, *, engine: str = "google",
        location: Optional[str] = None, num: int = 10,
    ) -> Iterator[SearchResult]:
        import httpx
        params: dict = {"api_key": self.api_key, "q": query, "engine": engine, "num": num}
        if location:
            params["location"] = location
        r = httpx.get("https://serpapi.com/search.json", params=params, timeout=30.0)
        r.raise_for_status()
        data = r.json()
        for item in data.get("organic_results", []):
            yield SearchResult(
                title=item.get("title", ""),
                url=item.get("link", ""),
                snippet=item.get("snippet", ""),
                source="serpapi",
            )


def search_sites(
    query: str, *, sites: list[str], client: GoogleSearchClient | SerpAPIClient,
    per_site: int = 10,
) -> Iterator[SearchResult]:
    """Brown's stakeholder-first recon: fan out the same query across N sites.
    Yields all results in arrival order."""
    for site in sites:
        scoped = f"{query} site:{site}"
        yield from client.search(scoped, num=per_site)
