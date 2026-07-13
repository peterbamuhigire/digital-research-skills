---
name: agentic-research-operations
description: "Use when designing, running, or auditing multi-agent research operations: wave planning, task briefs, agent roles, tool boundaries, verification loops, failure recovery, evaluation, and portable runtime behavior across Codex, Claude, and other agents."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Agentic Research Operations

<!-- dual-compat-start -->

## Use When

- Use when a project dispatches multiple research agents, verification agents, synthesis agents, or code agents.
- Use when building or changing orchestration, agent prompts, runtime portability, or evaluation gates.
- Use when a research workflow must be reproducible, auditable, and resilient to agent drift.

## Do Not Use When

- A single local edit or fact-check needs no orchestration.
- The user explicitly asks not to delegate or parallelize.

## Operations Intake Guidance

- Research goal, cohorts, source classes, outputs, risks, tools, time horizon, and verification standard.
- Current project context and any prior wave outputs.
- The hard evidence-discipline boilerplate for every sub-agent prompt.

## Legacy Operations Method

1. Decide whether agents help: split only independent work with clear boundaries and verifiable outputs.
2. Define roles: researcher, verifier, gap analyst, red-team reviewer, synthesizer, renderer, or code worker.
3. Write briefs with goal, scope, out-of-scope, source classes, deliverable, storage path, and hard constraints.
4. Assign disjoint ownership: cohorts, files, source classes, or verification questions.
5. Require structured outputs: findings, sources, gaps, confidence, and next actions.
6. Verify before merge: source liveness, quote checks, contradiction scan, and claim graph update.
7. Keep cross-cohort synthesis with the orchestrator unless a task is explicitly a bounded synthesis subproblem.
8. Record operational lessons in project status or evidence audit.

## Quality Standards

- Delegated tasks are independent, bounded, and material to the outcome.
- Agents receive enough context to avoid duplicate work but not so much that verification independence is lost.
- Every agent output has a merge criterion and rejection criterion.
- Tool access is least-privilege for the task.
- Verification is a separate pass, not trust in a polished answer.

## Anti-Patterns

- Delegating the critical path when the orchestrator is blocked on it.
- Multiple agents researching the same broad question without cohort boundaries.
- Asking a research agent to synthesize across cohorts it cannot see.
- Accepting sub-agent citations without verification.
- Hiding failures instead of logging them.

## Legacy Operations Deliverables

- Agent wave plan.
- Standard brief.
- Verification checklist.
- Merge/reject decision.
- Operations lesson log.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Operability | Wave plan | Markdown table | Agent, cohort, scope, output, verification |
| Release evidence | Merge record | Markdown table | Agent output accepted/rejected with reason |

## References

- Load `references/agent-brief-template.md` before dispatching agents.
- Load `references/agent-evaluation-loop.md` when accepting, rejecting, or improving agent outputs.

<!-- dual-compat-end -->

## Companion Skills

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Research plan, cohort boundaries, evidence clause | Orchestrator and project files | Stop dispatch until boundaries and evidence rules exist |
| Runtime capabilities and permissions | Host runtime | Use the least-capable read-only route and mark unavailable work |

## Capability Contract

Agents default to read-only research. File mutation, external messages, publication, destructive action, spending, and certification require explicit authority and bounded ownership.

## Degraded Mode

If delegation or tools are unavailable, run waves sequentially and return partial evidence with unassessed tasks and recovery checkpoints named.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Workstreams are independent | Delegate with non-overlapping ownership | Merge conflict |
| Shared file is involved | Keep with orchestrator | Concurrent overwrite |
| Agent violates evidence clause | Quarantine output and reverify | Fabricated evidence |

## Legacy Operations Scenario

Separate source-discovery cohorts may run concurrently, while the shared synthesis register remains under orchestrator ownership.

## Companion Skills

- `research-orchestration` supplies research wave structure.
- `source-evaluation` supplies mandatory evidence constraints.
- `evidence-claim-graph` supplies merge substrate.
- `skill-writing` applies when agent operations are encoded into skills.

## Workflow

1. Partition independent work and reserve shared files for the orchestrator.
2. Brief each agent with exact ownership, inputs, outputs, permissions, and the evidence clause.
3. Stop a cohort when evidence rules are violated, ownership overlaps, or required inputs are absent.
4. Recover by quarantining suspect output, repairing the brief, and retrying only the failed bounded task.
5. Verify checkpoint evidence before merging results into the shared synthesis substrate.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Agent briefs, checkpoints, and verified merge packet | Orchestrator and synthesis workflow | Ownership is non-overlapping and every accepted claim retains its evidence trail |

## Worked Example

Two source-discovery cohorts may run concurrently, but the orchestrator alone edits the shared claim register and rejects any checkpoint missing source links.
