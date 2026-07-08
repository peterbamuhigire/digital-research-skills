# Pathing Model - Engine vs Examples vs Active Projects

Last verified: 2026-07-08

This file defines what belongs in the reusable engine, what belongs in sanitized examples, and what belongs in active project workspaces. It closes the audit gap where project workspaces, generated artefacts, and engine doctrine blurred together.

## Classification rules

| Path family | Belongs here | Does not belong here | Release rule |
|---|---|---|---|
| `skills/` | Reusable skill entrypoints, references, and templates that can be applied across projects | Client-specific findings, one-off notes, raw source dumps | Every `SKILL.md` needs `name` and `description` frontmatter |
| `docs/source-registers/` | Dated standards, volatile-source registers, review cadence, official-source links | Undated web clippings or unverified scraped lists | Every volatile item needs last-verified, reviewer, and next-review fields |
| `docs/quality-gates/` | Release-blocking QA gates, validation protocols, scoring rules | Draft feedback on one project | Gates must state pass/fail criteria |
| `docs/world-class-exemplars/` | Benchmark-quality reusable exemplars and running example assets | Live client work | Examples must be sanitized and evidence-marked |
| `templates/` | Blank-fill templates reusable across deliverables | Completed examples | No placeholders that hide required evidence fields |
| `examples/` | Sanitized complete workflows with context, wave logs, evidence table, final output, gate verdict | Current or confidential projects | Each example must disclose fabricated sample names and unverifiable values |
| `tools/` | Runtime utilities, validators, dashboards, generators | Project-specific scripts that embed a client path | Tools must accept explicit input/output paths |
| `tests/` | Fixtures, negative examples, deterministic checks | Live project registries | Tests must be runnable without secrets |
| `projects/` | Optional local workspaces for active research | Reusable doctrine | Excluded from engine scoring unless promoted to `examples/` |

## Empty directory rule

An empty directory is allowed only when it is one of these:

- A documented future extension point with a `README.md` explaining the contract.
- A generated-output directory intentionally kept empty by a project scaffold.
- A cache directory excluded from engine scoring.

Otherwise the directory must be removed or converted into an explicit example/template.

## Validation contract

A validator should flag:

- `skills/**/SKILL.md` without `name` or `description` frontmatter.
- Any `projects/**` path cited from a skill as reusable doctrine.
- Empty directories outside `projects/`, caches, or documented extension points.
- Any example missing `context`, `wave-log`, `evidence-table`, `final-output`, or `gate-verdict`.
- Any compliance-sensitive reference missing `Last verified`.

## Promotion path

1. Active work begins under `projects/<project-id>/`.
2. When the work becomes reusable, remove confidential material and move the pattern to `examples/<family>/<example-id>/`.
3. If the pattern becomes a repeatable blank-fill asset, extract it to `templates/`.
4. If the pattern becomes a rule or standard, encode it under `skills/<skill>/references/` or `docs/quality-gates/`.

## Running example placement

The engine-wide running example is stored at `docs/world-class-exemplars/running-example.md`. Sub-skills should reference it rather than duplicating long background text.
