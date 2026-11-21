# Langkah 4: Penglihatan

🌐 [English](Step-4-Vision) · [Dansk](Step-4-Vision-da) · **Bahasa Malaysia**

Pencapaian `MIL-004`. Cabang dan pull request: satu untuk langkah ini.

![Kotak pengesanan dilukis pada gambar permainan sebenar dan ujian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/04-vision-detection-box.png)

## Apa yang dilakukan

Bahagian bot yang melihat: objek nilai `Box` dan `Frame`, `find_game_area` (garis tanah memberi kedudukan dan skala), `GameArea.detection_box` dan `is_collision` (adakah halangan dalam piksel?). Ujian unit menggunakan gambar yang dijana dalam ujian, jadi tiada skrin diperlukan.

## Apa yang diperoleh

- Tangkapan skrin kelabu hanyalah senarai nombor; garis tanah ialah baris dengan paling banyak piksel gelap dan lebarnya memberi skala skrin.
- Mengambil nilai kelabu paling biasa sebagai latar belakang membolehkan satu peraturan berfungsi dalam mod siang (gelap atas putih) dan mod malam (cerah atas hitam).
- Oleh kerana peraturan bekerja pada bait biasa, ujian boleh melukis kaktus dalam tiga baris dan menguji bot tanpa membuka permainan.
