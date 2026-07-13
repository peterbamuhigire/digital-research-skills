---
name: knowledge-mining
description: "Use when turning a corpus into reusable, monetizable, verifiable knowledge assets: entity-event-issue extraction, claim libraries, evidence maps, reusable briefs, ontology seeds, dossiers, and refresh cadences."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Knowledge Mining

<!-- dual-compat-start -->

## Use When

- Use when the goal is deep reusable knowledge, not just one report.
- Use after source verification and before knowledge productization.
- Use when building claim libraries, evidence maps, dossiers, reusable briefs, or refreshable intelligence assets.

## Do Not Use When

- The project is a one-off deliverable with no reuse path.
- The corpus has not yet passed verification.


## Knowledge Mining Required Context
- Verified sources, claim graph, audience needs, target products, and reuse constraints.
- Sensitivity, confidentiality, and commercial boundaries.


## Knowledge Mining Core Method Notes
1. Ingest the corpus by source, entity, event, issue, geography, and time.
2. Extract reusable claims and link them to evidence.
3. Build entity-event-issue maps.
4. Identify reusable frameworks, templates, visuals, and briefs.
5. Mark sensitivity and reuse limits.
6. Define refresh cadence and change triggers.
7. Hand the asset portfolio to productization.

## Quality Standards

- Every reusable asset keeps provenance.
- Reuse boundaries are explicit.
- Knowledge assets have buyers, users, or decisions attached.
- Refresh logic is defined for time-sensitive claims.


## Knowledge Mining Existing Failure Notes
- Treating knowledge mining as folder organization.
- Extracting insights without evidence links.
- Reusing client-sensitive knowledge as generic IP.
- Creating a knowledge base with no refresh trigger.


## Knowledge Mining Core Deliverables
- Knowledge asset inventory.
- Claim library.
- Entity-event-issue map.
- Reusable brief set.
- Refresh cadence.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Correctness | Claim library | Markdown/YAML | Claim, source IDs, reuse status |
| Release evidence | Asset inventory | Markdown table | Asset, audience, provenance, sensitivity |

## References

- Load `references/knowledge-mining-workflow.md` for extraction and asset rules.

## Inputs

| Artefact | Source or provider | Requirement | If absent |
|---|---|---|---|
| Verified corpus and source manifest | research workflow | required | Produce only a mining plan if the corpus is unavailable |

## Capability contract

Read and corpus-search access are required for extraction. Updating a claim library or ontology needs explicit authority; original sources and their identifiers must not be altered.

## Degraded mode

If the corpus or extraction tooling is unavailable, return a qualified mining schema and gap register, with identity resolution and coverage checks marked unassessed.

## Decision rules

| Choice | Action | Failure avoided |
|---|---|---|
| Claim lacks direct support | Keep as gap or inference | Fabricated knowledge asset |


## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Claim library, entity/event/issue register, and refresh notes | knowledge-productization and synthesis | Every asset traces to evidence and records gaps |


## Knowledge Mining Evidence Notes 1
- Preserve extraction provenance, entity-resolution decisions, contradiction status, refresh dates, and coverage gaps.

## Worked example

Extract one organisation mention as an entity node, connect dated actions as events, and keep conflicting accounts as separate claims until verified.

<!-- dual-compat-end -->

## Companion Skills

- `evidence-claim-graph` supplies the traceable substrate.
- `knowledge-productization` packages assets into offers.
- `analytical-report-shapes` chooses reusable output shapes.


## Workflow
1. Define the reusable asset types and extraction schema.
2. Extract entities, events, issues, and claims with source identifiers.
3. Stop promotion when a claim lacks verified evidence or conflicts remain unresolved.
4. Validate the register; recover by preserving the item as a gap or labelled inference.


## Knowledge Mining Evidence Notes 2
| Evidence | Consumer | Acceptance |
|---|---|---|
| Mining provenance and QA register | Knowledge-productization and synthesis | Every asset has evidence links, status, and refresh notes |


## Anti-Patterns
- Extracting claims without source identifiers. Fix: attach provenance at capture.
- Collapsing conflicting claims. Fix: preserve both and record the contradiction.
- Treating an entity mention as verified identity. Fix: resolve and corroborate it.
- Creating assets with no downstream use. Fix: name the consumer and decision.
- Hiding stale or missing evidence. Fix: record refresh status and gaps.

## Reference Index

- [Knowledge-mining workflow](references/knowledge-mining-workflow.md)
