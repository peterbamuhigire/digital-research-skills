"""Minimal registry schema definitions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RegistrySchema:
    filename: str
    root_key: str
    required_fields: tuple[str, ...]


SCHEMAS: tuple[RegistrySchema, ...] = (
    RegistrySchema("sources.yaml", "sources", ("id", "title", "ref", "tier", "accessed", "verification", "confidence")),
    RegistrySchema("claims.yaml", "claims", ("id", "claim", "source_ids", "confidence", "status")),
    RegistrySchema("quotes.yaml", "quotes", ("id", "quote", "source_id", "locator", "verified")),
    RegistrySchema("synthesis-map.yaml", "synthesis_map", ("id", "synthesis", "claim_ids", "status")),
    RegistrySchema("sign-offs.yaml", "sign_offs", ("id", "gate", "signed_by", "date", "status")),
    RegistrySchema("waivers.yaml", "waivers", ("id", "gate", "reason", "approved_by", "expires")),
    RegistrySchema("release-ledger.yaml", "releases", ("id", "version", "date", "artifacts", "validation_report")),
)


def schema_for(filename: str) -> RegistrySchema:
    for schema in SCHEMAS:
        if schema.filename == filename:
            return schema
    raise KeyError(filename)
