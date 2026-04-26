# Background-check workflow

McMahon's canonical workflow with FCRA permissible-purpose discipline.

## The 11-step intake-to-report flow

1. **Intake** — define purpose (employment / partner / M&A target / dating). Get **signed disclosure & release authorization** (FCRA §604(b)(2) for employment).
2. **Ground rules** — cost (budget), timeframe (deadlines), with or without subject's knowledge.
3. **Interviews** — for DD/M&A: key executives. For employment: just the application form.
4. **Public-records sweep** — civil suits, liens, judgments, divorces, criminal cases, UCC filings, bankruptcies, property tax assessments, land records, mortgages.
5. **Federal court sweep** — US District Courts, Tax Court, bankruptcy courts.
6. **Regulatory filings** — SEC, FTC, FCC, secretary of state (incorporation, amendments, annual reports), DMV/driving, BBB, AG complaints, state and local licensing, state comptroller.
7. **Business profile** — ownership/partnership interests, banking references, departed senior management within last 5 years, reasons for departure, current whereabouts.
8. **Principals review** — arrests/convictions, criminal targets, SEC litigation/consent decrees, personal/corporate bankruptcy, civil-litigation party-of-record, creditor/government suits.
9. **Source interviews** — weighed against bias; assess motives. Re-interview key personnel to clarify discrepancies.
10. **Interim report** with credibility assessment per item; explicitly preliminary.
11. **Final report** — review of investigative steps, results, credibility assessment, recommendations.

## Investigation depth by role

| Role | Depth |
|---|---|
| Entry-level employee | 5 years OR last 2 employers (whichever longer) |
| Technical / supervisor | 10 years OR last 3 employers |
| Management / executive | 15 years OR full career |

## Resume-fraud baselines

McMahon's working figures:
- ~30% of resumes fraudulent
- ~60% of salaries inflated
- 5% of personal references nonexistent
- 14% of educational claims bogus

**Always verify education directly with registrar.** It's the most-exaggerated section.

## Application-form anatomy

Mandatory fields:
- Name (full, including middle, plus aliases)
- Residence (current + prior 5+ years)
- Education (institution, dates, degree, major)
- Employment (employer, dates, position, supervisor, salary, reason left)
- Licenses / qualifications
- Military
- References (3+, with relationship)
- Criminal convictions (state-specific; check ban-the-box rules)

Backed by a **release** authorising verification, with caution clause near signature.

## FCRA compliance gate

Before pulling any consumer-report-style data:
1. Permissible purpose under FCRA §604 (employment, credit, tenant, court order, written consent)
2. Pre-adverse-action notice if findings will be used to deny employment
3. Adverse-action notice if final decision is adverse, including FCRA Summary of Rights

The engine's `pi-legal-and-ethical-bounds` skill enforces this gate.

## Output structure (from `pi-report-writing`)

Each finding paired with:
- Source (database / vendor / date)
- Credibility assessment (verified / preliminary / unconfirmed)
- Sample for human review

## Anti-patterns

- Skipping the disclosure & release — FCRA federal violation
- Verifying education from resume only (must call registrar)
- Trusting personal references at face value
- Ignoring departed senior management (best source of intelligence)
- Single-source confirmation for derogatory findings
- Discriminatory screens (Title VII; *Gregory v. Litton Systems*: arrest-record blanket rejection)
- Ban-the-box compliance ignored

## See also

- `pi-report-writing` — output format
- `pi-legal-and-ethical-bounds` — FCRA gate
- `due-diligence-framework` — DD-grade extension above this
- `evidence-discipline` — engine-wide rules apply
