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

## Required Inputs

- Model question, units, time period, data sources, assumptions, constraints, and intended decision.
- Source register and data-quality notes.

## Workflow

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

## Anti-Patterns

- Single-path market sizing with no triangulation.
- False precision from weak data.
- Mixing populations or time periods.
- Hiding assumptions inside formulas.

## Outputs

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

<!-- dual-compat-end -->

## Companion Skills

- `data-quality-pipeline` assesses datasets.
- `calibration-and-forecasting` governs probabilistic outputs.
- `source-verification` checks numeric claims.
