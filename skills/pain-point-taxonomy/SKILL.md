---
name: pain-point-taxonomy
description: Use when classifying problems surfaced by research into a structured taxonomy — sub-themes tagged with prevalence, severity, and cohort cross-cuts. Produces the canonical `analysis/themes.md` for any cohort.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Pain-point taxonomy

Free-text complaint lists are not actionable. Tagged taxonomies are.

## The shape

Two top-level categories per cohort, with sub-themes tagged on three axes.

### Top-level structure (template)

```
A. Demand-side / getting-in
B. Supply-side / running-it / getting-out
```

(Adjust labels to fit cohort — students might use "finding hostel" / "living in hostel"; landlords might use "operational" / "business".)

### Per sub-theme tagging

| Axis | Values |
|---|---|
| Prevalence | universal / high / specific / rare |
| Severity | critical / high / medium / low |
| Country scope | UG / KE / TZ / RW / BI / SS / regional |
| Cohort cross-cut | which other cohorts share this pain |
| Evidence anchor | the strongest source backing the pain |

## Decision rules

- **Every sub-theme has a prevalence + severity tag.** Never list pains without weighting.
- **Severity-weighted top 5** at the end of each themes file — explicit ranking that drives product strategy.
- **"Risk multipliers" section** — sub-cohorts that experience the pain disproportionately (e.g., "small landlords", "single women", "first-year students").
- **"What's not yet mapped" section** — feeds gap-analysis on the next pass.
- **Cohort cross-cuts** — when a pain appears for multiple cohorts (e.g., deposit theft for tenants AND students), tag both files and make the cross-cut visible.

## Standard themes file structure

```markdown
# <Cohort> theme taxonomy

## A. <Top-level category>
| # | Sub-theme | Prevalence | Severity | Key evidence |
|---|---|---|---|---|

## B. <Top-level category>
| # | Sub-theme | Prevalence | Severity | Key evidence |
|---|---|---|---|---|

## Cross-cutting risk multipliers
- ...

## Severity-weighted top 5 for product strategy
1. ...

## What's not yet mapped
- ...
```

## Anti-patterns

- Bullet lists of pains with no severity weighting
- Mixing critical and minor pains at the same level
- "Severity: high" applied to every row (not actually a tag)
- No risk-multiplier section — flattens vulnerable cohorts
- No cross-cohort visibility — same pain re-discovered in three reports

## See also

- `cross-cohort-synthesis` — consumes themes files to find shared pain
- `research-report-builder` — emits taxonomy as Word tables
