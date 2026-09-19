"""Small, read-only validators for the Phase 1 Kaizen evidence contracts.

These checks validate shape and release boundaries only. They do not decide
whether a source semantically supports a claim; that remains a human review
responsibility under source-evaluation and source-verification.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import re
from typing import Any, Iterable


NOT_ASSESSED = "NOT_ASSESSED"
_SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")
_LOCATOR_KINDS = {"line", "page", "paragraph", "offset", "section", "uri"}
_DISPOSITIONS = {
    "durable_synthesis",
    "current_supported",
    "inference",
    "partial",
    NOT_ASSESSED,
}
_OBSERVATION_TYPES = {"mention", "citation", "referral", "conversion"}


@dataclass(frozen=True)
class ContractFinding:
    """One deterministic contract finding."""

    code: str
    status: str
    message: str
    confidence: str = "low"


def _finding(code: str, status: str, message: str, confidence: str = "low") -> ContractFinding:
    return ContractFinding(code, status, message, confidence)


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: Any) -> bool:
    return isinstance(value, list) and all(_nonempty_string(item) for item in value)


def validate_index_layer(record: Any, *, known_source_ids: Iterable[str] | None = None) -> list[ContractFinding]:
    """Validate a subject/index/interpretation evidence record.

    Missing context or an unusable locator is deliberately ``NOT_ASSESSED``:
    the record may be repaired, but it cannot support a released claim.
    Source-hash disagreement is a hard integrity blocker.
    """

    findings: list[ContractFinding] = []
    if not isinstance(record, dict):
        return [_finding("index-record-shape", "blocker", "index record must be an object")]

    for field in ("subject_unit", "representation_method", "index_version"):
        if not _nonempty_string(record.get(field)):
            findings.append(_finding(f"index-missing-{field}", "blocker", f"{field} is required"))

    context = record.get("context")
    if not isinstance(context, dict) or not context or not any(_nonempty_string(v) for v in context.values()):
        findings.append(_finding("index-missing-context", NOT_ASSESSED, "context is missing; source-to-interpretation reconstruction is unavailable"))

    blind_spots = record.get("blind_spots")
    if not isinstance(blind_spots, list) or not blind_spots:
        findings.append(_finding("index-missing-blind-spots", NOT_ASSESSED, "blind_spots must contain at least one declared limitation"))
    else:
        for position, gap in enumerate(blind_spots):
            if not isinstance(gap, dict) or not _nonempty_string(gap.get("description")):
                findings.append(_finding("index-invalid-blind-spot", "blocker", f"blind_spots[{position}] requires a description"))

    source = record.get("source")
    if not isinstance(source, dict):
        findings.append(_finding("index-missing-source", "blocker", "source envelope is required"))
        source_hash = None
        source_id = None
    else:
        source_id = source.get("source_id")
        if not _nonempty_string(source_id):
            findings.append(_finding("index-missing-source-id", "blocker", "source.source_id is required"))
        source_hash = source.get("source_hash")
        if not _nonempty_string(source_hash) or not _SHA256.fullmatch(source_hash):
            findings.append(_finding("index-invalid-source-hash", "blocker", "source.source_hash must be a SHA-256 hex digest"))
        if known_source_ids is not None and _nonempty_string(source_id) and source_id not in set(known_source_ids):
            findings.append(_finding("index-unknown-source", "blocker", f"source ID is not present in the source register: {source_id}"))

    interpretations = record.get("interpretations")
    if not isinstance(interpretations, list) or not interpretations:
        findings.append(_finding("index-missing-interpretations", "blocker", "interpretations must be a non-empty list"))
        return findings

    for position, interpretation in enumerate(interpretations):
        prefix = f"interpretations[{position}]"
        if not isinstance(interpretation, dict):
            findings.append(_finding("index-invalid-interpretation", "blocker", f"{prefix} must be an object"))
            continue
        for field in ("id", "text", "source_hash"):
            if not _nonempty_string(interpretation.get(field)):
                findings.append(_finding("index-missing-interpretation-field", "blocker", f"{prefix}.{field} is required"))
        if source_hash and interpretation.get("source_hash") != source_hash:
            findings.append(_finding("index-source-hash-mismatch", "blocker", f"{prefix}.source_hash does not match the immutable source hash"))
        if interpretation.get("source_id") != source_id:
            findings.append(_finding("index-source-link-mismatch", "blocker", f"{prefix}.source_id must link to source.source_id"))

        locator = interpretation.get("locator")
        if not isinstance(locator, dict) or not _nonempty_string(locator.get("kind")) or not _nonempty_string(locator.get("value")):
            findings.append(_finding("index-missing-locator", NOT_ASSESSED, f"{prefix} has no usable source locator"))
        elif locator["kind"].strip().casefold() not in _LOCATOR_KINDS:
            findings.append(_finding("index-unsupported-locator", NOT_ASSESSED, f"{prefix}.locator.kind is outside the supported locator vocabulary"))
    return findings


def source_hash_is_stable(before: Any, after: Any) -> bool:
    """Return whether re-indexing preserved the source hash."""

    return (
        isinstance(before, dict)
        and isinstance(after, dict)
        and isinstance(before.get("source"), dict)
        and isinstance(after.get("source"), dict)
        and before["source"].get("source_hash") == after["source"].get("source_hash")
    )


def validate_objection_response(record: Any, *, known_source_ids: Iterable[str] | None = None) -> list[ContractFinding]:
    """Validate the objection-response release gate."""

    if not isinstance(record, dict):
        return [_finding("objection-record-shape", "blocker", "objection record must be an object")]
    findings: list[ContractFinding] = []
    objection = record.get("strongest_objection")
    alternative = record.get("alternative")
    response = record.get("response")
    if not _nonempty_string(objection):
        findings.append(_finding("objection-missing", "blocker", "the strongest objection is required"))
    if not _nonempty_string(alternative):
        findings.append(_finding("alternative-missing", "blocker", "an alternative explanation or option is required"))
    if not isinstance(response, dict) or response.get("outcome") not in {"defeats", "limits", "open"}:
        findings.append(_finding("objection-response-missing", "blocker", "response.outcome must be defeats, limits, or open"))
    elif response["outcome"] == "open":
        findings.append(_finding("objection-unresolved", "conditional", "unresolved objection is preserved; confidence must be lowered", "low"))

    referenced: list[str] = []
    for value in (record.get("source_ids"), record.get("objection_source_ids"), record.get("response_source_ids")):
        if value is None:
            continue
        if not _string_list(value):
            findings.append(_finding("objection-source-list-invalid", "blocker", "source references must be non-empty string lists"))
        else:
            referenced.extend(value)
    if known_source_ids is not None:
        known = set(known_source_ids)
        for source_id in referenced:
            if source_id not in known:
                findings.append(_finding("objection-fabricated-source", "blocker", f"source reference is not in the verified source register: {source_id}"))
    if record.get("fabricated_source") is True or record.get("misreported_source") is True:
        findings.append(_finding("objection-fabricated-source", "blocker", "fabricated or misreported source claims block release"))
    return findings


def validate_ai_search_claim(record: Any, *, as_of: date | None = None) -> list[ContractFinding]:
    """Validate an AI-search claim disposition and currentness boundary."""

    if not isinstance(record, dict):
        return [_finding("ai-claim-shape", "blocker", "AI-search claim must be an object")]
    findings: list[ContractFinding] = []
    disposition = record.get("disposition")
    observation = record.get("observation_type")
    source_ids = record.get("source_ids")
    if disposition not in _DISPOSITIONS:
        findings.append(_finding("ai-invalid-disposition", "blocker", "disposition is outside the contract vocabulary"))
    if observation not in _OBSERVATION_TYPES:
        findings.append(_finding("ai-invalid-observation-type", "blocker", "mention, citation, referral, and conversion are distinct observation types"))
    if not _string_list(source_ids):
        findings.append(_finding("ai-missing-evidence", NOT_ASSESSED, "source_ids must identify the evidence behind the observation"))
    if record.get("guarantee") is True or "guarantee" in str(record.get("text", "")).casefold():
        findings.append(_finding("ai-guarantee-blocked", "blocker", "AI-search guarantees fail closed"))
    if record.get("evidence_strength") == "weak":
        findings.append(_finding("ai-weak-evidence", NOT_ASSESSED, "weak evidence cannot support a released AI-search claim"))

    if disposition == "current_supported":
        for field in ("source_scope", "accessed_at", "review_after", "limitation"):
            if not _nonempty_string(record.get(field)):
                findings.append(_finding("ai-currentness-metadata-missing", NOT_ASSESSED, f"current_supported requires {field}"))
        if as_of is not None and _nonempty_string(record.get("review_after")):
            try:
                if date.fromisoformat(record["review_after"]) < as_of:
                    findings.append(_finding("ai-currentness-stale", NOT_ASSESSED, "currentness review date has passed; quarantine the claim"))
            except ValueError:
                findings.append(_finding("ai-currentness-date-invalid", NOT_ASSESSED, "review_after must be an ISO date"))
    return findings
