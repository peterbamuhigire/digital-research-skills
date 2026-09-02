# Kaizen Engine and Product Audit Reference

Use this reference with the portfolio standard at `docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md`.

## Audit output

Produce one table per applicable engine dimension and one table per product type. Record: evidence inspected, raw score, concrete gap, risk, and next action. Publish `min(raw overall score, 65)` as the audit score. Keep the raw scores visible so the cap cannot hide deterioration.

## Product types

Adapt the checklist to research reports, evidence packs, due-diligence files, datasets, dashboards, source registers, academic outputs, proposals, and Word/PDF deliverables. At minimum inspect:

- decision/audience fit and research design;
- source provenance, tiering, independence, timeliness, and limitations;
- claim-to-source links, quote/stat verification, and contradiction handling;
- reasoning, inference labels, uncertainty, and reproducibility;
- accessibility, readability, and format fidelity;
- privacy, safety, legal/ethical boundaries, and release blockers;
- reviewer handoff, registry completeness, and post-release feedback loop.

## 95-plan pattern

For every dimension below 95, create a P0/P1/P2 action. Each action needs a named file or validator, an owner, an expected measure, and acceptance evidence. The plan is incomplete if it adds prose without a fixture, test, source register, or reviewer result.

## Mandatory 65-to-95 gate

The initial analysis must show raw findings but publish a hard-capped score:
`capped_score = min(raw_score, 65)`. Keep missing evidence, defects, and stop
conditions visible; the cap never waives them. Only after recording that baseline
may the researcher run the improvement cycle toward 95/100. Each cycle item needs
a root cause, reversible intervention, owner, measure, guardrail, stop/rollback,
acceptance evidence, standardisation location, and re-audit date. Apply this both
to the research engine and to every report, evidence pack, dataset, dashboard,
proposal, Word/PDF, or other research product it produces.

## Research-specific measures

Useful measures include: percentage of load-bearing claims with verified source IDs; percentage of numeric claims spot-checked; unresolved-claim count; citation-density defects; source-register completeness; reproducibility of search and synthesis; reviewer agreement; and time from finding to standardised fix. These are measures to collect, not invented baselines.

## Book-driven Kaizen Wave 3

Apply the [18-source cross-engine study](book-driven-kaizen-wave-3-2026-09-02.md) when a
book-derived improvement is proposed. Admit durable concepts as hypotheses, verify volatile
claims against current primary sources, preserve access and safety boundaries, and keep the
prompt-engineering source `NOT_ASSESSED` until a valid artifact is supplied.
