# Langkah 2: Rangka

🌐 [English](Step-2-Scaffold) · [Dansk](Step-2-Scaffold-da) · **Bahasa Malaysia**

Pencapaian `MIL-002`. Cabang dan pull request: satu untuk langkah ini.

![Ujian asap lulus dalam .venv](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/02-scaffold-tests.png)

## Apa yang dilakukan

Projek Python kosong tetapi boleh dijalankan: `pyproject.toml` (Python 3.14 atau lebih baharu, Pillow dan PyAutoGUI sebagai kebergantungan masa jalan), pakej `src/dino_bot/` dengan `constants.py`, ujian asap, `Doxyfile`, `.gitignore` Python, `.editorconfig` dan README dengan langkah `.venv`. opengrep bersih sebelum push.

## Apa yang diperoleh

- `pyproject.toml` menyimpan metadata, kebergantungan, extra pilihan dan tetapan pytest dalam satu fail.
- `.venv` mengasingkan pakej projek daripada Python sistem; `python -m pip install --upgrade pip` dahulu mengelakkan kejutan pip lama.
- Setiap nombor bot (kelajuan permainan, saiz kotak, kekunci, kelewatan) berada dalam `constants.py`, jadi penalaan kemudian dilakukan di satu tempat.
