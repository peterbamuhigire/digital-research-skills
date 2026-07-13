---
name: pi-investigation
description: Use when an authorised licensed private-investigator workflow needs lawful collection, chain of custody, and an evidentiary report; use osint-investigation for public-source reconnaissance and refuse unlicensed surveillance or harm-enabling requests.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# PI Investigation

Single entry skill for licensed private-investigator workflows — the subset of investigative work where the artifact must satisfy evidentiary scrutiny (court, regulator, employer, insurer). For lighter open-source recon, load `osint-investigation`. For corporate vetting, load `due-diligence`.

## When to use this skill

- The output may be entered as evidence (employment dispute, custody, insurance claim, regulatory enforcement, civil litigation).
- The collection method itself must be lawful and documented (interviews, surveillance, records subpoenas).
- The jurisdiction requires PI licensure and the engagement is run by or for a licensed PI.
- A formal report is required with chain-of-custody.

If none of these applies, do not invoke this skill — `osint-investigation` is enough.

## Mandatory first step

**Load `references/legal-and-ethical-bounds.md` before any planning.** Every jurisdiction has different licensure, recording-consent, GPS-tracking, and pretexting rules. The engine refuses outputs that violate the relevant jurisdiction's PI law.


## Pi Investigation Core Method Notes
| Stage | Reference | Output |
|---|---|---|
| Engagement scoping (legal posture, jurisdiction, licensure) | `references/legal-and-ethical-bounds.md` | Engagement letter; jurisdiction matrix |
| Evidence collection | `references/evidence-custody.md` | Per-item custody log |
| Chain-of-custody maintenance | `references/evidence-custody.md` | Hash chain, transfer log, storage record |
| Final report | `references/mcmahon-pi-report.md` | McMahon 10-section PI report |

## Chain-of-custody discipline (universal)

Detail in `references/evidence-custody.md`. The engine's default:

1. Capture: timestamp (UTC), capturer, location, method, raw artefact.
2. Hash: SHA-256 of the artefact at capture; record in custody log.
3. Storage: secure, access-logged, write-once where possible.
4. Transfer: every transfer logged with from / to / timestamp / reason.
5. Reproduction: copies hashed at production; copy hashes match originals.

A break in the chain disqualifies the artefact for evidentiary use.

## McMahon's 10-section PI report

Detail in `references/mcmahon-pi-report.md`. The canonical structure:

1. Title / engagement reference / classification.
2. Investigator identity and licence number.
3. Client and authorisation.
4. Scope and methodology.
5. Chronology of investigation.
6. Findings (factual, dated, sourced).
7. Evidence index (with custody status per item).
8. Limitations and disclaimers.
9. Conclusions (within scope, evidence-bounded).
10. Signature, date, attestation.

Each section has non-negotiable contents; detail in the reference.

## Lawful / unlawful boundary (engine refuses)

The engine **refuses**:

- Surveillance or tracking of private individuals without lawful authority.
- Pretexting for credentials or accounts.
- Recording in jurisdictions that require all-party consent without that consent.
- GPS tracking on a vehicle the subject does not own.
- Any output that would identify a private individual's home / schedule / family in a way that enables harm.
- Work for parties barred from the subject (restraining orders, no-contact orders).
- Surveillance during legally protected activity (legal counsel meetings, medical care, religious worship).

The engine **permits**, with discipline and licensure where required:

- Public-record collection.
- Lawful interview of willing witnesses.
- Surveillance in public places, in jurisdictions where licensure permits.
- Records subpoenas through counsel.
- Adverse-media collation.
- Licensed pretexting only where jurisdictional law permits and ethical guidelines require disclosure of what was permitted.

## Universal output rule

Every evidentiary item carries:

- Custody log entry (capture / hashes / transfers / storage).
- Source / collection-method declaration.
- Lawfulness attestation (jurisdictional rule satisfied).
- Date / time (UTC).
- Investigator identifier and licence number.

Items missing any of those are excluded from the evidentiary section; they may appear in supplementary sections only with the gap flagged.

## Universal anti-patterns

- Reporting evidence with no custody log.
- Treating an OSINT artifact as evidence without explicit downgrade ("for context, not for evidentiary use").
- Recording in a two-party-consent state without consent.
- Pretexting financial-account access (illegal in most jurisdictions, regardless of licensure).
- Following the subject onto private property without authority.
- Producing a report whose conclusions exceed the evidence on the file.
- Skipping the limitations section.
- Naming third parties (uninvolved family / friends) outside the engagement scope.
- Using social-media data with platform-TOS violations as evidentiary support.
- Cross-jurisdiction collection without licensure check per jurisdiction.

## Universal ship gate

- [ ] Engagement letter signed; scope, jurisdiction, lawful posture documented.
- [ ] PI licence verified for the relevant jurisdiction(s).
- [ ] Every artefact has a custody log entry from capture to report.
- [ ] Hash chain unbroken; copies hash-matched.
- [ ] Lawfulness attested per artefact.
- [ ] McMahon's 10 sections all present and complete.
- [ ] Conclusions stay within the evidence; no extrapolation.
- [ ] Limitations section honest and specific.
- [ ] Refusal-list audit: no unlawful surveillance, pretexting, tracking, or third-party identification.
- [ ] Engine-level guardrail (`source-evaluation/references/evidence-discipline.md`) run.

## Companion skills

- `source-evaluation` — mandatory pairing.
- `osint-investigation` — for the open-source layer.
- `due-diligence` — for corporate / financial diligence layered into a PI engagement.
- `report-and-proposal-craft` — for the report container.

<!-- dual-compat-start -->
## Use When

- Use only for an authorised licensed-PI engagement requiring evidentiary collection or reporting.

## Do Not Use When

- Do not assist unlicensed surveillance, harassment, stalking, unlawful entry, access-control bypass, or work that puts a private person at risk.

## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Engagement authority, licence basis, jurisdiction, lawful methods, scope, and evidence protocol | Licensed investigator or authorised client | required | Stop; provide no operational collection guidance |


## Workflow
1. Verify engagement authority, licensure, jurisdiction, proportionality, and prohibited methods.
2. Approve a collection plan and chain-of-custody record before gathering evidence.
3. Preserve originals, identifiers, transfers, and notes; stop on custody break or unlawful instruction.
4. Draft the report, separate observation from inference, and recover by marking unavailable evidence or uncertain custody.

## Capability Contract

Default to read-only planning and review. Field collection, contact, surveillance, evidence handling, submission, or publication requires explicit lawful authority and competent licensed personnel.

## Degraded Mode

Without verified licence, engagement authority, or custody evidence, return only a legal-and-ethical gap list and refuse operational steps.

## Decision Rules

| Choice | Action | Failure avoided |
|---|---|---|
| Authority or method legality is unresolved | Stop and obtain competent jurisdictional confirmation | Unlawful investigation |
| Custody record has a break | Label the item compromised and segregate it | False evidentiary reliability |

## Outputs

| Artefact | Consumer | Acceptance |
|---|---|---|
| Investigation plan, custody register, and formal report | Licensed investigator, counsel, or authorised client | Authority is recorded; each item has provenance and custody status; inference is labelled |


## Pi Investigation Evidence Notes
- Preserve authority, method approvals, collection logs, custody transfers, original-item identifiers, and review disposition.

## Quality Standards

Protect subjects, preserve originals, report limitations, and never imply admissibility or legality that has not been competently established.

## Anti-Patterns

- Beginning before licence and authority checks. Fix: stop at intake.
- Mixing original evidence with working copies. Fix: preserve and identify both.
- Filling a custody gap from memory. Fix: mark the break explicitly.
- Reporting inference as observation. Fix: label and explain the reasoning.
- Including unrelated private data. Fix: minimise and redact.

## Worked Example

For an authorised evidence review, assign each supplied item an identifier, record each transfer, preserve the original, and state any custody limitation.

## References

- [Evidence custody](references/evidence-custody.md)
- [Legal and ethical bounds](references/legal-and-ethical-bounds.md)
- [PI report structure](references/mcmahon-pi-report.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Consumer | Acceptance |
|---|---|---|
| Authority and custody record | Licensed investigator or counsel | Each item has provenance, transfers, and custody status |
