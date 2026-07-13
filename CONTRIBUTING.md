# Contributing

Changes to this engine must preserve evidence discipline and pass the zero-debt skill contract.

## Skill changes

Start from [the local authoring standard](docs/skill-authoring-standard.md) and [skill template](templates/skill-template/SKILL.md). Read the target skill and its directly linked references before editing. Compare the nearest neighbours so the positive and negative triggers remain distinct. Do not edit the `skills/proposal-skills` submodule as part of this engine.

Add or update routing fixtures for trigger changes. Fixtures must cover the positive route, a negative or neighbouring route, limited capabilities, and a failure or stop path where applicable.

## Required checks

```powershell
python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json
python -X utf8 scripts/routing_smoke_test.py
python -X utf8 scripts/validate_engine.py
python -X utf8 C:\Users\Peter\.claude\skills\skills\sdlc-meta\skill-writing\scripts\quick_validate.py <skill-directory>
git diff --check
```

Run relevant syntax, link, unit, render, or domain checks as well. A check that cannot run is `not assessed`, not passed.

## Release procedure

1. Fetch the remote and confirm the branch is not behind `origin/main`.
2. Run all required checks and inspect the complete diff.
3. Remove generated caches and stage only intended files.
4. Review the staged statistics and representative skill, validator, fixture, and documentation diffs.
5. Commit once and push without force. Verify the local and remote commit identifiers match.
