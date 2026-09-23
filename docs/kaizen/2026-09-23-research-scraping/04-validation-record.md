# Validation record

Run from the repository root with Python 3.13.7:

- `python -m unittest discover -s tests -p "test_research_scraper.py"` —
  expected: 3 tests pass.
- `python -m pytest tests/test_research_scraper.py` — expected: 3 tests pass.
- Native engine validators are required before release; their result is
  recorded in the final report.

The tests are offline and do not establish robots compliance, target terms,
live selectors, browser rendering, current package compatibility beyond the
tested environment, or legal permission. Those checks remain `NOT_ASSESSED`.
