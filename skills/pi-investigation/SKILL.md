---
name: pi-investigation
description: Use for licensed private-investigator workflows where the artifact must survive evidentiary scrutiny — chain-of-custody, lawful collection methods, jurisdiction-specific licensure, McMahon's 10-section formal PI report. Three references; engine refuses unlicensed surveillance, harassment-enabling work, and any output that would put a private individual at risk.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
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

## Workflow

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
