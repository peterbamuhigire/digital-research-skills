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
    support_review:
      state: supported | unsupported | synthesis | inference | no-source
      reviewer: "named reviewer or test-labelled reviewer"
      basis: "brief human review basis"
      reviewed_at: 2026-08-11
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
CLAIM_SUPPORT_STATES = {"supported", "unsupported", "synthesis", "inference", "no-source"}


@dataclass(slots=True)
class CheckResult:
    item_type: str
    item_id: str
    status: str
    confidence: str
    evidence: str
    gaps: list[str] = field(default_factory=list)
    support_state: str | None = None


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
    source_entries = manifest_entries(manifest, "sources", results)
    claim_entries = manifest_entries(manifest, "claims", results)
    quote_entries = manifest_entries(manifest, "quotes", results)
    statistic_entries = manifest_entries(manifest, "statistics", results)
    sources = {str(s.get("id")): s for s in source_entries if isinstance(s, dict)}

    for source in source_entries:
        if isinstance(source, dict):
            results.extend(verify_source(source, check_archives=check_archives, timeout=timeout))
        else:
            results.append(CheckResult("source", "unknown", "fail", "low", "Source entry is not an object."))

    for claim in claim_entries:
        if isinstance(claim, dict):
            results.append(verify_claim(claim, sources))
        else:
            results.append(CheckResult("claim", "unknown", "fail", "low", "Claim entry is not an object."))

    for quote in quote_entries:
        if isinstance(quote, dict):
            results.append(verify_quote(quote, sources))
        else:
            results.append(CheckResult("quote", "unknown", "fail", "low", "Quote entry is not an object."))

    for stat in statistic_entries:
        if isinstance(stat, dict):
            results.append(verify_statistic(stat, sources))
        else:
            results.append(CheckResult("statistic", "unknown", "fail", "low", "Statistic entry is not an object."))

    summary = {"pass": 0, "warn": 0, "fail": 0}
    for result in results:
        summary[result.status] = summary.get(result.status, 0) + 1

    # A support_review label is reviewer input, not semantic certification. Keep
    # every labelled claim out of release-ready until an authorised release
    # process supplies evidence beyond this structural verifier.
    release_ready = (
        summary.get("fail", 0) == 0
        and all(r.confidence != "low" for r in results)
        and not any(r.item_type == "claim" and r.support_state in CLAIM_SUPPORT_STATES for r in results)
    )
    return VerificationReport(
        generated_utc=datetime.now(timezone.utc).isoformat(),
        input_path=str(path),
        release_ready=release_ready,
        summary=summary,
        results=results,
    )


def manifest_entries(manifest: dict[str, Any], key: str, results: list[CheckResult]) -> list[Any]:
    if key not in manifest:
        return []
    entries = manifest[key]
    if not isinstance(entries, list):
        results.append(
            CheckResult(
                "manifest",
                key,
                "fail",
                "low",
                f"Manifest field '{key}' must be a list.",
                [f"replace {key} with a list of objects"],
            )
        )
        return []
    return entries


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
    raw_source_ids = claim.get("source_ids")
    if not isinstance(raw_source_ids, list):
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Claim source_ids must be an explicit list.",
            ["use [] only for no-source; otherwise list non-empty source IDs"],
        )
    if any(not isinstance(source_id, str) or not source_id.strip() for source_id in raw_source_ids):
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Claim source_ids entries must be non-empty strings.",
            ["remove null, empty, or non-string source IDs"],
        )
    source_ids = [source_id.strip() for source_id in raw_source_ids]
    if len(source_ids) != len(set(source_ids)):
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Claim source_ids must not contain duplicates.",
            ["retain each source ID once"],
        )
    text = str(claim.get("text", "")).strip()

    review = claim.get("support_review")
    if not isinstance(review, dict):
        return CheckResult(
            "claim",
            claim_id,
            "warn",
            "low",
            "Source IDs may be known, but semantic claim support was not assessed by this verifier.",
            ["add support_review with a human review state"],
        )

    raw_state = review.get("state")
    if not isinstance(raw_state, str):
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Claim support_review.state must be a string.",
            ["use supported, unsupported, synthesis, inference, or no-source"],
        )
    state = raw_state.strip().casefold()
    if state not in CLAIM_SUPPORT_STATES:
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Claim support_review.state is invalid.",
            ["use supported, unsupported, synthesis, inference, or no-source"],
            support_state=state or None,
        )

    missing_review_fields = [
        field
        for field in ("reviewer", "basis", "reviewed_at")
        if not isinstance(review.get(field), str) or not review[field].strip()
    ]
    if missing_review_fields:
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Claim support review is incomplete.",
            [f"missing support_review.{field}" for field in missing_review_fields],
            support_state=state,
        )

    try:
        datetime.fromisoformat(review["reviewed_at"].replace("Z", "+00:00"))
    except ValueError:
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Claim support_review.reviewed_at must be an ISO-8601 date or datetime.",
            ["record a parseable review date"],
            support_state=state,
        )

    if state == "no-source":
        if source_ids:
            return CheckResult(
                "claim",
                claim_id,
                "fail",
                "low",
                "A no-source review state cannot list source IDs.",
                ["remove source_ids or change the review state"],
                support_state=state,
            )
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Human review recorded no source for this claim; the verifier does not promote it.",
            ["no source found", "claim remains unreleasable"],
            support_state=state,
        )

    if not source_ids:
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Claim has no source_ids for its recorded support state.",
            ["add source_ids or use no-source"],
            support_state=state,
        )

    missing = [sid for sid in source_ids if sid not in sources]
    if missing:
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Claim references unknown source IDs.",
            missing,
            support_state=state,
        )

    if state == "unsupported":
        return CheckResult(
            "claim",
            claim_id,
            "fail",
            "low",
            "Human review recorded the claim as unsupported; automated semantics are not assessed.",
            ["quarantine or revise claim"],
            support_state=state,
        )

    if len(text) < 10:
        return CheckResult("claim", claim_id, "warn", "low", "Claim text is too thin to review semantically.", ["thin claim text", "semantic support not assessed"], support_state=state)

    return CheckResult(
        "claim",
        claim_id,
        "warn",
        "low",
        f"Human review state '{state}' is recorded; automated semantics are not assessed or certified.",
        ["retain reviewer evidence and complete an authorised semantic review"],
        support_state=state,
    )


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
        "| Type | ID | Support state | Status | Confidence | Evidence | Gaps |",
        "|---|---|---|---|---|---|---|",
    ])
    for result in report.results:
        gaps = "; ".join(result.gaps)
        evidence = result.evidence.replace("|", "\\|")
        support_state = result.support_state or "not applicable"
        lines.append(f"| {result.item_type} | {result.item_id} | {support_state} | {result.status} | {result.confidence} | {evidence} | {gaps} |")
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
