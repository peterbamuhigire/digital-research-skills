# Reference — Ghost-Deck Pattern

**Source:** McKinsey internal practice. Documented in Rasiel, *The McKinsey Way* (1999), and reproduced widely in consulting-training material.

## The rule

Before opening any slide tool (PowerPoint, Keynote, Google Slides), draft the deck on paper or in markdown as a **ghost deck**: an ordered list of action titles with a one-line note on what each slide will show.

The ghost deck is "complete" when reading the action titles in sequence narrates the entire argument with no slide content needed. Only then design the slides.

## Why

- **Forces structure before design.** PowerPoint encourages the writer to design something pretty before deciding what it says. The ghost deck inverts this.
- **Cheap to revise.** Moving 12 action-title lines around takes 30 seconds. Moving 12 designed slides takes an hour.
- **Catches MECE failures early.** When the titles are written as a list, overlaps and gaps become visible. Hidden inside designed slides, they don't.
- **Catches skim-path failures early.** Reading the titles in sequence is the skim-path test. If the argument doesn't land at the ghost stage, no amount of design will save it.
- **Reader test before sunk-cost trap.** Show the ghost deck to a peer or a stand-in for the audience. Iterate before the design work begins.

## Structure of a ghost deck entry

Each entry has three parts:

```
SLIDE N. [Action title — complete declarative sentence stating the takeaway]
       [Chart family or visual: bar / line / pie / matrix / table / quote / map]
       [Source: pointer to the upstream research-corpus claim that grounds this]
```

Worked example for a slide:

```
SLIDE 4. Three new digital-first entrants now offer instant-bind motor cover at 22% below Acme's price.
       Chart: bar — 5 carriers × 3 product attributes (price, bind-time, distribution).
       Source: students/research/competitor-scan.md §3.2 (regulator filings + own-site checks, tier-1).
```

This is enough for the deck designer (or for the writer at design time) to build the slide without rethinking.

## The complete ghost-deck workflow

1. **Define the audience and the question.** Who reads this; what decision do they make?
2. **Write the governing thought.** One sentence. This is the title of the executive-summary slide (typically slide 2 after the cover).
3. **Decompose MECE.** Three groups under the governing thought. Each group becomes a section of the deck.
4. **Write the section action titles.** For each group, write one action title (the section divider) and the action titles of the supporting slides (the body).
5. **Skim-path test.** Read the section dividers and slide titles in order. Does the argument land?
6. **Add chart-family note + source pointer per slide.** Per the structure above.
7. **Peer review the ghost deck.** Show it to a stand-in audience. Revise.
8. **Now open the slide tool.** Build slides one at a time, each from its ghost-deck entry. Resist the urge to re-think structure; the structure is fixed.
9. **Final pass.** Read the designed deck against the ghost deck. Anything that drifted, restore.

## Standard deck shape (10–15 slides)

| Slide | Purpose |
|---|---|
| 1 | Cover |
| 2 | Executive summary (the governing thought + three sub-points + recommended action) |
| 3 | Agenda / how this deck unfolds |
| 4 | Section 1 divider (Group 1 action title) |
| 5–7 | Section 1 body (3 slides, each one fact group) |
| 8 | Section 2 divider |
| 9–11 | Section 2 body |
| 12 | Section 3 divider |
| 13–14 | Section 3 body |
| 15 | Recommendation slide (re-states the governing thought + clear next steps) |
| Appendix | Anything that didn't make the main deck but needs to be defendable on Q&A |

## Anti-patterns

- **Designing first.** The most common failure. Once a slide is designed, the writer protects it; structural changes become political even with oneself.
- **Chartjunk to fill the slide.** A slide with no message but a busy chart. The ghost-deck stage forces the writer to commit to a message; no message → no slide.
- **Ten-bullet "thought slide".** The slide that says everything and therefore nothing. Split into multiple slides, each with one message.
- **Appendix-as-dumping-ground.** The appendix is for material that strengthens the main story under questioning; not for material the writer couldn't bear to cut. If a slide is in the appendix, the writer must be able to say what question it answers.
- **Skipping the skim-path test.** The deck looks fine slide-by-slide; the argument doesn't land in sequence. This is the failure ghost-decking is designed to prevent.

## When NOT to use ghost-decking

- **Status updates / standing meeting decks.** Convention is fixed; structure is not the variable.
- **Highly designed marketing decks.** The visual brand is the message; ghost-decking still helps but the design pass is heavier.
- **Long-form reports rendered as PDF rather than slides.** Use the pyramid + action titles directly without the slide overhead.

## Companion patterns

- `references/pyramid-principle.md` — the ghost deck is a pyramid laid flat.
- `references/action-titles.md` — every ghost-deck entry leads with an action title.
- `references/zelazny-chart-selection.md` — the chart-family note in each entry uses Zelazny's families.
- `references/scqa-opener.md` — the executive-summary slide opens with a compressed SCQA.
