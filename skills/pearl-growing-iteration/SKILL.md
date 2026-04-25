---
name: pearl-growing-iteration
description: Use as the default search-iteration policy — run a broad query first, harvest controlled-vocabulary terms and adjacent concepts from the most on-target hits, then re-run a refined query. A two-pass policy strictly better than one-shot dispatch in unfamiliar domains. Adapted from Suzanne Bell, Librarian's Guide to Online Searching.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Pearl growing — iterative search refinement

A one-shot search assumes you already know the right vocabulary. In unfamiliar domains, you don't. Pearl growing makes ignorance an asset.

## The three-step loop

1. **Broad first pass.** Issue a deliberately under-specified query. Goal: surface 10–30 results that are at least partly on-topic.
2. **Harvest the vocabulary.** From the most on-target hits, extract: subject headings, controlled-vocabulary tags (MeSH, ERIC thesaurus terms, etc.), recurring author names, recurring institutions, terminology you didn't know existed, related-paper suggestions.
3. **Refined second pass.** Re-run with the harvested vocabulary. Often a different operator stack, different field restrictions, or different engine entirely.

Repeat until marginal value drops below the cost of another iteration.

## Decision rules

- **Two passes minimum.** A single search rarely finds what a researcher actually wants.
- **Harvest from refine-panel facets first** — top authors, journals, organisations, years. Free metadata, no reading required.
- **Read the most-cited 1–3 hits** before refining. Citation-rank works as importance proxy in early iterations.
- **Drop terms one at a time** if the broad pass returned nothing. Bell: "the biggest pitfalls in searching is not being willing to not look for a part of the information provided."
- **Broaden when sparse.** When a search returns few results, the right move is **fewer, broader** terms — not more, more-specific.
- **The search you start with is seldom the search you end up with.** Plan for it.

## Recall vs precision dial

Every query targets a point on this axis:

| Intent | Target | Strategy |
|---|---|---|
| Topic vetting (PhD lit-review) | Max recall | Broad terms, OR synonyms, no field restrictions |
| Hypothesis support (mid-paper) | Balanced | Phrase-quote core; OR synonyms; date limit |
| Single-fact lookup (citation needed) | Max precision | Phrase-quote; intitle; site:; date range |
| "I need a specific document I half-remember" | Fragment recovery | Use **single-citation-matcher** pattern |

Label every sub-query with its target on this dial.

## Anti-patterns

- One-shot dispatch in unfamiliar domains
- Adding more terms when broad search already returned too few
- Reading individual results before extracting aggregate vocabulary from refine panels
- Trusting the first set of harvested terms — vocabulary often shifts again on the third pass
- Treating "many results" as a quality signal — often just weak indexing
- Ignoring the controlled vocabulary the database provides for free

## Mental toolkit (Bell)

Three discipline rules for the iteration loop:

1. **Healthy skepticism** — assume user-provided info contains errors
2. **Willingness to let go** — drop pieces of provided info one at a time
3. **Mental clarity / one change at a time** — don't change three operators simultaneously and lose attribution of what worked

## See also

- `web-search-operator-grammar` — the operator layer beneath this loop
- `discipline-router` — picks which engine to iterate on
- `controlled-vocabulary-builder` — captures harvested vocabulary as a project asset
- `gap-analysis` — when iteration plateaus, gap-analysis reframes
