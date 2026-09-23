# Next cycle

Re-audit by 2026-10-23 or sooner after a live scrape exposes a defect.

1. Run the three-page authorized sample and verify source values against the
   pages, including missing fields and structured-data disagreement.
2. Add a fixture for redirect provenance and explicit `Retry-After` handling.
3. Recheck current package APIs and the active model catalogue; do not infer
   availability from memory or from the book.
4. Consider a Scrapy adapter only if measured workload exceeds the current
   bounded collector's needs.
