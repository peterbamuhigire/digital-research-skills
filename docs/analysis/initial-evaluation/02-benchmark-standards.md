# 02 — Synthesised Benchmark Standards

**Date:** 2026-04-26
**Source:** Four parallel research waves (preserved verbatim in `research-inputs/`)

This document distils the **must-meet** standards across the four comparator cohorts. Anything appearing in **two or more** cohorts is a baseline a serious research engine has to clear; single-cohort standards are flagged "consider".

---

## Part 1 — Methodological standards (universal across cohorts)

### 1. Source rigor

| Source | Standard | Cohort |
|---|---|---|
| ICD 203 §1 — Appropriate Sourcing | "Properly describe quality, credibility, and sources underpinning analytic judgments." | C |
| OCCRP fact-checking | "Every single fact verified, regardless of size … original documentation required, no reliance on secondary reporting." | D |
| Bellingcat OSINT | "Triangulation of data from diverse sources … methodology fully described in every report." | C, D |
| NATO Admiralty Code | Two-axis grading: source reliability (A–F) × information credibility (1–6). | C |
| AP Statement of News Values | "Accept nothing of value from news sources … real effort to obtain response when portraying someone negatively." | D |
| McKinsey Global Surveys | Methodology disclosure: weighting by GDP, qualified executive panels, response-rate adjustment. | A |

**Engine baseline:** the 5-tier credibility ladder + Burke pentad + Tudor twelve points already in `source-evaluation`. **Gap:** no two-axis grading equivalent to the Admiralty Code; no per-claim verification log at the granularity OCCRP demands.

### 2. Estimative discipline

| Source | Standard | Cohort |
|---|---|---|
| ICD 203 §2 — Level of Uncertainty | "Explicitly explain where uncertainty exists and to what degree analysis depends on assumptions." | C |
| ICD 203 §8 — Accuracy of Probability Judgments | Calibrated against actual outcomes. | C |
| Sherman Kent / ODNI lexicon | "Almost certainly" ≈ ≥95%; "very likely" ≈ 80–90%; "likely" ≈ 60–80%; "probably" ≈ 50–70%; "might" ≈ 20–50%; "unlikely" ≈ 10–20%; "very unlikely" ≤5%. | C |
| GRADE | Four-level evidence-quality rating (high / moderate / low / very low) with five downgrade and three upgrade factors. | D |

**Engine baseline:** confidence labels (high/medium/low) only. **Gap:** no calibrated probability lexicon; no GRADE-style up/downgrade factor logic.

### 3. Structured analytic techniques (SATs)

| Source | Standard | Cohort |
|---|---|---|
| Heuer & Pherson — *Structured Analytic Techniques for Intelligence Analysis* | 50 named techniques; each with when-to-use, value-added, step-by-step method, common pitfalls. | C |
| ICD 203 §4 — Analysis of Alternatives | "Multiple competing hypotheses must be explored before settling on a primary judgment." | C |
| McKinsey Red Team / Blue Team | Independent expert teams to challenge assumptions in "big bet" scenarios. | A |
| Heuer — *Psychology of Intelligence Analysis* | Catalog of cognitive biases (confirmation, mirror imaging, denial & deception). | C |

**Must-cover techniques (engine should expose all of these as named tools):**
ACH (Analysis of Competing Hypotheses), Key Assumptions Check, Devil's Advocacy, Red Team, Pre-Mortem, Indicators, What-If, High-Impact/Low-Probability.

**Engine baseline:** none of these are named skills today. The engine infers alternatives implicitly during synthesis but does not run a structured ACH matrix or a Pre-Mortem.

### 4. Quantitative rigor

| Source | Standard | Cohort |
|---|---|---|
| Bain market-sizing triangulation | Top-down + bottom-up + expert-validated; cross-validated as a 5-step framework. | A |
| McKinsey "uncertainty cube" | Expand from 3-scenario models to large numeric simulations across 6+ critical variables. | A |
| Sensitivity vs. scenario analysis | Sensitivity = vary one variable, measure output; scenario = vary multiple variables jointly (base/bull/bear). | A |
| Forrester Wave | Subscriber-adjustable Excel weighting model so users can re-rank vendors. | B |

**Engine baseline:** `data-quality-pipeline` (Walker 4-axis) covers data; nothing covers modelling. **Gap:** no skill or tool for market sizing, sensitivity, scenario, or simple financial models.

### 5. Communication craft

| Source | Standard | Cohort |
|---|---|---|
| Minto Pyramid Principle | Answer first → 3 supporting points → evidence; MECE decomposition. | A |
| McKinsey ghost deck | Outline structure on grid before opening PowerPoint; action titles must form a complete argument when read in sequence. | A |
| Bain "answer-first" | Lead with hypothesis + the few facts required to validate it. | A |
| Zelazny — *Say It With Charts* | Five chart types (component, item, time-series, frequency, correlation); the chart serves the message, not the data. | A |
| Reuters / AP Handbooks | Quote accuracy, sourcing transparency, correction discipline. | D |

**Engine baseline:** scaffolds a report; no enforced executive-summary discipline; no action-title rule; no chart-selection skill. **Gap:** the engine outputs a research corpus; it does not output a deck or a one-pager that competes with a McKinsey ghost deck.

### 6. Quality control / peer review

| Source | Standard | Cohort |
|---|---|---|
| ICD 203 §6, §7 — Logical Argumentation + Consistency | Reasoning follows logically from evidence; changes from prior judgments are explained. | C |
| Forrester Wave | Research director reviews all scores; consistency-assurance team enforces uniform methodology; vendor 5-day courtesy preview. | B |
| Gartner Magic Quadrant | Internal peer review by worldwide analyst community; management review required before publication. | B |
| McKinsey partner review | Twice-yearly performance reviews with feedback compiled and review committees. | A |
| OCCRP fact-checking team | 2 full-time + 6 part-time fact-checkers; multi-language coverage. | D |
| ICIJ collaborative verification | Cross-border fact-checking via peer journalist review. | D |

**Engine baseline:** evidence-audit log; no separate peer-review wave. **Gap:** no Wave-3.5 external SME review; no consistency-assurance pass; no change-tracking on revised judgments.

---

## Part 2 — Domain-specific standards

### 7. Investigative tradecraft (PI + journalism)

| Source | Standard | Cohort |
|---|---|---|
| FATF Recommendations 9, 10, 12 | Customer Due Diligence + Enhanced Due Diligence; PEP screening; source-of-wealth/funds; ongoing monitoring. | D |
| ASIS International Investigations Standard (ANSI-approved) | Impartiality, independence, fact-based analysis; legally defensible documentation. | D |
| CII (Council of International Investigators) | Six-stage investigative workflow: intake → scoping → physical/documentary evidence → testimonial → digital → analysis & reporting. | D |
| Bellingcat geolocation | Shadow analysis (SunCalc), architectural feature matching, satellite imagery, multispectral analysis, EXIF metadata. | C, D |
| Pulitzer Investigative Reporting | Sourcing rigor, transparency about methods, public-interest impact. | D |

**Engine baseline:** `due-diligence`, `osint-investigation`, `pi-investigation` skills cover the framework. **Gap:** operational tooling — sanctions feeds, UBO tracing, registry APIs — is mostly stub code (`tools/dd/`, `tools/sanctions/`, `tools/verification/`).

### 8. Academic reporting standards (Ivy / Oxbridge / LSE bar)

The owner has set the explicit standard that academic outputs must meet **Ivy-League / Oxford / Cambridge / LSE** quality. That bar comprises three layers:

**Layer 1 — Reporting standards (universal across health, social-science, and quantitative disciplines):**

| Standard | Domain | Items |
|---|---|---|
| **PRISMA 2020** | Systematic reviews | 27-item checklist + abstract checklist + flow diagram |
| **CONSORT 2025** | Randomised controlled trials | 30-item checklist + flow diagram (endorsed by 600+ journals incl. Lancet, BMJ, JAMA, NEJM) |
| **STROBE** | Observational studies (cohort / case-control / cross-sectional) | Checklist by study type |
| **MOOSE** | Meta-analysis of observational studies | 35-item checklist |
| **GRADE** | Evidence quality rating | 4-level + 5 downgrade + 3 upgrade factors |
| **Cochrane Handbook** | Systematic reviews + qualitative synthesis | RoB 2 + ROBINS-I tools; meta-analysis + network meta-analysis |
| **TOP Guidelines** | Transparency & openness | 8 modular standards × 3 implementation levels |
| **EQUATOR Network** | Master repository | 250+ guidelines across all study types |

**Layer 2 — Examination conventions at the named institutions:**

These are documented in each institution's published examination regulations (Cambridge "Special Regulations for the Degree of PhD", Oxford "Examination Regulations", LSE "Code of Practice for Research Degrees", Harvard / Yale / Princeton dissertation guidelines). Common requirements:

- Word-count discipline (typically 80,000 words for a humanities PhD, lower for sciences with paper appendices)
- Original contribution to knowledge stated explicitly in the abstract
- Literature review demonstrating mastery of the field
- Methodology section justifying every choice and acknowledging limits
- Viva voce defence assumes the candidate can defend every line
- Examiner reports filed against published criteria

**Layer 3 — Citation and style:**

- Bluebook (legal, Harvard Law especially)
- OSCOLA (Oxford legal)
- Chicago / Turabian (humanities)
- Author-Date / APA (social sciences)
- AMA / Vancouver (medicine)
- Discipline-specific style guides (e.g., MLA for literature)

**Engine baseline:** `academic-writing` covers citation styles and plagiarism prevention. **Gap:** no skill encodes PRISMA / CONSORT / STROBE / MOOSE / GRADE / Cochrane / TOP / EQUATOR; no skill encodes the named institutions' examination conventions; no skill enforces "original contribution to knowledge" as a structural requirement of the artefact.

### 9. Knowledge management

| Source | Standard | Cohort |
|---|---|---|
| McKinsey KNOW system | 50,000+ sanitised documents, "knowledge nuggets" (1–3 page distillations), ~1,800 dedicated knowledge professionals. | A |
| Bain Capability Network | Expertise-led model; internal websites store and serve prior-case knowledge. | A |
| BCG Henderson Institute | Think-tank publishing arm for cross-engagement insight. | A |
| ICIJ network | 100+ media partners; collaborative document repository. | D |

**Engine baseline:** none. Each project's research lives in its own `projects/<id>/` directory; nothing is sanitised and lifted into a reusable artefact library. **Gap:** no cross-project knowledge layer.

### 10. Reporting cadence and refresh

| Source | Standard | Cohort |
|---|---|---|
| Forrester Wave | 18-week cycle per market; quarterly publication across markets. | B |
| Gartner Magic Quadrant | Annual refresh; 360+ MQs published; faster cadence in fast-moving markets. | B |
| IDC MarketScape | Rolling schedule; some 2-year scope. | B |
| PwC Annual Global CEO Survey | 29 consecutive years; standardised methodology disclosure. | B |

**Engine baseline:** project-by-project. **Gap:** no concept of a "living document" that refreshes against the same brief on a cadence.

---

## Part 3 — Standards a research engine *must* satisfy to claim parity

Convergence across cohorts produces this minimum-bar list:

1. Every claim sourced; every source tier-rated; every load-bearing claim with confidence + verification trail. *(Engine: ✓ already.)*
2. Calibrated probability for forward-looking judgments. *(Engine: ✗.)*
3. Multiple competing hypotheses considered explicitly. *(Engine: ✗ as a named technique.)*
4. Structured analytic techniques (Heuer/Pherson catalog) available as named skills. *(Engine: ✗.)*
5. Triangulated quantitative estimates (top-down + bottom-up + expert) for any market-sizing claim. *(Engine: ✗.)*
6. Sensitivity / scenario analysis on any forward-looking quantitative claim. *(Engine: ✗.)*
7. Pyramid Principle (or equivalent) executive summary on every output. *(Engine: ✗.)*
8. Action-titled, one-message-per-page deck (or equivalent narrative discipline) for executive output. *(Engine: ✗.)*
9. Reporting-standard fluency (PRISMA / CONSORT / etc.) for academic output. *(Engine: ✗.)*
10. Per-fact verification log (OCCRP-grade). *(Engine: ✓ partial — EVIDENCE-AUDIT.md.)*
11. Independent peer review before publication. *(Engine: ✗.)*
12. Change-tracking on revised judgments. *(Engine: ✗.)*
13. URL archive snapshots before publication. *(Engine: ✗ — flagged in own ship-gate but not enforced.)*
14. Reusable knowledge artefact library across projects. *(Engine: ✗.)*
15. Conflict-of-interest disclosure on engagement. *(Engine: ✗.)*

**Score from this list:** 1.5 / 15 fully met, 1 partial → **~10 / 15 = ~17%** of the universal must-meet list. The dimension-weighted score in `00-executive-summary.md` (62 / 100) is more generous because some dimensions (evidence discipline, OSINT framework) sit far above this baseline.
