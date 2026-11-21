# Step 2: Scaffold

🌐 **English** · [Dansk](Step-2-Scaffold-da) · [Bahasa Malaysia](Step-2-Scaffold-ms)

Milestone `MIL-002`. Branch and pull request: one for this step.

![Smoke tests passing in the .venv](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/02-scaffold-tests.png)

## What was done

An empty but runnable Python project: `pyproject.toml` (Python 3.14 or newer, Pillow and PyAutoGUI as runtime dependencies), the package `src/dino_bot/` with `constants.py`, smoke tests, a `Doxyfile`, a Python `.gitignore`, an `.editorconfig` and the README with the `.venv` steps. opengrep ran clean before the push.

## What was gained

- `pyproject.toml` holds the metadata, the dependencies, the optional extras and the pytest settings in one file.
- A `.venv` keeps the packages of the project apart from the system Python; `python -m pip install --upgrade pip` first avoids old-pip surprises.
- Every number of the bot (game speed, box size, key, delays) lives in `constants.py`, so tuning the bot later happens in one place.
