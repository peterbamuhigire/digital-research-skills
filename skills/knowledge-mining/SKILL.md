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

## Required Inputs

- Verified sources, claim graph, audience needs, target products, and reuse constraints.
- Sensitivity, confidentiality, and commercial boundaries.

## Workflow

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

## Anti-Patterns

- Treating knowledge mining as folder organization.
- Extracting insights without evidence links.
- Reusing client-sensitive knowledge as generic IP.
- Creating a knowledge base with no refresh trigger.

## Outputs

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

<!-- dual-compat-end -->

## Companion Skills

- `evidence-claim-graph` supplies the traceable substrate.
- `knowledge-productization` packages assets into offers.
- `analytical-report-shapes` chooses reusable output shapes.
