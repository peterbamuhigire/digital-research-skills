# Agent Evaluation Loop

## Accept / Reject Gate

Accept an agent output only when:

- Scope matches the brief.
- Every load-bearing claim has a source reference.
- Quotes are verifiable or marked for verification.
- Gaps are explicit.
- Inferences and synthesis are labelled.
- Output has enough structure to merge into the claim graph.

Reject or quarantine when:

- A named source, URL, law, organization, person, or statistic appears unsourced.
- A direct quote lacks a locator.
- The output substitutes plausible narrative for "no source found."
- The agent performs cross-cohort synthesis without being asked.

## Evaluation Loop

1. Run source spot checks.
2. Map claims to registry IDs.
3. Compare against prior wave gaps.
4. Merge supported claims.
5. Log rejected claims or hallucination risks in the evidence audit.
6. Update the next brief to prevent repeat failure.

## Failure attribution and revision provenance

Keep the observed symptom tags and record one primary cause separately. Use `routing`, `knowledge`, `execution`, `source/tool`, `gold-label`, `mixed`, or `unknown`; an unclear disagreement stays `unknown` or `mixed` instead of becoming a guidance edit. Existing symptom tags remain valid: `retrieval-miss`, `citation-drift`, `quote-error`, `unsupported-claim`, `reasoning-gap`, `tool-failure`, `format-mismatch`, `latency-cost`, and `unsafe-output`.

Only reviewer-confirmed recurring knowledge gaps enter a guidance-revision proposal. Routing, runtime, source/tool, and label errors go to their own repair paths. Keep a portable provenance record with source/evaluation case IDs, immutable locators or permitted snapshot hashes, reviewer/adjudication state, candidate diff and hash, unchanged routing-description/model identifiers, emerging-case results, historical replay results, and rollback target. Do not depend on local machine paths or store source/book extracts in this reference.

The offline replay gate in `../ai-evaluation-and-data-flywheel/references/replay-gated-skill-revision.md` can reject a candidate on supplied, explicit regression labels. It cannot establish that those labels are true or authorize promotion. Protected labels remain unavailable to the proposer; automatic self-modification remains disabled.
