# Reference — MacLeod Investigative Search

**Canonical source:** MacLeod, Don. *How to Find Out Anything: From Extreme Google Searches to Scouring Government Documents, a Guide to Uncovering Anything About Everyone and Everything*. Prentice Hall Press, 2012. Tier 1. Local extract: `extracted-books/macleod-find-anything.txt`.

This reference covers the **investigative** application of MacLeod's material — government records, people-finding, company records, FOIA, public records aggregators. The general search-craft layer (Google operator catalog, deep web heuristics, the reference-interview discipline) lives in `research-techniques/references/macleod-search-mastery.md`.

**Scope.** All techniques here are **lawful only** and oriented to authorised investigative work. Several techniques touch laws that constrain who may use them and for what purpose; those constraints are flagged inline.

## The government-records workflow (Ch 9)

MacLeod, Ch 9: "*Public records research is like a treasure hunt.*"

**Federal entry portal:** https://www.usa.gov/ — "A–Z List of Agencies". MacLeod's spine: executive agencies hold most usable data; courts and Congress are secondary.

### Federal layer

- **Rule-making.** Federal Register + Code of Federal Regulations via GPO (https://www.govinfo.gov/) and Regulations.gov.
- **Federal courts (dockets, filings).** PACER — https://pacer.uscourts.gov/. Subscription, ~$0.10/page, $3 cap per document. Docket-number format: `02 civ 0897 (JGM)`.
- **Legislation.** congress.gov (succeeded MacLeod-era Thomas at LoC) — bill tracking, summaries, lifecycle status.
- **Agency records by topic.**
  - FAA Airmen Inquiry — pilot certification.
  - EPA MyEnvironment — by ZIP.
  - FDIC Bank Find — bank charter lookup.
  - FMCSA SafeStat — DOT-number lookup for trucking.
  - FEC — campaign-finance disclosure.
  - BJS — Bureau of Justice Statistics.
  - USGS — geological / earthquake data.
  - BLS — labor statistics, CPI.
  - NCES — education statistics.
  - Census FactSheet.
  - ATF — firearms trace data.
  - SEC EDGAR — corporate filings (see Company workflow).

### State layer

Don't memorise 50 sites — go through the **national association of administrators** for that function:

- NASS — National Association of Secretaries of State (incl. corporate registries) — https://www.nass.org/
- NAIC — National Association of Insurance Commissioners — https://www.naic.org/
- NCSC — National Center for State Courts — https://www.ncsc.org/
- NCSL — National Conference of State Legislatures
- NASBO, NASDA, NAAG (attorneys general), CSBS (banking), AAMVA (motor vehicles), NCSLA (alcohol), ECOS (environment), ASCA (corrections), CCSSO (education), NGA, NCSHA (housing), ILSA (labor), NASMD (Medicaid), NASPD, APPA (parole), NASEO (energy), AASCU, FTA (tax), NASTD, AASHTO (transportation), IAIABC (workers' comp).

### County layer

~3,068 counties. Clerks hold:
- **UCC-1 filings** — mechanic's liens, tax liens, attorney's liens, judgment liens, maritime liens.
- **Real estate** — deeds, tax assessments, mortgages.

Example workflow (MacLeod's own): NYC ACRIS (Automated City Register Information System) → state SoS corporate records → Google owner name → triangulate on associated entities.

### FOIA

- **National Security Archive guide** — https://nsarchive.gwu.edu/.
- **Reporters Committee for Freedom of the Press FOIA Letter Generator** — https://www.rcfp.org/foia-letter-generator/.
- **DOJ Office of Information Policy** — https://www.justice.gov/oip.
- **Nine FOIA exemptions** (b)(1)–(b)(9): national defense, internal personnel rules, statutory exemption, trade secrets, inter-agency memos, personal privacy, law-enforcement investigatory records, financial-institution records, well data.
- **State FOI** — Reporters Committee state-by-state comparison guide.

### Sourcebook

*The Sourcebook to Public Record Information* (BRB Publications, Weber/Sankey) — MacLeod's bible for jurisdiction-by-jurisdiction record locations and procedures.

## The people-finding workflow (Ch 7) and legal sensitivities

MacLeod, Ch 7: "*When we talk about finding people, we're really talking about finding a person's indicators.*"

Ordered approach:

1. **Phone book first.** AnyWho (AT&T), 411.com (WhitePages). Landlines only.
2. **Reverse lookup** — phone → address → neighbours (the skip-trace technique).
3. **People-finder aggregators.** Pipl, Spokeo, Wink, Zaba Search, Intelius, Firefox add-on "Who Is This Person?".
4. **Social.** Facebook, LinkedIn, Classmates, X/Twitter.
5. **Vital records.** CDC's *Where to Write for Vital Records* — state agency directory. **Restricted access**: birth/death/marriage records limited to subject, kin, executor, lawyer.
6. **Asset & financial.** Salary.com, BLS National Wage Data, GuideStar (charitable donations from IRS Form 990), Foundation Center, SEC Forms 3/4/5 (insider trades), Form 13-D (5%+ holders), bankruptcy via PACER.
7. **Specialised populations.** State medical boards (via AMA); DEA "Criminal Cases Against Doctors"; FindLaw / Martindale-Hubbell for lawyers; *Directory of Federal Judges*; *American Bench*; FAA Airmen Inquiry; state inmate locators; National Sex Offender Registry; Marquis *Who's Who* / *Who Was Who*; Social Register; Social Security Death Index (RootsWeb); Obit Central; eVetRecs (NARA).
8. **Email-address guessing** — when you have name + employer.
9. **Commercial paid.** Accurint (LexisNexis), KnowX (LexisNexis), AutoTrackXP / CLEAR (Thomson Reuters).

### Legal flags MacLeod calls out

- **DPPA (Drivers Privacy Protection Act, 1994).** No public DMV / license-plate lookups. Narrow exceptions: court use, recall, market research (with restrictions), licensed PIs.
- **Fair Credit Reporting Act.** KnowX requires user attestation that data is not used for hiring / insurance / credit decisions.
- **Cell-phone numbers** are not in any public registry; reverse-cell only narrows to carrier / region.
- **Vital-records access** restricted to subject, kin, executor, lawyer.
- **Credit reports / bank records** off-limits without legal purpose (Gramm-Leach-Bliley Act).
- **HIPAA** — health information.
- **State analogues** — many states have stricter local laws than federal.

The engine **defers to user counsel** on whether a given lookup is lawful in the user's jurisdiction; the engine surfaces the source URL and the legal flag, and asks the user to confirm before pursuing.

## The company / business records workflow (Ch 8)

MacLeod, Ch 8: "*If you had to pick one single EDGAR document to provide the best portrait of a company, you'd choose Form 10-K.*"

### Step 1 — classify

Public, private, nonprofit, foreign. The classification points to the right primary source.

### Step 2 — public companies — SEC EDGAR

https://www.sec.gov/edgar/search-and-access. Search by company, ticker, CIK, file number, state, SIC.

Key forms:

- **10-K** — annual; the "single best portrait" per MacLeod.
- **10-Q** — quarterly.
- **8-K** — current report on material events.
- **DEF 14A / PRE 14A** — proxy statement, includes executive compensation.
- **S-1 / 424B** — registration & prospectus.
- **3 / 4 / 5** — insider transactions.
- **13-D / 13-G** — 5%+ beneficial owners.

Commercial repackagers: KnowledgeMosaic, Intelligize, Refinitiv Accelus.

### Step 3 — state corporate registries

Secretary of State business-entity search in every state, routed via NASS portal. Many corps incorporated in Delaware, operate elsewhere as "foreign corporations" — check both incorporation state and state of operation.

### Step 4 — UCC-1 filings

County clerks; reveal liens and secured interests — useful for understanding what assets the entity has pledged.

### Step 5 — court dockets

PACER (federal), state courts via NCSC. Bankruptcy is its own PACER lane.

### Step 6 — private companies

Hoovers, D&B, Mergent, Bureau van Dijk, Dun & Bradstreet, *Ward's Business Directory*, *S&P Register*. Coverage thin compared to public; cost rises sharply for true private-company depth.

### Step 7 — industry / products

ThomasNet, Industrial Quick Search, Household Products Database (NLM), *Ulrich's Periodicals Directory*, Special Issues (Gary Price's list of industry rankings).

### Step 8 — foreign companies

SEDAR (Canada), Companies House (UK), FCA (UK), AMF (France), KvK (Netherlands), Handelsregister (Germany). For East African focus the engine adds: BRS Kenya (Business Registration Service), URSB Uganda (Uganda Registration Services Bureau), BRELA Tanzania, RDB Rwanda.

### Step 9 — industry codes

SIC and NAICS — MacLeod stresses learning these for filtering EDGAR, OSHA Fatality Database, EPA pollutant data.

### Step 10 — nonprofits

GuideStar (Form 990), Foundation Center, IRS Pub 78 / Exempt Organizations Select Check, state attorneys general charities bureaus.

### Reference guides MacLeod points to

- UNT Library "Company and Industry Research" meta-guide.
- NYPL SIBL "Searching for Company Information".

## Specialty databases — investigative master URL list

**Government:** usa.gov, sec.gov/edgar, govinfo.gov, regulations.gov, data.gov, congress.gov, pacer.gov, fdic.gov "Bank Find," fec.gov, fmcsa.dot.gov SafeStat, epa.gov MyEnvironment, bls.gov, bjs.ojp.gov, usgs.gov, data.census.gov, nces.ed.gov, faa.gov Airmen Inquiry, aphis.usda.gov, atsdr.cdc.gov, justice.gov/oip.

**FOIA:** rcfp.org/foia, nsarchive.gwu.edu, justice.gov/oip.

**State-association portals:** nass.org, naic.org, ncsc.org, ncsl.org, nasda.org, naag.org, csbs.org, aamva.org, ncsla.org, ecos.org, nasbo.org, asca.net, ccsso.org, nga.org, ncsha.org, ilsa.net, nasmd.org, naspd.org, appa-net.org, naseo.org, aascu.org, taxadmin.org, nastd.org, transportation.org, iaiabc.org.

**People:** AnyWho, 411.com, Pipl, Spokeo, Wink, Zaba Search, Intelius, "Who Is This Person?" Firefox add-on, FindLaw, Martindale, AMA state boards, eVetRecs (NARA), RootsWeb SSDI, Obit Central, Find-a-Grave, NewspaperArchive, Ancestry.com, MyHeritage.

**Public-records aggregators:** BRB Publications, Knight Digital Media Center, NETR Online, Zimmerman's Research Guide, Accurint, KnowX, AutoTrackXP / CLEAR, Virtual Gumshoe.

## Investigative heuristics

- **Reference-interview yourself first.** What do you know; what don't you know; what kind of answer satisfies; what category does this belong to.
- **Convert open-ended questions into factual cascades.**
- **Scope first; finite scope = finite research.**
- **Use one fact to find another** — the detective leverage principle.
- **Domain-restrict everything** — `site:.gov`, `site:state.us`, etc.
- **Read internal references, footnotes, blogrolls.**
- **Double-source every nontrivial claim.**
- **Talk to people** — librarians, association staff, county clerks.
- **Mind the bias of every source.**
- **Look in archived/cached versions** when content disappears (Google cache vs. Wayback distinction).
- **Tenacity.**

## Anti-patterns

- Defaulting to a Google keyword search for any question, including ones Google structurally can't answer (deep-web data lives in queryable databases).
- Trying to brute-force public records without the *Sourcebook* or an aggregator.
- Filing FOIA requests without following each agency's specific procedure (legitimate grounds for refusal).
- Using Google Scholar for serious legal research (per MacLeod, Ch 3, "not ready for prime time" — verify against Westlaw / Lexis / Bloomberg Law).
- Assuming a name is unique or correctly spelled.
- Confusing Google cache with the Wayback Machine.
- Asking for the wrong document because of a missed reference interview (MacLeod's "general counsel" anecdote).
- Pursuing a lookup that violates DPPA, FCRA, GLBA, HIPAA, or state analogues.

## Quotable passages

1. "When we talk about finding people, we're really talking about finding a person's indicators." (Ch 7)
2. "If you had to pick one single EDGAR document to provide the best portrait of a company, you'd choose Form 10-K." (Ch 8)
3. "Public records research is like a treasure hunt." (Ch 9)

## Companion references

- `research-techniques/references/macleod-search-mastery.md` — the general search-craft layer.
- `research-techniques/references/russell-search-literacy.md` — metacognitive layer.
- `references/google-stakeholder-recon.md` — adjacent technique.
- `references/skip-tracing-craft.md` — the engine's own skip-tracing pattern, which builds on §People above.
- `references/adverse-media-investigation.md` — adjacent.

## Sources

- MacLeod, Don. *How to Find Out Anything*. Prentice Hall Press, 2012. Tier 1.
- *Sourcebook to Public Record Information*. BRB Publications. Tier 1.
