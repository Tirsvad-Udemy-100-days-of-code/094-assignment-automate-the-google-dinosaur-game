# Baseline: plan the bot

## Metadata

| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | pending |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-004 Go, stand-in, not independent | pending |

---

## Purpose

Agree why and how the project is built: Business Case, Stakeholder Analysis, Project Plan and the milestones, so every later step has an accepted plan to follow.

## Target Date

2026-11-22

## Deliverable

BC-001, SA-001, PP-001 and MIL-001 to MIL-006, each with a `Go` review record

## Business Case Objectives

OBJ-1 to OBJ-5 (sets up all of them)

## Owner and Reviewer

Owner: S01. Approving reviewer: S01.

## Dependencies

none (first milestone)

## Go/No-Go Criteria

- Every artifact has an `RC-*` record with verdict `Go` against its QC checklist
- The Version History row of each artifact is `Accepted`
- The dry run of `sync-project.sh` lists 6 milestones and every task

## Branch and Pull Request

One branch `milestone/mil-001-baseline` and one pull request that closes the issues of the tasks below.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the Business Case | BC-001 with scope, measurable success criteria, risks and `Decided by default` assumptions | No | BC-001 |
| 2 | Write the Stakeholder Analysis | SA-001 with S01 to S03, power/interest grid and concern register CN-001 to CN-007 | No | SA-001 |
| 3 | Write the Project Plan and milestones | PP-001 and MIL-001 to MIL-006 with Go/No-Go criteria and tasks | No | PP-001 |
| 4 | Review the baseline | Review each artifact against its QC checklist and write the `RC-*` records | No | QC-BC-001, QC-SA-001, QC-PP-001, QC-MIL-001 |
| 5 | Create the repository and sync the plan | Set the repository description and topics, push the baseline, run `sync-project.sh --apply` for milestones and issues | No | PP-001 |
| 6 | Screenshot and wiki step page | Screenshot of this step in `docs/images/`, added to the README step list and to a wiki step page in en, da and ms that explains what was learned | No | CN-007 |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
