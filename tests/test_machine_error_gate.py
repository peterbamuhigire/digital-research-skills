import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "machine-error-gate-baseline.json"
PRESSURE_FIXTURE = ROOT / "tests" / "fixtures" / "machine-error-pressure-fixture.md"


class MachineErrorGateCoverageTests(unittest.TestCase):
    def test_shared_reference_and_all_engine_adapters_expose_every_check(self):
        contract = json.loads(FIXTURE.read_text(encoding="utf-8"))
        required_ids = contract["required_ids"]
        shared_reference = ROOT / contract["shared_reference"]
        self.assertTrue(shared_reference.exists(), shared_reference)
        shared_text = shared_reference.read_text(encoding="utf-8")
        for check_id in required_ids:
            self.assertIn(check_id, shared_text)

        missing = []
        for target in contract["targets"]:
            path = Path(target["path"])
            if not path.exists():
                missing.append(f"{target['engine']}: missing {path}")
                continue
            text = path.read_text(encoding="utf-8")
            for check_id in required_ids:
                if check_id not in text:
                    missing.append(f"{target['engine']}: missing {check_id}")
        self.assertEqual([], missing, "\n".join(missing))

    def test_pressure_fixture_covers_each_machine_error_and_exceptions(self):
        text = PRESSURE_FIXTURE.read_text(encoding="utf-8")
        for check_id in json.loads(FIXTURE.read_text(encoding="utf-8"))["required_ids"]:
            self.assertIn(f"{check_id}:", text)
        self.assertIn("functional exception", text.lower())


if __name__ == "__main__":
    unittest.main()
