"""Optional acceptance tests for the Module Three paycheck calculator.

Run from the repository root:
    python3 tests/test_paycheck_calculator.py

These tests are practice tools. They do not grade the Module Three Assignment.
"""

from pathlib import Path
import re
import subprocess
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = PROJECT_ROOT / "src" / "paycheck_calculator.py"


class PaycheckCalculatorAcceptanceTests(unittest.TestCase):
    """Check the optional program against numeric SRS acceptance cases."""

    def check_case(self, hours: int, expected_pay: int) -> None:
        """Run one case and look for the expected numeric result."""
        result = subprocess.run(
            [sys.executable, str(PROGRAM_PATH)],
            input=f"{hours}\n",
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=f"Program ended with an error:\n{result.stderr}",
        )

        # Accept common representations such as 800, $800, 800.0, or 800.00.
        pattern = rf"(?<![\d.]){expected_pay}(?:\.0+)?(?![\d.])"
        self.assertRegex(
            result.stdout.replace(",", ""),
            re.compile(pattern),
            msg=(
                f"Expected a paycheck value of {expected_pay} for {hours} hours.\n"
                f"Program output was:\n{result.stdout}"
            ),
        )

    def test_regular_hours(self) -> None:
        self.check_case(20, 400)

    def test_boundary_40_hours(self) -> None:
        self.check_case(40, 800)

    def test_first_overtime_hour(self) -> None:
        self.check_case(41, 830)

    def test_assignment_example(self) -> None:
        self.check_case(60, 1400)


if __name__ == "__main__":
    unittest.main(verbosity=2)
