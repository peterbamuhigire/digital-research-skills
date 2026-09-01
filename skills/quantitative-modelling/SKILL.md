---
name: quantitative-modelling
description: "Use when research requires quantitative modelling: market sizing, triangulation, sensitivity analysis, scenario models, assumption registers, forecast models, data-quality caveats, and model audit checks."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Quantitative Modelling

<!-- dual-compat-start -->

## Use When

- Use for market sizing, financial sizing, demand estimates, scenario models, sensitivity tables, and quantified opportunity/risk analysis.
- Use when numeric assumptions must be traceable, stress-tested, and auditable.
- Use with data-quality companion skills when datasets are involved.

## Do Not Use When

- Numbers are only cited facts with no model or derived estimate.
- The user asks for qualitative analysis only.


## Quantitative Modelling Required Context
- Model question, units, time period, data sources, assumptions, constraints, and intended decision.
- Source register and data-quality notes.


## Quantitative Modelling Core Method Notes
1. Define the model purpose and decision use.
2. Separate source data, assumptions, formulas, and outputs.
3. Build at least two estimation paths when feasible.
4. Run sensitivity on load-bearing assumptions.
5. State uncertainty, data gaps, and model limits.
6. Link every input to a source ID or mark it as an assumption.
7. Produce an audit note before publication.

## Quality Standards

- Units, time periods, and populations are explicit.
- Assumptions are visible and stress-tested.
- Derived numbers are labelled as estimates.
- Precision does not exceed data quality.


## Quantitative Modelling Existing Failure Notes
- Single-path market sizing with no triangulation.
- False precision from weak data.
- Mixing populations or time periods.
- Hiding assumptions inside formulas.


## Quantitative Modelling Core Deliverables
- Assumption register.
- Model table.
- Sensitivity analysis.
- Model audit note.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Correctness | Assumption register | Markdown/YAML | Input, source, range, rationale |
| Release evidence | Model audit note | Markdown | Limits, sensitivity, confidence |

## References

- Load `references/model-audit-checklist.md` before shipping quantified outputs.

## Inputs

| Artefact | Source or provider | Requirement | If absent |
|---|---|---|---|
| Decision question, verified data, assumptions, and units | requester and source register | required | Produce an assumption-gap register if evidence is insufficient |

## Capability contract

Read access to source data, assumptions, formulas, and units is required. Model edits or execution need explicit authority; publishing forecasts or changing operational inputs requires decision-owner approval.

## Degraded mode

When evidence or calculation execution is unavailable, return a qualified model specification and assumption-gap register, with reconciliation and sensitivity checks marked unassessed.

## Decision rules

| Choice | Action | Failure avoided |
|---|---|---|
| Input is uncertain but decision-sensitive | Model a sourced range and label it | False precision |


## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Model, assumption register, scenarios, and audit record | decision-maker and peer reviewer | Units reconcile; formulas are traceable; sensitivity and limitations are reported |


## Quantitative Modelling Evidence Notes 1
- Preserve sourced assumptions, unit conversions, formulas, scenario bounds, reconciliation variances, and sensitivity results.

## Worked example

Represent an uncertain driver as low, base, and high sourced assumptions; show the result range and do not collapse missing evidence into a base case.

<!-- dual-compat-end -->

## Companion Skills

- `data-quality-pipeline` assesses datasets.
- `calibration-and-forecasting` governs probabilistic outputs.
- `source-verification` checks numeric claims.


## Workflow
1. Define the decision, units, model boundary, and evidence-backed inputs.
2. Build formulas and assumption ranges with traceable sources.
3. Stop when a decision-sensitive input has neither evidence nor a defensible range.
4. Reconcile and stress-test outputs; recover by widening uncertainty or returning an assumption gap.


## Quantitative Modelling Evidence Notes 2
| Evidence | Consumer | Acceptance |
|---|---|---|
| Assumption and model-audit register | Decision-maker and peer reviewer | Inputs, units, formulas, sensitivity, and limitations are traceable |


## Anti-Patterns
- Using an uncited numeric input. Fix: source it or mark a gap.
- Mixing units or periods silently. Fix: normalise and label them.
- Reporting a single estimate from uncertain inputs. Fix: show a sourced range.
- Hiding a circular formula or balancing plug. Fix: expose and test it.
- Treating an unassessed check as passed. Fix: mark it not assessed.

## Reference Index

- [Model audit checklist](references/model-audit-checklist.md)
- `../source-evaluation/references/book-driven-source-admission-and-currentness.md` - currentness and evidence requirements for time-sensitive inputs.
