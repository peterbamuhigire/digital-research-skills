---
name: research-orchestration
description: Use as the FIRST step on any new research project — picks the research type, the discipline strategy, the reading mode, and the wave dispatch. Carries the multi-agent orchestrator (planned waves), the type/discipline/reading routers as references, and the orchestrator-output contract. Routes to companion skills (academic-writing, source-evaluation, web-scraping-foundations, research-techniques, research-design) as needed.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Research Orchestration

<!-- dual-compat-start -->

## Use When

- Use as the first step on any non-trivial research project, planned research wave, multi-cohort investigation, gap-fill pass, verification pass, or synthesis pass.

## Do Not Use When

- Do not use for a single known fact lookup, URL check, or short target read that does not need orchestration.

## Required Inputs

- Research goal, scope, audience, decision context, cohorts, constraints, source expectations, and desired output.

## Workflow

- Run the type, discipline, and reading-mode routers before wave dispatch.
- Select companion skills for evidence discipline, research design, methods, source evaluation, and output form.
- Dispatch planned waves, verify before merging, and reserve final synthesis for the orchestrator.

## Quality Standards

- Research waves must be scoped, source-aware, evidence-disciplined, and designed to produce insight rather than volume.

## Anti-Patterns

- Do not run a single mega-search when cohorts, source classes, or verification needs differ.
- Do not delegate cross-cohort synthesis to wave agents.

## Outputs

- Wave plan, agent brief, companion-skill route, verification plan, synthesis route, and output storage contract.

## References

- Use the routers and companion-skill table below.

<!-- dual-compat-end -->

The first skill loaded on any research project. Decides what kind of research is being run, what discipline its language and sources come from, what reading mode each retrieved source warrants, and how to dispatch the work as planned waves.

## Step 0 — pick the type, the discipline, the reading mode

Before any wave fires, run three routers (each lives in `references/`):

| Router | Reference | What it returns |
|---|---|---|
| **Research type** | `references/research-type-router.md` | Type (market, OSINT, DD, academic, historical, trend, social, product, policy …), the report schema, and which other skills to load |
| **Discipline** | `references/discipline-router.md` | Discipline strategy (sciences / medicine / social sciences / humanities / numerical / law) — vocabulary, databases, citation behaviour, date semantics |
| **Reading mode** | `references/reading-mode-router.md` | Per source: narrative / meditative / scan / mastery / partial-mastery — prevents over-reading low-density sources and under-reading core ones |

Skipping these is the most common cause of research that produces volume but not insight.

## Companion-skill router (load in addition to this skill)

| Trigger | Load |
|---|---|
| Output is a paper / essay / thesis / dissertation | `academic-writing` |
| Output is a report / proposal / white paper | `report-and-proposal-craft` |
| Output is a short business artifact | `business-writing` |
| Output must read like consulting-grade problem solving | `consulting-delivery` + `executive-communication` |
| Research includes interviews, observation, focus groups, or coded qualitative evidence | `primary-research` |
| Research must be reused across multiple deliverables or monetized into offers / IP | `knowledge-productization` |
| Output depends on charts, tables, maps, or dashboards carrying part of the argument | `data-visualization` |
| Open-source recon | `osint-investigation` |
| Corporate / financial vetting | `due-diligence` |
| Licensed-PI workflow | `pi-investigation` |
| Source vetting (always) | `source-evaluation` |
| Web data needed | `web-scraping-foundations` |
| Specific technique (gap analysis, brachiation, pearl-growing, crosswalk, mini-analysis, search-operator grammar, controlled vocabulary, etc.) | `research-techniques` |
| Formal research design (historical method, trend analysis, MROC, knowledge-lifecycle, Universal Methods of Design router, design document, report builder) | `research-design` |
| Dataset discovery / quality | `data-quality-pipeline`, `dataset-discovery-and-analysis` |

## The wave model

A research engine never runs as a single search. It runs as **planned waves**:

1. **Wave 1 — broad sweep.** One agent per cohort, broad query, ~50 sources target.
2. **Wave 2 — gap fill.** Specific gaps each Wave 1 agent flagged; deeper academic + regulatory sources.
3. **Wave 3 — verification.** Cross-source triangulation; verbatim-quote extraction; URL liveness check.
4. **Wave 4 — synthesis.** Cross-cohort patterns; product/policy inferences.

This skill defines when each wave fires and how outputs are stored.

## When to use

Trigger on:
- "Research X across [region]" — dispatch a Wave 1 sweep
- "Now do Y for [adjacent group]" — parallel Wave 1 on a new cohort
- "Do another thorough pass" — Wave 2 gap fill
- "Synthesise across cohorts" — Wave 4
- "Audit our research for what we missed" — Wave 3 + Wave 4

Do **not** use for: single-question lookups, fact-checks, or known-target reads.

## Decision rules

- **One cohort per agent.** Don't ask one agent to research students AND landlords. Split.
- **Run waves in parallel where independent.** A student-side gap-fill and an owner-side gap-fill have no shared state — fire them simultaneously.
- **Cap each agent at ~50 distinct sources.** Past that, marginal value drops sharply; better to fire a Wave-2 agent.
- **Never delegate synthesis to research agents.** The orchestrator (you) does the synthesis. Research agents return raw findings, not conclusions.
- **Always brief the agent on what's already known.** Wave-2 agents must see Wave-1 themes so they don't re-confirm; they're paid to find new material.

## Standard agent brief structure

Every research-agent prompt should contain:

1. **Goal** — one sentence
2. **Scope** — geography, cohort, time-window
3. **Audience / decision context** — who will use it and what decision it must support
4. **Out-of-scope** — what NOT to research (avoids duplicate work)
5. **Themes to cover** — explicit numbered list
6. **Sources to mine** — named outlets, repositories, platforms
7. **Deliverable shape** — markdown sections, source-count target, quote requirements
8. **Hard constraints** — exclusions (e.g., "do NOT cover topic X"), language, format

If the brief is missing any of those, the output will be uneven.

## Orchestrator outputs

After each wave, the orchestrator writes:

- `<cohort>/research/pain-points-report.md` (or `complaints-report.md` for student-style cohorts)
- `<cohort>/research/sources.md` — annotated source list with gaps section
- `<cohort>/research/quotes.md` — verbatim quotes
- `<cohort>/analysis/themes.md` — sub-theme taxonomy
- `<cohort>/analysis/by-country.md` (or by-segment, depending on dimension)
- `<cohort>/opportunities/product-ideas.md`

Wave 2 outputs append a `# Pass 2 — Gap-fill addendum` section to the existing files rather than overwrite.

## Anti-patterns

- Single-shot research with one mega-prompt — produces shallow coverage, missing perspective splits
- Re-running Wave 1 instead of running Wave 2 — wastes context, duplicates known
- Delegating cross-cohort synthesis — only the orchestrator has all four cohort outputs in context
- Forgetting hard constraints in Wave-2 briefs — agent re-introduces excluded scope

## See also

- `research-techniques` — gap analysis, mini-analysis, crosswalk matrix, cross-cohort synthesis, reference interview, controlled vocabulary, search-operator grammar, pearl-growing, brachiation, etc. (load when a Wave needs a specific technique)
- `research-design` — historical methods, trend analysis, MROC, knowledge lifecycle, Universal Methods of Design router, research design document, report builder (load when the project needs formal design, design-method selection, or a final assembled report)
- `source-evaluation` — Wave-3 verification logic; mandatory pairing for every source
- `academic-writing`, `report-and-proposal-craft`, `business-writing` — output containers
