# example-due-diligence-dossier

Research project workspace.

| Field | Value |
|---|---|
| Project id | `example-due-diligence-dossier` |
| Research type | due diligence |
| Audience | investor |
| Variant | evidence-dossier |

## Golden Path

1. Complete `_context/brief.md` and `_context/project-profile.md`.
2. Run research meta-initialization.
3. Execute research waves.
4. Run `python -m engine sync example-due-diligence-dossier`.
5. Run `python -m engine validate example-due-diligence-dossier`.
6. Build outputs in `05-output/`.
7. Run `python -m engine pack example-due-diligence-dossier --out export/example-due-diligence-dossier.zip`.
