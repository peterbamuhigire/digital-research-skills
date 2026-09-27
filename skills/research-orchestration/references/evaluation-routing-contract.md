# Research evaluation routing contract

This contract routes supplementary evaluation guidance for the offline SEEK-inspired prototype. It does not replace research planning, source evaluation, claim verification, or domain gates.

## Selection

- Start from the case question, decision, scope, risk class, and explicit task tags.
- Add every criterion whose `trigger_tags` match the case tags; multiple criteria may apply.
- Always load every mandatory guard in `criterion-bank.json`, independent of tags or route thresholds.
- If tags are missing/uncertain, use the named safe-minimum criteria and mark routing `NOT_ASSESSED`; escalate rather than infer a confidence score.
- An externally supplied router may be checked in `supplied` mode. Compare it with separately held development/oracle labels to detect route omissions; never pass protected labels into candidate selection.
- `all` mode is a diagnostic context comparison. `oracle` mode is allowed only on development/calibration or synthetic fixtures and is not a truth oracle for sources.

The current prototype uses explicit tags, not a model probability. Tag coverage and route quality have not been calibrated. No mode has production or release authority.

## Guidance identity and loading

Each criterion records a stable ID, paper mapping where applicable, owner, bank version, guidance path, SHA-256, trigger tags, required evidence, and boundary. Resolve guidance paths under the DRE root only. Reject traversal, missing files, duplicate IDs, or a digest mismatch. Record both selected and actually loaded criteria; reading a path does not prove the model applied it.

## Mandatory guards

Always preserve instruction/data separation and source provenance. Apply claim-level support to every material claim and currentness whenever the scope is time-sensitive. Domain controls are mandatory when the case says they apply; `unknown` applicability is an abstention, not an omission. A missing, failed, or unassessed mandatory guard prevents `ready`.

## Evidence-set result

The evaluator may report source-origin clusters, duplicated/related items, required subquestion gaps, and unresolved contradictions from explicit case metadata. It cannot determine whether metadata or prose is true. Every material finding must link to known source/claim IDs and a locator, or state `NOT_ASSESSED` and identify the gap.

The result is non-certifying. `ready` means only that this structural evaluation contract found no recorded blocker; source-verification and the responsible human/domain reviewer remain the release authorities. No model, source credibility, legal conclusion, or factual proposition is certified by this router.
