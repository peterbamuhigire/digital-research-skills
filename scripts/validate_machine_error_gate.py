"""Check textual gate identifier presence, not semantic, editorial or visual quality."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "machine-error-gate-baseline.json"


def load_contract(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(contract: dict, engines: set[str] | None = None) -> list[str]:
    required_ids = contract["required_ids"]
    errors: list[str] = []
    known = {target["engine"] for target in contract["targets"]}
    if not contract["targets"]:
        return ["targets must not be empty"]
    if engines is not None and (not engines or engines - known):
        return ["engine selection must be non-empty and contain only registered engines"]
    shared = ROOT / contract["shared_reference"]
    if not shared.exists():
        errors.append(f"shared reference missing: {shared}")
        return errors

    shared_text = shared.read_text(encoding="utf-8")
    for check_id in required_ids:
        if check_id not in shared_text:
            errors.append(f"shared reference missing {check_id}: {shared}")

    for target in contract["targets"]:
        if engines is not None and target["engine"] not in engines:
            continue
        path = Path(target["path"])
        if not path.is_file():
            errors.append(f"{target['engine']}: target missing: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        missing = [check_id for check_id in required_ids if check_id not in text]
        if missing:
            errors.append(f"{target['engine']}: missing {', '.join(missing)}: {path}")

    overlay_fixture_value = contract.get("overlay_pressure_fixture")
    overlay_ids = contract.get("overlay_ids", [])
    if overlay_fixture_value and overlay_ids:
        overlay_fixture = ROOT / overlay_fixture_value
        if not overlay_fixture.exists():
            errors.append(f"overlay pressure fixture missing: {overlay_fixture}")
        else:
            fixture_text = overlay_fixture.read_text(encoding="utf-8")
            for check_id in overlay_ids:
                if f"{check_id}:" not in fixture_text:
                    errors.append(f"overlay pressure fixture missing {check_id}: {overlay_fixture}")
            if "functional exception" not in fixture_text.lower():
                errors.append(f"overlay pressure fixture missing functional exception: {overlay_fixture}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--engine", action="append", help="Select textual gate targets only; repeat for each engine. Omit to require all textual targets. Visual hard-ban adapters have a separate all-visual integration gate.")
    args = parser.parse_args()
    contract = load_contract(args.fixture)
    selected = set(args.engine) if args.engine else None
    errors = validate(contract, selected)
    if errors:
        print("MACHINE_ERROR_GATE: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("MACHINE_ERROR_GATE: PASS (identifier presence only)")
    print("- semantic, editorial and visual verification: NOT ASSESSED")
    print("- visual hard-ban adapters: separate all-visual integration gate; not checked by this command")
    print(f"- checks: {', '.join(contract['required_ids'])}")
    print(f"- engines: {len(selected) if selected is not None else len(contract['targets'])}")
    print("- textual scope: " + (", ".join(sorted(selected)) if selected is not None else "all registered textual targets"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
