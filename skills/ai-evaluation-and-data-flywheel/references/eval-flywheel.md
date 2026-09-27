# Eval Flywheel

## Eval Case

| Field | Requirement |
|---|---|
| id | Stable case ID |
| task | User-like request |
| inputs | Immutable files, source snapshots/locators, and context; record content hashes where permitted |
| expected checks | Observable criteria |
| source integrity checks | Required citation/quote/URL checks |
| known failure | What this case protects against |
| status | active, retired, candidate |

### Research packet extension

For research-evaluation cases, add the fields needed to judge the packet as a whole without weakening item-level verification:

- `decision`, `scope`, `jurisdiction`, `as_of`, and task/risk class;
- selected sources and their original order/rank, with the reason for that order kept separate from source authority;
- source-origin or dependency clusters so copies and syndications do not count as independent corroboration;
- claim IDs, source/evidence locators, source snapshots or hashes, known gaps, unresolved contradictions, and the candidate synthesis;
- reviewer-expected criteria and findings, severity, support state, release state, and rationale, held back from candidate runs on protected cases;
- split, project/time/source-family clusters, reviewer/adjudication record, privacy/licence basis, and synthetic-data flag;
- criterion IDs and versions actually loaded, plus model/runtime/configuration IDs for every run.

Do not replace the source/claim registries or source verifier with a packet score. Retrieval rank is not evidential authority. Missing evidence is `NOT_ASSESSED`, not a pass; an unresolved critical contradiction or mandatory-control miss blocks `ready`.

### Evidence-set evaluation

Evaluate both item-level support and whether the set supports the decision. Review question coverage, source-origin independence, semantic duplication, claim-appropriate authority, method fit, complementary evidence, contrary evidence, and unresolved gaps. Record which findings are directly supported, synthesized, or inferred and link every material finding to source/claim locators.

Keep outcome labels separate: `ready`, `needs-work`, `blocked`, and `NOT_ASSESSED/abstain`. Reasons and severity are required; a single averaged score cannot conceal a critical miss or an ambiguous boundary case. The reviewer may mark a criterion `not_applicable` only with a scope-based reason. This is a Chwezi evaluation design, not a claim about another system's validated rubric.

### Protected evaluation splits

Create development, calibration, emerging-pattern holdout, and historical replay sets only after a value triage confirms a recurring need and usable cases exist. Split by project, source origin/family, and time; keep copies of one source in one cluster; remove near-duplicates across splits. Lock expected criteria, labels, and reviewer explanations on holdouts. If a case or its explanation influenced a rule change, it cannot remain an untouched holdout.

Sample sizes and acceptance margins are not defaults. Set them from observed prevalence, consequence, variance, reviewer capacity, and the planned comparison. If evidence is too small to distinguish safe from unsafe changes, retain the current workflow and report the affected acceptance slice `NOT_ASSESSED`.

### Failure attribution and revision boundary

Use a separate primary-cause label: `routing`, `knowledge`, `execution`, `source/tool`, `gold-label`, `mixed`, or `unknown`. A failed outcome is not automatically a knowledge gap. Preserve the original symptom tags and source records. Only a reviewed, recurring knowledge gap may propose a guidance edit; routing, tool/source, execution, or gold-label errors have their own repair paths.

Freeze the model, runtime, evidence, and evaluation contract when comparing routing strategies. Keep mandatory provenance, currentness, security, privacy, and domain controls always-on. The candidate cannot inspect protected labels, mutate production, promote itself, or change canonical source records. Promotion requires independent review, zero new critical misses, protected emerging cases, historical replay, uncertainty and slice results, and an authorised maintainer decision.

## Failure Tags

- `retrieval-miss`
- `citation-drift`
- `quote-error`
- `unsupported-claim`
- `reasoning-gap`
- `tool-failure`
- `format-mismatch`
- `latency-cost`
- `unsafe-output`

## Flywheel Rule

Only promote a feedback example into the eval set after a human or verifier confirms the expected behavior and source truth.
