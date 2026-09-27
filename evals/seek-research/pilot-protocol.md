# SEEK-inspired research evaluation pilot protocol

**Status:** design only; no labelled pilot cohort or performance result exists.
**Owner:** Digital Research evaluation owner; reviewer and annotation capacity not yet assigned.
**Purpose:** determine whether selectively loaded review criteria improve whole-evidence-set assessment while preserving current source admission, claim verification, and release controls.

## Evidence and transfer boundary

### Paper-derived information

The input is SEEK v1, an arXiv preprint submitted 2026-09-24. Its evaluation object is a ranked search-results page assessed as a whole, with item-level and multi-dimensional diagnoses. Its authors report experimental results for an industrial short-video search setting. The study notes and page-level details remain in `skills-kaizen/08-seek-paper-study.md`; this protocol does not reproduce the training stack, production claims, thresholds, or reported outcome as Chwezi evidence.

**Source record:** Zhongxin Huang et al., “SEEK: Skill-Routed Evaluation with Evolvable Knowledge for Industrial Search,” arXiv:2609.29803v1 (S17), submitted 2026-09-24; official arXiv record checked 2026-09-27. The versioned bibliographic record is retained in the Kaizen source register; a separate archival snapshot remains `NOT_ASSESSED`. Freshness: `partial` and version-pinned. The checked record listed v1 only; venue/DOI fields in the PDF are not treated as publication evidence. Supported claim: what the versioned paper proposes and reports about its own experiment. Transfer efficacy, Chwezi performance, reproducibility, costs, and production benefit: `NOT_ASSESSED`. Recheck at the source register's review date, 2026-10-03, or sooner if a new version or implementation decision appears.

### Existing failure triage

Reviewed bounded records, not a representative production sample:

| Record | Observed result | What it establishes | What remains open |
|---|---|---|---|
| P02 source-verifier boundary cases: stale source, future-effective source, unsupported live URL, wrong denominator, conflicting primary sources | Deterministic tests passed; semantic support states were supplied by human review | Item-level quarantine and release-readiness boundaries work for these fixtures | The verifier does not discover semantic mismatches or evaluate research-packet coverage |
| P07 synthetic stale-source replay | Stale source quarantined its dependent claim; missing dependency IDs were exposed; `release_ready=false` | Currentness and dependency failure are visible in the bounded synthetic path | It is one synthetic case, not evidence of prevalence or general performance |
| P07 verified source-to-decision chain | URL/currentness passed, but an inference remained a warning and `release_ready=false` | Metadata and reachability do not certify semantic support | No whole-packet source-dependence, coverage, or criterion-selection outcome was scored |

P05 is a Windows activity-report evaluation and supplies no research-evaluator behavior evidence. The triage therefore supports a narrow missing **evaluation contract** for research packets, but not a claim that current research outputs are failing or that a new evaluator will improve them. Existing source-evaluation, source-verification, evidence-claim-graph, and critical-reasoning skills retain their distinct owners.

### Required synthetic acceptance pattern

Before pilot use, an acceptance fixture must include eight apparently relevant pages derived from one source, one historically accurate primary source that falls outside the stated target period, and one material unresolved contrary result. It passes only when the evaluator groups the copied pages as one origin, retains the target-period gap, links the contradiction to its source and claim, and refuses a `ready` result when the missing or unresolved evidence is decision-critical. The fixture must be labelled synthetic; it is a behavior check, not evidence of real research quality or failure prevalence.

## Chwezi adaptation: criterion map

The paper's criterion names below are retained only to map concepts. These are proposed Chwezi review criteria, owned by existing skills; they do not create twelve skills or new release authority.

| Paper criterion | Proposed packet-level question | Existing owner / boundary |
|---|---|---|
| MainIntentMatch | Does the evidence address the stated decision question and scope? | `research-orchestration`; the brief owns the question |
| TaskNeedSatisfaction | Would the verified findings enable the intended decision? | `critical-reasoning-and-argument`; usefulness is not source truth |
| RankingFaithfulness | Are the strongest decision-relevant findings prominent? | `evidence-claim-graph`; retrieval order never establishes authority |
| InformationValueCheck | Does each included item add a distinct supported proposition? | `critical-reasoning-and-argument`; prose quality cannot substitute for evidence |
| FactualReliabilityCheck | Are material claims supported at exact locators, with scope/date preserved? | `source-verification`; remains an item-level gate |
| RiskComplianceCheck | Are mandatory risk, privacy, currentness, and domain boundaries met? | `source-evaluation` plus the domain owner; mandatory checks cannot be routed away |
| SourceDiversityCheck | Are purportedly independent sources genuinely independent in origin? | `source-evaluation`; count source families, not copied pages |
| TemplateDuplication | Does repetition add evidence or only repeat the same source/claim? | `ai-evaluation-and-data-flywheel`; preserve distinct corroboration |
| SubIntentCoverageCheck | Are required subquestions, countercases, and decision gaps represented? | `research-orchestration`; evaluator cannot invent missing evidence |
| SourceAuthorityCheck | Does each source have authority appropriate to its specific claim? | `source-evaluation`; official status is not infallibility |
| EvidenceProfessionalism | Does the method and expertise fit the claim and decision? | `source-verification` plus qualified domain review |
| HeterogeneousFulfillment | Are complementary evidence types present where the decision requires them? | `evidence-claim-graph`; diversity is functional, not decorative |

### Always-on controls and selected criteria

Always-on: instruction/data separation, source identity and provenance, material claim support, currentness when relevant, privacy/security boundaries, and the owning domain's mandatory safety controls. A criterion router may select additional question-fit, coverage, independence, duplication, authority, method-fit, and complementarity checks; it cannot turn off an always-on control.

Selected criteria are versioned and their **actual loaded IDs** are recorded. A threshold is a routing setting, not a calibrated probability. Begin only with transparent rules or an explicitly logged candidate; preserve abstention and reviewer escalation. Keep the current workflow as the authority until acceptance gates pass.

## Case and annotation contract

Each future case records:

- stable case/task/risk IDs, question, decision, scope, jurisdiction, and `as_of` date;
- immutable source IDs and snapshots/hashes where lawful, original selection order and its reason, source-origin clusters, claims, locators, evidence links, gaps, and contradictions;
- candidate synthesis and required output, with output claims linked back to the evidence set;
- applicable/mandatory criteria, reviewer-expected findings, severity, support state, expected release state, and reason;
- split, project/source-family/time grouping, provenance, reviewer IDs, adjudication, licence/privacy class, and `synthetic` flag;
- criterion-bank version and loaded IDs, model/runtime/prompt/configuration identifiers, and observed latency/cost if available.

Expected labels are assigned from source locators by qualified reviewers. Use a second reviewer for critical or disputed cases; adjudicate disagreement with a recorded basis. A model or teacher proposal is not gold truth. No private chain-of-thought is requested or stored. If a source or expected label cannot be verified, quarantine the case or set the relevant value to `NOT_ASSESSED`.

## Candidate split plan

Potential sets: development, routing calibration, emerging-pattern holdout, and historical replay. Group copied and syndicated material by origin; separate project and time clusters so related cases do not cross splits. Keep holdout labels and adjudication notes unavailable to candidate prompt/configuration authors. Any case used to author or revise a criterion leaves the untouched holdout.

The previously discussed 60/40/40/100 plan is a planning scenario only, not a quota, power calculation, or approved sample size. Do not create case indices or split IDs until real reviewed cases, source rights, project diversity, expected prevalence, risk, variance, and review capacity are known. If the ambiguous/needs-work slice is too small to evaluate safely, that gate stays `NOT_ASSESSED` and the current route remains active.

## Comparison and acceptance plan

Paired comparisons use identical evidence, output contract, approved model/runtime, and fixed prompt/configuration except for criterion access:

- **A — current workflow:** existing research routing and source/claim gates.
- **B — all proposed criteria:** diagnostic only; may expose criterion interference and context burden.
- **C — selected criteria:** selected extras plus mandatory controls.
- **D — human-selected criteria:** expert oracle for criterion selection, not a truth oracle for source claims.

Score mandatory-criterion recall; route precision/recall; whole-set decision support; source-origin independence; question/countercase coverage; semantic duplication; contradiction/gap preservation; item-level support and locator correctness; release-state confusion and critical false-ready rate; `NOT_ASSESSED` abstention quality; reviewer agreement/minutes; and cost/latency. Report risk and task slices, especially ambiguous/needs-work, separately. Engagement, criterion count, or aggregate F1 cannot stand in for research correctness.

Before running: preregister hypotheses, case eligibility, fixed model/runtime, randomisation/order/cache controls, paired analysis, score definitions, confidence method, noninferiority margins, exclusion rules, and stop/recovery steps. Derive margins from observed pilot variability and risk; do not copy SEEK's threshold or tolerance. Require zero new critical-control misses. Keep the existing workflow if the candidate is underpowered, worsens a critical slice, leaks holdout labels, or lacks independent review.

## Current decision and re-entry

- **Accepted now:** design-only criterion map and protocol, plus the bounded synthetic-only schema/evaluator described below; no operational routing change, training, data collection, or release authority.
- **Not yet accepted:** real-data labels, split IDs, performance thresholds, model configuration, or any behavior/performance claim.
- **Required to mobilise:** approved evidence-use basis; enough diverse and reviewed cases; named independent reviewers; held-out data protection; fixed candidate runtime; preregistered comparison; and a separate critical-control sentinel set.
- **Recovery:** if any source, label, split, runtime, or reviewer provenance is uncertain, quarantine it, preserve the current research workflow, and record the affected measure `NOT_ASSESSED`.

### P26 synthetic-only implementation boundary

The offline prototype is in `schemas/research-evaluation-case.schema.json`, `schemas/research-evaluation-result.schema.json`, and `tools/evaluation/research_evaluator.py`. Two fictional fixtures under `evals/seek-research/fixtures/` exercise source-origin clustering, a target-period coverage gap, an unresolved contrary result, and a dynamic-route miss on a tax/currentness criterion while the mandatory currentness guard blocks readiness. Its modes (`dynamic`, `all`, `oracle`, `supplied`) are structural route comparisons only; no model is called and the oracle mode is limited to synthetic/development/calibration records. These fixtures do not satisfy the reviewed real-case, protected-split, independent-review, or behavior-comparison gates above.

No real case count, routing quality, test accuracy, reviewer-time saving, cost/latency comparison, or improvement is claimed. `ready` means only that the recorded structural contract found no blocker; the evaluator is not a factual verifier or release authority.
