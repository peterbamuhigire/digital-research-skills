# Baseline scorecard

Published score is capped at 65/100 as required by the Portfolio Kaizen
Standard. Evidence is repository inspection on 2026-09-23.

| Dimension | Raw | Evidence and deficiency |
|---|---:|---|
| Doctrine | 70 | Scraping foundations and ethics existed; end-to-end collector contract was missing. |
| Taxonomy/routing | 62 | Scraping skills were discoverable; no CLI entry point or run-output route existed. |
| Skill depth | 58 | HTTP, cache, and extractors existed separately; no bounded crawl composition. |
| Applied proof | 42 | No focused tests for research scraping modules. |
| Standards currency | 55 | Currentness gate existed; runtime model catalogue was unavailable and policy check drifted. |
| Output readiness | 48 | No stable records-plus-manifest output contract. |
| Accessibility/inclusion | 45 | No target-specific language or accessibility extraction guarantee. |
| Production/handoff | 40 | No operator CLI or explicit stop/report behavior for a run. |
| Hygiene | 68 | Book cache was ignored; raw source leakage was not introduced. |
| Safety/integrity | 60 | Robots and block classes existed; same-host bounds and per-run provenance were incomplete. |

Raw mean: 54.8/100. Published capped score: `min(54.8, 65) = 54.8/100`.
Primary blocker: live target authorization and current behavior remain outside
repository tests.
