from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from engine.gates import run_all_gates
from engine.pack import build_pack
from engine.registry import sync_workspace
from engine.scaffold import ScaffoldOptions, create_project
from engine.workspace import Workspace


class KernelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="dre-kernel-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def test_scaffold_loads_as_workspace(self) -> None:
        workspace = create_project(ScaffoldOptions("Unit Project", "market", "internal", "standard", self.tmp))
        loaded = Workspace.load(workspace.root)
        self.assertEqual(loaded.project_id, "unit-project")

    def test_sync_repairs_missing_registry(self) -> None:
        workspace = create_project(ScaffoldOptions("Sync Project", "market", "internal", "standard", self.tmp))
        workspace.registry_path("claims.yaml").unlink()
        result = sync_workspace(workspace)
        self.assertEqual(len(result.created), 1)
        self.assertTrue(workspace.registry_path("claims.yaml").exists())

    def test_fresh_project_has_validation_blockers(self) -> None:
        workspace = create_project(ScaffoldOptions("Gate Project", "market", "internal", "standard", self.tmp))
        results = run_all_gates(workspace)
        blockers = [finding for result in results for finding in result.findings if finding.severity == "blocker"]
        self.assertGreater(len(blockers), 0)

    def test_pack_writes_zip(self) -> None:
        workspace = create_project(ScaffoldOptions("Pack Project", "market", "internal", "standard", self.tmp))
        result = build_pack(workspace, "export/test.zip")
        self.assertTrue(result.path.exists())
        self.assertGreater(result.files, 0)


if __name__ == "__main__":
    unittest.main()
