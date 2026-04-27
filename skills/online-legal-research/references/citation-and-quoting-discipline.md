# Citation and quoting discipline (legal sources)

**Date written:** 2026-04-27
**Drawn from:** Putman & Albright, *Legal Research, Analysis and Writing*, Part IV (Legal Writing), in particular Chapter 14 (Fundamentals of Writing) and Chapters 16–18 (memoranda and court briefs).

This reference governs how legal sources are cited and quoted in engine output. It is **method-only** — citation styles vary by jurisdiction (Bluebook in the US, OSCOLA in the UK and East African academic legal writing, jurisdiction-specific conventions for filings) — so this file teaches the *invariants* and points at the live style guide for any specific output.

## The invariants — every legal citation contains

1. **The authority's name** (case name, statute short title, regulation title, treaty name)
2. **The locating reference** (case neutral citation or reporter; statute section; regulation number; treaty article)
3. **The deciding body and date** (court and year for cases; legislature and year for statutes; signing/entry-into-force for treaties)
4. **The pinpoint** (paragraph for judgments; sub-section for statutes; specific article for treaties)
5. **The repository link or print reporter** so a reader can verify

Any citation missing one of these is incomplete and not safe to ship.

## Quoting rules

Putman's rules for quoting in legal writing — universally applicable regardless of jurisdiction:

1. **Quote the operative language only.** Long block quotes are usually a sign that the writer hasn't done the analysis.
2. **Reproduce verbatim.** No silent edits. Use brackets `[ ]` for substitutions and ellipses `...` for omissions; both must preserve the meaning.
3. **No alteration of emphasis without flagging.** "Emphasis added" or "emphasis in original" disclosed parenthetically.
4. **Pinpoint the quote.** Page or paragraph in the source, not just the case name.
5. **Quote primary, not secondary.** If a case quotes a statute, locate and cite the statute; do not quote the case quoting the statute as if the case were the source.
6. **Verify the quote exists.** Per evidence-discipline: every verbatim quote must reproduce text exactly as it appeared in the source.

## Paraphrase rules

A paraphrase that compresses or restates a holding still requires citation. Putman's discipline:

- The paraphrase must accurately capture the source's proposition
- The citation must follow the paraphrase, with pinpoint
- "(paraphrased)" can be used in informal output where that helps the reader
- A paraphrase may **not** invent qualifications, exceptions, or limits the source did not state

## Signal use (introductory citation signals)

Standard signals — common across legal citation systems:

| Signal | Meaning |
|---|---|
| (no signal) | The cited authority directly states the proposition |
| *See* | The authority supports the proposition by clear inference |
| *See, e.g.,* | The cited authority is one of several supporting examples |
| *Accord* | Other authorities in agreement; cite primary alongside |
| *Cf.* | Authority supports a different but analogous proposition |
| *But see* | Authority contradicts the proposition |
| *But cf.* | Authority is contrary by analogy |
| *Contra* | Authority directly contradicts |
| *See generally* | Authority provides background on the topic |

The signal must match the relationship between the proposition and the cited authority. Misusing *see* or *contra* is a credibility hit.

## Style-specific anchors (load before citing)

Pick the style by audience:

- **US output** — Bluebook (most common for academic and court work) or ALWD
- **UK / Commonwealth academic** — OSCOLA
- **East African academic** — typically OSCOLA or institution-specific (often a Harvard variant for non-law courses; see `kenya-academic-research` and `uganda-academic-research`)
- **East African court filings** — jurisdiction-specific practice rules (court rules of the relevant court; consult the court's practice direction)

The engine does not embed any one style's micro-rules — those rotate. The engine *does* enforce the invariants above.

## Confidentiality and attribution

Legal writing often involves client matters subject to privilege. The engine's discipline:

1. **Never reveal** confidential client identities in research output unless the user has confirmed clearance
2. **Anonymise** sample fact patterns (e.g., "the client" or "Mr X") unless the source is public
3. **Distinguish** the law from advice — research output describes what the law is; advice is the lawyer's province

## Common citation errors (Putman, Chapter 14, condensed)

- Citing a case without the deciding court (e.g., "Smith v. Jones (2019)" with no court) — reader cannot weigh authority
- Using "id." or short-form citation when the prior reference is more than a few sentences back
- Quoting from a syllabus or headnote instead of the judgment text
- Citing a statute by its popular name only without the section
- Listing many cases with no signal where the relationships differ
- Wrong jurisdiction abbreviation (e.g., "U.S." for a state case)
- Using "supra" / "infra" without unambiguous antecedent
- Citing an unreported case without its neutral citation or unique identifier

## Writing-process integration (Putman, Chapter 15)

Putman & Albright treat legal writing as a **process** — not one draft. The minimum cycle:

1. **Pre-writing** — research, IRAC outline, decide structure
2. **First draft** — write the analysis section before introduction
3. **Revision** — sentence-level: precision, brevity, signal accuracy
4. **Cite-check** — verify every cited authority, pinpoint, and quote against source
5. **Currency-check** — re-run citator on every authority (statutes amended? cases overruled?)
6. **Final read aloud** — catches voice and clarity issues a screen-read misses

The cite-check and currency-check are non-negotiable for the engine. Skipping either is malpractice-grade per evidence-discipline.

## Anti-patterns

- "(citation)" placeholders that survive into final output
- Quotes without page or paragraph pinpoints
- Bare URLs as citations — minimum is authority name + locating reference + URL
- Block-quoting an entire passage when a 12-word excerpt would do
- Pinpointing to a "page" in a paragraph-numbered judgment (use paragraphs)
- Statutes cited without revision/version date when amendments matter
- Pinpoints copied from another writer's secondary source without verifying against the primary
