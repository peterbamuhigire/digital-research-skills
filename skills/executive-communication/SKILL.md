---
name: executive-communication
description: Output craft for executive-grade artefacts. Covers the Minto Pyramid Principle (SCQA opener, single governing thought, MECE decomposition), the McKinsey ghost-deck and action-title discipline, the Bain "answer-first" pattern, and the Zelazny chart-selection rule. Use on every report, memo, deck, and one-pager intended for a senior reader. Six references; load only what the artefact demands.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: high
---

# Executive Communication

Single entry skill for turning a research corpus into an executive-grade artefact. The engine's research outputs are dense and source-disciplined; this skill makes them **read like a McKinsey, Bain, or BCG deliverable** — answer first, MECE-structured, action-titled, one-message-per-page, chart-selection-disciplined.

This skill does not invent claims. It restructures and surfaces claims the upstream research already produced. **Evidence-discipline applies in full**: every load-bearing fact in the executive output traces back to the upstream research's source manifest. The governing thought must come from a tested argument map produced through `critical-reasoning-and-argument`.

## When to use

Use this skill when producing any of:

- **Executive summary** (one page; ≤300 words)
- **One-pager** for a decision-maker
- **Slide deck** intended for senior audience (board, C-suite, partner, examiner)
- **Long-form report** that needs an answer-first storyline
- **Cover memo** or briefing note
- **Proposal** (where pyramid + SCQA structure are competitive table stakes)

Do **not** use this skill on raw research-corpus markdown, on internal scratchpads, on academic writing (use `academic-writing` + `academic-reporting-standards` instead), or on social-media output.

## The five rules (load first)

1. **Answer first.** The single governing thought of the artefact appears at the top, in one sentence, before any context or evidence. Reference: `references/pyramid-principle.md`.
2. **SCQA opener.** Every artefact opens with **S**ituation → **C**omplication → **Q**uestion → **A**nswer. The answer is the governing thought. Reference: `references/scqa-opener.md`.
3. **MECE decomposition.** Below the governing thought, support is broken into 3 (rarely 4) groups that are **Mutually Exclusive and Collectively Exhaustive**. No overlap; no gaps. Reference: `references/pyramid-principle.md`.
4. **Action titles.** Every section heading, slide title, or table caption is a complete sentence stating the takeaway — not a topic label. "Market is consolidating" is wrong; "Top three players will hold 70% share by 2028" is right. Reference: `references/action-titles.md`.
5. **One message per page; right chart for the message.** Each slide / section carries exactly one message; the chart serves the message. Use Zelazny's five chart families. Reference: `references/zelazny-chart-selection.md`.

## Decision router — load the matching reference

| Artefact type | Load |
|---|---|
| **Executive summary** | `references/scqa-opener.md` + `references/executive-summary-template.md` |
| **One-pager** | `references/scqa-opener.md` + `references/executive-summary-template.md` (truncate to 5 sentences) |
| **Slide deck** | `references/pyramid-principle.md` + `references/action-titles.md` + `references/zelazny-chart-selection.md` + `references/ghost-deck-pattern.md` |
| **Long-form report** | `references/pyramid-principle.md` + `references/scqa-opener.md` + `references/action-titles.md` |
| **Cover memo / briefing note** | `references/scqa-opener.md` + `references/action-titles.md` |
| **Proposal** | All references |

## The Pyramid Principle (Minto) — one-paragraph summary

Barbara Minto, then a McKinsey consultant in London, formalised the principle in the 1970s and published it in 1985 (revised 1996) as *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving*. The framework: any persuasive document carries **one governing thought** at the apex. That thought is supported by **3 sub-points** (groups). Each sub-point is supported by **3 facts** (or further sub-groups). Reading top-down, the document gives the answer first and the evidence after. Reading the section titles only — the "skim path" — must still convey a complete logical argument. (Minto, *The Pyramid Principle*, 1985 / 1996. Minto's own articles at https://www.barbaraminto.com/ and the MECE provenance interview at https://www.mckinsey.com/alumni/news-and-events/global-news/alumni-news/barbara-minto-mece-i-invented-it-so-i-get-to-say-how-to-pronounce-it.)

## The ghost deck (McKinsey practice)

Before opening any slide tool, draft the deck on paper or in markdown as a **ghost deck**: a numbered list of action titles. The ghost deck is "complete" when reading the action titles in sequence narrates the entire argument with no slide content needed. Only then design the slides. (Reference: `references/ghost-deck-pattern.md`. Documented in McKinsey-alumni training materials and Rasiel's *The McKinsey Way* (1999).)

## The "answer-first" pattern (Bain practice)

Bain trains consultants to **lead with the hypothesis** and then present only the few facts required to validate it. Distinct from McKinsey's exploratory framing. Use answer-first when the audience is time-constrained and decision-ready; use the fuller pyramid when the audience needs to follow the reasoning. Both are pyramid-shaped; only the opening differs. (Reference: `references/scqa-opener.md`.)

## Zelazny chart selection — one-paragraph summary

Gene Zelazny, McKinsey's longtime Director of Visual Communications, reduced business charting to **five families**: component (pie / stacked bar), item (bar / column / scatter), time-series (line), frequency (histogram), correlation (scatter / bubble). The rule: **pick the chart for the message**, not the data. If the message is "Acme dominates", use a bar (item comparison). If the message is "Acme has lost share over time", use a line (time-series). One message → one chart → one slide → 60 seconds. (Zelazny, *Say It With Charts: The Executive's Guide to Visual Communication*, 4th ed. 2001. Reference: `references/zelazny-chart-selection.md`.)

## Universal output ship-gate

Before any executive artefact ships, every box must be ticked:

- [ ] **Governing thought** stated as a single sentence in the first 50 words.
- [ ] **Critical-reasoning gate** passed before restructuring: governing thought, 3-5 support points, objections, and implications are tested.
- [ ] **SCQA opener** present (or a defensible variant: "Answer / Situation" if the audience is decision-ready).
- [ ] Support is **MECE** at the top level (no overlap; no obvious gap).
- [ ] Every section title is an **action title** — a complete declarative sentence.
- [ ] Each section / slide carries **one message**.
- [ ] Every chart is the **right family** for its message (Zelazny rule).
- [ ] Skim-path test: reading only headings, the argument is complete.
- [ ] Executive summary fits **one page** (≤ 300 words).
- [ ] **No claim is unsourced** — every fact still ties back to the upstream research manifest.
- [ ] Confidence-and-uncertainty discipline preserved from upstream (see `analytic-tradecraft` for estimative-probability vocabulary).

## Anti-patterns

- **Topic titles.** "Market overview", "Methodology", "Findings" — these are skeletons, not titles. Replace with a complete sentence stating what the section concludes.
- **Buried lede.** The decision-maker reads the first paragraph and the last paragraph. If the answer is in the middle, the artefact has failed.
- **3-card-monte structure.** Every section title says the same thing in different words. The reader can't navigate; the writer hasn't decomposed MECE.
- **Chart for chart's sake.** A visual added because "the slide felt empty". If no message, no chart.
- **Over-citation in the body.** Footnote density signals the writer is hiding behind sources rather than committing to a claim. Cite, but commit.
- **Mixed governance.** The artefact has two governing thoughts because the writer couldn't choose. Choose.
- **Audience-mismatch.** Pyramid Principle is for senior, time-constrained readers. For an examiner reading a thesis, use `academic-writing` + `academic-reporting-standards` instead — the conventions differ.

## Companion skills

- `report-and-proposal-craft` — long-form scaffolding (headers, sections, tone) — feeds into this skill's restructuring pass.
- `critical-reasoning-and-argument` — runs before this skill; supplies the tested governing thought, support chain, countercase, limits, and action implications.
- `professional-word-output` / `python-document-generation` — the rendering layer below this skill.
- `academic-writing` + `academic-reporting-standards` — for academic artefacts where a thesis examiner expects literature-review structure rather than answer-first.
- `analytic-tradecraft` — preserves estimative-probability language and competing-hypothesis discipline through the restructuring.
- `source-evaluation` — every claim still carries source + tier + confidence after restructuring.

## Sources for this skill

- Minto, Barbara. *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving*. Minto Books International, 1985 (revised 1996, 2002, 2009). Tier 1.
- Minto, Barbara. Personal site and articles — https://www.barbaraminto.com/ — Tier 1.
- McKinsey & Company Alumni interview with Barbara Minto on MECE — https://www.mckinsey.com/alumni/news-and-events/global-news/alumni-news/barbara-minto-mece-i-invented-it-so-i-get-to-say-how-to-pronounce-it — Tier 1.
- Zelazny, Gene. *Say It With Charts: The Executive's Guide to Visual Communication*. McGraw-Hill, 4th ed. 2001. Tier 1.
- Rasiel, Ethan M. *The McKinsey Way*. McGraw-Hill, 1999. Tier 1 (insider account).
- Rasiel, Ethan M. and Friga, Paul N. *The McKinsey Mind*. McGraw-Hill, 2001. Tier 1.

The verbatim attribution discipline applies: claims in the references that paraphrase Minto / Zelazny / Rasiel are labelled as paraphrase and tied back to the canonical book.
