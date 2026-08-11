from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from engine.gates import run_all_gates
from engine.output import assemble_output
from engine.scaffold import ScaffoldOptions, create_project
from scripts.seed_example_project import EXAMPLES, _complete_context, _complete_outputs, _complete_registries


class ExampleProjectSeedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="dre-example-seed-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def test_tracked_seeder_creates_all_registry_inputs_for_every_seeded_example(self) -> None:
        expected_files = {
            "tradecraft.yaml",
            "report-shapes.yaml",
            "productization-manifest.yaml",
            "calibration-log.yaml",
            "osint-tool-index.yaml",
        }

        for name, research_type, audience, family in EXAMPLES:
            with self.subTest(example=name):
                workspace = create_project(
                    ScaffoldOptions(
                        name,
                        research_type,
                        audience,
                        family,
                        self.tmp,
                    )
                )
                _complete_context(workspace, research_type, audience, family)
                _complete_registries(workspace)
                _complete_outputs(workspace, family)
                assemble_output(workspace, family)

                actual_files = {path.name for path in workspace.registry_dir.iterdir()}
                self.assertTrue(expected_files.issubset(actual_files))

                results = run_all_gates(workspace)
                blockers = [
                    finding
                    for result in results
                    for finding in result.findings
                    if finding.severity == "blocker"
                ]
                self.assertFalse(blockers, msg=f"{name}: {blockers}")


if __name__ == "__main__":
    unittest.main()
