# Cross-Engine Composability Check

Date: 2026-07-08
Engine: digital-research-engine

## Handoff Contracts

| Adjacent engine / skill family | When to route | Contract |
|---|---|---|
| design-system-skills | Visual formatting, typography, document/presentation appearance, charts | Research engine supplies verified claims, chart-ready data, labels, caveats, and source notes; design engine owns visual treatment |
| chwezi-accounting-doctrine | Finance, accounting, tax, IFRS, budgets, financial statements | Research engine supplies evidence pack and source register; accounting engine owns accounting treatment and statutory-rate validation |
| proposal-skills | Donor investment case, bid, EoI, proposal, pitch | Research engine supplies evidence base, verified claims, and source confidence; proposal engine owns evaluator journey and bid compliance |
| srs-skills / software requirements | Product or system requirements derived from research | Research engine supplies user evidence, decision constraints, and assumptions; SRS engine owns requirements formalisation |
| skills-web-dev | Web implementation of research outputs | Research engine supplies content, verified claims, and data contracts; web engine owns implementation |

## Consistency Checks

- Chwezi naming is consistent: `Chwezi Core Systems` or `Chwezi`; no prior brand name appears in newly written files.
- Visual/typographic doctrine is referenced, not duplicated.
- Finance/statutory facts are not hardcoded in this engine.
- Evidence discipline remains the first routing rule.
- Source registers use last-verified, reviewer, next-review, source-tier, and verification fields.

## Result

Pass. No cross-engine contract conflict found in the files created during this upgrade.
