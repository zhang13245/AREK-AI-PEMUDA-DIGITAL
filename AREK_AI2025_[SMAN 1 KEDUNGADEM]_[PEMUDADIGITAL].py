import random
import time

# ====== Kumpulan Teka-Teki ======
teka_teki = [
    # 1
    {
        "pelajaran": "Matematika",
        "soal": "Aku bukan bilangan genap, bukan juga bilangan prima. Jika kamu kalikan aku dengan 1 lalu kurangi 1, hasilnya tetap bilangan genap. Siapakah aku (satu kata)?",
        "jawaban": "bilangan ganjil komposit"
    },
    # 2
    {
        "pelajaran": "Fisika",
        "soal": "Aku selalu menahan benda agar tidak terus melaju lurus saat melalui lintasan melengkung. Besarku bergantung pada massa, kecepatan, dan seberapa melengkung lintasannya. Siapakah aku?",
        "jawaban": "gaya sentripetal"
    },
    # 3
    {
        "pelajaran": "Kimia",
        "soal": "Aku adalah zat yang jika larut dalam air dapat menghantarkan listrik karena ion-ionku bergerak. Biasanya aku terbentuk dari logam + non-logam. Siapakah aku?",
        "jawaban": "garam"
    },
    # 4
    {
        "pelajaran": "Biologi",
        "soal": "Aku membawa pesan genetik dari inti sel ke ribosom untuk pembuatan protein. Bentukku berupa rantai nukleotida tunggal. Siapakah aku?",
        "jawaban": "mrna"
    },
    # 5
    {
        "pelajaran": "Sejarah",
        "soal": "Aku sering disebut titik balik dalam perang karena pasukanku berhasil memutus jalur suplai musuh dan mengubah jalannya konflik. Istilah umum apakah aku?",
        "jawaban": "titik balik"
    },
    # 6
    {
        "pelajaran": "Geografi",
        "soal": "Aku terbentuk ketika satu lempeng tektonik turun di bawah lempeng lain. Aku sering menghasilkan gunung berapi di permukaan. Proses apakah aku?",
        "jawaban": "subduksi"
    },
    # 7
    {
        "pelajaran": "Ekonomi",
        "soal": "Aku terjadi saat harga naik terus-menerus dan nilai uang menurun; pembeli bisa membeli lebih sedikit dengan jumlah uang yang sama. Istilah apa aku?",
        "jawaban": "inflasi"
    },
    # 8
    {
        "pelajaran": "Bahasa Indonesia",
        "soal": "Aku adalah gaya bahasa yang menyamakan dua benda berbeda dengan kata penghubung seperti 'seperti' atau 'bagai'. Apa istilahku?",
        "jawaban": "simile"
    },
    # 9
    {
        "pelajaran": "Bahasa Inggris",
        "soal": "Dalam bahasa Inggris, aku bentuk kata kerja yang menunjukkan tindakan sedang terjadi sekarang (contoh: 'I am eating'). Apa nama tense-ku?",
        "jawaban": "present continuous"
    },
    # 10
    {
        "pelajaran": "Matematika (Logika)",
        "soal": "Jika pernyataan 'Semua A adalah B' benar dan 'Beberapa B adalah C' benar, apakah kita bisa menyimpulkan 'Beberapa A adalah C'? (Jawaban: ya/tidak)",
        "jawaban": "tidak"
    },
    # 11
    {
        "pelajaran": "Informatika",
        "soal": "Aku adalah aturan langkah demi langkah untuk menyelesaikan masalah, sering ditulis dalam pseudocode atau bahasa pemrograman. Siapakah aku?",
        "jawaban": "algoritma"
    },
    # 12
    {
        "pelajaran": "Kimia / Biologi",
        "soal": "Aku molekul kecil yang menjadi 'bahan bakar' sel untuk menghasilkan energi dalam bentuk ATP. Siapakah aku?",
        "jawaban": "glukosa"
    },

    # ===== Tambahan Soal Baru (28 soal) =====

    # 13
    {
        "pelajaran": "Matematika",
        "soal": "Aku adalah jarak antara titik data dengan nilai rata-rata, biasanya dikuadratkan. Apa istilahku?",
        "jawaban": "varian"
    },
    # 14
    {
        "pelajaran": "Fisika",
        "soal": "Aku adalah gaya gesek yang muncul ketika benda bergerak dalam fluida seperti udara atau air. Siapakah aku?",
        "jawaban": "gaya hambat"
    },
    # 15
    {
        "pelajaran": "Biologi",
        "soal": "Aku adalah organel tempat berlangsungnya respirasi sel dan penghasil energi. Siapakah aku?",
        "jawaban": "mitokondria"
    },
    # 16
    {
        "pelajaran": "Sejarah",
        "soal": "Aku adalah masa ketika manusia mulai mengenal tulisan. Zaman apakah aku?",
        "jawaban": "zaman sejarah"
    },
    # 17
    {
        "pelajaran": "Geografi",
        "soal": "Aku angin yang bertiup secara periodik tiap enam bulan sekali. Apa namaku?",
        "jawaban": "angin muson"
    },
    # 18
    {
        "pelajaran": "Ekonomi",
        "soal": "Aku adalah kondisi ketika jumlah barang yang tersedia lebih sedikit dibanding permintaan. Apakah aku?",
        "jawaban": "kelangkaan"
    },
    # 19
    {
        "pelajaran": "Bahasa Indonesia",
        "soal": "Aku adalah majas yang memberikan sifat manusia kepada benda mati. Siapakah aku?",
        "jawaban": "personifikasi"
    },
    # 20
    {
        "pelajaran": "Bahasa Inggris",
        "soal": "Aku adalah kata sifat yang berfungsi membandingkan dua hal, dicirikan dengan akhiran -er atau 'more'. Siapakah aku?",
        "jawaban": "comparative"
    },
    # 21
    {
        "pelajaran": "Informatika",
        "soal": "Aku adalah struktur data yang memasukkan dan mengeluarkan data dengan prinsip FIFO. Apakah aku?",
        "jawaban": "queue"
    },
    # 22
    {
        "pelajaran": "Kimia",
        "soal": "Aku adalah perubahan wujud dari gas menjadi cair. Proses apakah aku?",
        "jawaban": "kondensasi"
    },
    # 23
    {
        "pelajaran": "Fisika",
        "soal": "Aku adalah kecepatan yang berubah terhadap waktu. Istilah fisika apa aku?",
        "jawaban": "percepatan"
    },
    # 24
    {
        "pelajaran": "Matematika",
        "soal": "Aku adalah nilai tengah dari data yang sudah diurutkan. Siapakah aku?",
        "jawaban": "median"
    },
    # 25
    {
        "pelajaran": "Biologi",
        "soal": "Aku adalah proses perubahan ulat menjadi kupu-kupu. Apa namaku?",
        "jawaban": "metamorfosis"
    },
    # 26
    {
        "pelajaran": "Sejarah",
        "soal": "Aku adalah peristiwa penyerahan kekuasaan Jepang kepada Sekutu pada 1945. Istilah peristiwa apakah aku?",
        "jawaban": "kapitulasi jepang"
    },
    # 27
    {
        "pelajaran": "Geografi",
        "soal": "Aku adalah garis khayal yang menghubungkan tempat-tempat dengan tekanan udara sama. Apa istilahku?",
        "jawaban": "isobar"
    },
    # 28
    {
        "pelajaran": "Ekonomi",
        "soal": "Aku adalah jumlah barang yang ingin dan mampu dibeli pada tingkat harga tertentu. Apakah aku?",
        "jawaban": "permintaan"
    },
    # 29
    {
        "pelajaran": "Bahasa Inggris",
        "soal": "Aku adalah bentuk kata kerja masa depan yang menyatakan rencana (will + verb). Apa tense-ku?",
        "jawaban": "simple future"
    },
    # 30
    {
        "pelajaran": "Matematika",
        "soal": "Aku adalah himpunan pasangan berurutan yang menunjukkan hubungan antar elemen. Apa istilahku?",
        "jawaban": "relasi"
    },
    # 31
    {
        "pelajaran": "Kimia",
        "soal": "Aku adalah ion bermuatan positif. Siapakah aku?",
        "jawaban": "kation"
    },
    # 32
    {
        "pelajaran": "Biologi",
        "soal": "Aku adalah tempat berlangsungnya fotosintesis dalam sel tumbuhan. Apakah aku?",
        "jawaban": "kloroplas"
    },
    # 33
    {
        "pelajaran": "Informatika",
        "soal": "Aku adalah sistem bilangan yang hanya menggunakan dua angka: 0 dan 1. Siapakah aku?",
        "jawaban": "biner"
    },
    # 34
    {
        "pelajaran": "Sejarah",
        "soal": "Aku adalah masa ketika manusia masih mengandalkan berburu dan meramu. Zaman apakah aku?",
        "jawaban": "zaman berburu dan meramu"
    },
    # 35
    {
        "pelajaran": "Geografi",
        "soal": "Aku adalah aliran massa es besar yang bergerak lambat dari pegunungan tinggi. Siapakah aku?",
        "jawaban": "gletser"
    },
    # 36
    {
        "pelajaran": "Fisika",
        "soal": "Aku adalah energi yang dimiliki benda karena geraknya. Apa istilahku?",
        "jawaban": "energi kinetik"
    },
    # 37
    {
        "pelajaran": "Ekonomi",
        "soal": "Aku adalah kemampuan suatu negara memproduksi barang dan jasa untuk memenuhi kebutuhan masyarakat. Apakah aku?",
        "jawaban": "produktivitas"
    },
    # 38
    {
        "pelajaran": "Bahasa Indonesia",
        "soal": "Aku adalah kata yang memiliki makna berlawanan dengan kata lain. Apa istilahku?",
        "jawaban": "antonim"
    },
    # 39
    {
        "pelajaran": "Matematika",
        "soal": "Aku adalah garis yang memotong dua garis sejajar sehingga membentuk sudut sehadap dan berseberangan. Siapakah aku?",
        "jawaban": "garis transversal"
    },
    # 40
    {
        "pelajaran": "Fisika",
        "soal": "Aku adalah gelombang yang tidak membutuhkan medium untuk merambat, seperti cahaya. Apa jenis gelombangku?",
        "jawaban": "gelombang elektromagnetik"
    }
]

# ====== Pilihan Mode ======
print("=== GAME TEKA-TEKI PELAJARAN SMA ===")
print("Pilih Mode Permainan:")
print("1. Mode Latihan (jawaban langsung dinilai)")
print("2. Mode Tantangan (nilai keluar di akhir)")
print("3. Mode Waktu (10 detik per soal)\n")

mode = input("Pilih mode (1/2/3): ").strip()

while mode not in ["1", "2", "3"]:
    mode = input("Masukkan angka 1 / 2 / 3: ").strip()

print("\nKetik 'quit' untuk keluar dari permainan.\n")

# ====== Mode Tantangan (menyimpan skor) ======
jawaban_benar = 0
jawaban_salah = 0
total_soal = 0

while True:
    teka = random.choice(teka_teki)
    total_soal += 1

    print(f"[Pelajaran: {teka['pelajaran']}]")
    print(teka["soal"])

    # ========== MODE WAKTU ==========
    if mode == "3":
        print("⏳ Kamu punya 10 detik untuk menjawab!")
        start = time.time()

    jawaban = input("Jawabanmu: ").lower().strip()

    # Cek quit
    if jawaban == "quit":
        print("\nTerima kasih telah bermain! 😊")
        break

    # Cek waktu habis
    if mode == "3":
        if time.time() - start > 10:
            print("❌ Waktu habis! Jawaban yang benar:", teka["jawaban"], "\n")
            jawaban_salah += 1
            continue

    # MODE LATIHAN
    if mode == "1":
        if jawaban == teka["jawaban"]:
            print("Benar! 🎉\n")
        else:
            print("Salah! Jawaban yang benar adalah:", teka["jawaban"], "\n")

    # MODE TANTANGAN dan MODE WAKTU → skor dihitung, hasil ditampilkan akhir
    if mode in ["2", "3"]:
        if jawaban == teka["jawaban"]:
            jawaban_benar += 1
        else:
            jawaban_salah += 1

# ====== Jika mode tantangan atau waktu, tampilkan hasil akhir ======
if mode in ["2", "3"]:
    print("\n=== HASIL AKHIR ===")
    print("Total Soal :", total_soal)
    print("Benar      :", jawaban_benar)
    print("Salah      :", jawaban_salah)
    print("Skor akhir :", f"{jawaban_benar}/{total_soal}")
    print("====================")
