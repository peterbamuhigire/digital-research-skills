# Release Pack Specification

`python -m engine pack <project-id> --out export/<name>.zip` creates an
audit-ready zip for a project release.

The pack includes:

- markdown output source from `05-output/`
- rendered `.docx` and `.pdf` files in `05-output/`, when present
- all `_registry/*.yaml` files
- `_context/*.md`
- `EVIDENCE-AUDIT.md`
- `PROJECT-STATUS.md`
- generated `export/validation-report.md`

The command also appends a release entry to `_registry/release-ledger.yaml`.
Validation blockers are reported but do not prevent packaging; this allows draft
evidence packs for internal review while keeping the blocker count visible.
