<!--
Draft artifact for human review.
Target repository: GC-STEM/it140-m3-assignment
Draft date: 2026-08-15
-->

# IT 140 Module Three Assignment

- **Course**: IT 140 - Introduction to Scripting
- **Activity**: Module Three Assignment
- **Design problem**: Employee Paycheck Calculator
- **Graded deliverables**: `paycheck_calculator.drawio` and `paycheck_calculator.pseudo`

**Assignment progress:** **0 Start Here** → [1 Analyze](analysis/README.md) → [2 Design](design/README.md) → [3 Construct (Practice)](src/README.md) → [4 Test (Practice)](tests/README.md) → [5 Submit](#submit-your-assignment)

## Start With the Assignment Guidelines and Rubric

Before using this repository, open the **Module Three Assignment Guidelines and Rubric** in [D2L Brightspace](https://learn.snhu.edu/).

Review the complete assignment, including:

- Overview
- Prompt
- Flowchart requirements
- Pseudocode requirements
- What to Submit
- AI Usage
- Assignment Rubric

The **Module Three Assignment Guidelines and Rubric** is the official source for assignment requirements, grading criteria, and submission requirements. This repository provides starter files, working files, and step-by-step guidance to help you complete those requirements.

> [!IMPORTANT]
> This assignment is graded on the **flowchart** and **pseudocode** you create. Writing and testing a Python program is **optional practice** and is not a graded deliverable for this assignment.

After reviewing the Guidelines and Rubric, return here to set up your personal assignment repository.

## About This Repository

This repository organizes the assignment around a simplified Software Development Life Cycle (SDLC):

> **Analyze → Design → Construct → Test**

The module materials recommend working through these phases in order. For the graded assignment, you will complete the Analyze and Design work needed to produce your two design deliverables. After your designs are complete, you are encouraged to continue through Construct and Test for additional programming practice.

> [!NOTE]
> The Codio Virtual Desktop (CVD) is the reference environment for IT 140. If you completed the [Module One Setup Tasks](https://github.com/GC-STEM/it140-m1-setup-tasks) and use the CVD for this course, Git, GitHub CLI, VS Code, Draw.io integration, pseudocode support, Python, and the expected course repository configuration should already be available. We recommend all students use the CVD for coursework to minimize environment differences and troubleshooting issues.
>
> You may also complete this assignment on a supported local computer configured through the Module One Setup Tasks. Local environments can vary, so some commands or troubleshooting steps may differ.

You will create your own personal GitHub repository from this course repository template and clone your repository to the CVD or your supported local computer. Your personal repository lets you:

- Complete your assignment work
- Save changes with Git
- Push your work to GitHub for backup
- Continue working from your own copy of the assignment
- Practice a professional repository-based development workflow

The main assignment folders are:

```text
it140-m3-assignment/
├── analysis/
│   ├── README.md
│   └── paycheck_calculator_srs.md
├── design/
│   ├── README.md
│   ├── paycheck_calculator.drawio
│   ├── paycheck_calculator.pseudo
│   └── paycheck_calculator_sdd.md
├── src/
│   ├── README.md
│   └── paycheck_calculator.py
├── tests/
│   ├── README.md
│   └── test_paycheck_calculator.py
├── paycheck_calculator_sdw.md
└── README.md
```

### What You May Edit

Your required assignment work should be limited to:

- [`design/paycheck_calculator.drawio`](design/paycheck_calculator.drawio) — **graded flowchart deliverable**
- [`design/paycheck_calculator.pseudo`](design/paycheck_calculator.pseudo) — **graded pseudocode deliverable**

You may also edit these working or practice files:

- [`paycheck_calculator_sdw.md`](paycheck_calculator_sdw.md) — recommended Software Development Worksheet (SDW) notes; not submitted for grading
- [`src/paycheck_calculator.py`](src/paycheck_calculator.py) — optional Python construction practice; not submitted for grading

Leave the READMEs, SRS, SDD, tests, repository configuration, and other provided files unchanged unless your instructor or course instructions tell you otherwise.

## Set Up Your Personal Assignment Repository

Complete these steps only once before beginning the assignment.

If you already created an `it140-m3-assignment` repository in your GitHub account or already have an `it140-m3-assignment` folder in `~/Repos`, do not repeat these setup steps. Open your existing repository instead.

If you need to start over, see [Reset Your Assignment Repository](#reset-your-assignment-repository).

### 0. Complete the Module One Setup Tasks

If you have not completed the [Module One Setup Tasks](https://github.com/GC-STEM/it140-m1-setup-tasks) on the Codio Virtual Desktop (CVD) or your local computer, do so now. Return here after completing those tasks.

### 1. Open the VS Code Integrated Terminal

In VS Code, select:

> **Terminal > New Terminal**

You will use the integrated terminal in VS Code to create and clone your personal assignment repository.

> [!IMPORTANT]
> Windows users must use a **PowerShell** or **Git Bash** terminal in VS Code to run the commands in this file. A Command Prompt (`cmd.exe`) terminal will not work.

### 2. Confirm Your GitHub Account

1. Type the following command in the VS Code integrated terminal:

   ```bash
   gh auth status
   ```

2. Review the results and identify the active account.
   - If your IT 140 GitHub account is listed but is not active, continue to Step 2.3.
   - If your IT 140 GitHub account is not listed, continue to Step 2.4.
   - If the correct IT 140 GitHub account is active, continue to Step 3.

3. If your IT 140 GitHub account is listed but is not active, type the following command, replacing `your-github-username` with your GitHub username:

   ```bash
   gh auth switch --user your-github-username
   ```

   Then return to Step 2.1 to confirm that the correct account is now active.

4. If your IT 140 GitHub account is not listed, type:

   ```bash
   gh auth login --web
   ```

   Follow the GitHub CLI prompts and sign in with the GitHub account you use for IT 140.

5. When sign-in is complete, return to Step 2.1 and check your account again.

6. Continue to Step 3 - Create and Clone Your Personal Repository.

### 3. Create and Clone Your Personal Repository

The following command block will:

1. Go to your course `Repos` folder.
2. Configure Git to use your GitHub CLI authentication.
3. Star the original IT 140 assignment repository so it is easier to find again.
4. Create your personal assignment repository in GitHub from the current course template.
5. Make your personal repository private.
6. Clone your new repository to your CVD or local computer.
7. Enter the cloned repository folder.
8. Show the GitHub repository connected to your local copy.

Copy the entire command block and paste it into the VS Code integrated terminal:

```bash
cd ~/Repos
gh auth setup-git
gh api --method PUT /user/starred/GC-STEM/it140-m3-assignment
gh repo create it140-m3-assignment --template GC-STEM/it140-m3-assignment --private --clone
cd it140-m3-assignment
git remote -v
```

Review the final output and confirm that the repository belongs to your GitHub account.

If a command reports an error, do not repeat the entire command block. Review the error message and use the [Help and Support](#help-and-support) resources before continuing.

### 4. Open Your Assignment Repository in VS Code

In VS Code:

1. Select **File > Open Folder**.
2. Open `~/Repos/it140-m3-assignment`.
3. Confirm that `it140-m3-assignment` is the top-level folder shown in the Explorer.

You are now working in your personal copy of the Module Three Assignment.

## Complete the Assignment

### 1. Analyze the Requirements

Open the [Analyze Phase instructions](analysis/README.md).

Use the assignment Guidelines and Rubric, the provided Software Requirements Specification (SRS), and the optional SDW to make sure you understand:

- The input the program must use
- The pay rules the design must represent
- The decision the program must make
- The required output
- The boundary between regular and overtime hours

Do not begin by writing Python code. The purpose of this assignment is to practice designing the solution before constructing it.

### 2. Create the Graded Designs

Open the [Design Phase instructions](design/README.md).

Complete both required design files:

1. [`design/paycheck_calculator.drawio`](design/paycheck_calculator.drawio)
2. [`design/paycheck_calculator.pseudo`](design/paycheck_calculator.pseudo)

Your flowchart and pseudocode should describe the **same solution**. Review both files against the assignment Guidelines and Rubric before continuing.

### 3. Optional Practice: Construct the Python Program

After your graded design work is complete, you are encouraged to continue to the [Construct Phase](src/README.md).

Use your own completed flowchart and pseudocode as the plan for completing `src/paycheck_calculator.py`. This practice helps connect program design to working Python code.

This file is **not required for the Module Three Assignment grade**.

### 4. Optional Practice: Test the Python Program

If you complete the optional Python program, continue to the [Test Phase](tests/README.md).

Run your program with several input values, including the 40-hour boundary, and use the provided optional acceptance tests to check your implementation.

Testing is **not required for the Module Three Assignment grade**, but it provides practice with the full SDLC and helps you see whether the design you created can be implemented successfully.

### 5. Save Your Work to GitHub

Save your files normally while you work in VS Code.

Periodically commit and push your assignment work so your personal GitHub repository contains a current backup. From the repository root in the VS Code integrated terminal, run:

```bash
cd ~/Repos/it140-m3-assignment
git status
git add paycheck_calculator_sdw.md design/paycheck_calculator.drawio design/paycheck_calculator.pseudo src/paycheck_calculator.py
git commit -m "Save Module Three assignment progress"
git push
```

These commands:

- Show which files have changed.
- Stage the student working, graded deliverable, and optional practice files for this assignment.
- Create a Git commit containing those changes.
- Push the commit to your personal GitHub repository.

If Git reports that there is nothing to commit, your local files do not contain any new changes that need to be saved to GitHub.

> [!NOTE]
> GitHub is used to develop and back up your work. Assignment submission, grading, and instructor feedback remain in D2L Brightspace.

## Return to an Existing Assignment

You only create your personal assignment repository once.

When you return to the assignment later:

1. Open VS Code.
2. Select **File > Open Folder**.
3. Open `~/Repos/it140-m3-assignment`.
4. Continue working where you stopped.

You do not need to create the repository from the template again.

If you are working on another computer that does not yet have your assignment repository, clone your existing personal repository instead of creating another repository from the template:

```bash
cd ~/Repos
gh repo clone "$(gh api user --jq .login)/it140-m3-assignment"
cd it140-m3-assignment
git status
```

Then open the cloned `it140-m3-assignment` folder in VS Code.

## Reset Your Assignment Repository

If something goes wrong, choose the recovery option that matches the problem.

### Restore Your Local Copy From GitHub

Use this option when your files on the current computer are damaged or confusing, but the copy you previously pushed to GitHub is good.

This process preserves your current local folder as a backup and then clones a fresh local copy of your personal repository.

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

Your previous local folder remains in `~/Repos` with `local-backup` and a date and time added to its name.

### Start Over From the Original Course Template

Use this option only when you want to restart the entire assignment from the original course template.

This process preserves your current work by renaming your existing local assignment folder and personal GitHub repository before creating a new copy from the current course template.

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

Your previous local folder and GitHub repository are preserved using the generated backup name.

> [!IMPORTANT]
> Starting over creates a new copy of the current assignment template. Work that exists only in your previous repository is not automatically copied into the new assignment repository.

## Help and Support

The README files contain the instructions you need to work through each SDLC phase.

The [Module Three Assignment Wiki](https://github.com/GC-STEM/it140-m3-assignment/wiki) provides supplemental information about:

- The simplified SDLC used in this assignment
- Flowcharts and pseudocode
- Working with assignment documents in VS Code
- Git and GitHub workflows
- Optional testing and debugging practice
- Sources, citations, and AI use

Use [GitHub Issues](https://github.com/GC-STEM/it140-m3-assignment/issues) to report a technical problem with the provided course repository, starter files, documentation, or course tools.

Use [GitHub Discussions](https://github.com/GC-STEM/it140-m3-assignment/discussions) for repository-related questions when appropriate. Do not ask for or post completed solutions to the graded flowchart or pseudocode.

Post questions about course content that are not specific to this repository in your section's **General Questions** discussion topic.

For questions about assignment submissions, grading, deadlines, accommodations, or instructor feedback, contact your instructor through D2L Brightspace.

## Submit Your Assignment

Return to the **Module Three Assignment Guidelines and Rubric** in [D2L Brightspace](https://learn.snhu.edu/) before submitting your work.

Confirm that:

- Your flowchart uses the required types of symbols and arrows.
- Your pseudocode uses clear steps, appropriate indentation, and appropriate keywords.
- Both design files represent the same paycheck-calculation logic.
- Your work accounts for the regular/overtime boundary described in the assignment.
- Your final files are saved in the required formats:
  - `.drawio`
  - `.pseudo`
- Your latest work is backed up in your personal GitHub repository.

Follow the **What to Submit** instructions in the Module Three Assignment Guidelines and Rubric to submit the two required design files in D2L Brightspace.

Do **not** submit the SDW, SRS, SDD, optional Python program, tests, README files, or your GitHub repository unless the Module Three Assignment Guidelines and Rubric or your instructor specifically instructs you to do so.

GitHub does not submit your assignment for grading.
