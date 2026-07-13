# July 2026 Conformance Normalisation

Date: 2026-07-13
Benchmark: canonical `skills-web-dev` skill-writing, composition, engine-audit, anti-slop, and slop-audit contracts.

## Before state

Filesystem discovery found 58 active skills and three existing non-skill templates. The `skills/proposal-skills` Git submodule was classified as a separate engine and excluded from active metrics.

The canonical read-only scanner reported 0 fully compliant skills. Its failure counts were: degraded mode 56, decision rules 52, capability contract 50, input contract 49, five anti-patterns 41, trigger 36, portable metadata 24, portable sections 24, output contract 23, and one empty contract section.

Supplementary checks found no invalid YAML, name mismatch, duplicate name, unsupported top-level key, or over-500-line entrypoint. They found 24 overlong descriptions, 28 descriptions without the required positive-trigger form, 23 missing negative-trigger sections, 36 missing evidence contracts, five audit/review skills without an explicit read-only default, two runner-specific bodies, six broken relative links, 16 files with encoding noise, and 53 skills without a worked example.

## Cause and cohort plan

The engine's previous July upgrade improved routing, research tools, exemplars, and project-kernel validation, but its skills pre-dated the current portable contract. The repair is split into three non-overlapping skill cohorts. Shared authoring rules, validator, zero-debt baseline, routing fixtures, CI, routers, documentation, and release remain centrally owned.

## Implemented controls

- Local authoring standard and reusable template.
- Filesystem-discovered contract validator with mandatory-resource, reference, permission, degraded-mode, decision, example, encoding, line-limit, and duplicate checks.
- Machine-readable zero-debt baseline.
- Positive, negative, collision, limited-capability, and failure-path routing fixtures with a top-three release gate.
- Push and pull-request CI for contract, routing, and repository validation.

## Final evidence

The final filesystem inventory contains 58 active skills and four template artefacts, one of which is the new `SKILL.md` authoring template. No active skill was added, removed, renamed, consolidated, or deactivated.

| Gate | Final result |
|---|---|
| Local contract validator against zero-debt baseline | 58/58 compliant; empty failure counts |
| Canonical engine compliance scanner | 58/58 compliant; empty failure counts |
| Canonical quick validator | 58/58 passed |
| Routing smoke test | 28/28 fixtures in the expected top three; precision 1.000 against threshold 1.000 |
| Entrypoint line limit | 58/58 at or below 500 lines; maximum 485 |
| Kernel unit tests | 12 passed |
| Full pytest suite | 15 passed |
| Python syntax compilation | Passed for `engine`, `scripts`, and `tools` |
| Relative links and mandatory resources | Passed by local and canonical validators |
| Anti-slop audit | A; no blocking or generic repeated-line findings; `leverage point` retained only as the precise systems-thinking term |
| Diff whitespace check | Passed |

The canonical before-state failure counts are all zero after normalisation: capability contract 50 to 0, decision rules 52 to 0, degraded mode 56 to 0, five anti-patterns 41 to 0, input contract 49 to 0, output contract 23 to 0, portable metadata 24 to 0, portable sections 24 to 0, trigger 36 to 0, and empty contract section one to 0.

The release commit and remote equality are verified in Git at release time; Git remains the authoritative record for the commit identifier.

## Outside conformance

New research methods, additional output families, and deeper domain case libraries are capability expansion. They are not conformance debt and are not added solely to improve a metric.
