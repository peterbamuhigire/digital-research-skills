# Automated Reliability Triage

Automated reliability scoring is allowed only as triage. It may prioritise what
an analyst reviews first; it may not certify a source, promote a claim, or
replace the engine's source-evaluation rules.

This reference is based on the user-provided implementation note from
2026-05-16 and field-practitioner OSINT methodology sources listed below. The
practitioner sources are useful workflow prompts, but remain tier-5 unless
independently verified.

## When To Use

Use this reference when a project has too many candidate URLs for immediate
manual review, or when a fact-checking / OSINT workflow needs queue ordering.

Do not use it when the project has only a small number of high-stakes sources.
In that case, run `source-evaluation` manually.

## Core Rule

The score breakdown is the product. The composite score is only a sorting aid.

Every automated assessment must expose:

- domain / publisher signal;
- item-level evidence signal;
- claim-category freshness;
- cross-source independence;
- information veracity / evidence sufficiency;
- human-review flags;
- missing evidence.

If those fields are hidden, the score does not ship.

Separate source quality from claim truth. FIRST's CTI source-evaluation
curriculum separates source reliability from information reliability using
Admiralty-style axes. The Berkeley Protocol separately discusses credibility,
reliability, and veracity for open-source investigations. Engine scoring must
therefore keep `source_reliability`, `information_veracity`, and
`evidence_sufficiency` separate unless an analyst explicitly explains why they
are being combined for queue ordering.

## Axis 1: Domain / Publisher Signal

Domain reputation is a prior, not a verdict. A credible outlet can publish a
weak opinion item, and a generally weak outlet can publish a well-sourced
investigation.

Record publisher, owner / funder if known, author identity if visible, editorial
genre, and any prior reliability note from the project.

Human-review flags:

- high domain score but weak item-level evidence;
- low domain score but strong item-level evidence;
- source genre unclear;
- author or publisher hidden where they should be visible.

## Axis 2: Item-Level Evidence

Do not let domain reputation swallow the actual article or record.

Inspect whether the item contains primary documents, datasets, direct records,
named sources, links, and a clear distinction between fact, analysis, and
opinion.

Human-review flags:

- strong claim with no named evidence;
- direct quote with no original transcript, recording, or document;
- statistic without an identifiable source;
- report cites another report instead of the primary record.

Claim-level evidence is the unit of review. Dataset designs such as FEVER and
AVeriTeC model claims with attached evidence and labels rather than relying on
document reputation alone. Engine triage should therefore attach every
assessment to a `claim_id`, `source_id`, evidence locator, and verification
state. Use explicit states for `not_enough_evidence` and
`conflicting_or_cherry_picked` instead of forcing a binary result.

## Axis 3: Claim-Category Freshness

Freshness depends on the claim type. A single recency parameter is misleading.

| Claim category | Freshness posture |
|---|---|
| Active event / breaking news | Fast decay; old items need an explicit timestamp warning. |
| Political quote / speech | Original transcript, recording, or contemporaneous source outranks later summaries. |
| Scientific / technical claim | Authoritative reviews, standards, and peer-reviewed work may outrank newer press releases. |
| Legal / regulatory claim | Current official text and effective date control; stale commentary is not enough. |
| Definition / stable background | Recency has low weight unless the definition is contested or recently changed. |
| Company / person / product status | Verify current official record because roles, ownership, pricing, and availability change. |

Human-review flags:

- source date missing;
- claim category not assigned;
- current-looking article relies on old underlying data;
- old but authoritative source is penalised without category justification.

## Axis 4: Cross-Source Independence

Count independent source clusters, not URLs.

Eight articles from the same wire, press release, or syndication chain are one
confirmation cluster. Two outlets under the same owner or quoting the same
unnamed source may also be one weak cluster.

Cluster by primary origin, publisher / owner, wire service or press-release
source, author byline, shared text, geography, language family, and cited
evidence chain.

Human-review flags:

- many URLs collapse to one original source;
- confirmation comes from commentary on commentary;
- different outlets repeat identical language;
- no independent primary record found;
- coordinated campaign or citation-laundering risk.

Add a `leaked_factcheck_source` flag for fact-checking pipelines. Automated
retrieval can accidentally rediscover the fact-check article, dataset item, or
syndicated copy that supplied the label. That is not independent evidence.

## Composite Score

Use a composite only for queue ordering. Store the axis values and review flags
beside it.

Recommended shape:

```yaml
source_assessment:
  source_id: SRC-0001
  claim_id: CLM-0001
  assessed_at: "YYYY-MM-DD"
  claim_category: active-event
  source_reliability: medium
  information_veracity: not_enough_evidence
  evidence_sufficiency: low
  domain_signal: medium
  item_signal: low
  freshness_signal: high
  independence_signal: low
  composite_triage: medium-priority-review
  review_flags:
    - many URLs collapse to one source cluster
    - high freshness but weak item evidence
  analyst_decision: pending
```

Allowed composite labels: `high-priority-review`, `medium-priority-review`,
`low-priority-review`, `do-not-use-without-human-review`.

Do not use labels such as `true`, `false`, `trusted`, or `fake`. Those are claim
adjudications, not triage outcomes.

## Calibration

Calibrate on real resolved cases before trusting weights. The user-provided
implementation note reports that weights that looked strong on paper performed
poorly on actual disputed claims; the fix was to tune against labelled cases
with known outcomes.

Minimum calibration log:

- case ID;
- claim category;
- ground-truth decision and source of that decision;
- axis scores before analyst review;
- analyst decision;
- error type: false confidence, missed corroboration, stale source,
  citation-laundering, wrong category, or other;
- weight adjustment, if any.

If no labelled cases exist, say so and treat all automated output as
experimental queue ordering.

Confidence is not the same as score. Keep model confidence, analyst confidence,
and source reliability in separate fields. Calibrate confidence on held-out
verification cases where possible; route low-calibration domains or claim
categories to human review.

## Structured Metadata

`ClaimReview` markup can help discover and normalise published fact-checks, but
markup is not truth. Ingest `ClaimReview` fields as metadata, then independently
verify the underlying claim, reviewed source, evidence, date, and rating.

## Explainability Gate

Each automated assessment must include:

- input signals used;
- input signals missing;
- source / evidence chain;
- independence-cluster rationale;
- known limits;
- reason for human review, if flagged.

Do not output "reliable" or "unreliable" without rationale.

## Source Notes

- Dutch OSINT Guy, "OSINT Is A State Of Mind," Medium, 2018-01-14:
  https://medium.com/@Dutchosintguy/osint-as-a-mindset-7d42ad72113d.
- AaronCTI, "My OSINT Blueprint - Methodology and Tools Part One," 2024-05-02:
  https://aaroncti.com/my-osint-blueprint-methodology-and-tools-part-one/.
- AaronCTI, "My OSINT Blueprint - Methodology and Tools Part Two," 2024-10-06:
  https://aaroncti.com/my-osint-blueprint-methodology-and-tools-part-two/.
- CQCore, "OSINT Methodology," 2024-05-09:
  https://www.cqcore.uk/osint-methodology/.
- Sector035, "Week in OSINT #2023-06," 2023-02-13:
  https://sector035.nl/articles/2023-06.
- FIRST CTI SIG, "Source Evaluation":
  https://www.first.org/global/sigs/cti/curriculum/source-evaluation.
- Berkeley Protocol on Digital Open Source Investigations:
  https://humanrights.berkeley.edu/wp-content/uploads/2024/02/Berkeley-Protocol.pdf.
- FEVER dataset: https://fever.ai/dataset/fever.html.
- AVeriTeC dataset: https://fever.ai/dataset/averitec.html.
- TACL survey, "Automated Fact-Checking":
  https://aclanthology.org/2022.tacl-1.11.pdf.
- CREDULE / EVVER:
  https://arxiv.org/abs/2404.18971.
- NIST, "Four Principles of Explainable Artificial Intelligence":
  https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence.
- Schema.org `ClaimReview`: https://schema.org/ClaimReview.
- Google Fact Check structured data documentation:
  https://developers.google.com/search/docs/appearance/structured-data/factcheck.
- Guo et al., "On Calibration of Modern Neural Networks":
  https://arxiv.org/abs/1706.04599.
- NIST AI Risk Management Framework:
  https://www.nist.gov/itl/ai-risk-management-framework.
- NATO StratCom COE note on information laundering:
  https://stratcomcoe.org/news/a-new-report-focuses-on-information-laundering-in-the-nordic-baltic-region/133.
- Bellingcat Information Laundromat:
  https://bellingcat.gitbook.io/toolkit/more/all-tools/the-information-laundromat.
