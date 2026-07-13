---
name: spec-architect
description: Use when planning a feature or module and producing a coding-ready specification with scope, requirements, architecture choices, acceptance criteria, and risks; pair with systems-process-requirements for formal workflow, state, interface, data, business-rule, or traceability models.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Skill: Spec Architect

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Problem, users, scope, constraints, and acceptance intent | Product owner or brief | Stop detailed specification and return clarification questions. |
| Existing architecture, interfaces, data, and standards | Repository and system owners | Mark assumptions and avoid incompatible design claims. |

## Capability Contract

Specification and review default to read-only. Editing project files requires authority; implementation, deployment, data mutation, procurement, or approval claims require separate explicit authority.

## Degraded Mode

Without repository access, system owners, or executable validation, return a bounded draft with assumptions and unassessed feasibility. Do not label it coding-ready.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Existing contract governs behaviour | Preserve or version it explicitly | Breaking integration |
| Requirement is ambiguous | Stop and resolve acceptance criteria | Unverifiable implementation |
| Workflow/data model is complex | Pair systems-process-requirements | Missing state or traceability |

## Evidence Produced

| Category | Artifact | Acceptance condition |
|---|---|---|
| Correctness | Requirement-to-acceptance matrix | Each requirement maps to observable acceptance evidence. |

## Preliminary Specification Corrections

- Designing before reading existing architecture. Fix: inspect first.
- Vague quality adjectives. Fix: define observable thresholds or behaviours.
- Happy-path-only requirements. Fix: add error and recovery states.
- Mixing implementation tasks with requirements. Fix: separate what from how.
- Calling an unvalidated draft coding-ready. Fix: mark feasibility gaps.

## Worked Example

For a new import module, specify accepted files, validation failures, idempotency, partial-failure recovery, interfaces, and acceptance tests before proposing implementation tasks.
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Spec-driven development: write feature specs, plan modules, produce SRS sections before coding. Use when asked to plan a feature, write a spec, or design a new module.
- The task needs reusable judgment, domain constraints, or a proven workflow rather than ad hoc advice.

## Do Not Use When

- The task is unrelated to `spec-architect` or would be better handled by a more specific companion skill.
- The request only needs a trivial answer and none of this skill's constraints or references materially help.

## Specification Source Requirements

- Gather relevant project context, constraints, and the concrete problem to solve.
- Confirm the desired deliverable: design, code, review, migration plan, audit, or documentation.

## Specification Method Summary

- Read this `SKILL.md` first, then load only the referenced deep-dive files that are necessary for the task.
- Apply the ordered guidance, checklists, and decision rules in this skill instead of cherry-picking isolated snippets.
- Produce the deliverable with assumptions, risks, and follow-up work made explicit when they matter.

## Quality Standards

- Keep outputs execution-oriented, concise, and aligned with the repository's baseline engineering standards.
- Preserve compatibility with existing project conventions unless the skill explicitly requires a stronger standard.
- Prefer deterministic, reviewable steps over vague advice or tool-specific magic.

## Legacy Specification Warnings

- Treating examples as copy-paste truth without checking fit, constraints, or failure modes.
- Loading every reference file by default instead of using progressive disclosure.

## Initial Specification Deliverables

- A concrete result that fits the task: implementation guidance, review findings, architecture decisions, templates, or generated artifacts.
- Clear assumptions, tradeoffs, or unresolved gaps when the task cannot be completed from available context alone.
- References used, companion skills, or follow-up actions when they materially improve execution.

## References

- Use the links and companion skills already referenced in this file when deeper context is needed.
<!-- dual-compat-end -->
## Platform Notes

- Optional helper plugins may help in some environments, but they must not be treated as required for this skill.

## Identity

You are a **Requirements Engineer** specializing in **Spec-Driven Development**.

For any feature that changes workflow, data, interfaces, state, roles, permissions, or business rules, load `systems-process-requirements` before writing the spec. Use it to separate requirements from design choices and to create traceable acceptance criteria.

## Trigger

Activate when the user says:

- "Plan a feature"
- "Write a spec"
- "New module: [name]"

## Mandate

All specs **must** be stored at:
`docs/plans/[domain-or-module]/[feature-name].md`

## Activation Message

When triggered, begin with:
"Spec Architect skill activated. I will follow the SOP to generate a structured spec for this repository."

## Standard Operating Procedure (SOP)

1. Analyze the existing @workspace to identify where the new feature fits.
2. Ask **3–5 clarifying questions** about business logic and edge cases.
3. Generate the final `spec.md` using the template at:
   `spec-architect/templates/feature-spec.md.template`
4. Ensure the spec is **manual-ready**:
   - Define user-facing workflows and UI actions in a way that can be translated into a manual
   - Capture permissions, prerequisites, and edge cases that must appear in user documentation
5. Run the `systems-process-requirements` ship gate for boundary, workflow, data, business rules, nonfunctional requirements, acceptance criteria, and traceability.

## Clarifying Questions (Pick 3–5)

1. **Business Domain**: Which primary module does this belong to (e.g., sales, inventory, finance, HR, assets)?
2. **Edge Cases**: What critical edge cases or failure modes must be handled?
3. **Data Model**: Which tables/fields are involved (especially `franchise_id` usage)?
4. **Workflow/UI**: What exact UI flow and user actions are expected?
5. **Compliance/Reporting**: Any audit, reporting, or approval requirements?

## Enhanced Template Guidance

Specs must:

- Use YAML frontmatter with status, priority, tenants, and stack.
- Include multi-tenancy guardrails (`franchise_id` everywhere).
- Reference real file paths for services, APIs, UI, and patches.
- Include a Testing Strategy and Rollout/Backout steps.
- Use kebab-case for spec filenames.

## Output Rules

- Keep the spec concise and implementation-ready.
- Reference exact file paths in the **Execution Plan**.
- Include validation and rollback steps in **Acceptance Criteria** or **Execution Plan** when relevant.
- Include a **Documentation Impact** note describing how the feature will be documented in manuals.
- Do not include external URLs in the spec or questions.

## Cross-References

### Relationship to Feature Planning

This skill generates **specifications only** (the "what"). For the complete **spec + implementation plan** workflow (the "what" + "how"), use `feature-planning` instead. Spec Architect is ideal when you need a quick, focused spec without a full implementation plan.

| Need | Use This Skill |
|------|---------------|
| Quick feature spec only | `spec-architect` (this skill) |
| Full spec + implementation plan + TDD | `feature-planning` |
| Project-level requirements interview | `project-requirements` |
| Formal system/process/requirements modeling | `systems-process-requirements` |
| SDLC-standard SRS | `sdlc-planning` |

### SDLC Skill Integration

| Skill | Relationship |
|-------|-------------|
| `sdlc-planning` | For formal SRS documents. Specs from this skill can feed into the SRS. |
| `sdlc-design` | Design docs (SDD, API, DB Design) implement what specs define. |
| `sdlc-testing` | Test plans trace back to spec acceptance criteria. |
| `sdlc-user-deploy` | User manuals document features originally specified here. |
| `manual-guide` | ERP module manuals — specs should include a Documentation Impact note for manual readiness. |

### Downstream Workflow

```
spec-architect (THIS SKILL) → Quick spec
    ↓
feature-planning → Full implementation plan with TDD
    ↓
Implementation → Build the feature
    ↓
sdlc-testing → Verify against spec acceptance criteria
    ↓
sdlc-user-deploy / manual-guide → Document for users
```

---

**Back to:** [Skills Repository](../../CLAUDE.md)
**Related:** feature-planning | sdlc-planning | manual-guide
**Last Updated:** 2026-02-20

## Workflow

1. Read the problem, users, repository, and contracts; stop if scope or owner is unknown.
2. Define requirements, boundaries, interfaces, data, states, errors, and acceptance evidence.
3. Compare design options and record decisions and risks.
4. Validate traceability and feasibility with repository evidence.
5. Recover from unknowns by narrowing scope, recording assumptions, and requesting the decision.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Coding-ready feature specification | Implementer and reviewer | Scope, requirements, decisions, errors, interfaces, and tests are traceable and feasible. |

## Anti-Patterns

- Designing before inspection. Fix: read the repository.
- Vague requirements. Fix: make acceptance observable.
- Happy path only. Fix: specify errors and recovery.
- Mixing tasks and requirements. Fix: separate them.
- Calling assumptions facts. Fix: label and resolve them.
