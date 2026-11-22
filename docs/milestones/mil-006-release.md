# Release: documentation and version 1.0.0

## Metadata

| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [872bd57] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-009 Go, stand-in, not independent | [872bd57] |

---

## Purpose

Finish the documentation and publish the result, so coursists and viewers can run and learn from the project.

## Target Date

2026-11-28

## Deliverable

The complete wiki in en, da and ms, the reflection journal, the final README and a tagged release

## Business Case Objectives

OBJ-3, OBJ-4

## Owner and Reviewer

Owner: S01. Approving reviewer: S01.

## Dependencies

MIL-005

## Go/No-Go Criteria

- Every wiki page exists in en, da and ms and passes `QC-WIKI-001`
- README shows one screenshot per milestone and passes `check-readme.sh`
- The reflection journal answers the questions of the assignment
- Repository description and topics are set; all issues of MIL-001 to MIL-006 are closed

## Branch and Pull Request

One branch `milestone/mil-006-release` and one pull request that closes the issues of the tasks below.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the reflection journal | How the project was approached, what was hard, what was easy, what to improve and the biggest learning; in `docs/reflection.md` and a wiki page in en, da and ms | No | CN-001, CN-007 |
| 2 | Complete the wiki in three languages | Check every page set in en, da and ms against `QC-WIKI-001`; update `_Sidebar` | No | CN-007 |
| 3 | Finish the README | Final screenshots, step list and links | No | CN-003, CN-005 |
| 4 | Publish | Check description and topics, set version 1.0.0, tag `v1.0.0` | No | CN-005 |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[872bd57]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/commit/872bd573e49894903f1a134950ab479d0e78c47b
