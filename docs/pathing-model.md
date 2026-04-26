# Project Pathing Model

The canonical runtime unit is a project workspace under:

```text
projects/<project-id>/
```

The project id is the directory name. Engine commands accept either the id
(`east-africa-property-hostel`) or a direct path to the workspace.

## Mandatory Root Contract

Every kernel-managed project contains:

```text
README.md
PROJECT-STATUS.md
EVIDENCE-AUDIT.md
export/
_context/
_registry/
01-initiation/
02-research/
03-analysis/
04-synthesis/
05-output/
06-governance/
```

`_context/` is the user-approved project truth. It stores the brief, scope,
methodology, audience, output plan, hypotheses, success criteria, and project
profile.

`_registry/` is the machine-readable control plane. It stores source, claim,
quote, synthesis, sign-off, waiver, and release-ledger registries.

## Legacy Alias

Older projects may still contain cohort folders directly under the project
root:

```text
projects/<project-id>/<cohort>/research/
projects/<project-id>/<cohort>/analysis/
projects/<project-id>/<cohort>/opportunities/
```

The kernel treats those folders as legacy cohort directories. New work should
use the canonical numbered project phases and registry-backed evidence control,
while migration notes should preserve cohort evidence instead of deleting or
renaming it blindly.
