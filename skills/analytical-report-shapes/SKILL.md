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

## Shape Selection Intake

- Audience, decision context, time sensitivity, evidence maturity, confidentiality, and expected action.
- Output family, length, citation expectations, and whether the piece is descriptive, estimative, evaluative, or advisory.

## Legacy Shape Method

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

## Legacy Shape Pitfalls

- Treating "report" as a single genre.
- Using an academic essay shape for an executive decision.
- Using a consulting deck shape for an evidentiary investigation that needs audit trail.
- Hiding uncertainty in footnotes.
- Drafting before choosing the reader action.

## Legacy Shape Deliverables

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

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Audience, decision, urgency, evidence maturity | Brief and evidence register | Stop shape selection until audience and decision are known |
| Delivery constraints | Requester or publishing channel | Return a content architecture without claiming format readiness |

## Capability Contract

Shape selection and review are read-only. Creating, rendering, publishing, or replacing deliverables requires explicit authority.

## Degraded Mode

Without rendering or channel access, provide a qualified outline and state that visual and production checks are not assessed.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Urgent warning | Use warning note | Buried signal |
| Options require commitment | Use decision memo | Descriptive non-decision |
| Evidence remains exploratory | Use research report | Overstated recommendation |

## Legacy Shape Scenario

A time-sensitive indicator with an explicit trigger routes to a warning note, not a broad research report.

## Companion Skills

- `research-output-formats` covers broad academic, advocacy, commercial, and professional families.
- `executive-communication` supplies Minto, SCQA, and action-title structure.
- `analytic-tradecraft` supplies intelligence judgment discipline.
- `decision-support-analysis` supplies options and recommendation logic.

## Workflow

1. Identify the audience, decision, urgency, evidence maturity, and delivery constraint.
2. Select the smallest report shape that can carry the decision and required evidence.
3. Stop when the audience or decision is unknown, or the shape implies unsupported certainty.
4. Recover by selecting a less committal shape or returning a qualified architecture with format checks unassessed.
5. Validate section order, decision visibility, evidence placement, and channel fit.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Selected report shape and content architecture | Analyst, writer, and decision-maker | The form exposes the decision, evidence maturity, urgency, and required action without surplus sections |

## Anti-Patterns

- Choosing a format by habit. **Fix:** route from audience and decision.
- Using a broad report for an urgent warning. **Fix:** use a warning note.
- Forcing a recommendation from exploratory evidence. **Fix:** use a research report.
- Copying every template section. **Fix:** retain only decision-bearing sections.
- Claiming visual readiness without rendering. **Fix:** mark production checks unassessed.

## Worked Example

A time-sensitive indicator with a named trigger routes to a warning note, while an exploratory evidence review remains a research report.
