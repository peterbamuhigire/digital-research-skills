"""Repo-level validator for the project kernel."""

from __future__ import annotations

import subprocess
import sys


COMMANDS = (
    [sys.executable, "-X", "utf8", "scripts/skill_contract_validator.py", "--baseline", "tests/skill-engine/quality-baseline.json"],
    [sys.executable, "-X", "utf8", "scripts/routing_smoke_test.py"],
    [sys.executable, "-m", "engine", "doctor"],
    [sys.executable, "-m", "unittest", "discover", "-s", "engine/tests"],
)


def main() -> int:
    for command in COMMANDS:
        print("Running:", " ".join(command))
        result = subprocess.run(command, check=False)
        if result.returncode != 0:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
