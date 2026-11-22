# Pemasangan

🌐 [English](Install) · [Dansk](Install-da) · **Bahasa Malaysia**

Cipta persekitaran maya setempat dalam `.venv`, naik taraf pip dan pasang projek dengan alat ujiannya. Anda memerlukan Python 3.14 atau lebih baharu.

Linux dan macOS:

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

Main di desktop: buka permainan dalam Chrome di https://elgoog.im/t-rex/, mulakan bot dan klik pada permainan dalam masa kira detik. Gerakkan tetikus ke sudut skrin untuk menghentikan bot.

```bash
python -m dino_bot --countdown 5
```

Tonton tanpa menggunakan desktop: pasang extra tanpa kepala pilihan (memerlukan Google Chrome) dan jalankan dalam mod tanpa kepala.

```bash
python -m pip install -e ".[headless]"
python -m dino_bot --headless --seconds 150
```

Jalankan ujian (tiada skrin diperlukan):

```bash
python -m pytest
```
