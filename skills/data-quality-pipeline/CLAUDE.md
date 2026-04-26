# Claude-specific — data-quality-pipeline

- Run pipeline stages in order: encoding → tidy → clean → outliers → merge → score → manifest. Never skip.
- Default `encoding='utf-8-sig'` on read; never `pd.read_csv` before encoding repair.
- Default `validate='one_to_one'` or `'one_to_many'` on every merge — never default-merge.
- Outlier panel uses ≥2 methods; flag only on consensus.
- Composite score ≥ 0.70 to ship; override requires reason in manifest.
- Provenance packet (parquet + profile + dq + manifest) is mandatory; no manifest = not shippable.

See `SKILL.md`.
