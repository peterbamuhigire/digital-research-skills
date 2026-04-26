# 03 — Engine Current State Inventory

**Date:** 2026-04-26
**Method:** `Explore` sub-agent walked `skills/`, `tools/`, `projects/`, `extracted-books/`, root governance docs.

---

## 1. Skills inventory

The engine ships ~30 native skills + borrowed/imported skills. Grouped by function:

### 1.1 Core research-discipline skills (Tier-1 — always loaded)

| Skill | Status | Notes |
|---|---|---|
| `source-evaluation` | 🟢 Strong | 5-tier credibility ladder, Burke pentad, Tudor twelve points, Silverman/Bellingcat. Carries the engine's anti-hallucination clause. |
| `research-orchestration` | 🟡 Mid | Wave 1–4 lifecycle defined. Missing: cost / token-budget guidance; resource-budgeting; explicit stop-rules beyond Wave-2 gap-fill. |
| `research-techniques` | 🟢 Strong | Nine techniques (mini-analysis, crosswalk, synthesis, gap, interview, vocabulary, pain-point taxonomy, search operators, Google API). Each with structured outputs. |
| `data-quality-pipeline` | 🟢 Strong | Walker 4-axis (completeness, usefulness, reliability, relevance). Backed by `tools/data/dq_score.py`. |
| `dataset-discovery-and-analysis` | 🟢 Strong | Segnini 5-step profile; ~30 dataset hosts queried. |
| `validation-contract` | 🟢 Present | 7-evidence categories per skill. |

### 1.2 Domain skills (Tier-2 — load by research type)

| Skill | Status | Notes |
|---|---|---|
| `due-diligence` | 🟡 Mid | CRAWL + CARA frameworks. References mostly stub. No live sanctions / registry integration. |
| `osint-investigation` | 🟡 Mid | Six named references; lawful-only + PI-licence awareness. Practical workflow patterns thin. |
| `pi-investigation` | 🟡 Mid | McMahon 10-section structure; chain-of-custody. Assumes licensure enforced upstream. |
| `research-design` | 🟡 Thin | Outlines historical methods, trend, MROC, design-document. Many references stubs. |

### 1.3 Output / writing skills

| Skill | Status | Notes |
|---|---|---|
| `academic-writing` | 🟢 Strong | Plagiarism prevention; citation styles L/N/P/R; originality gate. Borrowed. |
| `business-writing` | 🟢 Strong | Email, memo, letter, blog, fundraising, speech, resume. Borrowed. |
| `report-and-proposal-craft` | 🟡 Mid | Reports, proposals, white papers; SCQA spine. |
| `professional-word-output` | 🟢 Strong | `.docx` generation, styling, branding. ~415 lines. |
| `python-document-generation` | 🟢 Strong | `.docx` / `.xlsx` / `.pdf` from Python. ~324 lines. |
| `excel-spreadsheets` | Present | Worksheet construction; formula discipline. |
| `markdown-lint-cleanup` | Present | Style-guide enforcement. |

### 1.4 Search / scraping craft

| Skill | Status | Notes |
|---|---|---|
| `web-scraping-foundations` | 🟡 Mid | Decision tree, parser choice, error taxonomy. ~80% complete. |
| `scraping-engineering-python` | 🟡 Mid | Concurrent downloads, caching, form interaction, Playwright. ~75% complete. |

### 1.5 Meta / governance

| Skill | Status |
|---|---|
| `skill-writing` | 🟢 Strong |
| `skill-composition-standards` | 🟢 Strong |
| `skill-safety-audit` | 🟢 Present |
| `capability-matrix` | 🟢 Present |
| `doc-architect`, `spec-architect` | Present |
| `manual-guide`, `update-claude-documentation` | Present |
| `east-african-english` | Present (regional style) |

---

## 2. Tools inventory (`tools/`)

| Subdir | Maturity | Notes |
|---|---|---|
| `scraping/` | 🟡 60% | http_client, cache, headless, pagination, robots, throttle. Foundational; not production-ready for high-concurrency. |
| `data/` | 🟢 80% | dq_score (Walker 4-axis), profiler, outlier_panel, tidy_check, encoding_repair. Strongest area. |
| `verification/` | 🔴 30% | exif, reverse_image, archive, provenance — mostly stubs. Critical gap given Silverman/Bellingcat methodology. |
| `academic/` | 🟢 85% | Citation density, hedging, originality, paraphrase, quotes, reporting verbs, banned phrases. Mature. |
| `google/` | 🟡 40% | search_api, stakeholder, tld_atlas — mostly scaffolding. |
| `dd/` | 🟡 40% | adverse_media, ubo, registry_atlas, foreign_extensions, identity_triangulator — outlines, no live integrations. |
| `pi/` | 🟡 50% | chain_of_custody, photo_log, surveillance_log. |
| `sanctions/` | 🔴 20% | No live OFAC / UN / EU watchlist integration. |
| `registry/` | 🔴 20% | No jurisdiction registry connectors. |
| `datasets/` | 🟡 50% | search, registry, retrieve, analyse. |

---

## 3. Projects inventory

### `projects/east-africa-property-hostel/` (only project to date)

- 4 cohorts (students, owners, landlords, tenants)
- ~250–350 sources, tier-rated
- `EVIDENCE-AUDIT.md` running log: 0 hallucinations shipped, 4 corrections applied, 10 open gaps
- Sample stat verified end-to-end: 58.1% bedbug prevalence in 384 Moshi students → ResearchGate peer-reviewed study
- `report-v1-2026-04-25.docx` ~165 KB

This is **production-grade evidence work**. It validates the engine's framework. It does not yet demonstrate the missing capabilities (estimative probability, scenario modelling, executive deck).

---

## 4. Extracted books

8 text files in `extracted-books/`:
- 7-steps.txt, business-reports.txt, eco-thesis.txt, reports-proposals.txt, ultimate-scraping.txt, webscraping-python.txt, white-papers.txt, writing-that-works.txt

Digests, not full books. Useful for skill-building; insufficient as a learning corpus.

---

## 5. Governance documentation

- `CLAUDE.md` — orchestrator instructions; evidence-discipline-first; standard research workflow
- `AGENTS.md` — Codex / generic-agent fallback
- `PROJECT_BRIEF.md` — engine mission, 19 report schemas (A–S), 10 design principles, roadmap
- `RESEARCH_CRAFT_INTEGRATION.md` — maps 6 canonical books → 15 new skills (+30 future)
- `README.md` — engine as research operating system

This documentation layer is **above industry standard** — most consulting firms don't expose their methodology this transparently.

---

## 6. Gap inventory (will be addressed in `04-recommendations.md`)

Identified absences, none of which are architectural blockers — all are addressable as new skills, tool builds, or framework adoptions:

1. No structured analytic techniques skill (ACH / KAC / Pre-Mortem / Red Team / Devil's Advocacy / Indicators / What-If / High-Impact-Low-Probability)
2. No estimative-probability skill (Sherman Kent / ODNI lexicon)
3. No quantitative-modelling skill (market sizing, sensitivity, scenario, financial models)
4. No executive-communication skill (Pyramid Principle, MECE, action titles, Zelazny)
5. No academic-reporting-standards skill (PRISMA, CONSORT, STROBE, MOOSE, GRADE, Cochrane, TOP, EQUATOR)
6. No primary-research skill (interview design, surveys, Delphi, qualitative coding)
7. No knowledge-base reuse layer (McKinsey-KNOW-equivalent)
8. No language coverage beyond English (Swahili / French / Luganda / Kinyarwanda / Arabic)
9. No paywalled-database access workflow (Bloomberg / Capital IQ / LexisNexis / Refinitiv)
10. No expert-network workflow (GLG / AlphaSights / Third Bridge equivalent processes)
11. No competitive-intelligence skill (patent analysis, technology scanning, pricing forensics)
12. No geospatial-analysis skill (mapping, satellite imagery beyond Bellingcat manual technique)
13. No data-visualisation-and-storytelling skill
14. No URL-liveness CI / archive snapshot enforcement (flagged in own ship-gate but not automated)
15. No external peer-review wave (Wave 3.5)
16. Most `tools/verification/` and `tools/sanctions/` are stubs
17. No conflict-of-interest disclosure mechanism on engagement
18. No "living document" / cadenced-refresh concept
19. No Ivy / Oxbridge / LSE examination-convention encoding (per the owner's added bar)
20. No formal cost-control or token-budget discipline in orchestration
