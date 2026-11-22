# Installation

🌐 [English](Install) · **Dansk** · [Bahasa Malaysia](Install-ms)

Opret et lokalt virtuelt miljø i `.venv`, opgradér pip og installér projektet med testværktøjerne. Du skal bruge Python 3.14 eller nyere.

Linux og macOS:

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

Spil på skrivebordet: åbn spillet i Chrome på https://elgoog.im/t-rex/, start botten og klik på spillet inden nedtællingen slutter. Flyt musen til et hjørne af skærmen for at stoppe botten.

```bash
python -m dino_bot --countdown 5
```

Se den uden at bruge skrivebordet: installér det valgfri headless-extra (kræver Google Chrome) og kør i headless-tilstand.

```bash
python -m pip install -e ".[headless]"
python -m dino_bot --headless --seconds 150
```

Kør testene (de behøver ingen skærm):

```bash
python -m pytest
```
