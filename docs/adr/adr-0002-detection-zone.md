# ADR-0002: A zone of pixels in front of the dinosaur that grows with the speed

## Metadata

| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [UC-001], [DCD-001], [ADR-0001] |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [22fd9e5] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-012 Go, stand-in, not independent | [22fd9e5] |

---

## Context

The bot must decide when to jump from a screenshot. The game speeds up from
6 to 13 game pixels per frame, and a jump lasts about half a second, so the
distance at which the jump must start grows with the speed. A first live run
with a short zone of 30 game pixels crashed after a few hundred points.

Options evaluated:

1. One zone of fixed size in front of the dinosaur.
2. A zone that starts just in front of the dinosaur and reaches further ahead as the speed grows.
3. A single probe pixel at a fixed distance (the simple solution many course solutions use).

## Decision

Option 2. The zone is measured in game pixels (600 wide) and scaled with the
measured scale of the screen. Its near edge is 4 game pixels from the dinosaur,
its far edge 75 game pixels at the start speed, growing with the speed up to
the highest speed. Its height covers a cactus and a low bird (7 to 36 game
pixels above the ground line), so bumps in the ground below it and high birds
above it are not seen. The zone counts as having an obstacle when at least 3
of its pixels differ from the most common grey value of the zone by at least 60.
The speed is estimated from the seconds since the start, because the bot sees
only pixels.

Tuning the far edge from 30 to 75 game pixels raised the score of the headless
runs from a few hundred to about 2300 in good runs; the score varies a lot from run to run.

## Consequences

Positive:

- One rule works at any scale and in day and night colours (BC-001 SC-2).
- The rule is a pure function of a picture and a number, tested with generated pictures (Maintainability).
- Few pixels are captured per look, so the bot looks about fifteen times a second in a headless Chrome and faster on the desktop (Performance Efficiency).

Negative:

- The speed is estimated from time, so a game that speeds up differently needs new constants (BC-001 R-1).
- A zone that reaches far can see the next obstacle early and jump twice; the cool-down of 0.15 seconds and the length of the jump keep this harmless.
- High birds are not handled: the bot never ducks (BC-001 AS-2).

## Affected Artifacts

- [UC-001]
- [DCD-001]
- [ADR-0001]

---

[BC-001]: ../business-case.md
[UC-001]: ../use-cases/uc-001-play-the-game/uc.md
[DCD-001]: ../dcd.md
[ADR-0001]: ./adr-0001-pixels-with-pillow-and-pyautogui.md
[22fd9e5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/commit/22fd9e5af17649b055d03cce46d18e7167108810
