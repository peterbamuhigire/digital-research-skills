# Legacy Project Migration Notes

Older projects, including `projects/east-africa-property-hostel/`, may use the
pre-kernel cohort layout:

```text
projects/<project-id>/<cohort>/research/
projects/<project-id>/<cohort>/analysis/
projects/<project-id>/<cohort>/opportunities/
```

Do not delete or rename sourced cohort files during migration. The safe path is:

1. Add the kernel root files: `PROJECT-STATUS.md`, `_context/`, `_registry/`,
   `01-initiation/` through `06-governance/`, and `export/`.
2. Preserve existing cohort folders as legacy cohort directories.
3. Run `python -m engine sync <project-id>` to create or repair registries.
4. Import source records from legacy `research/sources.md` files.
5. Fill `_context/` from the existing project README and cohort notes.
6. Add output manifests under `05-output/`.
7. Run `python -m engine validate <project-id>` and resolve blockers before
   treating the project as kernel-managed.

The evidence audit remains authoritative for human correction history. The
registries become the machine-readable control plane.
