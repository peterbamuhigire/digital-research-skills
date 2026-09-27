"""Deterministic, non-certifying research-packet contract evaluator.

Only explicit case metadata is inspected. It never fetches sources, judges prose,
or certifies factual truth. See the routing and evidence-set contracts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any


GUARDS = {
    "instruction_data_separation": "always",
    "source_provenance": "always",
    "claim_level_support": "always",
    "currentness_when_required": "currentness_required",
    "domain_controls_when_required": "domain_control_required",
}


def _unique_ids(items: list[dict[str, Any]], label: str, errors: list[str]) -> set[str]:
    ids = [str(item.get("id", "")) for item in items]
    seen: set[str] = set()
    for value in ids:
        if not value:
            errors.append(f"{label}: missing ID")
        elif value in seen:
            errors.append(f"{label}: duplicate ID {value}")
        seen.add(value)
    return seen


def evaluate(case: dict[str, Any], bank: dict[str, Any], root: Path, mode: str = "dynamic", supplied: list[str] | None = None) -> dict[str, Any]:
    if mode not in {"dynamic", "all", "oracle", "supplied"}:
        raise ValueError(f"unknown mode: {mode}")
    errors: list[str] = []
    criteria = bank.get("criteria", [])
    guards = bank.get("mandatory_guards", [])
    criterion_ids = _unique_ids(criteria, "criterion bank", errors)
    guard_ids = _unique_ids(guards, "mandatory guards", errors)
    expected_guard_ids = set(bank.get("routing", {}).get("mandatory_guard_ids", []))
    if guard_ids != expected_guard_ids:
        errors.append("mandatory guard registry mismatch")

    tags = set(case.get("tags", []))
    known_tags = {tag for item in criteria for tag in item.get("trigger_tags", [])}
    route_uncertain = mode == "dynamic" and (not tags or not tags.intersection(known_tags))
    if mode == "all":
        selected = list(criteria)
    elif mode == "oracle":
        if not case.get("synthetic", False) and case.get("split") not in {"development", "calibration"}:
            errors.append("oracle mode is restricted to synthetic/development/calibration cases")
        ids = set(case.get("diagnostic_expected_criteria", []))
        selected = [item for item in criteria if item.get("id") in ids]
        if ids - criterion_ids:
            errors.append("oracle labels contain unknown criterion IDs")
    elif mode == "supplied":
        ids = set(supplied or [])
        selected = [item for item in criteria if item.get("id") in ids]
        if ids - criterion_ids:
            errors.append("supplied route contains unknown criterion IDs")
    else:
        selected = [item for item in criteria if tags.intersection(item.get("trigger_tags", []))]
        if route_uncertain:
            selected = [item for item in criteria if item.get("id") in bank.get("routing", {}).get("safe_minimum", [])]

    loaded: list[dict[str, str]] = []
    for item in selected + guards:
        rel = item.get("guidance_path", "")
        candidate = (root / rel).resolve()
        try:
            candidate.relative_to(root.resolve())
        except ValueError:
            errors.append(f"guidance path escapes engine root: {rel}")
            continue
        if not candidate.is_file():
            errors.append(f"guidance file missing: {rel}")
            continue
        digest = hashlib.sha256(candidate.read_bytes()).hexdigest().upper()
        if digest != str(item.get("guidance_sha256", "")).upper():
            errors.append(f"guidance hash mismatch: {rel}")
            continue
        loaded.append({"id": item["id"], "path": rel, "sha256": digest})

    sources = case.get("sources", [])
    claims = case.get("claims", [])
    source_ids = _unique_ids(sources, "sources", errors)
    claim_ids = _unique_ids(claims, "claims", errors)
    source_by_id = {x.get("id"): x for x in sources}
    for source in sources:
        if not source.get("origin_cluster_id"):
            errors.append(f"source {source.get('id')}: missing origin cluster")
        if not source.get("locator"):
            errors.append(f"source {source.get('id')}: missing locator")
    for claim in claims:
        if not claim.get("source_ids"):
            errors.append(f"claim {claim.get('id')}: no source references")
        for sid in claim.get("source_ids", []):
            if sid not in source_ids:
                errors.append(f"claim {claim.get('id')}: unknown source {sid}")
        if claim.get("material", True) and not claim.get("locator"):
            errors.append(f"material claim {claim.get('id')}: missing locator")

    gaps = sorted(set(case.get("required_subquestion_ids", [])) - set(case.get("covered_subquestion_ids", [])))
    contradictions: list[str] = []
    blockers = list(errors)
    for item in case.get("contradictions", []):
        refs_ok = item.get("claim_id") in claim_ids and all(sid in source_ids for sid in item.get("source_ids", []))
        if not refs_ok:
            errors.append(f"contradiction {item.get('id')}: invalid claim/source references")
            blockers.append(f"invalid contradiction references: {item.get('id')}")
        if item.get("status") == "unresolved":
            contradictions.append(str(item.get("id")))
            if item.get("decision_critical"):
                blockers.append(f"critical unresolved contradiction: {item.get('id')}")

    guard_states = case.get("mandatory_guards", {})
    unknown_guard_states = set(guard_states) - guard_ids
    if unknown_guard_states:
        errors.append("unknown mandatory guard IDs: " + ", ".join(sorted(unknown_guard_states)))
        blockers.append("unknown mandatory guard IDs")
    for guard in guards:
        gid = guard.get("id")
        when = GUARDS.get(gid, "always")
        applicable = when == "always" or bool(case.get(when, False))
        state = guard_states.get(gid, "not_assessed")
        if applicable and state != "passed":
            blockers.append(f"mandatory guard {gid}: {state}")
        if not applicable and state not in {"not_applicable", "passed"}:
            blockers.append(f"guard applicability unresolved: {gid}")

    route_misses = sorted(set(case.get("diagnostic_expected_criteria", [])) - {x["id"] for x in selected}) if mode in {"dynamic", "supplied"} else []
    clusters: dict[str, list[str]] = {}
    for source in sources:
        clusters.setdefault(str(source.get("origin_cluster_id", "")), []).append(str(source.get("id", "")))
    findings: list[dict[str, Any]] = []
    if gaps:
        findings.append({"id": "subquestion_coverage", "severity": "major", "support_state": "not_assessed", "source_ids": [], "claim_ids": [], "locator": None, "summary": "Required subquestions remain uncovered: " + ", ".join(gaps)})
    for contradiction in case.get("contradictions", []):
        if contradiction.get("status") == "unresolved":
            findings.append({"id": str(contradiction.get("id")), "severity": "critical" if contradiction.get("decision_critical") else "major", "support_state": "not_assessed", "source_ids": contradiction.get("source_ids", []), "claim_ids": [contradiction.get("claim_id")], "locator": contradiction.get("locator"), "summary": "Contradiction is recorded as unresolved; evaluator does not adjudicate it."})

    status = "blocked" if blockers else ("not_assessed" if errors or route_uncertain or route_misses or gaps or contradictions else "ready")
    return {
        "case_id": case.get("case_id", ""), "mode": mode,
        "selected_criteria": [x["id"] for x in selected], "loaded_guidance": loaded,
        "routing_assessed": not route_uncertain,
        "findings": findings,
        "source_origin_clusters": [{"origin_cluster_id": key, "source_ids": sorted(values), "count": len(values)} for key, values in sorted(clusters.items())],
        "subquestion_gaps": gaps, "unresolved_contradictions": contradictions,
        "routing_misses": route_misses, "blockers": sorted(set(blockers)),
        "structural_errors": sorted(set(errors)), "status": status, "certifies_truth": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--bank", type=Path, default=Path("skills/ai-evaluation-and-data-flywheel/references/criterion-bank.json"))
    parser.add_argument("--mode", choices=("dynamic", "all", "oracle", "supplied"), default="dynamic")
    parser.add_argument("--criteria", default="", help="Comma-separated criterion IDs for supplied mode")
    args = parser.parse_args()
    try:
        case = json.loads(args.case.read_text(encoding="utf-8"))
        bank_path = args.bank if args.bank.is_absolute() else args.root / args.bank
        bank = json.loads(bank_path.read_text(encoding="utf-8"))
        result = evaluate(case, bank, args.root, args.mode, [x for x in args.criteria.split(",") if x])
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"evaluation error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["structural_errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
