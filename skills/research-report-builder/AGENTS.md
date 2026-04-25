# Codex / generic-agent guidance — research-report-builder

## Pipeline

1. Read project markdown corpus
2. Run `gap-analysis` against chosen schema
3. Run `cross-cohort-synthesis` if multi-cohort
4. Assemble master markdown matching schema
5. Lint with `markdown-lint-cleanup`
6. Render to `.docx` via `python-docx` or equivalent
7. Save `projects/<project-id>/report-v<N>-<date>.docx`

## Schema selection

Use `report_schema` field in project metadata:
- `pain-point` → Schema A
- `single-cohort` → Schema B
- `market-landscape` → Schema C
- `comparative` → Schema D

See `SKILL.md`.
