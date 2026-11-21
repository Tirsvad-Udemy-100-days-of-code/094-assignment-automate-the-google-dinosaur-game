# Jurnal Refleksi

🌐 [English](Reflection) · [Dansk](Reflection-da) · **Bahasa Malaysia**

Tugasan Hari 94: Automatikkan Google Dinosaur Game. Wiki membawa jurnal ini dalam bahasa Inggeris, Denmark dan Bahasa Malaysia.

## Bagaimana saya mendekati projek

Saya membaca tugasan dahulu dan kemudian mengukur permainan sebelum menulis sebarang kod. Saya membukanya dalam Chrome tanpa kepala, mengambil tangkapan skrin dan mengetahui di mana garis tanah berada, berapa piksel skrin yang diambil oleh 600 piksel permainan (956 dalam tetingkap saya, skala 1.6) dan warna kelabu yang digunakan untuk melukis dinosaur dan kaktus. Selepas itu saya merancang enam pencapaian, masing-masing dengan cabang dan pull request sendiri, mereka bentuk bot sebagai tiga bahagian kecil (skrin, peraturan dan papan kekunci), membina dan menguji bahagian yang melihat, dan barulah menyambung papan kekunci serta menala bot dengan permainan sebenar.

## Apa yang mudah

- Mencari permainan: garis tanah ialah baris dengan paling banyak piksel gelap, dan panjangnya memberi skala. Satu gelung merentasi baris sudah cukup.
- Bekerja dengan piksel: tangkapan skrin kelabu hanyalah senarai bait, jadi memotong, mengira dan membandingkan tidak memerlukan perpustakaan imej.
- Menguji bahagian yang melihat: ujian melukis kaktus dalam tiga baris dan 55 daripadanya berjalan dalam kurang 0.2 saat, tanpa skrin.

## Apa yang sukar

- Masa. Bot yang sama mendapat 233 dalam satu larian dan 2310 dalam yang lain. Tangkapan skrin mengambil puluhan milisaat, jadi kaktus dilihat beberapa bingkai terlewat, dan pada kelajuan tinggi beberapa bingkai ialah banyak piksel. Zon pertama saya sebanyak 30 piksel permainan gagal selepas beberapa ratus mata. Zon yang menjangkau 75 piksel permainan ke hadapan paling membantu, tetapi jika terlalu jauh dinosaur melompat terlalu awal dan mendarat di atas kaktus.
- Permainan hanya meregang ke lebar penuh selepas tekanan kekunci pertama, jadi mencari garis tanah sebelum bermula gagal. Bot kini menekan bar ruang, menunggu satu saat dan kemudian mencari.
- Dalam pelayar, bar ruang menatal halaman dan menggerakkan permainan jauh dari tempat bot menemuinya. Menyembunyikan tatal halaman menyelesaikannya.
- Tidak menggunakan desktop untuk ujian. Semua semakan langsung berjalan dalam Chrome tanpa kepala, jadi penyesuai Pillow dan pyautogui diuji dengan objek ganti dan hanya digunakan sebenar-benarnya oleh orang yang menjalankan bot.

## Apa yang akan saya ubah pada masa akan datang

- Mengukur kelajuan permainan daripada dua pandangan pada halangan yang sama dan bukannya menganggarkannya daripada masa sejak bermula.
- Menggunakan anak panah bawah untuk jatuh lebih cepat selepas lompatan, tunduk di bawah burung tinggi dan mengendalikan dua kaktus yang berdekatan; kematian yang saya lihat semuanya kes sebegitu.
- Menyimpan gambar bingkai terakhir setiap larian dan menjalankan banyak permainan berturut-turut, supaya perubahan pemalar dinilai pada sepuluh larian dan bukan satu.
- Mencuba penyesuai desktop sekali dalam Windows Sandbox pakai buang untuk melihatnya berfungsi dari hujung ke hujung.

## Pelajaran terbesar

Bot ialah gelung lihat, putuskan dan bertindak, dan bahagian yang sukar ialah masa, bukan kod. Mengekalkan peraturan sebagai fungsi tulen bagi bait menjadikannya mudah diuji, dan penyesuai yang nipis menjadikannya mudah diganti: Chrome tanpa kepala bermain dengan peraturan yang sama seperti desktop. Dalam lapan larian kod akhir, skornya ialah 233, 432, 547, 625, 704, 1109, 1301 dan 2310, jadi satu larian yang baik membuktikan sedikit dan jadual larian menceritakan kebenaran.
