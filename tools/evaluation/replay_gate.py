"""Read-only gate for proposed skill guidance revisions; never promotes or writes."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any


FAILURE_CAUSES = {"routing", "knowledge", "execution", "source/tool", "gold-label", "mixed", "unknown"}


def evaluate(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    candidate = record.get("candidate", {})
    controls = record.get("controls", {})
    emerging = record.get("emerging", {})
    replay = record.get("replay", {})
    ambiguous = record.get("ambiguous", {})
    def count(section: dict[str, Any], key: str, label: str) -> int:
        value = section.get(key, 0)
        if type(value) is not int or value < 0:
            errors.append(f"{label}.{key} must be a non-negative integer")
            return 0
        return value
    cause = candidate.get("primary_cause")
    if cause not in FAILURE_CAUSES:
        errors.append("unknown primary cause")
    if candidate.get("protected_labels_seen") is True:
        errors.append("candidate author saw protected labels")
    if not candidate.get("rollback_target"):
        errors.append("missing rollback target")
    if controls.get("routing_description_unchanged") is not True:
        errors.append("routing description changed or not verified")
    if controls.get("model_runtime_unchanged") is not True:
        errors.append("model/runtime changed or not verified")
    if controls.get("evaluation_contract_unchanged") is not True:
        errors.append("evaluation contract changed or not verified")

    critical = count(emerging, "critical_failures", "emerging") + count(replay, "critical_failures", "replay")
    false_ready = count(emerging, "critical_false_ready", "emerging") + count(replay, "critical_false_ready", "replay") + count(ambiguous, "critical_false_ready", "ambiguous")
    regressions = count(replay, "regressions", "replay")
    reasons = list(errors)
    if critical:
        reasons.append("critical failure observed")
    if false_ready:
        reasons.append("critical false-ready transition observed")
    if regressions:
        reasons.append("historical replay regression observed")

    if errors or critical or false_ready or regressions:
        status = "rejected"
    elif cause in {"mixed", "unknown"}:
        status = "not_assessed"
        reasons.append("cause is unresolved; do not create a guidance-only revision")
    elif cause != "knowledge":
        status = "not_assessed"
        reasons.append("primary cause belongs to a non-knowledge repair path")
    else:
        missing: list[str] = []
        if record.get("synthetic") is True or candidate.get("synthetic") is True:
            missing.append("evidence is synthetic")
        if controls.get("reviewed_labels_verified") is not True:
            missing.append("reviewed labels not verified")
        if count(record, "distinct_reviewed_cases", "record") < 3:
            missing.append("fewer than three reviewer-confirmed recurrence cases")
        if count(record, "distinct_source_clusters", "record") < 3:
            missing.append("fewer than three distinct source-origin clusters")
        if count(emerging, "cases", "emerging") < 1 or count(emerging, "improved", "emerging") < 1:
            missing.append("no measured emerging-case improvement")
        if count(replay, "cases", "replay") < 1:
            missing.append("no historical replay evidence")
        if controls.get("independent_review") is not True:
            missing.append("independent review absent")
        if controls.get("semantic_review_complete") is not True:
            missing.append("semantic review incomplete")
        if controls.get("uncertainty_reported") is not True:
            missing.append("paired uncertainty evidence absent")
        if count(ambiguous, "cases", "ambiguous") < 1:
            missing.append("ambiguous/needs-work slice is not assessed")
        if ambiguous.get("noninferiority_pass") is not True:
            missing.append("predeclared ambiguous-slice noninferiority gate not passed")
        if missing:
            status = "rejected" if errors else "not_assessed"
            reasons.extend(errors)
            reasons.extend(missing)
        else:
            status = "eligible_for_authorized_review"
            reasons.append("all supplied gates pass; maintainer must review this handoff")

    return {
        "candidate_id": candidate.get("candidate_id", ""),
        "status": status,
        "reasons": reasons,
        "rollback_target": candidate.get("rollback_target"),
        "promotion_performed": False,
        "canonical_guidance_written": False,
        "semantic_truth_certified": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"replay-gate input error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(evaluate(record), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
