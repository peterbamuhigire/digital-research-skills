# srs-skills-completion-2026 — Design Spec

**Date:** 2026-05-01
**Owner:** Peter Bamuhigire
**Target repo (subject):** `C:\wamp64\www\srs-skills`
**Producer repo (this engine):** `C:\wamp64\www\digital-research-engine`
**Source evaluation:** `C:\wamp64\www\srs-skills\docs\evaluation\2026-04-12\`

## 1. Goal

Produce a single Word document — `srs-skills-completion-2026-v1.docx` — containing ~17 Depth-2 implementation specs that the srs-skills dev team executes to close the Stage 1–3 gaps from the 2026-04-12 re-evaluation. The repository is currently scored **8.1 / 10**. Stages 1–3, fully executed, project to **~8.9–9.1 / 10**.

This is a spec-only deliverable. We do not edit `srs-skills/` as part of this engagement.

## 2. Honest score ceiling

The user's stated target is "close to 9.9/10." Stages 1–3 alone cannot deliver that. The evaluation's lowest dimensions — AI Integration (6/10), and the substantive/runtime/semantic depth deductions on Output Quality, Real-World Usability, Standards Alignment, and Validation & Governance — are unlocked by Stages 4–6 (traceability, runtime evidence ingestion, semantic correctness, AI hallucination scoring). Those are multi-quarter R&D, not "completion."

Projected per-dimension movement after Stages 1–3:

| Dimension | Current | Projected | Why |
|---|---:|---:|---|
| Coverage | 9 | 9 | Already strong; no Stage 1–3 lever. |
| Standards Alignment | 8 | 8.5 | Skill normalization helps; clause depth is Stage 6. |
| Methodology Support | 8 | 8 | Hybrid synchronization depth is Stage 4. |
| Instruction Quality | 8 | 9.5 | 15 skill fixes + path normalization closes this. |
| System Flow | 8 | 9.5 | Clean proof workspace + green tests directly closes this. |
| Validation & Governance | 8 | 9.5 | Engine suite green + clean project validation. |
| AI Integration | 6 | 6 | Untouched in Stages 1–3; needs Stage 6. |
| Real-World Usability | 8 | 9 | Frictionless setup; rest needs Stage 4. |
| Output Quality | 8 | 8.5 | Clean proof helps; semantic depth is Stage 6. |

The exec summary and `_context/scoring-ceiling.md` state this explicitly. No spec promises above 9.1/10.

## 3. Project layout

`projects/srs-skills-completion-2026/` under the producer repo, mirroring `webdevskills-engine-completion-2026`:

```
README.md
CLAUDE.md
PROJECT-STATUS.md
EVIDENCE-AUDIT.md
_context/
  gap-analysis.md            # verbatim copy of 2026-04-12 evaluation (all 9 files concatenated)
  design-spec.md             # this design
  implementation-plan.md     # wave plan
  per-spec-template.md       # Depth-2 template
  agent-brief-template.md    # cohort brief skeleton
  scope-exclusions.md        # Stages 4–6, AI assurance, runtime ingestion
  scoring-ceiling.md         # the 8.9–9.1 projection
00-front-matter/
  exec-summary.md            # incl. score ceiling
  evaluation-baseline.md     # condensed 2026-04-12 findings
  remediation-thesis.md      # why Stages 1–3 first
  cross-reference-matrix.md  # spec ↔ gap ↔ stage ↔ score dimension
01-stage1-proof-restoration/
  specs/
  sources.md
  verification-log.md
02-stage2-skill-normalization/
03-stage3a-academiapro-design/
04-stage3b-academiapro-release/
export/
  srs-skills-completion-2026-v1.docx
```

## 4. Spec inventory (17 specs across 4 cohorts)

### Cohort 01 — Stage 1: Proof Restoration

1. `01-demo-workspace-restoration` — regenerate `projects/_demo-hybrid-regulated`; required artifacts; how engine tests reach green.
2. `02-engine-suite-green-up` — fix the 2 failing tests (`engine/tests/test_cli_sabotage.py` family); fixture strategy; coverage claim repair.
3. `03-dev-environment-bootstrap` — `pip install -e ".[dev]"`, UTF-8, `pytest-cov`; frictionless setup spec.
4. `04-readme-proof-claims-rewrite` — README/PROJECT_BRIEF audit; replace stale numbers with reproducible commands.

### Cohort 02 — Stage 2: Skill Normalization

5. `05-canonical-skill-path-decision` — `skills/<name>` vs `skills/skills/<name>` decision; migration plan; AGENTS.md/README.md alignment.
6. `06-fifteen-skill-validator-fixes` — per-skill remediation table for the 15 failing entrypoints.
7. `07-portable-dual-compat-rollout` — Claude Code + Codex marker pattern across all 240 skills.
8. `08-broken-link-audit` — `../CLAUDE.md` and `../sdlc-lifecycle.md` legacy references; repair plan.
9. `09-contract-gate-zero-warnings` — close 17 warnings or document explicit exemptions.

### Cohort 03 — Stage 3a: AcademiaPro Design Layer

10. `10-academiapro-context-pack` — canonical `_context/` files (charter, stakeholders, scope, glossary, NFRs).
11. `11-architecture-decision-records` — ADR pack template + 8–12 seed ADRs aligned to AcademiaPro's decisions.
12. `12-threat-model-and-security-design` — STRIDE/LINDDUN model; security design doc; controls map.
13. `13-engineering-baseline-pack` — coding standards, env setup, contribution guide, branching/release policy.

### Cohort 04 — Stage 3b: AcademiaPro Release & Governance

14. `14-iso-29119-test-evidence-pack` — test plan, design, cases, results, completion report shaped to ISO/IEC/IEEE 29119.
15. `15-deployment-and-operations-pack` — deployment guide, runbook, monitoring/SLO doc, change-window, readiness review.
16. `16-agile-and-user-doc-pack` — sprint artifacts, backlog hygiene, end-user docs, training material.
17. `17-audit-and-evidence-pack-assembly` — risk register, audit report, control evidence, `engine pack` walkthrough.

Each spec follows the Depth-2 template: context, deliverable shape, source mapping, acceptance criteria, anti-patterns, verification commands, owner notes. Target ~10 pages each → ~170–200 page final doc.

## 5. Wave plan

- **Wave 0 (orchestrator, ~30 min):** scaffold project tree; copy 2026-04-12 evaluation into `_context/gap-analysis.md`; author design-spec, implementation-plan, per-spec-template, agent-brief-template, scope-exclusions, scoring-ceiling; author 00-front-matter exec-summary, evaluation-baseline, remediation-thesis, cross-reference-matrix.

- **Wave 1 (4 cohort agents in parallel, background, ~45–90 min each):** each cohort agent receives:
  - the verbatim evidence-discipline clause from `skills/source-evaluation/references/evidence-discipline.md`
  - the 2026-04-12 evaluation excerpts relevant to its stage
  - the per-spec template
  - its spec list and source-mining hints
  - the verbatim scope-exclusions list
  Sub-agents run via `Agent` tool with `subagent_type: content-marketing:search-specialist` (fallback `general-purpose`), `run_in_background: true`. Each produces specs + tier-classified `sources.md` + `verification-log.md`.

- **Wave 2 (orchestrator, ~30–45 min):** verify each cohort:
  - spot-check 10% of statistics and commands
  - confirm every cited URL resolves (WebFetch)
  - confirm every ISO/IEC/IEEE 29119, ITIL, ISO 27001, NIST clause reference is real
  - confirm AcademiaPro spec assumptions match what's actually in `srs-skills/projects/AcademiaPro/`
  - append `# Pass 2 — Gap-fill addendum` headers where gaps found

- **Wave 3 (orchestrator only, never delegated):** cross-cohort synthesis:
  - cross-reference matrix linking each spec to gap → stage → score dimension
  - consistency check (does Cohort 02's canonical-path decision match how Cohort 03 references skill paths?)
  - score-ceiling reconciliation against the actual specs produced

- **Wave 4 (orchestrator, ~20–30 min):** assemble `.docx` via `research-report-builder` → `professional-word-output`. Order: front matter → 17 specs in stage order → cross-reference matrix → score ceiling → appendix (sources by cohort).

## 6. Hard exclusions (verbatim in every cohort brief)

- Stages 4–6 of the remediation roadmap (traceability, runtime evidence, semantic/audit assurance, AI hallucination scoring).
- New skills outside the 240 already in the catalog.
- Repo edits to `C:\wamp64\www\srs-skills\` — this deliverable is spec-only.
- Cost estimates, vendor selection, hiring plans.
- Any score promise above **9.1 / 10** — the ceiling is honest, not aspirational.

## 7. Evidence discipline

Every cohort agent prompt includes the verbatim hard-constraint clause from `skills/source-evaluation/references/evidence-discipline.md`. Standards citations (29119, 27001, ITIL, NIST) must reference real, verifiable clause numbers. URLs must be live as of verification date. AcademiaPro-specific claims must match what's actually in the repo, not invented context. Violations log to `EVIDENCE-AUDIT.md` and are stricken before Wave 4.

## 8. Final deliverable

`projects/srs-skills-completion-2026/export/srs-skills-completion-2026-v1.docx` — ~170–200 pages.

Handoff: copy `.docx` to `C:\wamp64\www\srs-skills\docs\completion-2026\srs-skills-completion-2026-v1.docx`.

## 9. Out of scope (explicit)

- Stage 4 — Requirements-to-code-to-test traceability schema and validators
- Stage 5 — Release manifest ingestion, runtime SLO/incident linkage
- Stage 6 — Clause-level semantic proof, contradiction detection, audit-grade compliance views
- AI assurance kernel — model/prompt evaluation loop, hallucination register, regression harness
- Domain pack rule-engine conversion (agriculture, education, finance, government, healthcare, logistics, retail, Uganda)
- Hybrid bidirectional change propagation between agile delivery and formal baselines

A follow-on project (`srs-skills-deepening-2026-q3` or similar) covers these.
