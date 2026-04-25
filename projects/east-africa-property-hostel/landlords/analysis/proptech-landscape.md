# PropTech & rental-platform landscape — East Africa

The platforms landlords use (or could use) for listings, rent collection, screening, and management. Pulled from the landlord research; cross-checked against local press and platform sites.

## Listings & marketplaces

| Platform | Country | Listings | Model | Strength | Weakness |
|---|---|---|---|---|---|
| **BuyRentKenya** | KE | 7,500+ | Free | Filter quality; brand recognition | Limited filters on rentals |
| **Property24 Kenya** | KE | 5,000+ | Freemium | International parent; SEO | Stale listings not auto-removed |
| **Lamudi** | Regional | 800,000+ | Freemium | Multi-country reach | Cross-country dilution; quality drop |
| **Real Muloodi** | UG | 2,000–3,000 | Free 30 days | Zero-commission innovation | Low cross-border reach |
| **Kenya Property Centre** | KE | 5,000+ | Free | Active forum | UI dated |
| **AREA Uganda MLS** | UG | Expanding | Members-only | Industry credibility | Not consumer-facing |
| Facebook Marketplace + WhatsApp groups | All | n/a | Free | Reach; speed | No verification; scam risk |

**Gap:** No platform has dominant share in any single country, and no platform is genuinely cross-border. A regional brand could capture share quickly if backed by capital.

## Rent collection & payments

| Platform | Country | Model | Adoption |
|---|---|---|---|
| **Lipa Na M-Pesa Bills** | KE | Per-transaction fee | High among formal landlords |
| **KCB PesaLink** | KE | Bank-rail | <15% rent collection share |
| **Tingg (Cellulant)** | KE / UG / TZ | 1% transaction fee | Growing in SME |
| **MTN Uganda MoMo** | UG | Mobile-money | High |
| **Airtel Money** | Multi | Mobile-money | Moderate |
| **Selcom Pay** | TZ | Pilot | Early |
| **Nyumba Zetu** | KE | Landlord SaaS + M-Pesa | 2,000–5,000 users |

**Gap:** No regional rent-collection brand. A SaaS that wraps M-Pesa / MTN MoMo / Tigo Pesa / Airtel Money under one landlord dashboard, with auto-reconciliation against tenancy ledger, is still missing.

## Screening & credit

| Provider | Country | Cost | Adoption | Notes |
|---|---|---|---|---|
| **Metropol CRB** | KE | KSh 500–2,000 | <5% landlord | Loan-history focus, not rental |
| **TransUnion Kenya** | KE | KSh 1,000–3,000 | <3% landlord | Same gap |
| **Creditinfo Kenya** | KE | KSh 800–2,500 | <2% landlord | Same gap |
| **CreditInfo Uganda / Tanzania** | UG / TZ | varies | Negligible landlord | Bank-focused |
| **RentScore Africa** | KE | n/a (Baobab-funded 2024) | <1,000 landlords | Rental-specific scoring |
| Landlord WhatsApp / Telegram blacklists | All | Free | High informally | Discriminatory; DPA-2019 exposure |

**Gap:** A **rental-history-specific** credit product that tracks payment timeliness, deposit-refund history, eviction history per tenant, with proper DPA compliance, is the most obvious missing layer.

## Property management SaaS

| Tool | Country | Function | Adoption |
|---|---|---|---|
| **Nyumba Zetu** | KE | Listings + rent + ledger | 2,000–5,000 |
| **RentScore + Nesti** | KE | Screening + credit | <1,000 landlords |
| **Acorn (in-house)** | KE | Full PBSA stack | Institutional only |
| **Estate Intel** | Africa-wide | Market intelligence | Institutional / analyst |
| Generic real-estate CRM (international) | All | Sales-focused | Limited rental fit |

**Gap:** A landlord-facing PMS that handles small portfolios (5–50 units) — listings, ledger, M-Pesa rent reconciliation, maintenance ticketing, caretaker payroll, statutory reminders (KCCA rates, KRA RIT, NSSF, SHIF) — does not yet exist as a category leader.

## Tenant-side platforms (relevant for landlord research)

| Platform | Country | Function | Notes |
|---|---|---|---|
| Hakijamii | KE | Housing-rights advocacy | NGO; legal aid for slum tenants |
| Justice Centres Uganda | UG | Legal aid | Includes tenant disputes |
| Kenya Legal Aid | KE | Legal aid | Limited rental coverage |

**Implication for landlords:** The tenant-side legal-aid layer is thin. Landlords face less institutional pressure than they would in jurisdictions with stronger tenant unions.

## Industry associations & MLS

- **AREA Uganda** — most active landlord-side professional body in the region
- **KPDA (Kenya Property Developers Association)** — developer-focused; less landlord-of-existing-stock voice
- **EARB (Kenya Estate Agents Registration Board)** — licensing, not advocacy
- **LATAK (Kenya Landlords & Tenants Assoc.)** — Facebook page; informal
- **Real Estate Agents Association Tanzania** — emerging

**Gap:** No East African Community–level landlord federation. Cross-border lessons don't propagate; regulatory arbitrage between KE and UG goes unmonitored.

## Reddit-scraping methodology note

The Pass-1 sub-agent attempted real-time Reddit-quote extraction following the Medium article methods (PRAW, Pushshift archives, Apify scrapers). Constraints encountered:

- **PRAW** requires Reddit OAuth and respects rate limits (~60 requests / minute)
- **Pushshift** is largely deprecated; archives partial post-2023
- **Apify Reddit Scraper** is paid and requires explicit auth
- **Search-engine-indexed Reddit** is the fall-back used here — captures themes but not all quotes

**For a future pass:** running PRAW with auth credentials to pull the top 200 posts in r/Uganda, r/Kenya containing keywords (landlord, tenant, eviction, deposit, broker) would yield several hundred quotable comments — the highest-leverage incremental research move on the social-source axis.

## Strategic synthesis

The **largest unaddressed PropTech gap in EA** is a vertically integrated landlord OS for the 5–50 unit segment that:

1. Imports M-Pesa / MoMo / Tigo Pesa / Airtel Money rent payments
2. Reconciles against tenancy ledger automatically
3. Generates statutory reminders (KCCA rates, KRA RIT, NSSF, SHIF, NEMA)
4. Handles tenant screening via a rental-specific bureau
5. Generates compliant tenancy agreements (UG L&T Act 2022, KE pending Bill)
6. Manages maintenance tickets with caretaker payroll
7. Files deposit-escrow documentation usable by Tribunal / Small Claims Court

No single existing product covers all seven. The closest are Nyumba Zetu (KE, 1–3 layers) and Real Muloodi (UG, 1 layer). Whichever platform consolidates 5+ of those seven layers wins the category.
