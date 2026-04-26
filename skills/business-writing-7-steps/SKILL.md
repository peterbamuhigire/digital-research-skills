---
name: business-writing-7-steps
description: Use as the engine's general business-writing process — encodes Charles Maxwell's 7-Step Writing Process for reports, proposals, email, blogs, and web content (Identify Readers & Purpose · Collect · Brainstorm · Organize · Draft · Revise · Proof).
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Business Writing — 7 Steps (Maxwell)

Encodes Charles Maxwell's *7 Steps to Better Writing: How to write better reports, proposals, email, blogs, and web content* (Towering Skills, 2020) as the engine's default workflow for any non-academic prose artifact. Pair with `writing-that-works` for principles and `reports-proposals-craft` for structural depth.

## The 7-step process

| Step | Name | Goal | Artifact produced | Gate to next step |
|---|---|---|---|---|
| 1 | Identify Readers & Purpose | Know who and why | Reader-purpose statement | Audience and purpose are concrete and named |
| 2 | Collect Information | Gather raw material | Source dossier with annotations | Coverage of every claim you intend to make |
| 3 | Brainstorm | Generate every relevant idea | Unfiltered idea list | List exhausted; no self-editing yet |
| 4 | Organize | Build the structure | Outline (skeleton + section logic) | Outline survives a one-line-per-section read |
| 5 | Draft | Convert outline to prose | First full draft | Whole document drafted, even if rough |
| 6 | Revise | Improve content and structure | Revised draft after multi-pass review | All passes complete; structural issues resolved |
| 7 | Proof | Eliminate mechanical errors | Shippable artifact | Zero typos, formatting, link, or fact errors |

**Hard rule:** never skip a step; never collapse two steps into one (especially Steps 6 and 7 — revision is structural and substantive; proofing is mechanical).

## Step 1 — Identify Readers & Purpose

- Name primary, secondary, tertiary readers separately.
- For each: role, decision they make, knowledge level, attitude (friendly / neutral / hostile), preferred channel.
- State the **purpose** as a single sentence: *what should the reader think, feel, and do after reading?*
- If multiple readers conflict, pick the **decision-maker** as primary and write to them; serve the others with structure (executive summary, appendices, callouts) rather than tone.

Common Step-1 failures: writing for self, writing for the writer's manager, picking the gatekeeper as primary reader.

## Step 2 — Collect Information

- Build a **source dossier** with: source, date accessed, the specific claim it supports, your assessment of credibility.
- Triangulate any load-bearing fact across at least two independent sources.
- Capture more than you will use — pruning is cheaper than re-research.
- Mark every borrowed phrase verbatim with its source at capture time, not draft time. (Engine link: pair with `source-synthesis-craft` Trzeciak source-away rule.)

## Step 3 — Brainstorm

- List every possible point — *no self-censoring*.
- Push for 15–20 candidate items even when 7 will ship.
- Use techniques: free-listing, opposites ("what if the reverse were true?"), boundary-pushing ("could that be two ideas?"), preconceived-notion challenge ("what myth would this kill?").
- Stop when the list saturates, then move on. Do not select yet.

## Step 4 — Organize

- Pick the **structural pattern** that fits the purpose:
  - Chronological (events, processes)
  - Spatial (geography, layouts)
  - Comparison/contrast (alternatives evaluation)
  - Cause/effect (problem → impact)
  - Order of importance (recommendation lead)
  - Problem/solution (proposals, white papers)
- Build the outline as **descriptive headings + one-line per section**.
- Read the outline alone — should narrate the whole document.
- Get sign-off on the outline before drafting (saves 60 %+ of revision pain).

## Step 5 — Draft

- **Write fast.** First-draft drafting is generative; do not edit while drafting.
- Draft in **section-sized sittings** to preserve voice within a section.
- Leave placeholders (`[STAT TK]`, `[QUOTE TK]`) for missing facts; do not stop to look up.
- Default to active voice, short sentences, plain words — Step 6 polishes; Step 5 commits prose to paper.

## Step 6 — Revise

Multi-pass revision in fixed order:

1. **Structure pass** — does the outline still hold? Move sections, cut entire blocks, merge duplication.
2. **Paragraph pass** — first sentence = topic sentence; one idea per paragraph; transitions explicit.
3. **Sentence pass** — average length, active voice, parallelism, clarity.
4. **Word pass** — strike empty modifiers, replace abstract with concrete, kill jargon.

Avoid combining passes — combining is what produces "rewriting in circles."

## Step 7 — Proof

- **Mechanical only** — typos, spelling, grammar, punctuation, formatting, page breaks, link checks, cross-references, table of contents regeneration, filename and metadata.
- Read on paper, out loud, or backwards paragraph-by-paragraph — screen-reading misses ~30 % of typos.
- Run through tools (spell, grammar, link checker) but **never trust them as final**.
- Two human eyes minimum on anything that ships externally.

## Channel overlays — how the 7 steps shift

| Channel | Step 1 emphasis | Step 4 default | Step 5 length | Step 6 priority |
|---|---|---|---|---|
| **Email** | One reader, one ask | Inverted pyramid (ask → context) | ≤200 words; subject line carries the verb | Subject line and first sentence |
| **Report** | Decider + influencers grid | SCQA + decimal headings | Per `reports-proposals-craft` ranges | Exec summary stand-alone |
| **Proposal** | Buyer's silent objections | Situation → approach → deliverables → price | 8–25 pages | Risk and pricing precision |
| **Blog post** | Reader's one Googleable question | Hook → problem → solution → CTA | 800–2,000 words | Subhead scannability |
| **Web copy** | Visitor's intent in 3 seconds | F-pattern, value above the fold | ≤400 words / page | Microcopy, CTA visibility |

## Sentence- and paragraph-level rules

- **Active voice default.**
- **One idea per paragraph; one idea per sentence.**
- **Verb-first energy** — strong verb in subject's slot.
- **Parallel structure** in lists.
- **Signposts** at section boundaries ("First …" "However …" "Therefore …").
- **Sentence length variation** — short sentences punch; long sentences explain.
- **No hedge stacks** — choose one qualifier or none.
- **No throat-clearing** — strike "It is important to note that," "In order to."

## Anti-patterns

- Collapsing Step 1 into "the manager will read it."
- Drafting before outlining (Step 4 skipped).
- Editing while drafting (Step 5 corrupted with Step 6).
- Combining revision passes (rewriting in circles).
- Skipping the structural pass and polishing prose that should be cut.
- Treating proof (Step 7) as revision; missing typos and link rot.
- Running the spell-checker as the only proof pass.
- Writing email as a memo (no ask, paragraphs of context).
- Writing web copy as a report (walls of text, no scannability).
- One pass through, ship — no re-reading.

## Reusable 7-Step Checklist

- [ ] Step 1 — Reader profile and purpose sentence written.
- [ ] Step 2 — Source dossier complete; every claim has a source.
- [ ] Step 3 — Brainstorm exhausted; 15+ candidate items captured.
- [ ] Step 4 — Outline approved; one-line-per-section reads as the whole document.
- [ ] Step 5 — Full first draft committed; placeholders marked.
- [ ] Step 6 — Four passes (structure, paragraph, sentence, word) completed separately.
- [ ] Step 7 — Mechanical pass on paper / out loud / backwards; two human eyes; tools run but not trusted.

## Quotable rules

1. Identify your reader and purpose before you write a word.
2. Collect more than you can use; cut what you do not.
3. Brainstorm without judging; judge without brainstorming.
4. Outline until the document is already written in headings.
5. Draft fast, edit later — never both at once.
6. Revise in passes; do not combine them.
7. Proof on paper. Trust no tool. Two eyes minimum.

## See also

- `writing-that-works` — Roman/Raphaelson principles
- `reports-proposals-craft` — structural templates
- `white-paper-craft` — long-form persuasion
- `source-synthesis-craft` — note-card discipline
