# Vision: find the game and see obstacles

## Metadata

| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [872bd57] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-007 Go, stand-in, not independent | [872bd57] |

---

## Purpose

Build and test the part of the bot that looks: find the game on a screenshot and tell whether an obstacle is ahead.

## Target Date

2026-11-25

## Deliverable

The domain layer (`Box`, `Frame`, `GameArea`, `find_game_area`, `is_collision`) with unit tests on generated pictures

## Business Case Objectives

OBJ-1, OBJ-2, OBJ-3

## Owner and Reviewer

Owner: S01. Approving reviewer: S01.

## Dependencies

MIL-003, MIL-002

## Go/No-Go Criteria

- All unit tests pass without a screen; line coverage of the domain layer at least 90 %
- The game is found at scale 1 and at other scales, in day and in night colours
- A cactus in the box gives `is_collision` true; an empty box and a bird above the box give false
- opengrep reports 0 findings; code review against `qc-programming-python.md` is `Go`

## Branch and Pull Request

One branch `milestone/mil-004-vision` and one pull request that closes the issues of the tasks below.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Pictures and boxes | `Box` and `Frame` value objects: crop, rows, background colour | Yes | UC-001 |
| 2 | Find the game | `find_game_area`: the row with the most ink pixels is the ground line; its width gives the scale | Yes | UC-001 BR-1 |
| 3 | See obstacles | `GameArea.detection_box` and `is_collision`: pixels that differ from the background | Yes | UC-001 BR-2, BR-3 |
| 4 | Unit tests for the vision | Tests with generated pictures: scales, night mode, cactus, bird, noise, errors | Yes | UC-001 |
| 5 | Screenshot and wiki step page | Screenshot of the detection box on a real game picture, README step list and a wiki step page in en, da and ms | No | CN-007 |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[872bd57]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/commit/872bd573e49894903f1a134950ab479d0e78c47b
