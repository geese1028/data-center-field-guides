Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 10. Paket Laporan Formal

Laporan kilat (*flash report*) dirancang untuk triase teknis cepat di lokasi. Laporan ini memberikan penilaian lima baris langsung dalam waktu dua jam setelah penghentian pengujian bank beban sehingga manajer fasilitas, direktur komisioning, dan pimpinan kontraktor dapat menentukan apakah akan melangkah ke fase komisioning berikutnya atau menahan lokasi untuk perbaikan korektif.

Namun, laporan kilat tidak lenyap begitu saja ketika giliran kerja (*shift*) berakhir. Dokumen ini menjadi inti permanen dari **Paket Serah Terima Verifikasi Komisioning Formal**—dossier hukum dan teknis yang bertahan di sepanjang masa operasional pusat data dan diarsipkan untuk penjamin asuransi (*underwriters*), audit penyewa (*tenant*) hiperskala, dan sertifikasi ulang fasilitas tahunan.

Paket formal yang terdiri dari delapan puluh halaman brosur pemasaran dan pembuangan data mentah tanpa indeks akan langsung dibuang oleh auditor. Sebaliknya, paket yang terlalu ringkas sehingga tidak mampu mempertahankan angka-angkanya akan ditolak.

Bab ini mendefinisikan secara tepat apa yang harus disimpan dalam paket serah terima formal, apa yang harus dibuang tanpa ampun, dan bagaimana menyusun struktur arsip sehingga pihak asing independen dapat memverifikasi integritasnya sepuluh tahun setelah kru penguji dibubarkan dari lokasi.

## Apa yang Harus Disimpan: Tujuh Artefak Esensial

Paket serah terima formal harus memuat tujuh artefak bernomor yang terpisah. Jika salah satu dari ketujuh artefak ini hilang, paket tersebut dinyatakan tidak lengkap:

### Artefak 1: Laporan Kilat Eksekutif Satu Halaman
Lembar ringkasan definitif yang didefinisikan dalam Bab 1 dan diilustrasikan dalam Gambar 01:
- Metadata larian (ID Larian, lokasi fasilitas, tanggal, revisi spesifikasi yang dirujuk).
- Tabel lima kelulusan skenario (Prates, Gradien, Beban Lebih, Perubahan Langkah, Gangguan Pasokan Tunggal) dengan nilai terukur, durasi jeda, dan penilaian eksplisit LULUS/GAGAL/TIDAK DIJALANKAN.
- Klausul penilaian pengujian keseluruhan.
- Tanda tangan tinta basah atau kriptografis dari keempat peran yang ditunjuk (Pemilik Lembar, Operator, Pencatat, Orang Asing).

### Artefak 2: Sertifikat Persiapan dan Garis Dasar
Dokumentasi yang membuktikan bahwa kluster uji layak diuji sebelum pemanasan diperintahkan:
- Empat gerbang persiapan yang telah diverifikasi dan ditandatangani.
- Log stabilisasi dingin 10 menit, termasuk nilai rata-rata garis dasar satu menit.
- Catatan kalibrasi impedansi hidrolik dingin, yang mencantumkan posisi katup penyeimbang terkunci dan tekanan diferensial garis dasar (ΔP).

### Artefak 3: Lembar Konsistensi Multikabinet
Evaluasi statistik terhadap keseimbangan kluster di seluruh bank beban paralel:
- Koefisien Variasi (CV) terhitung untuk daya aktif listrik (CV ≤ 1,0%), aliran pendingin (CV ≤ 5,0%), kenaikan suhu (CV ≤ 3,0%), dan tekanan manifold (CV ≤ 5,0%).
- Pemeriksaan varians bukan-nol tersertifikasi (σ² > 0) yang membuktikan bahwa aliran turbulen langsung hadir dan tidak ada saluran yang menggemakan data *cache*/beku.

### Artefak 4: Blok Data Langkah dan Tabel Penutupan Entalpi
Neraca termodinamika lengkap untuk setiap langkah beban (25%, 50%, 75%, 100%, 110%):
- Statistik Empat Ringkasan (Minimum, Maksimum, Rata-Rata Aritmatika, Deviasi Standar) untuk semua saluran listrik, cairan, dan udara.
- Keseimbangan energi termodinamika prinsip pertama: daya listrik aktif (P_elec) dibandingkan terhadap entalpi cairan (Q_liquid = ṁ C_p ΔT) dan kalor sensibel udara pendamping (Q_air).
- Rasio Penutupan Entalpi tersertifikasi (≥ 97,0%).

### Artefak 5: Osilogram dan Grafik Deret Waktu
Grafik beresolusi tinggi berkualitas vektor yang dihasilkan dari data mentah yang tidak dapat diubah:
- Bentuk gelombang daya dan suhu yang dihamparkan untuk semua unit paralel, diplot pada skala yang secara jujur memperlihatkan divergensi kabinet individual.
- Plot respons perubahan langkah dinamis beranotasi, yang memerinci waktu penstabilan dan denyut tekanan hidrolik puncak.
- Osilogram transien kehilangan pasokan tunggal 2N, yang menangkap pemutusan kontaktor (< 20 ms) dan stabilitas bus kendali tanpa penurunan tegangan (*zero-dip*).

### Artefak 6: Log Audit Anomali dan Titik Perubahan (*Changepoint*) Algoritmik
Log lengkap telaah algoritmik otomatis:
- Waktu pemicu kandidat Focus dan FLOC daring yang dibandingkan secara kronologis terhadap log perintah Operator.
- Segmen kemiringan linear searah potongan CPOP luring di seluruh kotak jeda tunak.
- Label klasifikasi manusia yang diparaf untuk setiap kandidat: *Langkah Terduga (Expected Step)*, *Inspeksi / Pisahkan Penahanan (Inspect / Split Hold)*, atau *Tidak Berdampak (No Impact)*.

### Artefak 7: Arsip Data CSV Mentah Bertanda Tangan Kriptografis
Berkas telemetri mentah 1 detik penuh tanpa rekayasa yang diekspor langsung dari *edge gateway*:
- Setiap saluran sensor aktif dicatat sekali per detik dengan stempel waktu UTC ISO-8601.
- Disertai dengan berkas *checksum* kriptografis SHA-256 formal (misalnya, `LB_TEST_2026_H01_RAW.csv.sha256`) yang dibuat segera setelah penutupan berkas, menjamin bahwa angka mentah belum pernah dimodifikasi, difilter, atau diedit secara retroaktif.

## Apa yang Harus Dibuang Tanpa Kompromi

Paket serah terima formal adalah rekaman audit rekayasa, bukan portofolio iklan. Butir-butir berikut harus dikeluarkan secara tegas:

- **Foto Ponsel Cerdas Tanpa Kalibrasi**: Jangan menyertakan puluhan foto ponsel cerdas buram dari lampu panel yang menyala, wajah operator, atau bundel kabel. Foto LED hijau adalah cinderamata; itu bukan bukti kontinuitas listrik atau entalpi fluida. (Tangkapan pencitraan termal beresolusi tinggi dengan skala suhu terkalibrasi hanya diizinkan sebagai dokumentasi pendukung untuk pemeriksaan sepatu kabel terminal).
- **Brosur Pemasaran Vendor & Render 3D**: Jangan menggelembungkan dokumen dengan brosur penjualan mengilap, seni konsep hasil komputer, atau salindia profil perusahaan. Paket audit adalah milik mesin fisik di lantai uji, bukan brosur penjualan.
- **Data Klien Rahasia Tanpa Redaksi**: Jangan menyertakan identitas penyewa pelanggan, nama model AI kepemilikan (*proprietary*), kode akses keamanan tanpa redaksi, atau alamat IP jaringan internal perusahaan. Laporan ini memverifikasi kinerja termodinamika dan listrik; bukan memetakan jaringan data privat.
- **Pembuangan Log Mentah Multi-Gigabita Tanpa Indeks**: Jangan menempelkan jutaan baris log JSON mentah tanpa format atau keluaran terminal mentah ke dalam lampiran PDF. Simpan arsip CSV mentah di repositori digital aman terpisah, sitasi *hash* SHA-256-nya, dan jaga agar PDF laporan formal tetap bersih, mudah dibaca, dan terfokus.

## Struktur Folder Arsip

Susun paket serah terima digital akhir ke dalam struktur direktori folder yang bersih dan terstandarisasi:

```
├── 01_Executive_Flash_Report.pdf # Ringkasan 1 halaman bertanda tangan
├── 02_Preparation_and_Baseline.pdf # Gerbang dingin & kalibrasi hidrolik
├── 03_Consistency_and_Uniformity.pdf # Perhitungan CV & keseimbangan multikabinet
├── 04_Step_Data_Blocks_and_Enthalpy.pdf # Tabel rekonsiliasi termodinamika
├── 05_Time_Series_Charts.pdf # Osilogram resolusi tinggi & langkah dinamis
├── 06_Changepoint_Audit_Log.pdf # Log kandidat Focus / FLOC / CPOP
├── 07_Raw_Telemetry_Archive/
│ ├── LB_RAW_1HZ_TELEMETRY.csv # Berkas data mentah 1 detik lengkap
│ └── LB_RAW_1HZ_TELEMETRY.csv.sha256 # Hash kriptografis SHA-256 yang tidak dapat diubah
└── 08_Calibration_Certificates/
 ├── PT100_RTD_Calibration.pdf # Lembar kalibrasi NIST/ISO 17025
 ├── Vortex_Flow_Meter_Cal.pdf # Sertifikat kalibrasi aliran dari pabrik
 └── Power_Transducer_Class02.pdf # Tag kalibrasi pengukur listrik
```

Ketika seorang auditor atau agen komisioning menerima paket ini, mereka dapat memverifikasi *hash* SHA-256 dari berkas CSV mentah dalam lima detik, menjalankan ulang perhitungan agregasi di Python, dan mengonfirmasi secara independen setiap angka pada laporan kilat eksekutif.

Itulah standar dari sebuah panduan lapangan rekayasa.

## Keputusan yang Harus Dicatat

Sebelum menyegel paket serah terima formal, verifikasi dan dokumentasikan:

- *Checksum* SHA-256 terhitung dari berkas telemetri CSV mentah, yang ditandatangani oleh Pencatat.
- URI penyimpanan arsip atau lokasi repositori tempat berkas-berkas mentah yang tidak dapat diubah disimpan.
- Daftar semua sertifikat kalibrasi instrumen yang disertakan beserta tanggal kedaluwarsanya.
- Tanda tangan penerimaan akhir dari Pemilik Lembar dan CxA Pihak Ketiga.
