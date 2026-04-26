---
name: analytic-tradecraft
description: Structured analytic discipline for any forward-looking judgment or contested-evidence question. Encodes ICD 203 nine standards, the Heuer/Pherson Structured Analytic Techniques (ACH, KAC, Devil's Advocacy, Red Cell, Pre-Mortem, What-If, High-Impact/Low-Probability), the Kent estimative-probability lexicon, the Heuer/Bruce cognitive-bias checklist, and the NATO Admiralty Code source-grading overlay. Five references; load only what the question demands.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: critical
---

# Analytic Tradecraft

Single entry skill for any judgment that ships under uncertainty. Every output of every cohort agent that contains a forward-looking claim, a contested-evidence call, or a "we conclude / we estimate / we assess" statement must pass this skill's discipline before shipping.

This skill operates **after** `source-evaluation` (which establishes whether a source is trustworthy) and **before** `executive-communication` (which restructures the judgment for an executive reader). It is the layer that makes the engine's outputs estimative-grade, not merely sourced.

## When to use

Use this skill on any output that:

- Contains the words *we assess / we conclude / we estimate / likely / probably / almost certainly / unlikely*
- Forecasts an outcome or evolution
- Adjudicates between competing accounts of the same event
- Rests on a single source for a load-bearing claim
- Makes a recommendation under uncertainty
- Will be read by a decision-maker who treats the output as actionable intelligence (board, regulator, examiner, principal investigator, partner)

If the output is purely descriptive ("the regulator filed X on date Y"), this skill is not required — `source-evaluation` is sufficient.

## The five rules (load first)

1. **ICD 203 nine standards.** Every estimative output must satisfy all nine before shipping. Reference: `references/icd-203-and-tradecraft-standards.md`.
2. **Multiple competing hypotheses.** No load-bearing judgment ships from a single hypothesis without an Analysis of Competing Hypotheses (ACH) matrix run on it. Reference: `references/heuer-pherson-sats.md`.
3. **Calibrated probability.** Forward-looking confidence is expressed in the Kent / ODNI lexicon with explicit numeric bands. **Confidence in the source** and **probability of the judgment** are stated separately. Reference: `references/kent-estimative-probability.md`.
4. **Cognitive-bias self-audit.** Before shipping, the analyst names which biases the conclusion is most exposed to and what mitigation was applied. Reference: `references/cognitive-bias-checklist.md`.
5. **No single-source key judgment.** No key judgment may rest on a single uncorroborated stream. If only one source exists, the judgment ships as a hypothesis with a confidence label of LOW and an explicit indicator of what would corroborate it. Reference: `references/sourcing-and-deception.md`.

## Decision router — load the matching reference

| Situation | Load |
|---|---|
| **Universal floor** | `references/icd-203-and-tradecraft-standards.md` (always) |
| **Contested evidence; multiple plausible accounts** | `references/heuer-pherson-sats.md` (use ACH) |
| **Strong consensus on a high-stakes call** | `references/heuer-pherson-sats.md` (Devil's Advocacy or Pre-Mortem) |
| **Forecast / future-state judgment** | `references/heuer-pherson-sats.md` (What-If, High-Impact/Low-Probability, Indicators) + `references/kent-estimative-probability.md` |
| **Inherited assumptions or "everyone knows" claim** | `references/heuer-pherson-sats.md` (Key Assumptions Check) |
| **Adversary / competitor reasoning** | `references/heuer-pherson-sats.md` (Red Cell) + `references/sourcing-and-deception.md` (mirror-imaging, D&D) |
| **Single source / contested source** | `references/sourcing-and-deception.md` |
| **Pre-publication self-audit** | `references/cognitive-bias-checklist.md` |

## ICD 203 — one-paragraph summary

The Office of the Director of National Intelligence's Intelligence Community Directive 203 (revalidated January 2015) requires every IC analytic product to satisfy nine standards: appropriate sourcing; explicit uncertainty; distinction between assumption and judgment; analysis of alternatives; customer relevance; logical argumentation; consistency with prior judgments (with change explained); accurate probability judgments; and proper use of visual information. The engine adopts these as a universal ship-gate for any estimative output. Source: ODNI ICD 203 PDF — https://www.dni.gov/files/documents/ICD/ICD-203.pdf. Tier 1.

## Structured Analytic Techniques — one-paragraph summary

The catalog formalised by Richards Heuer Jr. and Randolph Pherson (Heuer & Pherson, *Structured Analytic Techniques for Intelligence Analysis*, CQ Press, 2010 and later editions) gives the analyst named, runnable mini-protocols — each with a trigger, step-by-step method, output template, and known pitfalls. The engine adopts: ACH, Key Assumptions Check, Devil's Advocacy, Team A / Team B, Red Cell, What-If, High-Impact/Low-Probability, Pre-Mortem, Indicators-and-Warning, Argument Mapping. Reference: `references/heuer-pherson-sats.md`.

## Estimative probability — one-paragraph summary

Sherman Kent (Office of National Estimates, 1951–1973) observed that vague verbal probability ("possible", "likely") was read inconsistently across readers. He proposed pairing each verbal term with an explicit numeric band. The ODNI lexicon (almost certainly ≈ ≥95%; very likely ≈ 80–90%; likely ≈ 60–80%; probably ≈ 50–70%; might ≈ 20–50%; unlikely ≈ 10–20%; very unlikely ≤5%) is a direct descendant. The engine requires every estimative claim to use the lexicon and to **separate probability of the judgment from confidence in the source**. Reference: `references/kent-estimative-probability.md`.

## Universal output ship-gate

Before any estimative output ships, every box must be ticked:

- [ ] **ICD 203 nine standards** all satisfied (run the checklist in `references/icd-203-and-tradecraft-standards.md`).
- [ ] **At least one alternative hypothesis** considered — even if rejected. ACH matrix attached for any high-stakes judgment.
- [ ] **Key Assumptions Check** run — every load-bearing assumption listed and challenged.
- [ ] **Confidence vocabulary** drawn from the Kent / ODNI lexicon, with numeric band attached.
- [ ] **Probability and source-confidence stated separately.**
- [ ] **Cognitive-bias audit** — analyst names which biases the conclusion is most exposed to and what mitigation was applied.
- [ ] **No single-source key judgment** — or, if one exists, it is labelled HYPOTHESIS, given LOW confidence, and accompanied by indicators that would corroborate.
- [ ] **Change explanation** — if this judgment differs from a prior judgment by the engine, the change is explained and the trigger evidence cited.
- [ ] **Dissents footnoted** — any minority view inside the analytic team or against an external SME is recorded as a footnote, NIE-style.
- [ ] Manifest entry attached: `{judgment, hypothesis-set, evidence, biases-considered, confidence-judgment, confidence-source, indicators}`.

## Universal anti-patterns

- **Confirmation bias dressed as analysis.** Cherry-picking evidence that supports the dominant hypothesis without surfacing evidence that disconfirms it.
- **Mirror-imaging.** Assuming a counterpart (competitor, adversary, examiner) reasons the way the analyst does.
- **Conflating source confidence with judgment probability.** "High-confidence judgment" that turns out to rest on a single uncorroborated source.
- **"High / medium / low" confidence with no anchor.** Useful only when paired with the Kent / ODNI numeric band.
- **Single-source key judgment.** The Iraq WMD NIE 2002 is the canonical case: the central claims rested on Curveball (HUMINT) and the Samarra trucks (IMINT), neither corroborated. The fix is structural, not editorial.
- **Devil's Advocate as theatre.** A devil's advocate without standing or budget is a box-tick. The advocate must be empowered to surface a contrary memo that ships alongside the main judgment.
- **No change explanation.** A judgment that contradicts a prior judgment ships without a paragraph on why. Examiners and decision-makers notice.
- **Word-smithing as coordination.** The Bruce critique of IC coordination: it has been "corrupted into a linguistic exercise" rather than a re-test of evidence-inference linkage.

## Companion skills

- `source-evaluation` — runs first; establishes whether each source is trustworthy and at what tier.
- `research-orchestration` — wave dispatch; this skill plugs into Wave 2 (gap-fill triggers ACH if a contested judgment emerges) and Wave 3 (verification triggers Key Assumptions Check + cognitive-bias audit).
- `executive-communication` — runs after; restructures the estimative judgment for the senior reader. **Estimative discipline survives the restructuring**: the Kent lexicon and the dissent footnotes do not get smoothed away.
- `academic-reporting-standards` — for academic outputs, the equivalent quality controls are GRADE (evidence quality), TOP (transparency), Cochrane RoB (risk of bias). The Heuer/Pherson SATs and ICD 203 are the intelligence-side analogue.
- `due-diligence` — DD outputs are estimative judgments by another name; this skill applies in full.

## Sources for this skill

- George, Roger Z., and Bruce, James B., eds. *Analyzing Intelligence: Origins, Obstacles, and Innovations*. Georgetown University Press, 2008. Tier 1. (Local extract: `extracted-books/analyzing-intelligence.txt`.)
- ODNI Intelligence Community Directive 203 — Analytic Standards. January 2015. https://www.dni.gov/files/documents/ICD/ICD-203.pdf. Tier 1.
- Heuer, Richards J., Jr. *Psychology of Intelligence Analysis*. CIA Center for the Study of Intelligence, 1999. https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/. Tier 1.
- Heuer, Richards J., Jr., and Pherson, Randolph H. *Structured Analytic Techniques for Intelligence Analysis*. CQ Press / SAGE, multiple editions. Tier 1.
- Kent, Sherman. *Words of Estimative Probability* (1964; declassified). https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf. Tier 1.
- NATO Admiralty Code (STANAG 2511 / AJP-2.1) — Source Reliability A–F × Information Credibility 1–6. Tier 1.
- Silberman-Robb WMD Commission Report, 2005. Tier 1.

The verbatim attribution discipline applies in full: claims in the references that paraphrase George/Bruce, Heuer, Pherson, Kent are labelled as paraphrase and tied back to the canonical source. Quotations carry chapter/page where the source allows.
