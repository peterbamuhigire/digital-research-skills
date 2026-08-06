# digital-research-engine

See [`docs/control-plane-adoption.md`](docs/control-plane-adoption.md) for
research agents, thin commands, evidence/currentness hooks, citation gates,
and resumable handoffs.

A **world-class research operating system** — multi-agent, evidence-disciplined, portable across AI runtimes — that produces research, status, intelligence, evaluation, and decision-support reports for diverse audiences and purposes.

This is not a document-generator. It is a skills engine that runs investigations, applies discipline, and produces the right report shape for the right audience.

> **Repository:** https://github.com/peterbamuhigire/digital-research-skills

## Architecture & cross-cutting engines (updated 2026-06-21)

This engine no longer relies on native skill discovery — **no engine on this machine is natively discovered anymore.** Every engine, including this one, is consulted through the global routing table by globbing its `SKILL.md` files and reading them directly (resolve each engine's path per-device from the routing table; never assume an absolute path). Consult these cross-cutting engines **in addition** to this one:

- **`design-system-skills`** — the single home for ALL design, typography, UI/UX, visual-identity, and visual-formatting skills, plus the **visual/typographic** anti-AI-slop doctrine. **Referenced, not mirrored** — resolve its path per-device. As of 2026-06-21 this engine's **`data-visualization` skill migrated out into `design-system-skills`**, which now holds the canonical, more complete copy. This engine **references** `design-system-skills` for all canonical font/typography/colour/chart doctrine rather than holding its own.
- **`chwezi-accounting-doctrine`** — cross-cutting finance/accounting engine. **Referenced, not mirrored.** Consult for any financial-statement, valuation, or budget work alongside this engine.

**What stays here:** the *textual* anti-AI-slop discipline. `anti-ai-slop` (real-time guardrail) and `ai-slop-audit` (per-iteration auditor, grades A/B/C/F, F blocks delivery) remain core to this engine — textual slop (clichés, hedging, preambles, voiceless template prose) is this engine's domain. **Visual/typographic** slop is the design engine's domain. When a deliverable needs charts or visual formatting, the evidence and narrative stay here and route their visual build to `design-system-skills`.

## What this engine does

Given a research question, the engine runs:

1. **Wave 1** — broad sweep (multiple parallel sub-agents, one per cohort)
2. **Wave 2** — targeted gap-fill on what Wave 1 missed
3. **Wave 3** — verification (URL liveness, statistic re-check, quote confirmation)
4. **Wave 3.5** — peer-review / structured analytic technique pass (ACH, KAC, Pre-Mortem) where a forward-looking judgment ships
5. **Wave 4** — cross-cohort synthesis and product-opportunity mapping
6. **Output** — Pyramid-Principle-structured executive artefact OR EQUATOR-compliant academic artefact, generated from versioned markdown source

## Non-negotiable rule

> **The AI agents in this engine MUST NOT hallucinate.** No statistic, quote, name, court case, statute, organisation, or URL appears in any output unless traceable to a real, verified source. See `skills/source-evaluation/SKILL.md` — the engine's evidence-discipline clause. It precedes every other skill.
>
> **And the agents MUST NOT produce AI slop.** Truth is necessary but not sufficient: a fully-sourced report can still read as generic, voiceless, template-extruded slop. `skills/anti-ai-slop/SKILL.md` is the real-time quality guardrail applied to every output; `skills/ai-slop-audit/SKILL.md` runs after each major iteration and as the ship gate, grading the artefact A/B/C/F. Every report must read as if a professional human researcher wrote it.

## The four operating layers

The engine's skills compose into four layers:

```
Layer 4 — OUTPUT CRAFT
          executive-communication (Pyramid + Zelazny)
          academic-reporting-standards (Brause + EQUATOR)
          [data-visualization → migrated to design-system-skills 2026-06-21]
          report-and-proposal-craft, business-writing
          professional-word-output, python-document-generation

Layer 3 — ANALYTIC DISCIPLINE
          analytic-tradecraft (ICD 203 + Heuer/Pherson SATs + Kent estimative + biases)
          academic-writing (citation, originality, plagiarism)
          consulting-delivery (issue trees + workplans + stakeholder handling)

Layer 2 — INVESTIGATION & METHOD
          due-diligence, osint-investigation, pi-investigation
          research-design, research-techniques, primary-research

Layer 1 — DISCIPLINE FOUNDATION
          source-evaluation (5-tier ladder, Burke pentad, Tudor 12-pt, Silverman)
          research-orchestration (wave dispatch)
          knowledge-productization (knowledge audit + asset ladder + audience variants)
          data-quality-pipeline, dataset-discovery-and-analysis
          web-scraping-foundations, scraping-engineering-python
```

## Skills inventory (current)

```
skills/
├── source-evaluation/                  Layer 1 — anti-hallucination + 5-tier credibility
├── anti-ai-slop/             [NEW]      Layer 1 — real-time quality guardrail (the slop counterpart to evidence-discipline)
├── ai-slop-audit/            [NEW]      Layer 1 — per-iteration slop auditor; grades A/B/C/F; F blocks delivery
├── research-orchestration/             Layer 1 — wave dispatch, multi-agent coordination
├── research-techniques/                Layer 1 — search craft (incl. MacLeod + Russell references)
├── research-design/                    Layer 1 — historical, trend, MROC, design-doc, report-builder
├── knowledge-productization/           Layer 1 — knowledge audit, asset ladder, monetization
├── data-quality-pipeline/              Layer 1 — Walker 4-axis quality scoring
├── dataset-discovery-and-analysis/     Layer 1 — Segnini 5-step + 30+ dataset hosts
├── web-scraping-foundations/           Layer 1 — decision tree, parser choice, error taxonomy
├── scraping-engineering-python/        Layer 1 — concurrent, caching, Playwright
│
├── due-diligence/                      Layer 2 — CRAWL + CARA, FATF EDD/CDD framework
├── osint-investigation/                Layer 2 — civilian lawful OSINT (incl. MacLeod investigative)
├── pi-investigation/                   Layer 2 — licensed PI workflows
├── primary-research/        [NEW]      Layer 2 — interviews, observation, coding, credibility
│
├── analytic-tradecraft/    [NEW]       Layer 3 — ICD 203 + Heuer/Pherson SATs + Kent estimative
├── academic-writing/                   Layer 3 — citation, originality, plagiarism, hedging
├── consulting-delivery/     [NEW]      Layer 3 — issue trees, workplans, clients, implementation
├── online-legal-research/   [NEW]      Layer 3 — primary/secondary authority, IRAC, citators, EA overlay
├── systems-thinking-and-mental-models/ [NEW] Layer 3 — systemigrams, causal loops, mental models, decision science
├── mind-mapping-and-synthesis/ [NEW]   Layer 3 — Buzan method + Mermaid mindmap patterns for synthesis
│
├── executive-communication/  [NEW]     Layer 4 — Pyramid + SCQA + action titles + Zelazny
├── academic-reporting-standards/ [NEW] Layer 4 — Brause + PRISMA/CONSORT/STROBE/MOOSE/GRADE/Cochrane/TOP
│   (data-visualization MIGRATED OUT → design-system-skills 2026-06-21; canonical copy lives there)
├── report-and-proposal-craft/          Layer 4 — long-form scaffolding
├── business-writing/                   Layer 4 — email, memo, letter, blog, proposal
├── professional-word-output/           Layer 4 — .docx generation + branding
├── python-document-generation/         Layer 4 — programmatic .docx/.xlsx/.pdf
├── excel-spreadsheets/                 Layer 4 — worksheet construction
├── markdown-lint-cleanup/              Layer 4 — style-guide enforcement
├── east-african-english/               Layer 4 — regional style
│
├── (skill-building meta-skills)
├── skill-writing/, skill-composition-standards/, skill-safety-audit/
├── validation-contract/, capability-matrix/
│
└── (project-documentation meta-skills)
    doc-architect/, spec-architect/, manual-guide/, project-requirements/
    update-claude-documentation/
```

## Tools (`tools/`)

```
tools/
├── scraping/        HTTP client, throttle, robots, retry, cache, pagination, headless
├── data/            dq_score (Walker 4-axis), profiler, outlier panel, tidy check, encoding repair
├── academic/        citation density, originality, plagiarism, hedging, paraphrase
├── google/          CSE / SerpAPI client, stakeholder enumeration, TLD atlas (scaffolded)
├── verification/    EXIF, archive, reverse-image, provenance (mostly stub — Month-2 build)
├── dd/              Adverse media, UBO, registry atlas, identity triangulator (scaffolded)
├── pi/              Chain of custody, photo log, surveillance log
├── sanctions/       OFAC/UN/EU watchlists (Month-4 build)
├── registry/        Jurisdiction registry connectors (Month-4 build)
└── datasets/        Federated dataset search across 30+ public hosts
```

See `tools/README.md` for full layout and dependency baseline.

## Research-craft foundations

The engine's design is grounded in canonical works on research, search, knowledge management, scraping, verification, intelligence analysis, and academic writing:

**Pass 1 — research methodology**
1. *Internet Research with Google* — Amanda Deason
2. *Essentials of Knowledge Management* — Bryan Bergeron
3. *Librarian's Guide to Online Searching* (4th ed.) — Suzanne S. Bell
4. *Digital Paper* — Andrew Abbott
5. *The Handbook of Online and Social Media Research* — Ray Poynter
6. *The Creative Guide to Research* — Robin Rowland

**Pass 2 — scraping + verification**
7. *Harnessing the Power of Google* — Christopher C. Brown
8. *Verification Handbook for Investigative Reporting* — Craig Silverman et al.
9. *Web Scraping with Python* — Richard Lawson
10. *The Ultimate Guide to Web Scraping* — Hartley Brody
11. *Hands-On Website Scraping with Python*
12. *Python Web Scraping for Developers* — Oxylabs

**Pass 3 — analytic tradecraft, output craft, academic discipline, search mastery**
13. *Analyzing Intelligence: Origins, Obstacles, and Innovations* — Roger Z. George & James B. Bruce (eds.)
14. *The Minto Pyramid Principle* — Barbara Minto
15. *Say It With Charts* — Gene Zelazny
16. *How to Find Out Anything* — Don MacLeod
17. *The Joy of Search* — Daniel M. Russell
18. *Writing Your Doctoral Dissertation: Invisible Rules for Success* — Rita S. Brause
19. *The Academic Phrasebank* (4e) — John Morley
20. *Doing Case Study Research* — Hancock & Algozzine
21. *No More Secrets: Open Source Information and the Reshaping of U.S. Intelligence* — Hamilton Bean

**Pass 4 — primary research, consulting craft, knowledge productization, visualization**
22. *Qualitative Research & Evaluation Methods* — Michael Quinn Patton
23. *Intelligence Analysis for Tomorrow* — National Research Council
24. *True or False: A CIA Analyst's Guide to Spotting Fake News* — Cindy L. Otis
25. *Complete Guide to Knowledge Management* — JoAnn T. Hackos
26. *Knowledge Management and Business Strategies*
27. *Essential Tools for Management Consulting* — Simon Burtonshaw-Gunn
28. *Inside the Minds: Leading Consultants*
29. *McKinsey Mind* — Rasiel & Friga
30. *The McKinsey Edge* — Shu Hattori
31. *Better Data Visualizations* — Jonathan Schwabish
32. *Rewired* — McKinsey

See `RESEARCH_CRAFT_INTEGRATION.md` for the per-book → engine-skill mapping.

## Initial evaluation (2026-04-26)

The engine ran a self-evaluation — dogfooding the orchestration model on itself — comparing its current capabilities against the published standards of McKinsey / Bain / BCG, Big 4 + Gartner / Forrester / IDC, U.S. intelligence-community analytic tradecraft (ICD 203, Heuer/Pherson SATs), PI / investigative-journalism / academic-reporting standards (ASIS, ICIJ, OCCRP, PRISMA, CONSORT, STROBE, MOOSE, GRADE, Cochrane, TOP).

Result: **62 / 100 baseline → 65 / 100 after the 2026-04-26 build session** that shipped `executive-communication`, `analytic-tradecraft`, `academic-reporting-standards` (full skills) plus enhancements to `research-techniques` and `osint-investigation`. This repository revision extends that path with `primary-research`, `consulting-delivery`, and `knowledge-productization`. (`data-visualization`, shipped in an earlier revision, was migrated out to `design-system-skills` on 2026-06-21 — see **Architecture & cross-cutting engines** above.)

See `docs/analysis/initial-evaluation/` — eight documents:
- `00-executive-summary.md`, `01-methodology.md`, `02-benchmark-standards.md`, `03-engine-current-state.md`, `04-recommendations.md`, `05-implementation-roadmap.md`, `06-scorecard.md`, `99-sources.md`, plus `research-inputs/` for traceability.

## 15 research types supported (19 schemas — 4 types come in academic + popular variants)

### Investigative / analytical (11)
1. Pain-point research (multi-cohort) → Schema A
2. Single-cohort deep-dive → Schema B
3. Market / industry landscape → Schema C
4. Comparative / benchmarking → Schema D
5. Social-media / sentiment research → Schema E
6. Due diligence → Schema F
7. OSINT → Schema G
8. Product research → Schema H
9. Historical research → Schema I
10. Trends research → Schema J
11. Policy / regulatory research → Schema K

### Long-form scholarly outputs (4 types × 2 variants = 8 schemas)
12. Master's / honours **thesis** — academic (L) | popular (M)
13. **Paper** / journal article — academic (N) | popular long-form (O)
14. PhD **dissertation** — academic (P) | popular book (Q)
15. **Essay** — academic (R) | popular (S)

Variant rules: thesis / dissertation default to academic; paper defaults to academic; essay must be specified by the user. Academic outputs (L–S academic variants) are subject to the **Ivy / Oxford / Cambridge / LSE bar** encoded in `academic-reporting-standards`.

## Cross-tool compatibility

Every skill ships with:
- `SKILL.md` — canonical instructions (Claude + generic)
- `README.md` — human-readable overview
- `CLAUDE.md` — Claude-Code-specific notes
- `AGENTS.md` — Codex / generic-agent notes
- `references/` — deep-dive references

## How to start a new project

1. `mkdir projects/<project-id>/`
2. Add `README.md`, `CLAUDE.md`, `EVIDENCE-AUDIT.md` to the project
3. Define cohorts (sub-projects) — typically 1–4 named populations being researched
4. For each cohort, run `research-orchestration` Wave 1
5. After waves complete, run cross-cohort synthesis
6. Apply `analytic-tradecraft` to any forward-looking judgment in the synthesis
7. Apply `executive-communication` (executive deliverable) or `academic-reporting-standards` (thesis / paper)
8. Generate the final document via `professional-word-output` or `python-document-generation`
9. End product: `projects/<project-id>/report-v<N>-<date>.docx`

## Kernel workflow

New projects are managed as kernel workspaces under `projects/<project-id>/`.

Golden path:

1. `python -m engine doctor`
2. `python -m engine new-project "<name>" --type "<research-type>" --audience "<audience>" --variant "<variant>"`
3. Run `00-meta-initialization` and complete `_context/`
4. Execute research waves under evidence discipline
5. `python -m engine sync <project-id>`
6. `python -m engine status <project-id>`
7. `python -m engine validate <project-id>`
8. `python -m engine assemble <project-id> <output-family>`
9. `python -m engine pack <project-id> --out export/<project-id>.zip`

The canonical workspace contract is documented in `docs/pathing-model.md`.
Output manifests are documented in `docs/output-manifests.md`. Release packs are
documented in `docs/release-pack-spec.md`. Legacy migration notes are in
`docs/migration-notes.md`. Candidate OSINT tool indexing is documented in
`docs/osint-tool-index.md`.

Optional OSINT toolkit ingestion:

```powershell
python -m engine index-osint-tools <project-id> <url>
```

Repo-level validation:

```powershell
python -X utf8 scripts\skill_contract_validator.py --baseline tests\skill-engine\quality-baseline.json
python -X utf8 scripts\routing_smoke_test.py
python -X utf8 scripts\validate_engine.py
```

## Current projects

- **`projects/east-africa-property-hostel/`** — pain points across students, hostel owners, residential landlords, and ordinary tenants in Uganda, Kenya, Tanzania, Rwanda, Burundi, South Sudan. 250+ sources across 4 cohorts; first project to ship at engine-grade evidence discipline.

## Status

The source-currentness adapter is `scripts/validate_source_currency.py`.
It fails closed for missing verification/review metadata and overdue
time-sensitive sources before a current claim can be released.

Engine v0.2 — initial self-evaluation complete; analytic + output + academic-reporting layers shipped. First project complete through Wave 2 on student & owner cohorts; Wave 1 on landlord & tenant cohorts. Final Word document not yet generated. See `docs/analysis/initial-evaluation/05-implementation-roadmap.md` for the next-six-months build plan.

## Kernel status

Engine v0.3 - project kernel implemented. The repo now has workspace
scaffolding, `_context/` and `_registry/` contracts, deterministic validation
gates, manifest-driven output assembly, evidence-pack export, three example
projects, and a repo-level validator. See
`docs/plans/engine-tune/01-project-kernel-implementation-plan.md`.

## July 2026 upgrade status

The July 2026 engine has 58 active skills discovered below `skills/`; the
`skills/proposal-skills` Git submodule is a separate engine. Each active skill
follows the portable authoring contract in `docs/skill-authoring-standard.md`.
The zero-debt baseline, routing fixtures, and push/pull-request CI prevent
contract or routing regressions. The conformance record is in
`docs/engine-upgrade-july-2026/conformance-normalisation.md`; the earlier
capability upgrade remains documented in `FINAL-UPGRADE-REPORT.md`.

Validation status:

```powershell
python -X utf8 scripts\skill_contract_validator.py --baseline tests\skill-engine\quality-baseline.json
python -X utf8 scripts\routing_smoke_test.py
python -X utf8 scripts\validate_engine.py
```

The release gate covers all 58 active skills, routing fixtures, the engine doctor,
and kernel unit tests. Project workspaces are intentionally untracked; validate a
local workspace separately with `python -m engine validate <project-id>`.

Maintained by Peter Bamuhigire.

## Book-derived 2026 capability upgrade

LEAN, Applying the Kaizen in Africa, Facility Move Playbook, Platform Enterprise, Designing for
AI, and MSC Software Magazine strengthen research orchestration with hypothesis/experiment/evidence
loops, source freshness, uncertainty, claim graphs, reproducibility, process learning, and
research-product audits. Historical, partial, corrupted, or unreadable inputs remain explicitly
labelled and cannot masquerade as current standards.

## Kaizen and product-audit contract

The research cycle is `Observe -> Baseline -> Select -> Experiment -> Check -> Standardise ->
Teach -> Re-measure`. Research-engine and research-product audits publish `min(raw_score, 65)` and
produce 95/100 plans with evidence, owner, measure, risk, rollback, and re-audit. This engine is
the portfolio route for current or uncertain claims, including legal, regulatory, tax, market,
security, safety, platform, vendor, and scientific claims. See `docs/continuous-improvement/` and
`skills/00-meta-initialization/references/kaizen-engine-and-product-audit.md`.
