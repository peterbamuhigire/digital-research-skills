# Concrete Build Backlog

| # | Filename/path | Purpose | Acceptance criteria | Effort |
| --- | --- | --- | --- | --- |
| 1 [DONE 2026-07-08] | docs/pathing-model-engine-vs-projects.md | Clarify what belongs in engine, examples, and active research projects. | Validation can flag project clutter or unmanaged empty phase folders. | S - Completed with path classification, empty-directory rules, validation contract, and promotion path. |
| 2 [DONE 2026-07-08] | tools/verification/source_verifier.py | Automate URL, archive, quote, statistic, and citation checks. | Produces per-source status, evidence, confidence, and unresolved verification gaps. | L - Completed with CLI verifier, Markdown/JSON reports, release-ready status, and manifest template. |
| 3 [DONE 2026-07-08] | examples/research-types/<schema-id>/ | Add exemplar outputs for all supported research schemas. | Each has context, wave logs, evidence table, final report, and slop/evidence gate verdict. | L - Completed for schemas A-S using the Chwezi running example. |
| 4 [DONE 2026-07-08] | tests/analytic-tradecraft/fixtures.yml | Create scored fixtures for ACH, KAC, pre-mortem, and estimative language. | Expected findings and confidence language are deterministic enough for regression checks. | M - Completed with four deterministic tradecraft fixtures. |
| 5 [DONE 2026-07-08] | tools/reports/citation_density_dashboard.py | Measure source density, freshness, and primary/secondary mix. | Dashboard flags unsupported claims and stale/high-risk sources. | M - Completed with CLI dashboard, source mix, stale-source, archive, quote, and numeric-claim checks. |
