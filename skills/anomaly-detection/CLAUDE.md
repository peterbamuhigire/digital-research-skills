# Claude-specific — anomaly-detection

- Profile first; skew/kurtosis pick IQR vs z-score.
- Run a panel, not a single method.
- Standardise before multivariate methods.
- Never silently drop — log to `<dataset>.outliers.json`.

See `SKILL.md`.
