# Software Design Document (SDD)

- **Course:** IT 140 - *Introduction to Scripting*
- **Activity:** Module Three Assignment
- **Program:** Paycheck Calculator
- **Status:** Provided design reference; do not edit

## 0. Purpose

This SDD helps you organize your design work without providing a completed flowchart or completed pseudocode. The graded design decisions belong in your own `paycheck_calculator.drawio` and `paycheck_calculator.pseudo` files.

The current Module Three Assignment Guidelines and Rubric remains the official source for assignment requirements.

## 1. Design Inputs

Use these sources while designing:

1. Module Three Assignment Guidelines and Rubric in D2L Brightspace
2. [Software Requirements Specification (SRS)](../analysis/paycheck_calculator_srs.md)
3. Optional [Software Development Worksheet (SDW)](../paycheck_calculator_sdw.md) notes

Keep the distinction clear:

> **SRS = what the program must do**
>
> **Your flowchart and pseudocode = how you plan for the program to do it**

## 2. Solution Model

The solution needs to represent four general kinds of work:

- **Input** — obtain the information required by the assignment.
- **Decision** — determine which pay-rule case applies.
- **Processing** — perform the calculation required for that case.
- **Output** — present the calculated weekly paycheck.

Your flowchart and pseudocode should make the relationship among these kinds of work clear without adding requirements that are not in the assignment.

## 3. Boundary to Represent

The assignment defines a boundary at **40 hours**:

- the first 40 hours use the regular rate; and
- only hours **above 40** use the overtime rate.

Your design must make that boundary unambiguous. Use the assignment example and the verification cases in the SRS to check your reasoning, but create the branch condition and processing steps yourself.

## 4. Flowchart Design

The official assignment requires appropriate arrows and symbols for:

- Start and End
- Input and output
- Decision branching
- Processing

A readable flowchart should let another programmer answer:

1. Where does execution begin?
2. What input is obtained?
3. What question creates the branch?
4. What processing occurs on each path?
5. Where do the paths continue?
6. What result is output?
7. Where does execution end?

This document intentionally does not provide the answers in flowchart form.

## 5. Pseudocode Design

The official assignment asks for pseudocode that outlines a series of steps and uses appropriate indentation and keywords.

Your pseudocode should therefore make clear:

- the order of operations;
- the required input;
- the decision structure;
- the processing associated with each path;
- the output; and
- which statements belong inside each branch.

Pseudocode is not executable Python. Prefer clear program logic over Python-specific syntax.

## 6. Design Consistency Review

The two graded artifacts should describe the same planned behavior.

| Check | Flowchart | Pseudocode |
| --- | :---: | :---: |
| Required input is present | ☐ | ☐ |
| The 40-hour boundary is represented | ☐ | ☐ |
| Both pay-rule cases are represented | ☐ | ☐ |
| Weekly pay is calculated | ☐ | ☐ |
| The result is output | ☐ | ☐ |
| Logic matches the other artifact | ☐ | ☐ |

If a check differs between the two designs, revise the design artifacts before submission.

## 7. Requirements Traceability

Use the SRS identifiers to review your design without copying a completed algorithm.

| Requirement | Question to ask about your design |
| --- | --- |
| FR-1 | Where does the design obtain hours worked? |
| FR-2 | Where is regular-pay processing represented? |
| FR-3 | Where is overtime-pay processing represented? |
| FR-4 | Where does the design choose the applicable pay-rule case? |
| FR-5 | Where is total weekly pay determined? |
| FR-6 | Where is the paycheck output? |
| DR-1 | Does the flowchart use appropriate symbols and arrows? |
| DR-2 | Does pseudocode use logical order, indentation, and suitable keywords? |
| DR-3 | Do both artifacts describe the same planned behavior? |

## 8. Trace Before Coding

A design can be checked before code exists. Select a verification case from the SRS and follow its value through the flowchart and pseudocode one step at a time.

If the two designs take different paths or produce different results, revise the design before optional construction.

## 9. Optional Construction Handoff

If you continue into the optional Construct phase, treat your completed flowchart and pseudocode as the design handed to the programmer.

Implement what your design says. If coding reveals a design problem, revise the design first, then update the code so the artifacts stay consistent.

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Three Paycheck Calculator Software Design Document
* Artifact Type: Provided design reference
* Artifact Purpose: Explain design concepts, traceability, and consistency checks without supplying a completed graded solution.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
