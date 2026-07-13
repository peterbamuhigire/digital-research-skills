---
name: 00-meta-initialization
description: Use when starting a scaffolded research workspace that needs an explicit project profile, methodology, audience-output matrix, wave roadmap, and dispatch gate; do not use for routine work inside an already initialised project.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
  priority: critical
---

# Research Meta-Initialization

Use this skill immediately after `python -m engine new-project ...` and before
any research sub-task is dispatched.

## Required Load Order

1. `skills/source-evaluation/SKILL.md`
2. `skills/source-evaluation/references/evidence-discipline.md`
3. `references/decision-tree.md`

## Objective

Convert the scaffolded `_context/` TODO files into a concrete project operating
plan:

- research type
- domain and geography
- audience
- output family and variant
- methodology mix
- primary-research need
- monetization or reuse intent
- roadmap and validation gates

## Intake

Ask the user only for facts that cannot be inferred from the existing brief.
If a field is unknown, mark it as `TODO` or `(gap)` instead of inventing detail.

Required fields:

| Field | Destination |
|---|---|
| Research type | `_context/project-profile.md` |
| Domain | `_context/project-profile.md` |
| Geography | `_context/scope.md` |
| Audience | `_context/audience.md` |
| Output family | `_context/output-plan.md` |
| Methodology mix | `_context/methodology.md` |
| Cohorts | `_context/cohorts.md` |
| Exclusions | `_context/exclusions.md` |
| Hypotheses | `_context/hypotheses.md` |
| Success criteria | `_context/success-criteria.md` |
| Monetization intent | `_context/monetization.md` |

## Roadmap Output

Write `_context/research-roadmap.md` with:

1. initiation tasks
2. research waves
3. verification pass
4. synthesis pass
5. output assembly
6. validation and release-pack steps

## Dispatch Gate

Research dispatch is blocked until the following are no longer blank:

- `_context/brief.md`
- `_context/project-profile.md`
- `_context/methodology.md`
- `_context/audience.md`
- `_context/output-plan.md`
- `_context/scope.md`
- `_context/success-criteria.md`

## Evidence Clause for Delegation

Every delegated research prompt must include the hard constraint from
`source-evaluation/references/evidence-discipline.md` verbatim. Do not shorten,
paraphrase, or soften it.

<!-- dual-compat-start -->
## Use When

Use for a new or materially re-scoped research project before collection begins.

## Do Not Use When

Do not rerun for routine work in an initialised project; use `research-orchestration` to revise active waves.

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Brief, audience, decision, output family | Requester or project files | Stop and request the missing decision or audience |
| Existing workspace state | Repository inspection | Record a new-project state; never invent files or prior decisions |

## Workflow

1. Inspect the workspace and stop if user-owned state would be overwritten.
2. Resolve project type, audience, decision, evidence risk, method, and outputs.
3. Choose cohorts and waves; recover a partial intake by recording open fields as gaps.
4. Apply the evidence clause to every delegated brief and release the roadmap only when dispatch gates pass.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Project profile and roadmap | Research orchestrator | Audience, decision, method, cohorts, outputs, gaps, and gates are explicit |

## Initiation Evidence Guidance

The completed intake, workspace inventory, decision record, and dispatch checklist form the initiation evidence.

## Capability Contract

Workspace inspection is read-only by default. Creating or changing project files requires explicit authority; deletion, publication, spending, and external communication are outside this skill.

## Degraded Mode

If files or tools are unavailable, return a qualified intake and wave outline with unverified fields marked `gap`; do not claim the project is dispatch-ready.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Decision or audience missing | Stop intake | Aimless research |
| Existing project materially changed | Re-profile and preserve prior record | Silent scope drift |
| Evidence gate incomplete | Hold dispatch | Unsourced collection |

## Quality Standards

The profile is traceable to supplied context, unresolved fields are visible, and no delegated task omits the evidence clause.

## Initialization Pitfalls

- Guessing the audience; ask or mark the gap.
- Starting collection before scope approval; hold dispatch.
- Overwriting existing project state; reconcile it.
- Treating a method label as a method rationale; record the choice and reason.
- Omitting stop conditions; define them before waves begin.

## Worked Example

A brief that names a topic but no decision produces a provisional profile and a blocked dispatch gate, not an invented executive audience.

## References

- [Initialization decision tree](references/decision-tree.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Intake record and dispatch checklist | Orchestrator and reviewer | Every supplied fact maps to its source and every unresolved field is marked as a gap |

## Anti-Patterns

- Guessing the audience. **Fix:** ask the requester or mark the audience as a blocking gap.
- Starting collection before approval. **Fix:** stop dispatch until scope and gates are accepted.
- Overwriting project state. **Fix:** reconcile existing files and preserve prior decisions.
- Naming a method without rationale. **Fix:** record why it fits the question and constraints.
- Omitting stop conditions. **Fix:** define completion, escalation, and evidence thresholds before waves begin.
