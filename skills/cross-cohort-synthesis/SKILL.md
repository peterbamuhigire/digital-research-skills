---
name: cross-cohort-synthesis
description: Use when 2+ cohort research streams have been completed and the orchestrator needs to surface shared pains, contradictory findings, and two-sided product opportunities. Wave-4 work in `research-orchestration`.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Cross-cohort synthesis

Single-cohort research finds problems. Cross-cohort synthesis finds **leverage**.

## What to look for

1. **Shared pains** — pain X hits cohort A and cohort B in the same way. Often the strongest product hook (e.g., deposit theft hits students + tenants identically).
2. **Symmetric pains** — same feature, opposite valence (e.g., eviction speed: fast = good for landlord, bad for tenant). Two-sided products must navigate, not just solve.
3. **Cascade pains** — A's failure causes B's pain (e.g., HELB delay → student can't pay → hostel owner cashflow crisis).
4. **Contradictions** — sources disagree. Investigate; sometimes truth is "both are right in different segments".
5. **Mutual reinforcement** — A's coping behaviour worsens B's pain (landlord blacklists worsen single-women rejection).

## Decision rules

- **Synthesis is the orchestrator's job.** Never delegate it to a research sub-agent — they don't have the full corpus in context.
- **Every shared pain gets a row** in a top-level synthesis file mapping cohorts × pains.
- **Two-sided product ideas** (idea relieves both cohort pains) get tagged in both `opportunities/product-ideas.md` files.
- **Cascade pains get a directional arrow** — A → B, not just "shared".
- **Contradictions are documented**, not hidden. Reader needs to see disagreement.

## Output target

A top-level synthesis section (in the project README or a dedicated `SYNTHESIS.md`) that includes:

- Shared-pains matrix (cohorts × pains)
- Cascade map (directional)
- Symmetric-pains list
- Two-sided product opportunities
- Highest-leverage interventions ranked by cohort-coverage

## Anti-patterns

- Treating each cohort report as an independent silo
- Delegating synthesis to sub-agents
- Not surfacing cascades — leaves leverage unidentified
- Cherry-picking shared pains; ignoring contradictions
- Counting a pain as "shared" without checking the underlying mechanism is the same

## See also

- `pain-point-taxonomy` — feeds the cohort × pain matrix
- `research-report-builder` — emits synthesis as a chapter in the final Word doc
