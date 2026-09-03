# Machine-Error Anti-Slop Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Standardise detection and prevention of machine errors across all 12 skill engines without weakening evidence, domain, accessibility, safety, or controlled-language requirements.

**Architecture:** Digital Research owns one dated reference and a deterministic coverage validator. Existing domain gates consume that reference through short, local adaptations. Engines without dedicated anti-slop skills expose the gate through their router and output standards. Semantic findings remain evidence-backed human judgements; automation checks coverage and lexical/structural signals only.

**Tech Stack:** Markdown skill files, Python `unittest`, PowerShell/native engine validators, Git repositories on local disk.

**Spec:** `C:/wamp64/www/digital-research-skills/docs/superpowers/specs/2026-09-03-machine-errors-anti-slop-design.md`

## Global Constraints

- Preserve intentional repetition required for legal precision, accessibility, requirements traceability, controlled vocabulary, formulas, and fixed templates.
- Treat unsupported semantic findings as `NOT_ASSESSED`; no keyword count alone may decide meaning.
- Do not weaken any existing quality baseline or release blocker.
- Currentness status for the new concept is `NO_TIME_SENSITIVE_CLAIMS`; dated repo and validator results must be recorded.
- Do not push to remotes unless separately requested.

---

### Task 1: Add the failing coverage contract

**Files:**
- Create: `C:/wamp64/www/digital-research-skills/tests/test_machine_error_gate.py`
- Create: `C:/wamp64/www/digital-research-skills/tests/fixtures/machine-error-gate-baseline.json`

- [x] Define the seven required IDs (`ME1`–`ME7`) and the 12 engine targets in the test fixture.
- [x] Write tests that require the shared reference, central production/audit skills, and each engine adapter to expose all seven IDs or an explicit router handoff.
- [x] Run `python -m unittest tests/test_machine_error_gate.py`; confirm it fails because the reference and adapters do not yet exist.

### Task 2: Create the shared machine-error reference

**Files:**
- Create: `C:/wamp64/www/digital-research-skills/docs/continuous-improvement/machine-errors-editorial-gate-2026-09-03.md`
- Modify: `C:/wamp64/www/digital-research-skills/skills/anti-ai-slop/SKILL.md`
- Modify: `C:/wamp64/www/digital-research-skills/skills/ai-slop-audit/SKILL.md`
- Modify: `C:/wamp64/www/digital-research-skills/docs/quality-gates/anti-slop-governance.md`

- [x] Define ME1–ME7 with recognition test, corrective action, severity, and valid exceptions.
- [x] Add a required semantic-delta review record: `unit`, `new_information`, `evidence_or_decision`, `action`, `reviewer`, `date`.
- [x] Add production-time checks to `anti-ai-slop` and independent audit checks/output fields to `ai-slop-audit`.
- [x] Record the Kaizen aim, baseline, hypothesis, measure, owner, rollback, adoption evidence, and 2026-10-03 re-audit date.

### Task 3: Add deterministic coverage validation

**Files:**
- Create: `C:/wamp64/www/digital-research-skills/scripts/validate_machine_error_gate.py`
- Modify: `C:/wamp64/www/digital-research-skills/tests/test_machine_error_gate.py`
- Modify: `C:/wamp64/www/digital-research-skills/AGENTS.md`

- [x] Implement a read-only validator that checks file existence, required IDs, central-reference links, and explicit `NOT_ASSESSED` handling.
- [x] Make missing files, missing IDs, and broken links fail; do not score semantic quality automatically.
- [x] Run the validator before and after the adapters are added.
- [x] Add the validator to the Digital Research skill-authoring release commands.

### Task 4: Adapt existing production/audit skills

**Files:**
- Modify SRS: `09-governance-compliance/28-anti-ai-slop/SKILL.md`, `09-governance-compliance/29-ai-slop-audit/SKILL.md`
- Modify Business Plan: `skills/meta-utility/anti-ai-slop/SKILL.md`, `skills/meta-utility/ai-slop-audit/SKILL.md`
- Modify Social Media: `skills/ai-marketing/anti-ai-slop/SKILL.md`, `skills/ai-marketing/ai-slop-audit/SKILL.md`
- Modify Proposal: `skills/meta/anti-ai-slop/SKILL.md`, `skills/meta/ai-slop-audit/SKILL.md`
- Modify Engineering: `skills/sdlc-meta/anti-ai-slop/SKILL.md`, `skills/sdlc-meta/ai-slop-audit/SKILL.md`

- [x] Add a short local adaptation for ME1–ME7 and link to the shared reference.
- [x] Add the semantic-delta review to live workflow, audit output, and ship gate.
- [x] Preserve domain exceptions: requirement traceability, financial reconciliation, campaign repetition, proposal headings, and code/API identifiers.
- [x] Run each engine's local contract and routing checks after its pair is updated.

### Task 5: Adapt website, design, and accounting gates

**Files:**
- Modify Website: `skills/content-copy/premium-commercial-writing/references/genuine-writing-and-ai-slop-gate.md`, `skills/build/design-system/references/ai-slop-prevention.md`, `skills/quality-gates/visual-qa/references/slop-rules.md`, `AGENTS.md`
- Modify Design: `doctrine/references/ai-slop-taxonomy.md`, `skills/00-cross-cutting-ops-qa-a11y/visual-product-slop-audit/SKILL.md`, `skills/00-cross-cutting-ops-qa-a11y/slop-doctrine-refresh-and-research-loop/SKILL.md`
- Modify Accounting: `governance/anti-slop-finance-output.md`, `AGENTS.md`

- [x] Apply ME1–ME7 to web copy, repeated UI modules, feature cramming, finance narratives, and audit explanations.
- [x] State that visual repetition and symmetry require a design purpose; repeated accounting lines remain valid when driven by ledger/control structure.
- [x] Keep design-currentness handling in the design refresh loop and route written-copy decisions to Digital Research.

### Task 6: Add router coverage for Linux, Windows, and political engines

**Files:**
- Modify: `C:/wamp64/www/linux-skills/AGENTS.md`
- Modify: `C:/wamp64/www/windows-admin-engine-skills/AGENTS.md`
- Modify: `D:/political-skills/AGENTS.md`
- Modify: `D:/political-skills/skills/political-essay-doctrine/SKILL.md`

- [x] Add explicit routing to the shared reference for runbooks, operational explanations, political prose, and public arguments.
- [x] Require a semantic-delta pass before release while preserving command syntax, safety steps, legal quotations, and doctrinal repetition where functional.
- [x] Add `NOT_ASSESSED` handling when the output or source evidence cannot be inspected.

### Task 7: Finish the red-green-refactor and Kaizen evidence cycle

**Files:**
- Modify: `C:/wamp64/www/digital-research-skills/tests/test_machine_error_gate.py`
- Modify: `C:/wamp64/www/digital-research-skills/tests/fixtures/machine-error-gate-baseline.json`
- Create: `C:/wamp64/www/digital-research-skills/docs/continuous-improvement/kaizen-machine-errors-2026-09-03.md`

- [x] Re-run the original failing coverage test and confirm it passes.
- [x] Run pressure fixtures for duplicate meaning, false symmetry, over-explanation, inflated stakes, generic examples, mannerism, and insight-shaped filler.
- [x] Manually review every fixture finding and confirm intentional exceptions are not blocked.
- [x] Run each changed repository's native validator, routing smoke test, source-ingestion guard, and relevant unit tests; record unavailable or pre-existing failures.
- [x] Record positive and negative evidence, unassessed checks, rollback, owner, and the next review date.

### Task 8: Final independent verification and handoff

- [x] Inspect all diffs and ensure no unrelated files changed.
- [x] Run `git diff --check` in every changed repository.
- [x] Run the coverage validator from Digital Research against the final tree.
- [x] Re-run Digital Research currentness checks and confirm `NO_TIME_SENSITIVE_CLAIMS` remains accurate.
- [x] Report pulled commits, changed repositories/files, test evidence, unassessed checks, and the no-push status.
