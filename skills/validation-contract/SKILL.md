---
name: validation-contract
description: Use when authoring or normalising a specialist skill, or preparing to ship a feature or release — defines the seven evidence categories every specialist skill must declare against and provides the canonical Release Evidence Bundle template. The contract spine that turns scattered validation skills into a coherent ship-readiness check.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Validation Contract

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Artifact/release scope, risk, acceptance criteria, and applicable categories | Owner and specialist skills | Stop release assessment and request the missing scope or criteria. |
| Concrete validation artifacts | Tests, audits, runbooks, scans, and reviewers | Mark the category missing or not applicable with reason; never fabricate evidence. |

## Capability Contract

Assessment defaults to read-only. Running safe validators requires execution authority; editing evidence, deploying, approving release, or making certification claims requires separate explicit authority.

## Degraded Mode

If a tool, environment, artifact, or reviewer is unavailable, mark that category unassessed and block any claim that depends on it. Produce the partial bundle and recovery action.

## Decision Rules

| Finding | Action | Failure/risk avoided |
|---|---|---|
| Required category has no artifact | Block ship | Evidence-free readiness claim |
| Category truly does not apply | Record N/A with same-line reason | Empty compliance theatre |
| Artifact contradicts acceptance criteria | Fail and remediate | Selective reporting |

## Preliminary Evidence Corrections

- Treating a checklist tick as evidence. Fix: link the artifact.
- Filling every category just for symmetry. Fix: map actual risks.
- Using unexplained N/A. Fix: state the reason.
- Writing the bundle after release. Fix: gate before ship.
- Editing evidence during review. Fix: preserve provenance.

## Worked Example

For a medium-risk release, map each applicable category to a concrete artifact, justify any N/A on the same line, block missing required evidence, and release only after the bundle matches acceptance criteria.
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Authoring a new specialist skill and deciding which validation evidence it should produce.
- Normalising an older specialist skill against the current house style.
- Preparing a feature or release for ship and assembling the Release Evidence Bundle.
- Reviewing a PR that claims a feature is production-ready.

## Do Not Use When

- The work is purely local, experimental, or explicitly throwaway with no path to production.
- The skill being authored is a baseline, process, or pure index skill. Those do not declare evidence.
- The task is unrelated to validation planning or shipping readiness.

## Validation Source Requirements

- The specialist skill or feature being validated, including its intended scope and risk tier.
- Access to the repository's existing validation skills (`advanced-testing-strategy`, `vibe-security-skill`, `observability-monitoring`, etc.) as the source of category-specific "how to validate" content.
- Awareness of the 14 canonical artifact templates in `skill-composition-standards/references/` so evidence rows can cite existing formats.

## Validation Method Summary

- Identify whether the skill or feature in scope is specialist (declares evidence) or baseline/process (does not).
- For specialist skills: map each artifact the skill produces to one of the seven evidence categories.
- For releases: produce a Release Evidence Bundle that links concrete artifacts under each of the seven categories, using `N/A — <reason>` only where an entire category legitimately does not apply.
- Cross-check risk tier guidance before permitting any `N/A` in high-risk releases.

## Quality Standards

- Every specialist skill that produces validation evidence declares at least one evidence category with a concrete artifact reference.
- Evidence declarations cite existing artifact templates where possible instead of inventing new formats.
- Release Evidence Bundles never carry empty cells. Every cell links evidence or carries an `N/A — <reason>` line.

## Legacy Validation Warnings

- Declaring every category on every skill "just in case". This kills the signal.
- Writing prose validation notes instead of linking concrete artifacts in a Release Evidence Bundle.
- Permitting unjustified `N/A` on Correctness, Security, Data safety, Operability, or Release evidence in high-risk releases.
- Treating the Release Evidence Bundle as a retrospective summary written after ship. It is produced before ship.

## Initial Validation Deliverables

- A specialist skill with a validated `## Evidence Produced` section declaring one or more of the seven categories.
- A Release Evidence Bundle in the project's `docs/` tree linking evidence for every applicable category at ship time.
- Clear `N/A — <reason>` annotations for non-applicable categories, with risk-tier-aware justification.

## References

- [references/evidence-categories.md](references/evidence-categories.md): per-category definition, indicative contributing skills, and common artifact shapes.
- [references/declaration-form.md](references/declaration-form.md): the `## Evidence Produced` table form, rules, and worked examples.
- [references/release-evidence-bundle-template.md](references/release-evidence-bundle-template.md): the canonical fillable Release Evidence Bundle.
- [references/integration-rollout.md](references/integration-rollout.md): audit trail of edits made to other skills during this skill's rollout.
<!-- dual-compat-end -->

## The three repository-wide contracts

The repository is held together by three contracts, each codified in a baseline skill:

1. **House-style contract** — every skill follows the same shape. Source: `skill-composition-standards`, Standard 1.
2. **Inputs/Outputs contract** — every skill declares the artifacts it consumes and produces. Source: `skill-composition-standards`, Standard 2.
3. **Evidence contract** — every specialist skill declares which of seven fixed validation categories its artifacts contribute to, and every release produces a Release Evidence Bundle. Source: this skill.

The three contracts stack. A skill that meets Standard 1 but skips Standard 2 or 3 is not repository-grade.

## The seven evidence categories

| # | Category | What the evidence proves |
|---|----------|--------------------------|
| 1 | **Correctness** | Behaviour matches spec; tests cover risk surface; contracts hold. |
| 2 | **Security** | Threat model exists; scans clean; secrets handled; auth/authorisation verified. |
| 3 | **Data safety** | Schema integrity; migration safety; backup, retention, and PII handling. |
| 4 | **Performance** | Budgets met; load profile understood; query plans acceptable. |
| 5 | **Operability** | SLOs defined; runbook exists; observability wired; rollback plan ready. |
| 6 | **UX quality** | Accessibility pass; design audit; content/UX-writing review; AI slop check. |
| 7 | **Release evidence** | Change record; migration plan; rollout/rollback log; post-deploy verification. |

The taxonomy is closed. Adding an eighth category requires editing this skill, not silently extending it elsewhere. Full definitions and indicative contributing skills live in [references/evidence-categories.md](references/evidence-categories.md).

## Declaration mechanic

Specialist skills add a `## Evidence Produced` section to their `SKILL.md`, between `## Outputs` and `## References`:

```markdown
## Evidence Produced

| Category | Artifact | Format | Example |
|----------|----------|--------|---------|
| Security | Threat model | Markdown doc per `skill-composition-standards/references/threat-model-template.md` | `docs/security/threat-model-checkout.md` |
| Operability | Runbook | Markdown doc per `skill-composition-standards/references/runbook-template.md` | `docs/runbooks/payment-failures.md` |
```

### Rules

- A specialist skill that produces validation evidence **MUST** declare at least one row.
- Each row's `Category` value **MUST** be one of the seven canonical names (case-sensitive).
- Each row's `Format` field **MUST** reference an existing template or define its own format inline in the same `SKILL.md`.
- A specialist skill **MAY** contribute to multiple categories.
- Baseline skills, process skills, and pure index/orchestration skills **MUST NOT** declare.

Worked examples live in [references/declaration-form.md](references/declaration-form.md).

## Specialist vs exempt skills

A skill is "specialist" for the purposes of this contract when it:

- Produces concrete project artifacts (code patterns, schemas, configs, documents).
- Is loaded for a specific domain or platform problem rather than as a baseline frame.

Skills exempt from declaring (non-exhaustive):

- `world-class-engineering`, `skill-composition-standards`, `validation-contract` itself.
- `system-architecture-design`, `engineering-management-system`, `git-collaboration-workflow`.
- `feature-planning`, `spec-architect`.
- All `superpowers:*` skills.

When a skill straddles the line, the default is **declare**. False positives are cheaper than silent omissions.

## The Release Evidence Bundle

When a feature or release is ready to ship, the reviewer produces a single fillable document — the Release Evidence Bundle — that links to the concrete artifacts satisfying each of the seven categories.

- **Template:** [references/release-evidence-bundle-template.md](references/release-evidence-bundle-template.md).
- **`N/A` semantics:** permitted **only with a reason on the same line**. An empty cell is not acceptable.
- **Risk tier guidance:**
  - **Low risk** — internal tools, docs, non-user-facing scripts. Typical bundle has 3-4 categories live.
  - **Medium risk** — user-facing feature, single-tenant. All 7 categories addressed; some may be `N/A` with reason.
  - **High risk** — multi-tenant data, payments, auth, external APIs, AI features. All 7 categories live; no `N/A` permitted on Correctness, Security, Data safety, Operability, or Release evidence.

## Strictness

- The contract uses **MUST**, **MAY**, **MUST NOT** in the RFC 2119 sense.
- Mechanical enforcement is **out of scope** for this skill. It lands separately as a CI contract-gate hook that will:
  - parse `## Evidence Produced` tables and warn on missing or invalid categories.
  - parse Release Evidence Bundles and warn on empty cells or unjustified `N/A`.
- Authoring with binding language now means the CI hook is a parser and CI integration only, not a policy debate.

## Integration with existing skills

The rollout in [references/integration-rollout.md](references/integration-rollout.md) lists every edit made to other skills when this skill was introduced. Future edits that touch this contract should update that file.

## Companion Skills

- `skill-composition-standards` — Standards 1 and 2. Load this before `validation-contract`.
- `world-class-engineering` — repository production-readiness bar. This contract makes the evidence of meeting that bar a first-class artifact.
- Category-specific skills — the source of truth for *how* to validate within each category (see [references/evidence-categories.md](references/evidence-categories.md)).

## Workflow

1. Confirm release scope, risk, acceptance criteria, and categories; stop if any is unknown.
2. Map each category to a concrete artifact and named consumer.
3. Review artifact provenance and acceptance evidence without altering it.
4. Block missing or contradictory required evidence.
5. Recover through authorised remediation and rebuild the bundle before ship.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Release Evidence Bundle | Release owner and reviewer | Every applicable category links accepted evidence or carries justified N/A. |

## Anti-Patterns

- Checklist ticks as evidence. Fix: link artifacts.
- Every category by default. Fix: map risk.
- Unexplained N/A. Fix: give reason.
- Bundle after release. Fix: gate before ship.
- Editing evidence during review. Fix: preserve provenance.
