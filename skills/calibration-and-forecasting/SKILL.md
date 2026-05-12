---
name: calibration-and-forecasting
description: Use when research output makes forecasts, probability judgments, risk calls, market outlooks, scenario likelihoods, warning indicators, or confidence claims that must be calibrated, scored, updated, and separated from source reliability.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Calibration And Forecasting

<!-- dual-compat-start -->

## Use When

- Use when output contains forecasts, likelihoods, risk rankings, early-warning indicators, market outlooks, adoption estimates, probability language, or confidence claims.
- Use when a project must track accuracy over time, update judgments after new evidence, or compare rival forecasts.
- Use when `analytic-tradecraft` identifies uncertainty and the project needs calibration discipline beyond prose hedging.

## Do Not Use When

- The output is purely descriptive and contains no probability, forecast, or risk judgment.
- A domain-prescribed grading framework controls the judgment.

## Required Inputs

- Forecast question, time horizon, base rate, alternatives, evidence set, and decision use.
- Prior judgment if one exists, including probability, date, rationale, and trigger indicators.
- Source register and uncertainty discipline from companion skills.

## Workflow

1. Frame the forecast as a resolvable question: event, threshold, geography/entity, time window, and resolution source.
2. Establish the outside view: relevant base rates, historical analogues, and reference class limits.
3. Add the inside view: current evidence, mechanism, constraints, incentives, and weak signals.
4. Generate alternatives: at least one rival path and one failure mode for the favored forecast.
5. Assign probability using numeric bands; never ship vague verbal confidence alone.
6. Separate event probability, source reliability, and analyst confidence.
7. Name update triggers: indicators that would raise, lower, or retire the forecast.
8. Record the forecast with date, horizon, rationale, and resolution rule.
9. When the horizon closes, score the forecast and log lessons.

## Quality Standards

- Forecasts are falsifiable, time-bounded, and resolvable.
- Probability language includes numeric bands and matches the project lexicon.
- Base rates are considered before vivid current evidence.
- Every probability change states what new evidence caused the update.
- Accuracy learning is preserved; forecasts are not overwritten without history.

## Anti-Patterns

- Forecast without a resolution date.
- "Likely" with no numeric anchor.
- Confidence in a source treated as probability of an event.
- Scenario prose that cannot be scored later.
- Model output treated as calibrated without validation.

## Outputs

- Forecast card with question, probability, base rate, evidence, alternatives, indicators, and resolution rule.
- Update log for changed judgments.
- Calibration review with resolved forecasts and lessons.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Correctness | Forecast card | Markdown/YAML | `forecast_id`, event, horizon, probability, alternatives |
| Release evidence | Calibration log | Markdown table | Prior probability, update trigger, new probability |

## References

- Load `references/forecast-card.md` for forecast templates and update records.
- Load `references/calibration-gates.md` for ship gates, scoring, and anti-patterns.

<!-- dual-compat-end -->

## Companion Skills

- `source-evaluation` runs before this skill.
- `analytic-tradecraft` supplies hypothesis and estimative-language discipline.
- `decision-support-analysis` turns forecasts into decisions and options.
- `evidence-claim-graph` preserves forecast evidence and updates.
