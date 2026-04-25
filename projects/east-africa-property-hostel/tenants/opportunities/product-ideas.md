# Product opportunities — residential tenants

Hypotheses to test. Each idea names the pain, who feels it, and likely failure modes. Cross-references the symmetric `landlords/opportunities/product-ideas.md` where applicable, since several ideas relieve both sides.

## 1. Deposit escrow + structured-inspection refund

**Pain served:** C1 (80% UG non-refund), C2 (vague damages deductions), C3 (landlord disappears)

**Hypothesis:** A neutral mobile-money escrow holds the deposit. Move-in and move-out happen with a structured photo / video inspection. Refund is determined by checklist + photo evidence. Disputes go to a panel before Tribunal / Small Claims Court.

**Why it might work:**
- The 80% Uganda non-refund stat is the sharpest single pain in this entire repo
- Uganda L&T Act 2022 already mandates 30-day refund — product productises law
- Kenya jurisprudence (Tribunal E007/2024 + Muhanda v LP Holdings 2025) gives 60-day Small Claims Court route
- Mobile-money escrow technically straightforward in KE / UG / TZ / RW

**Why it might fail:**
- Voluntary adoption requires landlord buy-in; they currently keep the deposit
- Mobile-money escrow regulation varies by country (KE most permissive)
- Single-side roll-out doesn't break the equilibrium — needs anchor distribution

**Cheap test:** WhatsApp-based concierge for 50 tenants entering new leases in Kampala / Nairobi. Match with a small set of pre-vetted landlords. 12-month observation cycle.

**Cross-ref:** `landlords/opportunities/product-ideas.md` #3 — same product viewed from supply side.

---

## 2. Verified-listing marketplace + landlord KYC

**Pain served:** A1 (viewing fees), A2 (30% UG fake listings), A3 (multi-deposit scam), A4 (holding-fee theft)

**Hypothesis:** Listings are verified by a local agent (physical visit, owner KYC, photo / video, registration check). Tenants can pay a flat marketplace fee instead of per-property viewing fees. Brokers can list on the platform but must register and accept conduct rules.

**Why it might work:**
- 30% fake-listing rate in Uganda is large and obvious
- Trust is the missing variable; existing platforms (Property24, BuyRent, Lamudi) don't verify
- Tenant willingness-to-pay is real — they already pay viewing fees with no guarantee

**Why it might fail:**
- Two-sided cold start
- Verification cost is high relative to listing margin
- Brokers have entrenched incentives against transparency

**Cheap test:** Concierge service for 100 freshers / new movers in Kampala. Manual property verification per request. KSh 1,000 / month subscription.

---

## 3. Tenant-side credit / payment-history record

**Pain served:** A5 (discrimination), feeds tenant counter-signal to landlord screening

**Hypothesis:** A tenant-permissioned record of on-time rent payments, deposit-refund outcomes, and tenancy history. Tenants opt in. They can share the record with prospective landlords as a counter to discrimination by group.

**Why it might work:**
- Single women, refugees, single mothers, PWDs all face stereotype-based rejection — payment data counters stereotypes
- Symmetric to `landlords/opportunities/product-ideas.md` #1 — same data, viewed from each side
- DPA-2019 compliant by design (tenant consent at every step)

**Why it might fail:**
- Critical-mass problem (need landlord acceptance + tenant adoption simultaneously)
- Discrimination may be too entrenched for data alone to fix
- Privacy concerns from tenants

---

## 4. Tenant rights chatbot + legal-aid triage

**Pain served:** D1 (<30% awareness), D3 (legal-aid scarcity)

**Hypothesis:** WhatsApp / SMS / Telegram bot that answers tenant questions on rights under the relevant statute, generates demand letters, and triages to Hakijamii / Justice Centres / appropriate paralegal when escalation is needed.

**Why it might work:**
- Awareness is the single largest structural gap
- Distribution via WhatsApp is essentially free in EA
- Pairs naturally with NGOs already doing legal aid

**Why it might fail:**
- Hard to monetise; relies on grant funding or NGO partnership
- AI-generated legal advice carries liability risk
- Tenant trust must transfer to a chatbot — non-trivial

**Cheap test:** Curated FAQ bot for Uganda L&T Act 2022 in Luganda + English. Free. Distribute via Justice Centres Uganda WhatsApp channels. Track question volume + escalation rate.

---

## 5. Class-action / collective dispute platform

**Pain served:** C7 (mass demolitions), C8 (election-cycle evictions), D2 (no tenant union)

**Hypothesis:** A platform that aggregates tenants in a single building / block / informal settlement facing simultaneous landlord or state action — collective representation, shared legal cost, joint Tribunal / Court filings.

**Why it might work:**
- 2024 Nairobi riparian demolitions (20,000+ displaced) is exactly the case for this
- Existing slum federations (Muungano wa Wanavijiji, Akiba Mashinani) provide ready partners
- Cost-per-tenant of legal action drops dramatically when shared

**Why it might fail:**
- Class-action procedural infrastructure is weak in EA
- Political risk in confronting state-led demolitions
- Funding model unclear

---

## 6. Accessible-building register

**Pain served:** PWD cohort (~95% inaccessible stock)

**Hypothesis:** Opt-in landlord register of accessibility-certified buildings. Listing premium passed to landlord; certified buildings command rent stability via reduced vacancy.

**Why it might fail:**
- Small addressable market in absolute numbers
- Capital cost of retrofit large for landlords
- Better as a layer on top of #2 than as standalone

---

## 7. Refugee-tenant legal-aid partnership

**Pain served:** Refugee-cohort discrimination + tenancy disputes

**Hypothesis:** Partnership with UNHCR / UN-Habitat / RefuSHE / HIAS to extend legal-aid services into rental disputes specifically. Funded via humanitarian grants rather than tenant fees.

**Why it might work:**
- 50,000–100,000 informal Somali tenants in Nairobi alone
- Humanitarian funders are looking for housing-vertical leverage
- Existing infrastructure can be extended rather than built

**Why it might fail:**
- Donor cycles short
- Pilot expansion challenging beyond 1–2 settlements
- Political risk (refugee policy is a domestic flashpoint)

---

## 8. Rent-abatement claim service

**Pain served:** B4 (water deficit), B5 (power outages), B12 (no remedy)

**Hypothesis:** Service that documents utility failures via tenant photo / smart-meter logs, generates abatement claim against landlord, and (where law allows) escrows the abatement amount.

**Why it might fail:**
- No EA jurisdiction explicitly provides rent abatement for utility failure
- Landlords can argue water / power are utility-company failures, not landlord obligations
- Hard to scale without statutory backing

**However:** A campaign for rent-abatement statute reform could be the policy companion to this product. Uganda L&T Act 2022 review window may open in 2027.

---

## Two-sided ideas (relieve tenant + landlord pain together)

### 9. Verified marketplace with deposit escrow & reviews

Combines #1 + #2 + tenant-side credit (#3). Charged primarily to landlord (LTV higher). The most defensible single integrated bet.

### 10. Tenant-side credit feeding landlord screening

Symmetric to `landlords/opportunities/product-ideas.md` #1. Same dataset, two products, two willingness-to-pay segments.

---

## Strategic notes

- **Sharpest single pain:** C1 — deposit theft. Idea #1 has the cleanest hook.
- **Largest addressable market:** A2 / A3 fake-listing scams (30% UG), reachable via #2.
- **Highest leverage on inequality:** #3 + #4 + #5 — fix the asymmetry between organised landlords and atomised tenants.
- **Best NGO-partnership angle:** #4, #5, #7 — fundable via legal-aid donors not tenant fees.

## Next step

Pick one. 2-week discovery sprint: 30 tenant interviews (Nairobi + Kampala mix; spread across vulnerable cohorts), 10 landlord interviews, 3 NGO interviews (Hakijamii, Justice Centres, MRA). Decide go/no-go on evidence, not enthusiasm.
