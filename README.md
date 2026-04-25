# digital-research-engine

A multi-agent web-research engine for systematic, evidence-disciplined investigation of complex topics. Built as a portable **skills engine** consumable by Claude Code, Codex, and any other agent runtime that loads `SKILL.md` / `AGENTS.md` files.

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

## The 11 engine skills (new)

| # | Skill | Purpose |
|---|---|---|
| 0 | **evidence-discipline** | The non-negotiable anti-hallucination rule. Precedes every other skill. |
| 1 | research-orchestration | Multi-wave, multi-agent research coordination |
| 2 | source-verification | 5-tier credibility ladder + triangulation |
| 3 | quote-extraction | Verbatim attribution discipline |
| 4 | gap-analysis | What's missing; classify search vs structural vs scope gaps |
| 5 | pain-point-taxonomy | Structured prevalence × severity classification |
| 6 | cross-cohort-synthesis | Shared / cascade / symmetric pain across cohorts |
| 7 | regulatory-landscape-mapping | Five-layer legal mapping (constitutional → enforcement) |
| 8 | academic-source-mining | Tier-1 peer-reviewed + dissertation pipeline |
| 9 | social-source-extraction | Reddit (PRAW + Apify), X, TikTok methodology |
| 10 | research-report-builder | Markdown → designed Word doc with 4 report-type schemas |

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
