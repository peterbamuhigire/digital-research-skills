---
name: 00-meta-initialization
description: Required first-run project kickoff for scaffolded research workspaces. Converts a new project into an explicit profile, methodology, audience-output matrix, and wave roadmap before research starts.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
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
