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

## Required Inputs

- Research goal, cohorts, source classes, outputs, risks, tools, time horizon, and verification standard.
- Current project context and any prior wave outputs.
- The hard evidence-discipline boilerplate for every sub-agent prompt.

## Workflow

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

## Outputs

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

- `research-orchestration` supplies research wave structure.
- `source-evaluation` supplies mandatory evidence constraints.
- `evidence-claim-graph` supplies merge substrate.
- `skill-writing` applies when agent operations are encoded into skills.
