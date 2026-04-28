# research-output-formats

Router skill for deciding **what kind of document** the engine is producing and which voice / citation regime applies.

Sits above `academic-writing`, `business-writing`, `report-and-proposal-craft`, `analytic-tradecraft`, `consulting-delivery`, and `online-legal-research`. Tells you which of those to invoke for the deliverable in hand.

## Files

- `SKILL.md` — entry, selection router, decision flow
- `CLAUDE.md` — Claude-Code-specific load order
- `AGENTS.md` — Codex / generic-agent equivalent
- `references/academic-formats.md` — essays, papers, theses, dissertations, research proposals, literature reviews
- `references/advocacy-and-public-formats.md` — pamphlets, op-eds, policy briefs
- `references/commercial-formats.md` — white papers, market research reports, market analyses, product descriptions, case studies, feasibility studies
- `references/analytical-and-professional-formats.md` — intelligence reports, legal opinions
- `references/academic-vs-nonacademic-variants.md` — voice, citation density, hedging, design across the variant axis

## The two axes

1. **Format family** — what document this is (essay, brief, white paper, opinion …)
2. **Academic vs non-academic variant** — who reads it and what they accept as proof

Resolve both before drafting.

## Hard rule

Format selection never overrides evidence discipline. The `source-evaluation` clause applies to every variant of every format — including pamphlets, op-eds, and product descriptions.
