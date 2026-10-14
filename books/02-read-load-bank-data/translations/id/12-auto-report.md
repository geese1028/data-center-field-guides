Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 12. Pembuatan Grafik Otomatis dan Integritas Visual

Generator laporan otomatis atau dasbor supervisi adalah alat yang ampuh untuk mengubah telemetri mentah menjadi representasi visual yang cepat. Namun, grafik otomatis bukanlah otoritas independen. Grafik hanyalah proyeksi visual dari angka-angka yang tercatat dalam blok data yang mendasarinya.

Jika grafik visual dan blok data laporan kilat (*flash report*) tidak sejalan, angka-angka dalam blok data selalu menjadi acuan utama. Kurva mulus dan indah yang dirender oleh pustaka grafik tidak memiliki kewenangan untuk meluluskan sebuah sel yang digagalkan oleh tabel data mentah.

Selain itu, pembuatan grafik dalam komisioning sarat dengan penipuan visual yang halus—sebagian tidak disengaja, sebagian disengaja. Sumbu vertikal yang tidak terkalibrasi dapat meratakan kelaparan aliran berbahaya sebesar 15% hingga tampak seperti garis setipis rambut, sementara judul yang salah label dapat menyebabkan auditor salah mengira konsumsi daya listrik sebagai kapasitas pendinginan cair yang tersertifikasi.

Bab ini mendefinisikan aturan ketat tentang pembuatan grafik otomatis, etika penskalaan visual, dan tata letak plot yang diwajibkan.

## Hal yang Harus Diatur Operator Sebelum Kurva Apa Pun Digambar

Skrip pelaporan otomatis tidak boleh dibiarkan menebak-nebak batasan dari kumpulan datanya. Sebelum menghasilkan satu grafik pun, Operator harus mendefinisikan dua parameter secara eksplisit dalam konfigurasi skrip:

1. **Jendela Waktu yang Tepat**: Stempel waktu mulai dan selesai, didefinisikan hingga hitungan detik yang tepat (misalnya, `START = 2026-10-14T14:00:00Z`, `END = 2026-10-14T15:30:00Z`). Skrip harus menarik data secara ketat dari dalam jendela ini. Laporan otomatis yang menggunakan jendela mengambang yang ambigu (seperti "60 menit terakhir") akan bergeser maju selama peninjauan, mengubah nilai rata-rata terhitung saat sistem mendingin.
2. **Daftar Unit Eksplisit**: Daftar nomor seri kabinet bank beban yang tepat yang aktif dalam pengujian (misalnya, `UNITS = ["LB-01", "LB-02", "LB-03", "LB-04"]`). Jangan pernah membiarkan templat pelaporan mempertahankan daftar unit yang dikodekan permanen (*hardcoded*) dari pekerjaan sebelumnya. Jika sebuah templat berjudul "Pengujian Baris 18-Kabinet" dijalankan pada hari ketika hanya 4 kabinet yang terhubung, angka-angka yang dihasilkan akan menjadi kekacauan administratif yang memalukan.

Setiap grafik yang dihasilkan harus mencetak jendela waktu dan daftar unit aktifnya langsung ke dalam *banner* subjudul atasnya.

## Persyaratan Dua Grafik: Kluster Bertumpuk vs. Telaah Mendalam Individual

Setiap kali parameter fisik disajikan dalam laporan otomatis, membuat grafik agregat tunggal dilarang keras. Grafik tunggal yang hanya menampilkan jumlah kluster atau rata-rata kluster akan menyembunyikan divergensi pada tingkat kabinet.

Mesin pelaporan harus menghasilkan **dua grafik komplementer** untuk setiap kuantitas yang dipantau:

### Grafik A: Grafik Kluster Bertumpuk (*Overlaid Cluster Chart*)
Semua kabinet paralel diplot bersama pada satu set sumbu tunggal, menggunakan warna garis yang kontras dan mudah dibedakan:
- Hal ini memungkinkan auditor untuk langsung melihat jika satu kabinet "meninggalkan kelompok"—misalnya, melihat tiga kabinet melacak pada 176 LPM sementara Kabinet 4 anjlok ke 124 LPM.
- Rata-rata aritmatika kluster (μ) diplot sebagai garis kuning putus-putus tebal melalui bagian tengah pita data.

### Grafik B: Grafik Telaah Mendalam Kabinet Individual (*Individual Cabinet Deep-Dive Chart*)
Setiap kabinet individual diberikan panel plot khususnya sendiri dengan sumbu vertikal yang dioptimalkan:
- Hal ini mencegah penipuan penskalaan umum: jika suhu kembali Kabinet 4 naik dari 45,0°C menjadi 49,8°C, memplotnya pada grafik bertumpuk yang sumbu vertikalnya membentang dari 0°C hingga 100°C akan membuat lonjakan 4,8 K terlihat sepele.
- Pada grafik telaah mendalam khususnya, sumbu vertikal membentang ketat melintasi jendela operasi (misalnya, 30°C hingga 55°C), memastikan bahwa kenaikan suhu dan fluktuasi (*hunting*) frekuensi tinggi terlihat jelas.

## Empat Statistik Ringkasan di Bawah Setiap Grafik

Di bawah setiap panel plot yang dihasilkan, mesin pelaporan otomatis harus menghitung dan mencetak tabel ringkasan terstandarisasi yang memuat empat metrik spesifik untuk jendela waktu tersebut:

1. **Nilai Minimum ($\min$)**
2. **Nilai Maksimum ($\max$)**
3. **Rata-Rata Aritmatika (μ)**
4. **Nilai Median ($\tilde{x}$)**

### Mengapa Median Wajib Dicantumkan
Dalam penyerapan telemetri otomatis, peralihan kontaktor listrik dan operasi pemutus arus tegangan tinggi dapat memicu denyut interferensi elektromagnetik (EMI) yang menyebabkan pengonversi analog-ke-digital (ADC) mencatat lonjakan palsu tunggal berdurasi 1 milidetik (misalnya, mencatat satu sampel 1200 kW sebelum kembali ke 120{,}0 kW).
- Dalam masa jeda 900 sampel, satu sampel buruk tersebut akan menarik rata-rata aritmatika ke atas sebesar 1{,}2 kW, mendistorsi perhitungan penutupan energi.
- Nilai median secara inheren kebal terhadap lonjakan pencilan (*outlier*) yang terisolasi. Membandingkan rata-rata (μ = 121{,}2 kW) terhadap median ($\tilde{x} = 120{,}0 kW$) langsung mengungkap adanya lonjakan asimetris.
- Jika nilai maksimum dan minimum identik ($\max = \min = 45{,}000°C$), mesin pelaporan harus secara otomatis menyorot tabel tersebut dengan warna merah dengan label: **"PERINGATAN: VARIANS NOL TERDETEKSI (BUFFER BEKU)."**

## Kategori Grafik Inti

Laporan otomatis harus menghasilkan lima rangkaian grafik terstandarisasi:

### 1. Rangkaian Grafik Daya Listrik
- Total daya aktif kluster (kW) seiring waktu.
- Daya aktif kabinet individual yang dihamparkan (*overlaid*) dan terpisah.
- Tegangan saluran-ke-saluran 3-fasa dan arus fasa penyulang.
- Verifikasi bahwa Penyulang A dan Penyulang B membagi daya secara simetris (50% ± 1{,}0%).

### 2. Rangkaian Grafik Hidrolika Cairan Pendingin
- Laju aliran volumetrik per kabinet (Q_v, dilaporkan dalam LPM).
- Tekanan diferensial manifold (ΔP = P_in - P_out, dilaporkan dalam kPa).
- Laju aliran *loop* sekunder total, secara eksplisit diturunkan sebagai jumlah dari pengukur aliran cabang.

### 3. Rangkaian Grafik Entalpi Termal
- Suhu cairan pendingin pasokan sekunder (T_in) dan suhu kembali (T_out) per kabinet.
- Kenaikan suhu diferensial (ΔT = T_out - T_in) per kabinet.
- **Gerbang Pemeriksaan Tanda**: Selisihnya harus bernilai positif secara tegas (T_out > T_in). Jika kesalahan pemipaan membalikkan posisi selang, ΔT akan terplot sebagai nilai negatif. Skrip pembuatan grafik dilarang keras menerapkan fungsi nilai mutlak (`abs(delta_t)`) untuk membuat sambungan terbalik tampak benar! ΔT negatif harus diplot sebagai nilai negatif dan memicu bendera GAGAL (*FAIL*) otomatis.

### 4. Rangkaian Grafik Kalor Terinferensi Sejati vs. Daya Listrik
- Daya aktif listrik (P_elec) diplot berdampingan dengan entalpi cairan terinferensi yang sebenarnya (Q_liquid = ṁ C_p ΔT).
- Dalam keadaan apa pun, jejak daya listrik tidak boleh diubah judulnya menjadi "Daya Pendinginan"!
- Daya listrik adalah energi yang disalurkan dari *switchgear*; daya pendinginan adalah energi termal yang diserap oleh aliran fluida. Memplot keduanya pada sumbu yang sama dengan warna yang berbeda langsung mengungkap kebocoran *bypass* internal atau kehilangan panas.

### 5. Rangkaian Grafik Udara Pendamping
- Suhu udara masuk bola kering (T_air,in) dan suhu udara buang (T_air,out).
- Diferensial suhu udara (ΔT_air).
- Kalor sensibel udara terinferensi (Q_air).

## Aturan Etika Skala Visual

Skala visual tidak boleh dimanipulasi untuk memuji-muji kinerja peralatan. Aturan pembuatan grafik berikut ini bersifat wajib:

- **Larangan Penekanan Titik Nol untuk Klaim Kapasitas**: Saat memplot total daya atau total aliran terhadap kapasitas nominal terukur, sumbu vertikal harus menyertakan garis dasar nol sehingga pengamat dapat melihat besaran langkah yang sebenarnya.
- **Larangan Sumbu yang Diperluas Berlebihan untuk Menyembunyikan Varians**: Saat memplot stabilitas suhu atau keseragaman aliran di sepanjang masa jeda tunak, sumbu vertikal tidak boleh diperluas secara artifisial hingga ± 100 K atau ± 500 LPM demi membuat fluktuasi liar tampak seperti garis lurus. Sumbu harus diskalakan secara ketat pada batas toleransi yang disitasi (misalnya, T_nominal ± 5{,}0 K).
- **Garis Kisi Eksplisit**: Setiap grafik harus menampilkan garis kisi (*gridlines*) horizontal dan vertikal yang tipis pada interval rekayasa standar (misalnya, setiap 5 menit, setiap 10 kW, setiap 1,0 K) guna memungkinkan audit visual cepat tanpa penggaris digital.

## Keputusan yang Harus Dicatat

Di bagian grafik pada laporan kilat, dokumentasikan:

- Stempel waktu mulai dan berhenti yang tepat dari jendela pembuatan grafik.
- Daftar nomor seri kabinet aktif terkonfirmasi yang disertakan dalam pembuatan visual.
- Resolusi pengambilan sampel dari setiap saluran yang diplot (mentah 1 detik vs rata-rata bergerak 60 detik).
- Konfirmasi bahwa tidak ada transformasi nilai mutlak atau filter penghalusan artifisial yang diterapkan pada deret data mentah.
