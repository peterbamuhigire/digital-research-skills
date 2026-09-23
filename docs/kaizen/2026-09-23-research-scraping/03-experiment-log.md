# Experiment log

## PDSA-1 — compose a bounded research scraper

- **Plan:** compose the existing HTTP, robots, throttle, cache, HTML,
  JSON-LD, OpenGraph, and URL-cleaning primitives into one injectable class.
- **Do:** add `tools/scraping/research_scraper.py` and
  `scripts/scrape_research_sources.py`; default to same-host scope and
  robots-respecting fetches.
- **Study:** offline fixtures prove extraction, link scope, cache reuse, and
  bad-page isolation. No live target was contacted as part of this change.
- **Act:** standardize the module, CLI, manifest contract, and tests. Keep
  browser automation and parallel crawling out of this first experiment until
  sequential behavior is observed.

Stop condition: any request to bypass robots, authentication, CAPTCHA, or a
server block is outside this experiment and must be surfaced as a gap.
