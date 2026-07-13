---
name: kenya-academic-research
description: Use when an academic proposal, thesis, dissertation, project, defence, or research-governance artefact must be checked against a named Kenya-based handbook; use primary-research for fieldwork design and source-evaluation for evidence quality.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Kenya Academic Research

Use this skill when an academic or applied-research artefact must meet Kenyan university or Kenya-based research-organization handbook expectations.

Always load `source-evaluation/references/evidence-discipline.md` first. All handbook-derived requirements must remain traceable to `references/kenya-handbook-standards.md`.

## Router

| Task | Load |
|---|---|
| Kenyatta University hospitality/tourism/leisure proposal or thesis | `references/kenya-handbook-standards.md` section "Kenyatta University" |
| Adventist University of Africa project, thesis, or dissertation | `references/kenya-handbook-standards.md` section "Adventist University of Africa" |
| Groundwater research project, data, authorship, publication, or PI conduct | `references/kenya-handbook-standards.md` section "Regional Centre on Groundwater Resources" |
| Viva / final oral defence | `references/kenya-handbook-standards.md` sections "AUA" and "Kenyatta University" + `academic-reporting-standards/references/viva-defense-preparation.md` |
| Ethics, plagiarism, publication integrity | `references/kenya-handbook-standards.md` sections "Ethics and integrity" and "Research-organization controls" |

## Operating Rules

1. Identify the target institution or organization before applying a format rule.
2. Do not merge AUA page ranges with Kenyatta University page/page-count rules.
3. Treat RCGW as a research-organization governance source, not a student thesis-format manual.
4. For Kenyatta University School of Hospitality work, enforce proposal page limits, APA style, plagiarism threshold, concept/proposal/thesis sequencing, and methodology justification.
5. For AUA work, distinguish project, thesis, and dissertation; each has different page ranges and defence-panel expectations.
6. For RCGW work, require research approvals, rigorous data handling, PI accountability, authorship discipline, peer review/validation, and publication integrity.
7. If the target institution is not named, use the Kenya default scaffold and mark institution-specific formatting as a gap.

## Companion Skills

- `academic-reporting-standards` for examiner-defensible dissertation logic and reporting checklists.
- `academic-writing` for APA, plagiarism prevention, paraphrase, and academic register.
- `research-design` for research design and report-building.
- `source-evaluation` for source credibility and anti-hallucination discipline.

<!-- dual-compat-start -->
## Use When

- Use when a named Kenya-based handbook governs an academic or research artefact.

## Do Not Use When

- Do not assume one institution's rules apply to another; use general academic skills when no Kenya-specific handbook governs.

## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Target institution, artefact, applicable handbook edition, and source register | Requester and verified handbook sources | required | Apply only general academic structure and mark institutional rules as gaps |

## Workflow

1. Identify institution, programme, artefact type, and handbook edition.
2. Load the matching section of the handbook standards reference and map each requirement to the draft.
3. Stop on conflicting, missing, or stale rules; verify before recommending a change.
4. Review in read-only mode, then edit only when authorised; recover from a missing rule by preserving the gap in the disposition record.

## Capability contract

Default to read-only review. Search and network verification may confirm current handbooks; editing, submission, or certification claims require explicit authority.

## Degraded mode

If the governing handbook cannot be accessed, return a general academic checklist with every institution-specific check marked not assessed.

## Decision rules

| Choice | Action | Failure avoided |
|---|---|---|
| Named handbook contains an explicit requirement | Apply and cite that requirement | Unsupported institutional rule |
| Handbooks conflict | Follow the governing institution and flag the conflict | Blended rule set |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Compliance matrix and authorised revision | Student, supervisor, or researcher | Each institutional finding cites the handbook section or is marked not assessed |


## Kenya Academic Research Evidence Notes
- Record handbook identity, requirement location, finding, disposition, and unresolved gap.

## Quality Standards

Do not claim institutional compliance from a generic checklist; preserve academic integrity and exact source traceability.

## Anti-Patterns

- Applying one university's format to another. Fix: identify the governing handbook.
- Citing a handbook without a requirement location. Fix: record the section or page locator.
- Treating a missing rule as permission. Fix: mark it as a gap.
- Editing before a read-only review is accepted. Fix: separate findings from remediation.
- Certifying plagiarism or ethics compliance without evidence. Fix: report only checks actually performed.

## Worked example

For a thesis review, map each heading and submission requirement to the named handbook section and leave unavailable defence rules marked not assessed.

## References

- [Kenya handbook standards](references/kenya-handbook-standards.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Consumer | Acceptance |
|---|---|---|
| Handbook compliance matrix | Student, supervisor, or researcher | Each finding has a handbook locator or not-assessed status |
