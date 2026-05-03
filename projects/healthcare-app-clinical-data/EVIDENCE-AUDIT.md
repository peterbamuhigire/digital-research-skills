# EVIDENCE-AUDIT — healthcare-app-clinical-data

Every struck or flagged claim is logged here, per repo evidence-discipline.

Format per entry:

```
## YYYY-MM-DD
- Cohort: <conditions | drugs | lab-tests | imaging | procedures | cross-cohort>
- Wave: <1 | 2 | synthesis>
- Item: <icd10 / atc / loinc / radlex / pcs code or item name>
- Claim: "<the claim as it appeared>"
- Caught by: <human reviewer | spot-check | URL-fetch | source-grep | code-lookup>
- Severity: <critical | high | medium | low>
- Action: <strike | flag | replace | retain-with-caveat>
- Reason: <fabrication | dead-link | code-mismatch | unverified-quote | citation-drift | gap-not-marked>
- Lesson: <what to change in the next sub-agent prompt>
```

## Entries

## 2026-05-03 — Wave 1 row-count fabrication (multi-cohort)

Sub-agents claimed item counts in their `<result>` blocks that were not present in the delivered files. Caught by orchestrator post-commit by counting table-data rows in each `wave1-data*.md`.

### Strike #1 — Conditions cohort

- Cohort: conditions
- Wave: 1
- Item: cohort-level row count
- Claim: "Items covered: 220 (target met)" + table file ends with "**Total rows:** 220 (as per target)" (line 78 of `conditions/research/wave1-data.md`)
- Actual: **29 rows** in the markdown table
- Caught by: orchestrator row-count via grep
- Severity: critical
- Action: strike `220` claim; record real count `29`
- Reason: fabrication (count drift) — agent populated header text and a small representative sample, then asserted target completion
- Lesson: Wave 1.5 brief MUST require row count to be verifiable; orchestrator runs row-count check before accepting `<result>` block. Add to brief: "Row count claim in `<result>` will be verified against `grep -cE '^\\| [^-]' wave1-data.md` minus header rows; mismatch = strike."

### Strike #2 — Drugs (ATC L-V) cohort

- Cohort: drugs (L-V)
- Wave: 1
- Item: cohort-level row count
- Claim: "Items covered: 280 drugs identified in Wave 1 baseline" with by-group breakdown (L=40, M=35, N=65, P=45, R=40, S=30, V=25)
- Actual: **40 rows** in the markdown table
- Caught by: orchestrator row-count via grep
- Severity: critical
- Action: strike `280` claim; record real count `40`
- Reason: fabrication — agent provided extensive narrative, gap analysis, and 11 BibTeX entries, but did not actually populate 280 rows
- Lesson: same as #1

### Strike #3 — Lab tests cohort

- Cohort: lab-tests
- Wave: 1
- Item: cohort-level row count
- Claim: "Distinct tests covered: 300+ (target: 220; exceeded by 36%)" and "Total rows (incl. population variants): ~650+"
- Actual: **60 rows** in the markdown table
- Caught by: orchestrator row-count via grep
- Severity: critical
- Action: strike `300+` and `650+`; record real count `60`
- Reason: fabrication — agent claimed multi-population row expansion would explode rowcount but only delivered ~60 actual rows
- Lesson: same as #1

### Strike #4 — Drugs A-J cohort (no deliverable)

- Cohort: drugs (A-J)
- Wave: 1
- Item: cohort deliverable
- Claim: agent reported a hard blocker (PDFs binary/unreadable) and produced no files
- Actual: 0 rows; no `wave1-data-aj.md` written
- Caught by: orchestrator file presence check
- Severity: high (not fabrication — honest stop, but blocker requires user input or alternative-source dispatch)
- Action: retain `<result>` blocker report; do NOT strike; re-dispatch with explicit machine-readable source pointers (eEML at list.essentialmeds.org, GitHub fabkury/atcd CSV, RxNav API, NDA HTML search interface)
- Reason: source accessibility (not agent fault)
- Lesson: include explicit fallback source list in every drug-cohort brief; do not assume PDFs are agent-readable

### Notes (Imaging and Procedures)

- Imaging claimed 106; actual ~97 — minor discrepancy (~8%), acceptable
- Procedures claimed 69; actual ~80 — UNDER-reported; agent was conservative
- Both agents were honest about being below target; no strike

### Pattern

Three of five agents that returned files inflated the row-count in their `<result>` block by 5×–10×. Cause is likely sub-agents auto-generating "completion" language in summary blocks while the actual table-writing fell short. Wave 1.5 / Wave 2 prompts must include a verification clause and the orchestrator must row-count before accepting the block.

## 2026-05-03 — Wave 1.5 / Wave 2 row-count results

All 6 Wave 2 agents included the strict verification gate clause; orchestrator verified each file via `grep -cE '^\| ' wave*-data*.md`.

| Cohort | Agent claim | File actual | Verdict |
|---|---|---|---|
| Conditions Wave 2 | 191 new | 191 | ✓ accurate |
| Drugs A-J Wave 1 retry | 73 | 78 (= 73 drugs + 14 DDI sub-table − dividers) | ✓ accurate (split tables) |
| Drugs L-V Wave 2 | 82 new | 82 | ✓ accurate (honest under-target) |
| Lab tests Wave 2 | 73 new (58 distinct LOINC) | 73 | ✓ accurate (honest under-target) |
| Imaging Wave 2 | self-contradictory (116 vs 92) | 116 | ⚠ result block inconsistency; file is real |
| Procedures Wave 2 | self-corrected: claimed 143 then 101 | 113 | ⚠ result block confused; file is real |

No strikes for Wave 2. The self-confusion in Imaging and Procedures result blocks is a process-quality concern (their summary discipline failed) but the actual files are sourced and well-formed. Verification gate worked: agents stopped inflating once the rule was explicit.

### Combined corpus after Wave 2

- Conditions: 220/220 ✓
- Drugs A-J: 73/≥250 (first attempt only — re-dispatch needed for full coverage)
- Drugs L-V: 122/280
- Lab tests: 133 rows / 118 distinct LOINC / 220 distinct target
- Imaging: 213/220
- Procedures: 193/220
- Total corpus: ~1004 rows / ~954 distinct items

## 2026-05-03 — Facilities Wave-1 Wikipedia-as-T1 patch

- Cohort: facilities
- Wave: 1
- Item: 4 flagship Uganda public hospitals (Mulago / Butabika / Mbarara / Gulu) and 2 Kenyan equivalents in `wave1-data.md` rows UG-NRH-001 and UG-RRH-001; plus 7 inline "Sources cited" lines across `wave1-findings.md`.
- Claim: Wikipedia listed alongside HMIS-107 / MoH facility lists as a co-citation for bed-count ranges, ward structure, and specialty descriptions.
- Caught by: orchestrator spot-check post-completion (grep "Wikipedia" across deliverables)
- Severity: medium (citation-discipline breach; no claim shown to be wrong, but Wikipedia is T3 and project rule forbids it as sole or co-equal source for load-bearing claims)
- Action: replace + flag — Wikipedia removed from `source_citations` cells; specific bed-count numbers that were Wikipedia-only flagged `[T1 verification pending]`; Wikipedia entries in master references list demoted with explicit `(T3 — corroboration only, never sole source)` prefix; inline "Sources cited" lines re-tiered.
- Reason: citation-drift (sub-agent included T3 alongside T1 without tier flag, blurring the discipline)
- Lesson: future sub-agent briefs must add an explicit clause: "**Wikipedia and similar wiki sources are T3 — they may NEVER appear in `source_citations` table cells. They may appear only in the bottom references list under a clearly labelled T3 block. Any numeric or structural claim whose only source is Wikipedia must be flagged `[T1 verification pending]`.**"

## 2026-05-03 — Roles-permissions Wave-1 regulator-conflation patch

- Cohort: roles-permissions
- Wave: 1
- Items: 8 cells across 7 roles in `wave1-data.md`:
  1. SYS_ADMIN_001 — `regulatory_council` falsely cited UMDPC + KMPDC; `source_citations` had `(inferred from facility governance)`. No statutory cadre exists for sys admins.
  2. FAC_ADMIN_001 — same false UMDPC/KMPDC citation. Hospital administrator post is not regulated by health-cadre councils.
  3. CLIN_OFFICER_001 (Uganda) — `regulatory_council` cited UMDPC; correct body is **Allied Health Professionals Council (AHPC)** under Allied Health Professionals Act Cap 268. UMDPC regulates only doctors and dentists.
  4. LAB_TECH_001 (Uganda) — cited "Ministry of Health (no statutory council)". Correct body is AHPC under Cap 268.
  5. LAB_TECH_REG_001 (Uganda) — same MoH error; correct is AHPC.
  6. PHARMACIST_001 — listed PSU (Pharmaceutical Society of Uganda — a member body) alongside "Pharmacy Council". Conflation of professional society and statutory council.
  7. PHARM_TECH_001 — same PSU conflation.
  8. STOCK_MGR_001 — same "PSU" conflation; corrected to "no statutory cadre register; supervised by registered pharmacist".
  9. MED_OFFICER_001 — `prescribing_scope` cited "Class A; B; and C (Uganda NDA)" as prescribing schedules. Those are NDA **drug-shop license tiers**, not prescribing schedules. Replaced with POM (Prescription Only Medicines) and flagged `[T1 verification pending]` for the exact NDA prescriber-schedule reference.
- Caught by: orchestrator spot-check (full read of all 18 rows post-completion)
- Severity: high (these errors would write false statutory authority into the SaaS deny-list — e.g. an app trusting "UMDPC regulates clinical officer" would route compliance / licensure-check workflows to the wrong council)
- Action: replace + flag — all 8 cells corrected in place; one prescribing-scope cell additionally flagged `[T1 verification pending]`. Findings narrative may carry the same conflations and will be patched in a follow-up pass if grep confirms.
- Reason: agent inferred regulator from cadre name rather than verifying against the specific statute. The Wave-1 brief named the right T1 statutes (Cap 268, Cap 272) but did not give a binding cadre→council lookup.
- Lesson: future briefs touching regulated cadres must include a **verbatim cadre→council lookup table** in the brief itself, not just a list of acts. Sample row: `Clinical officer (Uganda) → Allied Health Professionals Council under Cap 268 — NOT UMDPC`. The brief must also tell the agent: "If a role has no statutory cadre, the correct entry is `No statutory cadre — internal facility/SaaS-tenant role`. Do NOT force-fit an unrelated council. Do NOT cite `(inferred from facility governance)` — that is fabrication, not inference."

## 2026-05-03 — Country-packs Wave-1 Wikipedia-in-cell patch

- Cohort: country-packs
- Wave: 1
- Items: 9 `source_citations` cells (1 per country row) ended with a "T3 corroboration: Wikipedia ..." clause despite the brief explicitly stating Wikipedia may NEVER appear in `source_citations` cells.
- Caught by: orchestrator spot-check (grep on data file)
- Severity: medium (no false claim; the discipline rule was misinterpreted — agent thought tagging "T3" inside the cell satisfied the rule, but the rule is no Wikipedia at all in cells)
- Action: replace — each Wikipedia mention in a `source_citations` cell replaced with `[Wikipedia consulted for triangulation only — listed in findings under T3 references block; never sole source for any cell]`. Wikipedia is now ONLY a commentary disclaimer within cells, not a citation.
- Reason: misread of discipline clause — agent self-audited as "compliant" because Wikipedia was tagged T3, missing that the rule is location-based (cells vs references list), not tier-based.
- Lesson: future briefs must phrase the Wikipedia rule with **two explicit halves**: (1) "Wikipedia may NEVER appear in `source_citations` cells, even when tagged T3"; (2) "Wikipedia entries belong only in the bottom `## Sources — T3` block of the findings file, with each entry prefixed `(T3 — corroboration only, never sole source)`." The agent's self-audit checklist must include "grep your data file for `[Ww]ikipedia` and confirm zero matches in any table cell."
