# Data Analytics Research Method Extraction

Sources:

- *Mathematical Foundations of Big Data Analytics*
- *AI-Based Data Analytics: Applications for Business Management*
- *The Data Analytics Advantage*
- *Data Analytics using Python*
- *Introduction to Data Analytics*

Use this extraction when quantitative data, datasets, dashboards, forecasts, models, or
decision-support evidence appear in a research product.

## Core Analytics Ladder

Research analytics should be explicit about the question type:

- Descriptive: what happened, how much, how often, which group, which trend.
- Diagnostic: why it happened, which driver, which segment, which anomaly.
- Predictive: what may happen next, with what probability or uncertainty.
- Prescriptive: what should be done, under which constraints and trade-offs.

Do not present predictive or prescriptive claims when the data only supports descriptive
or diagnostic analysis.

## Research Analytics Workflow

1. Define the decision or knowledge claim the data must support.
2. Identify the dataset, source reliability, grain, time coverage, and licence.
3. Build a data dictionary or codebook before analysis.
4. Profile completeness, duplicates, outliers, entity integrity, and category codes.
5. Clean and transform with a logged row-count trail.
6. Select the analysis method by question and data structure.
7. Interpret results with limitations, uncertainty, and source caveats.
8. Visualize the result with an action title and source note.
9. Store provenance, cleaned outputs, assumptions, and reusable code.

## Mathematical Guardrails

- Probability, variance, and sampling error should be named when estimates are uncertain.
- Regression and correlation do not prove causation without design logic.
- Classification requires labels and fit-for-purpose metrics, not accuracy alone.
- Clustering is exploratory until validated by stability and domain meaning.
- Forecasts need historical depth, time ordering, backtesting, and intervals.
- Optimization needs an explicit objective function and constraints.
- More features are not automatically better; small datasets suffer from overfitting.

## Python Analytics Pattern

Use Python for:

- Data cleaning and feature engineering.
- Pandas or Polars transformations.
- Statistical tests.
- Time-series forecasting.
- Classification, clustering, or anomaly detection.
- Reproducible charts and dashboards.
- Exporting clean tables for Word/Excel/PDF outputs.

Minimum implementation discipline:

- Parse dates and types on load.
- Normalize data grain before joining.
- Validate merge cardinality.
- Keep raw, cleaned, profile, and manifest artifacts separate.
- Make notebooks reproducible or promote logic into scripts.
- Save assumptions with the output.

## Data Quality Dimensions

Assess every analytical dataset on:

- Completeness.
- Validity.
- Accuracy.
- Consistency.
- Timeliness.
- Integrity.
- Relevance.
- Privacy and authorization.

Data quality failures are findings. They should be reported rather than silently hidden.

## Visualization and Dashboard Rules

Analytics visuals must answer a research question:

- KPI cards for one or two headline numbers.
- Line charts for time trends.
- Bar charts for categorical comparison.
- Histograms or box plots for distributions.
- Scatterplots for relationships.
- Maps only when location explains the argument.
- Tables when readers need exact values or lookup.

Avoid 3D charts, unlabeled units, decorative colour, unexplained forecasts, and visuals
that hide uncertainty.

## Decision-Quality Output

Every analytical finding should state:

- Claim.
- Dataset and period.
- Method.
- Result.
- Limitation or uncertainty.
- Implication.
- Recommended next evidence or action.
