---
name: data-visualization
description: Use when charts, tables, maps, or dashboards carry part of the argument. Encodes perceptual ranking, chart selection, table/map discipline, style-guide rules, and redesign workflow so visuals clarify the analysis rather than decorate it.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
  priority: high
---

# Data Visualization

<!-- dual-compat-start -->
## Use When

- Use when charts, tables, maps, or dashboards carry part of the argument.
- Use when an analytical artifact needs visual redesign or a coherent style guide.

## Do Not Use When

- The task is pure prose with no visual reasoning component.
- The work only needs rendering without chart-selection judgment.

## Required Inputs

- The message the visual must carry.
- The analytic task type.
- The target artifact and audience.

## Workflow

- Read this `SKILL.md` first, then load the relevant reference file.
- Write the message before choosing the chart.
- Apply perceptual-ranking, chart-choice, and style-guide discipline before shipping.

## Quality Standards

- Each visual has a takeaway.
- Chart family matches the analytic task.
- Labels, units, and source line are present.

## Anti-Patterns

- Software-default charts.
- Decorative color with no analytic role.
- Pie or area displays used where bars or lines are clearer.

## Outputs

- A chart-choice rationale, style guide, redesign plan, or visualization-ready spec.

## References

- Use the `references/` files for perceptual ranking, chart routing, and redesign.
<!-- dual-compat-end -->

This skill governs the visual expression of evidence in reports, decks, proposals, dashboards, and books. It sits between analysis and rendering.

## When to use

- The deliverable includes charts, tables, maps, or scorecards
- A visual is needed to make a comparison, trend, distribution, or relationship legible
- A report needs a style guide so visuals feel coherent across pages
- An existing chart is correct but hard to read and needs redesign

## Five rules

1. **Message first.** Write the takeaway before choosing the chart.
2. **Use stronger perceptual channels first.** Position and length beat area, angle, and color saturation for comparison.
3. **Choose the chart for the task.** Comparison, time, distribution, geospatial, relationship, part-to-whole, qualitative, and table displays do different jobs.
4. **One visual language per artifact.** Color, typography, annotation, and labeling follow a deliberate style guide.
5. **Redesign is part of analysis.** If the message is unclear, revise the visual, not just the caption.
6. **Uncertainty is part of the visual.** Forecasts, samples, model outputs, and estimates
   need intervals, caveats, or confidence labels where the data warrants them.

## Router

| Situation | Load |
|---|---|
| Understanding perceptual strengths and weaknesses | `references/perceptual-rankings.md` |
| Choosing the right chart, table, or map | `references/chart-selection-router.md` |
| Building a consistent visual style and redesigning weak charts | `references/style-guide-and-redesign.md` |

## Ship gate

- [ ] Takeaway sentence exists before the visual
- [ ] Chart family matches the analytic task
- [ ] Labels, units, and source line are present
- [ ] Forecasts, estimates, or model outputs show uncertainty or limitation notes
- [ ] Color is used intentionally, not decoratively
- [ ] Visual can be understood without narration alone, but not without context
- [ ] If part of a set, it matches the artifact's style guide

## Anti-patterns

- Starting from software defaults
- Using area or pie slices for fine comparison when bars would work better
- 3-D effects, chartjunk, or decorative gradients
- Color encoding with no semantic job
- Tables that hide the one number that matters

## Companion skills

- `executive-communication` — storyline and action titles
- `consulting-delivery` — KPI trees and decision support
- `report-and-proposal-craft` — long-form narrative shell
- `python-document-generation` / `excel-spreadsheets` — rendering layer

## Sources for this skill

- Schwabish, Jonathan. *Better Data Visualizations*. Tier 1.
- Zelazny, Gene. *Say It With Charts*. Tier 1.
