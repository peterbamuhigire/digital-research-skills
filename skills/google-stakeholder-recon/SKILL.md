---
name: google-stakeholder-recon
description: Use to convert a research topic into a ranked list of likely publishing entities (IGO / foreign-gov / federal / state / NGO / academic / trade) plus a `site:` query bundle. Brown's Chapter 4 method codified. Backed by tools/google/stakeholder.py + tld_atlas.py.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Stakeholder-first recon

Brown's question: *Who cares about this topic enough to publish on it?* Answer that **before** searching, then convert each stakeholder into a `site:` + `filetype:` query.

## The method

1. **List the stakeholders.** International orgs / NGOs / IGOs / federal agencies / state agencies / counties / cities / commercial trade bodies / academic associations.
2. **Map each to a domain.** Use `tools/google/tld_atlas.py` for known anchors. Add custom domains as needed.
3. **Fan out site-scoped queries.** `topic site:domain filetype:pdf` for each.
4. **Iterate the file types.** PDF for reports; XLSX/CSV for primary stats; DOC for working drafts.
5. **Subtract dominant noise.** `site:.gov.ke -site:tax.go.ke` to peel off a swamping sub-domain.

## Standard usage

```python
from tools.google import enumerate_stakeholders, stakeholder_query_bundle, GoogleSearchClient

stakeholders = enumerate_stakeholders(
    topic="hostel safety",
    country_focus=["KE", "UG", "TZ"],
    include_igos=True,
    include_us_states=False,
    extra_ngos=["hakijamii.com", "knchr.org"],
    extra_academic=["uonbi.ac.ke", "mak.ac.ug"],
)
queries = stakeholder_query_bundle(
    "hostel safety", stakeholders, file_types=["pdf", "xlsx"], quote_topic=True,
)

client = GoogleSearchClient()
for q in queries:
    for r in client.search(q, num=10):
        # Filter, dedupe, store
        ...
```

## Stakeholder categories (with anchor domains)

| Category | Domain anchors |
|---|---|
| IGO | `un.org`, `who.int`, `worldbank.org`, `imf.org`, `oecd.org` |
| Foreign government | `.gov.uk`, `.go.ke`, `.go.ug`, `.gouv.fr`, `.gov.cn` |
| US federal | `.gov`, `.mil`, `fs.fed.us` |
| US state | `.gov` per state, `state.XX.us` (legacy) |
| US county | `co.NAME.XX.us` |
| US city | `ci.NAME.XX.us` |
| NGO | `.org` (filter aggressively) |
| Academic | `.edu` (US), `.ac.ke`, `.ac.ug`, `.ac.tz`, `.ac.rw` |
| Trade association | sector-specific |
| Media (last resort) | `nation.africa`, `monitor.co.ug`, etc. |

## Brown's domain-subtraction trick

When one site swamps a federation domain:

```
site:.fed.us -site:fs.fed.us  →  reveals long tail by peeling off Forest Service
```

Same pattern for `site:.un.org -site:unhcr.org` etc.

## Decision rules

- **Always include IGOs** for any cross-border or development-economics topic.
- **Always include both `state.XX.us` AND `XX.gov`** for US state-level research (Brown: 4080 vs 7110 hits for the same query).
- **Use `filetype:xlsx` / `filetype:csv`** for primary statistics; numerical content has no keyword handle without it.
- **Use `filetype:pdf`** for reports, regulatory filings, policy briefs.
- **Translate the topic into the local language** before issuing `site:.tld` searches in non-English jurisdictions (companion skill: `translate-then-search`, roadmap).

## Anti-patterns

- Searching topic-only without stakeholder fan-out
- Using `www.` inside `site:` (silently undercounts)
- Trusting Google Web's date filter (only metadata-compliant pages have one)
- Single-domain reliance — every state has both modern and legacy domains
- Treating SERP rank as authority — Brown: tilde (`~`) in URL = personal site

## See also

- `tools/google/stakeholder.py` + `tld_atlas.py` — implementation
- `google-search-api-operator` — issuing the queries
- `discipline-router` — picks discipline-appropriate stakeholder categories
- `evidence-discipline` — every result still needs verification
