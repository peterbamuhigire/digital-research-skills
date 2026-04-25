---
name: anomaly-detection
description: Use to detect outliers across univariate / multivariate / time-series methods. IQR + z-score + Cook's + KNN + Isolation Forest panel. Walker's discipline: outliers are not errors by default. Backed by tools/data/outlier_panel.py.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Anomaly detection

Walker: **distinguish *implausible* from *unusual***. The 7'4" person is unusual; the 7'4" 10-year-old is implausible. The panel approach gives multiple perspectives so the analyst can decide.

## Method selection

| Method | Best for | Assumption |
|---|---|---|
| **IQR** (1.5×) | Univariate, robust | None — works on any distribution |
| **Z-score** (\|z\|>3) | Univariate, large n | Approximate normality |
| **Isolation Forest** | Multivariate, high-dim | None |
| **Cook's distance** | Regression-influence | Linear regression context |
| **Period-over-period delta** | Time-series | Time-ordered rows |
| **STL residual** | Time-series with seasonality | Seasonal pattern stable |

**Default**: run IQR on each numeric column. Add Isolation Forest when columns interact.

## Standard usage

```python
from tools.data import detect_outliers

# Univariate IQR on one column
report = detect_outliers(df["wage"], methods=["iqr"], multiplier=1.5)
print(f"{report['iqr'].n_flagged} flagged of {report['iqr'].n_total}")

# Univariate z-score
report = detect_outliers(df["wage"], methods=["zscore"], threshold=3.0)

# Multivariate
reports = detect_outliers(df, methods=["isolation_forest"], contamination=0.05)

# Compose multiple methods
reports = detect_outliers(
    df, methods=["iqr", "zscore"],
    column="wage",  # required for univariate
)
```

## Walker's anti-pattern: deleting outliers by default

Outliers may be:
- **Real but unusual** — keep, document
- **Genuine errors** — fix or drop with audit log
- **Top-coded values** — flag as a known artefact (NLS97 wage capped at $235,884)
- **Data-collection artefacts** — investigate, then decide

The panel surfaces them; the analyst decides.

## Skew-aware method choice

Walker's rule:
- `|skew| > 1` → IQR (robust)
- `|skew| ≤ 1` and `|kurtosis-3| < 1` → z-score (approximately normal)

The `tools.data.profile_dataframe` already reports skew and kurtosis per column — use them to pick.

## Multivariate context

Some outliers are only visible in higher dimensions:
- A 6-foot person is unremarkable
- A 6-foot 5-year-old is highly anomalous

Isolation Forest catches this because it splits on combinations of features. KNN distance does similar. Always run a multivariate method when columns are correlated.

## Time-series outliers

Walker's `adjmeans` pattern — flag points where `|x_t - x_{t-1}| > k * baseline_volatility`. For seasonal data:

```python
from statsmodels.tsa.seasonal import STL

stl = STL(series, period=12).fit()
residuals = stl.resid
# Flag residuals beyond 3 std
flagged = residuals[abs(residuals) > 3 * residuals.std()]
```

## Decision rules

- **Profile first** — skew/kurtosis decide IQR vs z-score
- **Standardise before multivariate methods** (Isolation Forest)
- **Document every outlier action** — keep, fix, drop — in the cleaning log
- **Never silently drop** — keep an `<dataset>.outliers.json` audit
- **Top-coded values** — flag as known artefact, don't auto-drop

## Anti-patterns

- Single-method outlier handling (always run a panel)
- Deleting outliers without audit
- Z-score on heavily skewed data (use IQR)
- IQR on naturally bimodal distributions (IQR is invalid; use mixture model)
- Running multivariate methods on un-standardised features
- Mistaking top-coded values for valid extremes

## See also

- `tools/data/outlier_panel.py` — implementation
- `data-quality-assessment` — outlier rate feeds reliability score
- `data-cleaning-pandas` — full pipeline context
