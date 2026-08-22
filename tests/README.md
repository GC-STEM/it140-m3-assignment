<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Test Phase | Optional Practice

**SDLC progress:** [Start Here](../README.md) → [1 Analyze](../analysis/README.md) → [2 Design](../design/README.md) → [3 Construct (Practice)](../src/README.md) → **4 Test (Practice)** → [Submit](../README.md#submit-your-assignment)

## Purpose

Testing checks whether a constructed program behaves as its requirements and design say it should.

For the Module Three Assignment, testing Python code is **optional practice**. You do not submit the test file or optional Python program for grading.

## Before You Test

Complete this phase only if you chose to complete `src/paycheck_calculator.py`.

First confirm that:

- Your graded flowchart is complete.
- Your graded pseudocode is complete.
- Your optional Python program runs for at least one input value.

## 1. Test Manually

Run the program:

```bash
python3 src/paycheck_calculator.py
```

Use the acceptance cases in [`../analysis/paycheck_calculator_srs.md`](../analysis/paycheck_calculator_srs.md) to check:

- A normal regular-hours case
- Exactly 40 hours
- A value just above 40 hours
- The 60-hour example from the assignment

Compare the result with what you calculate from the stated pay rules.

## 2. Run the Optional Acceptance Tests

The provided [`test_paycheck_calculator.py`](test_paycheck_calculator.py) script runs the optional Python program several times and checks that the expected numeric paycheck appears in the output.

From the repository root:

```bash
python3 tests/test_paycheck_calculator.py
```

The test deliberately does not require one exact prompt or currency format because the assignment does not specify exact wording for an optional Python implementation.

> [!NOTE]
> These optional acceptance tests are **not** part of the active GitHub Assignment Checks. A student can receive a green repository check without completing the optional Python program. This keeps the automated workflow aligned with the Module Three graded requirements.

## 3. Debug One Problem at a Time

If a test fails:

1. Read the failing case and expected result.
2. Run your program manually with the same input.
3. Compare the program behavior with your pseudocode and flowchart.
4. Identify the first step where they differ.
5. Make one small correction.
6. Run the test again.

If coding reveals a design error, revise the graded design files so the design and optional implementation remain consistent.

## Check Your Work

- [ ] Regular-hours case works.
- [ ] Exactly 40 hours works.
- [ ] Overtime case works.
- [ ] The 60-hour assignment example produces a total of 1400.
- [ ] The program behavior still matches the flowchart and pseudocode.

## Help and Support

Use the [Module Three Assignment Wiki](https://github.com/GC-STEM/it140-m3-assignment/wiki) for supplemental testing and debugging guidance.

Use [GitHub Discussions](https://github.com/GC-STEM/it140-m3-assignment/discussions) for questions about using the optional practice tools.

Use [GitHub Issues](https://github.com/GC-STEM/it140-m3-assignment/issues) to report a technical problem with the provided test file or automated repository checks.

For assignment requirements, grading, or feedback, contact your instructor through D2L Brightspace.

## Next Step

Return to [Submit Your Assignment](../README.md#submit-your-assignment). Only the `.drawio` and `.pseudo` design files are required assignment deliverables.

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Three Assignment | Test Phase
* Artifact Type: Optional Python testing-practice guidance
* Artifact Purpose: Help students test and debug the optional paycheck-calculator Python implementation without making testing a graded Module Three requirement.
* Artifact Description: Students manually test their optional Python program, optionally run the provided acceptance tests, compare results with the SRS cases, and debug one problem at a time.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
