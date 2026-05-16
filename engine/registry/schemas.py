"""Registry schema definitions for project evidence contracts."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class RegistrySchema:
    filename: str
    root_key: str
    required_fields: tuple[str, ...]
    allowed_values: dict[str, tuple[str, ...]] = field(default_factory=dict)
    non_placeholder_fields: tuple[str, ...] = ()


SCHEMAS: tuple[RegistrySchema, ...] = (
    RegistrySchema(
        "sources.yaml",
        "sources",
        ("id", "title", "ref", "tier", "accessed", "verification", "confidence"),
        allowed_values={"tier": ("1", "2", "3", "4", "5"), "confidence": ("high", "medium", "low")},
        non_placeholder_fields=("id", "title", "ref", "tier", "accessed", "verification", "confidence"),
    ),
    RegistrySchema(
        "claims.yaml",
        "claims",
        ("id", "claim", "source_ids", "confidence", "status"),
        allowed_values={
            "confidence": ("high", "medium", "low"),
            "status": ("untested", "supported", "contested", "contradicted", "synthesis", "inference", "retired"),
        },
        non_placeholder_fields=("id", "claim", "source_ids", "confidence", "status"),
    ),
    RegistrySchema(
        "quotes.yaml",
        "quotes",
        ("id", "quote", "source_id", "locator", "verified"),
        non_placeholder_fields=("id", "quote", "source_id", "locator", "verified"),
    ),
    RegistrySchema(
        "synthesis-map.yaml",
        "synthesis_map",
        ("id", "synthesis", "claim_ids", "status"),
        allowed_values={"status": ("draft", "verified", "rejected", "released")},
        non_placeholder_fields=("id", "synthesis", "claim_ids", "status"),
    ),
    RegistrySchema(
        "tradecraft.yaml",
        "tradecraft_records",
        ("id", "judgment", "hypothesis_set", "evidence", "biases_considered", "confidence_judgment", "confidence_source", "indicators", "status"),
        allowed_values={"confidence_judgment": ("high", "medium", "low"), "confidence_source": ("high", "medium", "low")},
        non_placeholder_fields=("id", "judgment", "hypothesis_set", "evidence", "biases_considered", "confidence_judgment", "confidence_source", "indicators", "status"),
    ),
    RegistrySchema(
        "report-shapes.yaml",
        "report_shapes",
        ("id", "output_family", "shape", "audience", "action", "citation_regime", "verification_status", "status"),
        non_placeholder_fields=("id", "output_family", "shape", "audience", "action", "citation_regime", "verification_status", "status"),
    ),
    RegistrySchema(
        "productization-manifest.yaml",
        "productization_assets",
        ("id", "asset", "audience", "reuse_status", "provenance", "sensitivity", "commercial_claim_bounds", "status"),
        non_placeholder_fields=("id", "asset", "audience", "reuse_status", "provenance", "sensitivity", "commercial_claim_bounds", "status"),
    ),
    RegistrySchema(
        "calibration-log.yaml",
        "forecasts",
        ("id", "question", "horizon", "probability", "resolution_source", "source_confidence", "status"),
        allowed_values={"source_confidence": ("high", "medium", "low"), "status": ("open", "updated", "resolved", "retired")},
        non_placeholder_fields=("id", "question", "horizon", "probability", "resolution_source", "source_confidence", "status"),
    ),
    RegistrySchema(
        "osint-tool-index.yaml",
        "osint_tools",
        (
            "id",
            "name",
            "url",
            "category",
            "geography",
            "source_ids",
            "access_model",
            "legal_notes",
            "verification",
            "confidence",
            "status",
            "last_checked",
        ),
        allowed_values={
            "access_model": ("unverified", "free", "freemium", "paid", "account_required", "restricted"),
            "confidence": ("high", "medium", "low"),
            "status": ("candidate", "verified", "rejected", "retired"),
        },
        non_placeholder_fields=(
            "id",
            "name",
            "url",
            "category",
            "geography",
            "source_ids",
            "access_model",
            "legal_notes",
            "verification",
            "confidence",
            "status",
            "last_checked",
        ),
    ),
    RegistrySchema("sign-offs.yaml", "sign_offs", ("id", "gate", "signed_by", "date", "status")),
    RegistrySchema("waivers.yaml", "waivers", ("id", "gate", "reason", "approved_by", "expires")),
    RegistrySchema("release-ledger.yaml", "releases", ("id", "version", "date", "artifacts", "validation_report")),
)


def schema_for(filename: str) -> RegistrySchema:
    for schema in SCHEMAS:
        if schema.filename == filename:
            return schema
    raise KeyError(filename)
