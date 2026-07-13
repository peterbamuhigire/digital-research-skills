#!/usr/bin/env python3
"""Validate active skills against the Digital Research Engine authoring contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ACTIVE_ROOTS = (Path("skills"),)
EXCLUDED_TREES = (Path("skills/proposal-skills"),)
TEMPLATE_ROOTS = (Path("templates"),)
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}
ALLOWED_METADATA = {"portable", "compatible_with", "priority", "source"}
COMPATIBILITY = ["claude-code", "codex"]
MANDATORY_RESOURCES = (
    Path("SKILL.md"),
    Path("skills/source-evaluation/references/evidence-discipline.md"),
    Path("docs/quality-gates/release-blocking-gates.md"),
    Path("templates/research-evidence-pack-template.md"),
    Path("templates/source-verification-manifest-template.yaml"),
    Path("tools/verification/source_verifier.py"),
)
REQUIRED_SECTIONS = (
    "Use When",
    "Do Not Use When",
    "Inputs",
    "Workflow",
    "Outputs",
    "Evidence Produced",
    "Capability Contract",
    "Degraded Mode",
    "Decision Rules",
    "Quality Standards",
    "Anti-Patterns",
    "Worked Example",
    "References",
)
MOJIBAKE = ("Ãƒ", "Ã‚", "Ã¢â‚¬", "Ã¢â€", "Ã°Å¸", "â€”", "â€“", "â€™", "ï¿½", "\ufffd")
RUNNER_SPECIFIC = re.compile(
    r"\b(?:WebFetch|WebSearch|Bash tool|Task tool|Claude Code tool|Codex tool|mcp__[a-z0-9_]+|functions\.[a-z_][a-z0-9_]*(?=\s*\())\b",
    re.IGNORECASE,
)
FRONTMATTER_RE = re.compile(r"^\ufeff?---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--details", action="store_true")
    return parser.parse_args()


def under(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def discover(root: Path, roots: tuple[Path, ...], excludes: tuple[Path, ...] = ()) -> list[Path]:
    excluded = tuple((root / item).resolve() for item in excludes)
    found: set[Path] = set()
    for relative in roots:
        base = root / relative
        if not base.exists():
            continue
        for path in base.rglob("SKILL.md"):
            resolved = path.resolve()
            if path.is_file() and not any(under(resolved, blocked) for blocked in excluded):
                found.add(resolved)
    return sorted(found)


def parse_skill(path: Path) -> tuple[dict, str, str | None]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    match = FRONTMATTER_RE.match(raw)
    if not match:
        return {}, raw, "missing or malformed YAML frontmatter"
    try:
        metadata = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return {}, raw[match.end() :], f"invalid YAML: {exc}"
    if not isinstance(metadata, dict):
        return {}, raw[match.end() :], "frontmatter is not a mapping"
    return metadata, raw[match.end() :], None


def sections(body: str) -> dict[str, str]:
    matches = list(HEADING_RE.finditer(body))
    output: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        output[match.group(1).strip().casefold()] = body[match.end() : end].strip()
    return output


def get_section(parts: dict[str, str], wanted: str) -> str:
    aliases = {
        "Inputs": ("inputs", "required inputs"),
        "Capability Contract": ("capability contract", "capability and permission boundaries"),
        "Degraded Mode": ("degraded mode",),
        "Decision Rules": ("decision rules", "decision table"),
        "Worked Example": ("worked example", "worked examples"),
    }
    for name in aliases.get(wanted, (wanted.casefold(),)):
        if name in parts:
            return parts[name]
    return ""


def table_present(text: str) -> bool:
    lines = [line for line in text.splitlines() if line.lstrip().startswith("|")]
    return len(lines) >= 2 and any(re.search(r"\|\s*:?-{3,}", line) for line in lines)


def resolve_link(root: Path, skill: Path, target: str) -> bool:
    clean = target.strip().split("#", 1)[0]
    if not clean or clean.startswith(("http://", "https://", "mailto:", "#")):
        return True
    clean = clean.replace("%20", " ")
    return (skill.parent / clean).resolve().exists() or (root / clean).resolve().exists()


def assess(root: Path, path: Path) -> list[tuple[str, str]]:
    frontmatter, body, parse_error = parse_skill(path)
    raw = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(root).as_posix()
    findings: list[tuple[str, str]] = []

    def add(code: str, detail: str) -> None:
        findings.append((code, detail))

    if parse_error:
        add("invalid_frontmatter", parse_error)
    name = frontmatter.get("name")
    if name != path.parent.name:
        add("name_mismatch", f"frontmatter name {name!r} does not match {path.parent.name!r}")
    unsupported = sorted(set(frontmatter) - ALLOWED_FRONTMATTER)
    if unsupported:
        add("unsupported_frontmatter", ", ".join(unsupported))
    metadata = frontmatter.get("metadata", {})
    if not isinstance(metadata, dict):
        add("portable_metadata", "metadata must be a mapping")
        metadata = {}
    unsupported_metadata = sorted(set(metadata) - ALLOWED_METADATA)
    if unsupported_metadata:
        add("unsupported_metadata", ", ".join(unsupported_metadata))
    if metadata.get("portable") is not True or metadata.get("compatible_with") != COMPATIBILITY:
        add("portable_metadata", "require portable: true and compatible_with: [claude-code, codex]")
    description = frontmatter.get("description", "")
    if not isinstance(description, str) or not description.strip().lower().startswith("use when"):
        add("description_trigger", "description must begin with 'Use when'")
    elif "\n" in description or len(description.strip()) > 350:
        add("description_length", f"description length is {len(description.strip())}; maximum is 350")
    elif len(description.strip()) < 55:
        add("weak_description", "description is too short to distinguish scope and neighbour")

    heading_names = [match.group(1).strip().casefold() for match in HEADING_RE.finditer(body)]
    parts = sections(body)
    for title in REQUIRED_SECTIONS:
        content = get_section(parts, title)
        if not content:
            add("missing_or_empty_section", title)
        aliases = {
            "Inputs": ("inputs", "required inputs"),
            "Capability Contract": ("capability contract", "capability and permission boundaries"),
            "Worked Example": ("worked example", "worked examples"),
        }.get(title, (title.casefold(),))
        count = sum(heading_names.count(alias) for alias in aliases)
        if count > 1:
            add("duplicate_contract_section", f"{title} appears {count} times; consolidate or rename legacy detail")

    inputs = get_section(parts, "Inputs")
    if inputs and not (table_present(inputs) or re.search(r"\bno (?:input|upstream artefact)s?\b|\bnone\b", inputs, re.I)):
        add("input_contract", "Inputs must use a table or explicitly declare no inputs")
    outputs = get_section(parts, "Outputs")
    if outputs and (not table_present(outputs) or not re.search(r"consumer|consumed by", outputs, re.I) or not re.search(r"accept", outputs, re.I)):
        add("output_contract", "Outputs table must name consumer and acceptance condition")
    evidence = get_section(parts, "Evidence Produced")
    if evidence and not table_present(evidence):
        add("evidence_contract", "Evidence Produced must use a table")
    workflow = get_section(parts, "Workflow")
    if workflow and not re.search(r"^\s*\d+[.)]\s+", workflow, re.M):
        add("workflow_order", "Workflow must be ordered")
    if workflow and not re.search(r"\bstop|block|halt\b", workflow, re.I):
        add("workflow_stop", "Workflow must name a stop condition")
    if workflow and not re.search(r"\brecover|retry|fallback|resume|repair\b", workflow, re.I):
        add("workflow_recovery", "Workflow must name recovery behaviour")
    decisions = get_section(parts, "Decision Rules")
    if decisions and (not table_present(decisions) or not re.search(r"risk|failure|avoided|wrong", decisions, re.I)):
        add("decision_contract", "Decision table must name the risk or failure avoided")
    capabilities = get_section(parts, "Capability Contract")
    if capabilities and not re.search(r"\bread\b", capabilities, re.I):
        add("capability_contract", "minimum read capability is not stated")
    if capabilities and not re.search(r"authori[sz]|permission|explicit", capabilities, re.I):
        add("permission_boundary", "mutation authority boundary is not explicit")
    degraded = get_section(parts, "Degraded Mode")
    if degraded and not re.search(r"unassessed|not assessed|qualified|gap|cannot|unavailable|narrowest", degraded, re.I):
        add("degraded_mode", "must return a qualified narrow result and preserve unassessed checks")
    anti = get_section(parts, "Anti-Patterns")
    anti_count = len(re.findall(r"^\s*(?:[-*]|\d+[.)])\s+", anti, re.M))
    if anti and (anti_count < 5 or not re.search(r"\bfix\b|\bcorrection\b|\binstead\b", anti, re.I)):
        add("anti_patterns", f"found {anti_count}; require five concrete items paired with corrections")
    quality = get_section(parts, "Quality Standards")
    if quality and len(quality.split()) < 12:
        add("quality_contract", "Quality Standards is too thin to be observable")
    example = get_section(parts, "Worked Example")
    if example and len(example.split()) < 18:
        add("worked_example", "worked example is too thin to demonstrate the contract")

    lowered_name = str(name or "").casefold()
    if any(term in lowered_name for term in ("audit", "review", "analysis", "evaluation", "planning")):
        if not re.search(r"default(?:s| to)?\s+(?:to\s+)?read-only|read-only by default|default to read-only", capabilities, re.I):
            add("audit_read_only", "audit/review/analysis/planning skill must default to read-only")
    if RUNNER_SPECIFIC.search(body):
        add("runner_specific_body", "portable skill body contains runner-specific tool syntax")
    if any(marker in raw for marker in MOJIBAKE):
        add("encoding_noise", "mojibake marker present")
    line_count = len(raw.splitlines())
    if line_count > 500:
        add("line_limit", f"{line_count} lines")

    for target in LINK_RE.findall(body):
        if not resolve_link(root, path, target):
            add("broken_relative_link", target)

    return [(code, f"{rel}: {detail}") for code, detail in findings]


def run(root: Path) -> dict:
    active = discover(root, ACTIVE_ROOTS, EXCLUDED_TREES)
    templates = discover(root, TEMPLATE_ROOTS)
    all_findings: list[tuple[str, str]] = []
    names: defaultdict[str, list[str]] = defaultdict(list)
    descriptions: defaultdict[str, list[str]] = defaultdict(list)
    for path in active:
        frontmatter, _, _ = parse_skill(path)
        names[str(frontmatter.get("name"))].append(path.relative_to(root).as_posix())
        descriptions[str(frontmatter.get("description", "")).strip().casefold()].append(path.relative_to(root).as_posix())
        all_findings.extend(assess(root, path))
    for name, paths in names.items():
        if name != "None" and len(paths) > 1:
            all_findings.append(("duplicate_name", f"{name}: {', '.join(paths)}"))
    for description, paths in descriptions.items():
        if description and len(paths) > 1:
            all_findings.append(("duplicate_description", f"{', '.join(paths)}"))
    for resource in MANDATORY_RESOURCES:
        if not (root / resource).is_file():
            all_findings.append(("missing_mandatory_resource", resource.as_posix()))
    counts = Counter(code for code, _ in all_findings)
    return {
        "root": str(root),
        "active_skills": len(active),
        "template_skills": len(templates),
        "fully_compliant": len(active) - len({detail.split(":", 1)[0] for _, detail in all_findings if detail.startswith("skills/")}),
        "failure_counts": dict(sorted(counts.items())),
        "findings": [{"code": code, "detail": detail} for code, detail in all_findings],
    }


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    payload = run(root)
    baseline_error = None
    if args.baseline:
        baseline_path = args.baseline if args.baseline.is_absolute() else root / args.baseline
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
        expected = {
            "active_skills": baseline.get("active_skills"),
            "template_skills": baseline.get("template_skills"),
            "failure_counts": baseline.get("failure_counts", {}),
        }
        actual = {key: payload[key] for key in expected}
        if actual != expected:
            baseline_error = {"expected": expected, "actual": actual}
            payload["baseline_mismatch"] = baseline_error
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"skill-contract-validator: {root}")
        print(f"- active skills: {payload['active_skills']}")
        print(f"- template skills: {payload['template_skills']}")
        print(f"- fully compliant: {payload['fully_compliant']}")
        print(f"- failure counts: {json.dumps(payload['failure_counts'], sort_keys=True)}")
        if args.details:
            for finding in payload["findings"]:
                print(f"- {finding['code']}: {finding['detail']}")
        if baseline_error:
            print("- baseline mismatch")
    return 1 if payload["failure_counts"] or baseline_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
