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


## Peer Review Loop Required Context
- Draft analysis, source manifest, claim graph, assumptions, conclusions, and intended audience.
- Review mandate: source audit, methods audit, red team, decision review, or prose review.


## Peer Review Loop Core Method Notes
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


## Peer Review Loop Existing Failure Notes
- Review as grammar polishing.
- Devil's advocacy with no power to change the output.
- Reviewer sees only the conclusion, not the evidence.
- Dissent deleted without disposition.


## Peer Review Loop Core Deliverables
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

## Inputs

| Artefact | Source or provider | Requirement | If absent |
|---|---|---|---|
| Frozen review candidate, claims, sources, and method notes | authoring workflow | required | Return a review-readiness gap list if missing |


## Peer Review Loop Permission Notes
Read and source-search access are required, and peer review defaults to read-only. Remediation edits or release actions need explicit authority separate from the review mandate.

## Degraded mode

When sources, models, or methods cannot be inspected, issue a qualified review with those checks marked unassessed; do not close or downgrade the affected risk.

## Decision rules

| Choice | Action | Failure avoided |
|---|---|---|
| Finding challenges method or evidence materially | Block release pending disposition | Cosmetic review masks substantive error |


## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Read-only review report and disposition register | author and release owner | Every finding cites the artefact and records accept, revise, or reject |


## Peer Review Loop Evidence Notes 1
- Record the frozen candidate, cited findings, reviewer dissent, severity, author disposition, and rerun evidence.

## Worked example

A forecast with an uncited growth assumption receives a blocking finding tied to the exact model cell or paragraph and a request for source or removal.

<!-- dual-compat-end -->

## Companion Skills

- `analytic-tradecraft` supplies competing-hypothesis and bias checks.
- `source-verification` supplies source audit checks.
- `critical-reasoning-and-argument` supplies argument reconstruction.


## Workflow
1. Freeze the review candidate and define the review questions.
2. Challenge sources, method, reasoning, countercases, and decision implications.
3. Stop release on an unresolved material evidence or method defect.
4. Record dispositions; recover by revising the artefact and rerunning the affected checks.

## Capability Contract

Default to read-only review. Read and search are required; editing or publication requires explicit separate authority.


## Peer Review Loop Evidence Notes 2
| Evidence | Consumer | Acceptance |
|---|---|---|
| Review findings and disposition register | Author and release owner | Every finding cites the artefact and has an accepted disposition |


## Anti-Patterns
- Reviewing a moving draft. Fix: freeze and identify the candidate.
- Raising a finding without artefact evidence. Fix: cite the exact claim, cell, or method step.
- Treating style preference as a blocker. Fix: tie severity to decision risk.
- Suppressing dissent after majority agreement. Fix: record and disposition it.
- Closing a finding without rerunning the check. Fix: verify the revision.

## Reference Index

- [Review protocol](references/review-protocol.md)
