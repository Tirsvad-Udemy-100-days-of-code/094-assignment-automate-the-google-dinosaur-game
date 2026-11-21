# Langkah 3: Reka bentuk

🌐 [English](Step-3-Design) · [Dansk](Step-3-Design-da) · **Bahasa Malaysia**

Pencapaian `MIL-003`. Cabang dan pull request: satu untuk langkah ini.

![Kes guna UC-001 dan lapisan reka bentuk](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/03-design-class-diagram.png)

## Apa yang dilakukan

Kes guna UC-001 *Main permainan*, dua keputusan (ADR-0001: Pillow dan pyautogui dengan Chrome tanpa kepala pilihan; ADR-0002: kotak piksel di hadapan dinosaur), model domain DM-001 dan rajah kelas reka bentuk DCD-001, masing-masing disemak dengan rekod `Go`.

## Apa yang diperoleh

- Bot ialah gelung lihat, putuskan, bertindak. Menamakan ketiganya sebagai skrin, peraturan dan papan kekunci membolehkan peraturan diuji tanpa sebarang skrin.
- Kotak piksel kecil sudah cukup: bot tidak perlu mengenali kaktus, hanya menyedari ada sesuatu yang gelap di hadapan dinosaur.
- Menulis keputusan (ADR) merekodkan sebab idea lain, seperti padanan templat atau membaca keadaan halaman, ditinggalkan.
