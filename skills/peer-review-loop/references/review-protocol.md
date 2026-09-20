# Review Protocol

## Review Modes

| Mode | Best for | Core question |
|---|---|---|
| Source audit | Evidence-heavy reports | Do the sources support the claims? |
| Method review | Research design and datasets | Is the method fit for the question? |
| Red team | High-stakes judgments | What would make this conclusion wrong? |
| Devil's advocate | Strong consensus | What is the best contrary case? |
| Decision review | Recommendations | Are options, criteria, and risks fair? |

## Disposition Log

| Challenge | Severity | Accepted? | Change made | Reason | Owner |
|---|---|---|---|---|---|
| Claim overstates evidence | High | Yes | Reworded confidence | Source limits | Analyst |

## Dual-Reviewer Convergence Contract

Source: ECC's `santa-method` skill (`skills/santa-method/SKILL.md`), adapted to this
skill's existing reviewer-independence and disposition-log discipline rather than
replacing it. Use this contract whenever the review mandate can be reduced to a
pass/fail rubric — citation checks, claim-source audits, compliance sweeps, and any
batch verification pass. Narrative red-team or devil's-advocate review (open-ended
argument challenge) stays qualitative and uses the disposition log above instead.

1. **Two independent reviewers, no shared context.** Spawn two review agents in
   parallel from the same rubric and the same frozen candidate. Neither sees the
   other's verdict, findings, or reasoning. Context isolation is the point: a single
   reviewer, or two reviewers who can see each other's output, share the anchoring
   bias that produced (or missed) the defect in the first place.
2. **Both must PASS.** The candidate ships only when reviewer A and reviewer B both
   return PASS on every rubric criterion. One PASS and one FAIL is FAIL — a single
   reviewer catching a real issue means the issue is real; it is not evidence the
   other reviewer is right.
3. **Fresh reviewers each round.** Every re-review after a fix cycle uses newly
   spawned agents with no memory of the previous round's findings or verdict.
   Reviewers carrying prior-round context anchor on what they already flagged and
   under-scrutinise what they didn't.
4. **Bounded convergence — max 3 fix iterations, then escalate to a human.** Track
   iteration count in the disposition log. On iteration 4 without a clean double-PASS,
   stop the loop and escalate; do not keep cycling generator and reviewers
   indefinitely. An unbounded loop that keeps finding new issues after each fix is
   itself a signal the candidate needs human judgment, not more automated review.
5. **Structured verdicts, not prose.** Each reviewer returns a typed result per
   criterion (`PASS` / `FAIL` plus the specific defect cited to the exact claim,
   quote, or cell) — matching this skill's existing rule that a finding without
   artefact evidence is not a finding.

This contract is additive to, not a replacement for, the reviewer-independence and
dissent-disposition rules already in `SKILL.md`: it specifies *how many* independent
reviewers and *what counts as convergence* for the pass/fail case; the disposition
log above still governs how an accepted or rejected challenge is recorded.

## Stratified Batch Sampling — Citation Checking at Scale

Source: ECC's `santa-method` Pattern C (batch sampling). This engine's
`source-verification` and `peer-review-loop` currently treat citation checking as
all-or-nothing: every citation in the batch gets the full verification workflow.
For a batch above roughly 30-50 citations, that is not the discipline to apply
by default — use stratified sampling instead, and reserve full-batch verification
for material, high-stakes, or small batches.

1. **Sample 10-15% of the batch** (minimum 5 citations, whichever is larger) at
   random, not by convenience — do not just check the first N or the easiest N.
2. **Run full verification** (this skill's dual-reviewer convergence contract, plus
   `source-verification`'s quote/URL/statistic checks) on the sample.
3. **Classify every failure by type** — misquotation, dead URL, citation-support
   mismatch, wrong locator, fabricated source — rather than logging it as a generic
   defect.
4. **If a failure type is systematic** (the same defect class recurs across sample
   items), apply the targeted fix to every item in the batch matching that pattern,
   not just the sampled ones.
5. **Re-sample and re-verify** the corrected batch. Continue until a clean sample
   passes.
6. **Escalate to full verification** when: the batch is small enough that full
   verification is cheap, the content is high-stakes (legal, medical, financial,
   safety-relevant), or two successive samples both surface systematic failures —
   sampling is a cost-reduction tool for catching systematic defects, not a
   substitute for full verification when the stakes or the failure rate say
   otherwise.

Per ECC's data, this reduces verification cost to roughly 15-20% of full
per-citation verification while catching over 90% of systematic issues — spot
checks a full pass would also have caught, plus the pattern-level fix a
one-at-a-time pass would have applied 30-50 times redundantly. Record the sample
rate, sample size, failure taxonomy, and re-sample outcome in the disposition log
so the release gate can see the batch was sampled, not skipped.
