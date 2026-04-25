# digital-research-engine

A **world-class research operating system** — multi-agent, evidence-disciplined, portable across AI runtimes — that produces research, status, intelligence, evaluation, and decision-support reports for diverse audiences and purposes.

This is not a document-generator. It is a skills engine that runs investigations, applies discipline, and produces the right report shape for the right audience.

> **Repository:** https://github.com/peterbamuhigire/digital-research-skills

## What this engine does

Given a research question, the engine runs:

1. **Wave 1** — broad sweep (multiple parallel sub-agents, one per cohort)
2. **Wave 2** — targeted gap-fill on what Wave 1 missed
3. **Wave 3** — verification (URL liveness, statistic re-check, quote confirmation)
4. **Wave 4** — cross-cohort synthesis and product-opportunity mapping

The end product of every project is a **structured Word document** generated from versioned markdown source.

## Non-negotiable rule

> **The AI agents in this engine MUST NOT hallucinate.** No statistic, quote, name, court case, statute, organisation, or URL appears in any output unless traceable to a real, verified source. See `skills/evidence-discipline/SKILL.md` — that skill takes precedence over every other skill in the engine.

## Directory structure

```
digital-research-engine/
├── README.md             this file
├── CLAUDE.md             Claude Code operating instructions
├── AGENTS.md             Codex / generic-agent operating instructions
├── PROJECT_BRIEF.md      mission and direction
│
├── skills/               the skills library
│   ├── evidence-discipline/      NON-NEGOTIABLE anti-hallucination guardrail
│   ├── research-orchestration/   multi-wave agent coordination
│   ├── source-verification/      credibility tiering + triangulation
│   ├── quote-extraction/         verbatim attribution discipline
│   ├── gap-analysis/             corpus-coverage audit + Wave-2 briefing
│   ├── pain-point-taxonomy/      structured prevalence × severity tagging
│   ├── cross-cohort-synthesis/   shared / cascade / symmetric pain mapping
│   ├── regulatory-landscape-mapping/  five-layer legal mapping
│   ├── academic-source-mining/   peer-reviewed + dissertation pipeline
│   ├── social-source-extraction/ Reddit (PRAW + Apify) / X / TikTok
│   ├── research-report-builder/  markdown → Word doc with schema selection
│   │
│   ├── (skill-building skills, copied)
│   ├── skill-writing/
│   ├── skill-composition-standards/
│   ├── skill-safety-audit/
│   ├── validation-contract/
│   ├── capability-matrix/
│   │
│   ├── (project-documentation skills, copied)
│   ├── doc-architect/
│   ├── update-claude-documentation/
│   ├── project-requirements/
│   ├── spec-architect/
│   ├── manual-guide/
│   ├── markdown-lint-cleanup/
│   ├── professional-word-output/
│   ├── python-document-generation/
│   ├── excel-spreadsheets/
│   │
│   ├── (language / writing skills, copied)
│   ├── east-african-english/
│   ├── language-standards/
│   ├── content-writing/
│   ├── writing-quality/
│   ├── blog-writer/
│   │
│   └── doc-standards.md
│   └── encoding-patterns-into-skills.md
│
└── projects/             every research project lives here
    └── east-africa-property-hostel/
        ├── README.md
        ├── CLAUDE.md
        ├── EVIDENCE-AUDIT.md      hallucination-catch log
        ├── students/              cohort sub-project
        ├── owners/                cohort sub-project
        ├── landlords/             cohort sub-project
        └── tenants/               cohort sub-project
```

## The 18 engine skills

### Tier 1 — Always loaded
| # | Skill | Purpose |
|---|---|---|
| 0 | **evidence-discipline** | Non-negotiable anti-hallucination rule. Precedes every other skill. |
| 1 | research-type-router | Picks research type + report schema before any sub-agent fires |
| 2 | research-orchestration | Multi-wave, multi-agent research coordination |
| 3 | source-verification | 5-tier credibility ladder + triangulation |
| 4 | quote-extraction | Verbatim attribution discipline |
| 5 | gap-analysis | Classifies search vs structural vs scope gaps |

### Tier 2 — Loaded per research type
| # | Skill | Used for |
|---|---|---|
| 6 | pain-point-taxonomy | Pain-point / product research |
| 7 | cross-cohort-synthesis | Multi-cohort projects |
| 8 | regulatory-landscape-mapping | Policy / regulatory research |
| 9 | academic-source-mining | Any project needing tier-1 academic sources |
| 10 | social-source-extraction | Social-media / sentiment research |
| 11 | due-diligence-framework | Due-diligence projects |
| 12 | osint-methodology | OSINT projects |
| 13 | trend-analysis | Trend research |
| 14 | historical-research-methods | Historical research |
| 15 | academic-writing-conventions | Theses, dissertations, papers, academic essays |
| 16 | academic-citation-styles | Schemas L, N, P, R (academic variants) |

### Tier 3 — Final assembly
| # | Skill | Purpose |
|---|---|---|
| 17 | research-report-builder | Markdown → designed Word doc with 19 report schemas |

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

Variant rules: thesis / dissertation default to academic; paper defaults to academic; essay must be specified by the user.

## Cross-tool compatibility

Every skill ships with:
- `SKILL.md` — canonical instructions (Claude + generic)
- `README.md` — human-readable overview
- `CLAUDE.md` — Claude-Code-specific notes
- `AGENTS.md` — Codex / generic-agent notes
- `references/` — deep-dive references (placeholders to be expanded)

## How to start a new project

1. `mkdir projects/<project-id>/`
2. Add `README.md`, `CLAUDE.md`, `EVIDENCE-AUDIT.md` to the project
3. Define cohorts (sub-projects) — typically 1–4 named populations being researched
4. For each cohort, run `research-orchestration` Wave 1
5. After waves complete, run `cross-cohort-synthesis` and `research-report-builder`
6. End product: `projects/<project-id>/report-v<N>-<date>.docx`

## Current projects

- **`east-africa-property-hostel/`** — pain points across students, hostel owners, residential landlords, and ordinary tenants in Uganda, Kenya, Tanzania, Rwanda, Burundi, South Sudan. 250+ sources across 4 cohorts.

## Status

Engine v0.1 — first project complete through Wave 2 on student & owner cohorts; Wave 1 on landlord & tenant cohorts. Final Word document not yet generated.

Maintained by Peter Bamuhigire.
