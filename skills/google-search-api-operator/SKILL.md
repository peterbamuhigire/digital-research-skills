---
name: google-search-api-operator
description: Use when programmatic Google search is needed at scale — wraps Google Custom Search JSON API + SerpAPI + Brave Search API behind a single client. Closes the biggest gap in Brown's Harnessing the Power of Google. Backed by tools/google/search_api.py.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Google search API operator

Brown's *Harnessing the Power of Google* gives a richly worked **manual methodology** but no API surface. This skill closes that gap: every `site:` / `filetype:` / `OR` recipe converts cleanly to a programmatic call.

## When to use the API vs scraping the SERP

| Path | Use when |
|---|---|
| **Custom Search JSON API** | You have a Google Cloud project + CSE configured. ~$5/1000 queries above free tier. |
| **SerpAPI** | You don't want to manage Google API keys; need other engines (Bing, Brave, Yandex). ~$50/mo for 5k queries. |
| **Brave Search API** | Independent index; cheaper; 2k free queries/mo. |
| **Direct SERP scrape** | Don't. Google rate-limits and CAPTCHAs aggressively; explicit ToS violation. |

## Setup

### Custom Search JSON API
1. Create a Google Cloud project.
2. Enable Custom Search API.
3. Create an API key.
4. Create a Programmable Search Engine at https://programmablesearchengine.google.com/ — set "Search the entire web" to use it as general Google.
5. `export GOOGLE_API_KEY=... GOOGLE_CSE_ID=...`

### SerpAPI
1. https://serpapi.com/ — free tier 100 queries/mo.
2. `export SERPAPI_KEY=...`

## Standard usage

```python
from tools.google import GoogleSearchClient, SerpAPIClient, search_sites

client = GoogleSearchClient()  # or SerpAPIClient()

# Single query
for r in client.search('"hostel deposit" site:.go.ke filetype:pdf', num=20):
    print(r.title, r.url, r.snippet)

# Stakeholder fan-out (Brown's chapter 4 method)
sites = ["data.knbs.or.ke", "kra.go.ke", "treasury.go.ke", "judiciary.go.ke"]
for r in search_sites('"rental income tax"', sites=sites, client=client, per_site=10):
    print(r.host, r.title)
```

## Operator translation

Brown's manual operators map directly:

| Manual | API |
|---|---|
| `"phrase"` | quote within `q` parameter |
| `site:domain` | `siteSearch` parameter (CSE) or in `q` (SerpAPI) |
| `filetype:pdf` | `fileType` parameter (CSE) or in `q` (SerpAPI) |
| `-term` | `excludeTerms` (CSE) or `-term` in `q` |
| `OR` | use OR in `q` |
| date `dateRestrict=d7` | last 7 days; also `m1`, `y1` |

## Rate limits

- Google CSE: 100 free queries/day, then $5/1000.
- SerpAPI: tier-based; free 100/mo; $50/mo for 5k.
- **Always cache results** — re-running the same query is wasteful.

## Common recipes

### Stakeholder-first recon

Use with `google-stakeholder-recon` skill:

```python
from tools.google import enumerate_stakeholders, stakeholder_query_bundle, GoogleSearchClient

stakeholders = enumerate_stakeholders(
    topic="rental housing", country_focus=["KE", "UG", "TZ"], include_igos=True,
)
queries = stakeholder_query_bundle("rental housing", stakeholders, file_types=["pdf", "xlsx"])

client = GoogleSearchClient()
for q in queries:
    for r in client.search(q, num=10):
        # process
        ...
```

### Grey-literature hunt

```python
client.search("'security deposit' site:.go.ke filetype:pdf", num=20)
```

### Court records

```python
client.search('"rent restriction" site:kenyalaw.org', num=50)
```

### Cross-jurisdictional

```python
for tld in ["go.ke", "go.ug", "go.tz", "gov.rw"]:
    for r in client.search(f"household survey site:.{tld} filetype:xlsx", num=10):
        ...
```

## Anti-patterns

- Scraping `google.com/search` directly — ToS violation + IP ban
- Burning quota on unique queries that could be cached
- Treating snippet text as primary — fetch the underlying page for citation
- Single-engine dependence — combine 2+ engines for breadth
- Ignoring engine-specific result variance (Google ≠ Bing ≠ Brave)

## See also

- `tools/google/search_api.py` — implementation
- `google-stakeholder-recon` — feeds queries into this skill
- `web-search-operator-grammar` — operator vocabulary
- `tools/google/tld_atlas.py` — TLD reference data
