# Step 4: Vision

🌐 **English** · [Dansk](Step-4-Vision-da) · [Bahasa Malaysia](Step-4-Vision-ms)

Milestone `MIL-004`. Branch and pull request: one for this step.

![The detection box drawn on a real game picture, and the tests](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/04-vision-detection-box.png)

## What was done

The part of the bot that looks: `Box` and `Frame` value objects, `find_game_area` (the ground line gives the position and the scale), `GameArea.detection_box` and `is_collision` (is an obstacle in the pixels?). Unit tests use pictures generated in the test, so no screen is needed.

## What was gained

- A screenshot in grey is only a list of numbers; the ground line is the row with the most dark pixels, and its width tells the scale of the screen.
- Taking the most common grey value as the background makes one rule work in day mode (dark on white) and night mode (light on black).
- Because the rules work on plain bytes, tests can draw a cactus in three lines and check the bot without opening the game.
