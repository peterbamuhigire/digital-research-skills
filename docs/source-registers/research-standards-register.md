# Research Standards Register

Last verified: 2026-07-08
Reviewer: Builder upgrade pass
Next review: 2026-10-08 or when a listed standard is updated

This register tracks standards and source families that affect engine output quality. It is a routing aid, not a substitute for opening official sources during live research.

| Standard or source family | Version / edition implemented | Source | Applies to | Reverification trigger |
|---|---|---|---|---|
| PRISMA 2020 | PRISMA 2020 statement and checklist | https://www.prisma-statement.org/prisma-2020 and https://www.prisma-statement.org/prisma-2020-checklist | Systematic reviews, evidence maps, scoping review discipline | PRISMA update, journal requirement change |
| EQUATOR Network reporting guidance | Current guidance family as of 2026-07-08 | https://www.equator-network.org/reporting-guidelines/ | Academic health and social-science reporting standard selection | New reporting guideline or major checklist revision |
| ICD 203 analytic tradecraft | ODNI ICD 203 Analytic Standards | https://www.dni.gov/files/documents/ICD/ICD-203.pdf | Intelligence-style judgments and estimative products | New analytic standard or agency update |
| Heuer/Pherson structured analytic techniques | Structured analytic techniques reference corpus | Attached Markdown reference, mapped in `book-knowledge-map.md` | ACH, KAC, pre-mortem, red team, indicators | New edition or engine fixture drift |
| Minto Pyramid Principle | Executive communication structure | Attached Markdown reference, mapped in `book-knowledge-map.md` | Executive memos, board briefs, consulting reports | Material revision to executive-communication skill |
| Verification Handbook methods | Digital verification and UGC provenance | Attached Markdown reference, mapped in `book-knowledge-map.md` | URL, image, video, social-source, archive verification | New platform norms, tool changes, source access changes |
| Data quality assessment | Data journalism and data-quality practices | Attached Markdown reference, mapped in `book-knowledge-map.md` | Dataset discovery, cleaning, statistics | Data-quality skill update |
| SWEBOK | SWEBOK Guide V4.0 | https://www.computer.org/education/bodies-of-knowledge/software-engineering | Research tooling and validation scripts | New SWEBOK edition or tool architecture change |

## Required fields for volatile-source entries

When a project adds a live source register, each source row must include:

- source_id
- title
- url or locator
- publisher
- source_tier
- accessed_utc
- archived_url
- verification_method
- confidence
- owner
- next_review
- affected_claim_ids

## Release rule

Any compliance-sensitive claim without a last-verified date and source-tier assignment fails the release gate.
