---
name: data-cleaning-pandas
description: Use to clean tabular data — missing values, duplicates, outliers, type coercion, encoding, datetime, strings, categoricals. Walker's recipe library + Chen's pandas idioms. Backed by tools/data/.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Data cleaning — pandas recipes

Walker (Python Data Cleaning Cookbook) + Chen (Pandas for Everyone) converge on a stable recipe set. Each recipe specifies failure mode + correct fix.

## Recipe library

### 1. Encoding repair (always first)
```python
from tools.data import repair_encoding
report = repair_encoding("messy.csv")
# → detects encoding, strips BOM, fixes mojibake, writes UTF-8
```

### 2. Read with explicit dtypes
```python
df = pd.read_csv(
    "clean.csv",
    dtype={"id": "Int64", "amount": "float64", "country": "category"},
    parse_dates=["date_filed"],
    na_values=["NA", "N/A", "", "NULL", "-"],
    keep_default_na=True,
    low_memory=False,
)
```

### 3. Missing values
```python
df.isnull().sum(axis=0)                          # column-wise
df.isnull().sum(axis=1).value_counts()           # row-wise profile

# Group-mean impute (Chen)
df["bill"] = df.groupby("region")["bill"].transform(lambda s: s.fillna(s.mean()))

# KNN impute (Walker — when correlations exist)
from sklearn.impute import KNNImputer
df[["a", "b", "c"]] = KNNImputer(n_neighbors=5).fit_transform(df[["a", "b", "c"]])
```

Use `tools.data.advise_imputation(df, col)` to choose the method.

### 4. Duplicates
```python
df.duplicated().sum()
df = df.drop_duplicates(subset=["id"], keep="first")  # natural-key dedupe
```

### 5. Type coercion (always with errors='coerce')
```python
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce", format="%Y-%m-%d")
df["country"] = df["country"].astype("category")
```

### 6. String cleanup
```python
# AUDIT before cleaning (Walker's discipline)
df["name"].str.startswith(" ").any()
df["name"].str.endswith(" ").any()

# Then clean
df["name"] = df["name"].str.strip().str.lower()
df["name"] = df["name"].str.replace(r"\s+", " ", regex=True)
```

### 7. Outlier detection
```python
from tools.data import detect_outliers

# Univariate IQR
report = detect_outliers(df["wage"], methods=["iqr"])
# Multivariate
reports = detect_outliers(df, methods=["isolation_forest"])
```

### 8. Datetime normalisation
```python
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["year"] = df["date"].dt.year
df["quarter"] = df["date"].dt.quarter
df["weekday"] = df["date"].dt.day_name()
```

### 9. Categorical recoding (clear semantics)
```python
df["age_band"] = pd.cut(df["age"], bins=[0, 18, 35, 60, 120],
                        labels=["minor", "young_adult", "adult", "senior"])
```

### 10. Tidy-data violations
```python
from tools.data import tidy_check
violations = tidy_check(df)
# → "5 year-like columns. Run df.melt(...)"
```

## Walker's anti-patterns (always check)

- `iterrows()` / `itertuples()` for computation — use vectorised
- Setting on a copy — use `.loc[]` for combined row+column selection
- Trusting "similar" data files have the same schema — `symmetric_difference` columns after concat
- Merging without anti-join check — use `tools.data.check_merge`
- Flattening JSON eagerly — preserve nesting where it matters
- Treating outliers as errors by default — distinguish implausible from unusual
- Imputing without inspecting missingness mechanism (MCAR/MAR/MNAR)
- Dropping rows globally with `dropna()` — drop only on critical-column subset
- String cleanup without first auditing
- Top-coded values mistaken for valid extremes

## Decision rules

- **Audit before cleaning.** Always.
- **Document the cleaning script as code.** No interactive cell-level cleaning that disappears.
- **Hash inputs and outputs.** Reproducibility requires that re-running produces identical output.
- **Fail loudly on ambiguity.** Don't silently coerce; raise + log.

## See also

- `tools/data/` — implementations (profiler, dq_score, checkmerge, outlier_panel, encoding_repair, tidy_check, imputation_advisor)
- `data-quality-assessment` — upstream gate
- `tidy-data-craft` — Wickham violations specifically
- `merge-discipline` — joins
- `anomaly-detection` — outliers in depth
- `encoding-and-unicode` — mojibake / BOM / charset
