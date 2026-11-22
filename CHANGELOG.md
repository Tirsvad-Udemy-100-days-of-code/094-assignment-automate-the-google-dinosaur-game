# Changelog

## Unreleased

## 1.0.0 (2026-11-21)

First release: a bot that plays the Google Dinosaur Game by reading screen pixels with Pillow and hitting the space bar with pyautogui.

### Added

- `find_game_area`, `GameArea.detection_box` and `is_collision`: find the game from its ground line, look at a zone in front of the dinosaur that grows with the speed, and decide when to jump.
- The use case `play_game` with ports for screen, keyboard and clock, and the desktop adapters `DesktopScreen`, `DesktopKeyboard`, `hit` and `SystemClock`.
- `HeadlessGame` (optional extra `headless`) to play in a headless Chrome without using the desktop.
- The command line `python -m dino_bot` and `dino-bot` with `--seconds`, `--countdown`, `--region`, `--headless`, `--picture` and `-v`.
- Project documents, use case UC-001, two ADRs, 88 tests with 99 % coverage and a Doxygen configuration.
- Wiki in English, Danish and Bahasa Malaysia with a screenshot per step, and the reflection journal.
