# CLAUDE.md — east-africa-property-hostel project

Project-specific operating instructions. Inherits all rules from the engine root `CLAUDE.md` — this file only adds project-specific scope, exclusions, and conventions.

## Scope

Pain points across **four cohorts** in East Africa (Uganda, Kenya, Tanzania, Rwanda, Burundi, South Sudan):

- `students/` — students seeking and living in hostels
- `owners/` — student-hostel owners and managers
- `landlords/` — general residential landlords (NOT hostels)
- `tenants/` — ordinary residential tenants (NOT students)

Each is a **sub-project** with its own `README.md`, `CLAUDE.md`, `research/`, `analysis/`, `opportunities/`.

## Hard scope exclusions for this project

- **No LGBTQ+ topics.** The user has explicitly excluded this scope. Restate the exclusion in every sub-agent brief, and filter out any LGBTQ+ findings before merging into project files.
- Student hostels are NOT to be researched in `landlords/` or `tenants/` cohorts (they are covered in `students/` and `owners/`).
- General commercial-only buildings are out of scope.
- Hotels and short-let / Airbnb are out of scope (mention only briefly for landlord competitive context).

## Anti-hallucination — project specifics

The engine's `evidence-discipline` rule applies. Specific watch-outs for this project:

- **Court cases:** Verify on Kenyalaw.org / ULII / TanzLII / RwandaLII. Several real cases are already cited (Komakech & 7 Ors v Ayaa & Anor 2018; Tribunal Case E007/2024; Muhanda v LP Holdings 2025; Civil Case 56 of 2015). Do not invent new case names that follow the format.
- **Statutes:** Specific known-real ones in this project — Uganda L&T Act 2022; Kenya Rent Restriction Act 1982; Kenya Distress for Rent Act; Kenya Landlord & Tenant Bill 2021 (not yet enacted); Tanzania Land Act 1999; Tanzania Rent Restriction Act 1984; Kenya National Building Code 2024.
- **Statistics with specific source attribution required:**
  - "80% of UG tenants never recover deposits" — Daily Monitor Aug 2023
  - "30% of UG renters encounter fake listings" — Spectrum Real Estate Solutions
  - "Acorn Holdings 20,000 beds, KSh 1.52bn FY'25 profit" — Acorn / NSE filings
  - "Nairobi 250M-litre/day water deficit" — NCWSC
  - "Kigali 79% informal settlements; 54% earn $38–225/mo" — IGC 2024
- **Named operators that exist:** Acorn Holdings, CrossBoundary, Pearl Properties, Knight Frank Uganda, Bageine & Co, Yiga & Co, Tysons Ltd Kenya, Lloyd Masika, Pam Golding Kenya, Villa Care. Do not invent variants.
- **Named hostels that exist** (from the `students/` cohort research): Pearl View, Cotilde, Olympia, Kann, Frama, Hannington, Akamwesi, Madonna, Bavana, Paradise, New Nana, Cedes Sapientiae / Fox.

If a sub-agent introduces a name / case / statistic NOT on these lists, verify before accepting.

## Workflow status

- **students/**: Wave 1 + Wave 2 complete. ~90 sources.
- **owners/**: Wave 1 + Wave 2 complete. ~120 sources.
- **landlords/**: Wave 1 complete. ~60 sources.
- **tenants/**: Wave 1 complete. ~75 sources.
- **Cross-cohort synthesis**: not yet finalised — synthesis lives partially in the project README.
- **Word-document export**: not yet generated.

## Next steps

1. Run Wave 2 gap-fills on `landlords/` and `tenants/` to bring them to parity with the other two cohorts
2. Run formal cross-cohort synthesis into `SYNTHESIS.md` at this project level
3. Run a Wave 3 verification pass — spot-check stats, verify URLs, confirm court cases
4. Pick the report schema (Schema A — Pain-point research, multi-cohort) and assemble master markdown
5. Generate `report-v1-<date>.docx`

## Project file inventory

```
east-africa-property-hostel/
├── README.md
├── CLAUDE.md                    (this file)
├── EVIDENCE-AUDIT.md            (running log of caught hallucinations / corrections)
├── students/    8 markdown files (3 research + 3 analysis + 1 opportunity + 1 README + 1 CLAUDE)
├── owners/      9 markdown files
├── landlords/   8 markdown files
└── tenants/     8 markdown files
```

See engine root `CLAUDE.md` for engine-wide rules.
