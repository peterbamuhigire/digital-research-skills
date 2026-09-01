# Kaizen Currentness Gate

## Purpose

This is the mandatory Digital Research gate for every Kaizen operation across the eleven skill engines. It applies to audits, skill edits, reference updates, validator changes, routing decisions, and any decision to standardise a practice.

The gate prevents durable ideas from being mistaken for current facts. Books and other historical material may supply concepts, models, or questions; they do not establish the current version of a platform, standard, policy, law, security control, command, lifecycle, benchmark, or technology.

## Preflight

Before analysis or implementation, enumerate every claim that could have changed:

- standards, specifications, laws, regulations, policies, and security controls;
- product, platform, package, API, protocol, command, version, support, and lifecycle claims;
- benchmarks, market facts, operating assumptions, and dataset definitions; and
- dependencies, compatibility boundaries, and cross-engine handoffs.

Read the Digital Research `source-evaluation` and `source-verification` skills. Use authoritative primary sources first, then record why a secondary source is necessary. If the work contains no time-sensitive claims, record `NO_TIME_SENSITIVE_CLAIMS` and still complete the preflight.

## Evidence record

Every admitted current claim must be traceable to an evidence record containing:

`claim_id`, claim text, `source_id`, source tier, source scope, publication or version date, access date, verification date, freshness class, review date, support status, uncertainty or limitation, confidence, and owner.

Use the central register at `C:\wamp64\www\skills-web-dev\docs\source-registers\skills-engine-currentness-2026-09.json` where a claim is portfolio-wide. Engine-local registers may add detail, but must not weaken the central evidence contract.

## Freshness and disposition

Classify each claim as `stable`, `context-bound`, `time-sensitive`, `partial`, or `unusable`. Re-check time-sensitive claims at or before their review date and whenever the task changes the target platform, jurisdiction, version, or risk profile.

- `verified`: source scope matches the claim and the evidence is within its review window;
- `context-bound`: usable only with the recorded jurisdiction, version, date, or environment;
- `partial`: evidence supports only part of the claim; narrow the wording;
- `stale`: the review date has passed or the source no longer represents the target state; and
- `NOT_ASSESSED`: evidence is missing, inaccessible, ambiguous, or insufficient.

Quarantine stale, ambiguous, unsupported, or out-of-scope claims. Do not silently replace them with remembered defaults. A release-blocking currentness finding remains `NOT_ASSESSED` until a qualifying source and verification record exist.

## Release gates

1. Verify current evidence before turning a claim into a skill rule, template, standard, control, command, or acceptance criterion.
2. Test volatile commands, versions, integrations, and platform behaviour in the stated environment or a disposable lab; record the result and limitations.
3. Keep durable book-derived concepts separate from current-source facts and cite the independent synthesis where it changes the workflow.
4. Re-run currentness checks after edits and before release. If the evidence window closes, reopen the affected decision rather than carrying it forward.
5. Pass the engine's native validator, routing smoke tests, source-ingestion guard, and any domain-specific safety gate before claiming completion.

## Cross-engine handoff

An engine handing off a current claim must provide the claim, source IDs, scope, dates, freshness class, support status, limitations, and verification evidence. The receiving engine may narrow or reject the claim, but may not broaden it without a new Digital Research check.

## Kaizen record

Each improvement record should state the aim, baseline, measure, PDSA experiment, owner, decision rights, recovery path, adoption evidence, and re-audit date. Currentness is a control condition for the experiment, not a retrospective citation exercise.
