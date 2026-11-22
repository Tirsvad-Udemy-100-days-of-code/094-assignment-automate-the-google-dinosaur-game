# Reflection Journal

🌐 **English** · [Dansk](Reflection-da) · [Bahasa Malaysia](Reflection-ms)

Day 94 assignment: Automate the Google Dinosaur Game. The wiki carries this journal in English, Danish and Bahasa Malaysia.

## How I approached the project

I read the assignment first and then measured the game before I wrote any code. I opened it in a headless Chrome, took screenshots and found out where the ground line is, how many screen pixels the 600 game pixels take (956 in my window, a scale of 1.6) and which grey the dinosaur and the cacti are drawn with. After that I planned six milestones, each with its own branch and pull request, designed the bot as three small parts (a screen, a rule and a keyboard), built and tested the part that looks, and only then connected the keyboard and tuned the bot against the real game.

## What was easy

- Finding the game: the ground line is the row with the most dark pixels, and its length gives the scale. One loop over the rows does it.
- Working with pixels: a screenshot converted to grey is only a list of bytes, so cropping, counting and comparing need no image library.
- Testing the part that looks: the tests draw a cactus in three lines and 55 of them run in less than 0.2 seconds, without a screen.

## What was hard

- Timing. The same bot scored 233 in one run and 2310 in another. A screenshot takes tens of milliseconds, so the cactus is seen a few frames late, and at high speed a few frames are many pixels. My first zone of 30 game pixels crashed after a few hundred points. A zone that reaches 75 game pixels ahead helped most, but if it reaches too far the dinosaur jumps too early and lands on the cactus.
- The game only stretches to its full width after the first key press, so searching for the ground line before the start failed. The bot now presses the space bar, waits a second and then searches.
- In the browser the space bar scrolled the page and moved the game away from where the bot had found it. Hiding the page scroll fixed it.
- Not using the desktop for tests. All live checks run in a headless Chrome, so the Pillow and pyautogui adapters are tested with stand-ins and only used for real by the person who runs the bot.

## What I would do differently next time

- Measure the speed of the game from two looks at the same obstacle instead of estimating it from the time since the start.
- Use the down arrow to fall faster after a jump, duck under high birds and handle two cacti that come close together; the deaths I looked at were all such cases.
- Save a picture of the last frame of every run and run many games in a row, so a change of a constant is judged on ten runs and not on one.
- Check the desktop adapters once in a disposable Windows Sandbox, to have seen them work end to end.

## Biggest learning

A bot is a loop of look, decide and act, and the hard part is time, not code. Keeping the rule a pure function of bytes made it easy to test, and keeping the adapters thin made them easy to replace: the headless Chrome plays with the same rule as the desktop. Over eight runs of the final code the scores were 233, 432, 547, 625, 704, 1109, 1301 and 2310, so a single good run proves little and a table of runs tells the truth.
