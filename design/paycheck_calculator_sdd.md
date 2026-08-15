# Software Design Document (SDD)

- **Course**: IT 140 - Introduction to Scripting
- **Activity**: Module Three Assignment
- **Program name**: Paycheck Calculator
- **Status**: Design reference; do not edit

## 0. Purpose

This SDD helps you organize the design work without providing a completed flowchart or completed pseudocode. The graded design decisions belong in your own `paycheck_calculator.drawio` and `paycheck_calculator.pseudo` files.

The current Module Three Assignment Guidelines and Rubric remains the official source for assignment requirements.

## 1. Design Inputs

Use these sources while designing:

1. The Module Three Assignment Guidelines and Rubric
2. [`../analysis/paycheck_calculator_srs.md`](../analysis/paycheck_calculator_srs.md)
3. Your optional [`../paycheck_calculator_sdw.md`](../paycheck_calculator_sdw.md) notes

## 2. Design Model

The solution needs to represent four general types of work:

- **Input** — obtain the number of hours worked.
- **Decision** — determine which pay rule applies to the input.
- **Processing** — calculate the weekly paycheck using the applicable rule or rules.
- **Output** — present the calculated weekly paycheck.

Your flowchart and pseudocode should make the relationship among these steps clear without adding requirements that are not in the assignment.

## 3. Boundary to Represent

The assignment defines a boundary at **40 hours**:

- The first 40 hours use the regular rate.
- Only hours **above 40** use the overtime rate.

Your design must make the boundary unambiguous. Use the assignment example and the acceptance conditions in the SRS to check your reasoning, but create the branch condition and processing steps yourself.

## 4. Flowchart Design Constraints

Your flowchart must use appropriate symbols and arrows for:

- Start and end points
- Input and output
- Decision branching
- Processing steps

The flow should be readable from start to end, and each path created by a decision should lead to the correct later processing and output.

## 5. Pseudocode Design Constraints

Your pseudocode should:

- Use clear, ordered steps.
- Use indentation to show statements that belong to a branch.
- Use appropriate pseudocode keywords.
- Represent the same decision and calculations as the flowchart.

Do not worry about matching Python syntax. Pseudocode is a plan for code, not executable code.

## 6. Design Consistency Review

Before considering the design complete, compare the two artifacts.

| Question | Flowchart | Pseudocode |
| --- | --- | --- |
| Is the required input present? | Check | Check |
| Is the 40-hour decision represented? | Check | Check |
| Are both pay-rule cases represented? | Check | Check |
| Is the weekly paycheck calculated? | Check | Check |
| Is the result output? | Check | Check |
| Does the logic match the other artifact? | Check | Check |

## 7. Optional Construction Handoff

If you continue into the optional Construct phase, treat your completed flowchart and pseudocode as the design handed to the programmer.

Implement what your design says. If coding reveals a design problem, revise the design first, then update the code so the artifacts stay consistent.
