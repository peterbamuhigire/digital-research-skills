# Research Evidence Pack Template

Standard/version: Digital Research Engine July 2026 release pack
Last verified: 2026-07-08

## 1. Project Identity

Project ID:
Research type / schema:
Audience:
Decision supported:
Lead reviewer:
Release date:

## 2. Scope and Stop Conditions

In scope:

- 

Out of scope:

- 

Stop conditions:

- Any fabricated or unverifiable claim.
- Any legal, regulatory, or statistical claim that cannot be verified by a current source.
- Any private-person risk that has not passed safety review.

## 3. Source Register

| Source ID | Title | URL / locator | Tier | Accessed UTC | Archive URL | Verification method | Confidence |
|---|---|---|---|---|---|---|---|
| src-001 |  |  |  |  |  |  |  |

## 4. Claim Register

| Claim ID | Claim | Type | Source IDs | Confidence | Status |
|---|---|---|---|---|---|
| claim-001 |  | fact / inference / synthesis / gap |  |  | draft / verified / quarantined |

## 5. Wave Log

| Wave | Objective | Search / method notes | Output | Gaps found |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 | Verification |  |  |  |
| 4 | Synthesis |  |  |  |

## 6. Verification Results

Verifier command:

```powershell
python tools\verification\source_verifier.py projects\<project-id>\_registry\verification-manifest.yaml --out projects\<project-id>\_registry\verification-report.md
```

Citation dashboard command:

```powershell
python tools\reports\citation_density_dashboard.py projects\<project-id>\05-output\<output-family>\draft.md --manifest projects\<project-id>\_registry\verification-manifest.yaml --out projects\<project-id>\_registry\citation-density.md
```

## 7. Reasoning and Review

Key assumptions:

- 

Alternative explanations:

- 

Reviewer challenges:

- 

Disposition:

- 

## 8. Release Gate

| Gate | Status | Evidence |
|---|---|---|
| Evidence discipline | pass / fail |  |
| Verification | pass / fail |  |
| Analytic reasoning | pass / fail |  |
| Anti-slop | pass / fail |  |
| Output completeness | pass / fail |  |

Release decision:
