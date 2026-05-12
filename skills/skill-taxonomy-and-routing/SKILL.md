---
name: skill-taxonomy-and-routing
description: Use when normalizing skill names, resolving whether a capability should be a standalone skill or a reference file, updating routers, removing alias drift, or auditing the repository's research skill taxonomy.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Skill Taxonomy And Routing

<!-- dual-compat-start -->

## Use When

- Use when a router mentions a capability that may not exist as a top-level skill.
- Use when adding, renaming, merging, or splitting research skills.
- Use when aliases like verification, gap analysis, or synthesis create ambiguity.

## Do Not Use When

- The request only needs the current task executed.
- A skill name is already canonical and no routing change is involved.

## Required Inputs

- Current skill folders, router references, and requested capability.
- Evidence of overlapping skills or missing standalone folders.

## Workflow

1. Inventory top-level skill names.
2. Inventory router mentions and companion-skill references.
3. Classify each capability as standalone skill, reference under a skill, alias, deprecated name, or planned gap.
4. Normalize routers to point to canonical names.
5. Add alias notes only when they prevent future confusion.
6. Do not create a new skill when a reference file under an existing skill is enough.

## Quality Standards

- Each skill has a single reason to exist.
- Router rows distinguish top-level skills from reference files.
- Deprecated names have replacements.
- Taxonomy changes reduce ambiguity rather than increase surface area.

## Anti-Patterns

- Creating a new skill for every checklist.
- Hiding major workflows inside references that routers call as top-level skills.
- Letting several names refer to the same operation.

## Outputs

- Canonical skill map.
- Alias/deprecation register.
- Reference-vs-skill decision.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Operability | Canonical skill map | Markdown table | Capability, canonical skill, aliases |
| Release evidence | Routing audit | Markdown table | Router mention and correction |

## References

- Load `references/canonical-skill-map.md` for taxonomy decisions.

<!-- dual-compat-end -->

## Companion Skills

- `skill-writing` governs skill authoring.
- `doctrine-spine` governs operating order.
