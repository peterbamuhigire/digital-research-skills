# Systemigrams (Boardman & Sauser)

**Date written:** 2026-04-27
**Drawn from:** Boardman & Sauser, *Systemic Thinking — Building Maps for Worlds of Systems* (in particular the chapters on systemigram construction, the U.K. Rail System, the Bid/No-Bid Proposal, and the Intelligence Community case studies).

A systemigram is a directed graph that visualises the structure and behaviour of a complex system. It is constructed from a written **System of Interest (SoI) description** by extracting noun phrases as nodes and verb/preposition phrases as arrows. It is the engine's preferred notation when the question is *who does what to whom in this system, and why*.

## What a systemigram is — and is not

A systemigram **is**:

- A directed graph (nodes + arrows) with a clear mainstay flow
- Derived from a structured prose description of the system
- A *single* coherent picture: one source, one terminus, no crossing arrows
- An iteration on the system's owner / author understanding — built to be revised

A systemigram **is not**:

- A free-form mind map (those have a different purpose; see `mind-mapping-and-synthesis`)
- A flowchart of a process
- A causal loop diagram (those address dynamics; see `causal-loops-and-leverage-points.md`)
- A bare org chart, ER diagram, or BPMN diagram

## The starting move — the SoI description

Before drawing anything, write a **System of Interest description**: structured prose that names the system's purpose, its principal subject, its principal object, the major actors, and the most significant flows between them. Boardman's repeated insight: *the systemigram is only as good as its SoI description*. Spend disproportionate effort here.

Good SoI descriptions:

- Use **explicit noun phrases** — "the proposal team", "the customer's needs assessment process", not vague pronouns
- Use **active verbs** — "the team submits", "the process generates"
- Identify **one principal subject** (the doer that drives the mainstay)
- Identify **one principal object** (the recipient or terminal goal)
- Specify the **scope** — what is in the system and what is not
- State the **purpose** — what the system exists to do

## Construction rules (the laws of the systemigram)

Boardman & Sauser, paraphrased and condensed:

1. **Nodes are noun phrases** drawn from the SoI description. Each noun phrase appears at most once in the diagram. Everything semantically attached to that noun phrase from the prose connects through that single node.

2. **Arrows are verb / verb-phrase / sometimes prepositional phrases** from the SoI description. An arrow must reproduce a relationship that is in the prose.

3. **The principal subject sits at the top-left** corner of the diagram.

4. **The principal object sits at the bottom-right** corner.

5. **The mainstay** — the most significant thread between subject and object — runs diagonally, top-left to bottom-right.

6. **Arrows must not cross.** This rule is what makes systemigrams readable — and is the principal driver of redesign iterations.

7. **Containment nodes** are permitted: a node can contain other nodes (e.g., a "tender package" containing the priced cost-sheet, the technical proposal, and the schedule). Arrows can enter and leave the container or any contained node, provided the SoI prose supports the relationship.

8. **One source, one terminus.** Multiple start- or end-points are a sign the SoI description is not yet coherent.

9. **Failure is part of construction.** Boardman is explicit that good systemigrams emerge from many failed drafts. *"Be prepared for many, a great many, versions of what it is you are seeking to achieve to end up in the trash can."* Each failure reveals which connections actually need to be there.

## The construction loop

```
1. Write the SoI description (paragraph form)
2. Extract noun phrases       → candidate nodes
3. Extract verb / verb phrases → candidate arrows
4. Pick the principal subject and principal object
5. Place subject top-left, object bottom-right
6. Draw the mainstay diagonally between them
7. Add other nodes around the mainstay
8. Add arrows from the SoI description
9. If arrows cross — reorganise nodes, then redraw
10. If arrows still cross — return to the SoI description; the prose probably has a mismatch
11. Iterate until no arrows cross and the picture reads cleanly
12. Stress-test by reading the diagram as prose; does it match the SoI?
```

## Variants — multi-scene systemigrams

Boardman & Sauser's case studies (U.K. Rail System; Intelligence Community) demonstrate that a single SoI can be portrayed through **multiple systemigrams of the same system**, each highlighting a different aspect:

- **Mainstay** — the principal purpose flow
- **Corporate landscape** — actor and governance perspective
- **Follow the money** — economic flows
- **Way to go** — transformation / future-state perspective

For the engine's purposes: when one systemigram is becoming overloaded, split it into a series of complementary systemigrams of the same SoI, each emphasising a different theme. The mainstay stays consistent across all variants.

## When to use systemigrams in engine work

- **Regulatory landscape** mapping — actors (regulators, regulated entities, courts, civil society), flows (rule-making, enforcement, appeals, lobbying)
- **Stakeholder analysis** — who is connected to whom, by what relationship
- **Pain-point root-causing** at the system level — a shared pain point often emerges from a flow that is stuck or misdirected
- **Programme / project design** — how the proposed work will plug into the existing system
- **Organisational diagnosis** — where authority, information, and accountability flow in an organisation

## Output for the engine

Systemigrams are diagrams and ideally drawn in a tool that supports curved, non-crossing arrows. For the engine's markdown corpus, a systemigram is rendered either:

- As a Mermaid `flowchart LR` diagram with explicit positioning and minimal crossings (Mermaid is satisficing — true non-crossing layout often requires manual tools)
- As an SVG / PNG asset linked from the markdown
- As a textual SoI description plus a node-and-arrow list (when visual rendering is not available)

Always include the **SoI description** as prose alongside the diagram — the diagram is a compression, not a replacement.

## Anti-patterns

- Drawing the systemigram before writing the SoI description
- Replicating the same noun phrase as multiple nodes (each noun phrase is unique)
- Tolerating crossing arrows ("just this once") — they always indicate a real defect
- Multiple unconnected start/end points (the SoI description is incoherent)
- Confusing a flowchart with a systemigram (flowcharts are process; systemigrams are structure + flow)
- Treating the first draft as the answer
- Building a systemigram of a system the analyst doesn't understand prose-first — picture-first construction is unreliable
- Adding arrows that aren't supported by the SoI prose (the arrow must reproduce a relationship in the prose)
