---
name: merge-discipline
description: Use whenever joining two or more DataFrames — Walker's checkmerge anti-join + Chen's validate= cardinality assertion. Mandatory before any merge in research-grade work. Backed by tools/data/checkmerge.py.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Merge discipline

Silent row loss / explosion is the most common merge bug. Walker (Python Data Cleaning Cookbook, Ch. 8) + Chen (Pandas for Everyone, Ch. 6) both insist: **never merge without an audit**.

## The two pillars

### 1. Anti-join check (Walker)
Before / during the merge, count left-only / right-only / both:

```python
from tools.data import check_merge

merged, report = check_merge(
    left=tenants,
    right=regions,
    on="region_id",
    how="left",
    validate="many_to_one",   # cardinality assertion
)

print(report.left_only, report.right_only, report.both)
print(report.warnings)
print(report.fan_out_factor)

if not report.passes(max_left_only_rate=0.10, max_fan_out=1.5):
    # Escalate — orphan rate too high or fan-out too aggressive
    raise RuntimeError(f"merge audit failed: {report.warnings}")
```

### 2. Validate cardinality (Chen)
The `validate=` argument asserts the cardinality assumption:

| validate | Meaning |
|---|---|
| `one_to_one` | both sides unique on the join key |
| `one_to_many` | left unique; right may repeat |
| `many_to_one` | left may repeat; right unique (most common for reference-table joins) |
| `many_to_many` | both may repeat (rare; usually a bug indicator) |

If the assumption fails, pandas raises `MergeError` — caught early, before silent fan-out.

## Decision rules

- **Always pass `validate=`.** Pick the cardinality you expect; let the engine raise if wrong.
- **Always pass `indicator=True`** (the engine's `check_merge` does this by default).
- **Default `how='left'`** for reference-table enrichment — preserves left-side row count.
- **`how='inner'` is dangerous** — silently drops rows. Only use when you genuinely want the intersection.
- **Multi-key merges**: pass `on=["k1", "k2"]`, all keys must match.
- **Fuzzy joins**: never on the canonical pipeline. If keys need fuzzy matching, do it in a separate normalisation step (rapidfuzz / recordlinkage) and produce a clean key column first.

## When fan-out is real

Sometimes a many-to-many is genuine (one tenant has multiple deposits; one paper has multiple authors). Then:

1. Set `validate="many_to_many"`
2. Document the expected fan-out in the analysis (`expected_avg_deposits_per_tenant=2.3`)
3. After merge, verify counts: `merged.groupby("tenant_id").size().describe()`

## Anti-patterns

- Default merge with no `how`, no `validate`, no `indicator`
- Merging on text keys without prior normalisation (case, whitespace, punctuation)
- Using `how='inner'` when you meant `how='left'`
- Trusting that two CSVs with the same column name have the same key semantics (one might be `customer_id`, the other `cust_id`)
- Float columns as join keys (precision loss → orphans)
- NaN keys silently dropping rows (test with `key.isna().any()` first)

## Pair with

- `tools/data/checkmerge.py` — implementation
- `data-cleaning-pandas` — pre-merge cleanup
- `data-quality-assessment` — score both inputs first
- `evidence-discipline` — every merge documented in the cleaning log

## Worked example

```python
import pandas as pd
from tools.data import check_merge

# Tenants table — natural key tenant_id, may have NaN region_id
tenants = pd.read_parquet("tenants.parquet")
# Regions reference table — natural key region_id, must be unique
regions = pd.read_parquet("regions.parquet")

# Sanity check before merge
assert regions["region_id"].is_unique, "regions table not unique on region_id"
assert tenants["region_id"].notna().any(), "no region_id in tenants table"

# Merge with audit
merged, report = check_merge(
    left=tenants, right=regions,
    on="region_id", how="left",
    validate="many_to_one",
)

# Audit report
print(f"Left rows: {report.left_total}")
print(f"Both: {report.both} | Left-only: {report.left_only} | Right-only: {report.right_only}")
print(f"Fan-out: {report.fan_out_factor:.3f}x")

if report.left_only / report.left_total > 0.10:
    print("WARN: >10% tenants have no matching region — investigate before publishing")
    print(f"Sample orphans: {report.sample_left_only}")
```

## See also

- `tools/data/checkmerge.py` — implementation
- `data-cleaning-pandas` — pre-merge prep
- `tidy-data-craft` — sometimes the right move is to NOT merge
- `evidence-discipline` — merge documented as part of cleaning log
