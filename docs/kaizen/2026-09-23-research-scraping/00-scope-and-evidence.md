# Kaizen scope and evidence

Date: 2026-09-23
Cycle: `2026-09-23-research-scraping`
Owner: Peter Bamuhigire

## Aim

Make the digital research engine able to run a bounded, repeatable Python web
collection with raw-response caching, robots-aware acquisition, structured-data
extraction, same-host scope control, provenance, and restart-safe outputs.

## Source inputs

- Durable concept input: Ryan Mitchell, *Web Scraping with Python: Data
  Extraction from the Modern Web*, 3rd ed., O'Reilly, 2024. Local PDF was
  inspected outside the repository. SHA-256:
  `2140DAC5CE4E06CED3427FC1E644946AC04A3711CDB1AFF34F7B5AA74C9E29E5`.
- The book is not copied into the repository. No OCR, chapter dump, raw code
  extraction, or book text is committed. Only an independent implementation
  synthesis is retained below.
- Existing engine sources inspected: `web-scraping-foundations`,
  `scraping-engineering-python`, `tools/scraping/*`, and current tests.

## Scope and exclusions

The change covers public HTTP(S) pages supplied by an operator. It excludes
authentication bypass, CAPTCHA solving, proxy rotation to defeat limits,
form submission, personal-data targeting, and automatic cross-domain expansion.
Live target behavior, terms, and legal permission remain target-specific and
must be assessed before a production run.

## Book-to-engine synthesis

The useful concepts were translated into contracts rather than copied: choose
the least invasive acquisition path; separate crawling from parsing and
storage; preserve raw responses for re-extraction; normalize dirty text; treat
APIs and structured data as first-class inputs; classify blocks and failures;
test selectors against fixtures; and scale only after sequential behavior is
known. Current robots, library, and target behavior are not established by the
book.

## Currentness gate

Current model-release evidence was checked against official OpenAI model pages
on 2026-09-23: `https://developers.openai.com/api/docs/models` and
`https://developers.openai.com/api/docs/guides/model-selection`. The repository
policy check reported `DRIFT: root model policy drift`; the active
runtime/account catalogue was not exposed to this session. Model evaluation is
therefore `NOT_ASSESSED`; no model-policy file was changed.

The local Python 3.13.7 environment had requests 2.32.5, httpx 0.28.1,
beautifulsoup4 4.15.0, and lxml 6.1.1 installed on the access date. These are
environment observations, not a repository support promise. Target-site
robots, terms, permissions, selectors, and live response behavior are
`NOT_ASSESSED` until an operator runs a scoped acquisition plan.
