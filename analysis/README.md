<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Analyze Phase | Understand the Paycheck Requirements

**Required assignment progress:** [0 Start Here](../README.md) → **1 Analyze** → [2 Design](../design/README.md) → [3 Submit](../README.md#3-submit-your-assignment)

**Optional SDLC practice after Design:** [Construct](../src/README.md) → [Test](../tests/README.md)

## Purpose

During the Analyze phase, your goal is to understand **what the paycheck calculator must do** before deciding how to represent the solution in a flowchart or pseudocode.

The **Module Three Assignment Guidelines and Rubric in D2L Brightspace** is the official source for assignment requirements. The provided [Software Requirements Specification (SRS)](paycheck_calculator_srs.md) reorganizes those requirements into a software-development format so you can examine them systematically.

The Analyze phase does not create a graded deliverable. It prepares you to create the graded flowchart and pseudocode during Design.

## Deliverable

**This phase does not produce a graded or submitted file.**

You may record brief working notes in the [Software Development Worksheet (SDW)](../paycheck_calculator_sdw.md). The SDW is a learning aid and is not submitted unless your instructor specifically asks for it.

## What You Will Use

Use these materials:

- **Module Three Assignment Guidelines and Rubric** in D2L Brightspace — official assignment and grading requirements
- [Paycheck Calculator SRS](paycheck_calculator_srs.md) — organized requirements reference
- [Software Development Worksheet (SDW)](../paycheck_calculator_sdw.md) — optional guided working notes

Relevant zyBooks topics include:

- **3.1 If-else branches (general)**
- **3.2 If-else statement**
- **3.4 Equality and relational operators**
- **3.5 Boolean operators and expressions**
- **3.8 Code blocks and indentation**

## What You Will Do

### 1. Read the Official Assignment

Read the complete Module Three Assignment Guidelines and Rubric before working from the repository guidance.

Identify what the assignment says about:

- the employee's input;
- the regular hourly rate;
- the overtime hourly rate;
- the boundary between regular and overtime hours;
- the required result;
- the required flowchart elements; and
- the required pseudocode qualities.

### 2. Read the SRS

Open the [SRS](paycheck_calculator_srs.md) and read it from beginning to end.

Pay particular attention to:

- `## 1. Functional Requirements`
- `## 2. Design Requirements`
- `## 3. Technology and File Constraints`
- `## 4. Verification Cases`
- `## 5. Out of Scope Unless Your Instructor Adds a Requirement`

### 3. Identify Input, Processing, and Output

Think about the required behavior as:

> **Input → Processing → Output**

Identify:

- what information the program receives;
- what calculations the program must perform;
- where a decision is needed; and
- what result the program produces.

Record these ideas in the Analyze section of the [SDW](../paycheck_calculator_sdw.md), if useful.

### 4. Interpret the Pay Rules Carefully

The assignment states that:

- the first 40 hours use the regular rate; and
- the overtime rate applies to each hour **above 40 hours**.

That language makes **40 hours a boundary value**. A design should treat exactly 40 hours consistently with the first rule and hours greater than 40 consistently with the overtime rule.

Use the SDW to explain the boundary in your own words before writing a branch condition.

### 5. Distinguish Requirements From Design Decisions

During Analyze, focus on what is required rather than immediately deciding how to write the final branch or calculation.

> [!IMPORTANT]
> Do not add requirements that are not stated in the assignment. For example, the assignment does not specify how negative input must be handled, whether the program must re-prompt after invalid input, or an exact currency-output format.

Those behaviors should not become graded requirements unless your instructor or current course materials add them.

### 6. Review Verification Cases

The SRS includes a few numeric cases derived from the stated pay rules. Use them to check your understanding of the requirements.

The 60-hour case comes directly from the assignment example. The other cases are repository learning checks derived from the same rules; they do not add new assignment requirements.

### 7. Complete the Analyze Checkpoint

Use the checkpoint in the SDW before moving to Design.

## Check Your Work

Before continuing, make sure:

- [ ] I read the complete Module Three Assignment Guidelines and Rubric.
- [ ] I read the complete SRS.
- [ ] I can explain the paycheck calculator's purpose in my own words.
- [ ] I identified the required input, processing, decision, and output.
- [ ] I understand why 40 hours is an important boundary.
- [ ] I can distinguish the assignment requirements from optional design or implementation choices.
- [ ] I did not add input-validation, formatting, or other requirements that the assignment does not state.
- [ ] I am ready to create two design representations of the same solution.

## Help and Support

If you have difficulty completing this phase:

- Review the [SRS](paycheck_calculator_srs.md) first.
- See the [Module Three Assignment Wiki](https://github.com/GC-STEM/it140-m3-assignment/wiki) for supplemental explanations.
- Use [GitHub Discussions](https://github.com/GC-STEM/it140-m3-assignment/discussions) for questions about the repository or provided analysis materials.
- Use [GitHub Issues](https://github.com/GC-STEM/it140-m3-assignment/issues) to report a technical problem with repository files or tools.
- Contact your instructor through D2L Brightspace for assignment requirements, grading, or feedback.

## Next Step

When you can explain the requirements without writing the finished solution, continue to the [Design Phase](../design/README.md).

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Three Assignment | Analyze Phase
* Artifact Type: Required assignment guidance; no Analyze-phase deliverable submitted for grading
* Artifact Purpose: Guide students through understanding the paycheck-calculator requirements before creating the graded design.
* Artifact Description: Students review the official assignment and SRS, identify IPO and decision requirements, interpret the 40-hour boundary, and distinguish stated requirements from unstated behaviors.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
