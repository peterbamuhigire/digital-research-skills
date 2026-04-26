# Executive Summary — Digital Research Engine v0.1 Evaluation

**Date:** 2026-04-26
**Author:** Engine self-assessment (dogfooded; methodology in `01-methodology.md`)
**Audience:** Engine owner / consulting practice principal
**Verdict:** **62 / 100** baseline → **65 / 100** after the 2026-04-26 build session shipped `executive-communication`, `analytic-tradecraft`, and `academic-reporting-standards` (full skills with references) plus `research-techniques` and `osint-investigation` enhancements. Strong methodological foundation; closing the layers that separate a research *engine* from a research *organization*.

See `06-scorecard.md` for the post-session breakdown; biggest lifts were SAT coverage (+5.3) and output craft (+4.3) — the highest-leverage gaps the original eval named.

---

## TL;DR

The engine has built a defensible **evidence-discipline core** that already exceeds Big-4 thought-leadership transparency, matches OCCRP/ICIJ verification ethos, and partially aligns with U.S. IC tradecraft (ICD 203). It is **not** yet competitive with McKinsey/Bain/BCG, top-tier corporate intelligence firms (Kroll, Control Risks, K2), or intelligence-community analytic standards on six measurable dimensions:

1. **Estimative discipline** — no calibrated probability lexicon (Sherman Kent / ODNI ranges)
2. **Structured analytic techniques** — no ACH, Key Assumptions Check, Pre-Mortem, Red Team, Devil's Advocacy as named, executable skills
3. **Quantitative rigor** — no market-sizing triangulation, no scenario / sensitivity modeling, no financial models
4. **Communication craft** — no Pyramid Principle / MECE / "answer-first" / action-title discipline; no Zelazny chart selection
5. **Reporting-standard fluency** — no PRISMA 2020 / CONSORT 2025 / GRADE / TOP / Cochrane awareness for academic outputs
6. **Knowledge management** — no McKinsey-KNOW-equivalent (sanitised reusable artefacts, "knowledge nuggets", searchable case library)

Closing these six gaps is **6–9 months of focused build-out** and would lift the engine to ~**85/100**, a credible challenger for non-quantitative strategy + investigative work.

---

## Score breakdown (out of 100)

| Dimension | Weight | Score | Weighted |
|---|---|---|---|
| Evidence discipline & anti-hallucination | 15 | 88 | 13.2 |
| Source-tier rigor | 10 | 85 | 8.5 |
| Structured analytic technique coverage | 10 | 25 | 2.5 |
| Estimative / probability calibration | 5 | 10 | 0.5 |
| Quantitative & financial modelling | 10 | 15 | 1.5 |
| Primary-research workflow (interviews / surveys / Delphi) | 8 | 20 | 1.6 |
| Output craft (Pyramid, action titles, visualisation) | 10 | 35 | 3.5 |
| Academic-reporting standards (PRISMA / CONSORT / GRADE / TOP) | 7 | 30 | 2.1 |
| Investigative tradecraft (OSINT execution, chain-of-custody) | 7 | 70 | 4.9 |
| Due-diligence operational tooling (sanctions / UBO / registries) | 6 | 55 | 3.3 |
| Knowledge management & reuse | 5 | 25 | 1.25 |
| Multi-language / regional coverage | 4 | 30 | 1.2 |
| Tooling completeness (the Python layer) | 8 | 60 | 4.8 |
| **Total** | **100** | — | **62 / 100** |

Detailed scoring rationale → `06-scorecard.md`.

---

## What's already world-class

- **Evidence-discipline clause** — the verbatim hard-constraint enforced in every sub-agent brief outperforms what most analyst houses (Gartner, IDC) publish about their own methodology.
- **5-tier credibility ladder + Burke pentad + Tudor 12-point + Silverman/Bellingcat** — a stack matching Bellingcat's published OSINT toolkit and exceeding the NATO Admiralty Code's 6×6 in granularity for media/journalism.
- **Wave orchestration** — the 4-wave model (broad → gap-fill → verify → synthesis) matches Forrester Wave's 18-week analyst process in shape, with explicit verification embedded.
- **EVIDENCE-AUDIT.md per project** — comparable to OCCRP's per-fact verification log and beyond what most consulting firms produce.
- **Source-mining discipline** — the example project (East Africa housing) cites 250+ sources tier-rated; few consulting white papers do this.

## What's missing to compete with the named comparators

Six structural absences (each is an addressable skill or framework, not a re-architecture):

1. **No structured analytic techniques (SATs) skill.** Heuer & Pherson's catalog (ACH, KAC, Pre-Mortem, Red Team, Devil's Advocacy, Indicators, What-If, High-Impact/Low-Probability) is the working-grammar of every Western intelligence service and now of corporate-intelligence firms. The engine has none of these as named skills.
2. **No estimative-language skill.** Every load-bearing forward claim should carry a Sherman Kent / ODNI probability term ("almost certainly", "likely", etc.) tied to an explicit numeric range. The engine confidence labels are high/medium/low only — useful but not calibrated.
3. **No quantitative-modelling skill.** McKinsey, Bain, and BCG live in financial models, market sizing, sensitivity analyses. The engine has data-quality scoring (Walker 4-axis) but no skill or tool for building, stressing, or presenting a model.
4. **No communication-craft skill.** Pyramid Principle, MECE, "answer-first", action titles, Zelazny chart selection — these are the *output grammar* of the firms named. The engine has report scaffolding but no skill that enforces an executive-summary discipline equal to a McKinsey ghost deck.
5. **No academic-reporting-standards skill.** A doctoral thesis or systematic review needs PRISMA 2020 (27-item checklist), CONSORT 2025 (30-item RCT checklist), STROBE (observational), MOOSE (meta-analysis), GRADE (evidence quality), Cochrane Handbook, TOP Guidelines. The `academic-writing` skill handles citation; it does not handle reporting standards.
6. **No primary-research workflow.** Interview protocol design, structured panels, Delphi, survey construction, qualitative coding. Bain/McKinsey + ICIJ + every PhD thesis depends on this. The engine is currently a secondary-research engine.

## Six things to do next (priority order)

Detailed in `04-recommendations.md`:

1. Build `analytic-tradecraft` skill (Heuer/Pherson SATs + ICD 203 + estimative probability) — **2 weeks, single biggest lever**
2. Build `executive-communication` skill (MECE + Pyramid + action titles + Zelazny) — **2 weeks**
3. Build `academic-reporting-standards` skill (PRISMA/CONSORT/STROBE/MOOSE/GRADE/TOP) — **1 week**
4. Build `quantitative-modelling` skill + `tools/quant/` (market sizing triangulation, sensitivity, scenario cube) — **3 weeks**
5. Build `primary-research` skill (interview protocols, Delphi, qualitative coding) — **2 weeks**
6. Build `knowledge-base` reuse layer — sanitised artefacts library + retrieval — **2 weeks**

After this, run a controlled bake-off: produce a 30-page report on the same brief through the engine and through a manual McKinsey-style process. Score against ICD 203 standards and Pyramid Principle.

## Comparator positioning

| Comparator | Engine vs. comparator today | After 6 priority builds |
|---|---|---|
| **OCCRP / ICIJ** (investigative journalism) | At parity on verification; **behind** on collaborative workflow + legal review | At parity overall |
| **Bellingcat** (OSINT) | At parity on framework; **behind** on tool execution (verification tools mostly stubs) | Ahead on framework; at parity on execution |
| **Big 4 thought-leadership** (Deloitte, PwC, EY, KPMG) | **Ahead** on methodology transparency; behind on sample size / network access | Clearly ahead |
| **Gartner / Forrester / IDC** (analyst houses) | Behind on cadence + customer-base evidence; **ahead** on transparency | At parity for single-cycle research; still behind on living-document infrastructure |
| **McKinsey / Bain / BCG** | Far behind on quant + comm craft + reusable knowledge | Within sight on strategy work; still behind on quant modelling + brand |
| **U.S. IC analytic tradecraft** (ICD 203) | Partially aligned (sourcing, alternatives weakly); **behind** on calibrated probability + change-tracking + dissents | Substantially compliant |
| **Mossad / Unit 8200** | Not benchmarkable — tradecraft classified | Not benchmarkable |
| **PI industry** (ASIS, CII, WAD, FATF EDD) | At parity on framework; behind on operational tooling (sanctions feeds, UBO tracing) | Above industry standard |

## Document map

- `01-methodology.md` — how this evaluation was produced (the engine reviewed itself; what we did, what we caveat)
- `02-benchmark-standards.md` — synthesised standards from the four research waves
- `03-engine-current-state.md` — inventory of skills, tools, projects, gaps within the existing layer
- `04-recommendations.md` — skills to add, skills to enhance, tools to build, frameworks to adopt (with effort estimates)
- `05-implementation-roadmap.md` — sequenced 6-month plan
- `06-scorecard.md` — the 13-dimension scorecard with rubric and rationale per dimension
- `99-sources.md` — every source consulted across the four research waves, tier-rated
- `research-inputs/` — the four raw research-wave reports preserved for traceability

## Confidence

- **Score and gap diagnosis: high confidence.** Four independent agents converged on the same six structural absences.
- **Recommendation effort estimates: medium confidence.** Based on existing skill-build velocity in this repo; not yet calibrated against external benchmarks.
- **Comparator positioning: medium confidence.** OCCRP / Bellingcat / IC tradecraft positioning is well-evidenced. McKinsey / Bain positioning relies on insider-account books (Rasiel, Minto) and former-employee writing — Tier 1 but partial.
