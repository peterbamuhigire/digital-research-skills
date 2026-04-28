---
name: research-output-formats
description: Use when the engine has to deliver a research or knowledge-mining output and the question "what kind of document is this?" matters — covers essays, papers, pamphlets, white papers, theses, dissertations, research proposals, intelligence reports, market analyses, market research reports, legal opinions, product descriptions, policy briefs, case studies, feasibility studies, literature reviews, and op-eds. Each format has academic and non-academic variants; pick the variant before drafting. Five references, load only the family the deliverable belongs to.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: high
  depends_on:
    - source-evaluation
    - report-and-proposal-craft
    - academic-writing
    - business-writing
---

# Research output formats

The engine produces many document types. They share evidence discipline but differ in **purpose, audience, structure, voice, and citation regime**. Picking the wrong format is the most common reason a technically correct piece of research lands badly.

This skill is a **router**. Use it to:

1. Identify the format the deliverable belongs to.
2. Decide whether the academic or non-academic variant is appropriate.
3. Load the matching reference for structure, length, voice, and citation rules.

It does not replace `academic-writing`, `business-writing`, `report-and-proposal-craft`, `analytic-tradecraft`, `consulting-delivery`, or `online-legal-research` — it sits **above** them and tells you which to invoke for the given output.

## The non-negotiable guardrail

Every format defers to `source-evaluation/references/evidence-discipline.md`. No format excuses fabrication, even popular ones (op-eds, pamphlets, product descriptions). Format changes the **voice**, never the **truth standard**.

## The two axes

Every output sits on two axes:

| Axis | Question | Drives |
|---|---|---|
| **Format family** | What document type is this? | Structure, length, sections, citation style |
| **Academic vs non-academic variant** | Who is the reader and what do they accept as proof? | Voice, citation density, hedging, jargon, design |

Resolve both before drafting a single line.

## Selection router

Match the deliverable to a row, then load the named reference.

| Deliverable signal | Format | Reference |
|---|---|---|
| Argues a position in 800–5,000 words for a general or examiner audience | Essay | `references/academic-formats.md` §Essay |
| Original empirical or theoretical contribution, journal-shaped | Academic paper | `references/academic-formats.md` §Paper |
| Multi-chapter graduate research output (Master's) | Thesis | `references/academic-formats.md` §Thesis |
| Multi-chapter doctoral research output, original contribution to knowledge | Dissertation | `references/academic-formats.md` §Dissertation |
| Pre-research document seeking funding, ethics approval, or supervisor sign-off | Research proposal | `references/academic-formats.md` §Research-proposal |
| Standalone or chapter-length survey of existing scholarship | Literature review | `references/academic-formats.md` §Literature-review |
| Short, illustrated, persuasive, mass-distributed | Pamphlet | `references/advocacy-and-public-formats.md` §Pamphlet |
| 600–1,200 word newspaper or platform commentary, named author voice | Op-ed / commentary | `references/advocacy-and-public-formats.md` §Op-ed |
| 2–6 page recommendation document for a decision-maker on a specific policy choice | Policy brief | `references/advocacy-and-public-formats.md` §Policy-brief |
| Long-form authoritative analysis with thought-leadership intent, often vendor-published | White paper | `references/commercial-formats.md` §White-paper |
| Sized-and-segmented industry survey for buyers / investors | Market research report | `references/commercial-formats.md` §Market-research-report |
| Specific competitive / strategic question answered from market data | Market analysis | `references/commercial-formats.md` §Market-analysis |
| Short marketing copy for a single product or SKU | Product description | `references/commercial-formats.md` §Product-description |
| Single-subject narrative used to demonstrate a pattern, intervention, or outcome | Case study | `references/commercial-formats.md` §Case-study |
| Structured assessment of whether a project is viable | Feasibility study | `references/commercial-formats.md` §Feasibility-study |
| Decision-grade analysis with classified-style structure (BLUF, key judgments, confidence) | Intelligence report | `references/analytical-and-professional-formats.md` §Intelligence-report |
| Reasoned legal advice on a specific question, signed by counsel | Legal opinion | `references/analytical-and-professional-formats.md` §Legal-opinion |

After format is fixed, **always** load `references/academic-vs-nonacademic-variants.md` to choose voice and citation regime.

## Reference router

```
references/
  academic-formats.md                   essays, papers, theses, dissertations,
                                        research proposals, literature reviews
  advocacy-and-public-formats.md        pamphlets, op-eds, policy briefs
  commercial-formats.md                 white papers, market research reports,
                                        market analyses, product descriptions,
                                        case studies, feasibility studies
  analytical-and-professional-formats.md intelligence reports, legal opinions
  academic-vs-nonacademic-variants.md   the variant axis applied to every format
```

Load **only** the family file relevant to the deliverable, plus the variants reference. Loading every file is wasteful and dilutes attention.

## When to invoke this skill

- User asks for "a paper", "a white paper", "a brief", "a report", "an opinion", "a study" — these words map to different formats and you must disambiguate.
- The same research has to be repackaged for a new audience (e.g., an academic paper turned into a policy brief).
- Output is being generated by a sub-agent and you're writing the brief — name the format and variant in the brief.
- Reviewer says "this reads like an essay, not a brief" — you have a format mismatch, not a writing problem.

## When NOT to invoke

- Format is obvious and already locked (e.g., the user gave you a journal template, a publisher's house style, or a regulator's prescribed form). Use that template directly.
- The work is internal, throwaway, or conversational. No format selection needed.

## Decision flow

```
deliverable requested
        │
        ▼
  Is the format already prescribed (template, house style, statutory form)?
        │
   yes ─┴─ use that template, ignore this skill
        │
   no   ▼
  Match deliverable signal to selection-router row
        │
        ▼
  Load matching family reference for structure
        │
        ▼
  Load academic-vs-nonacademic-variants.md
        │
        ▼
  Pick variant; lock voice, citation regime, length
        │
        ▼
  Compose deliverable; cite-check against source-evaluation
```

## Common mistakes

| Mistake | Why it goes wrong | Fix |
|---|---|---|
| Treating "report" as a format | "Report" describes 6+ different documents in this skill alone | Force the user to pick a row in the selection router |
| Mixing variants in one document | Academic citation density inside a pamphlet voice repels both audiences | Lock variant before drafting |
| Skipping format selection on sub-agent briefs | Sub-agents default to "academic essay" voice — almost never what you want | Name format and variant verbatim in every brief |
| Treating a white paper as a longer brochure | A white paper makes an evidenced argument; brochures don't | Load `commercial-formats.md` §White-paper |
| Calling everything a "case study" | Case studies have a strict comparative or illustrative role | Load `commercial-formats.md` §Case-study |

## See also

- `report-and-proposal-craft` — long-form structure and proposal-specific patterns
- `academic-writing` — voice, citation, and argument standards for the academic variants
- `business-writing` — voice and structure for the non-academic variants
- `analytic-tradecraft` — drives the intelligence-report family
- `online-legal-research` — drives the legal-opinion family
- `consulting-delivery` — drives the market-analysis and feasibility-study families
- `professional-word-output` / `python-document-generation` — terminal renderers for any of these formats
