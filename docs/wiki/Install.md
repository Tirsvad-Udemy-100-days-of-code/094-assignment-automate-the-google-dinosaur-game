# Install

🌐 **English** · [Dansk](Install-da) · [Bahasa Malaysia](Install-ms)

Create a local virtual environment in `.venv`, upgrade pip and install the project with its test tools. You need Python 3.14 or newer.

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Windows (PowerShell):

```powershell
py -3.14 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Play on the desktop: open the game in Chrome at https://elgoog.im/t-rex/, start the bot and click on the game within the countdown. Move the mouse to a corner of the screen to stop the bot.

```bash
python -m dino_bot --countdown 5
```

Watch it without using the desktop: install the optional headless extra (needs Google Chrome) and run in headless mode.

```bash
python -m pip install -e ".[headless]"
python -m dino_bot --headless --seconds 150
```

Run the tests (they need no screen):

```bash
python -m pytest
```
