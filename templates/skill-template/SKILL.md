---
name: <directory-name>
description: Use when <concrete trigger>; use <nearest-neighbour> instead for <excluded trigger>. Produces <named result> for <consumer>.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# <Skill Title>

State the procedure's purpose and boundary in one or two sentences.

## Use When

- Name a concrete positive trigger.

## Do Not Use When

- Name the nearest neighbour and its distinct trigger.

## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---:|---|
| <input> | <upstream skill, user, repository, or source> | yes | Stop or return the named narrow fallback. |

## Workflow

1. Inspect the inputs and stop if a required artefact is absent.
2. Apply the domain decision rules and record the chosen branch.
3. Produce the outputs and evidence together.
4. Validate acceptance conditions; repair a failed check and rerun it before handoff.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| <output> | <downstream skill or person> | <observable condition> |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| <validation record> | Release owner | Names the check, result, and unresolved gap. |

## Capability Contract

Read access is required. State whether search, edit, execute, network, or delegation is needed. Default audit, critique, analysis, and planning work to read-only. Require explicit authority for mutation, publishing, destructive actions, spending, and certification claims.

## Degraded Mode

When a required capability is unavailable, return the narrowest useful qualified result, name the evidence gap, and mark affected checks `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| <condition> | <domain action> | <wrong-choice consequence> |

## Quality Standards

- State observable, domain-specific acceptance criteria and release blockers.

## Anti-Patterns

- <Concrete mistake>. Fix: <specific correction>.
- <Concrete mistake>. Fix: <specific correction>.
- <Concrete mistake>. Fix: <specific correction>.
- <Concrete mistake>. Fix: <specific correction>.
- <Concrete mistake>. Fix: <specific correction>.

## Worked Example

Show a realistic input, the decisive branch, the output, and the evidence that proves acceptance. Do not invent facts to make the example look complete.

## References

- Link each required local reference directly, or state that the entrypoint is self-contained.
