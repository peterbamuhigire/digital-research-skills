# srs-skills-completion-2026

**Date started:** 2026-05-01
**Owner:** Peter Bamuhigire
**Status:** Wave 0 (scaffold)

## Purpose

Produce a single Word document delivering 17 Depth-2 implementation specs that the srs-skills dev team uses to close Stages 1–3 of the 2026-04-12 remediation roadmap. Target movement: 8.1 → ~9.0 / 10.

## Final deliverable

`export/srs-skills-completion-2026-v1.docx` — ~170–200 pages.

## Spec inventory (17 total)

**Cohort 01 — Stage 1: Proof Restoration (4 specs):**
- `01-demo-workspace-restoration` — restore the demo workspace so proof claims in the README can be re-executed end-to-end.
- `02-engine-suite-green-up` — bring the engine test suite back to green and document the green-up procedure.
- `03-dev-environment-bootstrap` — produce a deterministic dev-environment bootstrap (Python, Node, Pandoc, fonts) that any reviewer can replicate.
- `04-readme-proof-claims-rewrite` — rewrite the README's proof section so every claim maps to an executable command and verified output.

**Cohort 02 — Stage 2: Skill Normalization (5 specs):**
- `05-canonical-skill-path-decision` — decide and document the canonical skill-path layout, including migration rules for legacy paths.
- `06-fifteen-skill-validator-fixes` — fix the 15 skills currently failing the validator and prove green status.
- `07-portable-dual-compat-rollout` — roll out the portable / dual-compat layer across the catalog so skills run on both harness variants.
- `08-broken-link-audit` — run a full broken-link audit across the catalog and remediate every failure.
- `09-contract-gate-zero-warnings` — drive the contract gate to zero warnings and lock the gate in CI.

**Cohort 03 — Stage 3a: AcademiaPro Design Layer (4 specs):**
- `10-academiapro-context-pack` — assemble the AcademiaPro context pack (vision, scope, stakeholders, glossary).
- `11-architecture-decision-records` — author the AcademiaPro ADR set covering the load-bearing design decisions.
- `12-threat-model-and-security-design` — produce the AcademiaPro threat model and security-design document.
- `13-engineering-baseline-pack` — produce the engineering baseline pack (coding standards, branching, review, build).

**Cohort 04 — Stage 3b: AcademiaPro Release & Governance (4 specs):**
- `14-iso-29119-test-evidence-pack` — produce the ISO/IEC/IEEE 29119-aligned test-evidence pack for AcademiaPro.
- `15-deployment-and-operations-pack` — produce the AcademiaPro deployment and operations pack (runbooks, SLOs, on-call).
- `16-agile-and-user-doc-pack` — produce the agile artefacts and user-facing documentation pack.
- `17-audit-and-evidence-pack-assembly` — assemble the master audit and evidence pack from cohort outputs.

## Hard exclusions

- Stages 4–6 of the remediation roadmap (traceability schema, runtime evidence ingestion, semantic correctness, AI hallucination scoring)
- New skills outside the existing 240 in the catalog
- Direct edits to `C:\wamp64\www\srs-skills\` (this is a spec-only deliverable)
- Cost estimates, vendor selection, hiring plans
- Score promises above 9.1/10 (the ceiling is honest)

## Source documents

- `_context/gap-analysis.md` — verbatim source gap analysis
- `_context/design-spec.md` — project design
- `_context/implementation-plan.md` — execution plan
- `_context/per-spec-template.md` — Depth-2 template all specs follow
- `_context/agent-brief-template.md` — common cohort agent brief
- `_context/scope-exclusions.md` — verbatim exclusions for every brief
- `_context/scoring-ceiling.md` — honest-ceiling rules (no score promises above 9.1/10)

## Status tracking

See `PROJECT-STATUS.md` for wave progress; `EVIDENCE-AUDIT.md` for any evidence-discipline incidents.
