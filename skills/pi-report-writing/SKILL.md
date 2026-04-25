---
name: pi-report-writing
description: Use to assemble a court-ready PI report — 10-section canonical structure with case-type variants (matrimonial / background / DD / fraud / insurance), exhibit linkage, witness statements, photo logs, chain-of-custody affidavits. From McMahon's Practical Handbook for Private Investigators.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# PI report writing

McMahon's canonical 10-section structure. Distinct from DD report (which is `due-diligence-report-architecture`); PI reports anticipate court testimony.

## The 10 required sections

1. **Identifying header** — file#, date, type of case, client info, fee/financial arrangement, investigator credentials
2. **Subject block** — full name, aliases/maiden, DOB, SSN, DL#, distinguishing features (HT/WT/race/hair/eyes/build/glasses/facial hair)
3. **Purpose / scope statement**
4. **Investigative steps** (chronological): each step with date, source, method
5. **Findings** by topic: address verification, education, employment, criminal, civil, workers-comp, DMV, surveillance, etc.
6. **Source-credibility assessments** per finding; preliminary vs verified
7. **Photographs & video** with photo log (case#, date, location, photographer, photo#, lens, ISO/film, flash, description)
8. **Witness statements** attached as exhibits — signed, page-numbered ("page __ of __"), free-and-voluntary closer
9. **Recommendations / further-investigation plan**
10. **Investigator signature & credentials**

## Case-type variants

| Variant | Distinct sections |
|---|---|
| **Background check** | Education verification (registrar-confirmed), resume-vs-record gap analysis |
| **Matrimonial / domestic** | Residency timeline, child-custody factors, asset dissipation; safety-flag prompts |
| **Insurance / SIU** | Surveillance video log with "no audio" attestation, claimant-activity matrix, recorded-statement transcripts |
| **Fraud / corporate** | M.O.M.M. framework (motivation/opportunity/methods/means), corporate-fraud taxonomy bucket |
| **Service of process** | Return-of-service affidavit per state; description capture; attempt log with GPS |
| **Skip-trace** | Database chain, interview chain, found-address verification |

## Exhibit linkage

Every report attachment is referenced inline:
- Photographs: *Exhibit A — Photo log* (use `tools.pi.PhotoLog`)
- Witness statements: *Exhibit B — Witness statement of [name]* (use `tools.pi.build_statement`)
- Chain of custody: *Exhibit C — Chain-of-custody affidavit* (use `tools.pi.ChainOfCustody.to_affidavit`)
- Surveillance log: *Exhibit D — Shift log* (use `tools.pi.SurveillanceLog`)

## Citation discipline (court-ready)

- Every factual claim cites date + source
- Hearsay marked as such
- Direct observation marked: *"Investigator observed at 14:30 EAT, 25 April 2026, that..."*
- Photographs cross-referenced to photo log
- Statements cross-referenced to witness exhibits
- Surveillance findings cross-referenced to shift log

## Standard usage (PI report flow)

```python
from tools.pi import ChainOfCustody, build_statement, PhotoLog, SurveillanceLog

# Each exhibit type produces its own DOCX
chain.to_affidavit("exhibit-c-coc.docx")
build_statement(witness_statement, output_path="exhibit-b-statement.docx")
photo_log.to_docx("exhibit-a-photolog.docx")
surveillance_log.to_docx("exhibit-d-shiftlog.docx")

# Then assemble the master report referencing all exhibits.
# (PI report builder is a roadmap item — for now, hand-assemble using
# professional-word-output skill.)
```

## Anti-patterns

- Conclusions without observation (everything must trace to a step)
- Hearsay reported as fact
- Exhibit references that don't link to actual exhibits
- Investigator opinions stated as findings (mark as opinion)
- Missing investigator signature + credentials block
- No subject distinguishing features (insufficient for identification at trial)
- Unsigned witness statements
- Photographs without photo log

## Court-readiness checklist

Before submitting:
- [ ] Investigator signed
- [ ] Subject identifiable (distinguishing features in block)
- [ ] Every finding cites date + source + credibility
- [ ] Every photograph referenced + logged
- [ ] Every statement referenced + signed
- [ ] Chain-of-custody affidavit attached for any physical evidence
- [ ] Surveillance shift log attached if surveillance performed
- [ ] No hearsay reported as direct observation
- [ ] Recommendations clearly distinct from findings

## See also

- `tools/pi/` — chain-of-custody, witness-statement, photo-log, surveillance-log builders
- `evidence-custody-discipline` — chain-of-custody discipline
- `court-testimony-preparation` (roadmap) — taking the report to the stand
- `due-diligence-report-architecture` — DD-grade variant
- `professional-word-output` — final DOCX rendering
