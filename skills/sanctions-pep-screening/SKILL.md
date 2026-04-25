---
name: sanctions-pep-screening
description: Use whenever a research project touches a person, company, vessel, or aircraft that may be on a sanctions, PEP, or watch list — wraps OFAC + EU + UN SC + UK HMT + OpenSanctions in a single multi-list screener with fuzzy matching, DOB / nationality boost, and three-tier confidence buckets. Backed by tools/sanctions/. From Hetherington's Authoritative Guide to Due Diligence.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Sanctions / PEP / watch-list screening

Hetherington: never assert "X is on OFAC" without verifying full-name + DOB + nationality + locator. This skill encodes the discipline behind that rule.

## What it covers

| List | Issuer | Coverage |
|---|---|---|
| OFAC SDN | US Treasury | US blocked persons + entities |
| OFAC Consolidated | US Treasury | US sectoral / non-SDN |
| EU Consolidated Financial | EEAS | EU + member states |
| UN Security Council Consolidated | UN SC | Globally adopted |
| UK HMT Financial Sanctions | OFSI | UK regime |
| OpenSanctions Default | opensanctions.org | Cross-jurisdictional consolidated |
| OpenSanctions PEPs | opensanctions.org | PEPs + family + close associates |
| ICIJ Offshore Leaks | ICIJ | Offshore registry leaks |

Paid commercial vendors (World-Check, Dow Jones Risk, Sayari, LexisNexis WorldCompliance, Refinitiv) are NOT required for the baseline coverage. Add them only when client mandates a specific commercial source.

## Standard workflow

```python
from tools.sanctions import refresh_lists, screen_name

# Once a day (cron) — pull latest lists into local cache
refresh_lists(dest_dir="./data/sanctions")

# Per investigation — screen a name
result = screen_name(
    name="John Smith",
    dob="1965-04-12",
    nationality="GB",
    aliases=["J. Smith", "Johnny Smith"],
    threshold_high=0.92,
    threshold_medium=0.78,
)

if result.high_confidence_hits:
    # Escalate to operator — do NOT auto-include in report
    for hit in result.high_confidence_hits:
        print(f"[HIGH] {hit.list_name}: {hit.matched_name} ({hit.similarity:.2f})")
```

## Three confidence buckets

The screener returns three buckets so callers can decide escalation:

| Bucket | Threshold | Action |
|---|---|---|
| **High** | ≥0.92 | Escalate immediately — likely real hit |
| **Medium** | ≥0.78 | Triangulate before reporting (≥3 sources) |
| **Low** | <0.78 | Log only — likely common-name false positive |

## Hetherington's confidence-boosting rules

The screener applies these automatically:

- **DOB year match** → similarity +0.05
- **Nationality match** → similarity +0.05
- **Identifier match** (passport, SSN-last-4, DUNS) → +0.10 (caller-supplied)

A bare name match without any of these is a low-confidence signal that requires further triangulation.

## Reporting discipline

Per Hetherington: every DD report must explicitly say what was searched AND what was NOT found:

> *"A search of OFAC SDN, EU Consolidated, UN SC Consolidated, UK HMT, and OpenSanctions on YYYY-MM-DD did not reveal matches against the subject."*

Reporting **negative findings** is as important as reporting hits — it shows the search was performed, not skipped. The `due-diligence-report-architecture` skill puts this in the standard report skeleton.

## Anti-patterns

- Asserting "X is sanctioned" from a single fuzzy match
- Treating same-name as same-person (the #1 defamation risk)
- Skipping DOB / nationality refinement when available
- Stale list cache (always refresh before screening)
- Hard-coding name spellings — match against alias lists
- Not searching aliases (Hetherington: "what name did your subject use 10 years ago?")
- Searching ONLY OFAC — multi-list is the discipline

## Refresh cadence

Set up a daily cron:

```bash
0 4 * * * cd /path/to/engine && python -c "from tools.sanctions import refresh_lists; refresh_lists()"
```

## Monetisation

Sanctions / PEP screening is a productisable layer:

- **Per-screen API**: $0.50–$5 per check, stacked into KYC SaaS
- **Subscription monitoring (Phase Three)**: $X/mo for ongoing watch on N entities, alerts on new hits
- **Compliance audit reports**: bulk-screen a customer book annually
- See `dd-saas-monetisation` (roadmap) for full pricing playbook

## See also

- `tools/sanctions/` — implementation
- `due-diligence-framework` — methodology context
- `due-diligence-report-architecture` — how to report findings
- `evidence-discipline` — overall verification rules
- `corporate-veil-investigation` — companion for entity-screening
