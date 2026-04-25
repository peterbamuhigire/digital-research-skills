---
name: tidy-data-craft
description: Use to detect and fix tidy-data violations (Wickham) — columns-as-values, multiple-vars-per-column, vars-split-rows-cols. Tidy form is the prerequisite for groupby/agg/plot/model. Backed by tools/data/tidy_check.py. From Chen (Pandas for Everyone).
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Tidy data craft — Wickham's three rules

1. Each **variable** in a column
2. Each **observation** in a row
3. Each **observational unit** in a table

Untidy data fights every downstream operation: groupby is awkward, plotting requires manual reshaping, joins are weird, modelling needs a pre-step. Tidying is upstream prep that pays off everywhere.

## Three common violations + fixes

### Violation 1: columns-are-values
Multiple columns whose names are *categories of one variable*:
```
religion         <$10k   $10-20k   $20-30k
Agnostic           27        34        60
Atheist            12        27        37
```

Fix:
```python
tidy = df.melt(id_vars=["religion"], var_name="income", value_name="count")
```

### Violation 2: multiple-vars-per-column
A single column holds two variables:
```
date_metric         value
2023-Q1_sales       100
2023-Q1_returns     5
2023-Q2_sales       110
```

Fix:
```python
df[["quarter", "metric"]] = df["date_metric"].str.split("_", n=1, expand=True)
df = df.drop(columns=["date_metric"])
```

### Violation 3: vars-split-rows-cols
A "type" or "element" column rotates which variable each row holds:
```
station   element   d1     d2     d3
USW00     tmin      -2.0   -1.0   0.0
USW00     tmax       3.0    4.0   5.0
```

Fix:
```python
tidy = df.pivot_table(
    index=["station"],
    columns="element",
    values=["d1", "d2", "d3"],
).stack(level=0).reset_index()
```

## Standard usage

```python
from tools.data import tidy_check

violations = tidy_check(df)
for v in violations:
    print(f"[{v.kind}] {v.columns}: {v.suggested_fix}")
```

## When wide is the right shape

Tidy is the analytical default. **But** wide format is correct for:

- ML feature matrices (one row per observation, columns = features)
- Pre-built dashboards / Excel templates
- Time-aligned panels (one row per date, columns = entities)

Don't blindly melt every dataset. The rule is: tidy for *analysis*, wide for *modelling/dashboards*.

## Decision rules

- **Always tidy_check after retrieval**, before any groupby / plot / merge.
- **Document the reshape** in the cleaning script.
- **Prefer `melt` and `pivot_table`** over manual `unstack` chains.
- **`pd.wide_to_long`** for the `Q1_sales / Q2_sales / ...` pattern — handles common cases automatically.

## Anti-patterns

- Reading wide data, then `groupby`-ing without tidying first
- Repeated melts and pivots in the same script (sign you should have tidied once and stayed there)
- Tidying for display (use a wide-format DataFrame derived from tidy data, don't tidy the source)
- Ignoring tidy violations because "groupby still works" — it works inefficiently and brittlely

## See also

- `tools/data/tidy_check.py` — Wickham violation linter
- `data-cleaning-pandas` — broader cleanup
- `data-quality-assessment` — tidy violations are a usefulness signal
