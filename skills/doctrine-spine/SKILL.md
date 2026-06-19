---
name: doctrine-spine
description: "Use when defining or auditing the mandatory operating sequence for the research engine: evidence discipline, research design, collection, verification, reasoning, tradecraft, calibration, decision support, report shape, productization, and export."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Doctrine Spine

<!-- dual-compat-start -->

## Use When

- Use at project start, engine audits, skill routing reviews, and major workflow redesigns.
- Use when deciding which skills must run and in what order.
- Use when the engine risks becoming a loose library rather than an operating system.

## Do Not Use When

- A small task already has a prescribed single-skill workflow.
- The user asks for a narrow source check or code edit.

## Required Inputs

- Project type, audience, output family, cohorts, evidence risk, and decision stakes.
- Existing project context and registry state.

## Workflow

1. Start with evidence discipline and source evaluation.
2. Define research design, cohorts, scope, and outputs.
3. Run collection waves and preserve sources.
4. Verify sources, claims, quotes, and gaps.
5. Build evidence-claim graph.
6. Run critical reasoning and analytic tradecraft.
7. Add calibration where forecasts or risk calls exist.
8. Add decision support where the output recommends action.
9. Select report shape and executive communication style.
10. Productize reusable knowledge only after verification.
11. Export with validation and release evidence.

## Quality Standards

- Mandatory order is explicit.
- No synthesis occurs before verification.
- No recommendation occurs before reasoning and tradecraft checks.
- No monetization claim outruns the evidence base.

## Anti-Patterns

- Jumping from source collection to polished report.
- Running report design before knowing the decision and evidence maturity.
- Treating source verification as optional.
- Productizing unverified claims.

## Outputs

- Mandatory skill route.
- Wave-to-gate crosswalk.
- Release readiness checklist.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Operability | Doctrine route | Markdown checklist | Skill order and gate order |
| Release evidence | Wave-to-gate crosswalk | Markdown table | Wave, output, validation gate |

## References

- Load `references/research-operating-sequence.md` for the canonical sequence and crosswalk.

<!-- dual-compat-end -->

## Companion Skills

- `research-orchestration` runs the wave model.
- `source-verification` enforces verification before synthesis.
- `analytical-report-shapes` selects the final artifact.
