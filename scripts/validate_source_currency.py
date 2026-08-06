#!/usr/bin/env python3
"""Fail-closed validation for source freshness and review metadata."""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

REQUIRED = {"id", "accessed", "verified_at", "review_after", "freshness_class"}
CURRENT_CLASSES = {"volatile", "current", "regulatory", "market", "platform"}


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
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read manifest: {exc}"]
    sources = data.get("sources")
    if not isinstance(sources, list):
        return ["sources must be a list"]
    findings: list[str] = []
    source_map: dict[str, dict[str, Any]] = {}
    check_date = as_of or date.today()
    for source in sources:
        if not isinstance(source, dict):
            findings.append("source entries must be objects")
            continue
        source_id = str(source.get("id", "<unknown>"))
        source_map[source_id] = source
        for field in sorted(REQUIRED):
            if field not in source:
                findings.append(f"{source_id}: missing {field}")
        accessed = parse_date(source.get("accessed"), "accessed", source_id, findings)
        verified = parse_date(source.get("verified_at"), "verified_at", source_id, findings)
        review_after = parse_date(source.get("review_after"), "review_after", source_id, findings)
        freshness = str(source.get("freshness_class", "")).strip().lower()
        if freshness not in CURRENT_CLASSES | {"static", "historical"}:
            findings.append(f"{source_id}: unsupported freshness_class: {freshness}")
        if freshness in CURRENT_CLASSES and not (source.get("publication_date") or source.get("revision_date") or source.get("as_of")):
            findings.append(f"{source_id}: current source requires publication_date, revision_date, or as_of")
        for field in ("publication_date", "revision_date", "as_of"):
            if field in source:
                parse_date(source.get(field), field, source_id, findings)
        if accessed and verified and verified < accessed:
            findings.append(f"{source_id}: verified_at precedes accessed")
        if verified and review_after and review_after < verified:
            findings.append(f"{source_id}: review_after precedes verified_at")
        if review_after and review_after < check_date:
            findings.append(f"{source_id}: review_after is overdue as of {check_date.isoformat()}")
    for claim in data.get("claims", []) or []:
        if not isinstance(claim, dict) or not claim.get("requires_currentness"):
            continue
        claim_id = str(claim.get("id", "<unknown>"))
        for source_id in claim.get("source_ids", []) or []:
            source = source_map.get(str(source_id))
            if source is None:
                findings.append(f"{claim_id}: unknown source {source_id}")
            elif str(source.get("freshness_class", "")).lower() not in CURRENT_CLASSES:
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
        print("PASS: source currency is complete")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
