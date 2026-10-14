Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 12. Penutupan dan Serah Terima

Pengujian beban panas termal yang berhasil bukanlah serah terima fasilitas. Mendemobilisasi bank beban dari aula data hanya menandakan bahwa verifikasi dinamis telah selesai. Transisi formal fasilitas dari konstruksi ke operasi TI aktif terjadi di bawah **Level 6 Penutupan, Serah Terima, dan Pelimpahan Operasi**.

Sertifikat serah terima yang ditandatangani saat butir-butir daftar cacat belum terselesaikan atau sebelum laporan komisioning akhir diaudit secara hukum adalah cacat (*legally defective*). Serah terima Level 6 adalah tonggak capaian formal di mana Pemilik Fasilitas, Kontraktor Utama, dan Otoritas Komisioning secara kolektif menyatakan bahwa sistem mekanikal, elektrikal, dan kontrol telah memenuhi Persyaratan Proyek Pemilik dan aman untuk menerima infrastruktur komputasi berdensitas tinggi.

```
+----------------------------------------------------------------------------------------------------+
| ARSITEKTUR DOKUMEN SERAH TERIMA LEVEL 6 |
+----+--------------------------------+--------------------------------------------------------------+
| 01 | RINGKASAN EKSEKUTIF & PERNYATAAN| Kalimat klaim tertandatangani, penilaian proyek akhir, & |
| | KLAIM TERVERIFIKASI | ringkasan kapasitas termal operasional yang didemonstrasikan.|
+----+--------------------------------+--------------------------------------------------------------+
| 02 | BATASAN LINGKUP & SURAT | Surat lingkup eksplisit mendokumentasikan level yg tdk |
| | PENGECUALIAN | dieksekusi, uji musiman ditangguhkan, & sistem pihak ketiga. |
+----+--------------------------------+--------------------------------------------------------------+
| 03 | SERTIFIKAT TONGGAK CAPAIAN | Sertifikat penyelesaian formal bertandatangan utk Level |
| | MASTER | 2, 3, 4, dan 5. |
+----+--------------------------------+--------------------------------------------------------------+
| 04 | TUJUH LEMBAR MASTER BERTANDA | Lembar 1 hingga 7, dieksekusi penuh, dicatat tinta, ttd. |
| | TANGAN | |
+----+--------------------------------+--------------------------------------------------------------+
| 05 | LOG KALIBRASI INSTRUMEN | Sertifikat kalibrasi ISO 17025 tertelusur utk seluruh alat. |
+----+--------------------------------+--------------------------------------------------------------+
| 06 | REPOSITORI DATA DERET WAKTU | Log CSV mentah lengkap, ekspor tren BMS, SHA kriptografis. |
+----+--------------------------------+--------------------------------------------------------------+
| 07 | REGISTER MASALAH TERSELESAIKAN | Log Cacat Master menunjukkan 100% butir Kat 1 & 2 tertutup. |
+----+--------------------------------+--------------------------------------------------------------+
| 08 | SUPLEMEN MANUAL SISTEM | Kurva pompa hasil uji, rentang operasi, setpoint aman-gagal. |
+----+--------------------------------+--------------------------------------------------------------+
| 09 | REKAMAN PELATIHAN OPERASI | Persetujuan bersaksi atas tinjauan SOP staf fasilitas. |
+----+--------------------------------+--------------------------------------------------------------+
```

## Struktur Laporan Komisioning Akhir

Laporan Komisioning Akhir adalah garis dasar rekayasa permanen dari infrastruktur pendinginan cairan. Beberapa dekade kemudian, ketika fasilitas mengalami perombakan (*retrofit*) atau investigasi kegagalan, tim rekayasa akan merujuk ke laporan ini untuk memverifikasi parameter operasi awal.

Laporan harus disusun dengan sembilan bagian standar:

### 1. Ringkasan Eksekutif dan Pernyataan Klaim Tersertifikasi
Dibuka dengan kalimat klaim pasti tanpa perubahan sebagaimana dirumuskan dalam Bab 1. Bagian ini memberikan ringkasan operasional yang tegas: total kapasitas termal yang diverifikasi (misalnya, 1,2 MW kontinu), kondisi pasokan pendingin primer, metrik keseimbangan aliran sekunder, dan sertifikasi formal bahwa semua sistem yang diuji beroperasi dalam spesifikasi.

### 2. Batasan Lingkup dan Surat Pengecualian Formal
Definisi batasan yang ketat. Jika tinjauan desain Level 0 atau pengujian pabrik Level 1 dikecualikan dari kontrak, Surat Pengecualian Lingkup formal yang ditandatangani oleh pemilik harus disematkan di sini. Jika pengujian musiman (seperti pengujian stres chiller pada kondisi ambien musim panas maksimum) harus ditangguhkan ke tanggal berikutnya, Protokol Pengujian yang Ditangguhkan (*Deferred Testing Protocol*) dan tanggal eksekusi terjadwal harus didokumentasikan secara formal.

### 3. Sertifikat Penyelesaian Tonggak Capaian Master
Halaman sertifikat formal untuk Level 2 (QA Penerimaan), Level 3 (PFC dan Startup), Level 4 (FPT Sistem Tunggal), dan Level 5 (IST Sistem Terintegrasi). Setiap sertifikat harus memuat tanda tangan tinta dari Pimpinan Komisioning, Insinyur Elektro, Insinyur Mesin, Eksekutif Kontraktor, dan Perwakilan Berwenang Pemilik.

### 4. Tujuh Lembar Lapangan Master
Lembar rekaman lapangan fisik yang telah selesai (Lembar 1 hingga 7 dari Bab 16), dipindai penuh warna yang memperlihatkan semua entri tinta, inisial saksi, stempel waktu langkah, dan catatan lapangan.

### 5. Register Instrumen Terkalibrasi
Log ketertelusuran lengkap yang mencantumkan setiap multimeter, penganalisis kualitas daya, pengukur aliran ultrasonik, termometer digital, pemancar tekanan diferensial, dan kamera pencitraan termal yang digunakan selama pengujian. Sematkan salinan sertifikat kalibrasi ISO/IEC 17025 masing-masing instrumen.

### 6. Repositori Data Deret Waktu Mentah
Arsip terstruktur yang memuat ekspor telemetri mentah 1 detik dari bank beban, meteran daya, dan log tren BMS. Untuk mencegah manipulasi pasca-pengujian, buat fungsi *hash* kriptografis (*checksum* SHA-256) untuk setiap berkas data mentah dan catat tabel *hash* tersebut di dalam lampiran laporan.

### 7. Register Masalah Master Terselesaikan
Salinan cetak final dari Log Masalah Komisioning. Setiap cacat Kategori 1 dan Kategori 2 harus memperlihatkan riwayat resolusi lengkapnya: temuan awal, perbaikan kontraktor, referensi lembar data pengujian ulang yang disaksikan, dan tanda tangan penutupan. Setiap butir kosmetik Kategori 3 yang masih terbuka harus diikat oleh rencana penutupan 30 hari yang disetujui.

### 8. Suplemen Operasional Manual Sistem
Jembatan operasional antara data komisioning dan operasi fasilitas harian. Bagian ini mengekstrak karakteristik garis dasar kritis dari data pengujian:
- Kurva pompa dingin tanpa panas terverifikasi versus titik-titik operasi panas (Lembar 6).
- Parameter *loop* PID terkalibrasi untuk katup modulasi primer (TCV-101).
- Inventaris fluida sekunder pasti (V_total) dan konsentrasi glikol (diverifikasi refraktometer 25,0% ± 0,5%).
- Matriks logika interlock darurat, yang mendefinisikan ambang batas trip perangkat keras.

### 9. Persetujuan Pelatihan Tim Operasi
Dokumentasi pelatihan serah terima operasional formal yang dilakukan bersama para insinyur fasilitas lokasi. Pelatihan harus mencakup peninjauan fisik mekanisme penghentian darurat, pengoperasian katup bypass manual, prosedur penambahan fluida sekunder, dan alur kerja pengakuan (*acknowledgement*) alarm.

## Pernyataan Batas Halaman Terakhir

Halaman terakhir dari laporan harus melindungi pihak penguji dan pemilik dengan menyatakan secara jelas apa yang tidak dicakup oleh verifikasi:

```
+----------------------------------------------------------------------------------------------------+
| PERNYATAAN BATAS FORMAL |
| |
| "Kampanye verifikasi ini menyertifikasi kinerja infrastruktur pendinginan cairan di bawah kondisi |
| simulasi beban listrik dan termal sebagaimana didokumentasikan secara eksplisit di sini. Ini tidak |
| menyertifikasi keandalan operasional, throughput beban kerja komputasi, atau kepatuhan garansi |
| perangkat keras TI produksi. Sistem yang ditandai sebagai dikecualikan atau tidak didemonstrasikan |
| tetap berada di luar lingkup sertifikasi ini. Semua kapasitas yang terverifikasi bergantung pada |
| pengoperasian fasilitas di dalam batas lingkungan, listrik, dan hidrolik yang ditetapkan dalam |
| laporan ini." |
+----------------------------------------------------------------------------------------------------+
```

## Keputusan yang Harus Dicatat Sebelum Mulai Pengujian

- Templat laporan akhir dan format arsip dokumentasi.
- Konfirmasi bahwa 100% butir daftar cacat Kategori 1 dan Kategori 2 telah ditutup.
- Register *checksum* kriptografis SHA-256 untuk semua berkas telemetri mentah.
- Sertifikat Serah Terima Level 6 formal, ditandatangani oleh semua pemangku kepentingan utama.
- Register Pelatihan Operasi Fasilitas yang ditandatangani dan suplemen Manual Sistem.
