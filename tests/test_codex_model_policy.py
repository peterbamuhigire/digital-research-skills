from __future__ import annotations

import importlib.util
import json
import shutil
from pathlib import Path
from typing import Callable

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "ensure_model_policy", ROOT / ".codex" / "ensure_model_policy.py"
)
assert SPEC and SPEC.loader
policy_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(policy_module)


def make_codex_home(tmp_path: Path) -> Path:
    policy, policy_text, templates = policy_module.load_policy(ROOT)
    home = tmp_path / "codex-home"
    home.mkdir()
    files = policy_module.expected(home, policy, policy_text, templates)
    for path, data in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.parent == home / "agents":
            data = data.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
        path.write_bytes(data)
    return home


def make_policy_root(tmp_path: Path) -> Path:
    root = tmp_path / "engine"
    codex = root / ".codex"
    codex.mkdir(parents=True)
    for name in ("model-policy.json", "model-policy.md"):
        shutil.copyfile(ROOT / ".codex" / name, codex / name)
    shutil.copytree(ROOT / ".codex" / "agents", codex / "agents")
    return root


def test_check_accepts_crlf_equivalent_role_templates_without_writing(tmp_path: Path) -> None:
    home = make_codex_home(tmp_path)
    role_paths = [
        home / "agents" / f"{role}.toml"
        for role in policy_module.load_policy(ROOT)[0]["roles"]
    ]
    before = {path: path.read_bytes() for path in role_paths}

    policy_module.check(home, ROOT)

    assert {path: path.read_bytes() for path in role_paths} == before


def test_stale_astra_default_reports_drift_without_writing_fixture(tmp_path: Path) -> None:
    home = make_codex_home(tmp_path)
    config = home / "config.toml"
    config.write_bytes(
        config.read_bytes().replace(b'model = "gpt-6-luna"', b'model = "gpt-6-astra"', 1)
    )
    before = {path: path.read_bytes() for path in home.rglob("*") if path.is_file()}

    with pytest.raises(policy_module.PolicyDrift, match="root model policy drift"):
        policy_module.check(home, ROOT)

    assert {path: path.read_bytes() for path in home.rglob("*") if path.is_file()} == before


def test_medium_root_reasoning_effort_reports_drift_without_writing(tmp_path: Path) -> None:
    home = make_codex_home(tmp_path)
    config = home / "config.toml"
    config.write_bytes(
        config.read_bytes().replace(
            b'model_reasoning_effort = "high"',
            b'model_reasoning_effort = "medium"',
            1,
        )
    )
    before = {path: path.read_bytes() for path in home.rglob("*") if path.is_file()}

    with pytest.raises(
        policy_module.PolicyDrift, match="root reasoning effort policy drift"
    ):
        policy_module.check(home, ROOT)

    assert {path: path.read_bytes() for path in home.rglob("*") if path.is_file()} == before


def test_apply_sets_high_root_effort_and_preserves_unrelated_config(tmp_path: Path) -> None:
    home = make_codex_home(tmp_path)
    config = home / "config.toml"
    config.write_bytes(
        b'approval_policy = "never"\n'
        + config.read_bytes().replace(
            b'model_reasoning_effort = "high"',
            b'model_reasoning_effort = "medium"',
            1,
        )
    )

    policy_module.apply(home, ROOT)
    after = policy_module.parse_config(config)

    assert after["model_reasoning_effort"] == "high"
    assert after["approval_policy"] == "never"


def test_check_rejects_semantic_model_drift_in_crlf_role(tmp_path: Path) -> None:
    home = make_codex_home(tmp_path)
    role = home / "agents" / "default.toml"
    role.write_bytes(
        role.read_bytes().replace(b'model = "gpt-6-luna"', b'model = "gpt-6-astra"', 1)
    )

    with pytest.raises(policy_module.PolicyDrift, match="role template drift: default"):
        policy_module.check(home, ROOT)


@pytest.mark.parametrize(
    ("mutate", "message"),
    [
        (lambda p: p.pop("root_model"), "root_model/review_model must be non-empty"),
        (lambda p: p.update(reasoning_effort="minimal"), "reasoning_effort must be high"),
        (lambda p: p.update(execution_model="gpt-5.6-luna"), "must pin root, review, and execution"),
        (lambda p: p["roles"].append("admin"), "roles must be the six supported roles"),
    ],
    ids=["missing-model", "unsupported-effort", "forbidden-model-family", "restricted-role"],
)
def test_shipped_policy_rejects_unsupported_model_contracts(
    tmp_path: Path, mutate: Callable[[dict], None], message: str
) -> None:
    root = make_policy_root(tmp_path)
    path = root / ".codex" / "model-policy.json"
    policy = json.loads(path.read_text(encoding="utf-8"))
    mutate(policy)
    path.write_text(json.dumps(policy), encoding="utf-8")

    with pytest.raises(policy_module.PolicyError, match=message):
        policy_module.load_policy(root)
