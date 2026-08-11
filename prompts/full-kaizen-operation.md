# Digital Research Full Kaizen Operation Prompt

Paste this prompt at the root of a research report, evidence pack, due-diligence file, dataset, dashboard, source register, literature review, policy analysis, or OSINT project.

## Configuration

```text
Research product and decision: [DISCOVER]
Audience, geography, period, and scope: [DISCOVER]
Research questions and material claims: [DISCOVER]
Source, dataset, notebook, and output locations: [DISCOVER]
Sensitivity, privacy, legal, and ethical constraints: [DISCOVER]
Known contradictions, evidence gaps, or reviewer feedback: [NONE OR LIST]
Cycle ID: [YYYY-MM-DD-short-name]
Improvement authority: project-local reversible edits are authorised; external publication is not
```

## Prompt

Run a full evidence-disciplined Kaizen operation on this research product. Improve decision usefulness and reproducibility without manufacturing certainty. Freeze a capped baseline, fix the highest-leverage evidence and reasoning gaps through bounded work, independently check results, standardise learning, and leave a re-audit handoff.

### Routes and authority

Read project instructions. Resolve Digital Research Skills and read root `SKILL.md`, `AGENTS.md`, `skills/source-evaluation/SKILL.md`, its required evidence-discipline reference, `skills/source-verification/SKILL.md`, the product-specific research route, `skills/00-meta-initialization/references/kaizen-engine-and-product-audit.md`, and `docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md`.

This prompt authorises read/search, reproducible analysis, and reversible edits to the current research project. It does not authorise deceptive access, account bypass, prohibited scraping, contacting subjects, publishing, deanonymising people, purchasing data, changing source systems, or canonical engine edits. Respect robots, terms, privacy, licensing, consent, safeguarding, and source-risk boundaries. Stop for illegal or unsafe collection, unclear decision scope, missing authority, or sensitive-person risk. Record unavailable evidence as `NOT ASSESSED`. Never fabricate sources, quotes, statistics, access dates, search coverage, or reviewer agreement.

### Evidence pack

Create `docs/kaizen/<cycle-id>/` with `00-scope-and-evidence.md`, `01-baseline-scorecard.md`, `02-improvement-backlog.md`, `03-experiment-log.md`, `04-validation-record.md`, `05-final-report.md`, and `06-next-cycle.md`. Inventory the decision, questions, protocol, queries, databases/sites, dates, inclusion/exclusion rules, source register, archived evidence where permitted, datasets, transformations, notebooks, claim map, citations, contradictions, inference labels, limitations, reviewers, formats, and release constraints.

### Capped baseline

Score ten equal dimensions with evidence, confidence, deficiency, and status:

1. Decision framing, audience, questions, scope, definitions, and success criteria.
2. Research design, search strategy, coverage, inclusion/exclusion, and bias controls.
3. Source authority, independence, provenance, accessibility, relevance, and tiering.
4. Currency, version/date control, jurisdiction/context fit, and supersession checks.
5. Claim-to-source traceability, citation precision, quote/stat context, and rights-safe use.
6. Numeric, table, quote, identity, and material-claim verification, including spot-check coverage.
7. Contradiction handling, counterevidence, inference labels, uncertainty, and confidence calibration.
8. Data quality, transformations, calculations, reproducibility, notebook/query audit trail, and error checks.
9. Privacy, security, legal/ethical limits, conflicts, harm controls, and sensitive-source handling.
10. Synthesis, decision usefulness, accessibility, format fidelity, reviewer handoff, registry completeness, and feedback loop.

Calculate raw overall and publish `min(raw_overall, 65)`. Freeze it. Unsupported load-bearing claims, fabricated or inaccessible citations, material contradictions, privacy/safety issues, or irreproducible calculations remain blockers outside the score.

### Improve toward 95

Create a P0/P1/P2 backlog. Each action names claim/dimension, evidence, root cause, exact register/query/notebook/section, hypothesis, owner/reviewer, primary measure, uncertainty or harm guardrail, smallest reversible intervention, rollback, stop rule, acceptance proof, standardisation location, target contribution, and re-audit date.

Run one bounded improvement at a time: verify a load-bearing claim, repair a query log, replace a weak source, reproduce a calculation, resolve a contradiction, narrow an inference, improve citation precision, or add a data-quality check. Preserve previous conclusions and negative searches. Distinguish no evidence found from evidence of absence. If verification weakens the conclusion, revise the conclusion rather than the standard.

### Strict anti-AI-slop gate

Apply anti-AI-slop discipline during collection, analysis, and writing; audit after every major wave/iteration and at final release. Grade F blocks release. Any fabricated source, URL, author, date, quote, statistic, dataset, court case, law, organisation, search coverage, calculation, or reviewer agreement is a hard blocker. Reject citation laundering, sources that do not support the attached claim, generic multi-source summaries, false balance, uniform “key findings” prose, unlabelled inference, cherry-picking, invented precision, outdated evidence presented as current, and confident synthesis that hides contradictory or missing evidence.

Open and verify load-bearing sources; trace numbers and quotes to context; label source statements, calculations, inferences, assumptions, and unknowns separately; preserve counterevidence and negative searches; and state coverage limits. Fluent prose, many citations, or a polished chart cannot compensate for weak provenance, irreproducible analysis, or unsupported certainty.

### Validate and standardise

Re-run searches where currency matters, source-tier checks, link/access checks, claim-map coverage, quote/stat spot checks, contradiction review, calculation/notebook reproducibility, data-quality tests, citation audit, privacy/ethics review, and rendered-output inspection. Report coverage denominators and sampling logic. Record exact queries, dates, commands, source IDs, result paths, failures, and unavailable checks.

Promote accepted learning into the project protocol, source register, query library, dataset test, notebook, claim map, evidence table, reviewer checklist, template, or release gate. Re-score from new evidence and report the uncapped final result. The final report must separate verified facts, source statements, calculations, inferences, assumptions, unknowns, limitations, and decision implications.

Return baseline/final scores, improved claims or methods, validation coverage, changed conclusions, blockers, evidence-pack path, release verdict, and re-audit date. Do not publish or overstate completeness.
