# Agent operating notes — online-legal-research

For Codex, Cursor, generic agents working in this skill.

## Load order

1. `source-evaluation/references/evidence-discipline.md` (universal floor)
2. `SKILL.md`
3. The references file matching the question (see router in `SKILL.md`)
4. `references/east-african-overlay.md` if Uganda/Kenya/EAC work

## Mandatory disciplines

- Cite primary authority before secondary
- Run citator (Shepard's, KeyCite, or manual) on every case before quoting
- Verify statute is in force and quote the version in force on the relevant date
- Pinpoint to paragraph (judgments) or section (statutes)
- Apply IRAC; include counter-analysis
- Invariant citation fields: name, locating reference, court+date, pinpoint, repository link

## Refusal cases

- Will not invent a case name, docket number, statute section, or repository URL
- Will not assert a foreign-jurisdiction case is binding in an East African brief
- Will not quote from a syllabus or headnote as if it were the judgment
- Will not skip currency-checking to save time

## Sub-agent boilerplate

Embed in every sub-agent brief:

```
HARD CONSTRAINT — NO HALLUCINATION:
- Do NOT invent statistics, names, organisations, court cases, statutes, or URLs.
- Cite every numeric claim and every direct quote at the point it appears.
- If you cannot find a source for a fact, mark it as a "gap" — do not fabricate filler.
- For any claim you assemble from multiple sources, mark it "(synthesis)".
- For any inference, mark it "(inference)".
- Verbatim quotes must reproduce text exactly as it appeared in the source — no creative editing.

JURISDICTION CONSTRAINT:
- Treat [jurisdiction] courts/statutes as the only mandatory authority.
- Other-jurisdiction material is persuasive at most — flag with "(persuasive)".
- Verify every cited case on [KenyaLaw / ULII / EACJ / specified repository] before quoting.
- Verify currency: is the statute amended? is the case overruled, reversed, or distinguished?
- Pinpoint cite to paragraph (judgments) or section (statutes), never a generic page.
- Provide a verifiable URL (with archive snapshot) for every authority.
```
