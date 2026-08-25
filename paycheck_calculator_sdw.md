<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Software Development Worksheet (SDW)

- **Course:** IT 140 - *Introduction to Scripting*
- **Activity:** Module Three Assignment
- **Program:** Paycheck Calculator

> Use this worksheet as optional working notes while you move through the **Analyze** and **Design** phases of the simplified Software Development Life Cycle (SDLC).
>
> Your notes do not need to be formal or polished. Keep your answers brief and write them in your own words. The purpose of the SDW is to help you understand the requirements and plan your own graded design.
>
> Look for **TODO** prompts. Replace them with your own answers if you use this worksheet.
>
> **This worksheet is not a graded deliverable.** Do not submit it in D2L Brightspace unless your instructor specifically asks for it.

## How to Use This Worksheet

> The worksheet uses the same pattern throughout:
>
> - **Where to look** tells you where to find the information you need.
> - **Prompt** tells you what to think about or answer.
> - Your response goes immediately after the prompt.
>
> The worksheet intentionally asks questions instead of supplying the completed paycheck algorithm. Your graded flowchart and pseudocode should contain **your** design.

# Analyze Phase

**Required assignment progress:** [0 Start Here](README.md) → **1 Analyze** → [2 Design](design/README.md) → [3 Submit](README.md#3-submit-your-assignment)

> During Analyze, focus on **what the program must do**. Use the official assignment and the SRS as your primary sources.

## 1. Review the Requirements

> **Where to look:**
>
> - [ ] Module Three Assignment Guidelines and Rubric in D2L Brightspace
> - [ ] [Software Requirements Specification (SRS)](analysis/paycheck_calculator_srs.md)
>   - `## 0. General Description`
>   - `## 1. Functional Requirements`
>   - `## 2. Design Requirements`
>   - `## 3. Technology and File Constraints`
>   - `## 4. Verification Cases`
>   - `## 5. Out of Scope Unless Your Instructor Adds a Requirement`

## 2. Program Purpose

> **Where to look:** official assignment problem statement and SRS `## 0. General Description`
>
> **Prompt:** In one or two sentences, what is the paycheck calculator supposed to accomplish?
>
> Write this in your own words. Do not describe how you will code it yet.

TODO: Replace this text with your brief statement of the program's purpose.

## 3. Inputs, Processing, and Outputs

> Think about the solution as three basic parts:
>
> **Input → Processing → Output**

### 3.1 IPO: Input

> **Where to look:** SRS `## 1. Functional Requirements`, especially **FR-1**
>
> **Prompt:** What information must the planned program obtain before it can calculate weekly pay?

TODO: Identify the required input in your own words.

> **Prompt:** Does the official assignment specify an exact data type or exact prompt wording for this input? If not, write **Not specified** rather than inventing a requirement.

TODO: Record what is specified and what is not specified.

### 3.2 IPO: Processing

> **Where to look:** SRS requirements **FR-2** through **FR-5**
>
> **Prompt:** What business rules and calculations must the solution represent before it can produce the result? Describe the rules in words without writing the final branch condition or completed pseudocode.

1. TODO: Describe the regular-pay rule.
2. TODO: Describe the overtime-pay rule.
3. TODO: Describe why the solution needs a decision.
4. TODO: Describe what the solution ultimately calculates.

### 3.3 IPO: Output

> **Where to look:** SRS **FR-6** and the official assignment prompt
>
> **Prompt:** What result must the program produce?

TODO: Identify the required output.

> **Prompt:** Does the assignment require exact wording, a dollar sign, or a particular number of decimal places? If the source does not say so, write **Not specified**.

TODO: Record the output-format requirement or write Not specified.

## 4. Requirements in My Own Words

> Explain selected requirements briefly in your own words. The goal is to confirm that you understand the requirement before designing a solution.

### 4.1 FR-2 — Regular Pay

> **Where to look:** [SRS](analysis/paycheck_calculator_srs.md) → **FR-2**
>
> **Prompt:** What does the regular-pay requirement mean in your own words?

TODO: Replace with your explanation.

### 4.2 FR-3 — Overtime Pay

> **Where to look:** [SRS](analysis/paycheck_calculator_srs.md) → **FR-3**
>
> **Prompt:** What does the phrase **above 40 hours** mean for the overtime rule?

TODO: Replace with your explanation.

### 4.3 FR-4 — Select the Applicable Calculation

> **Where to look:** [SRS](analysis/paycheck_calculator_srs.md) → **FR-4** and relevant Module Three decision-branching content
>
> **Prompt:** Why does the design need decision branching?

TODO: Replace with your explanation without writing the finished branch condition.

### 4.4 FR-6 — Output Weekly Pay

> **Where to look:** [SRS](analysis/paycheck_calculator_srs.md) → **FR-6**
>
> **Prompt:** What information must be available before the program can output the final result?

TODO: Replace with your explanation.

## 5. Boundary and Verification Cases

### 5.1 Understand the Boundary

> A **boundary value** is a value where program behavior changes from one case to another.
>
> **Where to look:** official assignment pay rules and SRS `## 4. Verification Cases`
>
> **Prompt:** Why is exactly 40 hours an important value to check?

TODO: Explain the 40-hour boundary in your own words.

### 5.2 Hand-Check the Official Example

> **Where to look:** the 60-hour example in the official assignment
>
> **Prompt:** Follow the example and explain why it results in the paycheck shown by the assignment. Use your own words; this is a requirements-understanding check, not your pseudocode.

TODO: Record your brief explanation of the 60-hour example.

### 5.3 Predict Other Cases

> Use the stated pay rules to predict the results below before creating your final design.

| Hours worked | What pay-rule case applies? | Expected weekly paycheck |
| ---: | --- | ---: |
| 20 | TODO | TODO |
| 40 | TODO | TODO |
| 41 | TODO | TODO |

> Compare your results with the [SRS verification cases](analysis/paycheck_calculator_srs.md#4-verification-cases). If they differ, revisit the pay rules before designing.

## 6. Constraints and Scope

> **Where to look:** SRS `## 3. Technology and File Constraints` and `## 5. Out of Scope Unless Your Instructor Adds a Requirement`
>
> **Prompt:** Identify the two files you must submit and their required file types.

1. TODO: Flowchart deliverable and file type.
2. TODO: Pseudocode deliverable and file type.

> **Prompt:** Identify two behaviors the assignment does **not** require. This helps prevent accidental extra requirements.

1. TODO: First behavior that is not required.
2. TODO: Second behavior that is not required.

## 7. Analyze Checkpoint

Before continuing, verify:

- [ ] I can explain the program's purpose in my own words.
- [ ] I identified the required input, processing, decision, and output.
- [ ] I understand the regular and overtime pay rules.
- [ ] I understand why exactly 40 hours is a boundary case.
- [ ] I checked the official 60-hour example.
- [ ] I can distinguish stated requirements from behaviors the assignment does not require.
- [ ] I know which two files are graded and submitted.
- [ ] I am ready to design without beginning with Python code.

# Design Phase

**Required assignment progress:** [0 Start Here](README.md) → [1 Analyze](analysis/README.md) → **2 Design** → [3 Submit](README.md#3-submit-your-assignment)

> During Design, focus on **how the planned program will meet the requirements**. Unlike Module Two, the design is not provided for you. Your flowchart and pseudocode are the graded work you create.

## 8. Review the Design Guidance

> **Where to look:**
>
> - [ ] [Design Phase instructions](design/README.md)
> - [ ] [Software Design Document (SDD)](design/paycheck_calculator_sdd.md)
> - [ ] [SRS](analysis/paycheck_calculator_srs.md)
> - [ ] Draw.io template **README**, **Symbols**, and **Snippets** tabs
> - [ ] Pseudocode starter comments and TODO prompts

Remember:

> **Requirements = what the program must do**
>
> **Design = how you plan for the program to do it**

## 9. Flowchart Plan

> **Where to look:** official flowchart requirements and SDD `## 4. Flowchart Design`
>
> **Prompt:** List the kinds of flowchart steps your solution needs in rough order. Use general descriptions here rather than writing the final content for each shape.

1. TODO: First kind of step.
2. TODO: Next kind of step.
3. TODO: Continue as needed.

> **Prompt:** Which required symbol types will you need?

- [ ] Start/End
- [ ] Input/Output
- [ ] Decision
- [ ] Process

## 10. Decision and Branch Plan

> **Where to look:** SRS **FR-2**, **FR-3**, and **FR-4**; SDD `## 3. Boundary to Represent`
>
> **Prompt:** In words, what question must the planned program answer to decide which processing path to follow? Do not write Python syntax.

TODO: Describe the decision in words.

> **Prompt:** What must be different about the processing on the two paths? Keep this as a high-level plan rather than completed pseudocode.

- **One path:** TODO: Describe the purpose of the processing on this path.
- **Other path:** TODO: Describe the purpose of the processing on this path.

> **Prompt:** What must be true after either path finishes so the program can continue to the output?

TODO: Describe the common result that must be available.

## 11. Pseudocode Plan

> **Where to look:** official pseudocode requirements and `design/paycheck_calculator.pseudo`
>
> **Prompt:** Which pseudocode keywords are likely to help express your design? Record only keywords you actually plan to use.

TODO: List useful pseudocode keywords such as INPUT, LET, IF, ELSE, OUTPUT, or others supported by your design.

> **Prompt:** How will indentation help a reader see which steps belong to each decision path?

TODO: Explain the indentation plan in one sentence.

## 12. Requirements-to-Design Traceability

> After you create both graded files, locate where each requirement is represented. Do not copy the full design into this table; briefly identify the location or step.

| Requirement | Flowchart evidence | Pseudocode evidence |
| --- | --- | --- |
| FR-1 — Obtain hours worked | TODO | TODO |
| FR-2 — Apply regular pay | TODO | TODO |
| FR-3 — Apply overtime pay | TODO | TODO |
| FR-4 — Select applicable calculation | TODO | TODO |
| FR-5 — Calculate weekly pay | TODO | TODO |
| FR-6 — Output weekly pay | TODO | TODO |

## 13. Trace a Boundary Case Through Both Designs

> **Where to look:** SRS verification cases
>
> Choose exactly 40 hours or another boundary-relevant case and trace it through both completed designs.

**Case selected:** TODO

### Flowchart trace

TODO: Briefly list the sequence of your flowchart steps for this case.

### Pseudocode trace

TODO: Briefly list the sequence of your pseudocode steps for this case.

### Result comparison

> **Prompt:** Do both designs take equivalent logical paths and produce the same expected result?

TODO: Write Yes or No. If No, revise the design files before continuing.

## 14. Compare the Graded Designs

After both files are complete:

- [ ] Same required input
- [ ] Same decision logic
- [ ] Same treatment of the 40-hour boundary
- [ ] Same regular-pay processing
- [ ] Same overtime-pay processing
- [ ] Same final weekly-pay result
- [ ] Same required output

If any item differs, revise one or both graded files until they represent the same planned program.

## 15. Rubric Review

### Flowchart

- [ ] My steps are organized in a logical sequence.
- [ ] I use appropriate symbols for Start/End, input/output, decisions, and processing.
- [ ] I use arrows to make the program flow clear.
- [ ] My design represents the paycheck requirements.

### Pseudocode

- [ ] My steps are logically ordered.
- [ ] My indentation shows branch structure.
- [ ] I use appropriate pseudocode keywords.
- [ ] My branching accounts for all input values covered by the stated pay rules.
- [ ] My design represents the paycheck requirements.
- [ ] No starter TODO prompts remain in the graded pseudocode.

## 16. Ready to Submit

Before leaving the graded path:

- [ ] I reviewed both files against the current Guidelines and Rubric.
- [ ] I compared the flowchart and pseudocode side by side.
- [ ] I traced at least one boundary-relevant case through both designs.
- [ ] I saved both files in their required formats.
- [ ] I committed and pushed a current backup to my personal GitHub repository.
- [ ] I understand that GitHub Assignment Checks do not assign a grade or submit the assignment.

Return to [Submit Your Assignment](README.md#3-submit-your-assignment).

# Optional Construct and Test Notes

Complete the remaining sections only if you choose to continue through the full simplified SDLC after your graded designs are ready.

## 17. Construct — Optional Practice

> Open [Construct Phase](src/README.md) and use **your completed flowchart and pseudocode** as the plan for `src/paycheck_calculator.py`.

### 17.1 Design-to-Code Mapping

| Design idea | Python concept you used |
| --- | --- |
| Input | TODO |
| Decision | TODO |
| Processing | TODO |
| Output | TODO |

### 17.2 Construction Checkpoint

- [ ] I completed the graded flowchart and pseudocode before optional coding.
- [ ] My Python program follows my own design.
- [ ] I used only Module Three-level concepts needed by the design.
- [ ] I ran after small changes and corrected syntax errors incrementally.

## 18. Test — Optional Practice

> Open [Test Phase](tests/README.md) only if you constructed the optional Python program.

### 18.1 Manual Test Notes

| Hours worked | Expected result | Actual result | Pass? |
| ---: | ---: | ---: | :---: |
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

### 18.2 Debugging Notes

> **Prompt:** If a test did not pass, what did you change in the design or implementation?

TODO: Record a brief debugging note, or write `No changes needed`.

### 18.3 Final SDLC Check

- [ ] Analyze: I understand the requirements.
- [ ] Design: My graded flowchart and pseudocode meet the assignment requirements.
- [ ] Construct (optional): My code follows my design.
- [ ] Test (optional): I checked the code with multiple cases.

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Three Paycheck Calculator Software Development Worksheet
* Artifact Type: Optional working notes; not a graded deliverable
* Artifact Purpose: Scaffold requirements analysis, design planning, traceability, consistency review, and optional SDLC extension without supplying a completed graded solution.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
