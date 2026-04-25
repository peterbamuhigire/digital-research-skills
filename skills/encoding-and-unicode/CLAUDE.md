# Claude-specific — encoding-and-unicode

- `repair_encoding` first, before `pd.read_csv`.
- Default `encoding='utf-8-sig'` on read.
- Log detected encoding in manifest.
- Always create .bak before in-place repair.

See `SKILL.md`.
