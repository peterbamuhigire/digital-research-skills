---
name: analytical-report-shapes
description: "Use when selecting or designing the exact shape of a decision-grade analytical artifact: intelligence brief, estimative memo, warning note, decision memo, status report, evaluation report, research report, due-diligence memo, market analysis, or executive one-pager."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Analytical Report Shapes

<!-- dual-compat-start -->

## Use When

- Use when the user asks for a report, memo, brief, paper, deck, one-pager, intelligence product, status update, evaluation, or recommendation and the exact shape matters.
- Use before drafting or briefing sub-agents so structure, evidence density, confidence language, and audience action are locked.
- Use alongside `research-output-formats`; this skill focuses on decision-grade analytical shapes.

## Do Not Use When

- The user provides a binding template, regulator form, journal template, or house style.
- The output is a raw research note that is not meant for a reader decision.

## Required Inputs

- Audience, decision context, time sensitivity, evidence maturity, confidentiality, and expected action.
- Output family, length, citation expectations, and whether the piece is descriptive, estimative, evaluative, or advisory.

## Workflow

1. Identify the reader's action: know, decide, approve, fund, investigate, monitor, challenge, or communicate.
2. Classify the analytic mode: descriptive, explanatory, estimative, warning, evaluative, advisory, or status.
3. Select the shape from `references/shape-catalogue.md`.
4. Load the matching template from `references/templates.md`.
5. Route to companion skills for evidence, reasoning, uncertainty, decision, executive writing, and rendering.
6. Run the shape-specific ship gate before final drafting.

## Quality Standards

- The first screen or page tells the reader why the artifact exists.
- The shape matches the decision lifespan: current brief, durable report, warning note, or reusable knowledge asset.
- Evidence density matches audience and stakes.
- Confidence language survives editing.
- Headings form a skim path that communicates the argument.

## Anti-Patterns

- Treating "report" as a single genre.
- Using an academic essay shape for an executive decision.
- Using a consulting deck shape for an evidentiary investigation that needs audit trail.
- Hiding uncertainty in footnotes.
- Drafting before choosing the reader action.

## Outputs

- Shape selection note.
- Artifact outline.
- Shape-specific quality gate.
- Sub-agent deliverable instructions.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| UX quality | Shape selection note | Markdown table | Audience, action, shape, reason |
| Release evidence | Shape ship gate | Checklist | Evidence, uncertainty, skim path, next action |

## References

- Load `references/shape-catalogue.md` to select the artifact.
- Load `references/templates.md` to draft the artifact skeleton.

<!-- dual-compat-end -->

## Companion Skills

- `research-output-formats` covers broad academic, advocacy, commercial, and professional families.
- `executive-communication` supplies Minto, SCQA, and action-title structure.
- `analytic-tradecraft` supplies intelligence judgment discipline.
- `decision-support-analysis` supplies options and recommendation logic.
