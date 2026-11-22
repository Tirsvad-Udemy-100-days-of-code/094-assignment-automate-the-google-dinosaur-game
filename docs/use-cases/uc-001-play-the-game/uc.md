# Use Case UC-001: Play the game

## Metadata

| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [SA-001], [BC-001], [MIL-003], [DM-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [6ca5d91] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-010 Go, stand-in, not independent | [6ca5d91] |

---

## Purpose

Describe the one user goal of the project: a student starts the bot and the
dinosaur runs and jumps over obstacles on its own. Answers CN-001, CN-003,
CN-004 and CN-006 for S01 and S02.

## Use Case

| Field | Value |
| --- | --- |
| Name | Play the game |
| Format | Fully Dressed |
| Scope | Dino Bot (the command-line program) |
| Level | User goal |
| Primary actor | Student (S01 or an S02 course participant who runs the bot) |

## Stakeholders and Interests

| Stakeholder | Interest |
| --- | --- |
| S01 Course participant | The assignment works end to end and practises screen capture and keyboard automation (CN-001, CN-002) |
| S02 Udemy course participants | The bot survives long, works at other screen sizes and has the assignment's function names (CN-003, CN-004) |
| S03 GitHub viewers | The code shows the idea clearly with few runtime dependencies (CN-005) |

## Preconditions

- The game is open in a browser window that is in front and not covered.
- The student can stop the bot: with `Ctrl+C`, with a time limit, or by moving the mouse to a corner of the screen.

## Postconditions

- Success: the dinosaur has jumped over the obstacles that came while the bot played. The student has been told how many jumps the bot made and for how many seconds it played.
- Failure: the student is told why the bot could not play (the game was not found on the screen); no key was pressed to jump.

## Main Success Scenario

1. The student starts the bot and, if they want, chooses a time limit, a countdown and the part of the screen to search, then brings the game to the front before the countdown ends.
2. The system hits the space bar to start the game (BR-1).
3. The system waits a moment for the game to reach its full width, takes a picture of the screen and finds the game and its scale (BR-2).
4. The system looks at the zone in front of the dinosaur; the zone reaches further ahead as the game speeds up (BR-3).
5. When something in the zone differs from the background, the system hits the space bar and the dinosaur jumps (BR-4, BR-5).
6. The system repeats steps 4 and 5 until the time limit is reached, the dinosaur has crashed, or the student stops the bot (BR-6).
7. The system tells the student the number of jumps and the seconds it played.

## Alternative Flows

- 3a. The game is not found on the screen: the system says so and stops without jumping.
- 5a. The zone shows pixels that are not an obstacle, such as a bump in the ground: bumps are below the zone and are not seen (BR-3).
- 6a. The student moves the mouse to a corner of the screen: the system stops, says so and reports the jumps so far (BR-6).
- 6b. The game runs in a headless browser and the dinosaur has crashed: the system stops and reports the score the game shows.

No step includes or extends another use case; UC-001 is the only use case.

## Business Rules

| ID | Step | Rule |
| --- | --- | --- |
| BR-1 | 2 | The space bar starts the game and makes the dinosaur jump; no other key is used (BC-001 AS-2) |
| BR-2 | 3 | The game is found from its ground line, the row with the most dark pixels; the width of the line gives the scale, so the bot works at any screen size and in night colours (BC-001 SC-2) |
| BR-3 | 4 | The zone starts just in front of the dinosaur, is as high as a cactus and low bird, and reaches 75 game pixels ahead at the start speed, more as the game speeds up (ADR-0002) |
| BR-4 | 5 | Something counts as an obstacle when at least 3 pixels of the zone differ from the background colour by a clear amount (ADR-0002) |
| BR-5 | 5 | After a jump the bot waits 0.15 seconds before it may jump again, because a key press in the air does nothing |
| BR-6 | 6 | The mouse-in-a-corner stop of pyautogui stays on, and the bot never presses a key after it has been stopped (BC-001 R-4) |

---

[SA-001]: ../../stakeholder-analysis.md
[BC-001]: ../../business-case.md
[MIL-003]: ../../milestones/mil-003-design.md
[DM-001]: ../../domain-model.md
[6ca5d91]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/commit/6ca5d91b6950a72a8010d23369b0dd84d1c1b122
