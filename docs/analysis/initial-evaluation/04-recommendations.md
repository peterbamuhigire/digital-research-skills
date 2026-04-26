# 04 — Recommendations

**Date:** 2026-04-26
**Audience:** Engine owner / build team
**Format:** Skills to add (priority-ordered) → skills to enhance → tools to build → frameworks to adopt → operating-model changes.

---

## A. Skills to add (in priority order)

### A1. `analytic-tradecraft` — STRUCTURED ANALYTIC TECHNIQUES
**Effort:** ~2 weeks. **Priority:** highest single lever.
**Why:** Closes the largest gap (no SATs, no estimative probability, partial ICD 203 alignment). Used by every Western intelligence service and increasingly by Kroll / Control Risks / K2.
**Coverage:**
- ICD 203 nine analytic standards as a ship-gate checklist
- Heuer & Pherson SATs: ACH, Key Assumptions Check, Devil's Advocacy, Red Team, Pre-Mortem, Indicators, What-If, High-Impact / Low-Probability — each as a runnable mini-protocol with input → output template
- Sherman Kent / ODNI estimative probability lexicon (with numeric ranges) embedded as a confidence-assignment helper
- NATO Admiralty Code (A–F × 1–6) as an alternative source-grading overlay for OSINT inputs
- Heuer cognitive-bias checklist (confirmation, mirror imaging, denial & deception, anchoring, satisficing) as a self-audit
**References to ship:** `references/icd-203.md`, `references/sats-catalog.md`, `references/estimative-probability.md`, `references/admiralty-code.md`, `references/cognitive-biases.md`
**Sources:** ODNI ICD 203 PDF; Heuer & Pherson "Structured Analytic Techniques" (Pherson Associates whitepapers); CIA "Psychology of Intelligence Analysis"; Sherman Kent "Words of Estimative Probability".

### A2. `executive-communication` — PYRAMID PRINCIPLE + ZELAZNY
**Effort:** ~2 weeks. **Priority:** second.
**Why:** Output craft is the visible layer the client experiences. McKinsey-grade outputs without a Pyramid Principle skill is impossible.
**Coverage:**
- Minto Pyramid Principle: SCQA opener → answer-first key line → 3 supporting points (MECE) → evidence
- "Action title" rule: every slide / section title is a complete sentence stating the takeaway
- Ghost-deck pattern: storyline before slides; titles read in sequence form a complete argument
- Bain "answer-first" deck pattern
- Zelazny chart-selection: 5 chart types (component, item, time-series, frequency, correlation), one chart / one message / one minute
- Executive summary discipline: one page, 5 sentences max, a grandparent-test readability bar
**References to ship:** `references/pyramid-principle.md`, `references/action-titles.md`, `references/zelazny-chart-selection.md`, `references/executive-summary-template.md`
**Sources:** Minto "Pyramid Principle"; Rasiel "The McKinsey Way" / "The McKinsey Mind"; Zelazny "Say It With Charts"; current McKinsey ghost-deck training material.

### A3. `academic-reporting-standards` — IVY / OXBRIDGE / LSE BAR
**Effort:** ~1.5 weeks. **Priority:** third (high because the owner has set this bar explicitly).
**Why:** Makes academic output (theses, dissertations, systematic reviews, journal articles) examinable at top-five-globally institutions. Closes the gap between `academic-writing` (citation discipline) and `reporting standards` (study-type-specific checklists examiners and journals require).
**Coverage:**
- **EQUATOR Network** as the master decision tree: study type → reporting guideline
- **PRISMA 2020** — 27-item checklist + abstract checklist + flow diagram, for systematic reviews
- **CONSORT 2025** — 30-item checklist + flow diagram, for RCTs
- **STROBE** — observational studies (cohort / case-control / cross-sectional)
- **MOOSE** — meta-analysis of observational studies (35-item)
- **GRADE** — 4-level evidence quality + 5 downgrade + 3 upgrade factors
- **Cochrane Handbook** — RoB 2, ROBINS-I, network meta-analysis, qualitative synthesis
- **TOP Guidelines** — 8 transparency standards × 3 levels (data, code, materials, pre-registration, replication, citation)
- **Examination conventions** at named institutions: Cambridge "Special Regulations for the Degree of PhD"; Oxford "Examination Regulations"; LSE "Code of Practice for Research Degrees"; Harvard / Yale / Princeton dissertation guidelines. Encode: word counts, original-contribution-to-knowledge requirement, literature-review depth, methodology justification, viva-defence preparation, examiner-report criteria.
- **Style guide router**: Bluebook (US legal), OSCOLA (Oxford legal), Chicago / Turabian (humanities), APA (social science), AMA / Vancouver (medicine), MLA (literature)
**References to ship:** `references/equator-decision-tree.md`, `references/prisma-2020.md`, `references/consort-2025.md`, `references/strobe.md`, `references/moose.md`, `references/grade.md`, `references/cochrane-handbook-summary.md`, `references/top-guidelines.md`, `references/oxbridge-examination-conventions.md`, `references/style-guide-router.md`
**Wave-2 task:** mine the named institutions' published examination regulations (Cambridge, Oxford, LSE, Harvard, Yale, Princeton) for current word-count and structural requirements before encoding into the skill.

### A4. `quantitative-modelling` — MARKET SIZING + SCENARIO + SENSITIVITY
**Effort:** ~3 weeks (skill + companion `tools/quant/`). **Priority:** fourth.
**Why:** No quant means no real strategy or DD work. McKinsey, Bain, BCG live here.
**Coverage:**
- Bain market-sizing 5-step framework with mandatory triangulation (top-down + bottom-up + expert-validated)
- Sensitivity analysis (vary one variable, plot output)
- Scenario analysis (base / bull / bear with explicit assumption sets)
- McKinsey "uncertainty cube" pattern (large numeric simulation across 6+ variables)
- Confidence-interval discipline: every quant claim ships with a range, not a point
- Financial-model basics: 3-statement model skeleton, DCF, comparable-company analysis, precedent transactions
- Unit-economics + cohort analysis
**Companion tools:** `tools/quant/sizing.py`, `tools/quant/sensitivity.py`, `tools/quant/scenario.py`, `tools/quant/confidence_band.py`
**Sources:** McKinsey Quarterly "Overcoming obstacles to effective scenario planning"; Bain market-sizing methodology pages; Damodaran corporate-finance reference works for valuation models.

### A5. `primary-research` — INTERVIEWS / SURVEYS / DELPHI / QUAL CODING
**Effort:** ~2 weeks. **Priority:** fifth.
**Why:** A research engine that cannot conduct primary research is a literature-review engine. McKinsey / Bain / ICIJ / every PhD requires this layer.
**Coverage:**
- Interview-protocol design: open-ended question construction; laddering; follow-up discipline
- Expert-network-style screening: vetting questions, conflict checks, recording consent, NDA pattern
- Survey construction: question types, ordering bias, response scales, sample-size calculation
- Delphi panel: round-1 broad → round-2 convergence → round-3 confirmation
- Qualitative coding: open coding, axial coding, selective coding (grounded theory); inter-rater reliability
- Verbatim transcription discipline; quote attribution; consent management
**References:** `references/interview-protocol.md`, `references/survey-design.md`, `references/delphi.md`, `references/qualitative-coding.md`, `references/consent-and-ethics.md`
**Sources:** Patton "Qualitative Research & Evaluation Methods"; Krueger & Casey "Focus Groups"; Linstone & Turoff "The Delphi Method"; Strauss & Corbin grounded-theory texts.

### A6. `knowledge-base` — REUSABLE ARTEFACT LAYER
**Effort:** ~2 weeks. **Priority:** sixth.
**Why:** McKinsey's 50,000-document KNOW system is a moat. Every project the engine produces should leave behind a sanitised, searchable artefact for the next.
**Coverage:**
- "Knowledge nugget" template: 1–3 page distillation of a project's reusable findings (frameworks discovered, sources by tier, quotable stats, scaffolding that worked)
- Sanitisation rules: client-identifying material stripped before the artefact lifts to the cross-project library
- Indexing schema: domain × method × source-tier
- Retrieval pattern: cohort agents query the KB before each new wave to avoid duplication
**Companion tools:** `tools/kb/index.py`, `tools/kb/search.py`, `tools/kb/sanitise.py`
**Sources:** APQC knowledge-management guides; McKinsey KNOW system descriptions in Knoco research and Document360 case studies (both Tier 2).

### A7. `peer-review-loop` — WAVE 3.5 EXTERNAL REVIEW
**Effort:** ~1 week. **Priority:** seventh.
**Why:** The engine's own ship-gate calls for verification, but no skill enforces a separate-mind review. ICIJ, Forrester, Gartner, Cochrane, Pulitzer-grade journalism all require this.
**Coverage:**
- External-SME identification + outreach pattern
- Review-brief template (what to challenge, where the analyst is least confident)
- Diff-style change log when judgments revise post-review
- Dissent footnoting (NIE-style) when unanimity isn't reached
**References:** `references/external-review-brief.md`, `references/dissent-footnoting.md`

### A8. Deferred / lower-priority (still strategically useful)

| Skill | Effort | Driver |
|---|---|---|
| `competitive-intelligence` | 2 wk | Patent analysis, technology scanning, pricing forensics — for product-strategy briefs |
| `geospatial-analysis` | 2 wk | Mapping, satellite-imagery exploitation beyond Bellingcat manual technique |
| `data-visualisation` | 2 wk | Tufte principles, infographic patterns, dashboard architecture (separate from Zelazny chart-selection) |
| `multi-language-research` | 3 wk | Swahili, French, Luganda, Kinyarwanda, Arabic operator grammars + source registries |
| `paywalled-database-access` | 1 wk (skill) + integration time | Bloomberg / Capital IQ / LexisNexis / Refinitiv workflow patterns |
| `cost-control` | 1 wk | Token budgets per wave; stop-loss thresholds; research-velocity tracking |

---

## B. Skills to enhance (existing skills with concrete upgrades)

| Skill | Upgrade | Effort |
|---|---|---|
| `source-evaluation` | Add NATO Admiralty Code as parallel grading lane; add per-fact verification log granularity (OCCRP-style, not just per-source) | 3 days |
| `research-orchestration` | Add cost-control + token-budget; add Wave 3.5 (peer review) hook; add living-document refresh cadence concept | 4 days |
| `due-diligence` | Wire to `tools/sanctions/` and `tools/dd/` once those tools are real; encode FATF Recommendations 9/10/12 structure; add tiered Level I/II/III DD report templates | 1 wk |
| `osint-investigation` | Encode Bellingcat geolocation playbook (SunCalc shadow analysis, architectural matching, multispectral satellite); link to `tools/verification/` | 1 wk |
| `pi-investigation` | Encode ASIS / CII / WAD ethical codes as a ship-gate; chain-of-custody connector to `tools/pi/chain_of_custody.py` | 4 days |
| `academic-writing` | Add discipline-specific style routing (Bluebook / OSCOLA / Chicago / APA / AMA / MLA); link to new `academic-reporting-standards` skill | 3 days |
| `report-and-proposal-craft` | Layer Pyramid Principle + action-title discipline (or delegate to `executive-communication`) | 3 days |
| `web-scraping-foundations` + `scraping-engineering-python` | Concrete recipes for: court documents, regulatory filings, news archives, sanctions lists. Distributed crawling + CAPTCHA discipline. | 2 wk |
| `research-design` | Battle-test on a real second project; flesh out MROC, historical methods, trend analysis references | 1 wk + project usage |

---

## C. Tools to build / complete

Priority order:

1. **`tools/verification/`** — implement the EXIF / reverse-image-search fan-out / archive resurrection / provenance-tracing modules. Without these, Silverman methodology in `source-evaluation` is aspirational. **2 wk.**
2. **`tools/sanctions/`** — live OFAC, UN, EU, UK, Canadian watchlist integration with fuzzy-match discipline and false-positive disposition log. **1.5 wk.**
3. **`tools/quant/`** — sizing / sensitivity / scenario / confidence-band utilities to back the new `quantitative-modelling` skill. **2 wk.**
4. **`tools/dd/registry_atlas.py`** — complete jurisdiction registry connectors (East Africa first, then global). API keys, fallback sequences. **2 wk.**
5. **`tools/google/`** — full CSE / SerpAPI integration with rate-limit handling, pagination, fallback logic. **1 wk.**
6. **`tools/kb/`** — knowledge-base index, search, sanitise utilities. **1 wk.**
7. **`tools/scraping/recipes/`** — concrete recipes per source family (courts, regulators, news, social). **rolling, ~2 wk first batch.**
8. **`tools/ci/url_liveness.py`** — automated URL-liveness + archive-snapshot enforcement before any output ships. **3 days.**

---

## D. Frameworks to adopt (cross-cutting)

| Framework | Why | Where it lands |
|---|---|---|
| **ICD 203** as universal ship-gate | Aligns the engine with the most rigorous public analytic standard | Top of every output checklist |
| **Sherman Kent / ODNI estimative lexicon** | Replaces vague "high / medium / low" with calibrated ranges | Confidence labels everywhere |
| **Pyramid Principle** | Output grammar | Every executive-facing artefact |
| **PRISMA 2020 + EQUATOR router** | Academic-output grammar | Every academic artefact |
| **NATO Admiralty Code (A–F × 1–6)** | Two-axis source grading parallel to the 5-tier ladder | OSINT and DD outputs |
| **TOP Guidelines** | Transparency baseline for academic + data work | Engine-wide; Level-2 / Level-3 attainable |
| **GRADE** | Evidence-quality rating that travels with claims | Replaces ad-hoc confidence on quantitative claims |
| **Cost-control discipline** | Token budgets per wave, hard stop-losses | `research-orchestration` |
| **Conflict-of-interest disclosure on engagement** | Standard at every named comparator | Project intake template |
| **Living-document refresh** | Forrester / Gartner cadence model | Project README + scheduler |

---

## E. Operating-model changes (non-skill)

1. **Run a controlled bake-off** after the six priority skills ship. Same brief, two paths: engine output vs. a manual McKinsey-style consultant pass. Score against ICD 203 + Pyramid Principle + PRISMA. Publish findings.
2. **Stand up a second project** outside East Africa housing — ideally a financial-services or healthcare DD — to stress-test `due-diligence`, the new `quantitative-modelling`, and `primary-research` skills under a different domain.
3. **Publish a one-page "Engine standards card"** the consulting practice can show clients: what the engine guarantees on every deliverable (sourcing, calibration, peer review, archive snapshots, conflict-of-interest disclosure). This is a competitive advantage no Big 4 firm publishes.
4. **Recruit one external SME peer reviewer** per major engagement until the `peer-review-loop` skill stabilises. Pay for time. Log feedback in `EVIDENCE-AUDIT.md`.
5. **Build a knowledge-management role** (even part-time) once the `knowledge-base` skill ships. McKinsey runs ~10% of headcount as knowledge professionals. The engine's analogue is automated, but it still needs a human who curates the library.
6. **Adopt a cadence** for engine self-evaluation. Re-run this evaluation each quarter. The score should move; if it doesn't, the rubric is wrong.

---

## F. Order-of-operations (sequenced 6-month build)

Detailed in `05-implementation-roadmap.md`. Headline:

- **Month 1:** A1 `analytic-tradecraft` + A2 `executive-communication` (highest leverage, lowest dependency)
- **Month 2:** A3 `academic-reporting-standards` + complete `tools/verification/`
- **Month 3:** A4 `quantitative-modelling` + `tools/quant/`
- **Month 4:** A5 `primary-research` + `tools/sanctions/` + run second project to stress-test
- **Month 5:** A6 `knowledge-base` + A7 `peer-review-loop`
- **Month 6:** Deferred-tier skills (multi-language, geospatial, viz, competitive-intel) + bake-off

After month 6, re-run this evaluation. Target: ≥ 85 / 100.
