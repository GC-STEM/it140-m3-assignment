# Software Development Worksheet (SDW)

- **Course**: IT 140 - Introduction to Scripting
- **Activity**: Module Three Assignment
- **Program**: Paycheck Calculator
- **Purpose**: Optional working notes for moving through the full SDLC

> [!NOTE]
> This worksheet is a learning aid. It is **not a graded deliverable** and should not be submitted unless your instructor specifically asks for it. Keep your answers brief. The graded work belongs in `design/paycheck_calculator.drawio` and `design/paycheck_calculator.pseudo`.

## SDLC Progress

> **Analyze → Design → Construct → Test**

For this assignment, **Design is the graded phase**. Construct and Test are included as optional practice so you can experience the complete sequence.

---

## 1. Analyze

Use the Module Three Assignment Guidelines and Rubric and the [`analysis/paycheck_calculator_srs.md`](analysis/paycheck_calculator_srs.md) file.

### 1.1 Purpose in Your Own Words

In one or two sentences, describe what the paycheck calculator needs to accomplish.

**Your notes:**

TODO: Write your own summary here.

### 1.2 Input

What information must the program receive before it can calculate the weekly paycheck?

**Your notes:**

TODO: Identify the required input.

### 1.3 Processing Rules

List the business rules that affect the calculation. Do not write Python code.

**Your notes:**

- TODO: Regular-pay rule
- TODO: Overtime-pay rule
- TODO: Important boundary value

### 1.4 Output

What result must the program produce?

**Your notes:**

TODO: Identify the required output.

### 1.5 Decision Point

What question must the program answer to decide which processing path to follow?

**Your notes:**

TODO: Describe the decision in words without writing code.

### Analyze Checkpoint

Before continuing, verify that you can explain:

- [ ] The required input
- [ ] The regular-pay rule
- [ ] The overtime-pay rule
- [ ] Why 40 hours is the boundary
- [ ] The required output

---

## 2. Design

The flowchart and pseudocode are the **graded deliverables**. Use this section only to plan before editing those files.

### 2.1 Flowchart Plan

Which kinds of flowchart symbols will you need? The assignment specifically identifies start/end, input/output, decision, and processing symbols.

**Your notes:**

TODO: List the kinds of steps your flowchart needs, in a rough order.

### 2.2 Branch Plan

Without writing the completed solution here, describe what must be different on the two paths created by the decision.

**Your notes:**

TODO: Describe what each path needs to accomplish.

### 2.3 Pseudocode Plan

Which pseudocode keywords will help make the order and branching clear?

**Your notes:**

TODO: List useful pseudocode keywords and how indentation will show branch structure.

### 2.4 Design Consistency

After completing both graded files, compare them.

- [ ] Same input
- [ ] Same decision
- [ ] Same branch behavior
- [ ] Same calculations
- [ ] Same output
- [ ] Same treatment of the 40-hour boundary

If any item differs, revise the design files before submitting.

---

## 3. Construct — Optional Practice

Complete this section only if you choose to implement your design in Python.

Open [`src/README.md`](src/README.md), then use your **own completed flowchart and pseudocode** to complete `src/paycheck_calculator.py`.

### 3.1 Design-to-Code Mapping

As you code, note how your design maps to Python concepts.

| Design idea | Python concept you used |
| --- | --- |
| Input | TODO |
| Decision | TODO |
| Processing | TODO |
| Output | TODO |

### 3.2 Construction Checkpoint

- [ ] I completed the graded flowchart and pseudocode before coding.
- [ ] My Python program follows my design.
- [ ] I used decision branching rather than separate unrelated programs.
- [ ] My program runs without a syntax error for a normal input value.

---

## 4. Test — Optional Practice

Complete this section only if you constructed the optional Python program.

Open [`tests/README.md`](tests/README.md).

### 4.1 Manual Test Notes

Record at least one regular-hours case and one overtime case. Include the 40-hour boundary when possible.

| Hours worked | Expected result | Actual result | Pass? |
| ---: | ---: | ---: | :---: |
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

### 4.2 Debugging Notes

If a test did not pass, what did you change?

**Your notes:**

TODO: Record a brief debugging note, or write `No changes needed`.

### 4.3 Final SDLC Check

- [ ] Analyze: I understand the requirements.
- [ ] Design: My flowchart and pseudocode meet the assignment rubric.
- [ ] Construct (optional): My code follows my design.
- [ ] Test (optional): I checked the code with multiple cases.

Return to the [top-level README](README.md#submit-your-assignment) for submission instructions.
