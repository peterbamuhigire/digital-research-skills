# Machine-Error Anti-Slop Gate Design

**Date:** 2026-09-03
**Status:** Approved for specification review
**Owner:** Peter Bamuhigire
**Scope:** The 12 registered skill engines and their human-facing editorial or presentation gates

## Problem

Existing anti-AI-slop controls catch many visible tells: banned vocabulary, unsupported claims,
generic openings, uniform structure, and visual defaults. They do not consistently catch the newer
class of errors described by the owner: prose that is grammatically competent but semantically
repetitive, artificially symmetrical, over-explained, inflated in significance, generic in example,
mannered in rhetoric, or shaped like an insight without adding one.

The failure is editorial rather than purely lexical. A sentence can pass grammar, citation, and
keyword checks while still imposing reading cost without adding information, judgement, evidence,
or a necessary instruction.

## Design

Digital Research will own a dated, portable reference:
`docs/continuous-improvement/machine-errors-editorial-gate-2026-09-03.md`.
It will define seven checks, each with a recognition test, corrective action, severity guidance,
and a reusable review record:

| ID | Check | Core question |
|---|---|---|
| ME1 | Semantic repetition | What new proposition does this unit add? |
| ME2 | Artificial symmetry | Is the parallel structure carrying meaning or merely shape? |
| ME3 | Over-explanation | Can the reader act or decide without the next restatement? |
| ME4 | Inflated significance | Does the rhetoric exceed the evidence and consequence? |
| ME5 | Generic examples | Is the example traceable to this audience, domain, or decision? |
| ME6 | Rhetorical mannerism | Has a device become a repeated authorial tic? |
| ME7 | Insight-shaped filler | What claim, warrant, evidence, or decision makes this paragraph necessary? |

The Digital Research `anti-ai-slop` skill will apply the checks during production. Its
`ai-slop-audit` companion will record concrete evidence, distinguish automated signals from human
judgement, and require a machine-error finding register. Neither skill will claim that semantic
meaning can be safely decided by keyword counts alone.

Domain engines will keep their own terminology and quality gates. Existing anti-slop skills in SRS,
business plans, social media, proposals, and engineering will link to the shared reference and add
domain-specific adaptations. Website, design, and accounting gates will add the relevant copy,
interface, and finance-output interpretations. Linux, Windows administration, and political writing
will expose the shared gate through their routers and output standards.

## Boundaries

- Do not ban all repetition: intentional recap, legal precision, requirements traceability, and
  accessibility repetition remain valid when their function is explicit.
- Do not force artificial variation: technical names, controlled vocabulary, formulas, and fixed
  templates are exempt when the constraint is documented.
- Do not turn style preference into a release blocker without observable evidence.
- Do not add current platform, legal, statistical, or benchmark claims. This change is a durable
  editorial synthesis from the owner-provided concept; currentness status is `NO_TIME_SENSITIVE_CLAIMS`.

## Validation and release

The change will add a deterministic coverage validator that checks that each engine's designated
gate or router exposes ME1–ME7 and links to the shared reference. A small pressure-test fixture will
contain semantically duplicated, symmetrical, over-explained, inflated, generic, mannered, and
insight-shaped-filler passages. Human review remains required for the semantic verdict.

Each repository's native validator and routing smoke test will run after its files change. Any
unavailable check is recorded `NOT_ASSESSED`; no baseline is weakened. The Kaizen record will log
baseline, hypothesis, measure, owner, rollback, adoption evidence, and the next re-audit date.

## Rollback

Revert the dated reference, local gate additions, and coverage validator as one change set per
repository. Existing anti-slop rules remain intact, so rollback removes the new lens without
weakening source, safety, accessibility, or domain controls.
