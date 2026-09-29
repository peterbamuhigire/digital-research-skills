# 09 Master scorecard

Engine: `digital-research-engine` at HEAD `2b9c87d`, 29 September 2026.
Labels: **M** = measured, **J** = judged, **NA** = NOT_ASSESSED.

## A. Engine dimensions (audit-dimensions.md, all 11)

| # | Dimension | Label | Score | Evidence |
|---:|---|---|---:|---|
| 1 | Doctrine and philosophy | J | 64 | Strengths: the hard-constraint clause, claim-level support states, the `NOT_ASSESSED` culture, the currentness gate and an untrusted-source contract. Weakness: doctrine is spread across `AGENTS.md` (268 lines: Codex model policy, design trigger, craft contract, prompt contract, English standard), `rules/`, the router and docs, with overlap and no single ordered doctrine file |
| 2 | Taxonomy and structure | J | 48 | Flat, with no maintained group index. About 14 of 59 skills are out of domain. Four duplicate pairs at 0.75 or above. 52 stale companion names. No benchmarking owner (see 02) |
| 3 | Skill depth and rigour | J | 54 | 59/59 contract-compliant locally (M). Deep references in the core (source-evaluation 10, OSINT 11, academic-writing 17). But 19 skills repeat sections, many carry generated padding headings, and quantitative modelling, decision support and forecasting are thin |
| 4 | Worked examples and applied proof | J (+M for T3) | 36 | 56/59 worked examples under 60 words. Example projects are three-line fixtures. Two real corpora (April and May 2026) have open verification items. T3 is 0 executed (NA) |
| 5 | Standards currency | J, with one external check | 52 | The register has 8 rows, verified 2026-07-08, next review 2026-10-08 (not overdue). `validate_source_currency.py` exits 0 (M, metadata only). The TOP entry is superseded (COS page accessed 2026-09-29). The legal overlay has no repository access dates. The 2026-09-28 model-policy review is current. Otherwise judged from the engine's own currentness records (no fresh external research) |
| 6 | Output-type readiness | J | 53 | Mean of 11 output types (05) |
| 7 | Accessibility and inclusivity | J | 45 | East African English and Kenya and Uganda academic skills are present. No other EAC jurisdictions. No Swahili or French source-language workflow beyond a caveat. Document accessibility is delegated to the design engine without a local check. Not in the weighted overall |
| 8 | Production and handoff | J (+M tests) | 58 | Kernel commands (`python -m engine new-project/sync/validate/assemble/pack`), Word, PDF and Excel generation, and a citation dashboard. 171 pytest passes (M). No render-fidelity evidence for a real deliverable. Not in the weighted overall |
| 9 | Redundancy and hygiene | J (+M CI) | 42 | CI red (2 cross-repository links, M). Duplicates with dev and srs. Retired `skill-safety-audit` still active. Absolute `C:/wamp64` paths in four files. Product residue in `update-claude-documentation`. Repeated sections in 19 skills |
| 10 | Discovery and routing | **M** | **57.5** | Engine Eval Readiness (below). The auditor's judged value, used for raw only: 58 |
| 11 | Safety and integrity | J | 64 | Explicit OSINT refusal list, private-surveillance stop condition, untrusted-source rules, a no-book-extraction check (M: `no-book-extractions: OK`) and the machine-error gate (M, exit 0). Held back by the retired safety skill left active, the absolute-path references and personal-data law coverage that is thin for an OSINT engine |

## B. Engine Eval Readiness (measured), recomputed

| Slot | Input | Fraction |
|---|---|---:|
| T1 | 3 of 3 declared validators pass on this host | 1.0000 |
| T2_p1 | precision@1 25/29 | 0.8621 |
| T2_neg | 7 local passes + 1 union mirror pass (056) out of 9; mirror 055 fails at rank 4 | 0.8889 |
| T2_cov | 0 of 59 skills with 3 or more positives and 2 or more owned negatives | 0.0000 |
| T2_clean | 0 undeclared of 4 cross-engine pairs at 0.75 or above | 1.0000 |
| T3 | 0 grading files; all planned runs NA | 0 |

- T1 = 30 × 1.0 = 30.00.
- T2 = 40 × (0.8621 + 0.8889 + 0 + 1) ÷ 4 = 40 × 0.68775 = 27.51.
- T3 = 0.
- **Readiness = 57.51, reported as 57.5.**

**The auditor agrees with the stored 57.5.** One caveat: T1 = 1.0 holds on this workstation
only. In clean CI the contract validator fails with two broken relative links. On a clean
checkout T1 would be 2/3, giving Readiness = 20.00 + 27.51 = 47.5. The portfolio figure is kept
as instructed, and the caveat is recorded here and in 11.

## C. Groups (from 03)

| Group | Score |
|---|---:|
| G1 Source discipline and validation | 60 |
| G2 Research design and execution | 56 |
| G3 Investigation and collection | 57 |
| G4 Data, analysis and synthesis | 50 |
| G5 Academic and regional | 52 |
| G6 Communication and deliverables | 50 |
| G7 Engine and agent practice | 42 |
| G8 Engineering and documentation imports | 32 |

## D. Output types (from 05)

| Output type | Score |
|---|---:|
| Verified fact brief | 62 |
| Source register | 60 |
| Model-policy and currentness review | 60 |
| Research wave plan and synthesis | 58 |
| OSINT / due-diligence report | 57 |
| Literature review | 55 |
| Quarterly ecosystem scan | 52 |
| Legal research memo | 50 |
| AI evaluation and data flywheel | 48 |
| Market-evidence pack | 45 |
| Benchmark / competitive study | 40 |
| **Mean** | **53.4 (used as 53)** |

## E. Overall, with arithmetic

The weights are 30 / 25 / 15 / 10 / 10 / 10. Depth and worked examples = (54 + 36) ÷ 2 = 45.

| Component | Weight | Raw | Measured-constrained |
|---|---:|---:|---:|
| Output readiness 53 | 0.30 | 15.90 | 15.90 |
| Depth and worked examples 45 | 0.25 | 11.25 | 11.25 |
| Standards currency 52 | 0.15 | 7.80 | 7.80 |
| Taxonomy 48 | 0.10 | 4.80 | 4.80 |
| Doctrine 64 | 0.10 | 6.40 | 6.40 |
| Hygiene | 0.10 | (42 + 58 + 64) ÷ 3 = 54.67 → 5.47 | (42 + 57.5 + 64) ÷ 3 = 54.50 → 5.45 |
| **Overall** | | **51.62 → 51.6** | **51.60 → 51.6** |

- **Raw: 51.6**
- **Measured-constrained: 51.6.** Routing is about 3.3 points of the total, and the judged 58 and
  measured 57.5 differ by 0.5.
- **Published: min(51.6, 65) = 51.6.** The cap applies because the portfolio craft standard's
  acceptance evidence is absent, but it does not bind at this level.
- With the clean-CI caveat (Readiness 47.5), measured-constrained would be 51.3.

## F. Scores of 70 or above

None. The engine's highest scores are doctrine (64), safety (64) and verified fact brief (62). No
extraordinary justification is required.

## G. Movement against prior audits

| Audit | Score | Comparable? | Observed movement |
|---|---|---|---|
| 2026-04-26 initial evaluation (self) | 62 → 65 | No; different, self-scored rubric | Engine added SAT, calibration, quantitative, primary-research and academic-standards skills since; their depth is now the constraint |
| 2026-09-06 Kaizen | Numeric NOT ASSESSED | Partly | Its P0 closures hold: currency validator rejects malformed input, tests are portable. Tests 124 → 171. CI turned red after it |
| 2026-09-23 scraping Kaizen | 54.8 raw (scraping only) | No; scoped | Scraping CLI and tests present; not re-scored separately |
