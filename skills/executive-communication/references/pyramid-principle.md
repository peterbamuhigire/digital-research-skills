# Reference — Pyramid Principle (Minto)

**Canonical source:** Barbara Minto, *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving* (1985; revised 1996, 2002, 2009). Available via the Minto Books International edition. Author's site: https://www.barbaraminto.com/.

This reference paraphrases Minto's framework in the engine's voice for skill use. It does not reproduce verbatim text from the book. Every claim below is consistent with Minto's published interviews, Minto's own articles, and McKinsey-alumni training materials including Rasiel's *The McKinsey Way* (1999).

---

## The shape

Every persuasive document forms a pyramid:

```
                    [ GOVERNING THOUGHT ]
                   /        |         \
            [ GROUP 1 ] [ GROUP 2 ] [ GROUP 3 ]
              / | \      / | \       / | \
            facts        facts        facts
```

- **Apex:** one governing thought — the answer the document delivers, in a single sentence.
- **Second tier:** typically 3 groups (sometimes 4; rarely 2 or 5). Each group is a sub-conclusion that supports the apex.
- **Third tier:** the facts, data, and quotations that support each group.

The pyramid is read **top-down by the reader** and **built bottom-up by the writer**. The writer gathers facts first, finds the groups they form, then articulates the governing thought the groups together support. The reader sees the answer first.

## Three rules below the apex

1. **Ideas at any level summarise the ideas grouped below them.** A group's heading must accurately summarise its three facts; a section's heading must accurately summarise its three sub-sections.
2. **Ideas in each grouping must be the same kind of idea.** All three sub-sections of a section must answer the same question — all "why" or all "how" or all "when", not a mix.
3. **Ideas in each grouping must be logically ordered.** Time order, structural order (e.g. North → South → East → West), or degree order (most → least important).

These rules are non-negotiable. A pyramid that breaks any of them is a pile of bullets, not an argument.

## MECE

**M**utually **E**xclusive, **C**ollectively **E**xhaustive. Coined by Minto. The three groups under the apex must:

- **ME:** not overlap. If two groups address the same point from different angles, collapse them.
- **CE:** together cover the whole problem. If a sceptic could ask "but what about X?" and X isn't in any group, the decomposition is incomplete.

MECE is the test for whether the second tier of the pyramid is actually structured or merely listed.

## The skim path

Pull every section title and group heading out of the document and read them in sequence with no body text. The result must be a complete, coherent argument. If it isn't, the document is broken: the headings are topics rather than takeaways (fix → `references/action-titles.md`), or the structure is wrong (fix → re-MECE).

McKinsey-alumni training calls this the **skim path** test. It is the single most diagnostic check on any artefact.

## The two reasoning patterns

Minto distinguishes:

- **Inductive reasoning** — supporting facts are different in kind, but together they suggest a conclusion. Group heading is the conclusion.
- **Deductive reasoning** — facts form a chain (A is true; if A then B; therefore B). Group heading is the "therefore". Use deductive sparingly: it is harder to read because the reader cannot skim.

Default to inductive at the section level. Reserve deductive for sub-sections where the chain is short and load-bearing.

## Building the pyramid — the workflow

1. **Define the question.** What is the reader's question? (If it is unclear, stop — go back to `research-orchestration` to scope.)
2. **State the answer in one sentence.** This is the governing thought. If you cannot, the analysis is incomplete.
3. **List the supporting points.** Brainstorm freely; do not yet group.
4. **Group the points MECE.** Aim for 3 groups; check ME (no overlap) and CE (no gaps).
5. **Write group headings as full takeaway sentences.** Not topics. (See `references/action-titles.md`.)
6. **Order the groups.** Time, structure, or degree.
7. **Skim-path test.** Read only the headings; verify the argument lands.
8. **Fill in evidence under each group.** Every fact ties back to the upstream research manifest; preserve source + tier + confidence.
9. **Write the SCQA opener.** Situation → Complication → Question → Answer. (See `references/scqa-opener.md`.)
10. **Final ship-gate.** Run the checklist in `SKILL.md`.

## Common failures

| Failure | Diagnostic | Fix |
|---|---|---|
| Three groups overlap | Sceptic can rephrase one as part of another | Collapse and re-MECE |
| Three groups leave a hole | Sceptic asks "but what about X?" and X is missing | Add a fourth group or re-MECE the three |
| Group has 7 sub-points | Reader can't hold them in mind | Re-MECE into 2–3 sub-groups |
| Headings are topics ("Findings") | Skim-path test fails | Action-title rewrite |
| Mixed kinds in one group | A group has one "why", one "how", one "what" | Split into separate groups |
| Apex changes mid-document | The governing thought drifts | Choose one; rewrite |

## When NOT to use the pyramid

- **Academic theses** at examination institutions (Oxford, Cambridge, LSE, Ivy): the convention is literature-review-first, methodology-then-findings, and a discussion that argues the conclusion. The pyramid's answer-first opening is wrong for an examiner who expects the candidate to demonstrate the reasoning. Use `academic-writing` + `academic-reporting-standards` instead.
- **Chronological narratives** (incident reports, case studies told in time order): the time order is the structure. Apply Minto's three rules within sections rather than at the document level.
- **Legal briefs**: the form is dictated by court rules (e.g. IRAC — Issue, Rule, Application, Conclusion). The pyramid hides inside the Conclusion, not the document.

## Companion patterns inside the engine

- `references/scqa-opener.md` — how to construct the apex sentence and the opener.
- `references/action-titles.md` — how to write group headings.
- `references/ghost-deck-pattern.md` — how to build the pyramid for a slide deck.
- `references/zelazny-chart-selection.md` — how to choose the chart that supports each group's evidence.
- `references/executive-summary-template.md` — pyramid compressed to ≤ 300 words.

## Source

Minto, Barbara. *The Pyramid Principle: Logic in Writing and Thinking*. Pitman / Minto Books International, 1985 / 1996 / 2002 / 2009. https://www.barbaraminto.com/. Tier 1.

Independent corroboration: Rasiel, *The McKinsey Way* (1999); McKinsey Alumni interview with Minto on MECE, https://www.mckinsey.com/alumni/news-and-events/global-news/alumni-news/barbara-minto-mece-i-invented-it-so-i-get-to-say-how-to-pronounce-it (Tier 1). Tier 2 corroboration in widely used consulting-prep texts (Cheng, Cosentino).
