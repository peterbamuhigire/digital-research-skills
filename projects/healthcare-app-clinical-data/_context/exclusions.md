# Exclusions

**Date:** 2026-05-03

These exclusions are **hard**. They must be restated verbatim in every sub-agent brief. If a sub-agent returns excluded content, filter it out before writing project files. Track each filtering action in `EVIDENCE-AUDIT.md`.

## Hard exclusions (out of scope)

- **Veterinary medicine** — no animal-only conditions, drugs, lab tests, imaging, or procedures
- **Traditional / herbal medicine** — no traditional African medicine, herbal preparations, or complementary/alternative medicine items, regardless of cultural prevalence
- **Cardiothoracic surgery** — no open-heart, coronary bypass, valve, or major thoracic procedures beyond what a Ugandan regional referral hospital routinely performs
- **Neurosurgery** — no cranial surgery, spinal cord procedures, or specialist neurosurgical interventions
- **Transplant surgery** — no solid-organ or stem-cell transplant procedures, peri-transplant drugs, or transplant-specific lab tests

## Hard inclusions (explicitly in scope)

- **Dental procedures** — full inclusion using CDT codes (subject to ADA licensing flagged in the procedures report)

## Edge-case handling

- **Cardiac conditions and drugs** — included even though cardiothoracic *surgery* is excluded. The app will still surface ischaemic heart disease, hypertensive heart disease, rheumatic heart disease, etc. as conditions, and ACE inhibitors / beta-blockers / etc. as drugs. The exclusion is procedure-only.
- **Spinal conditions** — included as conditions and as targets of conservative management (e.g., physiotherapy referral). Only specialist neurosurgical procedures are excluded.
- **Cancer** — included as conditions, in WHO EML chemotherapy section as drugs, in lab oncology markers, in imaging staging studies, and in cancer-related procedures **at the level a Ugandan regional referral hospital performs** (e.g., diagnostic biopsy, palliative care, common excisions). Specialist surgical oncology beyond regional referral scope is excluded.
- **Mental health / psychiatry** — fully included across all cohorts.
- **Forensic / coroner work** — fully included where it overlaps clinical practice.

## Why these specific exclusions

The app is targeted at facilities from Health Centre II through Regional Referral Hospital (RRH). Procedures that are only performed at Mulago National Referral Hospital or abroad would create app surfaces that no end-user can act on. The exclusions trim the corpus to what the app's actual users will see in front of them.

## When in doubt

Default to **include**, but mark with a `level_of_care_minimum` value of `RRH` or `NRH` (National Referral Hospital). The app team can choose whether to surface NRH-only items in their UI. Exclusions are reserved for items that fall **outside the corpus entirely**.
