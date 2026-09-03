# Machine-Error Editorial Gate

**Status:** active cross-engine Kaizen standard
**Checked:** 2026-09-03
**Owner:** Peter Bamuhigire
**Currentness:** `NO_TIME_SENSITIVE_CLAIMS`
**Input:** owner-provided editorial concept in the Kaizen request

## Why this gate exists

Grammar, spelling, and citation checks remove many older editorial failures. Generative systems
also produce a newer class of failures that can look polished: text that repeats meaning, arranges
ideas into decorative symmetry, explains past the point of use, inflates ordinary consequences,
uses examples that could belong anywhere, turns rhetorical devices into mannerisms, or gives a
paragraph the shape of an insight without doing the work of one.

The governing question is:

> Why does this sentence, paragraph, component, or section need to exist?

Keep it when it adds information, evidence, judgement, a decision, a constraint, an instruction,
or a necessary reader safeguard. Otherwise cut it, merge it, or label the missing work.

## The seven checks

| ID | Machine error | Recognition test | Corrective action |
|---|---|---|---|
| ME1 | Semantic repetition | Does this unit restate a nearby proposition without changing the evidence, scope, consequence, or decision? | Delete, merge, or make the delta explicit. |
| ME2 | Artificial symmetry | Are matched pairs, oppositions, or evenly shaped lists carrying a real distinction, or only producing polish? | Keep the structure only when the relationship matters; otherwise use the natural order. |
| ME3 | Over-explanation | Could the intended reader act, assess, or decide before the next explanation, example, recap, or conclusion? | Stop at sufficiency; remove the redundant teaching layer. |
| ME4 | Inflated significance | Does the emotional or strategic weight exceed the evidence, scale, or actual consequence? | State the concrete effect, boundary, and confidence; remove grand framing. |
| ME5 | Generic example | Could the example be swapped into another sector, country, client, or product unchanged? | Use a traceable contextual example or remove it. Never invent specificity. |
| ME6 | Rhetorical mannerism | Does the same device recur often enough to announce the generator or author rather than the idea? | Vary the construction or use plain prose. Count recurrence in the audit. |
| ME7 | Insight-shaped filler | Does the paragraph contain a claim, warrant, evidence, comparison, implication, or decision that earns its space? | Add the missing work from a real source or cut the paragraph. |

## Impeccable-derived anti-slop overlay

The [Impeccable Slop catalog](https://impeccable.style/slop/) is first-party evidence for its own
web-interface detector taxonomy. It distinguishes deterministic CLI checks, browser-layout checks,
and LLM-only judgements. Use the following overlay as scoped review guidance; it is not evidence
that a pattern is universally machine-generated and it is not a blanket visual taste ban.

| ID | Overlay | Recognition test | Default correction |
|---|---|---|---|
| AS1 | Default convergence | Is a common palette, typeface, layout, or copy pattern present without a recorded project reason? | Keep only with a brief-specific reason; otherwise choose a deliberate alternative. |
| AS2 | Unearned hierarchy | Do eyebrows, chips, badges, icon tiles, hero metrics, or numbered labels imply importance without improving the task? | Remove, integrate into useful content, or document the hierarchy reason. |
| AS3 | Module monoculture | Are identical cards, nested cards, or uniform spacing flattening distinctions between items? | Vary structure by information need, flatten nesting, or preserve it with a hierarchy rationale. |
| AS4 | Decorative attention | Does glow, gradient, marquee, cursor, pulse, bounce, hover transform, or similar motion lack state or task value? | Remove, reduce, or tie it to a real state/action; respect accessibility preferences. |
| AS5 | Placeholder material | Is an image, illustration, example, icon, or asset generic, shape-assembled, washed out, missing, or placeholder-valued? | Use traceable purposeful material or remove the slot. Never invent provenance. |
| AS6 | Copy tell | Do buzzwords, repeated em-dashes, manufactured aphorisms, or theatrical framing recur as a house cadence? | Replace with literal verbs/nouns and varied plain prose; count recurrence in the audit. |
| AS7 | Polish-covered delivery debt | Is content invisible, unreadable, cramped, overflowing, clipped, broken, or structurally invalid beneath the visual polish? | Fix the defect before judging style; record browser or render evidence. |

Apply the full overlay to web development, website, and design work. Other engines use only the
applicable content, structure, or delivery checks and must label non-applicable visual checks
`not_applicable`; unavailable browser, render, tool, context, or reviewer evidence is
`NOT_ASSESSED`, never a pass.

### Visual no-ship boundary

For websites, web products, presentations, and design artifacts, the following decorative choices
are no-ship: purple gradients, glassmorphism, neon glow, AI-beige defaults, decorative editorial
scaffolding, and decorative motion. This is a hard anti-convergence boundary, not a ban on a
functional status transition, an accessibility affordance, or a data-encoding colour when the
recorded task requires it. A retained exception must name the task, state, accessibility need, or
approved brand/design-system token.

## Apply in production

Run the checks while drafting, not only at the end:

1. Identify the reader's next action or decision.
2. Give each sentence one job and each paragraph one centre of gravity.
3. Compare a new unit with the preceding two or three units for meaning, not just matching words.
4. Mark deliberate repetition when it serves legal precision, accessibility, requirements traceability,
   controlled vocabulary, formula integrity, or an explicit recap.
5. Prefer an ordinary sentence with a clear consequence over a polished sentence with no delta.
6. Cut before expanding. If a missing claim or warrant cannot be sourced, record a gap instead.

## Audit record

For each finding, record:

```yaml
- id: ME1
  unit: "paragraph 3, sentence 2"
  evidence: "exact repeated proposition or structural pattern"
  new_information: "none | stated delta"
  evidence_or_decision: "source, constraint, judgement, or none"
  action: "keep | merge | cut | rewrite | not_assessed"
  severity: "minor | major | blocking"
  exception: "documented reason if repetition is intentional"
  reviewer: "name or role"
  date: "YYYY-MM-DD"
```

A semantic finding is not established by a keyword hit alone. The reviewer must cite the affected
units and explain the missing delta. When the artefact, context, or reviewer access is incomplete,
mark the check `NOT_ASSESSED`.

For AS findings, also record the evidence mode:

```yaml
- id: AS4
  unit: "hero status indicator"
  evidence_mode: "cli | browser | llm_only | human_review"
  new_information_or_task_value: "none | stated value"
  evidence_or_decision: "state change, task benefit, accessibility need, or none"
  action: "keep | reduce | remove | rewrite | not_applicable | not_assessed"
  severity: "minor | major | blocking"
  exception: "documented functional reason if retained"
  reviewer: "name or role"
  date: "YYYY-MM-DD"
```

## Domain exceptions

- **Requirements and code:** repeated identifiers, acceptance criteria, error states, and trace links
  are functional when they preserve testability or implementation safety.
- **Finance and controls:** repeated ledger, reconciliation, policy, and reviewer fields are valid
  when they preserve auditability; narrative repetition still needs a decision or evidence delta.
- **Legal and policy writing:** repeated operative wording may be required; do not rewrite it for
  style when the repetition carries scope or legal effect.
- **Accessibility and operations:** repeated labels, warnings, recovery steps, and state descriptions
  may be necessary for safe use.
- **Design and interfaces:** repeated components are acceptable when hierarchy, scanning, or state
  consistency is the reason; identical modules with no information hierarchy are a convergence tell.
- **Visual defaults:** a font, palette, radius, layout, or motion choice is not a defect merely
  because it is common; retain it when the project design system, audience, brand, or task gives a
  documented reason.
- **External detectors:** an unavailable Impeccable or equivalent detector is `NOT_ASSESSED`; do
  not turn a missing tool into a clean result.

## Release rule

The gate passes when all applicable units have either a clear information/decision purpose or an
explicit functional exception. Unsupported semantic judgements remain `NOT_ASSESSED`; they do not
become clean by default. The gate complements source verification, domain correctness, safety,
accessibility, and visual QA. It does not replace them.

## Kaizen record

- **Aim:** catch polished prose and presentation that imposes reading or interaction cost without
  adding meaning.
- **Baseline:** existing engines emphasised banned words, genericness, citation integrity, and
  visual convergence; semantic delta and insight-shaped filler were not consistently named.
- **Hypothesis:** a shared seven-check gate plus domain adapters will reduce repeated meaning,
  mannered structure, and hollow sections without increasing false positives for functional repetition.
- **Measure:** coverage validator passes in all 12 engines; pressure fixtures expose all seven checks;
  human review confirms intentional exceptions remain unblocked.
- **Owner:** engine maintainers under the Digital Research currentness gate.
- **Rollback:** remove this reference and its local adapters; retain existing anti-slop controls.
- **Re-audit:** 2026-10-03, or earlier if an engine reports false-positive harm.
