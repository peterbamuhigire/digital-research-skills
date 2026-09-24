# Kaizen research loop

Use this loop after every research wave and again before release. It turns a research process into a small, auditable learning system rather than a sequence of searches.

## Loop

1. **Observe**: capture the wave scope, query set, source classes, access failures, claim defects, duplication, and analyst toil.
2. **Baseline**: record counts that can be reproduced: sources screened, sources admitted, claims created, claims verified, unresolved claims, contradictions, citation defects, and elapsed effort. Never invent a baseline.
3. **Select**: choose one bottleneck or waste category (`muda`) whose removal is safe and likely to improve decision quality.
4. **Hypothesise**: state `If we change X, then Y will improve because Z`, including a guardrail such as source diversity, verification coverage, or unresolved-claim count.
5. **Experiment**: run the smallest reversible change in the next wave or on a held-out sample. Keep the original path available for comparison.
6. **Check**: compare the same measures and inspect failed paths, contradictions, false positives, and analyst/user effort.
7. **Standardise**: update the responsible skill, template, routing rule, or validator only when the evidence supports the change. Record the source and review date.
8. **Teach and re-measure**: add a worked example or fixture, brief operators, and re-run the measure in the next wave.

## Evidence record

| Field | Required content |
|---|---|
| Loop ID | Stable identifier and date |
| Observation | Defect, waste, gap, or user need with source/artefact locator |
| Baseline | Reproducible numerator, denominator, unit, and period |
| Hypothesis | Change, expected outcome, rationale, and guardrail |
| Experiment | Scope, comparison, owner, authorization, and stop condition |
| Result | Same measures, uncertainty, failed-path result, and contradictions |
| Standard | Exact skill/reference/template/validator changed, or reason not to standardise |
| Next cycle | Owner, due date, and re-measurement method |

## Research-specific guardrails

- A faster search that reduces source diversity or verification coverage is a failed experiment.
- A higher citation count is not improvement if claim-source fit or independence worsens.
- Treat inaccessible, incomplete, historical, or corrupted sources as explicit uncertainty states.
- Keep source records immutable; remediate the process or claim status separately.
- Route current legal, regulatory, platform, safety, vendor, and market assertions to current-source verification.

## Source input status register

Label every book, report, or dataset admitted as a process input before it shapes a standard:

| Status | Treatment |
|---|---|
| Readable and current | Admissible for concepts; current facts still need primary-source verification |
| Historical (older edition, dated platform or product claims) | Durable concepts only; replace versions, APIs, benchmarks, and legal claims with current sources |
| Partial (early release, missing chapters) | Cite only what was available; never present it as a complete standard |
| Unreadable or corrupted extraction | Not admitted; re-ingest a lawful readable copy before attributing anything to it |

Book-derived knowledge enters the engine only as paraphrased, task-oriented skill references; staging notes and extractions stay outside the repository.
