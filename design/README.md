<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Design Phase | Create the Flowchart and Pseudocode

**Required assignment progress:** [0 Start Here](../README.md) → [1 Analyze](../analysis/README.md) → **2 Design** → [3 Submit](../README.md#3-submit-your-assignment)

**Optional SDLC practice after Design:** [Construct](../src/README.md) → [Test](../tests/README.md)

## Purpose

During the Design phase, your goal is to decide **how** the paycheck calculator will meet the requirements before writing Python code.

You will represent the same planned program in two ways:

1. a **flowchart**, which shows the sequence and branches visually; and
2. **pseudocode**, which shows the sequence and branches as structured text.

These are the two graded Module Three deliverables.

## Graded Deliverables

Complete both files:

- [`paycheck_calculator.drawio`](paycheck_calculator.drawio) — graded flowchart
- [`paycheck_calculator.pseudo`](paycheck_calculator.pseudo) — graded pseudocode

The [Software Design Document (SDD)](paycheck_calculator_sdd.md) provides design guidance without giving you a completed solution. The [SDW](../paycheck_calculator_sdw.md) provides optional working space.

Do not submit the SDD or SDW unless your instructor specifically requests them.

## What You Will Use

Use:

- the Module Three Assignment Guidelines and Rubric in D2L Brightspace;
- the [SRS](../analysis/paycheck_calculator_srs.md);
- the [SDD](paycheck_calculator_sdd.md);
- the optional [SDW](../paycheck_calculator_sdw.md);
- the Draw.io starter template; and
- the pseudocode starter template.

Relevant zyBooks topics include decision branching, relational operators, Boolean expressions, and indentation.

## What You Will Do

### 1. Review Requirements Before Designing

Make sure you can identify:

- the required input;
- the regular-pay rule;
- the overtime-pay rule;
- the 40-hour boundary;
- the decision the solution must make; and
- the required output.

If any of these are unclear, return to the [Analyze Phase](../analysis/README.md) before editing the graded files.

### 2. Plan the Solution

Use the Design section of the [SDW](../paycheck_calculator_sdw.md), if useful, to plan the solution in words before placing flowchart shapes or writing detailed pseudocode.

Your plan should answer questions such as:

- What happens first?
- Where does the solution need a decision?
- What must happen on each possible path?
- Where do the paths rejoin, if appropriate?
- What result is produced at the end?

Do not begin by writing Python. The purpose of this assignment is to practice design before construction.

## 3. Create the Flowchart

Open [`paycheck_calculator.drawio`](paycheck_calculator.drawio) in VS Code using the Draw.io integration.

The template contains reference tabs:

- **Paycheck Calculator** — create your graded flowchart here.
- **README** — read the template instructions.
- **Symbols** — use the flowchart symbols required in IT 140.
- **Snippets** — review generic flowchart constructs without a paycheck solution.
- **References** — review source information for the symbols or conventions.

The official assignment requires appropriate arrows and symbols for:

- Start and end points
- Input and output
- Decision branching
- Processing steps

Build the chart so another programmer can follow the logic from Start to End. Every path created by the decision should continue to the correct later step and eventually reach End.

> [!TIP]
> The **Symbols** tab is a source for shapes. Copy the shapes you need to the Scratchpad or your Paycheck Calculator page, then replace placeholder text with your own design steps.

Do not replace the `.drawio` file with an image, PDF, or screenshot. The required submission format is `.drawio`.

## 4. Create the Pseudocode

Open [`paycheck_calculator.pseudo`](paycheck_calculator.pseudo).

Complete the `TODO:` prompts with your own pseudocode. Your finished pseudocode should:

- obtain the required input;
- show the processing needed to calculate weekly pay;
- use decision branching where the pay rules require different processing;
- account for all input values covered by the stated pay rules;
- show the required output; and
- use appropriate indentation and keywords such as `IF`, `ELSE`, and `LET` where they fit your design.

Pseudocode is a design tool, not Python. Focus on understandable logic rather than Python syntax.

## 5. Compare the Two Designs

Open the flowchart and pseudocode side by side.

Check that they agree about:

- the input;
- the decision condition;
- what happens on each decision path;
- the calculations;
- the 40-hour boundary; and
- the final output.

If one design contains a step or behavior the other does not, revise them until they represent the same planned program.

## 6. Trace Verification Cases

Use the [SRS verification cases](../analysis/paycheck_calculator_srs.md#4-verification-cases) to trace the design by hand.

At minimum, make sure you understand what path the design follows for:

- a regular-hours value;
- exactly 40 hours;
- a value just above 40 hours; and
- the 60-hour assignment example.

Do not change the requirements to make a case work. If tracing exposes a design problem, revise the design.

## 7. Review Against the Rubric

### Flowchart checklist

- [ ] The steps are organized from Start to End.
- [ ] Start and End use appropriate symbols.
- [ ] Input and output use appropriate symbols.
- [ ] Processing uses appropriate symbols.
- [ ] Decision branching uses an appropriate decision symbol.
- [ ] Arrows make sequence and branches clear.
- [ ] Every decision path is connected and eventually reaches End.
- [ ] The logic represents the stated paycheck requirements.

### Pseudocode checklist

- [ ] The steps are logically ordered.
- [ ] The required input is identified.
- [ ] The processing produces the weekly paycheck.
- [ ] Decision branching accounts for the pay-rule cases.
- [ ] Indentation shows which steps belong inside each branch.
- [ ] Appropriate pseudocode keywords are used.
- [ ] The required output is identified.
- [ ] No starter `TODO:` prompts remain.

### Consistency checklist

- [ ] The flowchart and pseudocode represent the same input.
- [ ] They use the same decision logic.
- [ ] They represent the same calculations.
- [ ] They treat the 40-hour boundary the same way.
- [ ] They produce the same output.

## 8. Review the Assignment Checks

After you commit and push, GitHub Assignment Checks can verify basic file state, including whether both graded files changed from their starter state, whether the Draw.io file remains readable XML, and whether the pseudocode starter TODOs were replaced.

The checks cannot evaluate whether your design is correct, well organized, or worthy of a particular grade. Use the official Guidelines and Rubric for that review.

## Help and Support

If you have difficulty completing this phase:

- Compare the [SRS](../analysis/paycheck_calculator_srs.md), [SDD](paycheck_calculator_sdd.md), and your SDW notes one requirement at a time.
- See the [Module Three Assignment Wiki](https://github.com/GC-STEM/it140-m3-assignment/wiki) for supplemental explanations of flowcharts and pseudocode.
- Use [GitHub Discussions](https://github.com/GC-STEM/it140-m3-assignment/discussions) for repository-related questions that do not request a completed graded solution.
- Use [GitHub Issues](https://github.com/GC-STEM/it140-m3-assignment/issues) to report a technical problem with the provided design files, documentation, or automated checks.
- Contact your instructor through D2L Brightspace for assignment requirements, grading, or feedback.

## Next Step

When both design files meet the current Guidelines and Rubric, go to [Submit Your Assignment](../README.md#3-submit-your-assignment).

After the graded work is ready, you may also continue to the [Construct Phase](../src/README.md) for optional Python practice.

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Three Assignment | Design Phase
* Artifact Type: Required assignment guidance for graded design deliverables
* Artifact Purpose: Guide students in creating, tracing, comparing, and reviewing the required paycheck-calculator flowchart and pseudocode.
* Artifact Description: Students create two representations of the same solution, trace verification cases, and review both artifacts against the assignment rubric before submission.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
