<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# IT 140 Module Three Assignment

- **Course:** IT 140 - *Introduction to Scripting*
- **Activity:** Module Three Assignment
- **Design problem:** Employee Paycheck Calculator
- **Graded deliverables:**
  - [`design/paycheck_calculator.drawio`](design/paycheck_calculator.drawio)
  - [`design/paycheck_calculator.pseudo`](design/paycheck_calculator.pseudo)

**Required assignment progress:** **0 Start Here** → [1 Analyze](analysis/README.md) → [2 Design](design/README.md) → [3 Submit](#3-submit-your-assignment)

**Optional SDLC practice:** [Construct](src/README.md) → [Test](tests/README.md)

> [!IMPORTANT]
> The **Module Three Assignment Guidelines and Rubric in D2L Brightspace** is the official source for assignment requirements, grading criteria, and submission requirements. This repository provides starter files, reference documents, and step-by-step guidance to help you complete those requirements.

## What You Are Doing in Module Three

In Module Two, you worked from a provided design toward a Python program. In Module Three, the focus moves earlier in the Software Development Life Cycle (SDLC): **you create the design**.

You will design a paycheck calculator that follows the company pay rules in the assignment. Your two graded files represent the same planned program in two different ways:

1. A **flowchart** shows the logic visually.
2. **Pseudocode** describes the logic as ordered, indented steps.

The repository also includes optional Python construction and testing practice so you can continue through the complete simplified SDLC:

> **Analyze → Design → Construct → Test**

For the graded Module Three assignment, however, your required path is:

> **Analyze → Design → Submit**

Construct and Test are optional practice and do not add graded deliverables.

## What You May Edit

### Graded and submitted

Edit and submit both of these files:

- [`design/paycheck_calculator.drawio`](design/paycheck_calculator.drawio) — graded flowchart
- [`design/paycheck_calculator.pseudo`](design/paycheck_calculator.pseudo) — graded pseudocode

### Working notes; not submitted

You may also edit:

- [`paycheck_calculator_sdw.md`](paycheck_calculator_sdw.md) — Software Development Worksheet (SDW) working notes

The SDW is a learning aid. It is not a graded deliverable unless your instructor specifically tells you otherwise.

### Optional practice; not submitted

After your graded designs are complete, you may edit:

- [`src/paycheck_calculator.py`](src/paycheck_calculator.py) — optional Python construction practice

The provided test file is a practice tool. Do not edit it to make a test pass.

### Course-provided reference and support files

Do not edit the SRS, SDD, README files, tests, `.github` files, repository configuration, or other course-managed files. They provide requirements, guidance, examples, checks, or configuration.

## 0. Meet the Prerequisites

Before starting this assignment:

- [ ] Complete the GitHub and Course IDE portions of the [Module One Setup Tasks](https://github.com/GC-STEM/it140-m1-setup-tasks).
- [ ] Complete the assigned Module Three zyBooks activities before relying on the assignment to teach decision branching from the beginning.
- [ ] Open the **Module Three Assignment Guidelines and Rubric** in D2L Brightspace and read the complete assignment before editing the starter files.

Relevant Module Three topics include `if`/`else` branching, relational operators, Boolean expressions, and code-block indentation.

## 1. Set Up or Open Your Assignment Repository

You create your personal `it140-m3-assignment` repository only once.

### If You Have Not Created It Yet

Use the VS Code integrated terminal. On Windows, use **PowerShell** or **Git Bash**, not Command Prompt (`cmd.exe`).

First confirm the GitHub account you use for IT 140:

```bash
gh auth status
```

If the correct account is not active, use the GitHub CLI sign-in or account-switching instructions from the Module One Setup Tasks before continuing.

Then run:

```bash
cd ~/Repos
gh auth setup-git
gh api --method PUT /user/starred/GC-STEM/it140-m3-assignment
gh repo create it140-m3-assignment --template GC-STEM/it140-m3-assignment --private --clone
cd it140-m3-assignment
git remote -v
```

Confirm that the final remote belongs to **your GitHub account**.

> [!NOTE]
> These creation commands are for the first successful setup only. If a personal repository or local folder already exists, open that existing work instead of creating another repository.

### If You Already Created It

Open VS Code and select **File > Open Folder**, then open:

```text
~/Repos/it140-m3-assignment
```

If you are on another computer and your personal repository exists on GitHub but not locally, clone your existing repository:

```bash
cd ~/Repos
gh repo clone "$(gh api user --jq .login)/it140-m3-assignment"
cd it140-m3-assignment
git status
```

## 2. Complete the Assignment

### 2.1 Analyze the Requirements

Open [Analyze Phase](analysis/README.md).

During Analyze, focus on **what** the paycheck calculator must do. Use:

- the official Guidelines and Rubric in D2L Brightspace;
- the provided [Software Requirements Specification (SRS)](analysis/paycheck_calculator_srs.md); and
- the optional [Software Development Worksheet (SDW)](paycheck_calculator_sdw.md).

Pay particular attention to the distinction between the first 40 hours and hours **above 40**. Do not add requirements such as negative-input validation or exact output formatting when the assignment does not specify them.

### 2.2 Create the Graded Designs

Open [Design Phase](design/README.md).

Complete both graded files:

1. [`design/paycheck_calculator.drawio`](design/paycheck_calculator.drawio)
2. [`design/paycheck_calculator.pseudo`](design/paycheck_calculator.pseudo)

Your flowchart and pseudocode must describe the **same planned program**. Compare them before submission and review each file against the current Guidelines and Rubric.

### 2.3 Save Your Work to GitHub

Save your files normally while you work in VS Code. Periodically commit and push your assignment work so your personal GitHub repository contains a current backup.

You can use the **Source Control** tools in VS Code or run the following from the repository root:

```bash
cd ~/Repos/it140-m3-assignment
git status
git add paycheck_calculator_sdw.md design/paycheck_calculator.drawio design/paycheck_calculator.pseudo src/paycheck_calculator.py
git commit -m "Save Module Three assignment progress"
git push
```

These commands stage only the student working, graded design, and optional practice files.

If Git reports that there is nothing to commit, your local files do not contain new changes that need to be saved to GitHub.

> [!NOTE]
> GitHub is used to develop and back up your work. **Assignment submission, grading, and instructor feedback remain in D2L Brightspace.**

### 2.4 Review the Assignment Checks

Each push runs the **Assignment Checks** workflow in your personal repository.

While you are still working, a red **X** can simply mean that one or both graded design files are still in the starter state. As you complete your work, the checks can verify basic repository conditions such as:

- required course files are still present;
- committed changes are limited to student-editable files;
- both graded design files changed from their starter state;
- the Draw.io file remains readable XML;
- the pseudocode retains its outer structure and no longer contains starter `TODO:` prompts; and
- course-provided Markdown and configuration remain internally consistent.

The Assignment Checks **do not grade the quality or correctness of your design**. A green check is not a grade and does not submit your assignment.

To review a run:

1. Open your personal repository on GitHub.
2. Select **Actions**.
3. Open the most recent **Assignment Checks** run.
4. Open **Check assignment repository** to see the results.

## 3. Submit Your Assignment

In D2L Brightspace, open the **Module Three Assignment** and follow the current submission instructions.

Submit exactly the two graded design files required by the assignment:

- [`design/paycheck_calculator.drawio`](design/paycheck_calculator.drawio)
- [`design/paycheck_calculator.pseudo`](design/paycheck_calculator.pseudo)

Do **not** submit the SDW, optional Python practice file, test file, GitHub Actions output, SRS, SDD, or repository README files unless your instructor specifically requests them.

## Optional: Continue Through Construct and Test

After both graded design files are complete and ready to submit, you may continue through the remaining SDLC phases for practice:

1. [Construct](src/README.md) — translate your own design into a small Python program.
2. [Test](tests/README.md) — manually test the program and optionally run the provided acceptance tests.

Optional practice is intended to help you connect design to implementation. It does not change the two-file Module Three submission.

## Restore or Restart Your Assignment Repository

Choose the recovery method that matches the problem. Preserve existing work whenever possible.

### Restore a Damaged Local Copy From GitHub

Use this when the copy you previously pushed to GitHub is good but the local folder is damaged or confusing.

#### CVD, Linux, macOS, or Git Bash on Windows

```bash
cd ~/Repos
mv it140-m3-assignment "it140-m3-assignment-local-backup-$(date +%Y%m%d-%H%M%S)"
gh repo clone "$(gh api user --jq .login)/it140-m3-assignment"
cd it140-m3-assignment
git status
```

#### Windows PowerShell

```powershell
cd ~/Repos
Rename-Item it140-m3-assignment "it140-m3-assignment-local-backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
gh repo clone "$(gh api user --jq .login)/it140-m3-assignment"
cd it140-m3-assignment
git status
```

### Start Over From the Current Course Template

Use this only when you intentionally want a fresh assignment copy. Preserve the old local folder and GitHub repository first.

#### CVD, Linux, macOS, or Git Bash on Windows

```bash
cd ~/Repos
backup="it140-m3-assignment-backup-$(date +%Y%m%d-%H%M%S)"
mv it140-m3-assignment "$backup"
gh repo rename "$backup" --repo "$(gh api user --jq .login)/it140-m3-assignment" --yes
gh repo create it140-m3-assignment --template GC-STEM/it140-m3-assignment --private --clone
cd it140-m3-assignment
git remote -v
```

#### Windows PowerShell

```powershell
cd ~/Repos
$backup = "it140-m3-assignment-backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
Rename-Item it140-m3-assignment $backup
gh repo rename $backup --repo "$(gh api user --jq .login)/it140-m3-assignment" --yes
gh repo create it140-m3-assignment --template GC-STEM/it140-m3-assignment --private --clone
cd it140-m3-assignment
git remote -v
```

> [!IMPORTANT]
> Starting over does not automatically copy work from the preserved repository into the new one.

## Help and Support

Use the [Module Three Assignment Wiki](https://github.com/GC-STEM/it140-m3-assignment/wiki) for supplemental explanations of the SDLC, assignment documents, flowcharts, pseudocode, course IDE tools, Git/GitHub, testing, sources, and AI use.

- Use [GitHub Discussions](https://github.com/GC-STEM/it140-m3-assignment/discussions) for questions about using this repository that do not request a completed graded solution.
- Use [GitHub Issues](https://github.com/GC-STEM/it140-m3-assignment/issues) to report a technical problem with the provided repository, starter files, documentation, automated checks, or course tools.
- Contact your instructor through D2L Brightspace for assignment requirements, grading, feedback, or course-specific questions.

Do not post your completed graded flowchart or pseudocode publicly when asking for help.

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Three Assignment Repository README
* Artifact Type: Required assignment guidance
* Artifact Purpose: Guide students through setup, analysis, design, submission, and optional SDLC practice for the Module Three Assignment.
* Artifact Description: Students create and submit a paycheck-calculator flowchart and pseudocode; optional construction and testing practice extends the assignment through the simplified SDLC without adding graded deliverables.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
