# Reference — Cognitive Bias Checklist

**Canonical source:** Heuer, Richards J. Jr. *Psychology of Intelligence Analysis*. CIA Center for the Study of Intelligence, 1999. https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/. Tier 1.

**Companion:** Davis, "Why Bad Things Happen to Good Analysts," Ch 10 in George & Bruce, *Analyzing Intelligence*, 2008. Bruce, Ch 11, same volume.

## How to use this checklist

Before any estimative output ships, the analyst writes — in the manifest, not just in their head — which biases the conclusion is most exposed to and what mitigation was applied. The "what mitigation" column tells the analyst which Heuer/Pherson SAT to deploy (see `references/heuer-pherson-sats.md`).

A clean run of the checklist produces a one-line bias-audit entry per judgment. A failed run sends the judgment back for a SAT.

## The thirteen biases

### 1. Confirmation bias / belief preservation
**Failure mode.** Analyst seeks evidence that supports the dominant hypothesis; ignores or explains away disconfirming evidence.
**Mitigation.** ACH — force evaluation against multiple hypotheses with explicit attention to disconfirming evidence. (Davis, p 160.)

### 2. Mirror-imaging / rationality bias
**Failure mode.** Analyst assumes the counterpart (adversary, competitor, examiner) reasons the way the analyst does.
**Mitigation.** Red Cell — model the counterpart's distinct rationality from the inside. (Davis, p 162.)

### 3. Mindset / paradox of expertise
**Failure mode.** The most experienced analyst is the most invested in the inherited paradigm and most likely to miss a paradigm-breaking signal. Davis cites the 1989 East European collapse: "a nearly perfect correlation between the depth of their expertise and the time it took to see what was happening" (p 161).
**Mitigation.** Rotate analysts; require Key Assumptions Check (KAC) on long-running judgments.

### 4. Hindsight bias
**Failure mode.** After an outcome is known, the analyst (or the reviewer) believes the signs were obvious all along, and back-projects judgment quality.
**Mitigation.** Record judgments with confidence labels ex ante; conduct post-mortems against the contemporaneous record, not the post-hoc reconstruction. (Davis, p 158.)

### 5. Groupthink
**Failure mode.** Coordinated analysis converges on a group answer because dissent is socially expensive; the group's confidence exceeds the evidence's confidence.
**Mitigation.** Diverse coordination; structured dissent channels; protect minority footnotes. (Davis, p 163.)

### 6. Boss-think
**Failure mode.** Senior reviewer rewrites the analytic line without engaging the evidence; analyst capitulates rather than raise the disagreement.
**Mitigation.** Senior reviewer cannot rewrite the line without naming the disagreement on the record. (Davis, p 163.)

### 7. Tribal-think
**Failure mode.** A unit or office develops a house view; outliers are filtered before they reach the senior analyst.
**Mitigation.** Explicit minority-view footnotes; protect paradigm-breaking drafts; circulate for cross-unit review. Davis cites the 1989 Berlin Wall case: tribal-think watered down the only prescient draft. (p 164.)

### 8. No-think
**Failure mode.** Coordinated text is treated as final and not re-opened when new disconfirming data arrives.
**Mitigation.** Re-open coordinated text when new data crosses a pre-defined threshold. (Davis, p 164.)

### 9. Layering / inherited assumptions
**Failure mode.** Each new judgment is built on top of prior judgments without re-examining the assumptions in the lower layers; the structure looks well-supported but the foundation is thin.
**Mitigation.** Annotate every key judgment with its evidentiary basis vs. its prior-NIE basis. KAC on long-running judgments. (Bruce, p 181.)

### 10. Anchoring on first report
**Failure mode.** The first report on a topic frames the analytic line; later reports are read as updates to the frame rather than as challenges to it.
**Mitigation.** Stage release of evidence in coordination; consider the latest report independently of the first.

### 11. Vividness bias / over-weighting clandestine HUMINT
**Failure mode.** Vivid sources (named witnesses, clandestine reports, leaked documents) are weighted more heavily than statistical or aggregate sources, regardless of corroboration.
**Mitigation.** Apply the source-evaluation grid before the judgment, not after. Tier-rate every source; weight by tier and corroboration, not by drama. (Bruce, Ch 11.)

### 12. Policy-preference bias / "elephant in the room"
**Failure mode.** Analyst silently shapes the analytic line to fit the customer's policy preference; or the customer shapes the question to elicit the desired answer.
**Mitigation.** Separate hypothesis-generation (the customer can supply the question) from hypothesis-testing (the analyst owns the evaluation). Document any pressure on the line. (Davis, pp 166–167.)

### 13. Card-stacking / negative-evidence neglect
**Failure mode.** Absence of expected evidence is explained away (e.g. as denial-and-deception) rather than treated as a hypothesis in its own right. The Iraq WMD NIE 2002 is the canonical case (Bruce, p 182).
**Mitigation.** Treat every "we don't see X" as a candidate hypothesis ("X may not exist"). Test it in ACH alongside the hypotheses that explain why X is hidden.

## The pre-ship bias-audit entry

For every estimative judgment that ships, the manifest carries:

```
Judgment: [single-sentence statement]
Bias exposure: [name 1–3 most likely biases from the checklist]
Mitigation applied: [name SAT(s) deployed; pointer to ACH matrix or KAC ledger]
Residual exposure: [biases not fully mitigated; flagged for the customer]
```

A judgment without a bias-audit entry does not pass the ship-gate.

## Anti-patterns

- **Performative audit.** Listing every bias in the checklist as "considered" with no mitigation. Reviewer ignores; the audit becomes paperwork.
- **Audit after ship.** Running the checklist as a post-hoc justification rather than a pre-ship discipline. The Davis warning: hindsight bias contaminates retrospective audit.
- **Single-bias focus.** Naming only confirmation bias because it is the one everyone knows. The other twelve are equally lethal.
- **Mitigation by note.** "Mitigated by being aware of it." Awareness without an SAT is not mitigation. Name the technique.

## Sources

- Heuer, *Psychology of Intelligence Analysis*. CIA CSI, 1999. Tier 1.
- George & Bruce, *Analyzing Intelligence*, Davis Ch 10, Bruce Ch 11. Tier 1.
- Heuer & Pherson, *Structured Analytic Techniques for Intelligence Analysis*. Tier 1.
