---
name: research-techniques
description: Use when a research project needs a specific named technique — mini-analysis, crosswalk matrix, cross-cohort synthesis, gap analysis, reference interview, controlled vocabulary, pain-point taxonomy, search-operator grammar, Google-search API. Companion to research-orchestration; load only the technique the situation demands.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Research Techniques

Library of named research techniques the engine applies on demand. The orchestrator (`research-orchestration`) decides *what kind* of research is being run; this skill provides the *specific tools* used inside the waves.

## When to use

The orchestrator (or another skill) tells you the project needs a named technique. Load only the matching reference. Do not load all references by default.

## Technique router

| Need | Reference | One-line description |
|---|---|---|
| Decompose a big question into smaller answerable analyses | `references/minianalysis-engine.md` | Abbott's brachiation — every research question broken into mini-analyses |
| Compare findings across heterogeneous source types | `references/crosswalk-matrix.md` | Sources × dimensions matrix to surface gaps and contradictions |
| Synthesize across cohorts / segments / regions | `references/cross-cohort-synthesis.md` | Wave-4 work: cross-cohort patterns, divergences, product/policy inferences |
| Identify what the existing literature has not answered | `references/gap-analysis.md` | Feeds Wave-2 brief construction; structures missing-evidence calls |
| Interview a librarian / SME / archivist for the right starting points | `references/reference-interview.md` | Bell's reference-interview discipline; reframes vague queries |
| Build a vocabulary the engine can reuse (subject headings, synonyms, related terms) | `references/controlled-vocabulary-builder.md` | Bell + Bergeron; precision-recall dial |
| Build a taxonomy of pain points / complaints / use cases from raw qualitative data | `references/pain-point-taxonomy.md` | Code → cluster → name → counts → exemplar quotes |
| Master Google / Bing / archive search operators | `references/search-operator-grammar.md` | site:, intitle:, inurl:, filetype:, before:, after:, allintext:, around:, exact phrase, exclusion, OR/AND |
| Programmatic search via Google CSE / Bing Web Search APIs | `references/google-search-api-operator.md` | API setup, query budget, JSON parsing, rate limits |
| MacLeod's full search-mastery layer — operator catalog, deep-web heuristics, anti-patterns, "never compile what's already compiled" | `references/macleod-search-mastery.md` | Don MacLeod, *How to Find Out Anything* (Tier 1) |
| Russell's metacognitive layer — clarify the question, lateral reading, knowing when to stop, triangulation standards, leading-question lint | `references/russell-search-literacy.md` | Daniel M. Russell, *The Joy of Search* (Tier 1) |

## Orchestration

```
new research wave
├─ load research-orchestration (decides type/discipline/reading mode + wave plan)
├─ if Wave-2 gap fill needed
│   └─ load references/gap-analysis.md
├─ if a question is too big for one analysis
│   └─ load references/minianalysis-engine.md
├─ if the source set is heterogeneous (academic + media + government + interview)
│   └─ load references/crosswalk-matrix.md
├─ if multi-cohort synthesis required
│   └─ load references/cross-cohort-synthesis.md
├─ if vague query needs reframing
│   └─ load references/reference-interview.md
├─ if precision/recall tuning matters
│   └─ load references/controlled-vocabulary-builder.md
└─ when issuing search queries
    ├─ load references/search-operator-grammar.md (manual)
    └─ load references/google-search-api-operator.md (programmatic)
```

## Universal rule — every technique outputs structured artifacts

Every technique in this skill produces an artifact the orchestrator can consume:

- mini-analysis → list of sub-questions, evidence-per-sub, mini-conclusion.
- crosswalk matrix → table (sources × dimensions) with cell entries.
- cross-cohort synthesis → patterns, divergences, inferences.
- gap analysis → list of named gaps with evidence-of-absence.
- reference interview → reframed query + recommended starting points.
- controlled vocabulary → preferred terms + synonyms + related terms + scope notes.
- pain-point taxonomy → coded clusters with exemplar quotes and counts.
- search query → operator-rich string + estimated result-set characteristics.

A technique that does not produce a structured artifact has been used incorrectly.

## Anti-patterns

- Loading all references at once instead of the matching one.
- Using a search-operator grammar reference to write English prose.
- Inventing pain points; the taxonomy must be built from coded raw data only.
- Synthesizing across cohorts before each cohort has its own complete corpus.
- Treating gap analysis as "things I haven't read yet"; gap analysis names what the *literature* has not answered.

## Companion skills

- `research-orchestration` — the dispatcher; this skill is its toolbox.
- `research-design` — formal research design (historical, trend, MROC, knowledge lifecycle, design document, report builder).
- `source-evaluation` — mandatory pairing whenever sources are involved.
- `academic-writing`, `report-and-proposal-craft`, `business-writing` — output containers.
