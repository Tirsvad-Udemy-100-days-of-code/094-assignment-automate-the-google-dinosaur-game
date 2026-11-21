# Trin 2: Skelet

🌐 [English](Step-2-Scaffold) · **Dansk** · [Bahasa Malaysia](Step-2-Scaffold-ms)

Milepæl `MIL-002`. Gren og pull request: én for dette trin.

![Smoke-tests består i .venv](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/02-scaffold-tests.png)

## Hvad der blev gjort

Et tomt, men kørbart Python-projekt: `pyproject.toml` (Python 3.14 eller nyere, Pillow og PyAutoGUI som kørselsafhængigheder), pakken `src/dino_bot/` med `constants.py`, smoke-tests, en `Doxyfile`, en Python-`.gitignore`, en `.editorconfig` og README med `.venv`-trin. opengrep var ren før push.

## Hvad vi fik ud af det

- `pyproject.toml` samler metadata, afhængigheder, valgfri extras og pytest-indstillinger i én fil.
- Et `.venv` holder projektets pakker adskilt fra systemets Python; `python -m pip install --upgrade pip` først undgår overraskelser med gammel pip.
- Alle botens tal (spillets fart, boksens størrelse, tast, forsinkelser) står i `constants.py`, så finjustering senere sker ét sted.
