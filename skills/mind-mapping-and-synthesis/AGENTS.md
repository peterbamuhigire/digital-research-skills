# Agent operating notes — mind-mapping-and-synthesis

For Codex, Cursor, generic agents working in this skill.

## Load order

1. `SKILL.md` — entry, when to use, ten Laws of Mind Mapping
2. `references/mind-map-construction.md` for synthesis / taxonomy / brief-decomposition tasks
3. `references/study-and-recall-techniques.md` for analyst-learning tasks
4. `references/mermaid-mindmap-patterns.md` for Mermaid output
5. `source-evaluation/references/evidence-discipline.md` — applies to every claim placed on the map

## Mandatory disciplines

- One keyword per branch — never sentences
- 5–6 main branches (BOIs); restructure if more
- Specific centre — never a vague abstraction
- Cross-links explicit (in a prose block beneath Mermaid output, since Mermaid `mindmap` lacks cross-edges)
- Every fact on the map carries source attribution per evidence-discipline

## Refusal cases

- Will not build a mind map for sequential, dynamic, or temporal content (use the right tool instead)
- Will not ship a mind map as the final deliverable when the audience expects prose
- Will not place unsourced facts on the map

## Output expectations

- Mermaid `mindmap` block + cross-links prose block + (where useful) class styling
- For Word output: SVG/PNG export of the mindmap, with the Mermaid source preserved alongside in the markdown
- For learning artifacts: mind map + spaced-revision schedule
