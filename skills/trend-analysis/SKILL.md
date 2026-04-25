---
name: trend-analysis
description: Use when forecasting, extracting signals from time-series, or surfacing weak signals before they become consensus. Distinguishes durable trends from fads, drivers from symptoms, leading indicators from coincident.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Trend analysis

Trend research is forecasting with discipline. The risk is **plausible-sounding bias dressed as foresight**. The discipline is to distinguish durable signal from noise, drivers from symptoms, leading from coincident.

## The five-step structure

1. **Define the domain & horizon.** "AI in EA banking, 2026–2029" is workable. "The future of work" is not.
2. **Inventory the data.** Time-series sources (statistics, prices, search trends, regulatory filings) + qualitative signals (commentary, conference activity, hiring patterns, capital flows)
3. **Separate signal types** — coincident, lagging, leading. Most trend reports over-weight lagging.
4. **Stress-test with scenario analysis** — best / base / worst case. A trend report without ≥3 scenarios is opinion, not analysis.
5. **Identify the few leading indicators to watch.** What 5 things would invalidate the base case?

## Signal types

| Type | Definition | Example |
|---|---|---|
| **Coincident** | Moves with the trend | Industry revenue this quarter |
| **Lagging** | Confirms after the trend | Layoffs, profit-warnings, late-stage M&A |
| **Leading** | Moves before the trend | Patent filings, hiring patterns, capital deployment, regulatory consultations |
| **Durable** | Sustained ≥3 cycles / years | Demographic shifts, infrastructure build-outs |
| **Fad** | Spikes and reverts | Viral product cycles, hype-driven funding rounds |

## Decision rules

- **Always 3+ scenarios.** Best, base, worst. Single-scenario forecasts are wishful.
- **Confidence intervals over point estimates.** "Between X and Y" is more honest than X.
- **Distinguish drivers from symptoms.** Rising rents is a symptom; underlying drivers may be supply constraints, currency, demographics.
- **Identify leading indicators explicitly.** A trend report should tell the reader what to watch next.
- **Mark assumptions clearly.** "Base case assumes interest rates stable at X%" — readers must be able to update if the assumption breaks.
- **Sources by tier still apply.** Trend research is not exempt from `source-verification`.

## Output structure

- `<project>/research/domain-horizon.md` — scope
- `<project>/research/signal-inventory.md` — sources organized by signal type
- `<project>/research/quantitative-trends.md` — charts, tables
- `<project>/research/qualitative-signals.md` — commentary
- `<project>/research/scenarios.md` — best / base / worst with assumptions
- `<project>/research/leading-indicators.md` — what to watch
- Final Word doc uses Schema J

## Anti-patterns

- Single-scenario forecasting (deterministic)
- Treating all signals as equally weighted
- Ignoring base rates (e.g., "the next 5 years will be unprecedented" — base rate of "unprecedented" claims is high)
- Recency bias — over-weighting last 3 months
- Confirmation bias — only citing sources that support the chosen narrative
- Failing to identify drivers separately from symptoms

## See also

- `evidence-discipline` — applies
- `source-verification` — applies
- `historical-research-methods` — needed when forecast horizon requires historical analogue
- `research-report-builder` — Schema J
