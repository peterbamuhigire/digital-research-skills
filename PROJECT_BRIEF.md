# PROJECT_BRIEF — digital-research-engine

## Mission

Build a **world-class research engine** — multi-agent, evidence-disciplined, portable across AI runtimes — that produces world-class research, status, intelligence, evaluation, and decision-support reports for diverse audiences and purposes.

This is not a document-generator. It is a research operating system. The Word document is one of many possible outputs.

## Audiences served

The engine produces work for distinct audiences with distinct standards:

- **Designers, product managers, founders** — pain-point and product research that informs new systems
- **Investors, M&A, lenders** — due-diligence and market-landscape research that informs capital decisions
- **Strategists, forecasters, planners** — trend research that informs scenario planning
- **Policy-makers, advocates, NGOs** — policy / regulatory research and single-cohort deep-dives
- **Journalists, researchers, academics** — historical research and OSINT
- **Security, integrity, brand teams** — OSINT and reputational research
- **Communications, brand, monitoring teams** — social-media and sentiment research
- **Internal decision-makers and external clients** — comparative / benchmarking research

Each audience has different tolerance for inference, different citation expectations, and different report shape requirements.

## Research types supported (15 types, 19 schemas)

The engine supports — and selects between — fifteen distinct research types. Four of them come in academic + popular variants, yielding nineteen report schemas in total.

### Investigative / analytical (11)
1. Pain-point research (multi-cohort)
2. Single-cohort deep-dive
3. Market / industry landscape
4. Comparative / benchmarking
5. Social-media / sentiment research
6. Due diligence
7. OSINT (open-source intelligence)
8. Product research
9. Historical research
10. Trends research
11. Policy / regulatory research

### Long-form scholarly outputs (4 types × 2 variants = 8 schemas)
12. Master's / honours thesis (academic | popular)
13. Paper / journal article (academic | popular long-form)
14. PhD dissertation (academic | popular book)
15. Essay (academic | popular)

Each maps to a specific orchestration approach, methodology skill set, and report schema (A–S). The `research-type-router` skill handles selection upfront before any sub-agent fires.

## Non-negotiable

**Anti-hallucination guardrail.** No claim, statistic, quote, name, court case, statute, organisation, or URL appears in any output unless traceable to a real source. The evidence-discipline reference inside `source-evaluation` takes precedence over every other rule in the engine. Each project keeps a running `EVIDENCE-AUDIT.md` log of caught fabrications, corrections, and verification status.

## Design principles

1. **Type-routing first.** Pick the research type before the first sub-agent fires.
2. **One cohort per agent.** Don't muddle perspectives in a single research wave.
3. **Plan in waves.** Broad sweep → gap fill → verification → synthesis.
4. **Synthesis is the orchestrator's job.** Never delegate it.
5. **Markdown is canonical.** Word docs are generated from markdown source.
6. **Tier every source.** A 5-level credibility ladder runs from peer-reviewed academic down to social-platform.
7. **Mark uncertainty explicitly.** "(synthesis)", "(inference)", "(paraphrased)", "(gap)".
8. **Skills are portable.** Every skill ships with `SKILL.md`, `README.md`, `CLAUDE.md`, `AGENTS.md`.
9. **Skill priority is fixed.** evidence-discipline first, always.
10. **Audience drives tone.** Internal-design tone is direct; client-deliverable tone is formal; due-diligence tone is legalistic; advocacy tone is evidence-heavy.

## Skill inventory (engine-native, post-consolidation)

The skills library has been consolidated since the original brief — see `README.md` for the current four-layer architecture and `docs/analysis/initial-evaluation/03-engine-current-state.md` for the inventory. Headline:

### Layer 1 — Discipline foundation
- `source-evaluation` — anti-hallucination clause + 5-tier credibility ladder + Burke pentad + Tudor twelve points + Silverman/Bellingcat
- `research-orchestration` — multi-wave dispatch
- `research-techniques` — search-craft library (mini-analysis, crosswalk, gap-analysis, controlled-vocabulary, pain-point taxonomy, search-operator grammar; **plus** MacLeod search-mastery + Russell search-literacy references)
- `research-design` — historical methods, trend analysis, MROC, knowledge-lifecycle, design-document, report-builder; **plus** case-study method (Hancock & Algozzine + Yin + Stake)
- `knowledge-productization` **[NEW]** — knowledge audit, reusable asset ladder, audience variants, monetization framing
- `data-quality-pipeline` — Walker 4-axis quality scoring
- `dataset-discovery-and-analysis` — Segnini 5-step + 30+ dataset hosts
- `web-scraping-foundations` + `scraping-engineering-python`

### Layer 2 — Investigation & method
- `due-diligence` — CRAWL + CARA, FATF EDD/CDD framework
- `osint-investigation` — civilian lawful OSINT (incl. MacLeod investigative-search; Bean OSINT doctrine + validation/anti-patterns)
- `pi-investigation` — licensed-PI workflows
- `primary-research` **[NEW]** — qualitative design, interviewing, observation, coding, credibility checks

### Layer 3 — Analytic discipline
- `analytic-tradecraft` **[NEW]** — ICD 203 + Heuer/Pherson SATs + Kent estimative + cognitive biases + sourcing & deception
- `academic-writing` — citation styles, originality, plagiarism, hedging; **plus** Morley *Academic Phrasebank* (rhetorical moves + reporting verbs + hedging device catalog)
- `consulting-delivery` **[NEW]** — issue trees, hypothesis-led workplans, stakeholder handling, implementation discipline

### Layer 4 — Output craft
- `executive-communication` **[NEW]** — Pyramid Principle + SCQA opener + action titles + ghost deck + Zelazny chart selection + executive-summary template
- `academic-reporting-standards` **[NEW]** — Brause practical-craft layer (invisible rules, chapter template, viva preparation) + EQUATOR formal-reporting layer (PRISMA/CONSORT/STROBE/MOOSE/GRADE/Cochrane/TOP). Built explicitly to the **Ivy / Oxford / Cambridge / LSE bar**.
- `data-visualization` **[NEW]** — perceptual rankings, chart-selection router, tables/maps, style-guide discipline, redesign
- `report-and-proposal-craft`, `business-writing`, `professional-word-output`, `python-document-generation`, `excel-spreadsheets`, `markdown-lint-cleanup`, `east-african-english`

Plus meta-skills (skill-writing, skill-composition-standards, skill-safety-audit, validation-contract, capability-matrix) and project-doc skills (doc-architect, spec-architect, manual-guide, project-requirements, update-claude-documentation).

### Initial self-evaluation (2026-04-26)

The engine ran a self-evaluation comparing its capabilities against the published standards of MBB consulting, Big 4 + analyst houses, U.S. IC tradecraft (ICD 203, Heuer/Pherson SATs, Sherman Kent), PI / investigative-journalism / academic-reporting standards. Result: 62/100 baseline → 65/100 after the 2026-04-26 build session shipped `executive-communication`, `analytic-tradecraft`, `academic-reporting-standards` (full skills) plus enhancements to `research-techniques`, `osint-investigation`, `academic-writing`, `research-design`. Projected ~89/100 after the 6-month roadmap. See `docs/analysis/initial-evaluation/`.

## Repository

https://github.com/peterbamuhigire/digital-research-skills

## Roadmap

- **v0.1** — engine scaffolded; first project (`east-africa-property-hostel`) complete through Wave 2; cross-cohort synthesis; EVIDENCE-AUDIT framework live.
- **v0.2** (current, 2026-04-26) — initial self-evaluation complete; analytic + output + academic-reporting layers shipped (`analytic-tradecraft`, `executive-communication`, `academic-reporting-standards`). Score: 65/100. See `docs/analysis/initial-evaluation/`.
- **v0.3** — Month-2 of roadmap: complete `tools/verification/`; institution-specific examination conventions (Cambridge / Oxford / LSE / Harvard / Yale / Princeton) into `academic-reporting-standards`.
- **v0.4** — Month-3 of roadmap: build `quantitative-modelling` skill + `tools/quant/` (Bain market-sizing triangulation, sensitivity, scenario, financial models).
- **v0.5** — Month-4 of roadmap: complete `tools/sanctions/` + stand up second project + expand primary-research templates from field use.
- **v0.6** — Month-5 of roadmap: build `knowledge-base` reuse layer + `peer-review-loop` skill + URL-liveness CI.
- **v0.7** — Month-6 of roadmap: deferred-tier skills (competitive-intel, multi-language, paywalled-database, cost-control); bake-off vs. McKinsey-style manual pass.

Target: **≥ 85 / 100** by end of 6-month roadmap. See `docs/analysis/initial-evaluation/05-implementation-roadmap.md` for sequencing.

## Engine status (2026-04-26)

| Aspect | Status |
|---|---|
| Engine skills | 30+ skills, consolidated into 4-layer architecture (foundation / investigation / analytic / output) |
| New engine-expansion skills | `primary-research`, `consulting-delivery`, `knowledge-productization`, `data-visualization` |
| Skill enhancements this session | `source-evaluation` (misinformation/bias checks), `analytic-tradecraft` (behavioral-science operations), `research-orchestration` (audience + decision routing), governance docs cleaned to canonical evidence path |
| Initial self-evaluation | Complete; 8 documents in `docs/analysis/initial-evaluation/`. Score 62 → 65 / 100. |
| First project | 4 cohorts × Wave 1 + Wave 2 (students/owners), Wave 1 + Wave 2 (landlords/tenants) |
| Word-document export | First draft generated (v1); next refresh after analytic + output + academic layers integration test |
| Evidence audit | Active; 0 hallucinations shipped; 4 corrections applied; 10 gaps logged |
| Books extracted into engine | 21 (Pass 1: 6; Pass 2: 6; Pass 3: 9 incl. Analyzing Intelligence, Pyramid Principle, MacLeod, Russell, Brause, Morley, Hancock & Algozzine, Bean) |
| Git | Initialised + committed; pushed to GitHub. v0.2 commit pending. |

Maintained by Peter Bamuhigire.

## Project kernel update (2026-04-26)

Engine v0.3 ships the project kernel described in
`docs/plans/engine-tune/01-project-kernel-implementation-plan.md`: workspace
scaffolding, `_context/` and `_registry/` contracts, deterministic validation
gates, status reporting, manifest-driven output assembly, evidence-pack export,
example projects, and `scripts/validate_engine.py`.
