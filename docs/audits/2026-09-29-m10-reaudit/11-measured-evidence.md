# 11 Measured evidence

**Host:** Windows 11, Python 3.13 (`C:\Python313\python.exe`).
**Working directory:** `C:\wamp64\www\digital-research-engine`, HEAD `2b9c87d`.
**Environment:** `PYTHONDONTWRITEBYTECODE=1`.
**Date:** 29 September 2026. `git status --short` was clean before and after the runs.

## T1: declared validators, plus the requested test suite

| # | Command | Exit | Key output |
|---:|---|---:|---|
| 1 | `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json` | 0 | `active skills: 59`, `template skills: 1`, `fully compliant: 59`, `failure counts: {}` |
| 2 | `python -X utf8 scripts/routing_smoke_test.py --min-rank1 84 --lint-fixtures` | 0 | `29/29 top-3 precision=1.000 threshold=1.000 (lexical proxy; not live routing)`, `precision@1: 25/29 (86.2%)`, `owned negatives: 9 (pass 7, fail 0, not assessed 2)`, `rank-1 floor: 84.0%`, `fixture lint findings: 0` |
| 3 | `python -X utf8 scripts/validate_engine.py` | 0 | Re-runs 1 and 2, then `no-book-extractions: OK`, `Engine doctor OK.`, `Ran 37 tests … OK` |
| 4 | `python -X utf8 -m pytest -q -p no:cacheprovider` | 0 | `171 passed, 2 skipped, 11 subtests passed in 26.51s` |

The routing results are lexical figures. They are a drift guard, not proof of live routing.

## Supplementary read-only checks

| Command | Exit | Key output |
|---|---:|---|
| `python -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json` | 0 | `findings: 0`; `PASS: metadata/date checks only; claim support NOT ASSESSED` |
| `python -X utf8 scripts/validate_machine_error_gate.py` | 0 | `checks: ME1…ME7, AS1…AS7`, `engines: 12`; `semantic, editorial and visual verification: NOT ASSESSED` |
| `python -X utf8 scripts/skill_fanin.py --engine digital-research-engine --json` (in chwezi-engine-agents) | 0 | `active_skills: 59`, `zero_inbound: 3` (`00-meta-initialization`, `capability-matrix`, `skill-taxonomy-and-routing`), 29 skills with no fixture reference |

## Remote CI (read-only `gh`)

- `gh run list --limit 5` shows "Skill engine quality" failed on the HEAD push
  (run `36520107821`, 2026-09-29T04:06Z) and on the previous push (run `36511456319`).
  "source-ingestion-guardrail" succeeded on both.
- `gh run view 36520107821 --log-failed` shows:
  - `fully compliant: 57`
  - `failure counts: {"broken_relative_link": 2}`
  - `baseline mismatch`
  - exit code 1
- The two links resolve outside the repository:
  - `skills/ai-slop-audit/SKILL.md:146` → `../../../chwezi-dev-engine/references/ai-slop-responsible-publishing-standard-2026-09-11.md`
  - `skills/anti-ai-slop/SKILL.md:129` → the same target
- This confirms the brief's report: red, with two broken cross-repository links.

## T2 and Readiness inputs (portfolio evidence, M10-14)

Source: `chwezi-engine-agents/docs/operations/m10-kaizen-evidence/M10-14/`.

| File | Entry for this engine |
|---|---|
| `eval-readiness.json` | `readiness 57.5`; slots T1 1.0, T2_p1 0.8621, T2_neg 0.8889, T2_cov 0.0, T2_clean 1.0, T3 0.0; `not_assessed: ["T3 (zero-spend rule; 0 grading.json files)"]` |
| `readiness/tier1-results.json` | `declared 3, passed 3, t1 1.0`, head `2b9c87d` |
| `readiness/t2-inputs.json` | p@1 25/29; owned negatives `pass_local 7, mirror_pass 1, mirror_fail 1, total 9`; `"056 rank 1; 055 rank 4 (fail)"` |
| `readiness/coverage.json` | `active_skills 59`, `skills_with_positive 28`, `skills_with_owned_negative 5`, `skills_ge3pos_ge2neg 0` |
| `readiness/collision-scan.json` | Cross-engine pairs at 0.75 or above involving this engine: 4, all declared `canonical_owner` (validation-contract 1.0, ai-slop-audit 0.8257 and 0.7895, excel-spreadsheets 0.823). Warnings below 0.75: project-requirements with dev 0.712; ai-slop-audit with business-plan 0.705. No within-engine pair for this engine |
| `route-oracles-summary.json` | `digital-research-skills` primary@1 1/1 |

The failing mirror is `evals/cases/055-route-release-evidence-mirror.yaml`. It expects
`chwezi-dev-engine/validation-contract` first, with the "identical descriptions; tie broken by
key order" note.

## Readiness arithmetic (recomputed)

1. T1 = 30 × 1.0000 = 30.00
2. T2 mean = (0.8621 + 0.8889 + 0.0000 + 1.0000) ÷ 4 = 2.7510 ÷ 4 = 0.68775
3. T2 = 40 × 0.68775 = 27.51
4. T3 = 30 × 0 = 0.00 (NOT_ASSESSED)
5. **Readiness = 57.51, reported as 57.5.** The auditor agrees.

Clean-CI sensitivity (not substituted): with T1 = 2/3, T1 = 20.00 and Readiness = 47.5.

## External currency check (web)

- The TOP Guidelines page, https://www.cos.io/initiatives/top-guidelines (accessed 2026-09-29),
  describes TOP 2025. It has seven research practices, three implementation levels (Disclose;
  Share and Cite; Certify), two verification practices and four verification study types.
- The engine states "8 modular standards × 3 implementation levels" at
  `skills/academic-reporting-standards/SKILL.md:90`. That is the superseded structure.

## Catalogue scans (auditor scripts in scratchpad, heuristic)

- Worked-example sections under 60 words: 56 of 59.
- Skills with a repeated H2 heading: 19.
- Skills with generated "… Notes/Guidance/Detail" headings: 39 (heuristic; includes some
  legitimate headings).
- Companion-list names resolving to neither an active skill nor a local reference file: 52
  distinct names, about 100 mentions.
- Files containing `C:/wamp64` under `skills/`: 4.

## NOT_ASSESSED list

| Item | Cause | Effect |
|---|---|---|
| T3 behavioural runs (all planned cases) | Zero-spend rule; 0 `grading.json` files | 30 Readiness points at 0; Readiness ceiling 70 |
| 2 local owned negatives | The smoke test reports `not assessed 2` (cross-engine owners); 1 is recovered by mirror 056 and 1 fails at 055 | Counted in the T2_neg denominator |
| Semantic claim support in any project corpus | Human review required; the validators check metadata only | No output type credited with verified semantic support |
| Visual and render fidelity of generated DOCX, PDF and XLSX | Not run; separate integration gate | Production dimension judged, not measured |
| Standards benchmark and reading list (files 06 and 08) | Not re-run in this re-audit | Standards currency judged from the engine's own records plus one external check |
| Parallel audit fleet | Replaced by a single auditor working through each concern in turn | Documented limitation (01) |
| Portfolio craft standard acceptance evidence | Absent | Published cap of 65 applies (does not bind) |
