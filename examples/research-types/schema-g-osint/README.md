# Schema G Exemplar - OSINT

Last verified: 2026-07-08
Benchmark: OCCRP/ICIJ-style open-source research dossier adapted for lawful civilian use.

## Context

The OSINT brief verifies public claims about border operations and programme actors. It avoids private surveillance and records provenance for each digital artefact.

## Wave Log

| Wave | Purpose | Output |
|---|---|---|
| 1 | Open-source lead collection | Search log and artefact register |
| 2 | Provenance tracing | Earliest-known source chains |
| 3 | Verification | Archive, metadata, reverse-search, entity checks |
| 4 | Synthesis | Claim confidence table and unresolved gaps |

## Evidence Table

| Claim ID | Claim | Evidence type | Verification status |
|---|---|---|---|
| G-C1 | Earliest source matters more than most-shared source. | Method rule | Enforced |
| G-C2 | Image claims require provenance checks. | Verification rule | Apply EXIF/reverse search |
| G-C3 | Private-person data requires safety review. | Ethics rule | Mandatory |

## Final Report Specimen

The dossier should distinguish a verified public record from a plausible social-media lead. The reader must be able to follow each claim back to the original or earliest available source.

## Gate Verdict

Status: pass as exemplar. Live report fails if it exposes private individuals unnecessarily or lacks provenance chains.

See also: `skills/osint-investigation/SKILL.md`, `tools/verification/provenance.py`.
