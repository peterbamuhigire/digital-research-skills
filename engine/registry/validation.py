"""Schema-aware registry validation helpers."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .schemas import RegistrySchema


PLACEHOLDER_VALUES = {"", "TODO", "TBD", "N/A", "UNKNOWN", "NONE", "NULL"}


@dataclass(frozen=True)
class RegistryIssue:
    path: Path
    message: str


def load_registry(path: Path, root_key: str) -> tuple[list[dict[str, Any]], list[RegistryIssue]]:
    if not path.exists():
        return [], [RegistryIssue(path, "registry file missing")]
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        return [], [RegistryIssue(path, f"invalid YAML: {exc}")]
    if not isinstance(data, dict):
        return [], [RegistryIssue(path, "registry must be a YAML mapping")]
    if root_key not in data:
        return [], [RegistryIssue(path, f"registry root key missing: {root_key}")]
    rows = data[root_key]
    if rows is None:
        return [], []
    if not isinstance(rows, list):
        return [], [RegistryIssue(path, f"registry root `{root_key}` must be a list")]
    invalid = [index for index, row in enumerate(rows, start=1) if not isinstance(row, dict)]
    issues = [RegistryIssue(path, f"row {index} must be a mapping") for index in invalid]
    return [row for row in rows if isinstance(row, dict)], issues


def validate_rows(path: Path, schema: RegistrySchema) -> tuple[list[dict[str, Any]], list[RegistryIssue]]:
    rows, issues = load_registry(path, schema.root_key)
    for index, row in enumerate(rows, start=1):
        row_id = str(row.get("id", f"row {index}"))
        for field in schema.required_fields:
            if field not in row:
                issues.append(RegistryIssue(path, f"{row_id}: missing required field `{field}`"))
        for field in schema.non_placeholder_fields:
            if field in row and is_placeholder(row[field]):
                issues.append(RegistryIssue(path, f"{row_id}: placeholder value in `{field}`"))
        for field, allowed in schema.allowed_values.items():
            if field in row and not is_placeholder(row[field]) and str(row[field]).lower() not in allowed:
                allowed_text = ", ".join(allowed)
                issues.append(RegistryIssue(path, f"{row_id}: `{field}` must be one of: {allowed_text}"))
    return rows, issues


def registry_ids(rows: list[dict[str, Any]]) -> set[str]:
    return {str(row["id"]) for row in rows if "id" in row and not is_placeholder(row["id"])}


def as_id_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if not is_placeholder(item)]
    if isinstance(value, str):
        if "," in value:
            return [item.strip() for item in value.split(",") if item.strip()]
        return [] if is_placeholder(value) else [value]
    return [str(value)]


def has_items(path: Path, root_key: str) -> bool:
    rows, _ = load_registry(path, root_key)
    return bool(rows)


def is_placeholder(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip().upper() in PLACEHOLDER_VALUES
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0
    return False
