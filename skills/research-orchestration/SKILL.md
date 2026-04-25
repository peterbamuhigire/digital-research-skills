---
name: research-orchestration
description: Use when running multi-pass, multi-agent web research on a topic — coordinating parallel sub-agent dispatch, planning gap-fill passes, consolidating outputs into a unified corpus. Default driver for any /research, "find pain points of X", or systematic literature surfacing task.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Research orchestration

A research engine never runs as a single search. It runs as **planned waves**:

1. **Wave 1 — broad sweep.** One agent per cohort, broad query, ~50 sources target.
2. **Wave 2 — gap fill.** Specific gaps each Wave 1 agent flagged; deeper academic + regulatory sources.
3. **Wave 3 — verification.** Cross-source triangulation; verbatim-quote extraction; URL liveness check.
4. **Wave 4 — synthesis.** Cross-cohort patterns; product/policy inferences.

This skill defines when each wave fires and how outputs are stored.

## When to use

Trigger on:
- "Research X across [region]" — dispatch a Wave 1 sweep
- "Now do Y for [adjacent group]" — parallel Wave 1 on a new cohort
- "Do another thorough pass" — Wave 2 gap fill
- "Synthesise across cohorts" — Wave 4
- "Audit our research for what we missed" — Wave 3 + Wave 4

Do **not** use for: single-question lookups, fact-checks, or known-target reads.

## Decision rules

- **One cohort per agent.** Don't ask one agent to research students AND landlords. Split.
- **Run waves in parallel where independent.** A student-side gap-fill and an owner-side gap-fill have no shared state — fire them simultaneously.
- **Cap each agent at ~50 distinct sources.** Past that, marginal value drops sharply; better to fire a Wave-2 agent.
- **Never delegate synthesis to research agents.** The orchestrator (you) does the synthesis. Research agents return raw findings, not conclusions.
- **Always brief the agent on what's already known.** Wave-2 agents must see Wave-1 themes so they don't re-confirm; they're paid to find new material.

## Standard agent brief structure

Every research-agent prompt should contain:

1. **Goal** — one sentence
2. **Scope** — geography, cohort, time-window
3. **Out-of-scope** — what NOT to research (avoids duplicate work)
4. **Themes to cover** — explicit numbered list
5. **Sources to mine** — named outlets, repositories, platforms
6. **Deliverable shape** — markdown sections, source-count target, quote requirements
7. **Hard constraints** — exclusions (e.g., "do NOT cover topic X"), language, format

If the brief is missing any of those, the output will be uneven.

## Orchestrator outputs

After each wave, the orchestrator writes:

- `<cohort>/research/pain-points-report.md` (or `complaints-report.md` for student-style cohorts)
- `<cohort>/research/sources.md` — annotated source list with gaps section
- `<cohort>/research/quotes.md` — verbatim quotes
- `<cohort>/analysis/themes.md` — sub-theme taxonomy
- `<cohort>/analysis/by-country.md` (or by-segment, depending on dimension)
- `<cohort>/opportunities/product-ideas.md`

Wave 2 outputs append a `# Pass 2 — Gap-fill addendum` section to the existing files rather than overwrite.

## Anti-patterns

- Single-shot research with one mega-prompt — produces shallow coverage, missing perspective splits
- Re-running Wave 1 instead of running Wave 2 — wastes context, duplicates known
- Delegating cross-cohort synthesis — only the orchestrator has all four cohort outputs in context
- Forgetting hard constraints in Wave-2 briefs — agent re-introduces excluded scope

## See also

- `gap-analysis` — feeds Wave-2 brief construction
- `source-verification` — Wave 3 verification logic
- `cross-cohort-synthesis` — Wave 4 work
- `research-report-builder` — final Word-document assembly
