# Public-Records Investigative Search

Use this guide for authorised investigative research into organisations and people through
public records: company registries, securities filings, courts, government agencies,
access-to-information requests and lawful people-finding. General search craft is in
`../../research-techniques/references/search-craft-and-deep-web.md`; registry coverage by country
is in `../../due-diligence/references/jurisdictional-registry-atlas.md`.

**Scope.** Lawful techniques only, for a documented, authorised purpose. Several lanes are
restricted by law; the legal flags below are mandatory checks, not footnotes.

## Inputs

- The subject (entity or person) with every known identifier: legal name, variants, registration
  number, addresses, directors, dates of birth where lawfully held.
- The purpose and legal basis of the enquiry, and who authorised it.
- Jurisdictions involved.
- Budget for paid registries and databases.

## Decision rules

1. **Classify the subject first.** Listed company, private company, non-profit, foreign entity,
   government body or individual. The class determines the primary source.
2. **Primary record over aggregator.** An aggregator or people-search site is a lead, never the
   citation. Confirm in the registry, court record or filing itself.
3. **Go through the coordinating body, not fifty websites.** In federal systems, national
   associations of state officials (secretaries of state, insurance commissioners, court
   administrators) maintain directories to each state's records.
4. **Names are not unique.** Match on at least two independent identifiers before attaching a
   record to a subject.
5. **Check the legal flag before the lookup,** and ask the user to confirm lawful purpose where a
   flag applies. The engine surfaces the source and the flag; it does not decide legality for
   the user.

## Procedure: organisations

1. **Registry.** Company registry in the country of incorporation and in each country of
   operation (a company incorporated in one jurisdiction may trade elsewhere as a foreign
   company). East Africa: URSB (Uganda), Business Registration Service (Kenya), BRELA (Tanzania),
   RDB (Rwanda). Elsewhere: Companies House (UK), state business-entity searches (US), SEDAR+
   (Canada), national commercial registers (EU). Capture registration number, status, officers,
   shareholders, registered address and filing history.
2. **Securities filings for listed companies.** US: SEC EDGAR. The annual report on Form 10-K is
   usually the single best overview; add 10-Q (quarterly), 8-K (material events), DEF 14A (proxy,
   including executive pay), S-1 (registration), Forms 3, 4 and 5 (insider transactions) and
   Schedules 13D and 13G (holders above 5%). East Africa: the Uganda, Nairobi, Dar es Salaam and
   Rwanda stock exchanges and the capital markets regulators publish listed-company disclosures.
3. **Security interests and property.** Collateral and lien registers (US UCC filings at state or
   county level; movable-property security registries where they exist), land registries and
   valuation rolls.
4. **Courts.** US federal dockets through PACER (paid per page; check the current fee schedule);
   state courts through state portals. East Africa: Kenya Law and ULII (Uganda Legal Information
   Institute) for judgments; cause lists and registries for pending matters.
5. **Regulators and licences.** Sector regulators (central banks, insurance, telecoms, energy,
   medicines, procurement authorities) publish licensee lists, sanctions and debarments.
6. **Non-profits.** US: IRS Tax Exempt Organization Search and Form 990 filings (also via
   Candid); East Africa: NGO bureaus and boards (for example Uganda's National Bureau for NGOs,
   Kenya's NGO Coordination Board or its successor).
7. **Industry codes.** Use SIC or NAICS (or ISIC) codes to filter filings and regulatory datasets
   by sector.
8. **Adverse media and sanctions.** Run `adverse-media-investigation.md` and `../../due-diligence/references/sanctions-pep-screening.md`.

## Procedure: people

1. Start from lawful, public, purpose-appropriate sources: registries (as officers or owners),
   court records, professional registers (medical, legal, engineering boards), gazettes,
   published directories and the subject's own public profiles.
2. Use one confirmed identifier to find the next (employer to professional register; address to
   land record), matching on two identifiers each time.
3. Treat commercial people-search results as unverified leads; confirm in a primary record.
4. For vital records (births, deaths, marriages), expect access limited to the subject, next of
   kin, executors and lawyers.
5. Build the chronology and residence history with `skip-tracing-craft.md`.

## Access-to-information requests

- **US:** Freedom of Information Act; the Department of Justice Office of Information Policy
  (justice.gov/oip) publishes agency contacts and guidance; the Reporters Committee for Freedom of
  the Press provides request templates and state-law guides; nine statutory exemptions
  (national security, internal personnel rules, other statutes, trade secrets, deliberative
  inter-agency memos, personal privacy, law-enforcement records, financial-institution
  supervision, and well data) are the usual refusal grounds.
- **East Africa:** Uganda's Access to Information Act 2005, Kenya's Access to Information Act
  2016, Tanzania's Access to Information Act 2016 and Rwanda's access-to-information law set
  request procedures and timelines; follow each agency's procedure exactly, since a procedurally
  defective request is a legitimate ground for refusal.
- Frame requests narrowly in scope and broadly in form ("all records, including emails and
  briefing notes, concerning X between dates").

## Legal flags (check before the lookup)

| Area | Examples |
|---|---|
| Vehicle and licence records | US Driver's Privacy Protection Act limits DMV data to permitted uses |
| Consumer reports | US Fair Credit Reporting Act governs data used for employment, credit, insurance or tenancy decisions |
| Financial records | US Gramm-Leach-Bliley Act; bank secrecy rules everywhere |
| Health records | US HIPAA; health-data provisions in national laws |
| Personal data generally | Uganda Data Protection and Privacy Act 2019; Kenya Data Protection Act 2019; Tanzania Personal Data Protection Act 2022; Rwanda Law No 058/2021; EU and UK GDPR |
| Pretexting and deception | Obtaining records under false pretences is unlawful in many jurisdictions |

Local law may be stricter than national or federal law. Defer to the user's counsel.

## Failure modes

Citing an aggregator instead of the record · attaching a record on name alone · skipping the
foreign-registration check · searching fifty state sites instead of the coordinating directory ·
a procedurally defective information request · relying on Google Scholar alone for case law
(verify in an official law report or a professional service) · pursuing a restricted lookup
without lawful purpose.

## Original worked example

Enquiry: a Kampala investor asks who controls a logistics company bidding for a warehouse lease.
- URSB search gives the registration number, two directors and a corporate shareholder
  registered in Kenya.
- The Kenyan Business Registration Service record for that shareholder shows a further
  individual shareholder; a match is accepted only after name and ID number agree across both
  registries' filings.
- ULII shows one commercial judgment against the Ugandan company; the procurement regulator's
  debarment list is clear. The report cites the registry extracts and judgment, not the search
  pages that led to them.

## Checklist

- [ ] Purpose and authorisation recorded; legal flags checked.
- [ ] Subject classified; primary source identified.
- [ ] Every record matched on two identifiers.
- [ ] Aggregator hits confirmed in primary records.
- [ ] Information requests follow the agency's procedure.
- [ ] Citations point to primary records with access dates.

Evidence and currentness: services named here were not all re-checked on 2026-09-24. Fee levels,
portal URLs and the continued operation of any named registry or portal: NOT_ASSESSED; verify at
task time. Services named in older manuals (several people-search sites and browser add-ons,
some agency lookup tools) have closed or been renamed and are deliberately omitted.

Sources: MacLeod (2012) *How to Find Out Anything*; BRB Publications *The Sourcebook to Public
Record Information*; statutes named above. Reorganised by task.
