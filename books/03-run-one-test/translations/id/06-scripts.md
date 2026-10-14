Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 6. Skrip Sebelum Beban Panas

Tidak ada pengujian komisioning dinamis yang boleh dieksekusi berdasarkan ingatan atau instruksi lisan. Pengujian yang dilakukan tanpa skrip pengujian bertahap yang telah disetujui di muka hanyalah demonstrasi peralatan informal. Hal tersebut tidak dapat menjadi dasar penerbitan sertifikat penyelesaian rekayasa.

Skrip yang disusun oleh tim penguji tetapi belum ditinjau dan ditandatangani secara formal oleh Insinyur Proyek Pemilik (*Owner’s Project Engineer*) hanyalah dokumen kerja internal. Dokumen itu tidak memiliki kekuatan kontrak. Mengeksekusi pengujian terhadap draf yang belum disetujui membuat tim penguji terpapar sepenuhnya pada perselisihan komersial dan tanggung jawab hukum jika terjadi kerusakan peralatan.

```
+----------------------------------------------------------------------------------------------------+
| HIERARKI DOKUMEN KOMISIONING |
+------------------------------------+---------------------------------------------------------------+
| 1. KODE & STANDAR | ASHRAE 0-2019, ASHRAE 90.4, NFPA 70, IEC 60364, BSRIA BG 29. |
+------------------------------------+---------------------------------------------------------------+
| 2. SPESIFIKASI KONTRAK & BOD | CSI Div 23 & 26, Persyaratan Proyek Pemilik, P&ID As-Built. |
+------------------------------------+---------------------------------------------------------------+
| 3. RENCANA KOMISIONING (Cx Plan) | Aturan tata kelola, gerbang level, protokol saksi, jadwal. |
+------------------------------------+---------------------------------------------------------------+
| 4. PROSEDUR UJI FUNGSIONAL (FPT) | Skrip bertahap disetujui di muka dgn rentang numerik pasti. |
+------------------------------------+---------------------------------------------------------------+
| 5. LEMBAR MASTER LAPANGAN (TINTA) | Rekaman lantai tertulis tinta; berkas deret waktu mentah. |
+------------------------------------+---------------------------------------------------------------+
```

## Anatomi Skrip Pengujian yang Dapat Diaudit

Setiap skrip Prosedur Uji Fungsional (*Functional Test Procedure* - FPT) dan Uji Sistem Terintegrasi (*Integrated System Test* - IST) harus disusun dengan bagian-bagian rekayasa yang konsisten dan dapat diaudit:

1. **Lingkup dan Batas Pengujian**: Komponen mekanikal dan elektrikal spesifik yang diuji, dan batas fisik pasti yang memisahkannya dari peralatan operasional di sekitarnya.
2. **Dokumen Referensi yang Mengatur**: Sitasi langsung dari revisi P&ID yang mengatur, diagram satu garis (*single-line diagram* - SLD) elektrikal, dan berkas pengajuan peralatan (*equipment submittals*). Setiap toleransi harus merujuk pada klausul kontrak spesifik atau standar manufaktur; toleransi penerimaan tanpa sumber yang disitasi hanyalah opini yang tidak terverifikasi.
3. **Jadwal Instrumentasi dan Kalibrasi**: Kelas instrumen spesifik, nomor seri, dan ID sertifikat kalibrasi yang disyaratkan untuk mengeksekusi prosedur.
4. **Gerbang Verifikasi Prasyarat**: Verifikasi tertulis bahwa semua persyaratan level sebelumnya (seperti pembongkaran peti kemas fisik, pemeriksaan megger tanpa energi, dan penahanan tekanan hidrostatik) telah sepenuhnya disetujui dan ditandatangani.
5. **Kontrol Keselamatan dan Batas Lingkungan**: Alat Pelindung Diri (APD) wajib, definisi batas kilatan busur (*arc-flash boundary*), penyiapan penahanan tumpahan, dan jalur penghentian darurat yang terverifikasi.
6. **Urutan Eksekusi Langkah demi Langkah**: Tabel sekuensial yang merinci setiap tindakan manual, umpan balik fisik pasti yang harus diamati, rentang toleransi numerik yang diharapkan, dan sel persetujuan khusus untuk data terukur serta inisial saksi.
7. **Kondisi Penghentian Eksplisit**: Batas operasional yang jelas yang mewajibkan penghentian pengujian segera jika terlanggar (seperti suhu pendingin sekunder melebihi 45,0°C, tekanan sekunder turun di bawah 100 kPa, atau ketidakseimbangan tegangan fasa pasokan melebihi 2,0%).

```
+----------------------------------------------------------------------------------------------------+
| STRUKTUR LANGKAH SKRIP PENGUJIAN STANDAR |
+----+-----------------------+-----------------------------+--------------------+-------+------------+
|LANG| PERINTAH TINDAKAN | HASIL FISIK YANG DIHARAPKAN | RENTANG PENERIMAAN |UKURAN |PARAF / WKT |
+----+-----------------------+-----------------------------+--------------------+-------+------------+
|4.2 | Naikkan Beban ke 50% | Daya aktif stabil | 600 kW +/- 1,5% | [ ] | Paraf: ___ |
| | (Tahap 2: total 600kW)| Suhu pasokan sekunder naik | 36,0°C +/- 0,5°C | [ ] | Waktu: ___ |
| | Tunggu: 45 menit | Rasio penutupan entalpi | 97,0% s/d 101,5% | [ ] | Lembar 3 |
+----+-----------------------+-----------------------------+--------------------+-------+------------+
```

## Membekukan Revisi Skrip di Lantai Kerja

Rapat Perdana Komisioning menetapkan status persetujuan spesifik yang disyaratkan sebelum sebuah skrip dapat dieksekusi di lantai kerja. Hanya skrip yang memuat cap status formal **"APPROVED FOR EXECUTION - REV [X]"** (Disetujui untuk Eksekusi - Rev [X]) yang diizinkan berada di aula data.

Jika selama pengujian instalasi mekanikal menunjukkan dinamika tak terduga yang tidak diantisipasi oleh skrip yang disetujui, memodifikasi skrip di lantai kerja dengan coretan pensil dilarang keras. Perubahan langsung yang tidak terkendali memungkinkan prosedur pengujian diam-diam menyesuaikan diri dengan apa pun yang kebetulan dilakukan oleh instalasi tersebut.

Ketika modifikasi prosedural memang diperlukan:
- Pimpinan Pengujian menghentikan sementara pengujian.
- Pemberitahuan Perubahan Rekayasa (*Engineering Change Notice* - ECN) formal disusun mendokumentasikan deviasi, justifikasi teknisnya, dan langkah-langkah yang diubah.
- ECN ditandatangani oleh Pimpinan Pengujian, Pimpinan Kontraktor, dan Insinyur Proyek Pemilik.
- Revisi skrip dinaikkan (misalnya, Rev 1.0 menjadi Rev 1.1) dan diterbitkan kembali.

Jika pemilik menolak ECN tersebut, pengujian dilanjutkan di bawah skrip asli, dan kegagalan instalasi untuk memenuhi hasil yang diharapkan semula dicatat dalam daftar cacat (*punch list*) master.

## Rangkaian Skrip Wajib untuk Aula Cairan Berdensitas Tinggi

Kampanye verifikasi yang lengkap membutuhkan rangkaian skrip mandiri yang komprehensif dan terpisah. Mencoba menggabungkan beberapa verifikasi operasional ke dalam satu prosedur tingkat tinggi menghasilkan dokumen yang tidak praktis yang pasti mengaburkan pemeriksaan keselamatan dan kinerja kritis.

Kampanye verifikasi membutuhkan sembilan skrip pengujian khusus:

### Fase 1: Daftar Periksa Pra-Mulai Statis (Level 2 / Level 3)
- **Skrip 01: Pembongkaran Peti Kemas Fisik, Kelurusan & QA Visual**: Verifikasi integritas sasis bank beban, perutean selang, segel fitting, dan pengikatan seismik.
- **Skrip 02: Uji Megger Listrik Tanpa Energi & Rotasi Fasa**: Pengujian resistansi isolasi (≥ 100 MΩ pada 1000V DC), kontinuitas pentanahan (≤ 0,1 Ω), dan konfirmasi urutan fasa searah jarum jam A-B-C.
- **Skrip 03: Pembilasan Loop Sekunder, Penahanan Tekanan Hidrostatik & Pembuangan Udara**: Verifikasi kecepatan pembilasan kimiawi (≥ 1,5 m/s sesuai BSRIA BG 29/2020), penahanan tekanan hidrostatik (1,5× tekanan kerja selama 2 jam tanpa penurunan tekanan), dan deaerasi otomatis.

### Fase 2: Pengujian Fungsional Sistem Tunggal (Level 4 FPT)
- **Skrip 04: Startup Otonom CDU, Garis Dasar Aliran & Tekanan**: Verifikasi profil kenaikan (*ramp*) VFD pompa kaleng, pelacakan *setpoint* tekanan diferensial manual, dan resistansi sistem dingin.
- **Skrip 05: Failover Pompa N+1 CDU & Kontrol Otonom**: Penjatuhan (*tripping*) fisik pada VFD pompa primer; verifikasi *auto-start* pompa siaga dalam waktu < 1,5 s tanpa kavitasi *loop*.
- **Skrip 06: Injeksi Alarm & Telemetri Titik-ke-Titik**: Injeksi fisik gangguan simulasi (aliran rendah sekunder, level rendah tangki ekspansi, pembasahan tali deteksi kebocoran) dan pemeriksaan silang telemetri BMS terhadap instrumentasi lokal.

### Fase 3: Pengujian Sistem Terintegrasi (Level 5 IST)
- **Skrip 07: Kurva Pompa Garis Dasar Dingin Tanpa Panas**: Pembuatan profil *head* hidrolik versus aliran melintasi 4 titik pencekikan katup manual dengan kontrol VFD otomatis dikunci mati.
- **Skrip 08: Tangga Panas Termal Bertingkat & Waktu Tunggu Beban Lebih**: Eksekusi termal bertahap (25%, 50%, 75%, 100% beban desain penuh, dan margin beban lebih 110%) dengan waktu tunggu (*dwell*) minimum 45 menit dan perendaman beban penuh selama 4 jam.
- **Skrip 09: Kegagalan Transien Dinamis & Penghentian Darurat**: Pemutusan pasokan daya primer 2N, ketahanan terhadap kehilangan air pendingin fasilitas (*facility chilled water*), dan urutan penghentian penurunan energi yang terkendali.

## Prinsip "Satu Skrip, Satu Tanda Tangan"

Setiap skrip dalam rangkaian ini berdiri sebagai dokumen kontrak independen dengan blok persetujuan khususnya sendiri. Menggabungkan kurva pompa dingin yang berhasil dan langkah beban lebih termal yang gagal ke dalam satu tanda tangan bersama akan menciptakan rekaman yang secara mendasar ambigu.

Setiap skrip harus menghasilkan penilaian tegasnya sendiri: **LULUS** (*PASS*), **GAGAL** (*FAIL*), atau **TIDAK DIEKSEKUSI** (*NOT EXECUTED*). Setiap kegagalan yang belum terselesaikan dalam suatu skrip segera menghasilkan entri dalam Log Masalah master.

## Keputusan yang Harus Dicatat Sebelum Mulai Pengujian

- Daftar lengkap seluruh sembilan skrip pengujian, dengan nomor revisi yang dibekukan dan cap persetujuan bertandatangan.
- Nomor dokumen kontrak yang mendukung setiap toleransi numerik dan rentang penerimaan.
- Proses ECN formal untuk menangani revisi di lantai kerja.
- Konfirmasi bahwa tidak ada skrip yang berada dalam status draf.
