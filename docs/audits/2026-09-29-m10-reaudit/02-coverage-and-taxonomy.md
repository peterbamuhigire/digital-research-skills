# 02 Coverage and taxonomy

**Taxonomy and structure: 48 / 100 (judged)**

## Structure as found

- The catalogue is flat: 59 folders directly under `skills/` with no group level. The router
  `SKILL.md` routes 16 intents to named primaries.
- `README.md` sets out seven workflow categories, but its table names only about 33 of the 59
  skills. The remaining skills belong to no declared group.
- `AGENTS.md` says the filesystem, not the README table, is the inventory. That is sound for
  discovery but leaves no maintained grouping.
- For scoring, the auditor assigned all 59 skills to eight working groups (see 03). Seven are the
  README categories. The eighth, *engineering and documentation imports*, collects skills with no
  research purpose.

## Named deficiencies

1. **Out-of-domain dilution (about 14 of 59 skills, 24 %).**
   - These seven have no research function:
     - `spec-architect`
     - `project-requirements`
     - `systems-process-requirements`
     - `doc-architect`
     - `update-claude-documentation`
     - `markdown-lint-cleanup`
     - `manual-guide`
   - `update-claude-documentation/SKILL.md:120` still carries a product-specific rule naming
     "pharmacy, localization" subdirectories.
   - Also in this set:
     - `capability-matrix`: a technology-stack lookup whose Validation column names design and
       engineering skills that do not exist in this engine.
     - `validation-contract`
     - `skill-safety-audit`
     - `skill-taxonomy-and-routing`
     - `skill-composition-standards`
     - `doctrine-spine`
     - `excel-spreadsheets`
   - These skills belong to, or duplicate, the dev engine.
2. **Cross-engine duplicates, declared but still present.** The union collision scan records the
   following cross-engine pairs at or above 0.75 involving this engine. All are declared as
   `canonical_owner` in `evals/routing/ownership.yaml`.

   | Pair | Cosine |
   |---|---:|
   | `validation-contract` with dev | 1.0 |
   | `ai-slop-audit` with dev | 0.826 |
   | `ai-slop-audit` with srs | 0.790 |
   | `excel-spreadsheets` with dev | 0.823 |

   Declaration keeps T2_clean at 1.0, but an identical skill in two engines remains a maintenance
   liability. The mirrored oracle 055 fails precisely on this tie. The dev engine's
   `skill-engine-audit` states that `skill-safety-audit` was retired and absorbed there; the
   research copy remains active.
3. **Unowned output types.**
   - Benchmarking and competitive study has no owning skill. No active SKILL.md mentions
     "benchmarking", "competitive intelligence" or "competitor analysis". The only asset is the
     35-line `examples/research-types/schema-d-comparative-benchmarking/README.md`.
   - Market sizing sits inside `quantitative-modelling`, which has one reference file and no
     sizing example.
4. **Stale companion names after consolidation.** About 100 companion-list mentions name 52 skills
   that are neither active skills nor local reference files. Examples:
   - `data-quality-assessment` (11 mentions)
   - `data-cleaning-pandas` (6)
   - `due-diligence-framework` (6)
   - `pearl-growing-iteration` (4; the content now lives in `academic-writing/references/pearl-growing.md`)
   - `due-diligence-report-architecture` (4)
   - `pi-report-writing` (3)

   `research-orchestration` routes to `data-visualization`, which lives in no local skill; it is a
   design-engine concern and is not labelled as cross-engine.
5. **Regional coverage imbalance.** Kenya and Uganda each have an academic-research skill and a
   legal overlay section. Tanzania, Rwanda, Burundi, South Sudan and the DRC appear only as a
   language caveat in the legal overlay. The standards register lists no regional statistical or
   legal repositories.
6. **Balance.** Communication and deliverables holds 12 skills, while the core source-discipline
   group holds five. The writing-and-formatting surface is larger than the verification surface in
   an engine whose declared purpose is verification.

## What works

- The router table is clear and short.
- Foundation skills are named and ordered: `source-evaluation`, evidence discipline and
  `anti-ai-slop`.
- `skill-writing` is correctly reduced to a pointer stub to the canonical dev skill, which is the
  right pattern for the other imports.
- Descriptions are "Use when" statements with explicit hand-offs, for example
  `source-evaluation` → `source-verification`.
- No within-engine pair reaches 0.75 in the collision scan.

## Proposed structure (P1)

- Keep a flat filesystem, but add a maintained group index, for example `skills/GROUPS.md`, that
  every skill appears in.
- Reduce the imports to pointer stubs or retire them. Target: about 45 research skills and at
  most 6 pointer stubs.
- Add `benchmarking-and-competitive-study`, and either split market sizing into
  `market-evidence-and-sizing` or harden it within `quantitative-modelling`.
