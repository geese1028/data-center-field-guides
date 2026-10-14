Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 10. Lembar Induk Hari (Day Sheet)

Lembar Induk Hari adalah buku besar hukum, teknis, dan operasional yang mengikat dari sif pusat data.

```
+-----------------------------------------------------------------------------+
| STRUKTUR LEMBAR INDUK HARI |
| |
| [BAGIAN 1] Audit Serah Terima Pra-Sif (Gangguan, Izin, Insiden, MOP) |
| | |
| [BAGIAN 2] Registri Pekerjaan Resmi & PTW (Lingkup, LOTO, Jam Kedaluwarsa) |
| | |
| [BAGIAN 3] Log Putaran Inspeksi Fisik Sif (6 Stasiun, Parameter Multi-Sensor)|
| | |
| [BAGIAN 4] Kronologi Insiden & Eskalasi (Klasifikasi, SLA T-15 Menit) |
| | |
| [BAGIAN 5] Audit Kapasitas & Redundansi (Aturan Daya 45%, Hidrolik CDU) |
| | |
| [BAGIAN 6] Kalimat Penutup Akhir (Tanda tangan tunggal yang tidak berubah) |
+-----------------------------------------------------------------------------+
```

![Manager Shift Closeout Sheet](../figures/fig-07-manager-shift-closeout-sheet.png)

Salin judul-judul di bawah ini ke dalam perangkat lunak operasional fasilitas Anda atau buku log serah terima tercetak. Baris kosong pada Lembar Hari mewakili bagian fasilitas yang tidak Anda periksa, risiko yang tidak Anda kelola, dan pemadaman yang akan menjadi tanggung jawab Anda sendiri.

---

## 1. Sebelum Sif (Gerbang Serah Terima)

- **Tanggal Sif & Jendela Waktu**: `________________________________________`
- **Duty Manager yang Bertugas (Masuk)**: `________________________________`
- **Duty Manager yang Keluar**: `__________________________________________`
- **Standar Operasi SLA Kontraktual yang Diacu**: `_______________________`
- **Periode Pemberitahuan untuk Deviasi SLA**: `_____ Menit`
- **Apa yang Secara Eksplisit TIDAK Dijanjikan Operasi Hari Ini**: `________`
- **Personel dalam Sif & Kualifikasi Keahlian Terverifikasi**:
 - Teknisi Listrik Utama (No. Lisensi & Kedaluwarsa): `__________________`
 - Spesialis Pendingin (No. Lisensi & Kedaluwarsa): `___________________`
 - Teknisi Sif yang Bertugas: `_________________________________________`
- **Tugas / Sistem yang Tidak Dicakup oleh Roster Hari Ini**: `____________`
- **Serah Terima dari Sif Sebelumnya Dibaca, Diperiksa Fisik, & Diterima**: `[YA / TIDAK]`
- **Kondisi Gangguan/Penurunan Aktif yang Dibawa**:
 - Pencegah Kebakaran (VESDA / Gas Dinonaktifkan): `____________________`
 - Gangguan Redundansi Listrik (Bypass / N-0): `________________________`
 - Gangguan Redundansi Mekanis (VFD Manual / Pompa Tunggal): `___________`
- **Izin Kerja (PTW) Terbuka yang Dibawa & Waktu Kedaluwarsa**: `___________`
- **Insiden Aktif yang Dibawa & Pemilik Teknis yang Ditugaskan**: `________`
- **Perubahan Terjadwal untuk Jendela Hari Ini & Penerima Risiko**: `_______`

---

## 2. Pekerjaan & Pemeliharaan Resmi

- **Rutinitas Sif Reguler (SOP) Selesai**: `[YA / TIDAK]`
- **Pekerjaan Intrusif Spesifik yang Dieksekusi (Hanya MOP yang Disetujui)**:
 - Tugas 1: Tag: `_________` Lingkup: `________________` No. MOP: `_____`
 - Tugas 2: Tag: `_________` Lingkup: `________________` No. MOP: `_____`
- **Izin yang Diterbitkan Hari Ini & Cap Waktu Kedaluwarsa Tepat**:
 - No. PTW: `_________` Lokasi: `____________` Berakhir pada: `________`
- **Verifikasi Energi Nol LOTO Selesai (ID Gembok)**: `____________________`
- **Suku Cadang Kritis Diperiksa di Lokasi Kerja Sebelum Alat Disentuhkan**: `[YA / TIDAK]`
- **Perubahan yang Dieksekusi Hari Ini**:
 - ID Aset: `____________` Parameter Lama: `_______` Baru: `___________`
 - Nama Penerima Risiko: `________________` No. Persetujuan CAB: `______`
 - Rencana Pembatalan Diverifikasi Sebelum Jendela Buka: `[YA / TIDAK]`
- **Kondisi Operasi Abnormal Ditampilkan di Papan Ruang Kendali**: `[YA / TIDAK]`
- **Vendor Pihak Ketiga di Lokasi**:
 - Nama Vendor: `______________` Tuan Rumah Lokasi Ditugaskan: `________`
 - Pekerjaan Dijaga Ketat dalam Lingkup Tertulis: `[YA / TIDAK]`

---

## 3. Putaran Inspeksi Fisik Sif

- **Rute Putaran Inspeksi yang Ditelusuri**: `Stasiun 1 sampai Stasiun 6 Selesai`
- **Waktu Mulai Putaran**: `________` **Waktu Selesai**: `________`
- **Nama Teknisi**: `___________________________________________________`
- **Stasiun 1 (Switchgear MV)**: Tekanan SF6 Normal `[Y/T]` | Pegas Terisi `[Y/T]` | Tegangan Bus DC: `____ V`
- **Stasiun 2 (Transformator)**: Suhu Maks Belitan: `____ °C` | Akustik Normal `[Y/T]` | Level Minyak: `____`
- **Stasiun 3 (UPS & Baterai)**: Suhu Ambien: `____ °C` | Float DC: `____ V` | Nol Melembung/Bocor `[Y/T]`
- **Stasiun 4 (Instalasi Chiller)**: Suhu Pendekatan: `____ K` | Tekanan Oli: `____ bar` | Getaran VFD Normal `[Y/T]`
- **Stasiun 5 (Stasiun CDU)**: Tekanan Pasok TCS: `____ MPa` | Refraktometer: `____ % PG` | Baki Kering `[Y/T]`
- **Stasiun 6 (Whitespace AI)**: Delta-P Pembendungan: `____ Pa` | Suhu IR Maks PDU: `____ °C` | Kopling Kering `[Y/T]`
- **Cacat Dimasukkan ke Register CMMS Resmi Sebelum Keluar Ruangan**: `[YA / TIDAK ADA CACAT]`
- **SLA Kontraktual Dipertahankan Selama Putaran**: `[YA / TIDAK]`

---

## 4. Log Insiden & Eskalasi

- **Status Insiden**: `[NIHIL / HANYA ALARM / INSIDEN AKTIF]`
- **Klasifikasi Keparahan**: `[P1 - KRITIS / P2 - MAYOR / P3 - MINOR]`
- **Cap Waktu Penemuan**: `HH:MM:SS UTC`
- **Gejala Fisik yang Teramati (Hanya Fakta)**: `_________________________`
- **Cap Waktu EOP Dieksekusi & Kondisi Aman Dicapai**: `HH:MM:SS UTC`
- **Cap Waktu Pemberitahuan Klien Dikirim**: `HH:MM:SS UTC (<= 15 menit)`
- **Konfirmasi: Hipotesis Dihilangkan dari Pemberitahuan Klien**: `[YA / TIDAK]`
- **Insiden Diselesaikan atau Dilanjutkan ke Sif Depan**: `[SELESAI / DILANJUTKAN]`
- **Tindakan Korektif Tunggal Bertuan Hasil dari Peristiwa**: `____________`
 - Pemilik Tindakan: `____________________` Tanggal Tenggat: `___________`

---

## 5. Tata Kelola Kapasitas & Redundansi

- **Daya Kontraktual yang Dijual**: `_______ kW` (Pasal: `_______________`)
- **Daya Aktif yang Digunakan**: `_______ kW` (Cap Waktu Meter: `__________`)
- **Audit Aturan Redundansi 2N**:
 - Utilisasi Penyulang / Bus A: `_______ %` (Wajib <= 45.0%)
 - Utilisasi Penyulang / Bus B: `_______ %` (Wajib <= 45.0%)
- **Pemanfaatan Hidrolik Pendinginan Sekunder**:
 - Beban Termal CDU: `_______ kW` (Wajib <= 83% dari kapasitas PHE)
 - Laju Aliran Sekunder: `_______ LPM` | Suhu Pasokan: `_______ °C`
- **Sisa Kapasitas Setelah Kegagalan Tunggal Terburuk**:
 - Nilai Dihitung: `_______ kW` (Tanggal Studi Rekayasa: `_______________`)
 - Status: `[DIVERIFIKASI STUDI / TIDAK DIKETAHUI]`
- **Permintaan Penyalaan Beban Tanpa Verifikasi Ditolak**: `[YA / NIHIL]`

---

## 6. Penutupan Akhir Sif & Tanda Tangan

- **Semua Jendela Pemeliharaan Ditutup atau Dijeda dengan Pemilik Nama**: `[YA / TIDAK]`
- **Kondisi Operasi Abnormal Dihapus dari Papan Ruang Kendali**: `[YA / TIDAK]`
- **Berkas Serah Terima Disiapkan untuk Sif Masuk**: `[YA / TIDAK]`
- **Kalimat Mengikat Tunggal yang Dapat Anda Tanda Tangani dengan Jujur**:
 > *"Saya menyatakan berdasarkan lisensi profesional saya bahwa selama sif ini, semua sistem daya dan pendingin kritis beroperasi dalam batas SLA kontraktual, semua pekerjaan dieksekusi di bawah prosedur yang disetujui tanpa gangguan yang tidak tercatat, dan semua cacat yang tercatat memiliki pemilik nama yang bertanggung jawab."*

- **Tanda Tangan Duty Manager**: `_______________________________________`
- **Nomor Lisensi / Sertifikasi**: `_____________________________________`
- **Tanggal & Cap Waktu Tepat**: `_______________________________________`
