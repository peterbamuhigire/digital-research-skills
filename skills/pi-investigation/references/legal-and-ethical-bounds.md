# PI legal and ethical bounds

McMahon's doctrinal layer + post-2001 modern overlay. The book predates GLBA enforcement, *US v. Jones*, and HIPAA criminal penalties — those are layered on top.

## The ten doctrinal pillars

1. **Defamation (slander/libel)** — strict accuracy required, or qualified privilege. Common-name confusion is the #1 PI defamation vector.
2. **False imprisonment / false arrest** — PI has no arrest power beyond citizen.
3. **Trespass** — never enter private property without consent.
4. **Assault & battery / negligent firearm use**.
5. **Invasion of privacy** — three triggers: unreasonable / obstructive surveillance, surveillance disturbing average sensibility, surveillance for non-legitimate purpose.
6. **Wiretapping & eavesdropping** — *Katz v. United States* (1967): Fourth Amendment protects reasonable expectation of privacy. Title III §2518: written, sworn, AG approval (federal) or principal prosecutor (state), 30-day max, must minimise innocent communication.
7. **Pen registers** — *Smith v. Maryland*: no expectation of privacy in numbers dialed; ECPA still requires court order for evidentiary admissibility.
8. **Beepers / GPS tracking** — *US v. Knotts*: monitor on **public roads** OK without warrant; *US v. Jones* (2012, post-McMahon): warrant required for government tracking. State PI statutes vary (CA Penal §637.7, FL §934.425 require consent).
9. **Recording laws** — one-party-consent vs two-party-consent. Two-party states: CA, CT, FL, IL, MD, MA, MI, MT, NV, NH, PA, WA. Default: never record audio without all-party consent.
10. **Disclosure of communications/documents** generated in investigation — discoverable.

## Modern overlay (post-McMahon — engine MUST add)

| Statute | Prohibits |
|---|---|
| **GLBA §521 (15 USC 6821)** | Pretexting financial information — federal crime |
| **HIPAA (42 USC 1320d-6)** | Pretexting medical records — federal crime |
| **Telephone Records and Privacy Protection Act 2006** | Pretexting phone records |
| **DPPA** | DMV-data permissible-purpose required (PI exemption §2721(b)(3)/(b)(8)) |
| **FCRA §604** | Permissible-purpose required for credit-style reports |
| **CFAA** | Accessing accounts even with leaked credentials = federal crime |
| **State stalking statutes** | Surveillance + intent to cause fear = criminal |

## State licensing

- US: most states require PI licence; **8 states do NOT** (county/municipal licences may apply)
- Florida model: A-license (agency, liability insurance) + C-license (individual, 2 years experience) + CC-license (intern, 2 years under C)
- Pennsylvania: county-level
- **No federal PI license** — investigative work in a state where you're unlicensed = often a misdemeanour
- Reciprocity is partial; check before each engagement

## Lawful vs not — quick reference

| Activity | Lawful? |
|---|---|
| Public-records research | ✅ |
| Surveillance from public roads | ✅ |
| Recording in one-party state when investigator is party | ✅ |
| Recording in two-party state without consent | ❌ Criminal |
| Trash on public curb (post-*Greenwood*) | ✅ (some local exceptions) |
| Trash on private property | ❌ Trespass |
| GPS on subject's vehicle without consent | ❌ State stalking statute |
| Pretexting bank for financial data | ❌ GLBA federal crime |
| Pretexting medical records | ❌ HIPAA federal crime |
| Calling competitors as customer for sales info | ✅ (legal, ethics-flagged) |
| Misrepresenting at trade show with false nametag | ❌ Ethics violation |
| Pulling credit report for employment without consent | ❌ FCRA federal violation |
| Wiretapping without Title III order | ❌ Federal crime |
| Pen-register evidence without ECPA court order | ❌ Inadmissible |

## The CRAWL "C" rule (Hetherington)

Before any investigation: *Communicate* the scope and sign an engagement letter. The "C" is the boundary fence — outside the engagement scope = outside lawful authority.

## Anti-patterns

- "We always do it that way" — case-by-case is required
- Stretching a permissible-purpose to fit a different use
- Using leaked data because it's "available"
- Pretexting on the assumption that detection is unlikely
- Surveillance + GPS + audio combined to defeat a target who has explicitly asked for privacy
- Operating in a state where unlicensed
- Recording calls without verifying state law

## Decision rules

- **When unsure**, **stop**. Consult counsel.
- **Document the legal basis** for every protected-data access in the case file.
- **Refuse** the engagement when the lawful path doesn't exist.

## See also

- `dd-legal-and-ethics-baseline` — DD-specific layer above this
- `evidence-discipline` — engine-wide rule
- `evidence-custody-discipline` — what happens after lawful collection
- `dd-client-engagement` — the SOW + NDA + engagement letter that scopes lawful authority
