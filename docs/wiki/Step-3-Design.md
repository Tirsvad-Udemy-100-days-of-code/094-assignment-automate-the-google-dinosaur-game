# Step 3: Design

🌐 **English** · [Dansk](Step-3-Design-da) · [Bahasa Malaysia](Step-3-Design-ms)

Milestone `MIL-003`. Branch and pull request: one for this step.

![Use case UC-001 and the layers of the design](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/03-design-class-diagram.png)

## What was done

The use case UC-001 *Play the game*, two decisions (ADR-0001: Pillow and pyautogui with an optional headless Chrome; ADR-0002: a box of pixels in front of the dinosaur), the domain model DM-001 and the design class diagram DCD-001, each reviewed with a `Go` record.

## What was gained

- A bot is a loop of look, decide, act. Naming the three as a screen, a rule and a keyboard lets the rule be tested without any screen.
- A small box of pixels is enough: the bot does not need to recognise a cactus, only to notice that something dark is in front of the dinosaur.
- Writing the decision down (ADR) records why other ideas, such as template matching or reading the page state, were left out.
