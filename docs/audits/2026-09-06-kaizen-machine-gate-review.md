# Independent review: machine-error gate scope

Current disposition: CLOSED through the user's explicit scope clarification
and the verified documentation/output patch below. The original findings and
pre-change reproduction are retained as historical evidence.

Original verdict: correct the live visual test's scope handling. The main validator's
explicit-selection logic passed the focused negative probes; its default still
requires the political target. The CLI result does not establish visual-adapter
hard-ban coverage. Evidence: [validator](../../scripts/validate_machine_error_gate.py#L19),
[live visual test](../../tests/test_machine_error_gate.py#L58), and reviewer
execution below (synthesis).

Scope: current changes to the machine-error validator, its test module, and
`tests/fixtures/machine-error-gate-baseline.json`. Read the root agent/router
instructions and relevant local Kaizen, machine-error, and anti-slop guidance;
retained the source-evaluation and evidence instructions already read in this
session. Source-currency work was not inspected or changed. Only this report
was written.

## Medium: explicit live-test selection does not constrain visual adapters

The machine-adapter test honours `SKILL_ENGINE_TARGETS`, but
`test_visual_hard_bans_are_declared_in_visual_adapters` always iterates every
visual target. With live tests opted in and only `digital-research` selected,
an unavailable engineering visual adapter still fails the suite. This prevents
an isolated selected-engine run on a host lacking unselected checkouts.
Evidence: [selection handling](../../tests/test_machine_error_gate.py#L19),
[unfiltered visual loop](../../tests/test_machine_error_gate.py#L61), and
[scope reproduction](#visual-scope-reproduction) (synthesis).

The baseline gives visual adapters distinct labels, such as
`engineering-visual`, rather than the main target's `engineering` ID. Filtering
those labels directly against selected main IDs would silently drop applicable
checks. Add an explicit owning-engine mapping and use it consistently, with
local tests proving that selected missing visual adapters fail, unselected
adapters are not required, and the default still checks all. This is the
recommended repair (inference), based on the
[fixture labels](../../tests/fixtures/machine-error-gate-baseline.json#L7).

## Coverage limitation: CLI success excludes declared visual hard bans

`validate()` never reads `visual_targets` or `visual_hard_ban_phrases`. A
synthetic missing visual adapter therefore leaves its result unchanged. The
new portable test only exercises main-target identifier presence and shared
pressure-fixture checks; the separate visual test is live-only. Evidence:
[validator](../../scripts/validate_machine_error_gate.py),
[portable test](../../tests/test_machine_error_gate.py#L68), and the reproduction
below (synthesis).

This validator omission predates the patch. The live-only skip is intentional,
not itself a defect. However, neither a local-suite pass nor the CLI's scope
summary may be cited as proof that the declared visual adapters were checked.
Either bring scoped visual validation into the common routine with portable
negative fixtures, or explicitly report that coverage as `NOT_ASSESSED`.
Actual semantic/visual quality remains outside this textual checker in either
case (inference).

## Reviewer execution

Executed only the scoped test module:

```powershell
python -X utf8 -m unittest discover -s tests -p test_machine_error_gate.py -v
```

Observed summary, reproduced verbatim:

```text
Ran 5 tests in 0.022s

OK (skipped=2)
```

The skipped tests were the installed-portfolio and installed-visual checks,
as declared in the [test module](../../tests/test_machine_error_gate.py).

Selection probe: copied the baseline in memory, gave every main target a
synthetic local path, and made only the political target's `is_file()` false.
Mocked other file checks/reads with synthetic required-ID text and the pressure
fixture's required exception marker. Called `validate()` with default scope,
all baseline IDs except political, an unknown ID, an empty set, and political
alone. Also called `main()` with mocked contract loading and explicit argv.
Observed outcomes:

| Probe | Observed result |
| --- | --- |
| Default scope | Rejected the missing political target |
| Explicit baseline IDs excluding political | No findings |
| Unknown or empty selection | Selection error |
| Political explicitly selected | Rejected the missing political target |
| Default CLI | Failed |
| Explicit selected CLI | Passed and listed the selected IDs |

These are synthetic local control tests, not claims about installed portfolio
coverage. No political checkout was read or exempted by default.

### Visual scope reproduction

Run from this repository. This uses only existing local shared text plus an
in-memory fixture override; the absent path is a synthetic fixture name.

```python
import importlib.util, json, os
from pathlib import Path
from unittest.mock import patch
from scripts import validate_machine_error_gate as gate
contract = gate.load_contract(gate.DEFAULT_FIXTURE)
shared = gate.ROOT / contract['shared_reference']
for target in contract['targets']:
    target['path'] = str(shared)
contract['visual_targets'] = [{'engine': 'engineering-visual',
    'path': str(gate.ROOT / 'synthetic-review/absent-visual.md')}]
print('validator findings:', gate.validate(contract, {'digital-research'}))
with patch.dict(os.environ, {'SKILL_ENGINE_LIVE_TESTS': '1',
                            'SKILL_ENGINE_TARGETS': 'digital-research'}):
    spec = importlib.util.spec_from_file_location(
        'review_machine_tests', gate.ROOT / 'tests/test_machine_error_gate.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    original_read = Path.read_text
    def read(path, *args, **kwargs):
        if path == module.FIXTURE:
            return json.dumps(contract)
        return original_read(path, *args, **kwargs)
    with patch.object(Path, 'read_text', read):
        case = module.MachineErrorGateCoverageTests()
        case.test_shared_reference_and_all_engine_adapters_expose_every_check()
        case.test_visual_hard_bans_are_declared_in_visual_adapters()
```

The reviewer observed no validator findings for a missing visual adapter.
With the same missing-visual setup, the selected machine-adapter test passed,
then the visual test raised an assertion on the excluded engineering adapter.
The reproduction ends with that expected assertion failure.

## Evidence limits and snapshot

No full installed-portfolio run was performed. Opt-in tests were exercised
only with the described local fixture override. No actual engine coverage,
semantic correctness, visual render, or external currentness is certified.
Currentness preflight: `NO_TIME_SENSITIVE_CLAIMS`; findings are context-bound
to the local code and test observations. Recheck after changes.

Baseline observed with `git rev-parse HEAD`:
`0ec5084c0461d068d5a4699ed16236a123ae770f`.
Reviewed hashes observed with `Get-FileHash`:

```text
scripts/validate_machine_error_gate.py
1631D4546D232D21FA8387B2054BF87211F92C0FB85FF43B218A3D349CE16B50
tests/test_machine_error_gate.py
C34E2DE0CEAFC815D8898F2EFCC12E60745F72595B9A7E0B5854E37A293063C0
tests/fixtures/machine-error-gate-baseline.json
5A099A3ED0A5FCA5E18E116D40DE0BDECEAFC42B39134566C4783A4DAC46622F
```

## Scope clarification and closure

The user chose the following contract: `--engine` and `SKILL_ENGINE_TARGETS`
select textual gate targets only. The visual hard-ban adapter test is a
separate, explicitly all-visual integration gate. It intentionally checks all
declared visual adapters when live tests are enabled. Accordingly, the original
excluded-visual reproduction describes that separate gate's expected behaviour;
filtering it by textual selection is not required under the clarified contract.

The test is now named
`test_all_visual_adapters_declare_hard_bans_integration`, and its module
documentation and skip reason explain the independent scope. CLI help makes
textual-only selection explicit. CLI success identifies identifier presence
only and marks semantic, editorial and visual verification `NOT_ASSESSED`.
Evidence: [test module](../../tests/test_machine_error_gate.py),
[CLI](../../scripts/validate_machine_error_gate.py), and the execution below
(synthesis).

The scope finding and coverage-reporting concern are closed by this authorised
clarification. The validator's selection algorithm and fixture were not changed;
default invocation still requires all registered textual targets. No owning-
engine mapping or broader validation redesign was introduced. This patch was
implemented and checked by the reviewing agent, not independently re-reviewed
by a different agent.

### Closure execution evidence

Ran the focused module in a child Python process with these environment values:

```python
import os, unittest
os.environ['SKILL_ENGINE_LIVE_TESTS'] = '1'
os.environ['SKILL_ENGINE_TARGETS'] = (
    'srs,business-plan,website-copy,social-media,linux,proposal,'
    'engineering,accounting,design,digital-research,windows'
)
suite = unittest.defaultTestLoader.discover(
    'tests', pattern='test_machine_error_gate.py')
raise SystemExit(not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful())
```

Observed summary, reproduced verbatim:

```text
Ran 5 tests in 0.033s

OK
```

This included the explicitly selected textual integration test and the renamed
all-visual hard-ban declaration test. It establishes local textual declarations,
not rendered visual quality or editorial effectiveness.

Executed the CLI with the same explicit selection:

```powershell
python -X utf8 scripts/validate_machine_error_gate.py --engine srs --engine business-plan --engine website-copy --engine social-media --engine linux --engine proposal --engine engineering --engine accounting --engine design --engine digital-research --engine windows
```

Observed output, reproduced verbatim:

```text
MACHINE_ERROR_GATE: PASS (identifier presence only)
- semantic, editorial and visual verification: NOT ASSESSED
- visual hard-ban adapters: separate all-visual integration gate; not checked by this command
- checks: ME1, ME2, ME3, ME4, ME5, ME6, ME7, AS1, AS2, AS3, AS4, AS5, AS6, AS7
- engines: 11
- textual scope: accounting, business-plan, design, digital-research, engineering, linux, proposal, social-media, srs, website-copy, windows
```

CLI help was inspected and the scoped `git diff --check` reported no whitespace
errors. Only the validator's explanatory text, the test's naming/documentation,
and this report were edited. The other worker's source-currency files were not
edited or tested as part of this task.

Post-patch hashes observed with `Get-FileHash`:

```text
scripts/validate_machine_error_gate.py
A61052C8B32FD53DAAC2FA8E5A681769F30F0E5E80CE1970F3673EFD4304A450
tests/test_machine_error_gate.py
6AC41038D4843F15F165B3D154CF3BEA2F95DF524C82B77637C55E81591DA613
```
