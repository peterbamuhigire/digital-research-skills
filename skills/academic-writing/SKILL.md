---
name: academic-writing
description: Use when drafting or revising an academic paper, essay, thesis, or dissertation with source-away composition, originality, citation, synthesis, voice, and register controls; use academic-reporting-standards for selecting formal study-reporting rules.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
  priority: critical
---

# Academic Writing

Academic prose must be reasoned, not merely cited. Before drafting any thesis statement, literature gap, interpretation, methodology justification, discussion, conclusion, or recommendation, load `critical-reasoning-and-argument` and run its argument map, countercase, fallacy, and certainty-calibration gates.

The single entry skill for any academic artifact: **paper, essay, thesis, dissertation** — in either the academic (peer-reviewed audience, strict conventions) or popular (general audience, conventions relaxed but rigor preserved) variant. Detail lives in `references/`; load only what the situation needs.

## Output-type router

| Output | Length | Audience | Original contribution required | Structural template (load) |
|---|---|---|---|---|
| **Essay (academic)** | 1,500–5,000 words | Course / journal / collection | Argument or interpretation, not new data | `references/conventions.md` § Essay |
| **Essay (popular)** | 800–2,500 words | General readers | Fresh angle, no formal contribution | `references/conventions.md` § Essay (popular) |
| **Paper (academic)** | 4,000–10,000 words | Peer-reviewed journal or conference | New finding, method, or argument | `references/conventions.md` § Paper |
| **Paper (popular)** | 1,500–4,000 words | Magazine / serious blog / Substack | Accessible synthesis or insight | `references/conventions.md` § Paper (popular) |
| **Thesis** | 15,000–30,000 words (Master's); discipline-dependent | Examiner committee | Master-level original contribution | `references/eco-thesis-craft.md` |
| **Dissertation** | 60,000–100,000 words (PhD) | Examiner committee + future scholars | Substantial original contribution | `references/eco-thesis-craft.md` |

**Pick the type before drafting.** Mixing a thesis structure into an essay (or essay register into a paper) is the most common failure mode.

## The four-question filter (Eco's gate, applied to every output)

Before writing, answer:

1. **Type** — paper / essay / thesis / dissertation.
2. **Variant** — academic or popular.
3. **Discipline** — sciences (IMRAD), social sciences (IBC or hybrid), humanities (essay/argument).
4. **Citation style** — APA / Chicago / MLA / Harvard / Vancouver. Load `references/citation-styles.md`.

Skipping any of these produces work that does not fit anywhere.

## The source-away workflow (mandatory)

The engine produces academic prose only via this pipeline:

```
Sources → Extract notes → SOURCE-AWAY GATE → Compose → Originality check → Output
```

Each step has a non-negotiable rule:

1. **Extract notes** — atomic note cards, fragments not sentences, with provenance per card. Load `references/trzeciak-note-discipline.md`.
2. **Source-away gate** — sources are removed from active context before composition begins. Trzeciak's law: *"You cannot copy what is not in front of you."*
3. **Compose** — synthesize across notes using `references/source-synthesis.md` patterns. Three or more sources synthesized into one paragraph is the strongest plagiarism shield.
4. **Originality check** — N-gram overlap audit against the source corpus. Load `references/originality-engine.md` and `references/plagiarism-prevention.md`. Any 7-word verbatim run is either restructured, quoted with attribution, or cited.

This pipeline is what makes the engine's "same prompt, three runs, three different but authentic outputs" property real.

## Reference index — when to load what

| Reference | Load when |
|---|---|
| `references/conventions.md` | Picking the structural template for the chosen output type |
| `references/eco-thesis-craft.md` | Thesis or dissertation — Eco's topic-gate, index-card system, ten commandments of quotation, plagiarism gates, prose rules, pride/humility posture |
| `references/trzeciak-note-discipline.md` | Always — pre-composition note-card discipline, source-away gate |
| `references/paraphrase-discipline.md` | Converting source material to engine prose — true paraphrase vs synonym-swap |
| `references/source-synthesis.md` | Combining multiple sources into one argument — agreement, disagreement, supplementation, gap-naming patterns |
| `references/quote-extraction.md` | Selecting and integrating direct quotations |
| `references/citation-brachiation.md` | Following citation chains backward and forward to build the working bibliography |
| `references/pearl-growing.md` | Iterative source discovery from a strong seed reference |
| `references/source-mining.md` | Mining databases, indexes, and open archives for academic sources |
| `references/citation-styles.md` | Picking and applying APA / Chicago / MLA / Harvard / Vancouver |
| `references/voice-and-register.md` | Hedging, modality, reporting verbs, signposting, register audit |
| `references/originality-engine.md` | Pre-delivery N-gram overlap audit |
| `references/plagiarism-prevention.md` | Pre-delivery five-rule audit (verbatim, structure, citation, quote-density, paraphrase fidelity) |
| `references/morley-rhetorical-moves.md` | Need a phrase for a rhetorical move (introducing work, citing literature, describing methods, reporting results, discussing findings, writing conclusions, hedging, comparing, signposting). Morley *Academic Phrasebank* (Tier 1). |
| `references/morley-reporting-verbs-and-hedges.md` | Choosing a reporting verb by stance (neutral / tentative / strong / critical) or selecting a hedge calibrated to evidence strength. Includes the Davis & Morley reuse-acceptability rule as a plagiarism-prevention guardrail. |
| `references/critical-literature-review.md` | Hardening a literature review so it synthesizes disputes, gaps, methods, and implications rather than listing sources |
| `references/thesis-production-hardening.md` | Thesis/dissertation planning, chapter logic, proposal checks, methodology justification, milestone and version discipline |

## Universal structural conventions

| Section | Paper | Essay | Thesis / Dissertation |
|---|---|---|---|
| Abstract | Required | Optional | Required |
| Introduction | Required | Required (often the hook) | Required (chapter) |
| Literature review | Embedded or separate | Embedded | Separate chapter |
| Methodology | Required (empirical) | Optional | Required (empirical) |
| Results | Required (empirical) | — | Required (chapter) |
| Discussion | Required | — | Required (chapter) |
| Conclusion | Required | Required | Required (chapter) |
| References / Bibliography | Required | Required | Required |
| Appendices | As needed | Rare | Common |

Detail in `references/conventions.md`.

## Variation across runs (per the engine's anti-plagiarism mandate)

Same prompt run three times must produce three authentic but distinct outputs. The variation comes from:

- **Different argument order** within the same outline structure.
- **Different opening hook** (anecdote, statistic, question, historical pivot).
- **Different reporting-verb subset** ("argues" vs "contends" vs "maintains" vs "claims").
- **Different paragraph-pattern** (claim-evidence-implication vs implication-evidence-claim).
- **Different sentence-length cadence**.
- **Different synthesis grouping** of the same source set.

The references and findings are the same. The argument, voice, and structure are different. Detail in `references/voice-and-register.md`.

## Universal anti-patterns

- Drafting before the source-away gate has fired (sources still in context).
- Synonym-swap "paraphrase" — load `references/paraphrase-discipline.md` and follow the four-step technique.
- Literature review as annotated bibliography — load `references/critical-literature-review.md` and `critical-reasoning-and-argument/references/literature-review-and-thesis-hardening.md`.
- Thesis or dissertation chapter that cites heavily but does not expose the research question, gap, method logic, contribution, and counter-literature.
- Verbatim 7-word runs from any single source — load `references/plagiarism-prevention.md`.
- Mixing citation styles within one document.
- One-source paragraphs — synthesize across three or more (`references/source-synthesis.md`).
- Dogmatic, unhedged claims (target 6–12 hedges per 1,000 words).
- Repeated reporting verbs ("Smith says ... Jones says ... Lee says").
- Mixing output types — thesis structure inside an essay, essay register inside a paper.
- Skipping the originality check before delivery.
- Treating the popular variant as the academic variant minus citations — popular still requires accuracy and attribution; only the form changes.

## Universal ship gate

- [ ] Output type and variant declared (paper / essay / thesis / dissertation × academic / popular).
- [ ] `critical-reasoning-and-argument` run on the central thesis, literature gap, methodology justification, interpretation, and conclusion.
- [ ] Citation style declared and applied consistently.
- [ ] Source-away gate fired before composition.
- [ ] Notes are fragments, not sentences (Trzeciak rule).
- [ ] Every paragraph cites where it should; quote-density audited.
- [ ] N-gram overlap check passed (no 7-word verbatim runs from any source).
- [ ] Voice audit passed (hedging in range, reporting-verb diversity).
- [ ] Structural template for the chosen type and variant followed.
- [ ] Reference list complete; every cited work is in the list, every list entry is cited at least once.
- [ ] DOI / persistent identifier captured where available.
- [ ] If thesis or dissertation: Eco's topic-gate, secret-title, provisional-TOC discipline applied.
- [ ] If thesis or dissertation: chapter logic, methodology justification, contribution-to-knowledge claim, limitations, and viva-defensible countercase are explicit.
- [ ] If popular variant: form relaxed, but accuracy and attribution preserved.

## Companion skills

- `dataset-discovery-and-analysis` — for empirical papers / theses, the data-finding layer.
- `critical-reasoning-and-argument` — mandatory for the argument, gap, method, interpretation, contribution, and countercase logic in every academic artifact.
- `data-quality-assessment` — score the data behind empirical claims on the four-axis model.
- `web-scraping-foundations` — when sources include web data.
- `business-writing` (planned) — for non-academic writing artifacts.
- `report-and-proposal-craft` (planned) — for business reports.

- `uganda-academic-research`, `kenya-academic-research` - local university documentation-style defaults, plagiarism thresholds, and proposal/thesis format rules.

## See also (within this skill)

The thirteen `references/` files together encode the body of academic-writing craft from Eco, Bailey, Trzeciak, and the engine's own discipline. Load only what the current task requires; do not load the entire references set by default.

<!-- dual-compat-start -->
## Use When

Use for source-grounded academic drafting, revision, synthesis, citation, paraphrase, and originality control.

## Do Not Use When

Do not use as the reporting-standard selector; route that decision to `academic-reporting-standards`.

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Research question, audience, genre | Author or brief | Stop and clarify the argument task |
| Verified source notes and citation style | Project corpus and venue rules | Produce an outline with gaps; do not invent citations |

## Workflow

1. Define the question, contribution, genre, and citation convention.
2. Build claim-to-source notes and separate quotation, paraphrase, synthesis, and inference.
3. Draft source-away from notes, then reconcile every claim to its source.
4. Stop on unattributed text or unsupported claims; recover by removing or marking the gap.
5. Run originality, structure, citation, and voice gates.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Academic draft and claim-source notes | Author, supervisor, or reviewer | Claims are traceable, citations conform, and originality checks expose no unresolved borrowing |

## Writing Evidence Guidance

Claim-source notes, quotation checks, citation audit, and originality checklist provide the writing evidence.

## Capability Contract

Review is read-only by default. Drafting or editing requires explicit authority; submission, authorship claims, and certification remain with the author.

## Degraded Mode

Without sources or citation rules, return a structured outline and explicit evidence gaps, not polished unsupported prose.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Exact wording matters | Quote and verify verbatim | Citation drift |
| Ideas combine across sources | Mark synthesis and cite all inputs | False single-source attribution |
| Claim lacks evidence | Remove or mark gap | Fabrication |

## Quality Standards

The argument answers the research question, sources support the claims attributed to them, and prose retains the author's defensible voice.

## Academic Writing Pitfalls

- Drafting from an open source paragraph; write from notes.
- Swapping synonyms to disguise copying; reconstruct the idea.
- Citation dumping; state each source's role.
- Inventing a bridge claim; mark synthesis or gap.
- Treating fluent prose as originality evidence; run the audit.

## Worked Example

Two sources supporting different parts of one conclusion are cited together and the resulting claim is marked `(synthesis)`.

## Book-derived additions

Use `dissertation-writing-process` when the deliverable spans chapter planning,
question-to-conclusion traceability, institutional formatting, and AI-use review.

## References

- [Source synthesis](references/source-synthesis.md)
- [Paraphrase discipline](references/paraphrase-discipline.md)
- [Plagiarism prevention](references/plagiarism-prevention.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Claim-source notes and originality audit | Author, supervisor, or reviewer | Quotations, paraphrases, syntheses, and inferences remain distinguishable and traceable |

## Anti-Patterns

- Drafting from an open source paragraph. **Fix:** close the source and draft from verified notes.
- Swapping synonyms to conceal copying. **Fix:** reconstruct the idea and cite its source.
- Dumping citations after unsupported claims. **Fix:** explain the evidentiary role of each citation.
- Inventing a bridge claim. **Fix:** mark it as synthesis or record an evidence gap.
- Treating fluency as originality evidence. **Fix:** run the source-away and originality checks.
