# Codex / generic-agent — tidy-data-craft

```yaml
tidy_check:
  violations:
    - kind: columns_are_values | multiple_vars_per_column | vars_split_rows_cols
      columns: [...]
      suggested_fix: "df.melt(...)"
      severity: warn | block
```

See `SKILL.md`.
