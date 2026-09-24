# Quantitative Analytics Method

[Owning skill](../SKILL.md) | Pair with `../../data-quality-pipeline/references/analytics-quality-method-gate.md`

Load this when a research product rests on a dataset, dashboard, statistical test, forecast,
model, or optimisation. The method gate decides whether the data can bear the claim; this
reference governs how the analysis is run and reported once it passes.

## Inputs

- The decision or knowledge claim the numbers must support, in one sentence.
- The dataset(s) with source tier, licence, collection method, grain, and time coverage.
- A codebook or data dictionary (build one before analysis if none exists).
- The intended claim strength: descriptive, diagnostic, predictive, or prescriptive.

## Procedure

1. **Frame.** Write the claim and the question type. If the reader needs a prescriptive answer
   but the data only supports description, say so now and narrow the claim.
2. **Admit the data.** Record source tier, licence, grain, period, and known collection bias.
   Run `analytics-quality-method-gate.md`; a failed gate downgrades the claim, it does not stop
   reporting.
3. **Profile before cleaning.** Completeness, validity, accuracy, consistency, timeliness,
   referential integrity, relevance, and privacy/authorisation. Use
   `../../data-quality-pipeline/references/quality-assessment-walker.md`.
4. **Clean with a trail.** Log every transformation with row counts before and after. Keep raw,
   cleaned, profile, and manifest artefacts separate. Joins follow
   `../../data-quality-pipeline/references/merge-discipline.md` (normalise grain first, assert
   cardinality, reconcile row counts).
5. **Choose the method by question and structure** (table below), not by what the tooling
   makes easy.
6. **Validate.** Hold-out or backtest anything predictive; test cluster stability; run
   sensitivity checks on the assumptions that move the result.
7. **Interpret.** State effect size and uncertainty, not only significance. Name what the
   design cannot rule out.
8. **Visualise** with an action title and a source note (chart rules below).
9. **Store provenance.** Code, assumptions, parameters, seed, and output tables sit with the
   finding so a second analyst can reproduce it.

## Method fit and guardrails

| Question | Typical methods | Guardrail that must be stated |
|---|---|---|
| How much / how often / which group | Summary statistics, cross-tabs, distributions | Denominator, period, and coverage gaps |
| Why did it move | Segmentation, variance decomposition, regression | Association is not causation without design logic (comparison group, timing, mechanism) |
| Which class | Classification | Labelled data exists; report precision, recall, and base rate, not accuracy alone |
| Which natural groups | Clustering | Exploratory until stable across seeds/samples and meaningful to a domain expert |
| What next | Time-series forecasting | Enough history, strict time ordering, backtest error, prediction intervals |
| What should we do | Optimisation, decision analysis | Explicit objective, constraints, and who holds decision authority |

Further rules:

- Name sampling error and variance whenever an estimate generalises beyond the observed rows.
- More features are not better on small datasets; prefer the simpler model when fit is similar.
- A significant p-value on a trivial effect is not a finding worth a headline.
- Outliers are classified (error, rare valid event, decision-relevant anomaly) and logged, never
  silently dropped.
- Data-quality failures are findings. Report them; do not hide them behind a clean chart.

## Reproducible implementation

- Scripted analysis (Python with pandas or Polars, or R) over spreadsheet hand-edits for any
  load-bearing number.
- Parse dates and types on load; fix encodings first (`../../data-quality-pipeline/references/encoding-and-unicode.md`).
- Notebooks are allowed for exploration; promote the final path to a script or a notebook that
  runs top to bottom without manual steps.
- Pin the environment (lock file or recorded package versions) with the output.

## Chart choice

| Reader need | Use | Avoid |
|---|---|---|
| One or two headline numbers | KPI tile with period and comparison | A chart for a single number |
| Change over time | Line chart | Bars for long continuous series |
| Compare categories | Sorted bar chart | Pie charts with many slices |
| Distribution | Histogram or box plot | Means without spread |
| Relationship | Scatterplot with fitted line and n | Implied causation in the title |
| Place explains the argument | Map | Maps where geography is incidental |
| Exact lookup | Table | Charts readers must squint at |

Never publish 3D charts, unlabelled units, decorative colour, or forecasts without intervals.
Visual styling routes to the design engine; this reference owns what the chart must claim.

## Finding format (every analytical finding)

`Claim | Dataset and period | Method | Result with uncertainty | Limitation | Implication | Next evidence or action`

### Worked example (original; figures are illustrative, not data)

A district health team asks whether a mobile-money reminder pilot raised antenatal
return visits in two Ugandan districts.

- Weak (generic): "The pilot significantly improved attendance, showing the power of digital
  health."
- Strong: "Return-visit rates in pilot facilities rose from 54% to 63% (Jan-Jun 2026, facility
  registers, n = 1,840 first visits); comparison facilities rose from 55% to 58%. The
  difference-in-differences estimate is +6 points (95% CI +1 to +11). Facilities were not
  randomised and two pilot sites gained a midwife in March, so the estimate may overstate the
  reminder effect. Implication: continue the pilot, add staffing as a covariate, and randomise
  the next rollout by facility."

## Failure modes

- Building a model because data exists, not because the decision needs one.
- Reporting a dashboard built on data that failed the quality gate.
- Forecast without backtest; clustering presented as discovered truth.
- Headline number without denominator, period, or source.

## Sources

Durable concept inputs, paraphrased and reorganised by task: Shikhman and Mueller (2021)
*Mathematical Foundations of Big Data Analytics*; *AI-Based Data Analytics: Applications for
Business Management*; *The Data Analytics Advantage*; *Data Analytics using Python*;
*Introduction to Data Analytics* (author and year for the last four: NOT_ASSESSED); the engine's
existing data-quality-pipeline references.

Evidence/currentness (2026-09-24): no tool version, API, or metric threshold is asserted here.
pandas and Polars are named as current, maintained libraries; version-specific behaviour is
NOT_ASSESSED and must be checked against their official documentation when code is written.
