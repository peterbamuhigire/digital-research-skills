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

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Live active-skill inventory, candidate skill/reference, and neighbouring descriptions | Filesystem and change request | Stop taxonomy changes and rediscover the catalogue. |
| Routing fixtures and alias/migration records | Repository | Mark collision and compatibility checks unassessed. |

## Capability Contract

Taxonomy analysis defaults to read-only. Renaming, moving, deactivating, deleting, or changing routers and aliases requires explicit repository authority and migration evidence.

## Degraded Mode

If the live catalogue, neighbouring descriptions, or routing fixtures are unavailable, return candidate placement and collision risks without changing taxonomy. Do not declare a route collision-free.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Capability has distinct triggers and workflow | Keep or create a skill | Hidden specialist behaviour |
| Material only deepens an existing workflow | Store it as a linked reference | Catalogue fragmentation |
| Names or triggers overlap | Tighten descriptions and negative triggers | Ambiguous routing |

## Preliminary Taxonomy Corrections

- Trusting a cached catalogue. Fix: discover SKILL.md files.
- Naming by technology buzzword. Fix: name the user intent.
- Deleting an alias without migration evidence. Fix: preserve the route.
- Counting references as active skills. Fix: separate roots.
- Resolving collision by broadening both descriptions. Fix: distinguish neighbours.

## Worked Example

If two skills both claim research planning, reserve wave and cohort planning for research-orchestration and formal method selection for research-design, then add fixtures for both boundaries.

<!-- dual-compat-start -->

## Use When

- Use when a router mentions a capability that may not exist as a top-level skill.
- Use when adding, renaming, merging, or splitting research skills.
- Use when aliases like verification, gap analysis, or synthesis create ambiguity.

## Do Not Use When

- The request only needs the current task executed.
- A skill name is already canonical and no routing change is involved.

## Taxonomy Source Requirements

- Current skill folders, router references, and requested capability.
- Evidence of overlapping skills or missing standalone folders.

## Taxonomy Method Summary

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

## Legacy Taxonomy Warnings

- Creating a new skill for every checklist.
- Hiding major workflows inside references that routers call as top-level skills.
- Letting several names refer to the same operation.

## Initial Taxonomy Deliverables

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

## Workflow

1. Discover the live catalogue and candidate capability; stop if active roots are unclear.
2. Compare closest neighbours, aliases, triggers, workflows, and references.
3. Decide whether the material is a skill, reference, alias, or existing route.
4. Test positive, negative, and collision prompts.
5. Recover from failed routing by narrowing names/descriptions and rerunning fixtures.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Taxonomy decision and routing changes | Maintainer and router | Decision cites neighbours, migration impact, and passing fixtures. |

## Anti-Patterns

- Trusting a cached catalogue. Fix: discover files.
- Naming by buzzword. Fix: name intent.
- Removing aliases without migration. Fix: preserve routes.
- Counting references as skills. Fix: separate roots.
- Broadening collisions. Fix: distinguish neighbours.
