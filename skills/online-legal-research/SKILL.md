---
name: online-legal-research
description: Use when a research question turns on statutes, regulations, case law, court decisions, treaties, legal authority, or jurisdictional analysis — covers identifying primary vs secondary sources, online search strategy, citator/currency validation, IRAC analysis, and citation discipline. Method-first and jurisdiction-agnostic at the core, with an East African overlay (Uganda, Kenya, EAC) as the engine's home jurisdictions. Five references, load only what the question demands.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: high
  derived_from:
    - "Putman & Albright, Legal Research, Analysis and Writing (Cengage, 2018)"
    - "Long, Legal Research Using the Internet"
    - "Legal Research (anonymous compendium)"
---

# Online legal research

Method skill for any research that touches binding legal authority. The engine's domain is largely **East African / Commonwealth** (Uganda, Kenya, EAC), but the core methodology is jurisdiction-agnostic and the legal source-books are US-faithful. The skill therefore separates **method** (universally portable) from **examples** (often US, retained as illustration only) and supplies an **East African overlay** for application in the engine's home jurisdictions.

## The non-negotiable guardrail

Embed the `source-evaluation` evidence-discipline clause verbatim in every sub-agent legal-research brief:

```
HARD CONSTRAINT — NO HALLUCINATION:
- Do NOT invent statistics, names, organisations, court cases, statutes, or URLs.
- Cite every numeric claim and every direct quote at the point it appears.
- If you cannot find a source for a fact, mark it as a "gap" — do not fabricate filler.
- For any claim you assemble from multiple sources, mark it "(synthesis)".
- For any inference, mark it "(inference)".
- Verbatim quotes must reproduce text exactly as it appeared in the source — no creative editing.
```

For legal work, the failure mode is severe: **a fabricated case name, statute number, or pinpoint citation is malpractice-grade**. Every case name and statute citation is verified against an authoritative repository before it ships.

## When to invoke this skill

- Question hinges on whether something is lawful, regulated, or actionable
- Output references statutes, regulations, court decisions, gazettes, parliamentary records
- A counterparty (regulator, lawyer, tribunal, court) might rely on the output
- The user asks for a "regulatory landscape", "compliance overview", "case law summary", or similar
- Cross-jurisdictional analysis (e.g., comparing Ugandan and Kenyan data-protection law)

## The legal-research workflow

```
1. Frame the legal question         → references/legal-analysis-irac.md (Issue step)
2. Identify the relevant jurisdiction(s) and forum(s)
                                    → references/source-hierarchy-and-authority.md
3. Locate primary authority         → references/source-hierarchy-and-authority.md
                                      + references/east-african-overlay.md (EA work)
4. Triangulate with secondary       → references/source-hierarchy-and-authority.md
5. Search online with discipline    → references/online-research-workflow.md
6. Validate currency (citator)      → references/online-research-workflow.md
7. Apply IRAC                       → references/legal-analysis-irac.md
8. Cite-check before shipping       → references/citation-and-quoting-discipline.md
```

## Reference router

| Need | Load |
|---|---|
| **Always — universal floor** | `source-evaluation/references/evidence-discipline.md` |
| Working out what counts as authority and how much weight it carries | `references/source-hierarchy-and-authority.md` |
| Building Boolean / field / natural-language searches; using citators; deciding free vs paid databases | `references/online-research-workflow.md` |
| Structuring the legal analysis (Issue, Rule, Application, Conclusion) | `references/legal-analysis-irac.md` |
| Quoting, paraphrasing, citing legal sources without distortion | `references/citation-and-quoting-discipline.md` |
| Applying any of the above in Uganda, Kenya, EAC, or wider Commonwealth East Africa | `references/east-african-overlay.md` |

## Core distinctions (load these into working memory)

**Primary vs secondary authority.** Primary authority is the law itself — constitutions, statutes, regulations, court judgments, treaties. Secondary authority is commentary on the law — textbooks, journal articles, encyclopaedias, restatements. *Only primary authority can bind a court.* Secondary authority guides interpretation but never controls.

**Mandatory vs persuasive authority.** Mandatory (binding) authority is primary authority that a court is **required** to follow — typically because it issued from a higher court in the same jurisdiction, or is a statute of that jurisdiction in force on the relevant date. Persuasive authority is everything else: primary authority from a different jurisdiction, dicta, lower-court decisions in a higher court, all secondary authority. A court *may* follow persuasive authority but is not bound to.

**Stare decisis.** The doctrine that requires a court to follow a previous decision of itself or a higher court when current facts and issues are sufficiently similar to the earlier case. Not absolute — exceptions include outdated reasoning, supervening legislation, and demonstrably bad reasoning (per Putman & Albright).

**Currency.** A statute may have been amended; a case may have been overruled, reversed, or distinguished. *Every cited authority must be checked for currency before it ships.* That check is the function of a citator (Shepard's, KeyCite, or jurisdiction-equivalent).

## Universal output rule for legal claims

Every legal claim ships with:

- **Authority cited** (case name, statute section, regulation number, treaty article)
- **Pinpoint reference** (paragraph, section, page — not just the case)
- **Source repository link** (KenyaLaw, ULII, eCase, court website, gazette PDF) with archive snapshot
- **Currency check** (verified active / not overruled / not amended on date X)
- **Tier assigned** via `source-evaluation/references/credibility-ladder.md` (legal authority is normally tier 1 or 2)
- **Date accessed** (UTC)

If any of those is missing, the claim does not ship.

## Universal anti-patterns in legal research

- Citing a case from a syllabus, headnote, or commentary without reading the judgment
- Treating a foreign-jurisdiction case as binding when it is at most persuasive
- Quoting a statute as enacted when it has since been amended (no currency check)
- Relying on a single secondary source (treatise, blog, AI summary) as if it were primary
- Pinpointing to a "page" in an electronic judgment with no pagination — must use paragraph numbers
- Confusing the *holding* (binding rule) with *dicta* (non-binding aside)
- Treating a judgment of a lower court as authoritative for a higher court
- Citing a US case in a Ugandan or Kenyan brief as if it were anything more than persuasive comparative material
- Inventing a case name, docket number, or section number — strike on sight per evidence-discipline

## Companion skills

- `source-evaluation` — universal floor; legal authority still carries tiers and verification
- `analytic-tradecraft` — when conflicting authorities require an estimative judgment
- `academic-writing` — when the legal output is academic (essay, journal article)
- `business-writing` — when the legal output is a memo, advisory, brief
- `osint-investigation` — when statutes/regulations interact with named entities
- `due-diligence` — when legal research feeds an entity-level risk picture
- `kenya-academic-research`, `uganda-academic-research` — for jurisdiction-specific style and language

## Sub-agent briefing template (legal cohort)

When dispatching a legal-research sub-agent, include — verbatim — the evidence-discipline clause above, plus:

```
JURISDICTION CONSTRAINT:
- Treat [jurisdiction] courts/statutes as the only mandatory authority.
- Other-jurisdiction material is persuasive at most — flag with "(persuasive)".
- Verify every cited case on [KenyaLaw / ULII / EACJ / specified repository] before quoting.
- Verify currency: is the statute amended? is the case overruled, reversed, or distinguished?
- Pinpoint cite to paragraph (judgments) or section (statutes), never a generic page.
- Provide a verifiable URL (with archive snapshot) for every authority.
```
