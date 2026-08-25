"""Validate the Module Three repository structure and assignment artifacts."""

from __future__ import annotations

import argparse
import json
import re
import struct
import subprocess
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parents[2]

# Student work is intentionally limited to the two graded design files,
# optional SDW notes, and optional Python practice source.
EDITABLE_PATHS = {
    "paycheck_calculator_sdw.md",
    "design/paycheck_calculator.drawio",
    "design/paycheck_calculator.pseudo",
    "src/paycheck_calculator.py",
}

GRADED_PATHS = {
    "design/paycheck_calculator.drawio",
    "design/paycheck_calculator.pseudo",
}

REQUIRED_FILES = (
    ".gitattributes",
    ".gitignore",
    "README.md",
    "pyproject.toml",
    ".github/RЕADME.md",
    ".github/ISSUE_TEMPLATE/report-a-problem.yml",
    ".github/ISSUE_TEMPLATE/request-an-improvement.yml",
    ".github/ci/check_repository.py",
    ".github/ci/check_starter.py",
    ".github/social-preview.png",
    ".github/workflows/tests.yml",
    ".vscode/settings.json",
    "analysis/README.md",
    "analysis/paycheck_calculator_srs.md",
    "design/README.md",
    "design/paycheck_calculator.drawio",
    "design/paycheck_calculator.pseudo",
    "design/paycheck_calculator_sdd.md",
    "paycheck_calculator_sdw.md",
    "src/README.md",
    "src/paycheck_calculator.py",
    "tests/README.md",
    "tests/test_paycheck_calculator.py",
)

# Course-managed Markdown is checked in both starter and student repositories.
PROVIDED_MARKDOWN = (
    "README.md",
    ".github/RЕADME.md",
    "analysis/README.md",
    "analysis/paycheck_calculator_srs.md",
    "design/README.md",
    "design/paycheck_calculator_sdd.md",
    "src/README.md",
    "tests/README.md",
)

# These markers intentionally focus on stable document structure rather than
# prose so routine wording changes do not require CI maintenance.
REQUIRED_TEXT_MARKERS = {
    "README.md": (
        "# IT 140 Module Three Assignment",
        "## 0. Meet the Prerequisites",
        "## 1. Set Up or Open Your Assignment Repository",
        "## 2. Complete the Assignment",
        "## 3. Submit Your Assignment",
        "## Optional: Continue Through Construct and Test",
        "## Help and Support",
    ),
    "analysis/README.md": (
        "# Analyze Phase",
        "## Purpose",
        "## Deliverable",
        "## What You Will Use",
        "## What You Will Do",
        "## Check Your Work",
        "## Help and Support",
    ),
    "analysis/paycheck_calculator_srs.md": (
        "# Software Requirements Specification (SRS)",
        "## 1. Functional Requirements",
        "## 2. Design Requirements",
        "## 3. Technology and File Constraints",
        "## 4. Verification Cases",
        "## 5. Out of Scope Unless Your Instructor Adds a Requirement",
        "## 6. Requirements Traceability",
    ),
    "design/README.md": (
        "# Design Phase",
        "## Purpose",
        "## Graded Deliverables",
        "## What You Will Use",
        "## What You Will Do",
        "## 3. Create the Flowchart",
        "## 4. Create the Pseudocode",
        "## 5. Compare the Two Designs",
        "## 7. Review Against the Rubric",
        "## Help and Support",
    ),
    "design/paycheck_calculator_sdd.md": (
        "# Software Design Document (SDD)",
        "## 2. Solution Model",
        "## 6. Design Consistency Review",
        "## 7. Requirements Traceability",
        "## 9. Optional Construction Handoff",
    ),
    "src/README.md": (
        "# Construct Phase",
        "## Purpose",
        "## Deliverable",
        "### Edit Only TODO Lines",
        "## What You Will Do",
        "## Check Your Work",
    ),
    "tests/README.md": (
        "# Test Phase",
        "## Purpose",
        "## Deliverable",
        "## 2. Test Manually",
        "## 3. Optional: Run the Automated Acceptance Tests",
        "## 4. Interpret the Results",
        "## 5. Debug One Problem at a Time",
    ),
}

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class Checks:
    """Collect validation results and emit one useful report."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.notes: list[str] = []

    def error(self, message: str) -> None:
        """Record a failing check."""
        self.errors.append(message)

    def note(self, message: str) -> None:
        """Record a successful or informational check."""
        self.notes.append(message)

    def finish(self) -> None:
        """Print results and exit nonzero if any checks failed."""
        for note in self.notes:
            print(f"PASS: {note}")

        if not self.errors:
            print("PASS: Repository and artifact checks completed.")
            return

        print("\nRepository checks failed:", file=sys.stderr)
        for error in self.errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def read_text(relative_path: str) -> str:
    """Read one repository text file as UTF-8."""
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def check_required_files(checks: Checks) -> None:
    """Verify required repository files exist and are nonempty."""
    missing_or_empty = 0
    for relative_path in REQUIRED_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            checks.error(f"Required file is missing: {relative_path}")
            missing_or_empty += 1
            continue
        if path.stat().st_size == 0:
            checks.error(f"Required file is empty: {relative_path}")
            missing_or_empty += 1

    if missing_or_empty == 0:
        checks.note("Required repository files are present and nonempty.")


def check_json_and_toml(checks: Checks) -> None:
    """Parse repository JSON and TOML configuration files."""
    settings_path = REPO_ROOT / ".vscode/settings.json"
    pyproject_path = REPO_ROOT / "pyproject.toml"

    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
        if not isinstance(settings, dict):
            checks.error(".vscode/settings.json must contain a JSON object.")
    except (OSError, json.JSONDecodeError) as exc:
        checks.error(f"Invalid .vscode/settings.json: {exc}")

    try:
        with pyproject_path.open("rb") as handle:
            pyproject = tomllib.load(handle)
        lint = pyproject.get("tool", {}).get("ruff", {}).get("lint", {})
        selected = set(lint.get("select", []))
        if not {"E", "F"}.issubset(selected):
            checks.error("pyproject.toml must keep Ruff E and F checks enabled.")
    except (OSError, tomllib.TOMLDecodeError) as exc:
        checks.error(f"Invalid pyproject.toml: {exc}")


def check_required_text_markers(checks: Checks) -> None:
    """Verify major course-managed documents keep expected sections."""
    missing = 0
    for relative_path, markers in REQUIRED_TEXT_MARKERS.items():
        text = read_text(relative_path)
        for marker in markers:
            if marker not in text:
                checks.error(
                    f"Required section is missing from {relative_path}: {marker}"
                )
                missing += 1

    if missing == 0:
        checks.note("Major Markdown artifacts keep their expected sections.")


def check_drawio(checks: Checks) -> None:
    """Verify the graded Draw.io file remains parseable XML."""
    path = REPO_ROOT / "design/paycheck_calculator.drawio"
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        checks.error(f"Invalid Draw.io XML in design/paycheck_calculator.drawio: {exc}")
        return

    tag = root.tag.rsplit("}", maxsplit=1)[-1]
    if tag != "mxfile":
        checks.error("design/paycheck_calculator.drawio must have an mxfile root.")
        return

    diagrams = [
        node
        for node in root.iter()
        if node.tag.rsplit("}", maxsplit=1)[-1] == "diagram"
    ]
    if not diagrams:
        checks.error("The Draw.io file contains no diagram pages.")
    else:
        checks.note("The graded Draw.io file is parseable XML.")


def check_pseudocode(checks: Checks, mode: str) -> None:
    """Verify the pseudocode keeps its expected outer structure."""
    text = read_text("design/paycheck_calculator.pseudo")
    begin = text.find("BEGIN paycheck_calculator")
    end = text.rfind("END paycheck_calculator")

    if begin < 0:
        checks.error("Pseudocode is missing 'BEGIN paycheck_calculator'.")
    if end < 0:
        checks.error("Pseudocode is missing 'END paycheck_calculator'.")
    if begin >= 0 and end >= 0 and begin >= end:
        checks.error("Pseudocode BEGIN must appear before END.")

    if mode == "student":
        todo_lines = [line.strip() for line in text.splitlines() if "TODO:" in line]
        if todo_lines:
            checks.error("The graded pseudocode still contains starter TODO prompts.")
        else:
            checks.note("The graded pseudocode starter TODOs were replaced.")
    elif begin >= 0 and end > begin:
        checks.note("The pseudocode has the expected BEGIN/END structure.")


def without_code_fences(text: str) -> str:
    """Remove fenced code blocks before scanning Markdown links."""
    output: list[str] = []
    in_fence = False
    fence_marker = ""

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if not in_fence:
            output.append(line)

    return "\n".join(output)


def local_link_target(raw_target: str) -> str | None:
    """Return a local Markdown link path or None for external links."""
    target = raw_target.strip()
    if not target:
        return None

    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]

    if target.startswith("#"):
        return None

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None

    path = unquote(parsed.path)
    if not path or path.startswith("/"):
        return None
    return path


def check_markdown_links(checks: Checks) -> None:
    """Verify local links in course-managed Markdown files."""
    broken = 0
    repo_root = REPO_ROOT.resolve()

    for relative_path in PROVIDED_MARKDOWN:
        file_path = REPO_ROOT / relative_path
        text = without_code_fences(file_path.read_text(encoding="utf-8"))

        for match in MARKDOWN_LINK.finditer(text):
            target = local_link_target(match.group(1))
            if target is None:
                continue

            resolved = (file_path.parent / target).resolve()
            try:
                resolved.relative_to(repo_root)
            except ValueError:
                checks.error(
                    f"Local link leaves the repository in {relative_path}: {target}"
                )
                broken += 1
                continue

            if not resolved.exists():
                checks.error(f"Broken local link in {relative_path}: {target}")
                broken += 1

    if broken == 0:
        checks.note("Local links in course-managed Markdown files resolve.")


def check_social_preview(checks: Checks) -> None:
    """Check the repository social-preview PNG signature, size, and ratio."""
    path = REPO_ROOT / ".github/social-preview.png"
    data = path.read_bytes()

    if len(data) > 1_048_576:
        checks.error(".github/social-preview.png must remain under 1 MiB.")
        return

    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        checks.error(".github/social-preview.png is not a valid PNG file.")
        return

    width, height = struct.unpack(">II", data[16:24])
    if width < 640 or height < 320:
        checks.error(
            "Social preview dimensions are unexpectedly small: "
            f"{width}x{height}."
        )
        return

    ratio = width / height
    if not 1.9 <= ratio <= 2.1:
        checks.error(
            "Social preview should remain approximately 2:1; "
            f"found {width}x{height}."
        )
        return

    checks.note(f"Social preview is valid ({width}x{height}, {len(data)} bytes).")


def git_output(*args: str) -> str:
    """Run Git and return stripped standard output."""
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(message or "Git command failed.")
    return result.stdout.strip()


def student_changed_paths(checks: Checks) -> set[str] | None:
    """Return committed paths changed since the template root commit."""
    try:
        roots = git_output("rev-list", "--max-parents=0", "HEAD").splitlines()
    except RuntimeError as exc:
        checks.error(f"Could not inspect repository history: {exc}")
        return None

    if len(roots) != 1:
        checks.error(
            "Could not identify one initial template commit for this personal repository."
        )
        return None

    try:
        changed_text = git_output(
            "diff",
            "--name-only",
            "--diff-filter=ACDMRTUXB",
            roots[0],
            "HEAD",
        )
    except RuntimeError as exc:
        checks.error(f"Could not compare with the template commit: {exc}")
        return None

    return {line for line in changed_text.splitlines() if line}


def check_student_change_scope(
    checks: Checks,
    changed: set[str] | None,
) -> None:
    """Ensure committed changes are limited to student-editable files."""
    if changed is None:
        return

    unexpected = sorted(changed - EDITABLE_PATHS)
    for path in unexpected:
        checks.error(
            "Provided repository file was added, removed, renamed, or changed: "
            f"{path}"
        )

    if not unexpected:
        checks.note("Committed changes are limited to student working/practice files.")


def check_student_graded_changes(
    checks: Checks,
    changed: set[str] | None,
) -> None:
    """Verify both graded design files differ from the template commit."""
    if changed is None:
        return

    missing = sorted(GRADED_PATHS - changed)
    for path in missing:
        checks.error(
            "Graded design file has not changed from the starter template: "
            f"{path}"
        )

    if not missing:
        checks.note("Both graded design files differ from the starter state.")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        required=True,
        choices=("starter", "student"),
        help="Validate the course starter or a personal student repository.",
    )
    return parser.parse_args()


def main() -> None:
    """Run repository and artifact checks."""
    args = parse_args()
    checks = Checks()

    check_required_files(checks)
    if checks.errors:
        checks.finish()

    check_json_and_toml(checks)
    check_required_text_markers(checks)
    check_drawio(checks)
    check_pseudocode(checks, args.mode)
    check_markdown_links(checks)
    check_social_preview(checks)

    if args.mode == "student":
        changed = student_changed_paths(checks)
        check_student_change_scope(checks, changed)
        check_student_graded_changes(checks, changed)
    else:
        checks.note("Starter mode skips student completion checks.")

    checks.finish()


if __name__ == "__main__":
    main()
