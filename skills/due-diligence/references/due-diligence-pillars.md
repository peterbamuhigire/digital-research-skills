# Due-diligence framework

Due diligence is research with **liability**. The same evidence-discipline rules apply but stricter — every flag attached to an entity could affect a deal, an investment, a hire, or a person's reputation.

## The eight DD pillars

For any named entity, work through:

1. **Identification & corroboration** — Confirm the entity exists; legal name, registration number, jurisdiction, addresses
2. **Legal & regulatory status** — Active registration, licences, court records, regulatory filings, sanctions screening
3. **Financial position** — Audited statements, credit reports, lender history, tax-compliance status
4. **Reputational footprint** — News coverage, social mentions, adverse-media findings, NGO reporting
5. **Beneficial ownership** — UBO trace, shareholder structure, related parties
6. **Counterparty / network** — Customers, suppliers, partners, board, executives — and their flags
7. **Adverse-media findings** — Litigation, fraud allegations, regulator actions, media exposés
8. **Source-of-funds / source-of-wealth** (AML contexts only) — Origin of capital being placed

## Flag system

| Flag | Meaning | Examples |
|---|---|---|
| 🟢 Green | No material findings; verified clean | Active registration; clean court record; positive sentiment |
| 🟡 Amber | Findings exist; non-disqualifying but require explanation | Old litigation settled; minor regulatory fine paid; thin financials |
| 🔴 Red | Material adverse findings; disqualifying without explicit mitigation | Active sanctions; pending fraud trial; UBO opacity |

## Verification rigour (stricter than general research)

- **Every flag must be tier 1 or tier 2 sourced** (see `source-verification`). Tier 3 supports a flag; tier 5 alone never warrants one.
- **Triangulate flags across ≥2 independent sources.** A single tweet alleging fraud is not a flag.
- **Date-stamp every flag.** Litigation 8 years ago carries different weight than 6 months ago.
- **Distinguish allegation from finding.** "Sued for X" ≠ "Found liable for X".
- **Clearly mark inference.** "(inferred — UBO chain not directly documented)".
- **Document the verification limit.** "Could not verify Z because [paywalled / not in public registry / language]".

## Standard outputs

- `<project>/research/dd-pillars.md` — one section per pillar with findings + flags
- `<project>/research/flag-summary.md` — single-pane red/amber/green ledger
- `<project>/research/source-confidence.md` — per-finding tier + verification status
- The final Word doc uses Schema F.

## Decision rules

- **Begin with identification.** A wrong-entity DD is worse than no DD.
- **Don't infer red.** Always be able to point to a tier-1/2 source.
- **Allegation ≠ finding.** Pending litigation is amber; adverse judgment is red.
- **The report's audience can sue.** Treat it like a legal document.
- **Conclude with explicit verification limits.** A clean DD that didn't check sanctions lists is not a clean DD.

## Anti-patterns

- Treating Google search results as primary
- Citing "online sources say" without naming them
- Marking 🔴 on the basis of a single forum post
- Skipping the UBO trace because it's hard
- Implying a person is corrupt because they "look" like someone in a sanctions list (sanctions hits require positive identification, not similarity)

## Sanctions / lists to check (where relevant)

- OFAC SDN list
- UK HMT financial sanctions
- EU consolidated sanctions
- UN Security Council Consolidated List
- FATF grey/black list (for jurisdiction risk, not entity)
- Country-specific PEP databases

## See also

- `evidence-discipline` — non-negotiable
- `source-verification` — tier discipline applies stricter
- `osint-methodology` — feeds DD pillars 1, 5, 6
- `regulatory-landscape-mapping` — feeds DD pillar 2
- `research-report-builder` — Schema F
