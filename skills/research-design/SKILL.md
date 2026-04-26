---
name: research-design
description: Use when a research project needs formal design discipline — historical research methods, trend analysis, MROC (Market Research Online Community), knowledge-lifecycle modelling, the canonical research-design document, or the final structured report-builder pipeline. Companion to research-orchestration; load only the design layer the project demands.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Research Design

Formal research-design layer. The orchestrator (`research-orchestration`) decides what kind of research is being run; this skill governs how that research is *designed* from question to artifact, when the project demands a formal design rather than an opportunistic sweep.

Research design starts with reasoning discipline. Use `critical-reasoning-and-argument` when framing empirical puzzles, theoretical puzzles, research questions, hypotheses, case-selection logic, method justification, and expected contribution.

## When to load

| Situation | Reference |
|---|---|
| Reconstructing past events from primary and secondary sources | `references/historical-research-methods.md` |
| Forecasting, time-series signal extraction, weak-signal surfacing | `references/trend-analysis.md` |
| Recruiting and running a Market Research Online Community for 3+ days | `references/mroc-design-and-management.md` |
| Modelling research artifacts as a state machine across the 8 lifecycle stages | `references/knowledge-lifecycle-pipeline.md` |
| Authoring or maintaining the canonical research-design document (Abbott "north-star artefact") | `references/research-design-document.md` |
| Assembling the final structured Word document from completed research | `references/research-report-builder.md` |
| Designing or executing a case study (single, multiple, intrinsic, instrumental, collective; exploratory, explanatory, descriptive) | `references/case-study-method.md` (definitions, typologies, validity, reporting) + `references/case-selection-and-analysis.md` (operating discipline) |
| Designing a Uganda- or Kenya-facing university proposal / thesis / dissertation | Load this skill for design logic, then load `uganda-academic-research` or `kenya-academic-research` for institution-specific format, ethics, viva, and examination rules |

## The canonical design document (always for projects ≥1 week)

For any project longer than a one-day sweep, load `references/research-design-document.md` and produce the 3–4 page document with:

- **Empirical puzzle** — what is the engine observing that is not yet explained?
- **Theoretical puzzle** — which existing frame breaks down here?
- **Research questions** — concrete, answerable, derived from the puzzles.
- **Action list** — sub-agent waves, methods, evidence targets.
- **Argument logic** — the puzzle-question-method-contribution chain tested through `critical-reasoning-and-argument`.

The document is the engine's north-star artefact. Every sub-agent reads it and may update it.

## Six design layers (load when relevant)

### 1. Historical methods
For historical / archival research: primary-source priority, source appraisal (Burke pentad — load `source-evaluation`), chronology discipline, historiographical-debate framing.

### 2. Trend analysis
For forecasting / signal extraction: durable trend vs fad, driver vs symptom, leading vs coincident indicators, signal-to-noise filters.

### 3. MROC (Market Research Online Community)
For longitudinal qualitative research with a recruited panel: recruitment screen, moderator playbook, prompts cadence, qualitative coding pipeline, quantitative scaffolding (polls, ratings), synthesis cadence.

### 4. Knowledge lifecycle (Bergeron)
8-stage state machine: discovery → capture → curation → storage → retrieval → application → re-use → retirement. Each stage has its own issues, support mechanisms, and value contribution.

### 5. Research design document (Abbott)
The 3–4 page artefact that names the empirical puzzle, theoretical puzzle, research questions, and action list. Maintained for the life of the project.

### 6. Research report builder
The pipeline that pulls from `research/`, `analysis/`, and `opportunities/` files, applies a topic-appropriate report schema, and emits a designed `.docx` via the engine's professional-word-output layer.

## Orchestration

```
new long-running research project
├─ load research-orchestration (type / discipline / reading mode / wave plan)
├─ load research-design
│   └─ produce references/research-design-document.md artefact
├─ during waves: load matching design layer
│   ├─ historical → references/historical-research-methods.md
│   ├─ forecasting → references/trend-analysis.md
│   ├─ panel-based → references/mroc-design-and-management.md
│   └─ artefact-flow modelling → references/knowledge-lifecycle-pipeline.md
└─ at finish
    └─ load references/research-report-builder.md to assemble the deliverable
```

## Universal anti-patterns

- Skipping the design document; running a multi-week project as if it were a single sweep.
- Treating a trend analysis as "list of things happening recently" without leading-vs-coincident discipline.
- Running an MROC as a focus group; it is longitudinal and qualitative + quantitative.
- Mixing knowledge-lifecycle stages in the same artifact (capture vs curation vs application have different rules).
- Building the final Word document by hand-stitching files; use the report-builder pipeline.
- Letting the design document drift; it must be updated as the project evolves, not snapshot at kickoff.
- Research question, method, or case selection that is plausible but not argued.

## Companion skills

- `research-orchestration` — the dispatcher; this skill is its formal-design layer.
- `critical-reasoning-and-argument` — mandatory for puzzle framing, research questions, hypotheses, method justification, case selection, and contribution logic.
- `research-techniques` — specific named techniques applied inside design phases.
- `source-evaluation` — every source consulted.
- `academic-writing`, `report-and-proposal-craft` — output containers.
- `uganda-academic-research`, `kenya-academic-research` — East African institutional research-handbook requirements.
- `data-quality-pipeline`, `dataset-discovery-and-analysis` — for empirical projects.
