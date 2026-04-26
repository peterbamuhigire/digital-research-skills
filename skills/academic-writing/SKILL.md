---
name: academic-writing
description: Use as the single entry point for any academic output — paper, essay, thesis, or dissertation, in either the academic or popular variant. Carries the output-type router, the source-away workflow, the originality gate, and orchestration rules across thirteen craft references (paraphrase, plagiarism prevention, citation styles, voice & register, note discipline, source synthesis, etc.).
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: critical
---

# Academic Writing

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
- [ ] If popular variant: form relaxed, but accuracy and attribution preserved.

## Companion skills

- `dataset-discovery-and-analysis` — for empirical papers / theses, the data-finding layer.
- `data-quality-assessment` — score the data behind empirical claims on the four-axis model.
- `web-scraping-foundations` — when sources include web data.
- `business-writing` (planned) — for non-academic writing artifacts.
- `report-and-proposal-craft` (planned) — for business reports.

## See also (within this skill)

The thirteen `references/` files together encode the body of academic-writing craft from Eco, Bailey, Trzeciak, and the engine's own discipline. Load only what the current task requires; do not load the entire references set by default.
