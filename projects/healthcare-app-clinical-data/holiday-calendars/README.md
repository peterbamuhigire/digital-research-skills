# Cohort — holiday-calendars

**Purpose:** seed `tbl_holiday_calendar` with national, religious, and regionally significant holidays so Medic8's appointment scheduler, accounting period close, and HR leave planner can correctly mark non-working days. Trivial-looking but blocking: scheduling and payroll both reference it from day 1.

## Scope (v1)

Per country (UG / KE / TZ / RW / CD / NG): national public holidays + the major religious holidays observed by significant population shares.

Five-year forward window (2026–2030) so onboarded tenants don't immediately need a refresh.

Categories per row:
- **National statutory** — Independence Day, Labour Day, New Year, etc.
- **Christian** — Christmas, Boxing Day (where observed), Good Friday, Easter Monday, All Saints (where observed).
- **Muslim** — Eid al-Fitr, Eid al-Adha, Mawlid (where statutory).
- **Regionally significant** — Heroes Day (UG), Mashujaa Day (KE), Saba Saba (TZ), Liberation Day (RW), independence-anniversary local variations.

Out of v1: UN observance days (World AIDS Day etc.) — not days off, but useful as a future tag.

## Data model

```
holiday_id, country_iso2, year, date_observed, holiday_name_en,
holiday_name_local, holiday_kind (NATIONAL_STATUTORY | CHRISTIAN |
MUSLIM | REGIONAL_OBSERVANCE), is_lunar_calculated,
is_substitute_day, observed_by_government,
typically_observed_by_facility (PUBLIC | PRIVATE | BOTH),
source_citations, code_system_version, code_accessed_date
```

## Cross-cohort dependencies

- `country_iso2` → `country-packs`
- referenced by Medic8 appointment-booking module, accounting-period-close logic, HR leave-planner

## Hard exclusions

- None — holiday data is fact-based, not clinical.

## Outputs

- `research/wave1-data.md` — holiday rows × 6 countries × 5 years
- `research/wave1-findings.md` — sourcing methodology (lunar calendar handling for Eid; date-shift rules when holiday falls on weekend), country-specific observance notes
- `analysis/gap-analysis.md`
- `opportunities/product-ideas.md`

## Source tiers

- **T1:** Government gazettes per country (UG Gazette, KE Gazette, TZ Government Notices, RW Official Gazette, CD Journal Officiel, NG Federal Gazette), Bank-of-X public holiday calendars.
- **T2:** UN OCHA country humanitarian information operating-day calendars (cross-reference).
- **T3:** General-purpose holiday APIs (Calendarific, Nager.Date) — sole-source not allowed; only used for triangulation.
