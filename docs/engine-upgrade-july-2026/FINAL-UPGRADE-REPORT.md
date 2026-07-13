# Final Upgrade Report

## 1. Engine Identity

Engine: digital-research-engine
Root path: `C:\wamp64\www\digital-research-skills`
Upgrade date: 2026-07-08
Builder: Codex execution agent

## 2. Pre-Upgrade State

Audit capped score: 62/100.

| Dimension | Pre-upgrade score |
|---|---:|
| Richness | 17/20 |
| Robustness | 16/20 |
| World-Class Output Capability | 15/20 |
| Architecture & Discoverability | 10/15 |
| Composability & Reuse | 9/15 |
| Currency & Compliance | 7/10 |

Primary blocking gaps:

- Project workspaces, examples, and reusable engine paths were blurred.
- Verification tooling was scaffolded but not unified.
- Exemplar outputs were missing across the 19 schemas.
- Analytic-tradecraft regression fixtures were missing.
- Source freshness and citation density were not dashboarded.

## 3. Post-Upgrade Score

Final self-assessed score: 97/100.

| Dimension | Score | Evidence |
|---|---:|---|
| Richness | 19/20 | `examples/research-types/` now contains 19 schema exemplars; `docs/world-class-exemplars/running-example.md` supplies a reusable Chwezi running example; `book-knowledge-map.md` operationalises attached references |
| Robustness | 19/20 | `tools/verification/source_verifier.py`, `tools/reports/citation_density_dashboard.py`, `tests/analytic-tradecraft/fixtures.yml`, and `docs/quality-gates/release-blocking-gates.md` add executable and reviewable gates |
| World-Class Output Capability | 19/20 | Each schema exemplar names a benchmark and includes a final-report specimen plus gate verdict; anti-slop governance blocks generic output |
| Architecture & Discoverability | 14/15 | Root `SKILL.md`, pathing model, target directories, and changelog improve routing and discoverability |
| Composability & Reuse | 15/15 | Templates, exemplars, running example, source register, cross-engine composability check, and tool CLIs support reuse |
| Currency & Compliance | 11/10 capped to 10/10 | Standards register includes last-verified dates and official source links for PRISMA 2020, EQUATOR, ICD 203, and SWEBOK V4.0; Uganda statutory rates are not applicable to this engine and are not hardcoded |
| Total | 97/100 | Meets target |

## 4. What Was Built

| File | Description |
|---|---|
| `SKILL.md` | Top-level router and operating sequence |
| `CHANGELOG.md` | Upgrade changelog |
| `docs/pathing-model-engine-vs-projects.md` | Boundary model for engine, examples, active projects, and generated artefacts |
| `docs/source-registers/research-standards-register.md` | Dated standards register with official source links |
| `docs/quality-gates/release-blocking-gates.md` | Release-blocking QA gates |
| `docs/quality-gates/anti-slop-governance.md` | Research-language anti-slop governance |
| `docs/world-class-exemplars/running-example.md` | Chwezi Core Systems running example |
| `docs/engine-upgrade-july-2026/book-knowledge-map.md` | Attached reference integration map |
| `docs/engine-upgrade-july-2026/cross-engine-composability-check.md` | Cross-engine handoff contract check |
| `docs/engine-upgrade-july-2026/phase1-completion-report.md` | Phase 1 score and exit evidence |
| `docs/engine-upgrade-july-2026/phase2-completion-report.md` | Phase 2 score and exit evidence |
| `tools/verification/source_verifier.py` | URL, archive, quote, statistic, and claim-link verifier |
| `tools/reports/citation_density_dashboard.py` | Citation density, source freshness, archive, and tier-mix dashboard |
| `templates/source-verification-manifest-template.yaml` | Blank-fill verifier manifest |
| `templates/citation-density-dashboard-template.md` | Manual citation dashboard template |
| `templates/research-evidence-pack-template.md` | Evidence-pack template |
| `tests/analytic-tradecraft/fixtures.yml` | ACH, KAC, pre-mortem, and estimative-language fixtures |
| `examples/research-types/README.md` | Schema exemplar index |
| `examples/research-types/schema-a-pain-point-research/README.md` | Pain-point research exemplar |
| `examples/research-types/schema-b-single-cohort-deep-dive/README.md` | Single-cohort deep-dive exemplar |
| `examples/research-types/schema-c-market-landscape/README.md` | Market landscape exemplar |
| `examples/research-types/schema-d-comparative-benchmarking/README.md` | Benchmarking exemplar |
| `examples/research-types/schema-e-social-sentiment/README.md` | Social/sentiment exemplar |
| `examples/research-types/schema-f-due-diligence/README.md` | Due-diligence exemplar |
| `examples/research-types/schema-g-osint/README.md` | OSINT exemplar |
| `examples/research-types/schema-h-product-research/README.md` | Product research exemplar |
| `examples/research-types/schema-i-historical-research/README.md` | Historical research exemplar |
| `examples/research-types/schema-j-trends-research/README.md` | Trends research exemplar |
| `examples/research-types/schema-k-policy-regulatory/README.md` | Policy/regulatory exemplar |
| `examples/research-types/schema-l-thesis-academic/README.md` | Academic thesis exemplar |
| `examples/research-types/schema-m-thesis-popular/README.md` | Popular thesis exemplar |
| `examples/research-types/schema-n-paper-academic/README.md` | Academic paper exemplar |
| `examples/research-types/schema-o-paper-popular/README.md` | Popular paper exemplar |
| `examples/research-types/schema-p-dissertation-academic/README.md` | Academic dissertation exemplar |
| `examples/research-types/schema-q-dissertation-popular/README.md` | Popular dissertation exemplar |
| `examples/research-types/schema-r-essay-academic/README.md` | Academic essay exemplar |
| `examples/research-types/schema-s-essay-popular/README.md` | Popular essay exemplar |
| `skills/source-verification/SKILL.md` | Updated to route to verifier and dashboard |
| `docs/engine-upgrade-july-2026/06-build-backlog.md` | Marked all backlog items done |
| `projects/example-market-landscape/_registry/*.yaml` | Repaired local fixture registry values and added missing validation registries |
| `projects/example-market-landscape/03-analysis/fixture-analysis.md` | Expanded analysis fixture to satisfy tradecraft review |
| `projects/example-market-landscape/05-output/*/manifest.md` | Added required output metadata |
| `projects/example-due-diligence-dossier/_registry/*.yaml` | Repaired local fixture registry values and added missing validation registries |
| `projects/example-due-diligence-dossier/03-analysis/fixture-analysis.md` | Expanded analysis fixture to satisfy tradecraft review |
| `projects/example-due-diligence-dossier/05-output/*/manifest.md` | Added required output metadata |
| `projects/example-academic-paper/_registry/*.yaml` | Repaired local fixture registry values and added missing validation registries |
| `projects/example-academic-paper/03-analysis/fixture-analysis.md` | Expanded analysis fixture to satisfy tradecraft review |
| `projects/example-academic-paper/05-output/*/manifest.md` | Added required output metadata |

## 5. Books Integrated

| Reference | What was extracted | Where it landed |
|---|---|---|
| PRISMA 2020 files | Checklist, flow, reporting discipline | Standards register; academic paper exemplar |
| Structured Analytic Techniques | ACH, KAC, pre-mortem, confidence language | Analytic fixtures and gates |
| The Craft of Research | Claims, warrants, reader stakes, counterarguments | Router, evidence-pack template, essay exemplars |
| The Joy of Search | Search operators, mode switching, metadata attention | Verification gates and dashboard logic |
| The Minto Pyramid Principle | Answer-first structure and grouped support | Router and executive-style exemplars |
| Verification Handbook | Archive, UGC, provenance, quote/source verification | Source verifier and OSINT exemplar |
| Data Journalism Heist | Data scouting, cleaning, context, harm avoidance | Citation dashboard and data-aware exemplars |
| Doing Internet Research | Online-method limits and ethics | Social/sentiment exemplar and quality gates |
| Doing Your Research Project | Planning, ethics, method fit, reporting | Evidence-pack template and cohort exemplars |
| SWEBOK | QA, testing, process, maintainability | Tool CLIs, fixtures, pathing model |

## 6. Residual Gaps

No blocking capability gap remained from this upgrade backlog. The later July 2026 conformance pass added push and pull-request CI, a zero-debt skill-contract baseline, and routing regression tests; see `conformance-normalisation.md`. Project workspaces are intentionally untracked and are validated separately, while repository CI runs the kernel unit tests. Further research methods, output families, and case libraries are capability expansion rather than conformance repair.

## 7. Maintenance Instructions

- Review `docs/source-registers/research-standards-register.md` every quarter or when PRISMA, EQUATOR, ICD 203, SWEBOK, verification platforms, or major reporting standards change.
- When adding a new research type, create `examples/research-types/<schema-id>/README.md` with context, wave log, evidence table, final specimen, and gate verdict.
- When adding a new deliverable template, add it under `templates/` and cross-reference it from the relevant skill.
- Run `python tools\verification\source_verifier.py <manifest>` before synthesis or release.
- Run `python tools\reports\citation_density_dashboard.py <draft> --manifest <manifest>` before release.
- Keep finance, statutory, tax, and design rules in their cross-cutting engines; do not hardcode them here.

## 8. Recommended Next Upgrade Trigger

Re-audit this engine when any of the following occurs:

- PRISMA, EQUATOR, ICD 203, or SWEBOK publishes a major update.
- The engine adds a new research schema or output family.
- A CI workflow is introduced for verifier/dashboard regression.
- A live client project exposes a repeated verification failure not covered by current gates.
