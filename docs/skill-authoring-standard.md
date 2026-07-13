# Digital Research Skill Authoring Standard

This is the local, executable form of Peter Bamuhigire's July 2026 skill-writing and composition contract. The canonical source remains `C:\Users\Peter\.claude\skills`; this file records only the rules this engine enforces locally.

## Catalogue boundary

Active skills are filesystem-discovered `SKILL.md` files below `skills/`, excluding the `skills/proposal-skills` Git submodule because it is a separate engine. Skill templates live below `templates/` and never enter active-skill metrics. Do not use README tables as inventory.

## Entrypoint contract

Every active skill must meet all of these conditions:

- Frontmatter `name` matches its directory. `description` is one line, begins `Use when`, stays at or below 350 characters, and distinguishes the closest neighbour. Supported top-level keys are `name`, `description`, `license`, `allowed-tools`, and `metadata`.
- Portable metadata declares `portable: true` and `compatible_with: [claude-code, codex]`. Runner commands and tool names belong in adapters, not portable skill bodies.
- `Use When` and `Do Not Use When` give positive and negative triggers. The negative trigger names the nearest competing route.
- `Inputs` names each artefact, its source or provider, whether it is required, and the response to absence. A foundational skill may explicitly declare no upstream input.
- `Workflow` is ordered and includes a decision, a stop condition, validation, and recovery after a failed check.
- `Outputs` names each artefact, its consumer, and an observable acceptance condition. `Evidence Produced` records what proves the result.
- `Capability Contract` states the minimum capabilities and permission boundary. Audit, review, critique, analysis, and planning default to read-only. Editing, publishing, production mutation, destructive actions, spending, and certification claims need explicit authority.
- `Degraded Mode` returns the narrowest useful qualified result, exposes unavailable evidence or checks, and never changes `not assessed` into a pass.
- `Decision Rules` uses a domain-specific table that connects each choice to an action and the failure or risk avoided.
- `Quality Standards` is observable. `Anti-Patterns` contains at least five concrete mistakes paired with corrections. `Worked Example` demonstrates inputs, the decisive branch, output, and acceptance evidence.
- `References` links the local material required by the entrypoint directly. Each reference extracted during normalisation links back to `../SKILL.md`. A self-contained entrypoint says so explicitly.
- `SKILL.md` stays at or below 500 lines. Extract catalogues, schemas, case material, and background into references without moving routing, safety, decisions, workflow, degraded mode, outputs, or acceptance out of the entrypoint.

The [skill template](../templates/skill-template/SKILL.md) is the starting point. It is a template, not an active skill.

## Evidence discipline

Research skills inherit [evidence discipline](../skills/source-evaluation/references/evidence-discipline.md). Do not add a claim, statistic, quotation, name, case, statute, organisation, or URL unless it is traceable to a real source. Examples may use labelled placeholders or repository exemplars; they must not invent specifics.

## Mechanical gates

Run from the repository root:

```powershell
python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json
python -X utf8 scripts/routing_smoke_test.py
python -X utf8 scripts/validate_engine.py
```

The baseline is zero debt, not a waiver. Any finding, duplicate name, missing mandatory resource, active-count drift, template-count drift, or routing miss fails CI. After changing a skill, also run the canonical quick validator with the skill directory as its argument.

## Change procedure

1. Discover the current active catalogue from the filesystem and inspect neighbouring descriptions.
2. Preserve domain content; separate deterministic syntax repairs from domain judgement.
3. Update the skill, its directly linked references, and routing fixture when the trigger changes.
4. Run the local validator, routing smoke test, canonical quick validator, engine tests, and link checks.
5. Inspect line counts, diffs, generated caches, and human-facing prose before committing.
