---
name: mind-mapping-and-synthesis
description: Use when synthesising a literature pass, taxonomising findings across cohorts, planning a research wave, decomposing a brief, or compressing a large corpus into a navigable map. Teaches Buzan's mind-mapping method (radial organisation, BOIs, Laws of Mind Mapping) adapted for analyst use, plus Mermaid `mindmap` patterns as the engine-native artifact. Three references; method-first with concrete diagram templates.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: medium
  derived_from:
    - "Tony Buzan, Mind Map Mastery — The Complete Guide to Learning and Using the Most Powerful Thinking Tool in the Universe"
    - "Tony Buzan, Buzan Study Skills Handbook (the EPUB is image-only; method is taken from Mind Map Mastery, which covers the same content)"
---

# Mind mapping and synthesis

Mind mapping is a radial organisation technique developed by Tony Buzan: a central image or topic, with branches radiating outward, each branch carrying a single keyword or image, with sub-branches deepening the structure. The engine uses mind maps as a **synthesis** tool — for compressing a large corpus into a navigable structure and for finding relationships that linear notes hide.

This is **not** an aesthetic choice. Mind maps and linear notes do different cognitive work; choosing the right one matters for output quality.

## When to invoke this skill

- A literature pass has produced a large body of notes that needs structure
- Pain points across multiple cohorts need a taxonomy
- A regulatory landscape needs a navigable overview
- A research brief has multiple dimensions that won't fit a linear outline
- Synthesis across cohorts (`research-orchestration`) is producing too much narrative and not enough structure
- The analyst is stuck in linear thinking and the problem has hierarchical or radial structure

When **not** to use mind mapping:

- The output is purely sequential (a procedural runbook, a chronology)
- The structure is dynamics, not hierarchy (use `systems-thinking-and-mental-models`)
- The output is a legal analysis (use `online-legal-research` IRAC)
- The audience expects prose (mind maps are a *thinking* tool; the output may need to be re-rendered as prose)

## Buzan's seven steps (Mind Map Mastery, Chapter 1)

Verbatim from Buzan, lightly condensed:

1. **Place the sheet of paper in landscape format.** Use at least three different colours to draw an image in the very centre of the paper that represents the subject. The central image activates imagination and triggers associations.
2. **Pick a colour and draw a thick branch coming away from the central image, like the bough of a tree.** Let the branch curve organically. Its thickness symbolises the weight of the association in the hierarchy.
3. **Label the branch with a single word in capital letters** — or a symbol. Each branch carries one keyword.
4. **Send out secondary-level shoots from the main branch. Then third-level branches** that spread out from the secondary shoots. Write keywords or draw symbols on all branches.
5. **Pick another colour and create the next main branch**, working around the central image. Continue until you have about five or six main branches.
6. **Move freely around the Mind Map**, leaping between branches, filling gaps and adding new sub-branches as ideas occur.
7. **Add arrows, curving lines and links between main branches** to reinforce connections.

## The Laws of Mind Mapping (Mind Map Mastery, Chapter 2 — verbatim from Buzan)

1. Always use a blank sheet of paper, placed in landscape position.
2. Draw a picture in the centre of the paper, representing your subject, using at least three colours.
3. Use images, symbols, codes and dimension throughout your Mind Map.
4. Select keywords and write these using capital letters.
5. Place each word or image on its own branch, so that it stands by itself.
6. Radiate flowing branches out from the central image. Make the branches thicker toward the centre of the Mind Map, and thinner as they radiate outward.
7. Keep branches the same length as the words or images on them.
8. Use colours throughout, developing your own colour code in the branches.
9. Use emphasis, arrows and connecting lines to depict associations between different related topics.
10. Aim for clarity by positioning your branches in carefully thought-through space. The space between things is often as important as the things themselves.

These laws are not arbitrary aesthetic preferences. Buzan's argument: each law strengthens the cognitive grip the map has on the brain — colour, single keywords, radial structure, and curved branches all contribute to recall and association.

## How the engine adapts Buzan for analyst work

The engine outputs markdown corpora and Word documents. Hand-drawn radial mind maps don't translate directly. The translation rules:

| Buzan's law | Engine adaptation |
|---|---|
| Landscape paper, central image | Mermaid `mindmap` block with the central topic as `root` |
| At least three colours | Mermaid theme styling on classes; or annotation markers (★, ●, ▲) when colour is unavailable |
| Single keyword per branch | One noun/noun-phrase per branch; never sentences |
| Radial branches | `mindmap` natively does this |
| Colour code | Class names in Mermaid; conventional categories: blue=evidence, green=opportunity, red=risk, gold=insight |
| Cross-links between branches | Annotated as separate `relationships:` block beneath the mindmap, since Mermaid `mindmap` does not natively support cross-links |
| Images / symbols | Unicode glyphs (📌 ⚖ 🔍 ⚠ 💡 🌍) where the audience expects them; otherwise omit |

## Reference router

| Need | Load |
|---|---|
| **How to construct a mind map for analyst purposes** (synthesis pass, taxonomy, brief decomposition) | `references/mind-map-construction.md` |
| **How to use mind maps for learning, recall, and study** (analyst preparing for an unfamiliar domain) | `references/study-and-recall-techniques.md` |
| **Concrete Mermaid `mindmap` templates** for engine output (cohort synthesis, pain-point taxonomy, regulatory landscape, research-plan map) | `references/mermaid-mindmap-patterns.md` |

## Use cases in the engine

### Cohort synthesis

After research-wave outputs are merged into `<cohort>/research/`, a mind map captures the cohort's structure: central node = the cohort question; main branches = themes; sub-branches = specific findings; cross-links = recurring patterns. The mind map becomes part of `<cohort>/analysis/` and feeds `cross-cohort-synthesis`.

### Pain-point taxonomy

When `pain-point-taxonomy` is the active skill, the radial structure helps: pain category as a main branch, specific instances as sub-branches, cross-links between cohorts that share the same pain.

### Regulatory landscape

A regulatory landscape mind map — central node = the regulated activity; main branches = regulators / statutes / cases / guidance; sub-branches = specifics. Pairs well with a systemigram from `systems-thinking-and-mental-models` (the systemigram shows flows; the mind map shows hierarchy).

### Research-plan decomposition

A brief with multiple cohorts decomposes naturally into a mind map: central node = the project; main branches = cohorts; sub-branches = themes within each cohort; further branches = sources to mine. Helps spot scope-creep and gaps before sub-agents are dispatched.

### Brief decomposition for sub-agents

Each sub-agent's portion of the project corresponds to one main branch. Reading off the branch produces the sub-agent brief.

## Universal anti-patterns

- Writing sentences on branches (one keyword per branch is non-negotiable)
- Branches all the same colour / class — defeats the cognitive purpose
- Mind map with no cross-links when the corpus has obvious connections (relationships are part of the value)
- Treating the mind map as the deliverable when the audience needs prose (it's a *thinking* artifact; re-render for the audience)
- Building a mind map when the underlying structure is sequential, dynamic, or temporal (use the right tool)
- Skipping the central image / topic — the centre is the anchor; without it the radial structure becomes arbitrary
- Adding branches to fill space rather than because the structure demands them (every branch should earn its place)
- Using a mind map to *avoid* doing the linear-prose work — the mind map is upstream of prose, not a substitute

## Companion skills

- `research-orchestration` — for sequencing mind-map syntheses across waves
- `systems-thinking-and-mental-models` — for dynamics work that mind maps cannot capture
- `analytic-tradecraft` — when the synthesis becomes a formal estimative judgement
- `documentation-generation:mermaid-expert` — for richer Mermaid notation when the mindmap shape isn't enough
- `professional-word-output`, `python-document-generation` — for rendering the mind map into a Word artifact

## Sub-agent briefing — when to ask for a mind map

Some sub-agent tasks should return a mind map rather than (or in addition to) a narrative report. Trigger words:

- "taxonomy of …"
- "structure of …"
- "categories of …"
- "landscape of …"
- "map the relationships between …"

When dispatching such a task, request the deliverable as a Mermaid `mindmap` block plus a short prose key. The brief still includes the evidence-discipline clause from `source-evaluation`.
