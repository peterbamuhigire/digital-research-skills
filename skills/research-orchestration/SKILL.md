---
name: research-orchestration
description: Use when starting or replanning a multi-source research project that needs a research-type choice, discipline strategy, reading mode, wave plan, verification, gap filling, and synthesis; use research-design for formal method design and research-techniques for one bounded technique.
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

| Input | Source/provider | If absent |
|---|---|---|
| Research goal, scope, audience, decision context, cohorts, constraints, source expectations, and desired output | Requester or project brief | Stop wave dispatch and define the missing framing |

## Workflow

1. Run the type, discipline, and reading-mode routers before wave dispatch.
2. Select companion skills for evidence discipline, research design, methods, source evaluation, and output form.
3. Dispatch planned waves, verify before merging, and reserve final synthesis for the orchestrator.
4. Stop when scope, evidence rules, or verification ownership is unresolved.
5. Recover from unavailable agents or providers by running sequentially and preserving unassessed gaps.

## Quality Standards

- Research waves must be scoped, source-aware, evidence-disciplined, and designed to produce insight rather than volume.

## Anti-Patterns

- Do not run a single mega-search when cohorts, source classes, or verification needs differ. Fix: split non-overlapping waves.
- Do not delegate cross-cohort synthesis to wave agents. Fix: reserve synthesis for the orchestrator.
- Do not merge an unverified wave. Fix: quarantine claims and schedule verification.
- Do not hide provider failure. Fix: label the gap and preserve the attempted path.
- Do not optimise speed at the expense of source diversity. Fix: keep a quality guardrail.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Wave plan, agent briefs, companion-skill route, verification plan, synthesis route, and output storage contract | Research team and orchestrator | Non-overlapping waves, evidence rules, verification ownership, and handoff are explicit |

## References

- Use the routers and companion-skill table below.
- Use `references/kaizen-research-loop.md` after each wave and before release.

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

## Article SEO and SERP evidence standard

Apply this standard before drafting any article, blog post, thought-leadership
piece, or other search-discoverable long-form content. Search visibility is a
research input, not evidence of a factual claim, and no research wave promises
a ranking, citation, traffic level, or search volume.

### Three-wave article study

1. **Wave 1 — intent and query map.** Define the reader, decision, market,
   language and page job. Build 3–7 related query clusters from buyer language,
   questions, geography and the decision the article must support. Record the
   date, provider/tool and exact queries. Collect up to five leading results per
   cluster using an approved search/API tool; do not scrape Google result pages
   directly and do not invent volume data.
2. **Wave 2 — top-five reading and gap map.** Read each accessible result in the
   chosen set, not only its snippet. Record the title, headings, format,
   audience, evidence, sources, local relevance, calls to action, strengths and
   missing reader jobs. Mark blocked, paywalled or otherwise unread results
   `UNASSESSED`; never treat a snippet as a verified source.
3. **Wave 3 — evidence-led synthesis.** Compare the result set by intent and
   content gap, then choose a defensible angle, outline, keyword map, internal
   links and answer-first sections. Verify every material fact against primary
   or otherwise authoritative sources. Separate a competitor pattern from a
   factual source, and record what remains unknown or needs later measurement.

### Required article research record

Store a dated record containing: market and language; decision and audience;
exact queries and clusters; provider and access date; five-result URLs per
cluster with read/blocked status; recurring competitor patterns; content and
AI-answer gaps; primary evidence sources; selected terms and intent; planned
outline/internal links; unresolved checks; and the limitation that rankings,
citations and volumes are not guaranteed. For bilingual work, run and record
the English and French query maps separately; translate intent, not just words.

Any article request routes through this standard before drafting. Social or
distribution copy supporting an article inherits its verified intent and source
map, but does not turn a competitor page into proof.

## Kaizen after every wave

Every wave must leave a short learning record: observation, reproducible baseline, one hypothesis, smallest reversible experiment, guardrail, result, failed-path result, and standardisation decision. Useful measures include source admission rate, verified-claim coverage, unresolved-claim count, contradiction count, duplicate-search rate, and time-to-verified-finding. These are measures to collect, not values to invent. If the experiment improves speed but weakens source diversity, independence, or verification coverage, reject it and preserve the prior standard.

## When to use

Trigger on:
- "Research X across [region]" — dispatch a Wave 1 sweep
- "Now do Y for [adjacent group]" — parallel Wave 1 on a new cohort
- "Do another thorough pass" — Wave 2 gap fill
- "Synthesise across cohorts" — Wave 4
- "Audit our research for what we missed" — Wave 3 + Wave 4

Do **not** use for: single-question lookups, fact-checks, or known-target reads.

## Wave Choice Rules

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

## Wave Failure Modes

- Single-shot research with one mega-prompt — produces shallow coverage, missing perspective splits
- Re-running Wave 1 instead of running Wave 2 — wastes context, duplicates known
- Delegating cross-cohort synthesis — only the orchestrator has all four cohort outputs in context
- Forgetting hard constraints in Wave-2 briefs — agent re-introduces excluded scope

## See also

- `research-techniques` — gap analysis, mini-analysis, crosswalk matrix, cross-cohort synthesis, reference interview, controlled vocabulary, search-operator grammar, pearl-growing, brachiation, etc. (load when a Wave needs a specific technique)
- `research-design` — historical methods, trend analysis, MROC, knowledge lifecycle, Universal Methods of Design router, research design document, report builder (load when the project needs formal design, design-method selection, or a final assembled report)
- `source-evaluation` — Wave-3 verification logic; mandatory pairing for every source
- `academic-writing`, `report-and-proposal-craft`, `business-writing` — output containers

## Orchestration detail inputs

| Input | Source/provider | If absent |
|---|---|---|
| Research question, decision, audience, scope, and deadline | Requester or project brief | Stop wave dispatch and return the missing framing fields. |
| Existing corpus, registries, and constraints | Project filesystem and source providers | Start with discovery; record unavailable sources as gaps. |

## Orchestrator outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Wave plan and agent briefs | Research team | Cohorts do not overlap, every brief has evidence rules, and verification/gap passes are scheduled. |
| Synthesis-ready evidence registry | Synthesiser | Claims, sources, contradictions, and gaps are traceable by cohort. |

## Evidence Produced

| Category | Artifact | Acceptance condition |
|---|---|---|
| Correctness | Wave checkpoint record | Each cohort reports sources, verification status, gaps, and unresolved conflicts. |

## Capability Contract

Planning and review are read-only. Delegation is permitted only when the runtime and task authorise it; external contact, publishing, spending, or destructive actions require explicit authority.

## Degraded Mode

Without delegation, network, or provider access, run waves sequentially and return the verified local result plus named gaps. Never collapse skipped verification into a pass.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Small bounded question | Use one research pass, then verify | Coordination overhead |
| Multiple independent cohorts | Dispatch non-overlapping briefs, then verify each wave | Duplicated effort |
| Contradictions remain | Hold synthesis and issue a gap-fill brief | False consensus |

## Worked Example

For a multi-region market question, assign one cohort per region, require the same comparison fields and evidence discipline, verify each checkpoint, then synthesise only reconciled claims.

## Wave workflow

1. Define the question, cohorts, deadline, and evidence standard; stop if scope is unresolved.
2. Select research type, discipline, reading mode, and non-overlapping wave briefs.
3. Run each wave and verify its checkpoint before the next.
4. Dispatch gap-fill work where evidence conflicts or coverage is incomplete.
5. Recover from unavailable agents or providers by running sequentially and preserving unassessed gaps.

## Wave anti-patterns

- Overlapping cohort briefs. Fix: assign exclusive boundaries.
- Synthesising before verification. Fix: gate each checkpoint.
- Omitting the evidence clause. Fix: include it verbatim.
- Treating no result as absence. Fix: report no source found.
- Hiding provider failure. Fix: mark it unassessed and recover sequentially.
