---
name: academic-reporting-standards
description: Academic-output discipline at Ivy / Oxford / Cambridge / LSE quality. Three layers — practical-craft (Brause's "invisible rules", chapter-by-chapter dissertation template, viva preparation, examiner expectations), institution-specific examination conventions (Cambridge, Oxford, LSE, Harvard, Yale, Princeton), and formal-reporting (PRISMA 2020, CONSORT 2025, STROBE, MOOSE, GRADE, Cochrane Handbook, TOP Guidelines, EQUATOR Network). Use on any thesis, dissertation, journal article, systematic review, or examinable academic artefact. Load only what the artefact demands.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: critical
---

# Academic Reporting Standards

Single entry skill for any academic artefact intended for an examination committee, a peer-reviewed journal, or an institutional review at Ivy-League / Oxbridge / LSE quality. The skill operates **alongside** `academic-writing` (which handles citation styles, plagiarism prevention, and originality), **through** `critical-reasoning-and-argument` (which tests the claim-gap-method-contribution logic), and **above** `report-and-proposal-craft` (which handles long-form scaffolding for non-academic outputs).

This skill has three layers, all load-bearing:

- **Practical craft** — the "invisible rules" Rita Brause articulates: dissertation as apprenticeship, chair-as-quasi-parental relationship, parallel work, pilot everything, recursive process. The unwritten conventions every examination committee assumes the candidate knows. Reference: `references/brause-dissertation-craft.md`.
- **Institutional examination conventions** — current published rules for Cambridge, Oxford, LSE, Harvard, Yale, and Princeton. This layer encodes word-count discipline, thesis-by-papers structures, original-contribution language, viva/defense procedures, examiner criteria, and explicit gaps where no central word-count cap is published. Reference: `references/oxbridge-ivy-examination-conventions.md`.
- **Formal reporting** — the published study-type-specific checklists (PRISMA / CONSORT / STROBE / MOOSE / GRADE / Cochrane / TOP) hosted by the EQUATOR Network. The conventions every top journal and every doctoral committee require. Reference: `references/equator-decision-tree.md`.

A thesis or paper that satisfies only one layer fails. Examiners look for all applicable layers.

## When to use

Use this skill on any of:

- **Doctoral dissertation / thesis** at Ivy / Oxbridge / LSE / equivalent
- **Master's dissertation** at the same standard
- **Journal article** for a peer-reviewed venue (Lancet, BMJ, JAMA, NEJM, Nature, Science, top-tier social-science journals)
- **Systematic review** — any
- **Conference paper** at A* venues
- **Grant proposal / research proposal** for an institutional or funding-body review
- **Book proposal** for an academic publisher

Do **not** use on: executive summaries (use `executive-communication`), business reports (use `report-and-proposal-craft`), blog posts, internal memos.

## The five rules (load first)

1. **Genre-correct structure.** Academic artefacts use neutral topic headings (Introduction, Literature Review, Methodology, Findings, Discussion, Conclusion) — not action titles. Reference: `references/brause-dissertation-craft.md`.
2. **Original contribution declared.** Every doctoral artefact states explicitly, in the abstract and in chapter 1, what is new. The contribution is gap-filling, inconsistency-resolving, conflict-clarifying, theory-testing, or theory-building. Reference: `references/originality-claim.md`.
3. **Methodology justified, not described.** Every methodological choice carries its rationale, tied back to the theory or phenomenon under investigation. Reference: `references/methodology-justification-checklist.md`.
4. **Reporting-standard compliance.** The artefact ships with the appropriate EQUATOR-network checklist completed and submitted. Reference: `references/equator-decision-tree.md`.
5. **Examiner-defensible.** Every paragraph must be defensible at viva. Apprentice-level statements ship without hedge; expert-level statements require evidence; original-contribution statements require the gap-evidence-fit chain. Reference: `references/viva-defense-preparation.md`.
6. **Argument defensible.** Every literature gap, original-contribution claim, methodology choice, interpretation, implication, and recommendation passes `critical-reasoning-and-argument` before the manuscript is treated as examinable.

## Decision router — load the matching reference

| Artefact type | Load |
|---|---|
| **Doctoral dissertation** | `references/brause-dissertation-craft.md` (always) + `references/oxbridge-ivy-examination-conventions.md` for Oxbridge/Ivy/LSE targets or the relevant regional skill (`uganda-academic-research`, `kenya-academic-research`) + `references/methodology-justification-checklist.md` + `references/originality-claim.md` + `references/viva-defense-preparation.md` |
| **Master's research thesis / dissertation** | `references/oxbridge-ivy-examination-conventions.md` for Oxbridge/Ivy/LSE targets or the relevant regional skill (`uganda-academic-research`, `kenya-academic-research`) + `references/methodology-justification-checklist.md` + `references/originality-claim.md` where original research is required |
| **Systematic review** | `references/equator-decision-tree.md` (PRISMA 2020 + Cochrane Handbook) + GRADE for evidence quality |
| **Randomised controlled trial paper** | `references/equator-decision-tree.md` (CONSORT 2025) + GRADE |
| **Observational study paper** | `references/equator-decision-tree.md` (STROBE) + GRADE |
| **Meta-analysis of observational studies** | `references/equator-decision-tree.md` (MOOSE) + GRADE |
| **Mixed-methods or qualitative study** | `references/equator-decision-tree.md` (Cochrane qualitative synthesis) |
| **Research proposal** | `references/brause-dissertation-craft.md` + `references/originality-claim.md` + `references/methodology-justification-checklist.md` |
| **Journal article (any)** | Reporting-standard for the study type + `references/findings-interpretation-criteria.md` |

## The Brause practical-craft layer — one-paragraph summary

Rita S. Brause's *Writing Your Doctoral Dissertation: Invisible Rules for Success* (1999) names the unwritten conventions that determine completion at Ivy / Oxbridge / LSE-equivalent institutions. Faculty see the dissertation as an apprenticeship (proof of capacity for scholarly work), not as a final examination on coursework. The chair-student relationship is quasi-parental and quasi-political; choice of chair predicts completion more than choice of topic. Students self-initiate every interaction; silence is interpreted as progress. Work in parallel — never wait for a chapter to come back. The proposal is a contract once approved, but new administrations can change the rules; finish fast. ABD is a trap. Pilot everything. The process is recursive; linear plans fail. Reference: `references/brause-dissertation-craft.md`.

## The formal-reporting layer — one-paragraph summary

The EQUATOR Network (Enhancing the QUAlity and Transparency Of health Research, https://www.equator-network.org/) hosts the master decision tree of 250+ published reporting guidelines. The engine encodes the most consequential: **PRISMA 2020** (27-item checklist for systematic reviews); **CONSORT 2025** (30-item checklist for randomised controlled trials, endorsed by 600+ journals including Lancet, BMJ, JAMA, NEJM); **STROBE** (cohort, case-control, cross-sectional studies); **MOOSE** (meta-analyses of observational studies, 35-item); **GRADE** (4-level evidence quality with 5 downgrade and 3 upgrade factors); **Cochrane Handbook** (systematic-review gold standard, includes RoB 2 and ROBINS-I tools); **TOP Guidelines** (Transparency and Openness Promotion — 8 modular standards × 3 implementation levels). For style, the engine routes: Bluebook (US legal), OSCOLA (Oxford legal), Chicago / Turabian (humanities), APA (social sciences), AMA / Vancouver (medicine), MLA (literature). Reference: `references/equator-decision-tree.md`.

## The institution-specific layer — one-paragraph summary

The named institutions do not share one universal dissertation word count. Cambridge and Oxford require the exact Degree Committee / Examination Regulation because word limits vary by subject. LSE publishes a school-wide PhD limit of 100,000 words including footnotes and excluding bibliography and appendices. Harvard, Yale, and Princeton central guidance reviewed in the Wave-2 mining pass did not publish a universal PhD dissertation word-count cap; their enforceable requirements are programme/department format, original-contribution standards, committee/reader reports, and defense/FPO procedures. Reference: `references/oxbridge-ivy-examination-conventions.md`.

## Universal output ship-gate

Before any academic artefact ships, every box must be ticked:

- [ ] **Title** is a descriptive title that names variables and population (hypothesis-testing) or research focus (hypothesis-generating). Revised through the project.
- [ ] **Abstract** ≤ 350 words; covers title, problem, theoretical frame, data sources, analytic procedures, outcomes. (DAI standard.)
- [ ] **Chapter 1 / Introduction** establishes that the study is doable, significant, comprehensive, and addresses a pivotal disciplinary issue.
- [ ] **Literature review** is organised topically (not chronologically) where the field permits; identifies the gap / inconsistency / conflict the study addresses; closes with a potential-significance statement.
- [ ] **Methodology** justifies every choice with reference to the theory under investigation. Pilot evidence, sample-size justification, IRB approval, validity, limitations all explicit.
- [ ] **Findings** ship tables/figures first, narrative second, synthesis third. Five tests: thorough, clear, logical, relevant, cautious.
- [ ] **Discussion** acknowledges biases, the bases for them, and other perspectives; avoids polemics.
- [ ] **Conclusion** has four sub-sections: summary, conclusions, implications, recommendations.
- [ ] **Original-contribution claim** is explicit in the abstract and chapter 1; defensible by the gap-evidence-fit chain.
- [ ] **Critical-reasoning gate** passed: argument map, countercase, fallacy audit, and certainty calibration completed for the contribution, method, findings interpretation, and recommendations.
- [ ] **Institution-specific regulation check** completed: exact institution, school/department, degree, format, word-count inclusions/exclusions, and viva/defense rules recorded. If no published central cap exists, the gap is stated rather than filled with a guessed number.
- [ ] **Reporting-standard checklist** for the study type is completed and submitted with the artefact.
- [ ] **Citation style** matches the institution / journal: Bluebook / OSCOLA / Chicago / APA / AMA / Vancouver / MLA.
- [ ] **Plagiarism check** run via `academic-writing` skill.
- [ ] **Viva defensibility** — every paragraph is defensible; biases are acknowledged; alternative perspectives are accommodated.

## Universal anti-patterns

- **Treating the dissertation as a long term paper.** The genre is different. The lit review is not background; the methodology is not a recipe.
- **Choosing the chair by prestige.** Brause's data: completion rate tracks the chair's history of graduating students, not the chair's reputation.
- **Outsourcing statistical or methodological work without owning the logic.** Orals expose memorised verbatim answers within minutes.
- **Equating statistical with substantive significance.** A p < 0.001 finding can be substantively trivial; a non-significant finding can be substantively important.
- **Over-claiming or under-claiming findings.** Both are examiner red flags. Findings are calibrated to the data.
- **Action titles in academic chapters.** The convention is neutral topic headings. Reserve action titles for the executive-summary version of the work (use `executive-communication` for that).
- **Skipping the EQUATOR checklist.** Every top-tier journal requires the relevant reporting-standard checklist. Submitting without it signals amateur.
- **Inventing a universal Ivy/Oxbridge word count.** Cambridge and Oxford vary by subject; Harvard/Yale/Princeton central guidance does not supply a universal cap in the mined sources. Use the exact department/programme rule or state the gap.
- **Polemics in the discussion.** Brause Ch 14: "acknowledge biases and the bases for these, while recognising the possibility of other perspectives. Avoid polemics."

## Companion skills

- `academic-writing` — citation styles, plagiarism prevention, originality, hedging discipline. Runs alongside this skill.
- `critical-reasoning-and-argument` — mandatory for examiner-defensible claim, gap, methodology, interpretation, contribution, and countercase logic.
- `analytic-tradecraft` — for any forward-looking judgment inside the discussion section, the Heuer/Pherson SATs apply (KAC, ACH for contested findings).
- `source-evaluation` — every source in the literature review carries a tier and verification trail.
- `uganda-academic-research`, `kenya-academic-research` — institution-specific East African proposal, thesis, dissertation, viva, ethics, and formatting rules.
- `executive-communication` — for the executive-summary version of the work that ships to non-academic audiences alongside the dissertation.
- `python-document-generation` / `professional-word-output` — rendering layer for the final manuscript.

## Sources for this skill

- Brause, Rita S. *Writing Your Doctoral Dissertation: Invisible Rules for Success*. Falmer Press / RoutledgeFalmer, 1999. Tier 1. (Local extract: `extracted-books/doctoral-dissertation.txt`.)
- EQUATOR Network. *Enhancing the QUAlity and Transparency Of health Research*. https://www.equator-network.org/. Tier 1.
- PRISMA 2020. https://www.equator-network.org/reporting-guidelines/prisma/. Tier 1.
- CONSORT 2025. https://www.equator-network.org/reporting-guidelines/consort/. Tier 1.
- STROBE. https://www.equator-network.org/reporting-guidelines/strobe/. Tier 1.
- MOOSE. https://www.equator-network.org/reporting-guidelines/moose/. Tier 1.
- GRADE Working Group. https://www.gradeworkinggroup.org/. Tier 1.
- Cochrane Handbook. https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current. Tier 1.
- TOP Guidelines (Center for Open Science). https://www.cos.io/initiatives/top-guidelines. Tier 1.
- Cambridge, Oxford, LSE, Harvard, Yale, Princeton institutional examination and dissertation guidance. See `references/oxbridge-ivy-examination-conventions.md`. Tier 1.

The verbatim attribution discipline applies. References to Brause carry chapter; references to PRISMA / CONSORT / GRADE etc. carry the canonical institutional URL.

## Wave-2 task: institution-specific examination conventions

Completed in `references/oxbridge-ivy-examination-conventions.md`. Refresh this reference before high-stakes use because institutional regulations can change annually. The refresh must use current institutional primary sources and preserve the rule that missing word-count rules are marked as gaps, not inferred.
