# Software Requirements Specification (SRS)

- **Course:** IT 140 - *Introduction to Scripting*
- **Activity:** Module Three Assignment
- **Program:** Paycheck Calculator
- **Status:** Provided requirements reference; do not edit

## 0. General Description

The Paycheck Calculator is a small program design for calculating an employee's weekly paycheck from the number of hours worked during a week. The design must represent the company's regular-pay and overtime-pay rules and produce the employee's total weekly paycheck.

This SRS reorganizes requirements from the Module Three Assignment Guidelines and Rubric. It does not replace or expand that assignment. If this file and the current Guidelines and Rubric differ, follow the Guidelines and Rubric.

## 1. Functional Requirements

The planned program shall:

- **FR-1 — Obtain hours worked.** Obtain the number of hours the employee worked during the week.
- **FR-2 — Apply regular pay.** Apply a rate of **$20 per hour** to the first **40 hours** worked.
- **FR-3 — Apply overtime pay.** Apply a rate of **$30 per hour** to each hour worked **above 40 hours**.
- **FR-4 — Select the applicable calculation.** Use decision branching so the appropriate pay calculation is performed for the hours worked.
- **FR-5 — Calculate weekly pay.** Calculate the employee's total weekly paycheck.
- **FR-6 — Output weekly pay.** Output the calculated weekly paycheck.

## 2. Design Requirements

The graded assignment shall represent the solution in both required design artifacts.

### DR-1 — Flowchart

Create `design/paycheck_calculator.drawio` using appropriate symbols and arrows for:

- start and end points;
- input and output;
- decision branching; and
- processing steps.

### DR-2 — Pseudocode

Create `design/paycheck_calculator.pseudo` with:

- logically ordered steps;
- appropriate indentation;
- appropriate pseudocode keywords; and
- decision branching that accounts for all input values covered by the stated pay rules.

### DR-3 — Design Consistency

The flowchart and pseudocode should represent the same required input, decision logic, processing, and output.

## 3. Technology and File Constraints

- **TC-1:** The flowchart deliverable shall remain a Draw.io file (`.drawio`).
- **TC-2:** The pseudocode deliverable shall remain a pseudocode text file (`.pseudo`).
- **TC-3:** Python construction and testing are optional practice and are not graded Module Three deliverables.

## 4. Verification Cases

A design is ready for final review when it can be followed through the stated pay rules and produces the expected paycheck for representative and boundary cases.

The 60-hour case is the example in the official assignment. The other cases below are **repository learning checks derived from the same requirements**. They do not add new graded requirements or prescribe an output format.

| Hours worked | Expected weekly paycheck | Why this case is useful |
| ---: | ---: | --- |
| 20 | $400 | Regular-hours case |
| 40 | $800 | Boundary: all hours use the regular rate |
| 41 | $830 | First hour above the regular-hours boundary |
| 60 | $1,400 | Official assignment example |

These cases can be traced through either design before optional Python code exists.

## 5. Out of Scope Unless Your Instructor Adds a Requirement

The Module Three Assignment Guidelines and Rubric does **not** specify requirements for:

- rejecting negative values;
- limiting the maximum number of hours;
- re-prompting after invalid input;
- payroll deductions or taxes;
- exact prompt wording; or
- exact currency formatting of optional Python output.

Do not add these as graded requirements unless your instructor or current course materials direct you to do so.

## 6. Requirements Traceability

Use this table to see where the requirements are addressed without revealing a completed solution.

| Requirement | Design evidence to look for |
| --- | --- |
| FR-1 | Input appears in both the flowchart and pseudocode. |
| FR-2 | Regular-pay processing is represented where applicable. |
| FR-3 | Overtime-pay processing is represented where applicable. |
| FR-4 | A decision separates the pay-rule cases. |
| FR-5 | The design produces one total weekly paycheck. |
| FR-6 | The calculated paycheck is output. |
| DR-1 | The flowchart uses appropriate symbols and arrows. |
| DR-2 | The pseudocode uses ordered, indented steps and appropriate keywords. |
| DR-3 | Both graded artifacts describe the same planned behavior. |

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Three Paycheck Calculator Software Requirements Specification
* Artifact Type: Provided requirements reference
* Artifact Purpose: Reorganize official assignment requirements into an SRS without adding requirements.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
