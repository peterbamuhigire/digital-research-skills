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

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Claim-source registry with URLs, quotes, statistics, and citations | Research project | Stop verification and report the missing registry. |
| Source access and archive/provider tools | Source providers | Mark unreachable checks unassessed and seek an authorised alternative. |

## Capability Contract

Verification defaults to read-only. Network access may inspect sources when authorised; archive writes, source contact, registry edits, or publication require explicit authority.

## Degraded Mode

If a URL, archive, provider, or tool is unavailable, report the claim as unverified with the attempted check. Never convert inaccessibility into confirmation.

## Decision Rules

| Finding | Action | Failure/risk avoided |
|---|---|---|
| Quote or number differs from source | Reject or correct with provenance | Misquotation |
| URL resolves but does not support claim | Reject claim-source link | Citation laundering |
| Source unavailable and no archive exists | Mark unresolved | False verification |

## Preliminary Verification Corrections

- Checking URL status only. Fix: verify claim support.
- Paraphrasing during quote verification. Fix: compare exact text.
- Accepting a secondary citation when primary is available. Fix: trace origin.
- Treating archive absence as falsity. Fix: mark unresolved.
- Editing evidence during read-only review. Fix: separate remediation.

## Worked Example

For a quoted statistic, open the cited source, confirm definition, period, unit, and exact value, record the supporting location, and reject the citation if any material element differs.

<!-- dual-compat-start -->

## Use When

- Use after research waves and before synthesis, drafting, export, or release.
- Use when checking quotes, statistics, URLs, source registries, claim registries, archive links, and citation drift.
- Use when a sub-agent output contains sourced material that must be accepted, rejected, or quarantined.

## Do Not Use When

- The task is initial source quality assessment; use `source-evaluation` first.
- The output contains no source-backed claims.

## Verification Source Requirements

- Source registry, claim registry, quote registry, synthesis map, and draft output.
- Source files, URLs, document locators, and access dates.
- Any source-evaluation notes, credibility tiers, and verification trails.

## Verification Method Detail

1. Validate registry shape: roots, required fields, allowed values, and no placeholder values.
2. Check source liveness and archive references.
3. Verify quotes against cited locators.
4. Spot-check statistics and numeric claims against source text.
5. Confirm every claim references valid source IDs.
6. Confirm every synthesis references valid claim IDs.
7. Quarantine unverified claims and log failures.
8. Produce a verification manifest for release.

## Tooling

Use the unified verifier when a project has a machine-readable source manifest:

```powershell
python tools\verification\source_verifier.py projects\<project-id>\_registry\verification-manifest.yaml --out projects\<project-id>\_registry\verification-report.md
```

Use the citation-density dashboard on any Markdown draft before release:

```powershell
python tools\reports\citation_density_dashboard.py projects\<project-id>\05-output\<output-family>\draft.md --manifest projects\<project-id>\_registry\verification-manifest.yaml --out projects\<project-id>\_registry\citation-density.md
```

Both tools return a non-zero exit code when release readiness fails.

## Quality Standards

- Verification is independent of the agent that collected the source.
- Numeric claims and direct quotes are checked at point of claim.
- Dead URLs are replaced, archived, or removed.
- Claims with missing source links do not ship.

## Verification Failure Catalogue

- Treating a bibliography as verification.
- Checking only that a URL exists, not that it supports the claim.
- Accepting a quote without locator or exact-match check.
- Allowing imported legacy sources to appear release-ready without audit.

## Verification Artifact Detail

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
- `docs/quality-gates/release-blocking-gates.md` defines ship/no-ship criteria.

## Workflow

1. Confirm the claim-source registry and accessible evidence; stop if the registry is absent.
2. Verify URL identity, source content, quotations, definitions, periods, units, and claim support.
3. Record exact supporting locations and contradictions.
4. Reject fabricated, mismatched, or unsupported links.
5. Recover from unavailable sources through authorised archives or mark the claim unassessed.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Verification manifest | Researcher and release gate | Every claim is verified, rejected, or explicitly unassessed with attempted checks. |

## Anti-Patterns

- Checking status only. Fix: verify support.
- Paraphrasing a quote. Fix: compare exact text.
- Stopping at secondary citation. Fix: trace origin.
- Treating archive absence as falsity. Fix: mark unresolved.
- Editing evidence in review. Fix: separate remediation.
