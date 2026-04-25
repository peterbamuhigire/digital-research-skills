# Regulatory landscape — what owners must comply with

Country-by-country compliance map. Use as a starting point for any regtech / compliance-as-a-service product targeting owners.

## Uganda

### Landlord & Tenant Act, 2022

- **Written agreements** mandatory for tenancies above UGX 500,000. Oral agreements must be documented and shared within 14 days.
- **Tenant ID verification** — landlord must obtain national ID, driving permit, passport, or student ID before lease signature.
- **Habitability** — landlord must provide premises "fit for human habitation" and maintain exterior + common areas.
- **Rent increase notice** — 90 days' written notice required.
- **Eviction** — no more "distress for rent" (self-help seizure). Court order required for unpaid-rent recovery. Unlawful self-help eviction = tenant compensation of 3 months' rent + damages.

### Tax stack

| Tax | Rate / threshold | Authority |
|---|---|---|
| Property Rates | 6% of rateable value | KCCA / Municipal |
| Local Hotel Tax | Per occupant, monthly | KCCA / Municipal |
| Rental Income Tax | Per URA schedule | URA |
| VAT | 18% above UGX 150m / year (or 37.5m / 3 months) | URA |
| Corporate Income Tax | 30% on chargeable income | URA |
| NSSF | Mandatory employer contribution | NSSF |
| NHIF | Mandatory employer contribution | NHIF |

**Effective combined burden ≈ 35–40% of revenue for a fully compliant operator.**

### Accreditation

Makerere University Hostel Inspection Committee (HIC, since 2023). 37 hostels graded A/B/C. Voluntary now; recommendation is for an MOU framework registering all hostels in a database (name, owner, capacity, cost, location, contacts).

## Kenya

### Landlord & Tenant Bill, 2021 (status: bill, not yet enacted at compile date)

- **Rent increases** capped at preceding year's average inflation rate.
- **Frequency** — once / 12 months (residential) or 24 months (business).
- **Notice** — 90 days written; failure to provide invalidates the increase.

### Rent Restriction Act / Penal Code

- **Section 22** — penalises landlord who removes tenant furniture or deprives access. Fine up to 1,000 KSh or 6 months' jail.
- **Penal Code §194** — forcible entry is a criminal offence.
- **Environment & Land Court (ELC)** has ruled non-court-ordered evictions unlawful.
- **Eviction notice periods:** 30 days (non-payment), 60 days (lease breach), 7–30 days (illegal activity).

### Tax stack

| Tax | Rate / threshold | Authority |
|---|---|---|
| Rental Income Tax | 7.5% on KSh 280k–15m / year (eff. 1 Jan 2024) | KRA |
| Income Tax (above 15m) | Annual return | KRA |
| NSSF | 6% of salary, capped KSh 72k/month, lower limit KSh 8k | NSSF |
| SHIF (formerly NHIF) | 2.75% of gross | SHIF |
| PAYE | Per income bands | KRA |
| Affordable Housing Levy | Per recent statute | KRA |

**Non-compliance penalty:** up to KSh 2m fine / 3 years' jail.

### PPP context (regulatory-adjacent)

- Kenyatta University Hostels: 20-year concession, USD 57m, **rent collected via tuition**.
- UoN Mamlaka: 30-year DBFOT concession, 4,000 beds.
Private operators within 5km radii compete against state-backed structures.

## Tanzania

### Status

- HESLB governs student loan disbursement (operates with documented delays).
- Tanzanian housing law emphasises tenure security but enforcement uneven.
- No published student-hostel-specific regulatory framework equivalent to Makerere's HIC.
- KIUT (KIU Tanzania) publishes accommodation standards expecting reliable electricity, water, and hygiene from private hostels.

### Tax

Tanzania Revenue Authority charges rental income tax at progressive rates; VAT applies to commercial accommodation services. Specifics evolve — check current TRA schedules before any compliance work.

## Rwanda

### Status

- Rwanda Revenue Authority charges rental income tax with progressive bands.
- University of Rwanda lacks published hostel-accreditation framework but is mobilising Private Sector Federation to expand supply.
- Female-safety expectations are de-facto enforced by parent and student demand.
- Construction permitting and KYC standards generally rigorous relative to UG/KE.

## Cross-cutting

### Insurance

- **Public liability** — covers third-party injury, death, property damage claims.
- **Property insurance** — fire, structural, water damage.
- **Coverage in EA is uneven** — "no guaranteed minimum" (CrossBoundary). Many small operators are uninsured or underinsured.
- A single fire / death / assault can financially destroy an uninsured operator.

### Employment compliance

All countries require:
- Statutory pension registration (NSSF UG/KE/TZ; RSSB Rwanda)
- Health-fund registration (NHIF UG; SHIF KE; NHIF Tanzania; CBHI Rwanda)
- Tax-on-payroll (PAYE)

Most informal hostels skip these, accepting legal exposure.

### Data protection (emerging)

Uganda's Data Protection and Privacy Act 2019 and Kenya's Data Protection Act 2019 apply when landlords store tenant national-ID data, tenancy records, or surveillance footage. Owner ignorance of these obligations is widespread; enforcement is sporadic but growing.

## Compliance-as-a-service opportunity

A simple SaaS that:
1. Generates compliant tenancy agreements per jurisdiction
2. Tracks notice periods (rent increase, eviction, deposit return)
3. Handles tax filing reminders and integrations (URA, KRA, KCCA)
4. Manages staff payroll with NSSF / SHIF / NHIF compliance
5. Stores tenant IDs in a Data Protection Act–compliant manner
6. Accreditation submission helper (Makerere HIC, future KE equivalent)

…would map directly onto the regulatory pain documented above. See `owners/opportunities/product-ideas.md` for fuller treatment.
