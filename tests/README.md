<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Test Phase | Optional Practice

**Required assignment path:** [Start Here](../README.md) → [Analyze](../analysis/README.md) → [Design](../design/README.md) → [Submit](../README.md#3-submit-your-assignment)

**Optional SDLC practice:** [Construct](../src/README.md) → **Test**

## Purpose

Testing checks whether a constructed program behaves as its requirements and design say it should.

For Module Three, testing Python code is **optional practice**. You do not submit the optional Python program, the test file, or test output for grading.

You can also use testing ideas before code exists by tracing verification cases through your flowchart and pseudocode.

## Deliverable

**This phase produces no graded or submitted Module Three deliverable.**

You may make corrections to your graded design files if testing exposes a design problem, and you may correct the optional `src/paycheck_calculator.py` implementation.

## What You Will Use

Use:

- [`../src/paycheck_calculator.py`](../src/paycheck_calculator.py) — optional program you constructed;
- your graded [flowchart](../design/paycheck_calculator.drawio) and [pseudocode](../design/paycheck_calculator.pseudo);
- the [SRS verification cases](../analysis/paycheck_calculator_srs.md#4-verification-cases); and
- [`test_paycheck_calculator.py`](test_paycheck_calculator.py) — provided optional automated acceptance tests.

Do not modify the provided test file to make a failing test pass.

## 1. Make Sure the Program Runs

Before automated testing, run your optional program yourself from the repository root:

```bash
python3 src/paycheck_calculator.py
```

On Windows, if your environment uses `python` rather than `python3`, use:

```powershell
python src/paycheck_calculator.py
```

If Python reports a syntax or runtime error, return to the [Construct Phase](../src/README.md), correct one problem, and run the program again.

## 2. Test Manually

Use several input values rather than checking only one example.

Useful cases include:

- a normal regular-hours case;
- exactly 40 hours;
- a value just above 40 hours; and
- the 60-hour example from the assignment.

Compare the program result with the [SRS verification table](../analysis/paycheck_calculator_srs.md#4-verification-cases).

Also compare the path the **program** appears to follow with the path represented in your **flowchart and pseudocode**. The implementation should follow the design.

## 3. Optional: Run the Automated Acceptance Tests

The provided [`test_paycheck_calculator.py`](test_paycheck_calculator.py) script runs the optional program several times and checks whether the expected numeric paycheck appears in the output.

You have not studied Python testing yet. You are not expected to understand or modify all of the test code.

From the repository root, run:

```bash
python3 tests/test_paycheck_calculator.py
```

The tests intentionally do **not** require one exact prompt, dollar-sign style, or currency format because the assignment does not specify those details for the optional Python implementation.

> [!NOTE]
> These optional acceptance tests are not part of the active student Assignment Checks. A student can receive a green repository check without completing the optional Python program.

## 4. Interpret the Results

### All Tests Pass

A passing test normally ends with:

```text
... ok
```

When all four tests pass, the summary ends with:

```text
OK
```

`OK` means the optional program produced the expected numeric result for all four repository verification cases.

It does **not** mean:

- your assignment has been graded;
- the flowchart automatically satisfies the rubric;
- the pseudocode automatically satisfies the rubric; or
- the assignment has been submitted.

### A Test Fails

A failed acceptance test is normally reported as `FAIL`.

Read:

1. the name of the failing case;
2. the expected paycheck in the failure message; and
3. the program output shown in the message.

Then compare the same case with:

- the SRS;
- your flowchart;
- your pseudocode; and
- your Python code.

Find the **first place** where the artifacts stop agreeing.

### The Program Has a Python Error

If the program cannot run normally, the test output may show `ERROR` or a message that the program ended with an error.

Read the last part of the Python error information, correct one problem in `paycheck_calculator.py`, run the program manually, and then rerun the tests.

Do not edit `test_paycheck_calculator.py` simply to remove a failure.

## 5. Debug One Problem at a Time

Testing is iterative:

> **Test → Find a problem → Correct → Retest**

A useful debugging sequence is:

1. Reproduce one failing case manually.
2. Check what the SRS requires for that input.
3. Trace the same input through your flowchart.
4. Trace it through your pseudocode.
5. Compare those steps with the Python implementation.
6. Identify the first mismatch.
7. Correct the appropriate artifact.
8. Retest the same case before changing anything else.

If coding reveals a design error, revise the graded design first and then bring the optional implementation back into alignment.

## 6. Check Your Work

- [ ] The optional program runs without a Python error.
- [ ] I manually checked a regular-hours case.
- [ ] I checked exactly 40 hours.
- [ ] I checked an overtime case.
- [ ] I checked the 60-hour assignment example.
- [ ] My program behavior remains consistent with my flowchart and pseudocode.
- [ ] If a test failed, I found and corrected the cause rather than modifying the provided test.
- [ ] If I changed a graded design file, I reviewed it again against the official rubric.

## Help and Support

If you have difficulty:

- Review the [SRS verification cases](../analysis/paycheck_calculator_srs.md#4-verification-cases).
- Review [Construct](../src/README.md) for syntax, indentation, and incremental-development guidance.
- See the [Module Three Assignment Wiki](https://github.com/GC-STEM/it140-m3-assignment/wiki) for supplemental testing and debugging explanations.
- Use [GitHub Discussions](https://github.com/GC-STEM/it140-m3-assignment/discussions) for questions about optional practice tools.
- Use [GitHub Issues](https://github.com/GC-STEM/it140-m3-assignment/issues) to report a technical problem with the provided test file or repository checks.
- Contact your instructor through D2L Brightspace for assignment requirements, grading, or feedback.

## Next Step

Return to [Submit Your Assignment](../README.md#3-submit-your-assignment). Only the `.drawio` and `.pseudo` design files are required Module Three submissions.

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Three Assignment | Test Phase
* Artifact Type: Optional Python testing-practice guidance
* Artifact Purpose: Help students test and debug the optional paycheck-calculator implementation while keeping testing outside the graded Module Three requirements.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
