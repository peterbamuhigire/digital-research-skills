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

## Doctrine Intake Guidance

- Project type, audience, output family, cohorts, evidence risk, and decision stakes.
- Existing project context and registry state.

## Doctrine Method Detail

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

## Legacy Doctrine Pitfalls

- Jumping from source collection to polished report.
- Running report design before knowing the decision and evidence maturity.
- Treating source verification as optional.
- Productizing unverified claims.

## Doctrine Deliverable Detail

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

## Capability Contract

Routing and audit are read-only by default. Changing routers, skills, project state, publication, or release requires explicit authority.

## Degraded Mode

If project state or a mandatory gate is unavailable, return the verified prefix of the route and mark later gates blocked; never infer readiness.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Evidence is unverified | Hold synthesis | Unsupported claim |
| Output recommends action | Add reasoning and decision support | Advice without logic |
| Reusable product is proposed | Verify before productization | Scaling error |

## Doctrine Correction Examples

- Skipping verification; hold synthesis.
- Drafting before the decision is known; return to intake.
- Monetising unverified claims; block productization.
- Treating optional craft as a mandatory gate; justify route.
- Claiming release with missing evidence; mark blocked.

## Doctrine Scenario

A verified descriptive brief may skip forecasting, but cannot skip evidence discipline or source verification.

## Companion Skills

- `research-orchestration` runs the wave model.
- `source-verification` enforces verification before synthesis.
- `analytical-report-shapes` selects the final artifact.

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Project type, audience, decision, risk, output family | Brief and registry | Stop and request missing decision context |
| Gate status and active catalogue | Project evidence and filesystem | Return only the verified route prefix |

## Workflow

1. Establish evidence discipline, project design, audience, decision, and output.
2. Sequence collection, verification, reasoning, and applicable downstream gates.
3. Stop when a mandatory upstream gate fails or its evidence is unavailable.
4. Recover by repairing the failed gate and resuming from its checkpoint.
5. Release only when every included gate has an observable pass condition.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Mandatory route and gate crosswalk | Orchestrator and release reviewer | Every stage has an owner, predecessor, evidence output, stop condition, and acceptance gate |

## Anti-Patterns

- Skipping verification. **Fix:** hold synthesis until claims pass.
- Drafting before the decision. **Fix:** return to intake.
- Productising unverified claims. **Fix:** block reuse.
- Making every skill mandatory. **Fix:** justify the minimum route.
- Claiming release without evidence. **Fix:** mark the route blocked.

## Worked Example

A verified descriptive brief may omit forecasting, but still passes evidence discipline, verification, reasoning, output-shape, and release gates.
