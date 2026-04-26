# Regulatory landscape mapping

Domain research without legal framing tells half the story. This skill builds the other half.

## Five layers per jurisdiction

| Layer | What | Example sources |
|---|---|---|
| 1. Constitutional | Constitutional rights / protections | Constitution of Kenya 2010, Uganda 1995 |
| 2. Statute | Acts of Parliament currently in force | Kenya Rent Restriction Act 1982, Uganda L&T Act 2022 |
| 3. Subsidiary | Regulations, rules, codes, by-laws | Kenya National Building Code 2024, KCCA by-laws |
| 4. Case law | Precedent that interprets the above | Kenyalaw, ULII, TanzLII, RwandaLII |
| 5. Enforcement | What regulators actually do | KRA, URA, NEMA, IRA, EARB filings |

A regulatory mapping that stops at layer 2 misses where the law actually bites — or fails to.

## Output target — `<cohort>/analysis/regulatory-landscape.md`

```markdown
# Regulatory landscape — <domain>

## <Country>

### Layer 1 — Constitutional anchors
- Article X — non-discrimination

### Layer 2 — Statute
- <Act name>, <year> — key provisions
- <Bill name>, <year> — status (enacted / pending / lapsed)

### Layer 3 — Subsidiary
- <Regulation>

### Layer 4 — Case law
- <Citation> — ratio decidendi
- <Citation> — ratio decidendi

### Layer 5 — Enforcement
- Regulator: <name>
- Recent enforcement actions: ...
- Capacity / capture / corruption notes

### Enforcement gap
- The recurring finding: statute exists, enforcement reaches <X% of cases
```

## Decision rules

- **Always include Layer 5.** A statute that's never enforced is functionally absent — the report must say so.
- **Pin every claim to a citation.** "Section 22 of the Rent Restriction Act" is a usable claim; "Kenyan law says..." is not.
- **Note the bill / act / regulation status.** A pending bill is not the law.
- **Track recent jurisprudence by year.** Court precedent rots when superseded.
- **Flag enforcement gaps as findings**, not as embarrassments.

## Standard EA jurisdictions covered

- **Kenya** — Kenyalaw.org, Parliament of Kenya, KRA, NEMA, EARB, IRA Kenya
- **Uganda** — ULII, KCCA, URA, NEMA Uganda, IRA Uganda, AREA-Uganda
- **Tanzania** — TanzLII, BRELA, NEMC
- **Rwanda** — RwandaLII, RRA, REMA
- **Burundi / South Sudan** — limited published material; primary research often required

## Anti-patterns

- Stopping at "the law says X" without checking enforcement
- Listing acts without statuses (enacted vs pending)
- Treating regulator websites as primary instead of case law
- Ignoring the difference between distress-for-rent abolished (UG 2022) and still operative (KE)
- Citing journalism summaries of laws instead of the laws themselves

## See also

- `source-verification` — Tier 2 sources are the regulatory backbone
- `gap-analysis` — enforcement gaps are a primary research output
- `research-report-builder` — emits regulatory landscape as a Word-doc chapter
