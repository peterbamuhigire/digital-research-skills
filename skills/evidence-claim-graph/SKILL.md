---
name: evidence-claim-graph
description: Use when research must become a traceable evidence-to-claim knowledge graph rather than loose notes. Encodes source, evidence, claim, warrant, inference, synthesis, gap, contradiction, and finding nodes with registry-ready relationships.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Evidence Claim Graph

<!-- dual-compat-start -->

## Use When

- Use when a project needs reusable, auditable knowledge rather than a one-off narrative.
- Use before synthesis, report generation, claim verification, or productization.
- Use when multiple agents contribute evidence and the orchestrator must merge without losing provenance.

## Do Not Use When

- The task is a single fact lookup with no downstream reuse.
- The corpus is too immature; run source collection and evaluation first.


## Required Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Source registry, extracted quotes, notes, claims, hypotheses, and gaps | Research project | Stop and record a provenance gap |
| Intended output family and audience | Research brief | Narrow the graph scope |
| Evidence discipline from source evaluation | Source-evaluation skill | Stop claim promotion |


## Workflow
1. Atomize sources into evidence items: one quote, statistic, observation, dataset field, or document fact per item.
2. Convert prose notes into explicit claims with scope, status, and source IDs.
3. Add warrants: why the evidence supports the claim.
4. Mark inferences and synthesis explicitly; never store them as raw facts.
5. Link contradictions and rival claims instead of smoothing them away.
6. Promote only verified, warranted claims into findings.
7. Preserve gaps as first-class nodes with owner, next search path, and decision impact.
8. Export registry-ready entries for source, claim, quote, and synthesis registries.
9. Stop promotion when provenance, support, or relationship validation is missing.
10. Recover by demoting unsupported propositions to explicit gaps and retaining the failed evidence trail.

## Learning and experiment nodes

For a process or product improvement, add explicit `hypothesis`, `experiment`, `measurement`, and `learning` records linked to the affected source, claim, gap, or finding. A learning record must state the baseline, guardrail, result, uncertainty, failed-path result, and standardisation decision. Do not promote an experiment result to a general claim without a source or a clearly labelled inference.

## Quality Standards

- Every finding traces to claims, and every claim traces to source IDs.
- Claims carry status: untested, supported, contested, contradicted, synthesis, inference, retired.
- Contradictions survive into synthesis until resolved.
- The graph is useful for both verification and reuse.

## Anti-Patterns

- Paragraph-level source dumps with no claim extraction.
- Findings with no warrant.
- Synthesis that hides which claims were combined.
- Deleting contradictory evidence because it complicates the story.
- Treating gaps as failures instead of research objects.


## Evidence Claim Graph Core Deliverables
- Evidence-claim graph table.
- Claim register rows.
- Contradiction map.
- Gap register.
- Finding promotion log.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Correctness | Claim graph | Markdown/YAML | Claim IDs linked to source IDs and warrants |
| Release evidence | Promotion log | Markdown table | Claim promoted to finding with verifier/date |

## References

- Load `references/graph-schema.md` for node and edge types.
- Load `references/claim-promotion-gate.md` before synthesis or final drafting.

## Graph storage inputs

| Artefact | Source or provider | Requirement | If absent |
|---|---|---|---|
| Verified source register | source-evaluation and source-verification | required | Stop and record a gap if provenance is absent |

## Capability contract

Read and graph-search access are required to resolve node provenance. Graph mutation needs explicit authority; source records remain immutable, and publication waits for relationship validation.

## Degraded mode

If graph storage or validation is unavailable, return a qualified node-and-edge draft, mark integrity checks unassessed, and retain unsupported propositions as gaps.

## Decision rules

| Choice | Action | Failure avoided |
|---|---|---|
| Evidence supports wording directly | Link evidence to claim | Unsupported promotion |


## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Evidence-claim graph | synthesis and report builders | Every claim node has source or explicit inference/synthesis status |


## Evidence Claim Graph Evidence Notes 1
- Preserve node identifiers, source locators, promotion decisions, contradictions, and the graph-integrity result.

## Worked example

A paragraph that combines two verified sources becomes a synthesis node linked to both evidence nodes; an unresolved discrepancy becomes a contradiction node, not a finding.

<!-- dual-compat-end -->

## Companion Skills

- `source-evaluation` supplies source tier and verification trail.
- `critical-reasoning-and-argument` supplies warrants and inference tests.
- `research-techniques` supplies gap analysis and synthesis methods.
- `knowledge-productization` reuses graph assets in monetizable outputs.


## Graph export workflow
1. Register sources and evidence before creating claims.
2. Link warrants, inference, synthesis, gaps, and contradictions explicitly.
3. Stop claim promotion when provenance or support is absent.
4. Validate graph integrity; recover by demoting unsupported claims to gaps.


## Evidence Claim Graph Evidence Notes 2
| Evidence | Consumer | Acceptance |
|---|---|---|
| Graph validation record | Synthesis and release review | Provenance, gap status, and relationship checks are recorded |

## Reference Index

- [Graph schema](references/graph-schema.md)
- [Claim promotion gate](references/claim-promotion-gate.md)
