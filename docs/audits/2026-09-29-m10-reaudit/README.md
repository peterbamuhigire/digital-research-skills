# Digital Research Engine: M10-14 measured re-audit (29 September 2026)

Engine: `digital-research-engine` (GitHub repository `digital-research-skills`, catalogue id
`digital-research-skills`), audited read-only at committed HEAD `2b9c87d`. There are 59 active
skills. The auditor did not execute any my-10-kaizen phase.

## Headline numbers

| Number | Score /100 | Basis |
|---|---:|---|
| **Raw** | **51.6** | Weighted overall from judged dimensions, routing judged at 58 |
| **Measured-constrained** | **51.6** | Raw with routing replaced by Engine Eval Readiness (57.5) |
| **Published** | **51.6** | `min(51.6, 65)`. The 65 cap does not bind; the portfolio craft standard's acceptance evidence is absent in any case |
| **Engine Eval Readiness** | **57.5** | T1 30.00 + T2 27.51 + T3 0 (NOT_ASSESSED); ceiling 70 while T3 is unexecuted. Recomputed and agreed |

Weighting: output readiness 30, skill depth and worked examples 25, standards currency 15,
taxonomy 10, doctrine 10, hygiene 10 (hygiene = mean of redundancy, discovery/routing, safety).
No dimension, group, skill or output type scored 70 or above.

## Verdict

The engine's evidence doctrine is the strongest part of it. Every research route is held to
claim-level sourcing, `NOT_ASSESSED` states and currentness records, and a 171-test suite passes
locally. The skill layer does not yet deliver on that doctrine. In 56 of 59 skills the worked
example is a single sentence. The three `projects/example-*` "worked" outputs are three-line
kernel fixtures. Routing fixture coverage is 0 of 59 skills. About a quarter of the catalogue is
engineering or documentation material that belongs to, or duplicates, the dev engine. Two output
types the engine claims, benchmarking and competitive study, and market-evidence packs, have no
owning skill of adequate depth. Remote CI ("Skill engine quality") is red at HEAD because of two
cross-repository relative links. The local T1 pass depends on the host, not on the repository.
The engine is competent and honest about its own limits, but its applied proof falls well short
of top intelligence-shop or peer-reviewed level.

## Files

| File | Contents |
|---|---|
| [00-executive-summary.md](00-executive-summary.md) | Verdict, headline findings, strengths, path to the bar |
| [01-methodology-and-rubric.md](01-methodology-and-rubric.md) | Method, commands, rubric, weighting, limitations, independence |
| [02-coverage-and-taxonomy.md](02-coverage-and-taxonomy.md) | Taxonomy score and named deficiencies |
| [03-existing-groups-audit.md](03-existing-groups-audit.md) | Eight groups scored; 16 sampled skills scored |
| [05-per-output-type-readiness.md](05-per-output-type-readiness.md) | Eleven output types scored and ranked |
| [09-master-scorecard.md](09-master-scorecard.md) | All 11 dimensions, groups, output types, three overall numbers with arithmetic |
| [10-roadmap-to-world-class.md](10-roadmap-to-world-class.md) | P0/P1/P2 moves with named files and phase targets |
| [11-measured-evidence.md](11-measured-evidence.md) | Commands, exit codes, output lines, Readiness arithmetic, NOT_ASSESSED list |

Files not produced in this re-audit:

- `04-gap-analysis-new-skills.md`: not re-run in the M10-14 measured re-audit. The short gap list is in 02 and 10.
- `06-standards-benchmark.md`: not re-run in the M10-14 measured re-audit. One external currency check is recorded in 09 and 11.
- `07-hardening-existing-skills.md`: not re-run in the M10-14 measured re-audit. The hardening moves are in 10.
- `08-reading-list.md`: not re-run in the M10-14 measured re-audit.

## Prior audits compared

- `docs/audits/2026-09-06-kaizen.md` published no numeric score ("NOT ASSESSED, capped at 65").
  Its two companion reviews covered the source-currency validator and the machine-error gate only.
- `docs/kaizen/2026-09-23-research-scraping/01-baseline-scorecard.md` gave 54.8 raw, scoped to
  scraping only.
- `docs/analysis/initial-evaluation/00-executive-summary.md` (26 April 2026) was a self-assessment
  on a different rubric: 62, then 65.

None of these scores is comparable one-for-one with this audit. Movement is described in 00 and 09.
