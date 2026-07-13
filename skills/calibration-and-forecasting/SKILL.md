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

## Forecast Intake Guidance

- Forecast question, time horizon, base rate, alternatives, evidence set, and decision use.
- Prior judgment if one exists, including probability, date, rationale, and trigger indicators.
- Source register and uncertainty discipline from companion skills.

## Forecast Method Detail

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

## Forecast Failure Notes

- Forecast without a resolution date.
- "Likely" with no numeric anchor.
- Confidence in a source treated as probability of an event.
- Scenario prose that cannot be scored later.
- Model output treated as calibrated without validation.

## Forecast Deliverable Detail

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

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Resolvable question, horizon, evidence, base rate | Analyst and verified corpus | Stop; return a question-design gap |
| Prior forecasts and scoring rule | Forecast register | Start a labelled uncalibrated baseline |

## Capability Contract

Forecasting and review are read-only. Operational action, market transactions, publication, or changing decision thresholds requires explicit authority.

## Degraded Mode

Without base rates or outcome data, provide conditional scenarios and mark calibration and scoring `not assessed`.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Question is not resolvable | Rewrite it | Unscoreable forecast |
| New evidence changes odds | Timestamp an update | Hindsight rewriting |
| Outcome cannot be observed | Use scenario analysis | False calibration claim |

## Forecast Scenario

A forecast with no observable resolution criterion is rewritten before any probability is assigned.

## Companion Skills

- `source-evaluation` runs before this skill.
- `analytic-tradecraft` supplies hypothesis and estimative-language discipline.
- `decision-support-analysis` turns forecasts into decisions and options.
- `evidence-claim-graph` preserves forecast evidence and updates.

## Workflow

1. Rewrite the question so outcome, horizon, and resolution source are observable.
2. Establish base rates, evidence, and scoring before assigning probability.
3. Stop when the question is unresolvable or decisive evidence lacks provenance.
4. Recover by reformulating the question or returning conditional scenarios with calibration unassessed.
5. Timestamp updates and score after resolution without rewriting history.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Forecast card and calibration record | Decision-maker and forecast reviewer | Question, horizon, probability, rationale, update history, resolution source, and score are present |

## Anti-Patterns

- Forecasting an unresolvable question. **Fix:** define an observable outcome and deadline.
- Ignoring base rates. **Fix:** record the relevant reference class.
- Rewriting after new evidence. **Fix:** preserve timestamped updates.
- Confusing source reliability with probability. **Fix:** assess them separately.
- Claiming calibration without outcomes. **Fix:** mark scoring unassessed.

## Worked Example

A forecast lacking a named resolution source is rewritten before probability assignment, preventing later disagreement about whether the outcome occurred.
