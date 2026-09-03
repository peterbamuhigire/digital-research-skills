"""Check that every registered engine exposes the shared machine-error gate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "machine-error-gate-baseline.json"


def load_contract(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(contract: dict) -> list[str]:
    required_ids = contract["required_ids"]
    errors: list[str] = []
    shared = ROOT / contract["shared_reference"]
    if not shared.exists():
        errors.append(f"shared reference missing: {shared}")
        return errors

    shared_text = shared.read_text(encoding="utf-8")
    for check_id in required_ids:
        if check_id not in shared_text:
            errors.append(f"shared reference missing {check_id}: {shared}")

    for target in contract["targets"]:
        path = Path(target["path"])
        if not path.exists():
            errors.append(f"{target['engine']}: target missing: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        missing = [check_id for check_id in required_ids if check_id not in text]
        if missing:
            errors.append(f"{target['engine']}: missing {', '.join(missing)}: {path}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    args = parser.parse_args()
    errors = validate(load_contract(args.fixture))
    if errors:
        print("MACHINE_ERROR_GATE: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("MACHINE_ERROR_GATE: PASS")
    print(f"- checks: {', '.join(load_contract(args.fixture)['required_ids'])}")
    print(f"- engines: {len(load_contract(args.fixture)['targets'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
