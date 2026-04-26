# Reference — EQUATOR Decision Tree

**Canonical source:** EQUATOR Network — Enhancing the QUAlity and Transparency Of health Research. https://www.equator-network.org/. Tier 1.

The EQUATOR Network hosts 250+ published reporting guidelines and is the definitive routing layer for "which reporting standard does my study type need?". This reference encodes the most consequential routings; for less-common study types, route via https://www.equator-network.org/reporting-guidelines/.

## The decision tree

```
What is the study type?
├── Systematic review of intervention studies          → PRISMA 2020 + Cochrane Handbook + GRADE
├── Network meta-analysis                              → PRISMA-NMA extension
├── Scoping review                                     → PRISMA-ScR extension
├── Randomised controlled trial                        → CONSORT 2025 + GRADE
├── Cluster RCT                                        → CONSORT cluster extension
├── Pilot / feasibility trial                          → CONSORT extension for pilot trials
├── Observational study (cohort / case-control / cross-sectional) → STROBE + GRADE
├── Meta-analysis of observational studies             → MOOSE + GRADE
├── Diagnostic accuracy study                          → STARD
├── Prediction model development / validation          → TRIPOD
├── Qualitative study                                  → COREQ or SRQR; Cochrane qualitative-synthesis chapter
├── Case report                                        → CARE
├── Animal research                                    → ARRIVE
├── Quality improvement study                          → SQUIRE
├── Economic evaluation                                → CHEERS
└── Mixed-methods                                      → GRAMMS + applicable component standards
```

For any study type — submit the matching checklist with the manuscript. Top-tier journals (Lancet, BMJ, JAMA, NEJM, Nature, Science) require the relevant checklist; rejection on first pass is common when it is missing.

## PRISMA 2020 — Systematic Reviews

**Source:** https://www.equator-network.org/reporting-guidelines/prisma/. Page, McKenzie, Bossuyt et al., *BMJ* 2021.

**Components:**
- 27-item checklist (sections: title, abstract, introduction, methods, results, discussion, other information)
- Abstract checklist (12 items)
- Flow diagram (revised; supports original and updated reviews)

**Implementation tools:** PRISMA Shiny App; GoodReports online platform.

**Engine workflow.** Before writing the systematic review:
1. Pre-register the protocol (PROSPERO or OSF).
2. Document the search strategy (databases, dates, terms, filters) per PRISMA-S extension.
3. Run the search; capture results.
4. Screen titles + abstracts; resolve conflicts.
5. Full-text screen; record exclusions with reasons (flow diagram).
6. Extract data; assess risk of bias (RoB 2 or ROBINS-I per Cochrane Handbook).
7. Synthesise (meta-analytic if appropriate; narrative otherwise).
8. Apply GRADE for evidence-quality rating.
9. Complete the 27-item PRISMA checklist; submit with manuscript.

## CONSORT 2025 — Randomised Controlled Trials

**Source:** https://www.equator-network.org/reporting-guidelines/consort/. Endorsed by 600+ journals including Lancet, BMJ, JAMA, NEJM, WAME, ICMJE.

**Components:**
- 30-item checklist
- Flow diagram documenting participant progress through enrolment, allocation, follow-up, and analysis

**Coverage:** Trial design, conduct, analysis, interpretation. Substantial revision in 2025 from the 2010 version for methodological advancements.

**Engine workflow.** Pre-register the trial (clinicaltrials.gov, ISRCTN, or comparable). Follow CONSORT throughout; the 30-item checklist is not a post-hoc fit but a structural guide for the whole manuscript.

## STROBE — Observational Studies

**Source:** https://www.equator-network.org/reporting-guidelines/strobe/.

**Coverage:** Cohort studies, case-control studies, cross-sectional studies. Conference-abstract version available. Inspired by CONSORT, adapted for observational designs.

## MOOSE — Meta-Analysis of Observational Studies

**Source:** https://www.equator-network.org/reporting-guidelines/moose/.

**Components:** 35-item checklist for standardised reporting. Greater emphasis vs. PRISMA on unpublished / non-English studies and on quality assessment (observational studies are more bias-prone than RCTs).

## GRADE — Evidence Quality Rating

**Source:** GRADE Working Group, https://www.gradeworkinggroup.org/. Handbook: https://gradepro.org/handbook/.

**Quality categories** (applied to the body of evidence, not individual studies):

| Level | Meaning |
|---|---|
| High | Further research is very unlikely to change confidence in the estimate of effect. |
| Moderate | Further research is likely to have an important impact on confidence and may change the estimate. |
| Low | Further research is very likely to have an important impact and is likely to change the estimate. |
| Very low | Any estimate of effect is very uncertain. |

**Starting points:**
- Randomised trials: high-quality evidence.
- Observational studies: low-quality evidence.

**Five downgrade factors:** risk of bias, inconsistency, indirectness, imprecision, publication bias.

**Three upgrade factors:** large effect size, dose-response gradient, all plausible confounders would reduce the observed effect.

**Engine workflow.** Apply GRADE to every key outcome of a systematic review. Build a Summary of Findings table. The GRADE rating travels with the claim into any executive summary that derives from the review.

## Cochrane Handbook — Systematic Review Gold Standard

**Source:** https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current. Most cited synthesis methodology resource.

**Coverage:**
- Review planning, question construction, study grouping
- Meta-analysis and network meta-analysis
- Risk of bias assessment (RoB 2 for randomised trials; ROBINS-I for non-randomised intervention studies)
- Reporting bias framework
- Evidence identification and technical advances (text mining, machine learning)
- Qualitative evidence synthesis (Cochrane-Campbell Handbook)

The Cochrane Handbook is the operating manual for systematic reviews; PRISMA is the reporting checklist for them. Both are required.

## TOP Guidelines — Transparency and Openness Promotion

**Source:** Center for Open Science, https://www.cos.io/initiatives/top-guidelines.

**Eight modular standards × three implementation levels:**

1. Citation standards (cite data, code, materials)
2. Data transparency
3. Analytic methods (code) transparency
4. Research materials transparency
5. Design and analysis transparency
6. Study pre-registration
7. Analysis plan pre-registration
8. Replication

**Levels:** Level 1 (authors disclose use/non-use of open practice); Level 2 (authors required to use); Level 3 (journal verifies).

**Engine workflow.** Aim for Level 2 on data, code, materials, and pre-registration in every artefact intended for a top-tier venue. Document each standard's implementation in the methods section.

## Citation style routing

Confirm the institution's or journal's preferred style; default by discipline:

| Style | Discipline |
|---|---|
| Bluebook | US legal scholarship |
| OSCOLA | Oxford / UK legal scholarship |
| Chicago / Turabian | Humanities (history, literature, philosophy in some sub-fields) |
| APA (7th ed.) | Social sciences, education, psychology |
| AMA (11th ed.) | Medicine (American venues) |
| Vancouver | Medicine (international biomedical journals; ICMJE-recommended) |
| MLA (9th ed.) | Literature, languages, modern philology |
| Harvard | Sciences (UK and Commonwealth) |
| IEEE | Engineering, computer science |
| ACS | Chemistry |

The `academic-writing` skill handles the mechanics of each style; this skill confirms which to apply.

## Sources

- EQUATOR Network. https://www.equator-network.org/. Tier 1.
- PRISMA 2020 — Page MJ et al. *BMJ* 2021;372:n71. Tier 1.
- CONSORT 2025 — https://www.consort-spirit.org/. Tier 1.
- STROBE — https://www.strobe-statement.org/. Tier 1.
- MOOSE — Stroup DF et al. *JAMA* 2000;283:2008-2012. Tier 1.
- GRADE Working Group. https://www.gradeworkinggroup.org/. Tier 1.
- Cochrane Handbook. https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current. Tier 1.
- TOP Guidelines (Center for Open Science). https://www.cos.io/initiatives/top-guidelines. Tier 1.
- ICMJE Recommendations. https://www.icmje.org/recommendations/. Tier 1.
