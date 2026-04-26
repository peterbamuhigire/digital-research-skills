# Reference — Zelazny Chart Selection

**Canonical source:** Gene Zelazny, *Say It With Charts: The Executive's Guide to Visual Communication*, McGraw-Hill, 4th ed. 2001 (1st ed. 1985). Zelazny was Director of Visual Communications at McKinsey for over four decades.

## The core rule

**The chart serves the message, not the data.**

Pick the chart for what you want the reader to conclude, not for what shape the data happens to take. If the message is "Acme dominates", a bar comparison says it. If the message is "Acme's lead is shrinking", a time-series line says it. The same data justifies both messages; the chart choice depends on which message you are landing.

## Zelazny's five chart families

| Family | Use when the message is about… | Standard chart |
|---|---|---|
| **Component** | Share of a whole at one moment | Pie, 100% stacked bar |
| **Item** | Comparison of items on one dimension | Bar (horizontal for ranked items), column (vertical for time-stamped items) |
| **Time series** | Change in something over time | Line; column for discrete periods |
| **Frequency distribution** | How items are distributed across a range | Histogram, line |
| **Correlation** | Relationship between two variables | Scatter, paired bar, bubble (for a third dimension) |

Decide the family from the message verb:

- "X **is** Y% of Z" → Component (pie / stacked bar)
- "X **is more / less than** Y" → Item (bar / column)
- "X **changed** from A to B" → Time series (line)
- "X **is distributed** as ..." → Frequency (histogram)
- "X **relates to** Y" → Correlation (scatter)

## The chart-construction discipline

1. **Write the chart title as an action title.** The title states the conclusion the chart supports. ("Acme has lost 11pp of share since 2022; two new entrants captured most of it.") See `references/action-titles.md`.
2. **Pick the family from the title's verb.** Per the table above.
3. **Pick the standard chart in that family.** Don't experiment unless the audience has a specific reason to read a non-standard chart.
4. **Strip everything that doesn't serve the title.** Gridlines, 3-D effects, decorative shadows, colour gradients on bars. All out unless they serve the message.
5. **Label directly.** Put the data labels on the bars / lines / segments. Avoid forcing the reader to read a legend then a chart then back.
6. **One message per chart.** If two messages need to come out of the same data, make two charts.
7. **Source the chart.** Footnote with the source of the data, the date of the data, and the upstream research-manifest entry.

## Chart anti-patterns

- **Pie chart with > 5 segments.** The reader cannot judge segment angles past 5 slices. Use a bar instead.
- **3-D pie / 3-D bar.** Distorts proportions. Always 2-D.
- **Dual-axis charts.** Reader cannot tell whether two lines correlate or one was simply scaled to look like the other. Split into two charts.
- **Line chart through 3 points.** Use a column chart; lines imply continuous change.
- **Colour for decoration.** Each colour should mean something. Otherwise grey.
- **Title that describes the chart.** "Bar chart of market share by carrier, 2020 vs 2026" is wrong; "Acme has lost 11pp of share..." is right.
- **Chartjunk.** Backgrounds, drop shadows, ribbons, animation. Out.

## When NOT to use a chart

- **No message yet.** If you can't write the action title, you don't have a message; don't draw a chart.
- **The number is the message.** "$1.4 bn at risk" is a single statistic; render as a callout, not a chart.
- **The story is qualitative.** Three patient quotes are more persuasive than a bar chart of patient ratings.
- **The reader will project intent onto a chart that doesn't carry it.** A scatter with 5 points is noise, not correlation.

## Worked example

**Message:** "Three of five hostel cohorts share the same scam pattern."
- Verb: "share" → similarity comparison across items → **Item family** → bar chart.
- Chart: 5 cohort bars, two segments per bar (this scam / other complaints), with the three matching cohorts highlighted in colour, the other two in grey.
- Title: "Three of five hostel cohorts (students, parents, landlords) report the same deposit-scam pattern; tenants and owners report different scams."
- Source: students/research/complaints-report.md §2.1 + cross-cohort matrix (tier-1 sources, 12 verbatim quotations).

## Companion patterns

- `references/pyramid-principle.md` — every chart supports a fact under a group; the group supports the apex.
- `references/action-titles.md` — chart titles follow the action-title rule.
- `references/ghost-deck-pattern.md` — chart family is decided at ghost-deck time, not at design time.

## Sources

- Zelazny, *Say It With Charts*, McGraw-Hill, 4th ed. 2001. Tier 1.
- Zelazny, *Say It With Presentations*. McGraw-Hill, 2nd ed. 2006. Tier 1.
- Tufte, Edward. *The Visual Display of Quantitative Information*, 2nd ed. 2001. Tier 1 — independent corroboration of "ink-to-data ratio" and chartjunk discipline.
