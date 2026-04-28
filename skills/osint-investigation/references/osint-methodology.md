# OSINT methodology

Open-source intelligence is research with **operational consequence**. The findings may be used to make security decisions, journalism, or investigation. The standards differ from market or pain-point research.

## What OSINT covers

- **Person profiling** — identification, employment history, online footprint, contact details, associates
- **Organisation profiling** — corporate structure, key personnel, operational footprint, public claims vs reality
- **Domain / infrastructure** — DNS, hosting, certificates, registrar, related domains, IP neighbourhoods
- **Geolocation** — image, video, and text-based location identification
- **Network mapping** — relationships between any of the above

## Legal & ethical guardrails

- **Open source only.** No purchased / leaked / breached / hacked data.
- **No social engineering.** Even if technically open, manipulating a target into revealing information is out of scope.
- **No active interaction with the target.** Passive collection only.
- **No PII publication unprovoked.** Findings are research outputs, not exposés.
- **Respect platform ToS.** Reddit, X, LinkedIn, Facebook all have ToS limits — note them.
- **Deconfliction.** If multiple researchers / orgs may be working a target, surface this in the brief.

## Standard sources

- **Person:** LinkedIn, GitHub, Twitter/X, Mastodon, archived blogs, conference attendance lists, paper authorship, court records, professional registries, alumni directories
- **Org:** Companies House (UK), corporateaffairs (KE), URSB (UG), BRELA (TZ), SEC filings, regulator registers, news archives, NGO disclosures
- **Domain:** WHOIS, DNS records, certificate-transparency logs (crt.sh), Wayback Machine, archive.today, BuiltWith
- **Geolocation:** Google Earth historical, Sentinel Hub, Yandex reverse-image, OSM, Mapillary, Bellingcat tooling
- **Network:** Maltego, Shodan, Censys

## Verification rigour

- **Identification first.** A misidentified target is the most common OSINT failure. Never proceed past this step on weak ID.
- **Triangulate every claim.** Cross-reference any single-source finding before promoting it past "indicative".
- **Confidence ratings per finding.** High (multi-source verified), Medium (single tier-1/2 source), Low (single tier-3+ source).
- **Document temporal context.** Information dates fast in OSINT — every finding gets a timestamp.
- **Distinguish association from causation.** "X follows Y on Twitter" ≠ "X works for Y".

## Output structure

- `<project>/research/osint-targets.md` — target list with disambiguation
- `<project>/research/footprint.md` — per-target online footprint
- `<project>/research/network.md` — relationships
- `<project>/research/infrastructure.md` — technical (where applicable)
- `<project>/research/confidence-log.md` — per-finding confidence + sources
- Final Word doc uses Schema G

## Operational security caveats

- **Note any tool used that may reveal researcher identity** — Shodan / Censys queries leave logs
- **Pivoting via VPN / Tor** is the researcher's choice, not the engine's; document the chosen posture

## Hetherington Phased Approach — working overlay

Cynthia Hetherington's *Guide to Online Due Diligence Investigations* (Facts on Demand Press, 2nd ed., 2015) gives a useful client-facing compression of the OSINT cycle for investigations that may run into corporate or personal background work. The phased approach maps cleanly onto the engine's `plan → collect → analyse → disseminate` loop and pairs naturally with the `due-diligence` skill's CRAWL framework.

| Phase | Name | What it covers | Stop signal |
|---|---|---|---|
| **1** | Preliminary / Online Due Diligence | Internet research, social-network searches, US/foreign government databases, local media, online litigation research for relevant jurisdictions; written memorandum of issues identified | Most assignments end here. ~95 % of investigator daily work sits in Phase 1. |
| **2** | Comprehensive / Boots-on-the-Ground | Reference contacts, court retrievers in every jurisdiction the subject lived or worked in, hard-copy records pulled from offline registries (~32 % of US courts are not online; ratio is far higher outside the US) | Continues only if Phase 1 surfaces anchor points needing physical verification. |
| **3** | Recommended Next Steps | Subject-interview, former-employer outreach, ongoing monitoring, escalation per discovery (e.g., evidence of a CEO's gambling habit triggering a deeper personal-conduct review) | Closes when the named risk has been resolved or formally escalated. |

The phases are **client-facing units of cost and consent**, not separate analytic stages. Every phase still runs `plan → collect → analyse → disseminate` internally; the boundaries exist so the client can stop at any point with a clean deliverable.

### Universal investigation scaffold (Hetherington ch. 1)

Every Phase-1 OSINT pass on a person works through this checklist before concluding:

**Personal identifiers and assets** — name (incl. aliases / former names), date of birth, social-security or national-ID number (only as lawfully accessible), home address (incl. past addresses), contact numbers, family members, corporate ownership / partnership / business involvement, gift donors and beneficiaries (≥ a stated threshold), professional-association affiliations and tenure, educational certification and membership verification, automobiles / vessels / planes, property ownership.

**Financial history** — personal debt, real-property interests (incl. mortgages held), outside business interests, local / state / federal tax liens, recorded judgments and liens, bankruptcy or financial-insolvency records.

**Civil and criminal filings** — criminal convictions, pending or post-civil / criminal / administrative actions, racketeering / unfair-trade-practice proceedings, federal or state regulatory actions, association with known organised-crime affiliates or politically exposed persons (PEPs).

A Phase-1 deliverable that has not at least *attempted* every line in this scaffold has a reporting gap. Where a line is intentionally skipped (legal, ethical, scope), say so explicitly in the report — silence is not a closing argument.

### Four "necessary ingredients" for the investigator (Hetherington ch. 1)

1. **Critical / analytical thinking, imagination, raw determination.** Investigations are not for the lazy; the difference between a finished case and a stalled one is a willingness to push through the mounds of detail.
2. **Computer proficiency.** Beyond word processors and spreadsheets — knowing how the web, email transmission, and information storage actually work changes the questions you can ask.
3. **Speaking the language.** Distinguish a docket from a disposition; understand the business community and industries you operate in. A seasoned investigator sounds like an attorney when discussing the public record.
4. **Access to the best databases.** Some free (LinkedIn for resume validation), some paid (LexisNexis-aggregated public records, Accurint, IRBsearch). Subscriptions are means, not ends — the test is whether the investigator can answer on-the-spot client questions about each finding.

### Recommended-Next-Steps section

Every Phase-1 and Phase-2 report ends with a **Recommended Next Steps** block that lists tangent leads, monitoring suggestions, and escalation paths the engagement did not cover. This block is the bridge to the next phase (or the next engagement) and is the single most under-written section in junior OSINT reports.

## Source books

- Hetherington, *The Guide to Online Due Diligence Investigations: The Professional Approach on How to Use Public and Private Internet Resources*, 2nd ed., Facts on Demand Press, 2015 — chs. 1, 11.
- See also `due-diligence` skill, which carries the CRAWL framework and CARA report architecture from the same author.
- **Some sources require log-in** — don't use personal accounts for sensitive lookups

## Anti-patterns

- Passing OSINT off as due diligence (different rigour, different liability)
- Publishing PII without operational necessity
- Assuming a username connects across platforms without proof
- Using leaked data to verify claims (out of scope)
- Single-source identification

## See also

- `evidence-discipline` — non-negotiable
- `source-verification` — tier discipline
- `due-diligence-framework` — overlapping but stricter on liability
- `social-source-extraction` — feeds the social-platform layer
- `research-report-builder` — Schema G
