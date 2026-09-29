# 05 Per-output-type readiness

All scores are judged against the bar: a top intelligence-shop or peer-reviewed product. Each
output type is scored on whether the engine can drive it from end to end, with evidence and a
worked proof. No output type has an executed Tier-3 behavioural run (`NOT_ASSESSED`), so no score
reflects demonstrated agent performance.

## Ranked table

| Rank | Output type | Score | Owning route | Biggest gaps | Lift moves |
|---:|---|---:|---|---|---|
| 1 | Verified fact brief | 62 | `source-evaluation` → `source-verification` → `tools/verification/source_verifier.py` | One-sentence worked examples. No filled brief in the repository apart from the model-policy review. Semantic support stays human-only (correctly), but no reviewer exemplar exists | Add `source-verification/examples/verified-fact-brief.md` with a real manifest and verification report |
| 2 | Source register | 60 | `source-evaluation`, `templates/source-verification-manifest-template.yaml`, `validate_source_currency.py` | Example registers are fixtures (`SRC-0001 "Fixture source"`). The standards register has 8 rows. No example of `affected_claim_ids` in use | A real 15–30-row register from a completed wave, with archive links and review dates |
| 3 | Model-policy and currentness review | 60 | `AGENTS.md` Codex section, `docs/continuous-improvement/kaizen-currentness-gate.md` | The dated 2026-09-28 review is well sourced (S01–S07, R01–R03), but it covers the Codex pin only. No equivalent record exists for the Claude runtime or for non-model standards. It is vendor-sourced by nature | A generic currentness-review template reused for standards, laws and platforms |
| 4 | Research wave plan and synthesis | 58 | `research-orchestration`, `mind-mapping-and-synthesis`, `agentic-research-operations` | No filled wave plan, agent brief or cross-cohort synthesis exemplar. Wave-merge verification (10 % stats, 5 quotes) is stated but has no recorded example | Add a worked four-wave plan and brief set for the running example |
| 5 | OSINT / due-diligence report | 57 | `osint-investigation`, `due-diligence`, `pi-investigation` | The worked dossier is a three-line fixture. No case-vault, chronology or CARA exemplar. The Berkeley Protocol is not central. Personal-data law coverage (for example the Uganda Data Protection and Privacy Act, Kenya's Data Protection Act, GDPR) is thin | Synthetic but complete CARA report; a chronology with per-event confidence; a data-protection checklist per jurisdiction |
| 6 | Literature review | 55 | `academic-reporting-standards`, `academic-writing`, `research-design` | Rigour defaulting is good, but there is no PRISMA flow, search log or screening table example. TOP is stated in its superseded form. PRISMA-S (search reporting) is not named | Worked scoping-review search log with a PRISMA 2020 flow; correct TOP to the 2025 structure |
| 7 | Quarterly ecosystem scan | 52 | dev `skill-engine-audit` intake; `docs/continuous-improvement/ecosystem-scan-2026-Q4.md` (158 lines) | One quarter recorded. Owned by the dev method, not by a research skill. Verdicts depend on the agents register | Keep it; add a research-specific source-evaluation pass per candidate |
| 8 | Legal research memo | 50 | `online-legal-research` | US-derived source books. The EA overlay is categories only (2026-04-27). No repository coverage or access log. No memo exemplar. Duplicated degraded and evidence sections | A dated repository register (KenyaLaw, ULII, EACJ, gazettes) with access and coverage checks; one worked memo on a synthetic fact pattern |
| 9 | AI evaluation and data flywheel | 48 | `ai-evaluation-and-data-flywheel`, `evals/seek-research/` | The pilot protocol is "design only; no labelled pilot cohort or performance result exists". The replay gate uses synthetic fixtures only. T3 is `NOT_ASSESSED` | First labelled cohort (20–30 real cases) with a baseline measurement |
| 10 | Market-evidence pack | 45 | `quantitative-modelling`, `dataset-discovery-and-analysis`, `schema-c-market-landscape` | One reference file for modelling. No sizing exemplar (top-down against bottom-up reconciliation). The market-landscape example project is a fixture | Harden `quantitative-modelling` with a sizing reference and a worked triangulated model |
| 11 | Benchmark / competitive study | 40 | None; only `examples/research-types/schema-d-comparative-benchmarking/README.md` (35 lines) | No owning skill, method, scoring-frame guidance, like-for-like normalisation or competitor-evidence rules | New `benchmarking-and-competitive-study` skill with a worked comparison matrix |

**Output-type readiness (mean of 11): 587 ÷ 11 = 53.4, used as 53.**

The brief named nine output types. The engine purpose statement adds two more, the
eval flywheel and the quarterly ecosystem scan, so both are scored above and included in the mean.
