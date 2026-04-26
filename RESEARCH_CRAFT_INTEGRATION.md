# Research-Craft Integration

How twenty-one canonical books on research, search, knowledge management, scraping, verification, intelligence analysis, output craft, and academic discipline informed the engine's skill set.

## Pass 1 — research methodology (compiled 2026-04-25)

| # | Book | Author | Year | What it brings |
|---|---|---|---|---|
| 1 | *Internet Research with Google* | Amanda Deason | recent | Operator-grammar field manual; deepest layer 0 |
| 2 | *Essentials of Knowledge Management* | Bryan Bergeron | 2003 | KM frameworks, intellectual-capital valuation, monetisation |
| 3 | *Librarian's Guide to Online Searching* (4th) | Suzanne S. Bell | 2015 | Searcher's Toolkit, vendor-syntax matrix, discipline-router |
| 4 | *Digital Paper* | Andrew Abbott | 2014 | Project design, minianalysis, brachiation, reading-mode router |
| 5 | *The Handbook of Online and Social Media Research* | Ray Poynter | 2010 | MROC design, panel quality, listening pipeline, MR ethics |
| 6 | *The Creative Guide to Research* | Robin Rowland | 2000 | Investigative-journalism craft, FOIA, chronology-as-gap-detector |

## Pass 2 — scraping and verification (2026-04)

| # | Book | Author | Year | What it brings |
|---|---|---|---|---|
| 7 | *Harnessing the Power of Google* | Christopher C. Brown | 2017 | Programmatic CSE / SerpAPI; stakeholder enumeration |
| 8 | *Verification Handbook for Investigative Reporting* | Craig Silverman et al. | 2015 | Media-forensics workflow (EXIF, reverse-image, geolocation, archive) |
| 9 | *Web Scraping with Python* | Richard Lawson | 2015 | Concurrent download, caching, form interaction, Playwright |
| 10 | *The Ultimate Guide to Web Scraping* | Hartley Brody | 2017 | Decision tree, parser choice, error taxonomy |
| 11 | *Hands-On Website Scraping with Python* | — | recent | Recipes; structured-data shortcuts |
| 12 | *Python Web Scraping for Developers* | Oxylabs | 2024 | Distributed crawling, CAPTCHA discipline |

## Pass 3 — analytic tradecraft, output craft, academic discipline, search mastery (2026-04-26)

| # | Book | Author | Year | What it brings | Skill / reference |
|---|---|---|---|---|---|
| 13 | *Analyzing Intelligence: Origins, Obstacles, and Innovations* | Roger Z. George & James B. Bruce (eds.) | 2008 | ICD 203 lineage; Heuer/Pherson SATs; Sherman Kent estimative practice; cognitive-bias catalog; sourcing & deception (Curveball case); IC quality control | NEW skill `analytic-tradecraft` (5 references) |
| 14 | *The Minto Pyramid Principle* | Barbara Minto | 1985 / 1996 | MECE decomposition; governing thought; SCQA opener; skim-path discipline | NEW skill `executive-communication` — `references/pyramid-principle.md` + `scqa-opener.md` |
| 15 | *Say It With Charts* (4e) | Gene Zelazny | 2001 | Five chart families; one-message-per-slide; ink-to-data discipline | NEW skill `executive-communication` — `references/zelazny-chart-selection.md` |
| 16 | *How to Find Out Anything* | Don MacLeod | 2012 | Google operator catalog; deep-web heuristics; FOIA / PACER / EDGAR / public-records aggregator workflow; people-finding with legal sensitivities (DPPA, FCRA, GLBA, HIPAA) | `research-techniques/references/macleod-search-mastery.md` + `osint-investigation/references/macleod-investigative-search.md` |
| 17 | *The Joy of Search* | Daniel M. Russell | 2019 | Search literacy; metacognition; clarify-the-question discipline; lateral reading; triangulation standards; leading-question lint; `tools/google/` design recommendations | `research-techniques/references/russell-search-literacy.md` |
| 18 | *Writing Your Doctoral Dissertation: Invisible Rules for Success* | Rita S. Brause | 1999 | Dissertation as apprenticeship; chair-as-quasi-parental; chapter-by-chapter template; original-contribution claim; methodology-justification chain; Brause's five tests for findings; viva preparation. Foundation of the **Ivy / Oxbridge / LSE bar**. | NEW skill `academic-reporting-standards` — `references/brause-dissertation-craft.md` + `originality-claim.md` + `methodology-justification-checklist.md` + `findings-interpretation-criteria.md` + `viva-defense-preparation.md` |
| 19 | *The Academic Phrasebank* (4e) | John Morley | 2017 | Rhetorical-move catalog (introducing work / referring to literature / methods / results / discussion / conclusions); reporting-verb register (neutral / tentative / strong / critical); hedging device catalog; Davis & Morley reuse-acceptability rule | `academic-writing/references/morley-rhetorical-moves.md` + `morley-reporting-verbs-and-hedges.md` |
| 20 | *Doing Case Study Research: A Practical Guide* | Hancock & Algozzine | 2006 | Case-study definition; intrinsic / instrumental / collective × exploratory / explanatory / descriptive typologies; purposeful sampling; gatekeeper protocol; interview protocol; Berg's content-analysis stage model; member checking; Stake-derived narrative checklist | `research-design/references/case-study-method.md` + `case-selection-and-analysis.md` |
| 21 | *No More Secrets: Open Source Information and the Reshaping of U.S. Intelligence* | Hamilton Bean | 2011 | OSINT institutional lineage (FBIS → OSC); four competing definitions; speed-vs-verification / volume-vs-signal / over-classification tensions; SARS and Aspin-Brown Burundi positive cases; over-classification and "Googlification" anti-patterns | `osint-investigation/references/osint-doctrine-and-history.md` + `osint-validation-and-anti-patterns.md` |

## Pass 3 — formal-reporting standards (not books, but encoded into `academic-reporting-standards`)

EQUATOR Network routing tree: PRISMA 2020 (systematic reviews); CONSORT 2025 (RCTs); STROBE (observational); MOOSE (meta-analysis of observational); GRADE (evidence-quality rating); Cochrane Handbook (systematic-review gold standard); TOP Guidelines (transparency); style-guide router (Bluebook / OSCOLA / Chicago / APA / AMA / Vancouver / MLA / Harvard / IEEE / ACS). Reference: `academic-reporting-standards/references/equator-decision-tree.md`.

## Pass 1 — high-convergence findings (recommended by 2+ books)

These are the highest-leverage additions because multiple authoritative sources independently identified them as load-bearing:

| Pattern | Books citing | Skill |
|---|---|---|
| Citation chasing / brachiation | Abbott + Bell + Rowland | **citation-brachiation** |
| Reference / clarification interview | Bell + Rowland | **reference-interview** |
| Reading-mode router | Abbott (explicit 5-mode) + Bell | **reading-mode-router** |
| Source-provenance scrutiny | Abbott (5-term Burke) + Rowland (document interviewing) + Bell (coverage axes) | **five-term-source-doubt** + **tudor-twelve-point-evaluation** |
| Controlled vocabulary as personal theory | Bergeron + Bell (MeSH) + Abbott | **controlled-vocabulary-builder** |
| Pearl growing / iterative search | Bell (named) + Deason (operator iteration) + Rowland (prepared browsing) | **pearl-growing-iteration** |
| Project design document as governing contract | Abbott + Rowland (premise) + Bergeron (knowledge audit) | **research-design-document** |
| Crosswalk / matrix as bridge | Abbott (crosswalk) + Rowland (chronology) + Bergeron (knowledge mapping) | **crosswalk-matrix** |
| Minianalysis as atomic unit | Abbott (named) + Bell (refine-panel snapshot) + Rowland (chronology pieces) | **minianalysis-engine** |
| Vendor / engine syntax adaptation | Bell (matrix) + Deason (operator grammar) | **web-search-operator-grammar** + **discipline-router** |
| Stop discipline / defamiliarisation | Abbott + Rowland (Tuchman) | **defamiliarisation-pause** (folded into research-design-document) |
| Listening pipeline (find / extract / analyse) | Poynter (3-stage) + complements social-source-extraction | **listening-pipeline** (enhances social-source-extraction) |
| Ethics for online research | Poynter (ESOMAR) + Rowland (FOIA) | folded into **mr-ethics-and-consent** + existing evidence-discipline |
| Knowledge valuation / monetisation | Bergeron + Poynter (ROI / MROC pricing) | **knowledge-audit-engagement** + **research-monetisation-playbook** |

## Per-book unique contributions (single-book-novel)

### From Deason — *Internet Research with Google*
- Web-search operator stack (Boolean × field × proximity × refinement)
- URL anatomy as credibility heuristic
- Deep-web failure taxonomy (7 categories of why a search returns nothing)
- Grey-literature recipes (`site:.edu filetype:pdf`)
- Cache + recovery fallbacks (`cache:`, archive.org)
- Answer-card-first routing (calc/conv/def served without page fetch)

### From Bergeron — *Essentials of Knowledge Management*
- Eight-stage knowledge lifecycle (Creation → Disposal × 6 issue-axes)
- DIKW-Plus ladder (Data → Information → **Metadata** → Knowledge → Instrumental Understanding)
- Three-tier knowledge model (tacit / **implicit** / explicit) — implicit is highest-ROI capture
- Intellectual capital decomposition (human / structural / customer)
- Magic ↔ Technology continuum (19-attribute matrix for automate-vs-leave-to-human)
- Process–practice gap detection
- Balanced scorecard for intangible outcomes
- Time-value-of-knowledge decay
- Risk hexagon (Mgmt / Politics / Finance / Law / Tech / Marketing)
- Five-phase implementation roadmap with Modify/Extend/Maintain/Disable exits

### From Bell — *Librarian's Guide*
- Searcher's Toolkit — 7 universal database primitives
- Recall vs precision as explicit tuning dial
- "Question behind the question" — 6 types of misstated query
- Citation chasing forward + backward as named primitive
- Bibliographic coupling — relevance via shared references, not shared words
- Single-Citation-Matcher pattern for fragment recovery
- Refine-panel snapshot — aggregate facets before reading individual hits
- Six coverage axes for source evaluation
- Discipline-specific strategy (sciences vs medicine vs social sciences vs humanities vs numerical)
- Anti-pattern: NOT in commercial DBs, broaden-don't-narrow on sparse, black-box-corpora flagging

### From Abbott — *Digital Paper*
- Research as project management, not finding
- Massive-parallel non-linear pipeline (7 concurrent activities)
- Three-phase project lifecycle gated by artefacts
- Empirical-puzzle vs theoretical-puzzle distinction (`why is X true?` vs competing accounts)
- Establishment minianalysis as gate-keeping pre-flight check
- Brachiation through citation graph (back-and-forth, expert-anchored, vintage-aware)
- Five reading modes (narrative / meditative / scan / mastery / partial-mastery)
- Five-term doubt framework (author / provenance / production / mechanics / aims)
- Provenance-anchored 2–10 line atomic notes
- Six-item rule for filing (cardinality discipline)
- Six rhetorical structures (chronology / emblem / narrative / case / comparison / stages)
- Anti-pattern: tag-everything-with-everything = "refusing to think"

### From Poynter — *Online and Social Media Research*
- MROC (Market Research Online Communities) design — short-term and long-term taxonomy
- Online qualitative: bulletin-board groups, online focus groups, parallel IDIs, MEGs
- Netnography / e-ethnography (Kozinets) — observational / interactive / WE-research
- Panel quality (ESOMAR-26, ISO-26362, ARF Foundations of Quality)
- River sampling and access-panel decision matrix
- Listening pipeline (find → extract → analyse) for social-media listening
- Sentiment / share-of-voice / authority ranking
- Prediction markets as concept-test alternative
- Mixed-purpose research (Category 6) protocol
- International research localisation (internet-penetration-aware sampling)
- B2B research patterns (LinkedIn, client DB, recognition-problem mitigation)
- MR ethics: lurk-vs-announce, paraphrase-not-quote, sensitive-data classes, opt-in
- Four MR-specific report shapes (static / interactive / dynamic / process)
- Cost ladder: F2F = 100, telephone = 60, online = 36

### From Rowland — *The Creative Guide to Research*
- Pure-research vs applied-research two-phase model
- 5W+ in 4 layers (traditional + narrative + personal + applied + Wish List)
- Rashomon multi-perspective pass (≥3 conflicting accounts)
- Tudor's 12-point evaluation rubric
- "Interviewing the document" — 5W applied to static text
- McGraw's three-round interview (official line / POV / accountability)
- Spin detection + ratcheting (bridging / punting; off-record → on-record)
- Cashore source-database (mandatory story-field, ~25 new sources + 25 to-dos per document)
- Reverse-genealogy / endpoint pivot when forward search fails
- Stack-serendipity / prepared-browsing budget for off-axis exploration
- FOIA / FOI request engineering (narrow scope / broad form, briefing notes, exemption appeals)
- Chronology-as-gap-detector (Cashore: "the heart of investigative journalism")
- Untouched-corpus prioritizer (No-Gun-Ri lesson — un-indexed primary > re-crawled indexed)
- Stop discipline (Tuchman: "one must stop before one has finished")
- Training-Officer relationship — persistent practitioner mentor per domain

## The 15 highest-leverage new skills scaffolded in this pass

Tier-ordered by leverage (multi-book convergence + structural importance):

### Layer 0 — Search & retrieval craft (5)
1. **web-search-operator-grammar** (Deason) — operator stack lowest layer
2. **pearl-growing-iteration** (Bell + Deason + Rowland) — broad → harvest → refine
3. **citation-brachiation** (Abbott + Bell + Rowland) — bidirectional citation traversal
4. **discipline-router** (Bell) — strategy by sciences/medicine/social/humanities/numerical
5. **reading-mode-router** (Abbott) — narrative / meditative / scan / mastery / partial-mastery

### Layer 1 — Project design & discipline (4)
6. **research-design-document** (Abbott + Rowland + Bergeron) — north-star artefact
7. **minianalysis-engine** (Abbott) — bounded ≤1-week atomic units
8. **crosswalk-matrix** (Abbott + Rowland + Bergeron) — question × source bridge
9. **controlled-vocabulary-builder** (Bergeron + Bell + Abbott) — personal evolving ontology

### Layer 2 — Source engagement (3)
10. **reference-interview** (Bell + Rowland) — intent elicitation upstream
11. **five-term-source-doubt** (Abbott) — Burke pentad on every primary doc
12. **tudor-twelve-point-evaluation** (Rowland) — extends source-verification with 12 criteria

### Layer 3 — Investigation (1)
13. **chronology-construction** (Rowland + Abbott) — gap-detection by timeline

### Layer 4 — Knowledge management (1)
14. **knowledge-lifecycle-pipeline** (Bergeron) — 8-stage research-artifact state machine

### Layer 5 — Market research (1)
15. **mroc-design-and-management** (Poynter) — most novel MR craft, beyond scraping

## Roadmap — additional ~15 skills for next pass

To be scaffolded in a future iteration when these 15 are battle-tested:

- url-provenance-heuristic (Deason)
- deep-web-failure-taxonomy (Deason)
- vendor-syntax-adapter (Bell)
- bibliographic-coupling (Bell)
- citation-disambiguation (Bell)
- single-citation-matcher (Bell)
- recall-precision-tuner (Bell)
- false-drop-suppression (Bell)
- refine-panel-snapshot (Bell)
- knowledge-audit-engagement (Bergeron)
- dikw-plus-ladder (Bergeron)
- tacit-implicit-explicit-capture (Bergeron)
- balanced-scorecard-for-research (Bergeron)
- knowledge-decay-shelf-life (Bergeron)
- risk-hexagon-checklist (Bergeron)
- community-of-practice-orchestration (Bergeron)
- after-action-review-and-exit-knowledge-capture (Bergeron)
- librarian-role-and-archive-maintenance (Bergeron)
- empirical-vs-theoretical-puzzle (Abbott)
- establishment-minianalysis-gate (Abbott)
- provenance-anchored-notes (Abbott)
- six-item-filing-rule (Abbott)
- rhetorical-structure-selector (Abbott)
- writing-in-bits (Abbott)
- defamiliarisation-pause (Abbott)
- idea-notebook (Abbott)
- divergent-evidence-detector (Abbott)
- foia-request-engineering (Rowland)
- rashomon-multiperspective (Rowland)
- mcgraw-three-round-interview (Rowland)
- spin-detection-and-ratcheting (Rowland)
- source-database-cashore (Rowland)
- reverse-genealogy-pivot (Rowland)
- stack-serendipity (Rowland)
- training-officer-relationship (Rowland)
- untouched-corpus-prioritizer (Rowland)
- document-cross-reference-mining (Rowland)
- online-qualitative-methods (Poynter)
- netnography-ethnography (Poynter)
- panel-quality-assessment (Poynter)
- listening-pipeline (Poynter — enhances social-source-extraction)
- river-sampling-and-recruitment (Poynter)
- mr-ethics-and-consent (Poynter)
- mixed-purpose-research-rules (Poynter)
- international-research-localisation (Poynter)
- mr-reporting-deliverables (Poynter)
- prediction-markets (Poynter)
- mobile-and-in-the-moment (Poynter)
- professional-respondent-fraud-detection (Poynter)
- co-creation-collaborative-polls (Poynter)
- research-monetisation-playbook (composite)

## Updates to existing skills (this pass)

- **research-orchestration** — adopt three-phase Preliminary→Midphase→Endphase lifecycle (Abbott); load reading-mode-router and discipline-router upfront
- **source-verification** — 5-tier ladder now augmented by Bell's six coverage axes + Tudor's 12-point check + Burke's 5-term doubt; black-box-corpus flagging mandatory
- **quote-extraction** — adopt Abbott's 2–10 line atomic-note discipline + Poynter's paraphrase-not-quote rule for online posts
- **academic-source-mining** — explicit citation-brachiation step + bibliographic coupling
- **social-source-extraction** — adopt Poynter's find→extract→analyse pipeline; add lurk-vs-announce ethics rule
- **research-report-builder** — adopt Abbott's six rhetorical structures as a chooser before assembly; add Poynter's four MR-specific report shapes
- **gap-analysis** — chronology-construction is now the primary gap-detection mechanism for time-bounded projects
- **research-orchestration** — research-design-document is now the canonical project artefact every wave reads + updates

## How to use this integration

When starting any new project:

1. Load `research-type-router` to pick type + schema
2. Load `research-design-document` to author the north-star artefact
3. Load `discipline-router` to pick search strategy template
4. Load type-appropriate methodology skill (DD / OSINT / market / academic / etc.)
5. **Now** dispatch sub-agents with `research-orchestration`
6. Sub-agents use `web-search-operator-grammar` and `pearl-growing-iteration` at the search layer
7. Findings are filed as `minianalysis` units with `provenance-anchored-notes` discipline
8. Synthesis uses `crosswalk-matrix` + `cross-cohort-synthesis` + `chronology-construction`
9. `research-report-builder` assembles by chosen rhetorical structure
10. `evidence-discipline` enforces throughout

The result: a research operating system that works the way world-class researchers actually work, not the way pipelines pretend they work.
