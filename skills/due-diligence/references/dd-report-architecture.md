# Due-diligence report architecture

A DD report has a different shape from a research report. Audience can sue. Format is courtroom-ready. Hetherington's canonical structure:

## Required sections (in order)

1. **Cover page**
   - Title (DUE DILIGENCE REPORT)
   - **Privileged and Confidential** (mandatory)
   - **Attorney Work Product** (when retained by counsel)
   - Subject / Client / Date / Investigator firm
2. **Objective** — one paragraph: who hired whom, on whom, using what sources, for what purpose
3. **Executive Summary** — *findings up front* (NEVER bury OFAC / criminal / sanctions hits past page 2)
4. **Traffic-Light Flag Table** — red / amber / green with one-line summaries
5. **CARA Profile** (for persons) OR **SWOT** (for companies)
6. **Body sections** in priority order, anomalies first:
   - Vital information (DOB, addresses, household)
   - Professional history with **gap analysis** (unexplained gaps may indicate prison or expat period)
   - Board positions with conflict-of-interest annotations
   - Political affiliations & charitable works
   - Academic credentials (verified directly with registrar — "the most frequently exaggerated section")
   - Identified assets — real property, vehicles, vessels, aircraft, financial assets, IP
   - Legal findings — criminal first, then civil
   - Regulatory / sanctions / disciplinary issues — **report negatives explicitly**
   - Financial troubles (liens, judgments, bankruptcies)
   - Media findings (descending date order)
7. **Sources cited** — every database / vendor / date in-line
8. **Disclaimer** (fixed liability-management language; verbatim)

## CARA framework (persons)

| Letter | Element |
|---|---|
| **C** | Characteristics — physical, demographic, professional |
| **A** | Associations — affiliations, partnerships, board memberships |
| **R** | Reputation — adverse-media, peer assessments, public-record signals |
| **A** | Affiliations — political, religious, professional bodies |

## SWOT for companies

Standard 2×2 — strengths, weaknesses, opportunities, threats. Plus supply-chain and value-chain attached as separate sections.

## Reporting negatives is mandatory

Hetherington: "what you don't find is as important as what you find." Every search performed must be reported, even if zero hits:

> *"A search of OFAC SDN, EU Consolidated, UN SC Consolidated, UK HMT, and OpenSanctions on 25 April 2026 did not reveal matches against the subject."*

This proves the search was performed, not skipped.

## Citation discipline (APA-aligned)

Every factual claim cites source vendor + date in-line:

- *"Per a search of LexisNexis Accurint dated 25 April 2026..."*
- *"Per the State of Florida Disciplinary Actions database..."*
- IP citations: `Smith, J. (1995). U.S. Patent No. 123,434. Washington, D.C.: U.S. Patent and Trademark Office.`

## Standard usage

```python
from tools.dd import build_dd_report, DDReport, FlaggedFinding
from datetime import date

report = DDReport(
    client="Acme Capital LLP",
    subject_name="John Smith",
    subject_type="person",
    objective="Pre-investment background on Mr Smith prior to Series B participation.",
    privileged=True,
    attorney_work_product=True,
    flags=[
        FlaggedFinding(flag="red", title="OFAC SDN match", summary="High-confidence hit on OFAC consolidated list (similarity 0.94 on name + DOB).", sources=["OFAC SDN 2026-04-25"]),
        FlaggedFinding(flag="amber", title="Civil litigation", summary="Defendant in commercial dispute, settled 2021, no admission of liability.", sources=["PACER 2026-04-25"]),
        FlaggedFinding(flag="green", title="Education verified", summary="MBA Wharton 2008 confirmed via direct registrar inquiry.", sources=["Wharton Registrar 2026-04-25"]),
    ],
    cara_indicators={
        "Characteristics": "Male, b. 1965 UK, finance executive",
        "Associations": "Director, Acme Holdings; Trustee, Smith Foundation",
        "Reputation": "No adverse media; one civil settlement",
        "Affiliations": "Conservative Party (UK) donor 2018-2022",
    },
)

build_dd_report(report, output_path="dd-john-smith-2026-04-25.docx")
```

## Anti-patterns

- Burying red-flag findings in the body
- Omitting "Privileged and Confidential" — loses legal protection
- Proprietary boilerplate replacing the standard disclaimer
- Vendor citations without dates
- Listing only positive findings
- "Traffic light" flags without specific evidence cited
- Educational gaps ignored (Hetherington's #1 fraud signal)

## See also

- `tools/dd/report_builder.py` — implementation
- `due-diligence-framework` — methodology behind the structure
- `sanctions-pep-screening` — feeds the flag table
- `corporate-veil-investigation` — feeds entity body sections
- `adverse-media-investigation` — feeds the media section
- `evidence-discipline` — every claim must be sourced
