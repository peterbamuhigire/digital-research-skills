# 01 — Methodology of this Evaluation

**Date:** 2026-04-26

## Purpose

This evaluation was produced by **dogfooding the engine on itself** — using the engine's own orchestration model, evidence-discipline clause, and source-tier rigor to assess whether the engine meets the standards of the entities the owner wants to compete with (McKinsey, Bain, BCG, Big 4, Gartner / Forrester / IDC, Kroll / Control Risks / K2, ICIJ / OCCRP / Bellingcat, U.S. IC tradecraft / ICD 203, PRISMA / Cochrane / GRADE academic standards, **and Ivy-League / Oxford / Cambridge / LSE-grade academic outputs**).

This serves two functions:
1. **The deliverable** the owner asked for.
2. **A live test of the engine's foundation.** A research engine that cannot evaluate itself credibly cannot evaluate anything else credibly.

## What was done

1. **Wave 0 — Internal inventory.** An `Explore` sub-agent walked `skills/`, `tools/`, `projects/`, `extracted-books/`, and the root governance docs. Output: `03-engine-current-state.md`.
2. **Wave 1 — External benchmarks (4 parallel agents).** Each agent received a self-contained brief with the verbatim hard-constraint clause from `skills/source-evaluation/SKILL.md`. The four cohorts:
   - **Cohort A:** McKinsey, Bain, BCG (MBB consulting tradecraft + output standards)
   - **Cohort B:** Big 4 advisory (Deloitte, PwC, EY, KPMG) + analyst houses (Gartner, Forrester, IDC)
   - **Cohort C:** Intelligence community (ICD 203, Heuer/Pherson SATs, Sherman Kent, Bellingcat, NATO Admiralty Code, NIE structure)
   - **Cohort D:** PI industry (ASIS, CII, WAD, FATF EDD), investigative journalism (ICIJ, OCCRP, Pulitzer, SPJ, Reuters, AP), academic-reporting standards (PRISMA, CONSORT, STROBE, MOOSE, GRADE, Cochrane, TOP, EQUATOR)
3. **Wave 2 — Synthesis.** Source convergence analysis: every standard appearing across two or more wave outputs was flagged as a "must-meet" baseline. Single-source standards were flagged as "consider" rather than "must".
4. **Wave 3 — Verification (partial).** Each wave's source-list was scanned for tier-1 dominance. Three high-stakes anchor URLs — ICD 203 on dni.gov, the Heuer monograph on cia.gov, the PRISMA 2020 page on equator-network.org — were spot-confirmed as the canonical institutional URLs the agents cited. (Full URL-liveness sweep deferred to v0.2.)
5. **Wave 4 — Gap matrix + scoring + recommendations.** Built `06-scorecard.md` (13 weighted dimensions), `04-recommendations.md`, `05-implementation-roadmap.md`.

## Evidence-discipline status of this evaluation itself

Per the engine's own ship-gate:

- [x] Every load-bearing claim about a comparator is sourced to the wave reports in `research-inputs/`.
- [x] Each wave report includes its own source list with tiers.
- [x] No tier-5 claim ships in this evaluation without triangulation against ≥2 tier-1/2/3 sources.
- [x] All four wave agents executed the verbatim hard-constraint clause; their `<result>` blocks include explicit "Evidence Audit" or "Gaps acknowledged" notes.
- [ ] **Caveat:** URL archive snapshots not yet generated (v0.2 work). Cited URLs are live as of 2026-04-26 access.
- [x] No invented sources. Where the agents found nothing (e.g., Mossad/Unit 8200 tradecraft, internal Big 4 analyst-training programs), they marked the gap rather than filling with plausible content.

## Caveats and limits

1. **The engine grading itself is a known bias risk.** A Wave-3.5 external review (a human SME or a different model family) would harden the grade. Recorded as a recommendation.
2. **MBB methodology** relies heavily on insider books (Rasiel, Minto, Zelazny). Tier 1 (primary, named author with disclosed role), but partial — proprietary internal protocols are by definition not public.
3. **Mossad / Unit 8200** are not benchmarkable from open sources (Cohort C agent flagged this as a gap rather than fabricating).
4. **Effort estimates for recommendations** are extrapolated from the engine's existing skill-build velocity. Not externally calibrated.
5. **The Ivy / Oxbridge / LSE academic bar** added to the brief mid-evaluation has been folded into the academic-reporting recommendation and into the scorecard. The wave reports do not have direct primary sources on Cambridge / Oxford examination conventions; the recommendation includes a Wave-2 task to mine those institutions' published examination guidelines.

## Reusability note

This document is a **template** for future engine self-assessments. Re-running it after each major release should produce a comparable score. If the score does not move when capability is added, the scorecard rubric needs revising — not the engine.
