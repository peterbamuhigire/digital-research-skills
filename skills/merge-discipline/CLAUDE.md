# Claude-specific — merge-discipline

- Always use `tools.data.check_merge` not raw `pd.merge`.
- Always pass `validate=` (one_to_one / one_to_many / many_to_one / many_to_many).
- Default `how='left'` for reference-table joins.
- `report.passes()` before proceeding.

See `SKILL.md`.
