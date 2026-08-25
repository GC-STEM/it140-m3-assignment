<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Construct Phase | Optional Python Practice

**Required assignment path:** [Start Here](../README.md) → [Analyze](../analysis/README.md) → [Design](../design/README.md) → [Submit](../README.md#3-submit-your-assignment)

**Optional SDLC practice:** **Construct** → [Test](../tests/README.md)

## Purpose

During Construct, a programmer turns a design into working code.

For the Module Three Assignment, construction is **optional practice**. Your grade is based on the flowchart and pseudocode, not on `paycheck_calculator.py`.

Complete this phase only **after** your two graded design files are complete and ready to submit. The purpose is to practice treating your own design as the plan for a Python program.

## Deliverable

**This phase does not produce a graded or submitted Module Three deliverable.**

You may complete [`paycheck_calculator.py`](paycheck_calculator.py) for practice. Do not submit it for the Module Three Assignment unless your instructor specifically requests it.

## What You Will Use

Use:

- your completed [`../design/paycheck_calculator.drawio`](../design/paycheck_calculator.drawio);
- your completed [`../design/paycheck_calculator.pseudo`](../design/paycheck_calculator.pseudo);
- the provided [`paycheck_calculator.py`](paycheck_calculator.py) starter;
- the [SRS](../analysis/paycheck_calculator_srs.md) when checking requirements; and
- Module Three decision-branching concepts.

Relevant zyBooks sections include:

- **1.3 Basic input and output**
- **1.15 Numeric types: Floating-point**
- **1.16 Arithmetic expressions**
- **2.6 Type conversions**
- **2.7 String formatting**
- **3.1 If-else branches (general)**
- **3.2 If-else statement**
- **3.4 Equality and relational operators**
- **3.5 Boolean operators and expressions**
- **3.8 Code blocks and indentation**

## Read the Starter Before Editing

Open [`paycheck_calculator.py`](paycheck_calculator.py) and read it from beginning to end.

The file is organized approximately as:

```text
Module docstring
Constants
Main function
Main guard
References
```

Some of this structure uses concepts you have not formally studied yet. It is included as instructional scaffolding so the optional program resembles the structured Python files used elsewhere in the course.

### Edit Only TODO Lines

For this optional practice, **change only lines marked with `TODO:`**.

This includes:

- `TODO:` lines inside the module docstring;
- `# TODO:` comments inside `main()`; and
- `# TODO:` lines in the References section.

Do not change the provided constants, `main()` definition, function docstring, main guard, or other course-provided lines.

When replacing a TODO inside `main()`, keep your Python code indented four spaces so it remains inside the function.

## Understand the Starter Structure

### Module Docstring

The triple-quoted text at the top is a **module docstring**. It asks you to summarize the optional program and describe its Input → Process → Output behavior.

Use your own Analyze and Design work as the source for those descriptions. The usage example should use your own input value rather than copying a repository verification case.

### Constants

The starter defines:

```python
REGULAR_RATE = 20
OVERTIME_RATE = 30
REGULAR_HOURS_LIMIT = 40
```

These values come directly from the assignment's pay rules. The uppercase names indicate that the program intends to treat them as constants.

Do not change these lines for this practice activity.

### Main Function

All optional implementation TODOs are inside:

```python
def main() -> None:
    """Run the optional paycheck calculator practice program."""
```

You will study functions in more depth later. For now, treat `main()` as the place where the program's main sequence of steps belongs.

### Main Guard

The starter ends with:

```python
if __name__ == "__main__":
    main()
```

This is commonly called a **main guard**. When the file is run directly, it calls `main()`.

You do not need to master this structure in Module Three. Do not change it.

## What You Will Do

### 1. Put Your Design Beside the Starter

Open your completed flowchart or pseudocode to the side of `paycheck_calculator.py`.

Use **your pseudocode as the primary coding guide**. Read one design step at a time and identify the Python concept that performs the same job.

### 2. Complete the Documentation TODOs

Use your own SDW/design work to describe:

- the program purpose;
- input;
- processing;
- output; and
- an original usage example.

The docstring is practice documentation, not a graded Module Three requirement.

### 3. Complete the Input TODO

Translate your design's input step into the simplest Python statement that obtains the required value in a numeric form your calculations can use.

Review input and type conversion in zyBooks if needed.

### 4. Complete the Decision and Processing TODOs

Use the branch condition and calculations from **your own graded design**.

Keep the implementation simple. Module Three concepts are sufficient:

- variables;
- arithmetic expressions;
- `if` / `else`;
- relational operators; and
- indentation.

If your design and code disagree, revise the design first, then update the code.

### 5. Complete the Output TODO

Translate the output step from your design into Python.

The official assignment does not require an exact prompt or currency format for this optional implementation, so do not add complexity merely to satisfy an imagined formatting requirement.

### 6. Run After Small Changes

Work incrementally:

1. Replace one code TODO.
2. Run the program.
3. Correct syntax or runtime errors.
4. Continue only after the program runs again.

This makes it easier to identify which recent change caused a problem.

From the repository root:

```bash
python3 src/paycheck_calculator.py
```

On Windows, if your configured environment uses `python` rather than `python3`, use:

```powershell
python src/paycheck_calculator.py
```

### 7. Complete the References Section

If you used outside sources, examples, people, IDE-generated suggestions, or generative AI assistance while completing the optional practice, acknowledge the assistance according to current SNHU and assignment guidance.

If you did not use an outside source, delete the unused reference TODO line.

## Check Your Work

Before moving to optional testing, make sure:

- [ ] My graded flowchart and pseudocode were complete before I began optional coding.
- [ ] I changed only TODO lines in the starter.
- [ ] My module docstring describes this paycheck calculator, not another assignment.
- [ ] My code follows my own pseudocode and flowchart.
- [ ] I left the constants, `main()` definition, and main guard unchanged.
- [ ] Code inside `main()` remains indented correctly.
- [ ] I ran after small changes and corrected errors incrementally.
- [ ] I added references for outside help I actually used or deleted the unused reference TODO.
- [ ] No TODO lines remain in my completed optional file.
- [ ] The program runs without a Python error for a normal input value.

## Help and Support

If you have difficulty:

- Start with your completed pseudocode and translate one step at a time.
- Return to [Design](../design/README.md) if the design is incomplete or inconsistent.
- See the [Module Three Assignment Wiki](https://github.com/GC-STEM/it140-m3-assignment/wiki) for supplemental guidance.
- Use [GitHub Discussions](https://github.com/GC-STEM/it140-m3-assignment/discussions) for questions about optional practice tools.
- Use [GitHub Issues](https://github.com/GC-STEM/it140-m3-assignment/issues) to report technical problems with the provided starter.
- Contact your instructor through D2L Brightspace for assignment requirements or grading questions.

## Next Step

Continue to [Test](../tests/README.md) for optional practice, or return to [Submit Your Assignment](../README.md#3-submit-your-assignment).

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Three Assignment | Construct Phase
* Artifact Type: Optional Python construction-practice guidance
* Artifact Purpose: Help students translate their completed graded designs into a simple Python program using Module Three concepts.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
