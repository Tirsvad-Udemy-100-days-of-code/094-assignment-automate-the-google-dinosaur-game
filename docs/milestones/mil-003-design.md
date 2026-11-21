# Design: play the game from pixels

## Metadata

| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | pending |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-006 Go, stand-in, not independent | pending |

---

## Purpose

Decide how the bot sees and acts before any code is written: the use case, the main decisions, the concepts and the classes.

## Target Date

2026-11-24

## Deliverable

UC-001, DM-001 and DCD-001, and ADRs for the pixel approach and the detection box, each with a `Go` review

## Business Case Objectives

OBJ-1, OBJ-3

## Owner and Reviewer

Owner: S01. Approving reviewer: S01.

## Dependencies

MIL-001

## Go/No-Go Criteria

- UC-001, ADR-0001, ADR-0002, DM-001 and DCD-001 have an `RC-*` record with verdict `Go`
- The DCD maps every concept of the DM to a design element
- Every dependency in the DCD points inward (domain, application, infrastructure)

## Branch and Pull Request

One branch `milestone/mil-003-design` and one pull request that closes the issues of the tasks below.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the use case | UC-001 Play the game: fully dressed, with business rules for the detection box, the jump rhythm and the stop conditions | Yes | UC-001 |
| 2 | Decide the pixel approach | ADR-0001 Pillow and pyautogui at runtime and a headless Chrome as an optional extra | No | ADR-0001 |
| 3 | Decide the detection rule | ADR-0002 a box of pixels in front of the dinosaur that grows with the speed | No | ADR-0002 |
| 4 | Model and design | DM-001 domain model and DCD-001 design class diagram | No | DM-001, DCD-001 |
| 5 | Screenshot and wiki step page | Screenshot of the design in `docs/images/`, README step list and a wiki step page in en, da and ms | No | CN-007 |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
