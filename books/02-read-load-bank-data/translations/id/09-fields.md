Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 9. Kolom Otomatis dan Penilaian Manusia

Platform komisioning modern menggunakan skrip penyerapan data otomatis, *pipeline* Python, dan dasbor *cloud* untuk menyerap ribuan titik telemetri Modbus dan MQTT per detik. Otomatisasi sangat efisien, konsisten, dan kebal terhadap kelelahan perhitungan manual.

Namun, skrip otomatis yang menghitung angka tidak boleh disamakan dengan skrip otomatis yang memberikan penerimaan teknis.

Laporan kilat (*flash report*) menetapkan batas tegas antara dua kategori sel yang berbeda:
1. **Sel yang Diisi Skrip**: Kuantitas aritmatika dan statistik yang dihitung secara deterministik dari telemetri mentah.
2. **Sel yang Diisi Manusia**: Penilaian kualitatif, penentuan kepatuhan kontraktual, dan tanda tangan hukum penerimaan teknis.

Sebuah algoritma tidak memiliki lisensi rekayasa profesional, tidak dapat hadir di pengadilan, dan tidak dapat memikul tanggung jawab finansial atau operasional atas kebakaran aula data. Algoritma menghitung angka; manusia menuliskan penilaiannya.

## Apa yang Boleh Diisi oleh Skrip

Skrip otomatis, *pipeline* penyerapan data, dan kueri agregasi basis data sangat ideal untuk matematika deterministik. Sebuah skrip boleh—dan harus—mengisi kolom-kolom berikut tanpa intervensi manusia:

- **Stempel Waktu dan Jumlah Sampel**: Waktu mulai dan selesai yang tepat hingga milidetik, durasi jeda dalam detik, dan jumlah total sampel mentah 1 detik valid yang diterima per saluran.
- **Ringkasan Statistik**: Rata-rata aritmatika (μ), nilai minimum ($\min$), maksimum ($\max$), deviasi standar sampel (σ), dan varians (σ²) di seluruh jendela waktu yang ditentukan.
- **Perhitungan Fisik Turunan**: Laju aliran massa (ṁ), densitas limbak fluida (ρ), kapasitas kalor spesifik (C_p), penyerapan entalpi cairan (Q_liquid), dan kalor sensibel udara pendamping (Q_air).
- **Metrik Multikabinet**: Rata-rata kelompok, deviasi standar kelompok, dan Koefisien Variasi (CV) di seluruh kabinet paralel.
- **Rasio Penutupan Entalpi**: Persentase penutupan yang tepat antara daya listrik aktif dan disipasi kalor termodinamika total (P_elec vs Q_liquid + Q_air).
- **Bendera Anomali Algoritmik**: Peringatan otomatis yang mengindikasikan garis datar varians-nol (σ² ≤ 1,0 × 10^{-4}), celah komunikasi yang hilang, pembacaan sensor di luar batas, dan waktu pemicu kandidat titik perubahan (*changepoint*) dari Focus, FLOC, atau CPOP.

Komputer mengeksekusi aritmatika jauh lebih cepat dan dengan presisi yang jauh lebih tinggi daripada manusia dengan kalkulator saku. Biarkan skrip melakukan aritmatikanya.

## Apa yang Dilarang Keras Ditulis oleh Skrip

Dalam keadaan apa pun, skrip otomatis, makro dasbor, atau model AI tidak boleh menghasilkan kata-kata:
- **LULUS (*PASS*)**
- **GAGAL (*FAIL*)**
- **TIDAK DIJALANKAN (*NOT RUN*)**
- **DIABAIKAN / DIBERI DISPENSASI (*WAIVED*)**

Skrip otomatis yang mengevaluasi suatu baris, melihat bahwa suhu terhitung adalah 45,1°C terhadap batas atas 46,0°C, lalu secara otomatis membubuhkan kata "LULUS" pada PDF telah melampaui wewenangnya.

### Mengapa "Lulus" Otomatis Berbahaya
Pertimbangkan apa yang tidak dapat diketahui oleh algoritma:
- Algoritma tidak tahu bahwa RTD yang melaporkan 45,1°C secara tidak sengaja terpasang pada cabang pipa buntu (*dead-leg*) yang dingin dan bukan pada aliran aktif.
- Algoritma tidak tahu bahwa selang *bypass* sementara tertekuk di belakang kabinet, atau bahwa penyetelan katup manual yang tidak tercatat telah dilakukan selama penahanan beban.
- Algoritma tidak tahu bahwa klien mengeluarkan buletin lisan darurat pagi itu yang menurunkan batas koridor pengujian dari 46,0°C menjadi 44,0°C.

Skrip otomatis yang menuliskan "LULUS" meninabobokan tim rekayasa ke dalam rasa aman palsu. Operator berhenti memeriksa pipa fisik, berhenti mendengarkan kavitasi pompa, dan berhenti memverifikasi tanda kalibrasi instrumen, dengan asumsi bahwa "perangkat lunak yang mengurus kepatuhan."

Dalam panduan lapangan ini, sel-sel penilaian pada templat laporan kilat terlahir dalam kondisi kosong. Sel tersebut hanya dapat diisi oleh tangan manusia menggunakan pena bertinta atau tanda tangan kriptografis digital yang terotentikasi.

## Kejahatan Penimpaan (*Override*) oleh Manusia

Moda kegagalan sebaliknya juga sama berbahayanya: seorang manusia yang melihat sel matematika yang gagal dihitung oleh skrip lalu menimpa penilaian tersebut dengan "LULUS" yang tidak sah.

Jika skrip dengan benar menghitung bahwa CV aliran adalah **7,2%** terhadap ambang batas maksimum **5,0%**, seorang insinyur tidak boleh menuliskan "LULUS" di samping sel tersebut dan menambahkan alasan lisan: *"Aliran memang sedikit tidak rata, tetapi pendinginan secara keseluruhan terlihat baik-baik saja."*

Tindakan tersebut bukanlah interpretasi rekayasa. Itu adalah pengabaian/dispensasi (*waiver*) tidak tercatat yang tidak sah.

Jika sel terhitung gagal:
- Penilaian manusia untuk baris tersebut harus **GAGAL (*FAIL*)**.
- Jika tim proyek benar-benar yakin bahwa kegagalan tersebut tidak mengorbankan tujuan komisioning yang lebih luas, Pemilik Lembar harus menerapkan **Protokol Dispensasi (*Waiver Protocol*)** formal:
 1. Merevisi spesifikasi dasar desain untuk memperlebar toleransi secara eksplisit dari 5,0% menjadi 7,5%;
 2. Menetapkan tanda revisi dokumen baru (misalnya, Rev 2.5);
 3. Mengklasifikasi ulang klaim tersebut secara formal sebagai batasan yang diketahui;
 4. Memperoleh otorisasi tertulis dan bertanda tangan dari pemilik fasilitas.

Dispensasi yang dieksekusi secara terang-terangan dengan revisi dokumen yang diperbarui adalah keputusan rekayasa yang dapat diaudit. Sebuah "LULUS" dari manusia yang ditulis di atas sel yang gagal di dalam kegelapan lembar sebar (*spreadsheet*) adalah pemalsuan rekaman pengujian.

## Merancang Antarmuka Dua Kolom

Untuk menegakkan disiplin ini dalam perangkat lunak dan dokumen cetak, setiap templat laporan kilat harus menerapkan **Antarmuka Dua Kolom** yang ketat:

| Kolom Kiri: Blok Data Otomatis (Milik Skrip) | Kolom Kanan: Evaluasi & Penilaian (Milik Manusia) |
| :--- | :--- |
| • Daya yang Diperintahkan: 120,0 kW | • Sitasi Batas yang Dirujuk: DOC-SPEC Rev 2.4, Tabel 2 |
| • Daya Terukur: 120,2 kW | • Keseimbangan Penyulang Terverifikasi: Ketidakseimbangan fasa < 1,0% |
| • Kalor Cairan Terinferensi: 98,6 kW | • Kelayakan Termodinamika: Terkonfirmasi |
| • Penutupan Entalpi: 98,0% | • Inspeksi Fisik Perangkat Keras: Tidak ada kebocoran / Suara normal |
| • CV Aliran Terhitung: 2,95% (σ = 5,21 LPM) | • Verifikasi Konsistensi: Lulus dalam ambang batas 5,0% |
| • Masker Kualitas: 0x0007 (Valid, σ² > 0) | • **Penilaian Manusia**: **LULUS** [Paraf: E.V., Lead CxA] |

Kolom kiri memuat angka-angka mentah tanpa rekayasa yang dihasilkan oleh kode program. Kolom kanan memuat telaah manusia, pemeriksaan verifikasi manual, dan tanda tangan penanggung jawab akhir.

## Keputusan yang Harus Dicatat

Di bagian tata kelola pada laporan kilat, catat:

- Versi perangkat lunak, *checksum* skrip (*hash* SHA-256), dan *branch* repositori dari *pipeline* agregasi data otomatis.
- Pernyataan tersertifikasi bahwa semua sel penilaian (Lulus/Gagal/Tidak Dijalankan) telah ditinjau dan dimasukkan secara manual oleh otoritas manusia yang ditunjuk.
- Setiap dispensasi formal yang diajukan selama kampanye pengujian, dengan mereferensikan revisi dokumen yang diotorisasi dan tanda tangan pemilik.
