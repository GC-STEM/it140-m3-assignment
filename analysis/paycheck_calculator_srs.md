# Software Requirements Specification (SRS)

- **Course**: IT 140 - Introduction to Scripting
- **Activity**: Module Three Assignment
- **Program name**: Paycheck Calculator
- **Status**: Provided requirements reference; do not edit

## 0. General Description

The Paycheck Calculator is a small program design for calculating an employee's weekly paycheck from the number of hours worked during a week. The design must represent the company's regular-pay and overtime-pay rules and produce the employee's total weekly paycheck.

This SRS reorganizes requirements from the Module Three Assignment Guidelines and Rubric. If this file and the current Guidelines and Rubric differ, follow the Guidelines and Rubric.

## 1. Functional Requirements

The program shall:

- **1.1** Obtain the number of hours the employee worked during the week.
- **1.2** Apply a rate of **$20 per hour** to the first **40 hours** worked.
- **1.3** Apply a rate of **$30 per hour** to each hour worked **above 40 hours**.
- **1.4** Use decision branching so the appropriate pay calculation is performed for the hours worked.
- **1.5** Calculate the employee's total weekly paycheck.
- **1.6** Output the calculated weekly paycheck.

## 2. Design Requirements

The graded design shall include both of the following artifacts:

- **2.1 Flowchart**: A `.drawio` flowchart that organizes the solution using appropriate symbols and arrows for:
  - Start and end points
  - Input and output
  - Decision branching
  - Processing steps
- **2.2 Pseudocode**: A `.pseudo` file that details the solution using logically ordered steps, appropriate indentation, and appropriate pseudocode keywords.
- **2.3** The flowchart and pseudocode shall represent the same program behavior.
- **2.4** The decision logic shall account for all input values covered by the two pay rules: hours at or below the regular/overtime boundary and hours above that boundary.

## 3. Technology and File Constraints

- **3.1** The flowchart deliverable shall remain in Draw.io format (`.drawio`).
- **3.2** The pseudocode deliverable shall remain a pseudocode text file (`.pseudo`).
- **3.3** Python construction and testing are optional practice for this assignment and are not graded deliverables.

## 4. Acceptance Conditions

A design is ready for submission when it can be followed to produce the correct paycheck for ordinary and boundary cases and when it satisfies the flowchart and pseudocode criteria in the current assignment rubric.

The following numeric cases are useful for checking the design logic. They are not required output formats.

| Hours worked | Expected weekly paycheck | Purpose |
| ---: | ---: | --- |
| 20 | $400 | Regular-hours case |
| 40 | $800 | Boundary case: no overtime hours |
| 41 | $830 | First hour above the boundary |
| 60 | $1,400 | Assignment example |

## 5. Out of Scope Unless Your Instructor Adds a Requirement

The assignment Guidelines and Rubric does not specify requirements for:

- Rejecting negative values
- Limiting the maximum number of hours
- Re-prompting after invalid input
- Payroll deductions or taxes
- Exact wording or currency formatting of optional Python output

Do not add these as graded requirements unless your instructor or current course materials direct you to do so.
