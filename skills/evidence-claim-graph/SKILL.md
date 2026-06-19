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

- Source registry, extracted quotes, notes, claims, hypotheses, and gaps.
- Intended output family and audience.
- Evidence discipline from source evaluation.

## Workflow

1. Atomize sources into evidence items: one quote, statistic, observation, dataset field, or document fact per item.
2. Convert prose notes into explicit claims with scope, status, and source IDs.
3. Add warrants: why the evidence supports the claim.
4. Mark inferences and synthesis explicitly; never store them as raw facts.
5. Link contradictions and rival claims instead of smoothing them away.
6. Promote only verified, warranted claims into findings.
7. Preserve gaps as first-class nodes with owner, next search path, and decision impact.
8. Export registry-ready entries for source, claim, quote, and synthesis registries.

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

## Outputs

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

<!-- dual-compat-end -->

## Companion Skills

- `source-evaluation` supplies source tier and verification trail.
- `critical-reasoning-and-argument` supplies warrants and inference tests.
- `research-techniques` supplies gap analysis and synthesis methods.
- `knowledge-productization` reuses graph assets in monetizable outputs.
