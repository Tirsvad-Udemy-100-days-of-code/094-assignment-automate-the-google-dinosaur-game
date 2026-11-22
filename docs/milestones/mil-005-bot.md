# Bot: jump, start and run

## Metadata

| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [872bd57] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-008 Go, stand-in, not independent | [872bd57] |

---

## Purpose

Connect the vision to the keyboard and run the bot, on the desktop and in a headless Chrome.

## Target Date

2026-11-26

## Deliverable

`python -m dino_bot` plays the game; the use case, the desktop and headless adapters and the command line, with tests

## Business Case Objectives

OBJ-1, OBJ-2, OBJ-3, OBJ-5

## Owner and Reviewer

Owner: S01. Approving reviewer: S01.

## Dependencies

MIL-004

## Go/No-Go Criteria

- Unit and integration tests pass with fakes; no test uses the screen, the keyboard or the network
- A headless run reaches a score of at least 1000 in at least one of three runs
- The fail-safe of pyautogui stops the bot cleanly
- opengrep reports 0 findings; code review against `qc-programming-python.md` is `Go`

## Branch and Pull Request

One branch `milestone/mil-005-bot` and one pull request that closes the issues of the tasks below.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Ports and the use case | `ScreenSource`, `Keyboard` and `Clock` ports and `play_game`: start, locate, look, jump | Yes | UC-001 |
| 2 | Desktop adapters | `DesktopScreen` (Pillow ImageGrab), `DesktopKeyboard` and `hit` (pyautogui), `SystemClock` | Yes | UC-001 |
| 3 | Headless adapter and command line | `HeadlessGame` (Playwright, optional extra) and `python -m dino_bot` with `--seconds`, `--countdown`, `--region`, `--headless` | Yes | UC-001 |
| 4 | Tests for the bot | Tests with fake screen, keyboard and clock; command line tests | Yes | UC-001 |
| 5 | Headless live run | Run the bot in a headless Chrome, tune the constants, keep the evidence for the README | Yes | UC-001 |
| 6 | Screenshot and wiki step page | Screenshot of a headless run, README step list and a wiki step page in en, da and ms | No | CN-007 |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[872bd57]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/commit/872bd573e49894903f1a134950ab479d0e78c47b
