---
name: source-verification
description: Use when a research project must verify sources, URLs, quotes, statistics, claim-source links, archive snapshots, registry completeness, and release readiness after source evaluation and before synthesis or publication.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Source Verification

<!-- dual-compat-start -->

## Use When

- Use after research waves and before synthesis, drafting, export, or release.
- Use when checking quotes, statistics, URLs, source registries, claim registries, archive links, and citation drift.
- Use when a sub-agent output contains sourced material that must be accepted, rejected, or quarantined.

## Do Not Use When

- The task is initial source quality assessment; use `source-evaluation` first.
- The output contains no source-backed claims.

## Required Inputs

- Source registry, claim registry, quote registry, synthesis map, and draft output.
- Source files, URLs, document locators, and access dates.
- Any source-evaluation notes, credibility tiers, and verification trails.

## Workflow

1. Validate registry shape: roots, required fields, allowed values, and no placeholder values.
2. Check source liveness and archive references.
3. Verify quotes against cited locators.
4. Spot-check statistics and numeric claims against source text.
5. Confirm every claim references valid source IDs.
6. Confirm every synthesis references valid claim IDs.
7. Quarantine unverified claims and log failures.
8. Produce a verification manifest for release.

## Quality Standards

- Verification is independent of the agent that collected the source.
- Numeric claims and direct quotes are checked at point of claim.
- Dead URLs are replaced, archived, or removed.
- Claims with missing source links do not ship.

## Anti-Patterns

- Treating a bibliography as verification.
- Checking only that a URL exists, not that it supports the claim.
- Accepting a quote without locator or exact-match check.
- Allowing imported legacy sources to appear release-ready without audit.

## Outputs

- Verification manifest.
- Rejected-claim log.
- Quote/stat spot-check notes.
- Registry repair list.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Correctness | Verification manifest | Markdown/YAML | Source, claim, quote, and synthesis checks |
| Release evidence | Quarantine log | Markdown table | Claim ID, reason, action, reviewer |

## References

- Load `references/verification-routine.md` for the verification checklist and manifest.

<!-- dual-compat-end -->

## Companion Skills

- `source-evaluation` defines source credibility.
- `evidence-claim-graph` defines claim-source relationships.
- `agentic-research-operations` uses this skill for merge/reject decisions.
