# Replay-gated skill revision

## Cause before change

Record one primary cause separately from the original symptom tags: `routing`, `knowledge`, `execution`, `source/tool`, `gold-label`, `mixed`, or `unknown`. Route non-knowledge failures to their owner. `mixed` and `unknown` do not qualify for a guidance-only revision. A reviewer-confirmed critical failure triggers containment even if the recurrence threshold has not been met. A noncritical candidate investigation requires at least three reviewer-confirmed cases from distinct case and source-origin clusters; this is an investigation trigger, not proof of generality.

## Candidate boundary

Write a separate candidate with rationale, affected rule/claim IDs, source or fixture locators, counterexamples, scope, expected effect, previous/candidate hashes, and rollback target. Keep model/runtime, evidence, evaluation contract, and routing-description identity fixed. The candidate author must not see protected labels. Do not edit canonical guidance or source records during evaluation.

## Replay decision

Compare a frozen baseline and candidate on emerging cases and historical replay, with a separately reported ambiguous/needs-work slice. Reject on protected-label exposure, routing/model/runtime drift, any critical miss, false-ready critical case, or historical replay regression. No aggregate score can offset a critical regression. Insufficient independent cases, verified labels, uncertainty evidence, or independent review yields `NOT_ASSESSED`. Keep the accepted workflow active in every non-accepting state.

The executable helper returns only `rejected`, `not_assessed`, or `eligible_for_authorized_review`. The last state is a handoff to an authorised maintainer after independent review; it is not promotion. The helper has no write path to canonical guidance and cannot authorize or perform production changes. Its synthetic scenario demonstrates a negative replay result only.
