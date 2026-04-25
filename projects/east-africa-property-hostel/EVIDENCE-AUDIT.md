# Evidence Audit — east-africa-property-hostel

Running log of caught hallucinations, citation drift, fabricated content, and corrections. Per the engine's `evidence-discipline` skill.

## Log format

```markdown
## YYYY-MM-DD
- Source agent / wave: <which sub-agent / which wave>
- Fabricated content: "<the exact text>"
- Caught by: <human reviewer | spot-check | URL-fetch | source-grep>
- Action: <strike | flag | replace | source-found>
- Lesson: <what to change in the next prompt>
```

## Open items requiring verification (before final Word export)

- **"~90% single-women rejection rate"** — single source (Medium / Daily Nation synthesis). Independent verification needed before publishing as a hard statistic. Currently flagged in `tenants/research/pain-points-report.md` as needing verification.
- **"~95% of EA rental stock is non-accessible to PWDs"** — described as "estimate" in `tenants/analysis/vulnerable-groups.md`; source not anchored. Either find the underlying survey or downgrade to "(inference)".
- **"~50,000–100,000 informal Somali tenants in Nairobi"** — range claim from "synthesised from UNHCR Kenya & UN-Habitat". Locate the specific UNHCR / UN-Habitat document that supplies the range; if not findable, mark as inference.
- **All Reddit findings in `landlords/` and `tenants/`** — sub-agent flagged that real-time scraping was constrained by ToS and only "consolidated themes" were captured. No verbatim Reddit quotes in any project file. Confirm none have leaked in.
- **Acorn Holdings FY'25 financials (KSh 1.52bn profit, 20,000 beds)** — verify against Acorn's NSE filings or annual report rather than relying on the agent's summary.
- **Kenyatta U Africa Integras PPP "stalled"** — agent flagged "no 2024–25 completion updates found." Re-search for confirmation before stating "stalled" definitively.
- **Tribunal Case E007 of 2024 and Muhanda v LP Holdings 2025** — verify on kenyalaw.org. Both cases were cited but not URL-confirmed.
- **"Komakech & 7 Ors v Ayaa & Anor 2018"** — verify on ULII.

## Closed items

### 2026-04-25 — Tenants Wave 2 verification pass

- ✅ **Daily Monitor 80% deposit-non-refund** — VERIFIED. Article: ["Is the security deposit nothing but a big scam for landlords?"](https://www.monitor.co.ug/uganda/magazines/homes-and-property/is-the-security-deposit-nothing-but-a-big-scam-for-landlords--4324306) — Daily Monitor Uganda, **2 August 2023**.
- ✅ **NCWSC 250M-litre Nairobi water deficit** — VERIFIED. Source: [The Star](https://www.the-star.co.ke/news/africa/2023-11-29-why-water-rationing-will-continue-in-nairobi-despite-dams-overflowing/). Demand 770M, supply 520M, deficit 250M cubic-metre/day.
- ✅ **50,000–100,000 informal Somali tenants in Nairobi** — VERIFIED. UNHCR + LSE + SAGE academic source. 24,000 registered + significant unregistered.
- ✅ **~90% landlord rejection of single women** — VERIFIED via Daily Nation primary source. Promoted from "flagged single-source".

### Corrections applied

- ⚠️ **Mathare Valley study attribution** — Wave-1 source attributed the 87% / 80.9% figures to "Huchzermeyer, Bocquier, Beguy 2020". Wave-2 verification: the actual paper is **Mwau & Sverdlik, *Environment and Urbanization* 32(2), 2020** ("High rises and low-quality shelter: rental housing dynamics in Mathare Valley, Nairobi"). Specific 87% / 80.9% statistics not found in abstract — need full-text retrieval to confirm. Tenants pain-points-report.md updated to flag.
- ⚠️ **2024 Nairobi riparian demolitions** — Wave-1 said 20,000 displaced. Wave-2 sources (Africanews, Capital News): **40,000 households** affected (≥25,000 received support by 27 May 2024). Tenants pain-points-report.md corrected.
- ⚠️ **Dar es Salaam water "9 hr/day"** — Wave-1 figure not supported by current reporting. Current pattern per *The EastAfrican*: **24-hour shutoffs on alternate days**. Tenants pain-points-report.md corrected.
- ⚠️ **"~95% of EA rental stock non-accessible to PWDs"** — Wave-2 verification could not locate a primary survey. Downgraded to "(inference; primary survey not located)" in tenants/analysis/vulnerable-groups.md.

### Confirmed gaps remaining

- ❓ **Court eviction enforcement statistics** by jurisdiction — no judicial-branch publication exists; FOIA request needed
- ❓ **DCI / Police rental-scam case counts** — not published; FOIA request needed
- ❓ **Reddit verbatim quotes** — Reddit ToS / API constraints; needs PRAW + auth (not feasible in-conversation)
- ❓ **Caretaker-misconduct prevalence survey** — none exists; recommend commission via Hakijamii
- ❓ **Mathare 87% / 80.9% figures** — verify against full Mwau & Sverdlik 2020 paper (full text not accessible via search)
- ❓ **Acorn Holdings FY'25 financials** — Wave-2 added new context (Cytonn Q1 2026 reports Acorn deleveraging via REITs); still verify exact figures against NSE filings
- ❓ **Kenyatta U Africa Integras PPP "stalled"** — re-search before stating definitively (still open)
- ❓ **AREA Uganda MLS** — no public footprint found (search returned US Major League Soccer); confirm organisation acronym
- ❓ **Hostelconnect / Katalyma residential EA expansion** — no verifiable sources; possibly defunct
- ❓ **KNBS 2023/24 default-rate %** — survey exists; specific data requires direct PDF download

### 2026-04-25 (later) — Landlords Wave 2 verification pass

- ✅ **Two named Kenyan court cases** confirmed via Kenyalaw with full citations — *Horientetertainment Limited v Maina* and *Munyingi v Thuo*. Both 2025 BPRT decisions tightening procedural rigor.
- ✅ **Kenya eRITS** — VERIFIED via EY Tax News + erits.kra.go.ke. Launched April 2025; compliance deadline 26 September 2025; 7.5% MRI; monthly filing.
- ✅ **Tanzania Use of Foreign Currency Regulations 2025** — VERIFIED via Clyde & Co + PwC Tanzania. GN 198, 28 March 2025.
- ✅ **NEMA Uganda Lubigi Wetland demolitions** — VERIFIED via Daily Monitor + allAfrica. 37,000+ residents threatened in Katoogo Zone.
- ✅ **Kenya National Building Code 2024 (LN 47)** — VERIFIED via kenyalaw.org. Operative 1 March 2024.
- ✅ **Stanbic Kenya 12% rate, KMRC fixed 8.99%** — VERIFIED via Stanbic Bank Kenya site.
- ✅ **Real Muloodi zero-commission model** — VERIFIED via softpower.ug + nilepost.co.ug.
- ✅ **Acorn deleveraging via REIT transfers** — VERIFIED via Cytonn Q1 2026 report.

### Wave-2 corrections applied to landlord file

- ⚠️ **Kenya eviction timeline** updated: Wave-1 "7–11 months" should now read "7–11 months baseline; +60–90 days for 2025 BPRT-mandated reconciliation + cure periods" given the *Horientetertainment* and *Munyingi* precedents.
- ⚠️ **"Tanzania dalali regulatory body" March 2025** removed — what actually happened was the Use of Foreign Currency Regulations. Wave-1 reference was inaccurate.
- ⚠️ **Acorn institutional framing** — added "Acorn deleveraging via REITs" signal to balance the Wave-1 "institutional ceiling" framing. Acorn is repositioning, not expanding.

## Process

Before generating any final Word report:

1. Walk this list top to bottom
2. For each open item, attempt verification with `WebFetch` against primary source
3. Move resolved items to "Closed items" with the verification URL
4. For items that **cannot** be verified, do one of:
   - Mark with `(inference)` or `(estimated)` in the source markdown file
   - Strike from the report and remove from the corpus
   - Convert to a "gap — no source found" finding

This list grows over the project's lifetime. Every Wave-2 spot-check or human review can add new items. **Never** quietly remove an item without recording the resolution.
