# Mind-map construction for analyst work

**Date written:** 2026-04-27
**Drawn from:** Tony Buzan, *Mind Map Mastery* (Chapters 1–3 in particular: What is a Mind Map; How to Mind Map; What Is *Not* a Mind Map).

This reference applies Buzan's seven steps and ten Laws to the engine's working contexts: synthesising research output, taxonomising findings, decomposing briefs, planning waves. It is the practical operator's manual for `mind-mapping-and-synthesis`.

## The starting move — choose the centre

Buzan: *"When you have a subject in mind, start to draw a central image in the centre of the paper."* The centre is the **anchor of the entire structure**. Everything else radiates from it.

For analyst work the centre is one of:

- A **research question** ("What pain points do clinical researchers face in Uganda?")
- A **deliverable name** ("UPF CRIS engagement design")
- A **system** ("Kenyan data-protection regulatory landscape")
- A **brief** ("Wave 2 cohort scope")
- A **cohort** ("UPF CRIS clinical-researcher cohort")

The centre **is not**:

- A theme (themes are branches, not centres)
- A finding (findings are sub-branches)
- A vague abstraction ("research", "law", "thinking") — the centre needs specificity

If the centre is hard to choose, the mind map is premature. Refine the brief first.

## Three essential characteristics (Buzan, Chapter 1)

A good mind map has:

1. **A central image** capturing the main subject
2. **Thick branches** radiating from the central image, each representing a key theme
3. **A single key image or word** placed on each branch — never sentences

Each main branch then sprouts secondary and tertiary branches relating to associated themes.

## The radial structure — why it matters

Buzan's argument (Chapter 4 onwards): the brain associates radially, not linearly. A linear list forces a single reading order, suppressing the connections that don't fit the sequence. A radial structure preserves *all* the connections and makes the structural relationships visible.

For analyst work this matters when:

- The corpus has multiple equally-important themes (a list privileges the first one)
- Themes interact across the corpus (linear notes hide cross-references)
- The structure is genuinely hierarchical (themes → sub-themes → specifics)

## Construction sequence — Buzan's seven steps adapted for the engine

### Step 1 — Place the centre

Render the mind map's centre as the `root` of a Mermaid `mindmap`, or as the central node of a hand-drawn or tool-rendered diagram. Use a noun phrase. Pair with a unicode glyph if the deliverable supports them (📌 for project, ⚖ for legal, 🔍 for investigation, 🌍 for landscape, 💡 for synthesis).

### Step 2 — Main branches

Decide on the **basic ordered ideas (BOIs)** — Buzan's term for the major themes. Five to six is the typical count Buzan recommends: enough to cover the territory, few enough to remember.

For analyst work, BOI patterns:

- **Research question** → `Context | Stakeholders | Evidence | Gaps | Next moves`
- **Deliverable** → `Audience | Key messages | Evidence | Risks | Open questions`
- **Regulatory landscape** → `Statutes | Regulators | Case law | Guidance | Practice`
- **Pain-point taxonomy** → `Operational | Financial | Reputational | Regulatory | Strategic`
- **Cohort synthesis** → `Quotes | Statistics | Case studies | Patterns | Outliers`

The BOIs are the skeleton. Choose with care; the rest of the map hangs from them.

### Step 3 — Keywords on branches

One keyword per branch. The keyword constraint forces precision: it asks "what is *the* word for this?" rather than "what is everything I could say?"

Buzan: capital letters for keywords. Engine equivalent: clear, short noun-phrase labels in Mermaid `mindmap` syntax.

### Step 4 — Sub-branches

From each main branch, send out secondary-level shoots; from those, tertiary-level. Each sub-branch is one keyword or one short noun phrase.

Stopping rule: stop adding sub-branches when the next layer would be quoting evidence verbatim. Quotes belong in the corpus, not the map. The map points *to* the evidence.

### Step 5 — Build the next main branch

Buzan recommends working clockwise around the centre, but free-form is fine. The discipline is: complete each main branch's primary structure before moving to the next, then iterate.

### Step 6 — Move freely; fill gaps

Once the main branches are placed, move freely across the map adding sub-branches, filling gaps, and recognising connections. This is the cognitive payoff: connections that linear notes hide become visible.

### Step 7 — Add cross-links

Use arrows or curved lines to connect related items on different branches. Buzan: "Use emphasis, arrows and connecting lines to depict associations between different related topics."

In the engine's Mermaid output, cross-links live in a separate annotated block beneath the `mindmap` (Mermaid's `mindmap` syntax does not natively support cross-links). Format:

```
Cross-links:
- [Statutes::Privacy Act] ↔ [Case law::Smith v Republic] (statutory test applied)
- [Operational pain::Long approval cycle] ↔ [Regulatory pain::Multiple regulators] (root cause)
```

## What is *not* a mind map (Buzan, Chapter 3)

Buzan is firm: many things people call "mind maps" aren't. Things that look like mind maps but aren't:

- **Spider diagrams** — radial branches but no hierarchy, no colour-code, sentences on branches
- **Concept maps** — different intellectual heritage; nodes and labelled relationships, less radial
- **Org charts / hierarchy diagrams** — top-down rather than radial
- **Bubble diagrams** — clustering without structural rules
- **Linear outlines re-drawn radially** — the radial form is cosmetic; the underlying thinking is still linear

For the engine: when the audience expects a particular notation (org chart, ER diagram, BPMN), use that notation. The mind map is for *thinking* and *radial synthesis*. Do not relabel one as the other.

## Working size

A mind map should fit one page or one screen. If it's overflowing, that's diagnostic:

1. The BOIs are wrong — too many, or the wrong ones; restructure
2. The map is trying to do two jobs — split into two maps
3. The detail belongs in the corpus, not on the map — prune

## Iteration

A first-draft mind map is rarely the final one. Buzan: *"Take your Mind Mapping journey step by step."* Expect to:

- Re-cut the BOIs after the first pass reveals the real structure
- Move sub-branches to different main branches as relationships clarify
- Discover cross-links during the building, not at the end
- Compress a too-detailed branch by promoting its real content up a level

## Anti-patterns

- Writing sentences instead of keywords — defeats the precision discipline
- Choosing too many BOIs — Buzan's "5–6" is roughly correct; >8 means restructure
- Treating the first draft as final
- Using mind-map shape for content that is sequential or dynamic
- Skipping the central image / specific centre
- All branches in the same visual style — colour-coding (or class-coding in Mermaid) is part of the cognitive benefit
- Treating the mind map as the deliverable when the audience expects prose
- Adding branches to fill space (every branch must earn its place)
