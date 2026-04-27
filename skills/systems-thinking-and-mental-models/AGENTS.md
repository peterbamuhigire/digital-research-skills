# Agent operating notes — systems-thinking-and-mental-models

For Codex, Cursor, generic agents working in this skill.

## Load order

1. `SKILL.md` — router
2. The references file matching the question (one or two; rarely all four)
3. `source-evaluation/references/evidence-discipline.md` — applies to every claim regardless of which toolkit is in use

## Mandatory disciplines

- Systemigram: prose SoI description before the diagram. No crossing arrows; one source, one terminus.
- CLD: variables with polarity (`+`/`−`), closed loops labelled R or B, delays explicit. Diagram must predict observed behaviour.
- Mental-models catalog: applied as a discipline, not a slogan. Record which models were applied and what each produced.
- Decision-science: probability claims include base rate, reference class, and calibration note.

## Refusal cases

- Will not present a system map without the prose description that generated it
- Will not draw a causal loop diagram without specifying polarity on every arrow
- Will not ship a forecast without a base rate or stated reference class
- Will not invent loops, archetypes, or base rates to fit a desired conclusion

## Output expectations

- Systemigrams output as Mermaid `flowchart` or linked SVG, accompanied by SoI prose
- CLDs output as Mermaid graphs or annotated diagrams, accompanied by behaviour-over-time description
- Mental-models output names which models were applied
- Decision-science output names the calibration discipline used
