# Analytics Quality Method Gate

Use this gate before running statistical tests, forecasts, machine-learning models,
dashboards, or quantitative research claims.

## Gate Questions

1. What question is being answered: descriptive, diagnostic, predictive, or prescriptive?
2. What is the dataset grain?
3. What is the source reliability tier?
4. What fields are required for the method?
5. Are missing values random, systematic, or meaningful?
6. Do joins preserve the expected row count and business key?
7. Are outliers errors, rare valid events, or decision-relevant anomalies?
8. Does the sample size support the intended claim?
9. Is personal or sensitive data minimized and authorized?
10. Can the analysis be reproduced from raw source to final output?

## Method Fit Rules

- Descriptive analysis needs clean definitions and complete enough coverage.
- Diagnostic analysis needs dimensions that can explain variation.
- Predictive analysis needs historical depth, target labels or future actuals, and
  validation data.
- Prescriptive analysis needs constraints, objectives, and decision authority.

If the dataset fails the method fit rule, downgrade the claim. A failed predictive dataset
may still support descriptive or diagnostic work.

## Required Manifest Additions

Add these fields when a dataset feeds analytics:

- `analytics_question_type`
- `decision_or_claim_supported`
- `dataset_grain`
- `required_fields`
- `method_fit_assessment`
- `sample_or_history_depth`
- `known_biases`
- `privacy_notes`
- `analysis_limitations`

## Anti-Patterns

- Building a model because a dataset exists.
- Treating correlation as a causal finding.
- Publishing forecasts without backtesting or intervals.
- Cleaning away outliers without recording them.
- Combining datasets before reading codebooks.
- Reporting a dashboard from data that failed the quality gate.
