# Output Manifests

Every deliverable family under `05-output/` should define assembly order in a
plain markdown manifest:

```text
05-output/<family>/
  manifest.md
  sections/
    01-introduction.md
    02-findings.md
```

The manifest is an ordered list:

```markdown
# Manifest

- sections/01-introduction.md
- sections/02-findings.md
```

Run:

```powershell
python -m engine assemble <project-id> <family>
```

The command writes `05-output/<family>/assembled.md` unless `--out` is supplied.
Markdown remains canonical; `.docx` and `.pdf` rendering stays downstream.
