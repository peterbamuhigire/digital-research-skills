"""Repo-level validator for the project kernel."""

from __future__ import annotations

import subprocess


COMMANDS = (
    ["python", "-m", "engine", "doctor"],
    ["python", "-m", "unittest", "discover", "-s", "engine\\tests"],
    ["python", "-m", "engine", "validate", "example-market-landscape"],
    ["python", "-m", "engine", "validate", "example-due-diligence-dossier"],
    ["python", "-m", "engine", "validate", "example-academic-paper"],
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
