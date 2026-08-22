<!--
MAINTAINER NOTE:
This filename intentionally contains a Cyrillic capital IE: Е (U+0415)
instead of the ASCII capital E: E (U+0045).

It is visually similar to README.md, but GitHub does not treat it as the
special .github/README.md file that would override the repository-root README.

Do not "correct" the filename unless this behavior is no longer desired.
-->

# About the `.github` Folder

> [!IMPORTANT]
> Do **not** modify or delete the `.github/` folder or any files in it. This
> folder is for repository administration. It is not part of the student
> procedures or graded deliverables for this assignment.

## What Is Here?

This repository uses `.github/` for GitHub-specific configuration:

- `ISSUE_TEMPLATE/` — forms for reporting a repository problem or requesting
  an improvement
- `ci/` — scripts used by the automated repository checks
- `workflows/tests.yml` — the active **Assignment Checks** workflow
- `workflows/tests.yml.disabled` — an intentionally disabled optional Python
  practice-test workflow retained for maintainers
- `social-preview.png` — the repository social-preview image

The active Assignment Checks protect the repository and verify the two graded
design artifacts at a basic file/structure level. They do **not** grade the
quality of a student's flowchart or pseudocode and do not run the optional
Python acceptance tests.

For additional information about the `.github` folder, see the
[Module One Setup Tasks `.github` README](https://github.com/GC-STEM/it140-m1-setup-tasks/blob/main/.github/R%D0%95ADME.md).

## Issue or Assignment Question?

Use a GitHub Issue for a technical problem with the provided repository,
documentation, starter files, automated checks, or course tools.

Do **not** use an Issue to request or post a completed solution to the graded
flowchart or pseudocode.

Questions about assignment requirements, grading, submissions, deadlines,
accommodations, or instructor feedback belong with your instructor in D2L
Brightspace.
