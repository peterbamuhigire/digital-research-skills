"""Unified source verification command-line tool.

Checks URLs, archive availability, quotes, statistics, and claim-source links
from a JSON or YAML manifest. The tool is intentionally conservative: an item
is release-ready only when required checks pass or the unresolved gap is
explicitly logged.

Input manifest shape:

sources:
  - id: src-001
    url: https://example.org/report
    archive_url: https://web.archive.org/...
    tier: 1
claims:
  - id: claim-001
    text: "..."
    source_ids: [src-001]
quotes:
  - id: quote-001
    text: "quoted text"
    source_id: src-001
    source_text_path: path/to/source.txt
statistics:
  - id: stat-001
    value: "42%"
    claim_id: claim-001
    source_id: src-001
    source_text_path: path/to/source.txt
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

try:
    import httpx
except ImportError:  # pragma: no cover - reported at runtime
    httpx = None  # type: ignore[assignment]

try:
    import yaml
except ImportError:  # pragma: no cover - JSON still works
    yaml = None  # type: ignore[assignment]

try:
    from .archive import all_snapshots
except ImportError:  # direct script execution
    from archive import all_snapshots  # type: ignore


REQUIRED_SOURCE_FIELDS = {"id", "tier"}


@dataclass(slots=True)
class CheckResult:
    item_type: str
    item_id: str
    status: str
    confidence: str
    evidence: str
    gaps: list[str] = field(default_factory=list)


@dataclass(slots=True)
class VerificationReport:
    generated_utc: str
    input_path: str
    release_ready: bool
    summary: dict[str, int]
    results: list[CheckResult]

    def to_dict(self) -> dict[str, Any]:
        return {
            "generated_utc": self.generated_utc,
            "input_path": self.input_path,
            "release_ready": self.release_ready,
            "summary": self.summary,
            "results": [asdict(r) for r in self.results],
        }


def load_manifest(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        if yaml is None:
            raise RuntimeError("PyYAML is required for YAML input; use JSON or install pyyaml.")
        data = yaml.safe_load(text)
    else:
        data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("Manifest root must be an object.")
    return data


def verify_manifest(path: Path, *, check_archives: bool = True, timeout: float = 20.0) -> VerificationReport:
    manifest = load_manifest(path)
    results: list[CheckResult] = []
    sources = {str(s.get("id")): s for s in manifest.get("sources", []) if isinstance(s, dict)}

    for source in manifest.get("sources", []) or []:
        if isinstance(source, dict):
            results.extend(verify_source(source, check_archives=check_archives, timeout=timeout))
        else:
            results.append(CheckResult("source", "unknown", "fail", "low", "Source entry is not an object."))

    for claim in manifest.get("claims", []) or []:
        if isinstance(claim, dict):
            results.append(verify_claim(claim, sources))

    for quote in manifest.get("quotes", []) or []:
        if isinstance(quote, dict):
            results.append(verify_quote(quote, sources))

    for stat in manifest.get("statistics", []) or []:
        if isinstance(stat, dict):
            results.append(verify_statistic(stat, sources))

    summary = {"pass": 0, "warn": 0, "fail": 0}
    for result in results:
        summary[result.status] = summary.get(result.status, 0) + 1

    release_ready = summary.get("fail", 0) == 0 and all(r.confidence != "low" for r in results)
    return VerificationReport(
        generated_utc=datetime.now(timezone.utc).isoformat(),
        input_path=str(path),
        release_ready=release_ready,
        summary=summary,
        results=results,
    )


def verify_source(source: dict[str, Any], *, check_archives: bool, timeout: float) -> list[CheckResult]:
    source_id = str(source.get("id", "unknown"))
    results: list[CheckResult] = []
    missing = sorted(REQUIRED_SOURCE_FIELDS - set(source))
    if missing:
        results.append(CheckResult("source", source_id, "fail", "low", "Missing required fields.", missing))
        return results

    tier = source.get("tier")
    if str(tier) not in {"1", "2", "3", "4", "5"}:
        results.append(CheckResult("source", source_id, "fail", "low", "Source tier must be 1-5.", ["invalid tier"]))

    url = source.get("url")
    if url:
        results.append(check_url(source_id, str(url), timeout=timeout))
        if check_archives:
            results.append(check_archive(source_id, str(url), source.get("archive_url")))
    else:
        results.append(CheckResult("source", source_id, "warn", "medium", "No URL supplied; verify locator manually.", ["manual locator"]))

    return results


def check_url(source_id: str, url: str, *, timeout: float) -> CheckResult:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return CheckResult("source-url", source_id, "fail", "low", f"Invalid URL: {url}")
    if httpx is None:
        return CheckResult("source-url", source_id, "warn", "medium", "httpx unavailable; URL check not run.", ["install httpx"])
    try:
        response = httpx.head(url, timeout=timeout, follow_redirects=True)
        if response.status_code in {405, 403}:
            response = httpx.get(url, timeout=timeout, follow_redirects=True)
        if 200 <= response.status_code < 400:
            return CheckResult("source-url", source_id, "pass", "high", f"HTTP {response.status_code}: {response.url}")
        return CheckResult("source-url", source_id, "fail", "low", f"HTTP {response.status_code}: {response.url}")
    except Exception as exc:  # network-specific exceptions vary by httpx version
        return CheckResult("source-url", source_id, "fail", "low", f"URL check failed: {exc}")


def check_archive(source_id: str, url: str, archive_url: Any) -> CheckResult:
    if archive_url:
        return CheckResult("source-archive", source_id, "pass", "high", f"Archive supplied: {archive_url}")
    try:
        snapshots = all_snapshots(url)
    except Exception as exc:
        return CheckResult("source-archive", source_id, "warn", "medium", f"Archive lookup failed: {exc}", ["archive unresolved"])
    if snapshots:
        first = snapshots[0]
        return CheckResult("source-archive", source_id, "pass", "high", f"Archive found: {first.archive_url}")
    return CheckResult("source-archive", source_id, "warn", "medium", "No archive snapshot found.", ["archive missing"])


def verify_claim(claim: dict[str, Any], sources: dict[str, dict[str, Any]]) -> CheckResult:
    claim_id = str(claim.get("id", "unknown"))
    source_ids = [str(x) for x in claim.get("source_ids", [])]
    if not source_ids:
        return CheckResult("claim", claim_id, "fail", "low", "Claim has no source_ids.")
    missing = [sid for sid in source_ids if sid not in sources]
    if missing:
        return CheckResult("claim", claim_id, "fail", "low", "Claim references unknown source IDs.", missing)
    text = str(claim.get("text", "")).strip()
    if len(text) < 10:
        return CheckResult("claim", claim_id, "warn", "medium", "Claim text is too thin to verify confidently.", ["thin claim text"])
    return CheckResult("claim", claim_id, "pass", "high", f"Claim references {len(source_ids)} known source(s).")


def verify_quote(quote: dict[str, Any], sources: dict[str, dict[str, Any]]) -> CheckResult:
    quote_id = str(quote.get("id", "unknown"))
    source_id = str(quote.get("source_id", ""))
    if source_id not in sources:
        return CheckResult("quote", quote_id, "fail", "low", "Quote references unknown source.", [source_id])
    quote_text = normalize_ws(str(quote.get("text", "")))
    if not quote_text:
        return CheckResult("quote", quote_id, "fail", "low", "Quote text is empty.")
    source_text = load_source_text(quote)
    if source_text is None:
        return CheckResult("quote", quote_id, "warn", "medium", "No source_text_path supplied; exact match not run.", ["manual quote check"])
    if quote_text in normalize_ws(source_text):
        return CheckResult("quote", quote_id, "pass", "high", "Exact quote found in source text.")
    return CheckResult("quote", quote_id, "fail", "low", "Exact quote not found in source text.", ["citation drift risk"])


def verify_statistic(stat: dict[str, Any], sources: dict[str, dict[str, Any]]) -> CheckResult:
    stat_id = str(stat.get("id", "unknown"))
    source_id = str(stat.get("source_id", ""))
    if source_id not in sources:
        return CheckResult("statistic", stat_id, "fail", "low", "Statistic references unknown source.", [source_id])
    value = str(stat.get("value", "")).strip()
    if not value:
        return CheckResult("statistic", stat_id, "fail", "low", "Statistic value missing.")
    source_text = load_source_text(stat)
    if source_text is None:
        return CheckResult("statistic", stat_id, "warn", "medium", "No source_text_path supplied; statistic requires manual spot-check.", ["manual statistic check"])
    if statistic_value_present(value, source_text):
        return CheckResult("statistic", stat_id, "pass", "high", f"Statistic value found in source text: {value}")
    return CheckResult("statistic", stat_id, "fail", "low", f"Statistic value not found in source text: {value}", ["citation drift risk"])


def load_source_text(item: dict[str, Any]) -> str | None:
    path = item.get("source_text_path")
    if not path:
        return None
    p = Path(str(path))
    if not p.exists():
        return None
    return p.read_text(encoding="utf-8", errors="replace")


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def statistic_value_present(value: str, text: str) -> bool:
    text_norm = normalize_ws(text)
    candidates = {value, value.replace(",", ""), value.replace("%", " percent")}
    for candidate in candidates:
        if candidate and candidate in text_norm:
            return True
    numbers = re.findall(r"\d+(?:[.,]\d+)?%?", value)
    return bool(numbers) and all(num in text_norm or num.replace(",", "") in text_norm for num in numbers)


def render_markdown(report: VerificationReport) -> str:
    lines = [
        "# Source Verification Report",
        "",
        f"Generated UTC: {report.generated_utc}",
        f"Input: `{report.input_path}`",
        f"Release ready: {'yes' if report.release_ready else 'no'}",
        "",
        "## Summary",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for key in ("pass", "warn", "fail"):
        lines.append(f"| {key} | {report.summary.get(key, 0)} |")
    lines.extend([
        "",
        "## Results",
        "",
        "| Type | ID | Status | Confidence | Evidence | Gaps |",
        "|---|---|---|---|---|---|",
    ])
    for result in report.results:
        gaps = "; ".join(result.gaps)
        evidence = result.evidence.replace("|", "\\|")
        lines.append(f"| {result.item_type} | {result.item_id} | {result.status} | {result.confidence} | {evidence} | {gaps} |")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify research source manifests.")
    parser.add_argument("manifest", type=Path, help="JSON or YAML manifest to verify")
    parser.add_argument("--out", type=Path, help="Write report to this path")
    parser.add_argument("--format", choices=["json", "md"], default="md")
    parser.add_argument("--no-archive", action="store_true", help="Skip archive lookup")
    parser.add_argument("--timeout", type=float, default=20.0)
    args = parser.parse_args(argv)

    report = verify_manifest(args.manifest, check_archives=not args.no_archive, timeout=args.timeout)
    if args.format == "json":
        output = json.dumps(report.to_dict(), indent=2, ensure_ascii=False)
    else:
        output = render_markdown(report)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output, encoding="utf-8")
    else:
        print(output)
    return 0 if report.release_ready else 2


if __name__ == "__main__":
    sys.exit(main())
