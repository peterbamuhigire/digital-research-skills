#!/usr/bin/env python3
"""Fail-closed validation for source freshness and review metadata."""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

REQUIRED = {"id", "accessed", "verified_at", "review_after", "freshness_class"}
CURRENT_CLASSES = {"volatile", "current", "regulatory", "market", "platform", "context-bound"}


def parse_date(value: Any, field: str, source_id: str, findings: list[str]) -> date | None:
    if not isinstance(value, str) or not value.strip():
        findings.append(f"{source_id}: {field} is required as ISO date")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        findings.append(f"{source_id}: {field} is not ISO date: {value}")
        return None


def validate_manifest(path: Path, as_of: date | None = None) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"cannot read manifest: {exc}"]
    if not isinstance(data, dict):
        return ["manifest must be an object"]
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        return ["sources must be a nonempty list"]
    findings: list[str] = []
    source_map: dict[str, dict[str, Any]] = {}
    check_date = as_of or date.today()
    for source in sources:
        if not isinstance(source, dict):
            findings.append("source entries must be objects")
            continue
        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id.strip():
            findings.append("source id must be a nonempty string")
            continue
        if source_id in source_map:
            findings.append(f"duplicate source id: {source_id}")
            continue
        source_map[source_id] = source
        for field in sorted(REQUIRED):
            if field not in source:
                findings.append(f"{source_id}: missing {field}")
        accessed = parse_date(source.get("accessed"), "accessed", source_id, findings)
        verified = parse_date(source.get("verified_at"), "verified_at", source_id, findings)
        review_after = parse_date(source.get("review_after"), "review_after", source_id, findings)
        freshness_value = source.get("freshness_class")
        freshness = freshness_value.strip().lower() if isinstance(freshness_value, str) else ""
        if freshness not in CURRENT_CLASSES | {"static", "historical"}:
            findings.append(f"{source_id}: unsupported freshness_class: {freshness}")
        if freshness in CURRENT_CLASSES and not (source.get("publication_date") or source.get("revision_date") or source.get("as_of")):
            findings.append(f"{source_id}: current source requires publication_date, revision_date, or as_of")
        if freshness == "context-bound" and (
            not isinstance(source.get("scope"), str) or not source["scope"].strip()
        ):
            findings.append(f"{source_id}: context-bound source requires nonempty scope")
        for field in ("publication_date", "revision_date", "as_of"):
            if field in source:
                parse_date(source.get(field), field, source_id, findings)
        if accessed and verified and verified < accessed:
            findings.append(f"{source_id}: verified_at precedes accessed")
        for field, value in (("accessed", accessed), ("verified_at", verified)):
            if value and value > check_date:
                findings.append(f"{source_id}: {field} is in the future as of {check_date.isoformat()}")
        if verified and review_after and review_after < verified:
            findings.append(f"{source_id}: review_after precedes verified_at")
        if review_after and review_after < check_date:
            findings.append(f"{source_id}: review_after is overdue as of {check_date.isoformat()}")
    claims = data.get("claims", [])
    if not isinstance(claims, list):
        findings.append("claims must be a list")
        return findings
    claim_ids: set[str] = set()
    for claim in claims:
        if not isinstance(claim, dict):
            findings.append("claim entries must be objects")
            continue
        claim_id = claim.get("id")
        if not isinstance(claim_id, str) or not claim_id.strip():
            findings.append("claim id must be a nonempty string")
            continue
        if claim_id in claim_ids:
            findings.append(f"duplicate claim id: {claim_id}")
        claim_ids.add(claim_id)
        current = claim.get("requires_currentness")
        if not isinstance(current, bool):
            findings.append(f"{claim_id}: requires_currentness must be boolean")
        source_ids = claim.get("source_ids")
        if not isinstance(source_ids, list):
            findings.append(f"{claim_id}: source_ids must be a list")
            continue
        if current is True and not source_ids:
            findings.append(f"{claim_id}: current claim requires nonempty source_ids")
        seen_sources: set[str] = set()
        for source_id in source_ids:
            if not isinstance(source_id, str) or not source_id.strip():
                findings.append(f"{claim_id}: source_ids entries must be nonempty strings")
                continue
            if source_id in seen_sources:
                findings.append(f"{claim_id}: duplicate source id: {source_id}")
            seen_sources.add(source_id)
            source = source_map.get(source_id)
            if source is None:
                findings.append(f"{claim_id}: unknown source {source_id}")
            elif current is True and (
                not isinstance(source.get("freshness_class"), str)
                or source["freshness_class"].strip().lower() not in CURRENT_CLASSES
            ):
                findings.append(f"{claim_id}: source {source_id} is not currentness-qualified")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()
    findings = validate_manifest(args.manifest.resolve(), args.as_of)
    print("source-currency-validator:")
    print(f"- manifest: {args.manifest}")
    print(f"- as-of: {args.as_of.isoformat()}")
    print(f"- findings: {len(findings)}")
    for finding in findings:
        print(f"[FAIL] {finding}")
    if not findings:
        print("PASS: metadata/date checks only; claim support NOT ASSESSED")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
