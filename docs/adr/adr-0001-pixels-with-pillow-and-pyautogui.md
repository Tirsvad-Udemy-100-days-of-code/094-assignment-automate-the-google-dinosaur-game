# ADR-0001: See with Pillow, act with pyautogui, check live in a headless Chrome

## Metadata

| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [UC-001], [DCD-001] |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [0287dd0] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-011 Go, stand-in, not independent | [0287dd0] |

---

## Context

UC-001 needs a bot that sees the game and presses a key. The assignment names
two tools: Pillow for the pixels of the screen and pyautogui for the keyboard.
BC-001 AS-6 and the framework rule in `process/gui-testing.md` forbid testing a
GUI on the host desktop, so the project also needs a way to check the bot live
without taking the mouse and keyboard of S01.

Forces: the assignment's tools (CN-003), few runtime dependencies (CN-005),
reaction time, tests that need no screen (CN-006), and a live check that does
not use the desktop.

Options evaluated:

1. Pillow `ImageGrab` for the screen and pyautogui for the key, behind small interfaces, plus an optional Playwright adapter that plays in a headless Chrome.
2. OpenCV template matching to recognise the cactus and the dinosaur.
3. Read the game state from the page (the Chrome dinosaur game exposes its runner object) and press keys through a browser driver.

## Decision

The bot sees only pixels, taken with Pillow, and acts only with pyautogui
(option 1). Both sit behind the interfaces `ScreenSource` and `Keyboard`, so the
use case and its tests know no screen. Playwright is an optional extra
(`headless`) that implements the same two interfaces for a headless Chrome; it
is used for the live check and for the documentation screenshots. It also reads
two values from the page, whether the dinosaur has crashed and the score, only
to stop a headless run and to report it, never to decide a jump.

## Consequences

Positive:

- The runtime dependencies are the assignment's two tools (Flexibility, CN-005).
- The rules work on plain bytes and are tested without a screen (Maintainability, CN-006).
- The live check does not use the desktop (Safety, CN-006).

Negative:

- Pillow screenshots are slower than reading the page, so only a small zone is captured (see ADR-0002).
- The desktop adapters are thin and not unit tested; they are checked by the headless run (BC-001 AS-5).
- A headless run uses the browser's own screenshots, not `ImageGrab`, so the desktop screen adapter is not exercised by it.

## Affected Artifacts

- [UC-001]
- [DCD-001]

---

[BC-001]: ../business-case.md
[UC-001]: ../use-cases/uc-001-play-the-game/uc.md
[DCD-001]: ../dcd.md
[0287dd0]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/commit/0287dd0a7f6e9ec9ce16250a06ea46cd968f2175
