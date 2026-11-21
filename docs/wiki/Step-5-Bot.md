# Step 5: Bot

🌐 **English** · [Dansk](Step-5-Bot-da) · [Bahasa Malaysia](Step-5-Bot-ms)

Milestone `MIL-005`. Branch and pull request: one for this step.

![A headless run of the bot with its score](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/05-bot-headless-run.png)

## What was done

The bot runs: the use case `play_game`, the ports for screen, keyboard and clock, the desktop adapters (`DesktopScreen` with Pillow, `hit` and `DesktopKeyboard` with pyautogui), the headless Chrome adapter and the command line `python -m dino_bot`. Tests use fakes. A first headless run died at a score of 270, so the constants were tuned; the best runs now reach 2000 and more, and the score differs from run to run.

## What was gained

- Grabbing only a small box is fast enough; a full-screen grab on every look would be too slow to react in time.
- The game speeds up, so the box must reach further ahead as time passes. Widening it from 30 to 75 game pixels was the biggest improvement.
- A headless Chrome lets you watch the bot play without taking the mouse and keyboard; pyautogui keeps its fail-safe (mouse in a corner stops the bot) for desktop runs.
