#!/usr/bin/env python3
"""CLI for bounded, provenance-first research web collection.

Examples:
  python scripts/scrape_research_sources.py https://example.org --out runs/demo
  python scripts/scrape_research_sources.py --url-file urls.txt --max-pages 50 --out runs/demo
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Make direct execution from any working directory resolve the repository
# package without requiring an editable install.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.scraping.research_scraper import ResearchScraper


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("urls", nargs="*", help="Seed HTTP(S) URLs")
    parser.add_argument("--url-file", type=Path, help="UTF-8 file with one seed URL per line")
    parser.add_argument("--out", required=True, type=Path, help="Run directory for records, cache, and manifest")
    parser.add_argument("--max-pages", type=int, default=25)
    parser.add_argument("--delay", type=float, default=1.0, help="Minimum seconds between requests per host")
    parser.add_argument("--user-agent", default="digital-research-engine/1.0 (+https://github.com/peterbamuhigire/digital-research-skills)")
    parser.add_argument("--allow-cross-host", action="store_true", help="Allow discovered links on other hosts")
    parser.add_argument("--ignore-robots", action="store_true", help="Requires explicit operator authority")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    urls = list(args.urls)
    if args.url_file:
        urls.extend(line.strip() for line in args.url_file.read_text(encoding="utf-8").splitlines()
                    if line.strip() and not line.lstrip().startswith("#"))
    if not urls:
        raise SystemExit("provide at least one URL or --url-file")
    if args.ignore_robots:
        print("WARNING: robots.txt checks disabled by explicit operator flag")
    run = ResearchScraper(args.out, user_agent=args.user_agent, delay=args.delay,
                          max_pages=args.max_pages, same_host_only=not args.allow_cross_host,
                          respect_robots=not args.ignore_robots).run(urls)
    print(f"pages_seen={run.pages_seen} succeeded={run.pages_succeeded} failed={run.pages_failed}")
    print(f"manifest={args.out / 'manifest.json'}")
    return 0 if run.pages_failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
