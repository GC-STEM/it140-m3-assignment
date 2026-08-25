"""Validate the intentional starter state of the Module Three assignment."""

from __future__ import annotations

import ast
import sys
from pathlib import Path
import xml.etree.ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = REPO_ROOT / "src/paycheck_calculator.py"
TEST_PATH = REPO_ROOT / "tests/test_paycheck_calculator.py"
PSEUDOCODE_PATH = REPO_ROOT / "design/paycheck_calculator.pseudo"
DRAWIO_PATH = REPO_ROOT / "design/paycheck_calculator.drawio"
SDW_PATH = REPO_ROOT / "paycheck_calculator_sdw.md"

EXPECTED_TEST_CASES = {
    "test_regular_hours": (20, 400),
    "test_boundary_40_hours": (40, 800),
    "test_first_overtime_hour": (41, 830),
    "test_assignment_example": (60, 1400),
}

SOURCE_TODO_MARKERS = (
    "TODO: Replace with a one-line summary of the optional program",
    "TODO: Replace with the major input, including its type and source.",
    "TODO: Replace with a brief description of the major processing.",
    "TODO: Replace with the major output, including its destination.",
    "TODO: Replace with an original hours-worked input example.",
    "TODO: Replace with the resulting paycheck output for your example.",
    "TODO: Replace with code to obtain hours worked in a numeric form.",
    "TODO: Replace with decision branching and processing from your design.",
    "TODO: Replace with code to display the calculated weekly paycheck.",
)

PSEUDOCODE_TODO_MARKERS = (
    "TODO: Obtain the required program input.",
    "IF TODO: Replace with the decision condition",
    "TODO: Show the processing steps for this decision path.",
    "TODO: Show the processing steps for the other decision path.",
    "TODO: Output the calculated weekly paycheck.",
)

SDW_REQUIRED_MARKERS = (
    "# Software Development Worksheet (SDW)",
    "## How to Use This Worksheet",
    "# Analyze Phase",
    "## 7. Analyze Checkpoint",
    "# Design Phase",
    "## 12. Requirements-to-Design Traceability",
    "## 16. Ready to Submit",
    "# Optional Construct and Test Notes",
)

EXPECTED_DIAGRAM_PAGES = {
    "Paycheck Calculator",
    "README",
    "Symbols",
    "Snippets",
    "References",
}


class StarterChecks:
    """Collect starter validation failures."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        """Record a failing starter check."""
        self.errors.append(message)

    def finish(self) -> None:
        """Print results and exit nonzero when starter checks fail."""
        if not self.errors:
            print("PASS: Course starter state is intentionally incomplete.")
            print("PASS: Graded design templates are intact.")
            print("PASS: Optional SDW scaffolding is intact.")
            print("PASS: Optional Python practice scaffolding is intact.")
            print("PASS: Optional acceptance-test definitions are intact.")
            return

        print("Course starter checks failed:", file=sys.stderr)
        for error in self.errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def is_docstring_statement(node: ast.stmt) -> bool:
    """Return True if a statement is a string-expression docstring."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )


def check_source(checks: StarterChecks) -> None:
    """Verify the optional source stays a valid, incomplete starter."""
    text = SOURCE_PATH.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text, filename=str(SOURCE_PATH))
    except SyntaxError as exc:
        checks.error(f"Optional starter source is not valid Python: {exc}")
        return

    for marker in SOURCE_TODO_MARKERS:
        if marker not in text:
            checks.error(f"Optional source is missing marker: {marker!r}")

    # Guard against accidental M2 name/age wording in the M3 practice starter.
    stale_markers = ("name-input", "age-input", "name_age", "birth year")
    for marker in stale_markers:
        if marker.lower() in text.lower():
            checks.error(
                "Optional source contains stale Module Two wording: "
                f"{marker!r}"
            )

    expected_constants = {
        "REGULAR_RATE": 20,
        "OVERTIME_RATE": 30,
        "REGULAR_HOURS_LIMIT": 40,
    }
    found_constants: dict[str, object] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in expected_constants:
                try:
                    found_constants[target.id] = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    found_constants[target.id] = None

    for name, expected in expected_constants.items():
        if found_constants.get(name) != expected:
            checks.error(
                f"Optional source constant {name} must remain {expected}."
            )

    main_functions = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "main"
    ]
    if len(main_functions) != 1:
        checks.error(
            "Optional starter must contain exactly one main() function."
        )
    else:
        body = main_functions[0].body
        if len(body) != 1 or not is_docstring_statement(body[0]):
            checks.error(
                "Optional starter main() must remain intentionally incomplete; "
                "only its docstring should be executable."
            )

    guards = [
        node
        for node in tree.body
        if isinstance(node, ast.If)
        and "__name__" in ast.unparse(node.test)
        and "__main__" in ast.unparse(node.test)
    ]
    if len(guards) != 1:
        checks.error("Optional starter must contain one __main__ guard.")
    else:
        calls_main = any(
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id == "main"
            for node in guards[0].body
        )
        if not calls_main:
            checks.error("The __main__ guard must call main().")


def check_pseudocode(checks: StarterChecks) -> None:
    """Verify graded pseudocode template markers remain intact."""
    text = PSEUDOCODE_PATH.read_text(encoding="utf-8")
    if "BEGIN paycheck_calculator" not in text:
        checks.error("Pseudocode starter must keep BEGIN paycheck_calculator.")
    if "END paycheck_calculator" not in text:
        checks.error("Pseudocode starter must keep END paycheck_calculator.")

    for marker in PSEUDOCODE_TODO_MARKERS:
        if marker not in text:
            checks.error(f"Pseudocode starter is missing marker: {marker!r}")


def check_drawio(checks: StarterChecks) -> None:
    """Verify starter Draw.io template keeps its reference pages."""
    try:
        root = ET.parse(DRAWIO_PATH).getroot()
    except (OSError, ET.ParseError) as exc:
        checks.error(f"Draw.io starter is not valid XML: {exc}")
        return

    pages = {
        node.attrib.get("name", "")
        for node in root.iter()
        if node.tag.rsplit("}", maxsplit=1)[-1] == "diagram"
    }

    missing = sorted(EXPECTED_DIAGRAM_PAGES - pages)
    if missing:
        checks.error(
            "Draw.io starter is missing template page(s): " + ", ".join(missing)
        )


def check_sdw(checks: StarterChecks) -> None:
    """Verify the optional SDW keeps its guided Analyze/Design structure."""
    text = SDW_PATH.read_text(encoding="utf-8")
    for marker in SDW_REQUIRED_MARKERS:
        if marker not in text:
            checks.error(f"SDW starter is missing section: {marker!r}")

    if "TODO:" not in text:
        checks.error("SDW starter should remain intentionally incomplete.")


def check_tests(checks: StarterChecks) -> None:
    """Verify optional acceptance-test suite still has four cases."""
    text = TEST_PATH.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text, filename=str(TEST_PATH))
    except SyntaxError as exc:
        checks.error(f"Acceptance-test file is not valid Python: {exc}")
        return

    test_class = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.ClassDef)
            and node.name == "PaycheckCalculatorAcceptanceTests"
        ),
        None,
    )
    if test_class is None:
        checks.error(
            "Acceptance-test class PaycheckCalculatorAcceptanceTests missing."
        )
        return

    test_functions = {
        node.name: node
        for node in test_class.body
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    }

    actual = set(test_functions)
    expected = set(EXPECTED_TEST_CASES)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        if missing:
            checks.error(f"Acceptance tests are missing: {', '.join(missing)}")
        if extra:
            checks.error(
                f"Unexpected acceptance tests found: {', '.join(extra)}"
            )

    for test_name, expected_case in EXPECTED_TEST_CASES.items():
        function = test_functions.get(test_name)
        if function is None:
            continue

        found = False
        for node in ast.walk(function):
            if not isinstance(node, ast.Call):
                continue
            if not isinstance(node.func, ast.Attribute):
                continue
            if node.func.attr != "check_case" or len(node.args) != 2:
                continue
            try:
                actual_case = tuple(ast.literal_eval(arg) for arg in node.args)
            except (ValueError, TypeError):
                continue
            if actual_case == expected_case:
                found = True
                break

        if not found:
            hours, pay = expected_case
            checks.error(
                f"Acceptance case changed in {test_name}; "
                f"expected ({hours}, {pay})."
            )

    expected_path = 'PROJECT_ROOT / "src" / "paycheck_calculator.py"'
    if expected_path not in text:
        checks.error(
            "Acceptance tests no longer target src/paycheck_calculator.py."
        )


def main() -> None:
    """Run all course-starter checks."""
    checks = StarterChecks()
    check_source(checks)
    check_pseudocode(checks)
    check_drawio(checks)
    check_sdw(checks)
    check_tests(checks)
    checks.finish()


if __name__ == "__main__":
    main()
