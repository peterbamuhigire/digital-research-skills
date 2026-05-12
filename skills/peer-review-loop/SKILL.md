---
name: peer-review-loop
description: Use when research, analysis, forecasts, or recommendations need adversarial review, red-team challenge, devil's advocacy, source audit, method review, dissent handling, and revision disposition before release.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Peer Review Loop

<!-- dual-compat-start -->

## Use When

- Use before high-stakes publication, decisions, investment recommendations, policy advice, due diligence, or intelligence judgments.
- Use when the analysis is consensual, contested, surprising, or based on limited sources.
- Use after draft synthesis and before final executive communication.

## Do Not Use When

- The task is low-stakes formatting or mechanical conversion.
- The output has no claims or recommendations.

## Required Inputs

- Draft analysis, source manifest, claim graph, assumptions, conclusions, and intended audience.
- Review mandate: source audit, methods audit, red team, decision review, or prose review.

## Workflow

1. Assign review mode and reviewer independence.
2. Reconstruct the argument from the draft.
3. Audit sources and claim links.
4. Challenge assumptions, methods, and excluded alternatives.
5. Write a dissent or red-team memo when warranted.
6. Produce a revision disposition log.
7. Re-run verification on changed claims.

## Quality Standards

- Review attacks the argument, not the prose first.
- Dissent is preserved until resolved.
- Every accepted change has a reason.
- Every rejected challenge has a reason.

## Anti-Patterns

- Review as grammar polishing.
- Devil's advocacy with no power to change the output.
- Reviewer sees only the conclusion, not the evidence.
- Dissent deleted without disposition.

## Outputs

- Review memo.
- Red-team or devil's advocate memo.
- Revision disposition log.
- Residual-risk note.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Correctness | Review memo | Markdown | Findings, severity, evidence |
| Release evidence | Disposition log | Markdown table | Challenge, decision, reason |

## References

- Load `references/review-protocol.md` for review modes and disposition.

<!-- dual-compat-end -->

## Companion Skills

- `analytic-tradecraft` supplies competing-hypothesis and bias checks.
- `source-verification` supplies source audit checks.
- `critical-reasoning-and-argument` supplies argument reconstruction.
