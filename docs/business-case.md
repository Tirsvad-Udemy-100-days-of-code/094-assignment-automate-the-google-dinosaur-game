# Business Case: Dino Bot

## Metadata

| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [872bd57] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-001 Go, stand-in, not independent | [872bd57] |

---

## Summary

Build a small Python program that plays the Google Dinosaur Game on its own. It
looks at the pixels of the screen with Pillow, decides when a cactus or a low
bird is close, and hits the space bar with pyautogui. The project is the Day 94
assignment ("Automate the Google Dinosaur Game") of "100 Days of Code: The
Complete Python Pro Bootcamp" and is published in the organisation
`Tirsvad-Udemy-100-days-of-code` as `094-assignment-automate-the-google-dinosaur-game`.

**Recommendation: Go.** The cost is the course time budget of 200 minutes plus
documentation, there is no money at stake, and the result is a reusable,
documented example for the course community (S02, S03).

## Problem and Opportunity

The assignment asks for a script that plays a real-time game by reading the
screen, which is a good way to practise screen capture, simple image analysis
and the timing of keyboard input. Doing it with a clean structure and tests
that need no screen makes the code readable for others and safe to run in
automatic checks.

## Objectives

| ID | Objective | Stakeholder concerns |
| --- | --- | --- |
| OBJ-1 | Deliver a bot that survives a long time in the game by reading screen pixels and pressing the space bar | CN-001, CN-004 |
| OBJ-2 | Practise screen capture (Pillow), keyboard input (pyautogui) and simple pixel analysis | CN-002 |
| OBJ-3 | Publish readable, runnable, tested code with clear run instructions and only the runtime dependencies that are needed | CN-003, CN-005 |
| OBJ-4 | Document each step: README, a wiki in English, Danish and Bahasa Malaysia, a screenshot per step and a reflection journal | CN-003, CN-005, CN-007 |
| OBJ-5 | Keep personal tokens out of the repository and never drive the host desktop from a test | CN-006 |

Stakeholders and concerns are defined in [SA-001].

## Scope

### In Scope

- Find the game on the screen from its ground line, in any size and place.
- Look at a small box of pixels in front of the dinosaur and jump when an obstacle is in it; the box reaches further ahead as the game speeds up.
- Hit the space bar with pyautogui to start the game and to jump.
- Use the assignment's names for the two central functions: `is_collision` (is an obstacle in the pixels?) and `hit` (press a key).
- A command line `python -m dino_bot` with a countdown, a time limit and a search region.
- A headless mode that plays in a headless Chrome, so the bot can be watched without using the mouse and keyboard of the computer.
- Unit tests with pytest that need no screen, using generated pictures and fakes.
- Project files: `pyproject.toml`, `constants.py`, `.gitignore`, `.editorconfig`, `Doxyfile`, doxygen comments, `README.md` from the framework template.
- Wiki in en, da and ms, one screenshot per milestone, reflection journal.
- Repository description and topics on the git host.

### Out of Scope

- Reading the game state from the page (the bot sees only pixels; the headless mode reads the page only to stop when the dinosaur has crashed and to report the score).
- Ducking under high birds and learning from play (no machine learning).
- Games other than the dinosaur game.

## Cost-Benefit

The benefit is qualitative: a completed course step, a portfolio repository and
practice of screen automation. The cost is time only.

| Item | Estimate |
| --- | --- |
| Course time budget for the build | 200 minutes |
| Planning and review documents | 60 minutes |
| Wiki in three languages, screenshots, reflection | 90 minutes |
| Money | 0 (free, open-source tools) |

## Success Criteria

| ID | Criterion | Target |
| --- | --- | --- |
| SC-1 | The bot plays well | In a headless run the game reports a score of at least 1000 in at least one of three runs of 150 seconds |
| SC-2 | The game is found | The bot finds the game from a screenshot at 100 % and at other scales, in day and night colours; the unit tests prove it |
| SC-3 | Tests | 100 % of pytest tests pass; line coverage of `src/` at least 90 % (the desktop adapters excluded, see AS-5); no test uses the screen, the keyboard or the network |
| SC-4 | Security scan | opengrep reports 0 findings before every push |
| SC-5 | Runtime dependencies | Only Pillow and PyAutoGUI; Playwright is an optional extra for the headless mode |
| SC-6 | Documentation | Every wiki page exists in en, da and ms; one screenshot per milestone in README and wiki; reflection journal present |
| SC-7 | Delivery | One pull request per milestone, each closing its issues |

## Assumptions

Each `Decided by default` entry is a choice made where the assignment is
silent; it stays open to challenge by S01.

| ID | Assumption | Decided by default | Rejected alternative |
| --- | --- | --- | --- |
| AS-1 | The game is the copy at https://elgoog.im/t-rex/ and runs in Google Chrome; any copy of the Chrome dinosaur game with the same look works | Yes | Only the offline Chrome game |
| AS-2 | The bot hits the space bar for every jump and never ducks | Yes | Also use the down arrow for high birds |
| AS-3 | The package is called `dino_bot` and follows the clean architecture layers of the framework | Yes | One script file |
| AS-4 | "Python greater than 3.14" means `requires-python = ">=3.14"` | Yes | `>=3.15` |
| AS-5 | The code that touches the real screen and keyboard (Pillow ImageGrab, pyautogui, the headless browser) is a thin adapter that is not unit tested; it is checked by a headless live run | Yes | Test it on the host desktop (forbidden by `framework/process/gui-testing.md`) |
| AS-6 | The live check runs in a headless Chrome, not on the interactive desktop | Yes | A live run on the desktop of S01 |

## Constraints

- Python 3.14 or later in a local `.venv`; pytest for tests.
- Folder structure `src/`, `tests/`, `docs/`; constants in `constants.py`.
- Doxygen comments in the source and a `Doxyfile`.
- Tokens come from `.env`, which is never committed, imported or tested.
- opengrep runs on the Product Owner's computer before each push.
- One branch and one pull request per milestone.
- A GUI is never tested on the host desktop (`framework/process/gui-testing.md`).
- The wording rules of S01 apply to every artifact.

## Risks

| ID | Risk | Impact | Mitigation |
| --- | --- | --- | --- |
| R-1 | The game changes its look or its speed curve | The bot jumps too early or too late | All numbers are constants; the live run is repeated and the constants tuned |
| R-2 | A high-resolution screen scales the game | The detection box is in the wrong place | The scale is measured from the width of the ground line |
| R-3 | The bot reacts too slowly because screenshots are slow | The dinosaur crashes | Only a small box is captured; the box reaches further ahead as the speed grows |
| R-4 | pyautogui moves the mouse into a corner and stops (fail-safe) or keeps pressing keys | Lost control of the computer | The fail-safe stays on; the bot stops cleanly and reports it; a time limit option exists |
| R-5 | A token is committed | Account misuse | `.env` in `.gitignore`, opengrep and the pre-commit hook before push |

## Methodology

ISO/IEC 25010:2023 quality characteristics in the QC checklists, Larman-style
use case and design artifacts, and the plan-first gate of the framework
(`framework/process/plan-first-gate.md`).

---

[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
[872bd57]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/commit/872bd573e49894903f1a134950ab479d0e78c47b
