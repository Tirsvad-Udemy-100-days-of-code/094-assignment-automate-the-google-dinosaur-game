# Langkah 5: Bot

🌐 [English](Step-5-Bot) · [Dansk](Step-5-Bot-da) · **Bahasa Malaysia**

Pencapaian `MIL-005`. Cabang dan pull request: satu untuk langkah ini.

![Larian tanpa kepala bot dengan skornya](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/05-bot-headless-run.png)

## Apa yang dilakukan

Bot berjalan: kes guna `play_game`, port untuk skrin, papan kekunci dan jam, penyesuai desktop (`DesktopScreen` dengan Pillow, `hit` dan `DesktopKeyboard` dengan pyautogui), penyesuai Chrome tanpa kepala dan baris perintah `python -m dino_bot`. Ujian menggunakan objek palsu. Larian tanpa kepala pertama gagal pada skor 270, jadi pemalar ditala; larian terbaik kini mencapai 2000 dan lebih, dan skor berbeza dari satu larian ke satu larian.

## Apa yang diperoleh

- Mengambil hanya kotak kecil sudah cukup pantas; tangkapan skrin penuh pada setiap pandangan akan terlalu perlahan untuk bertindak balas tepat pada masanya.
- Permainan bertambah laju, jadi kotak mesti menjangkau lebih jauh ke hadapan apabila masa berlalu. Melebarkannya daripada 30 kepada 75 piksel permainan ialah penambahbaikan terbesar.
- Chrome tanpa kepala membolehkan anda menonton bot bermain tanpa mengambil tetikus dan papan kekunci; pyautogui mengekalkan fail-safe (tetikus di sudut menghentikan bot) untuk larian desktop.
