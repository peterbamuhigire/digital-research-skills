# CLAUDE.md — srs-skills-completion-2026

Operating instructions for this project. Inherits the root `CLAUDE.md` rules — most importantly the evidence-discipline clause from `skills/source-evaluation/references/evidence-discipline.md`.

## Workflow phase

This is a research project (not a kernel project). Phases:

1. Wave 0 — Scaffold + front matter (orchestrator)
2. Wave 1 — Four parallel cohort agents (background)
3. Wave 2 — Verification (orchestrator)
4. Wave 3 — Cross-cohort synthesis (orchestrator only — never delegated)
5. Wave 4 — Word doc assembly (orchestrator)

## Hard rules (in addition to root)

- Every cohort agent prompt MUST include the verbatim hard-constraint clause from `skills/source-evaluation/references/evidence-discipline.md`.
- Standards citations (29119, 27001, ITIL, NIST) must reference real, verifiable clause numbers — no fabricated clause IDs.
- URLs must be live as of verification date; cite with `(fetched YYYY-MM-DD)`.
- AcademiaPro-specific claims must match what is actually in `C:\wamp64\www\srs-skills\projects\AcademiaPro\` — no invented context.
- Append, don't overwrite. Wave-2 fixes use `# Pass 2 — Gap-fill addendum` headers.
- Never delete a sourced claim without logging in `EVIDENCE-AUDIT.md`.

## Where things live

- Front matter: `00-front-matter/`
- Cohort specs: `<NN-cohort-name>/specs/<spec-id>.md`
- Cohort sources: `<NN-cohort-name>/sources.md` (tier-classified)
- Verification log: `<NN-cohort-name>/verification-log.md`
- Final Word doc: `export/srs-skills-completion-2026-v1.docx`
