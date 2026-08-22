<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Design Phase | Create the Flowchart and Pseudocode

**SDLC progress:** [Start Here](../README.md) → [1 Analyze](../analysis/README.md) → **2 Design** → [3 Construct (Practice)](../src/README.md) → [4 Test (Practice)](../tests/README.md) → [Submit](../README.md#submit-your-assignment)

## Purpose

The Design phase is the focus of the Module Three Assignment. You will turn the paycheck requirements into two representations of the same solution:

1. A **flowchart**
2. **Pseudocode**

These are the two files you submit for grading.

## Graded Deliverables

Complete both files in this folder:

- [`paycheck_calculator.drawio`](paycheck_calculator.drawio) — flowchart
- [`paycheck_calculator.pseudo`](paycheck_calculator.pseudo) — pseudocode

The [Software Design Document (SDD)](paycheck_calculator_sdd.md) is a reference that explains the design goals and consistency checks without providing a completed solution. The [SDW](../paycheck_calculator_sdw.md) is optional working space.

## Before You Design

Make sure you have:

1. Read the Module Three Assignment Guidelines and Rubric.
2. Completed the [Analyze Phase](../analysis/README.md).
3. Reviewed the [SRS](../analysis/paycheck_calculator_srs.md).
4. Identified the input, decision, processing, output, and 40-hour boundary.

If decision branching is still unclear, review the Module Three course content and the relevant zyBooks sections on `if`/`else` branches, relational operators, Boolean expressions, and code-block indentation.

## 1. Create the Flowchart

Open [`paycheck_calculator.drawio`](paycheck_calculator.drawio) in VS Code using the Draw.io integration.

The template contains these tabs:

- **Paycheck Calculator** — create your graded flowchart here.
- **README** — template instructions.
- **Symbols** — flowchart symbols used in IT 140.
- **Snippets** — example flowchart constructs you may use as references.
- **References** — source information for the provided flowchart symbols and conventions.

Use the symbols required by the assignment for:

- Start and end points
- Input and output
- Decision branching
- Processing steps

Connect the steps with arrows so another programmer can follow the logic from start to end. Make sure every possible path created by your decision reaches the correct later step and ultimately reaches the end.

> [!TIP]
> The assignment template's **Symbols** tab can be used as a source for the correct symbol shapes. You can copy symbols to the Draw.io Scratchpad or directly into your Paycheck Calculator page, then replace the placeholder text with your own design steps.

Do not replace the `.drawio` file with an image, PDF, or screenshot. The required submission format is `.drawio`.

## 2. Write the Pseudocode

After your flowchart logic is organized, open [`paycheck_calculator.pseudo`](paycheck_calculator.pseudo).

Complete the `TODO:` prompts in the file. Your pseudocode should:

- Identify the input the computer needs.
- Show the processing needed to calculate the weekly paycheck.
- Use decision branching where the pay rules require different actions.
- Account for all input values covered by the required pay rules.
- Show the output.
- Use appropriate indentation and pseudocode keywords such as `IF`, `ELSE`, and `LET` where appropriate.

Pseudocode is a design tool, not Python. Focus on clear logic rather than Python syntax.

## 3. Compare the Two Designs

Before submitting, read the flowchart and pseudocode side by side.

Check that they agree about:

- The input
- The decision condition
- What happens on each branch
- The calculations
- The final output

If one design says something the other does not, revise them until they represent the same solution.

## 4. Check Against the Rubric

### Flowchart checklist

- [ ] Start and end points use appropriate symbols.
- [ ] Input and output use appropriate symbols.
- [ ] Processing steps use appropriate symbols.
- [ ] Decision branching uses an appropriate decision symbol.
- [ ] Arrows make the order and branches clear.
- [ ] The logic represents the paycheck requirements.

### Pseudocode checklist

- [ ] The steps are in a logical order.
- [ ] The input is identified.
- [ ] The processing steps produce the required paycheck.
- [ ] Decision branching accounts for the required pay-rule cases.
- [ ] Indentation shows which steps belong inside each branch.
- [ ] Appropriate pseudocode keywords are used.
- [ ] The output is identified.

> [!NOTE]
> The GitHub **Assignment Checks** can verify basic file state, including whether both graded design files changed from the starter, whether the Draw.io file remains readable XML, and whether the pseudocode starter TODOs were replaced. The checks cannot evaluate the quality or correctness of your design. Use the assignment Guidelines and Rubric for that review.

## Help and Support

For supplemental explanations about flowcharts, pseudocode, or the course tools, see the [Module Three Assignment Wiki](https://github.com/GC-STEM/it140-m3-assignment/wiki).

Use [GitHub Discussions](https://github.com/GC-STEM/it140-m3-assignment/discussions) for repository-related questions that do not ask for a completed graded solution.

Use [GitHub Issues](https://github.com/GC-STEM/it140-m3-assignment/issues) to report a technical problem with the provided design files, documentation, or automated checks.

For assignment requirements, grading, or feedback, contact your instructor through D2L Brightspace.

## Next Step

Your graded design work is complete when both design files meet the current Guidelines and Rubric.

You may now:

- Go to [Submit Your Assignment](../README.md#submit-your-assignment), or
- Continue to the [Construct Phase](../src/README.md) for optional Python practice.

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Three Assignment | Design Phase
* Artifact Type: Required assignment guidance for graded design deliverables
* Artifact Purpose: Guide students in creating and reviewing the required paycheck-calculator flowchart and pseudocode.
* Artifact Description: Students create the graded Draw.io flowchart and pseudocode, compare the two representations for consistency, and review them against the assignment rubric.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
