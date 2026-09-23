from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.scraping.http_client import FetchResult
from tools.scraping.research_scraper import ResearchScraper


HTML = """<!doctype html>
<html><head><title>Example Research</title>
<meta property='og:description' content='A concise description'>
<script type='application/ld+json'>{"@type":"Article","headline":"Example Research"}</script>
</head><body><main><h1>Example Research</h1><p>Useful source text.</p>
<a href='/next'>Next</a><a href='https://other.example/no'>Outside</a></main></body></html>"""


class ResearchScraperTests(unittest.TestCase):
    def test_extracts_provenance_and_keeps_links_in_scope(self) -> None:
        calls: list[str] = []

        def fake_fetch(url: str, **_: object) -> FetchResult:
            calls.append(url)
            return FetchResult(url=url, status=200, headers={"content-type": "text/html"},
                               text=HTML, content=HTML.encode(), final_url=url, elapsed_seconds=0.01)

        with tempfile.TemporaryDirectory() as tmp:
            run = ResearchScraper(tmp, user_agent="test-bot", delay=0, max_pages=2,
                                  fetch_fn=fake_fetch).run(["https://example.test/start"])
            records = [json.loads(line) for line in (Path(tmp) / "records.jsonl").read_text().splitlines()]
            self.assertEqual(run.pages_succeeded, 2)
            self.assertEqual(len(calls), 2)
            self.assertEqual(records[0]["title"], "Example Research")
            self.assertEqual(records[0]["opengraph"]["og:description"], "A concise description")
            self.assertEqual(records[0]["links"], ["https://example.test/next", "https://other.example/no"])

    def test_cache_prevents_refetch_on_second_run(self) -> None:
        calls = 0

        def fake_fetch(url: str, **_: object) -> FetchResult:
            nonlocal calls
            calls += 1
            return FetchResult(url=url, status=200, headers={}, text=HTML, content=HTML.encode(),
                               final_url=url, elapsed_seconds=0.01)

        with tempfile.TemporaryDirectory() as tmp:
            first = ResearchScraper(tmp, user_agent="test-bot", delay=0, max_pages=1,
                                    fetch_fn=fake_fetch).run(["https://example.test/start"])
            second = ResearchScraper(tmp, user_agent="test-bot", delay=0, max_pages=1,
                                     fetch_fn=fake_fetch).run(["https://example.test/start"])
            self.assertEqual(first.pages_succeeded, 1)
            self.assertEqual(second.pages_succeeded, 1)
            self.assertEqual(calls, 1)
            record = json.loads((Path(tmp) / "records.jsonl").read_text().splitlines()[0])
            self.assertTrue(record["from_cache"])

    def test_bad_page_is_recorded_without_aborting_run(self) -> None:
        def fake_fetch(url: str, **_: object) -> FetchResult:
            if url.endswith("bad"):
                raise RuntimeError("fixture failure")
            return FetchResult(url=url, status=200, headers={}, text="<title>ok</title>",
                               content=b"<title>ok</title>", final_url=url, elapsed_seconds=0.01)

        with tempfile.TemporaryDirectory() as tmp:
            run = ResearchScraper(tmp, user_agent="test-bot", delay=0, max_pages=2,
                                  fetch_fn=fake_fetch).run(["https://example.test/bad", "https://example.test/good"])
            self.assertEqual(run.pages_failed, 1)
            self.assertEqual(run.pages_succeeded, 1)
            self.assertEqual(run.errors[0]["error_type"], "RuntimeError")


if __name__ == "__main__":
    unittest.main()
