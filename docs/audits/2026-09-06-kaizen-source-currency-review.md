# Source-currency validator repair, 6 September 2026

Disposition: scoped robustness defects CLOSED with regression evidence. This is
a local code review for the engine maintainer, not a research-product approval.
Preflight: `NO_TIME_SENSITIVE_CLAIMS`; no external source collection was required.

Read root AGENTS/router, local Kaizen/currentness/adoption and authoring guides,
source-evaluation/evidence-discipline, source-verification and relevant freshness
and verification references. Their evidence boundary governs the CLI wording:
`PASS: metadata/date checks only; claim support NOT ASSESSED`.

## Changes and acceptance

| Observed defect | Implemented control and regression evidence |
|---|---|
| Non-object roots crash; empty sources pass | Object root and nonempty source list required; malformed rows return findings. |
| IDs coerced or overwritten | Source/claim IDs require nonblank strings; duplicate definitions and duplicate claim source IDs fail without coercion. |
| Malformed claims skipped or coerced | Claims, when supplied, require a list of objects; each requires a boolean currentness flag and a typed source-ID list. Unknown references fail even for noncurrent claims. |
| Current claims without sources pass | Current claims require at least one known, currentness-qualified source. |
| Future access/verification dates pass | Both dates must be on or before the assessment date. Same-day access, verification and review pass; overdue and reversed chronology still fail. |
| Encoding errors escape | Invalid UTF-8, invalid JSON and unreadable files return findings; CLI decoding/JSON failures exit 1 without traceback. |
| Existing test writes beside tracked fixtures | All new/mutated manifests use pytest `tmp_path`; CLI regression verifies input bytes remain unchanged. |

Compatibility: positional manifest and `--as-of` remain. Absent or empty `claims`
remain valid for a source-only register. An explicit false currentness flag may
have an empty source list, but cannot bypass shape checks. Scheduled review dates
may be future dates. Actual register dates and the tracked fixture were not edited.

## Validation evidence

Baseline code: HEAD `0ec5084c0461d068d5a4699ed16236a123ae770f`, loaded into an
in-memory module without reverting files. The new test suite excluding CLI and
encoding cases recorded **58 failed, 23 passed, 3 deselected**, exit 1. This count
includes diagnostic-contract assertions as well as bypasses; it is not 58
distinct defects. No original test that wrote into tracked fixtures was run.

| Check from repository root | Result | Exit |
|---|---|---:|
| `python -B -X utf8 -m pytest tests/test_source_currency.py -q -p no:cacheprovider` | 84 passed | 0 |
| `python -B -X utf8 -m pytest -q -rs -p no:cacheprovider` | 113 passed, 2 skipped, 11 subtests passed | 0 |
| `python -B -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json` | 0 findings as of 2026-09-06; metadata/date PASS only | 0 |
| `python -B -X utf8 scripts/source_ingestion_guardrail.py` | 0 findings | 0 |
| `python -B -X utf8 scripts/routing_smoke_test.py` | 29/29 | 0 |
| `python -B -X utf8 scripts/validate_engine.py` | 59 compliant active skills, 1 template; routing 29/29; doctor OK; 22 kernel tests passed | 0 |

The two skips require installed portfolio/visual adapters and explicit opt-in;
they were not enabled. No other engine was opened. Skill counts are observed
validator output, not a catalogue change made by this sidecar.

## Limits and next review

Only `scripts/validate_source_currency.py`, `tests/test_source_currency.py` and
this report were edited with `apply_patch`. Concurrent machine-error-gate changes
belong to the main worker and were left intact. No commit, publication, external
claim verification or source-register mutation occurred.

The validator checks declared metadata, references and dates; it does not fetch
sources, establish authenticity or decide semantic claim support. Those checks
remain NOT ASSESSED. Local editorial review retained concrete findings and these
limits; visual checks are not applicable and automated genericness is NOT ASSESSED.
No numeric engine-readiness score is inferred from test counts.

Owner: engine maintainer. The experiment standardises fail-closed input checks
through the regression suite. Re-review on the next manifest-schema change;
acceptance is the focused suite plus native gates without changing evidence dates.
Recovery is a scoped reversal of this repair only, preserving unrelated work.
