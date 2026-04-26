# Meta-Initialization Decision Tree

## 1. Identify Research Type

Choose exactly one primary type:

- pain-point research
- single-cohort deep-dive
- market / industry landscape
- comparative / benchmarking
- social-media / sentiment research
- due diligence
- OSINT
- product research
- historical research
- trends research
- policy / regulatory research
- thesis
- paper
- dissertation
- essay

If the project spans multiple types, choose the type that determines the
evidence standard and output shape. Record secondary types in
`_context/project-profile.md`.

## 2. Select Methodology Mix

Map the primary type to methods:

| Research type | Default methods |
|---|---|
| pain-point research | cohort search, complaint mining, quote extraction, synthesis |
| market landscape | desk research, category mapping, competitor scan, trend analysis |
| due diligence | registry checks, adverse media, sanctions/PEP screening, source triangulation |
| OSINT | lawful open-source collection, provenance tracing, chronology construction |
| policy / regulatory | statute/regulation collection, case/source verification, comparative table |
| thesis/paper/dissertation | research design, literature review, methodology justification, citation audit |

## 3. Decide Primary-Research Need

Primary research is needed when:

- published sources do not answer the decision question
- stakeholder experience is central to the claim
- source coverage is biased toward institutions or vendors
- the output requires defensible qualitative evidence

Mark as `(gap)` if the need is likely but participants, ethics, or access are
not yet confirmed.

## 4. Select Output Family

Choose one or more:

- executive report
- proposal
- academic paper
- thesis/dissertation
- white paper
- book manuscript
- internal memo
- evidence dossier

Record each audience-output pairing in `_context/audience-output-matrix.md`.

## 5. Define Release Standard

A project is not release-ready until:

- required context is complete
- every source has a registry entry
- every load-bearing claim maps to one or more sources
- every direct quote maps to a source and location
- synthesis claims map back to claim ids
- output manifests define assembly order
- validation gates have no blocking findings
