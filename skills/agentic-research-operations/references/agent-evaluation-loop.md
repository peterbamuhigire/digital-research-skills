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

## Local Source Register

- `C:\Users\Peter\Downloads\Documents\res_markdown\AI Engineering (for True Epub).md`
- `C:\Users\Peter\Downloads\Documents\res_markdown\Developing AI Applications - An Introduction.md`
- `C:\Users\Peter\Downloads\Documents\res_markdown\Teaching with AI A practical guide to a new era of human learning.md`
