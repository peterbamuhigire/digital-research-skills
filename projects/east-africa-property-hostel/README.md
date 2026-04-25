# Students-Hostels — East Africa Housing Research Project

Four-corner research workspace investigating East African housing pain points across **students, hostel owners, residential landlords, and ordinary tenants** in Uganda, Kenya, Tanzania, Rwanda, Burundi, and South Sudan. Grounded in 250+ sources across news media, social platforms, university repositories, court records, regulatory filings, industry reports, and academic publications.

## Why this project

The East African rental and housing market has **mutually reinforcing dysfunction across four cohorts**:

- **Students** lose money to scams, live with bedbugs and sewage, get evicted unfairly
- **Hostel owners** absorb HELB/HESLB delays, viral reputational risk, PPP competition, capital lock-in
- **Residential landlords** suffer 7–11-month eviction delays, screening blindness, currency-driven cost spikes
- **Ordinary tenants** lose 80% of deposits (Uganda), face discrimination (90% rejection for single women), and live with utility failures they can't seek remedy for

The four reports in this repo cover each cohort, then look for product opportunities — especially **two-sided products** that resolve pain on multiple cohorts simultaneously.

## Structure

```
Students-Hostels/
├── README.md                      this file
│
├── students/                      students seeking & living in hostels
│   ├── research/   (complaints-report, sources, quotes)
│   ├── analysis/   (themes, by-country, named-hostels)
│   └── opportunities/  (product-ideas)
│
├── owners/                        hostel owners & managers
│   ├── research/   (pain-points-report, sources, academic-publications, quotes)
│   ├── analysis/   (themes, by-country, regulatory-landscape)
│   └── opportunities/  (product-ideas)
│
├── landlords/                     general residential landlords
│   ├── research/   (pain-points-report, sources, quotes)
│   ├── analysis/   (themes, by-country, proptech-landscape)
│   └── opportunities/  (product-ideas)
│
└── tenants/                       ordinary residential tenants
    ├── research/   (pain-points-report, sources, quotes)
    ├── analysis/   (themes, by-country, vulnerable-groups)
    └── opportunities/  (product-ideas)
```

## Top findings by cohort

**Students:** 80% of Ugandan tenants never get their deposit refunded; UoN water shortages run for months; bedbugs at 58% prevalence in Tanzanian boarding studies; UR Huye students slept in the gymnasium in 2025; U-Juba police raided a female hostel arresting 23 (June 2024).

**Hostel owners:** Hostel owners evicted 30+ MUBS students because the government hadn't paid allowances for 3 months; Kenyan developers face 18–22% rates vs 4–8% foreign; Uganda's tax stack ≈35–40% of revenue; Acorn Holdings' 20,000-bed B1-rated portfolio is the institutional ceiling; Kenya National Building Code 2024 (post-Sept 2024 fire) is the first real fire-code enforcement.

**Residential landlords:** 7–11-month eviction delays in Kenya magistrate courts; <5% CRB adoption for tenant screening; mortgage penetration only 3.6% in Kenya; KSh -26.8% vs USD pushed material costs +30–50%; *dalali* market in Tanzania still unregulated.

**Tenants:** 80% of Ugandan tenants never recover deposits despite 2022 Act; ~90% single-women rejection rate vs single men; 30% of Ugandan renters encounter fake listings; Nairobi 250M-litre/day water deficit; 2024 riparian demolitions displaced 20,000+ Nairobi residents with KSh 10,000 compensation each; <30% of tenants know their statutory rights.

## Cross-cohort patterns

- **Deposit theft** hits students (`students/`), hostel residents (`students/`), and tenants (`tenants/`) in identical ways. The 80% Uganda non-refund stat is the single sharpest pain in the entire repo.
- **Brokers / middlemen** extract from students, tenants, and even landlords. Verification + escrow is the universal product hook.
- **Government payment delays** (HELB, HESLB, allowance) cascade from student → hostel owner; equivalent dynamic in commercial-rent corporate-housing-allowance flow.
- **Eviction infrastructure** is the dominant landlord-side pain and the dominant tenant-side fear — same feature, opposite valence.
- **Regulatory frameworks exist on paper, fail in enforcement.** Uganda L&T Act 2022, Kenya L&T Bill 2021, Makerere 2023 Hostel Inspection Report — all create rights / duties that aren't enforced. Enforcement infrastructure, not new statutes, is the largest single gap.

## How to use

1. Pick a cohort. Read its `research/pain-points-report.md` (or `complaints-report.md` for students).
2. Cross-reference with `analysis/themes.md` and `analysis/by-country.md`.
3. Compare with the symmetric cohort's themes file (e.g. `landlords/themes.md` ↔ `tenants/themes.md`).
4. `owners/research/academic-publications.md` lists peer-reviewed and dissertation sources for citation in any pitch deck or grant.
5. Use each cohort's `opportunities/product-ideas.md` and look for ideas that appear on multiple sides — these are the highest-leverage two-sided plays.

## Status

Compiled 2026-04-25 across four research streams plus a Pass-2 gap-fill on student & owner sides.

| Cohort | Sources | Notable depth |
|---|---|---|
| students | ~90 (50 + 40 Pass 2) | Mental-health, dropout, female-specific harm; named-hostel inventory |
| owners | ~120 (84 + 40 Pass 2) | Acorn financials, Kenya Building Code 2024, currency risk |
| landlords | 60+ | PropTech landscape, eviction-time matrix, court precedents |
| tenants | 75+ | Vulnerable-groups deep-dive, riparian demolitions, awareness gap |

**Living document.** Pass-3 priorities flagged across all four `*/research/sources.md` "gaps" sections. Top three: (1) PRAW-with-auth Reddit corpus extraction; (2) primary owner / landlord interviews with verbatim quotes; (3) court / tribunal data extraction by jurisdiction.

Maintained by Peter Bamuhigire.
