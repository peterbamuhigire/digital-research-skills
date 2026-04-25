# Claude-specific — data-cleaning-pandas

- Audit before cleaning. Always.
- `errors='coerce'` on every type coercion.
- `tools.data.advise_imputation` to pick missing-value method, not gut feel.
- Document the cleaning as a script, not interactive cells.

See `SKILL.md`.
