"""Citation density and freshness dashboard for research drafts.

The tool reads a Markdown draft and an optional source manifest, then reports
paragraph-level citation coverage, source-tier mix, stale-source risk, and
unsupported-claim flags. It is designed as a release gate companion, not a
style checker.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore[assignment]


CITATION_PATTERNS = [
    re.compile(r"\[[^\]]+\]\([^)]+\)"),
    re.compile(r"\[[A-Za-z0-9_.:-]+\]"),
    re.compile(r"\(source:\s*[^)]+\)", re.IGNORECASE),
    re.compile(r"\b(?:src|source)-\d{3,}\b", re.IGNORECASE),
]
NUMERIC_CLAIM = re.compile(
    r"(?<!\w)(?:\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)(?:\s?%|\s+(?:million|billion|trillion|km|kg|USD|UGX|KES|TZS|years?|months?))",
    re.IGNORECASE,
)
QUOTE = re.compile(r'"[^"\n]{30,}"')


@dataclass(slots=True)
class ParagraphFinding:
    index: int
    status: str
    citations: int
    numeric_claims: int
    quotes: int
    excerpt: str
    issue: str


def load_manifest(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        if yaml is None:
            raise RuntimeError("PyYAML is required for YAML manifests.")
        return yaml.safe_load(text) or {}
    return json.loads(text)


def split_paragraphs(markdown: str) -> list[str]:
    blocks = [p.strip() for p in re.split(r"\n\s*\n", markdown) if p.strip()]
    ignored_prefixes = (
        "|",
        "```",
        "#",
        "Last verified:",
        "Benchmark:",
        "Status:",
        "See also:",
    )
    return [p for p in blocks if not p.startswith(ignored_prefixes)]


def count_citations(text: str) -> int:
    return sum(len(p.findall(text)) for p in CITATION_PATTERNS)


def analyse_paragraphs(markdown: str) -> list[ParagraphFinding]:
    findings: list[ParagraphFinding] = []
    for idx, para in enumerate(split_paragraphs(markdown), start=1):
        citations = count_citations(para)
        numeric = len(NUMERIC_CLAIM.findall(para))
        quotes = len(QUOTE.findall(para))
        issue = ""
        status = "pass"
        if (numeric or quotes) and citations == 0:
            status = "fail"
            issue = "Numeric claim or quote without paragraph-level citation."
        elif citations == 0 and len(para) > 280:
            status = "warn"
            issue = "Long analytical paragraph without citation."
        findings.append(
            ParagraphFinding(
                index=idx,
                status=status,
                citations=citations,
                numeric_claims=numeric,
                quotes=quotes,
                excerpt=re.sub(r"\s+", " ", para)[:160],
                issue=issue,
            )
        )
    return findings


def source_mix(manifest: dict[str, Any], *, today: date) -> dict[str, Any]:
    sources = [s for s in manifest.get("sources", []) if isinstance(s, dict)]
    tiers: dict[str, int] = {}
    stale: list[str] = []
    missing_archive: list[str] = []
    for source in sources:
        tier = str(source.get("tier", "missing"))
        tiers[tier] = tiers.get(tier, 0) + 1
        source_id = str(source.get("id", "unknown"))
        if source.get("url") and not source.get("archive_url"):
            missing_archive.append(source_id)
        accessed = source.get("accessed_utc") or source.get("accessed")
        if accessed and is_stale(str(accessed), today=today):
            stale.append(source_id)
    primary_secondary = sum(tiers.get(str(t), 0) for t in (1, 2, 3))
    total = len(sources)
    return {
        "total_sources": total,
        "tier_counts": tiers,
        "tier_1_to_3_share": round(primary_secondary / total, 3) if total else None,
        "stale_source_ids": stale,
        "missing_archive_source_ids": missing_archive,
    }


def is_stale(value: str, *, today: date) -> bool:
    match = re.search(r"\d{4}-\d{2}-\d{2}", value)
    if not match:
        return True
    try:
        accessed = datetime.strptime(match.group(0), "%Y-%m-%d").date()
    except ValueError:
        return True
    return (today - accessed).days > 365


def build_report(draft: Path, manifest_path: Path | None) -> dict[str, Any]:
    markdown = draft.read_text(encoding="utf-8")
    manifest = load_manifest(manifest_path)
    findings = analyse_paragraphs(markdown)
    summary = {"pass": 0, "warn": 0, "fail": 0}
    for finding in findings:
        summary[finding.status] += 1
    today = datetime.now(timezone.utc).date()
    return {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "draft": str(draft),
        "manifest": str(manifest_path) if manifest_path else None,
        "release_ready": summary["fail"] == 0,
        "paragraph_summary": summary,
        "source_mix": source_mix(manifest, today=today) if manifest else {},
        "findings": [asdict(finding) for finding in findings if finding.status != "pass"],
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Citation Density Dashboard",
        "",
        f"Generated UTC: {report['generated_utc']}",
        f"Draft: `{report['draft']}`",
        f"Manifest: `{report['manifest']}`",
        f"Release ready: {'yes' if report['release_ready'] else 'no'}",
        "",
        "## Paragraph Coverage",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for key, value in report["paragraph_summary"].items():
        lines.append(f"| {key} | {value} |")
    if report["source_mix"]:
        mix = report["source_mix"]
        lines.extend([
            "",
            "## Source Mix",
            "",
            f"- Total sources: {mix['total_sources']}",
            f"- Tier 1-3 share: {mix['tier_1_to_3_share']}",
            f"- Tier counts: `{json.dumps(mix['tier_counts'], sort_keys=True)}`",
            f"- Stale sources: {', '.join(mix['stale_source_ids']) or 'none'}",
            f"- Missing archives: {', '.join(mix['missing_archive_source_ids']) or 'none'}",
        ])
    lines.extend([
        "",
        "## Findings",
        "",
        "| Paragraph | Status | Citations | Numeric claims | Quotes | Issue | Excerpt |",
        "|---:|---|---:|---:|---:|---|---|",
    ])
    for finding in report["findings"]:
        excerpt = str(finding["excerpt"]).replace("|", "\\|")
        issue = str(finding["issue"]).replace("|", "\\|")
        lines.append(
            f"| {finding['index']} | {finding['status']} | {finding['citations']} | "
            f"{finding['numeric_claims']} | {finding['quotes']} | {issue} | {excerpt} |"
        )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate citation density dashboard.")
    parser.add_argument("draft", type=Path, help="Markdown draft to inspect")
    parser.add_argument("--manifest", type=Path, help="Optional JSON/YAML source manifest")
    parser.add_argument("--out", type=Path, help="Write report to this path")
    parser.add_argument("--format", choices=["json", "md"], default="md")
    args = parser.parse_args(argv)

    report = build_report(args.draft, args.manifest)
    output = json.dumps(report, indent=2, ensure_ascii=False) if args.format == "json" else render_markdown(report)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output, encoding="utf-8")
    else:
        print(output)
    return 0 if report["release_ready"] else 2


if __name__ == "__main__":
    sys.exit(main())
