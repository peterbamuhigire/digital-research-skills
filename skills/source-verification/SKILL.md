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

## Verification inputs

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

## Semantic claim-support boundary

Every release-bound claim should carry a `support_review` record with `state`
set to `supported`, `unsupported`, `synthesis`, `inference`, or `no-source`,
plus a reviewer, basis, and parseable review date. `source_ids` must be an
explicit list: use `[]` only with `no-source`, and use at least one known source
ID for every other state. The verifier rejects malformed state/source
combinations and non-list manifest collections. It does not decide whether the
wording is semantically supported. Every support state remains non-certifying;
metadata cannot promote an unsupported, no-source, or inference claim to
release-ready. Use `tests/fixtures/claim-support-review.json` and its
deterministic tests as the contract fixture.

<!-- dual-compat-start -->

## Use When

- Use after research waves and before synthesis, drafting, export, or release.
- Use when checking quotes, statistics, URLs, source registries, claim registries, archive links, and citation drift.
- Use when a sub-agent output contains sourced material that must be accepted, rejected, or quarantined.

## Do Not Use When

- The task is initial source quality assessment; use `source-evaluation` first.
- The output contains no source-backed claims.

## Required Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Source, claim, quote, synthesis registries, and draft output | Research project | Stop verification and report the missing registry |
| Source files, URLs, document locators, and access dates | Source providers | Mark checks unassessed |
| Source-evaluation notes, credibility tiers, and verification trails | Source-evaluation skill | Narrow the verification claim |

## Workflow

1. Validate registry shape: roots, required fields, allowed values, and no placeholder values.
2. Check source liveness and archive references.
3. Verify quotes against cited locators.
4. Spot-check statistics and numeric claims against source text.
5. Confirm every claim has a correctly shaped source-ID list, references valid source IDs, and carries an explicit semantic support-review state.
6. Confirm every synthesis references valid claim IDs.
7. Quarantine unverified claims and log failures.
8. Produce a verification manifest for release.
9. Stop release when material support is missing or unresolved.
10. Recover through an authorised archive or mark the claim unassessed; never convert inaccessibility into confirmation.

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

## Anti-Patterns

- Treating a bibliography as verification. Fix: check claim support at the cited locator.
- Checking only that a URL exists, not that it supports the claim. Fix: verify content and scope.
- Accepting a quote without locator or exact-match check. Fix: compare the exact source text.
- Allowing imported legacy sources to appear release-ready without audit. Fix: classify freshness and uncertainty.
- Editing evidence during review. Fix: separate remediation from the read-only verification record.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Verification manifest, rejected-claim log, quote/stat spot-check notes, and registry repair list | Researcher and release gate | Every claim is verified, rejected, or explicitly unassessed with attempted checks |

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Correctness | Verification manifest | Markdown/YAML | Source, claim, quote, and synthesis checks |
| Release evidence | Quarantine log | Markdown table | Claim ID, reason, action, reviewer |

## References

- Load `references/verification-routine.md` for the verification checklist and manifest.
- Load `references/research-product-audit.md` before release of a research product.

<!-- dual-compat-end -->

## Companion Skills

- `source-evaluation` defines source credibility.
- `evidence-claim-graph` defines claim-source relationships.
- `agentic-research-operations` uses this skill for merge/reject decisions.
- `docs/quality-gates/release-blocking-gates.md` defines ship/no-ship criteria.

## Freshness, uncertainty, and product audit

Verification must check not only whether a source is reachable, but whether it is complete enough, current enough, and context-matched for the exact claim. Record publication/revision/access dates, locator, source status, and uncertainty. Historical, early-release, inaccessible, or corrupted material must remain visibly qualified. Before release, run `references/research-product-audit.md`; its raw score is shown but the published audit is capped at 65/100, and every remediation plan targets 95/100 with acceptance evidence.

After each verification wave, capture one process defect or waste category, define a reversible hypothesis, compare the same verification measures, and standardise only a demonstrated improvement. Do not edit source evidence during the audit; change claim status or the process in a separate remediation step.

## Extended verification workflow

1. Confirm the claim-source registry and accessible evidence; stop if the registry is absent.
2. Verify URL identity, source content, quotations, definitions, periods, units, and claim support.
3. Record exact supporting locations and contradictions.
4. Reject fabricated, mismatched, or unsupported links.
5. Recover from unavailable sources through authorised archives or mark the claim unassessed.

## Extended verification outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Verification manifest | Researcher and release gate | Every claim is verified, rejected, or explicitly unassessed with attempted checks. |

## Extended verification anti-patterns

- Checking status only. Fix: verify support.
- Paraphrasing a quote. Fix: compare exact text.
- Stopping at secondary citation. Fix: trace origin.
- Treating archive absence as falsity. Fix: mark unresolved.
- Editing evidence in review. Fix: separate remediation.
