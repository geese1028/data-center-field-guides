Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 15. Lembar Mana yang Harus Dipegang

Bab 16 menyediakan tujuh lembar rekaman rekayasa master. Cetak lembar-lembar ini di atas kertas tahan air, susun dalam binder lapangan khusus, dan bawalah ke lantai kerja aula data.

Jangan mencoba meringkas kisi-kisi ini menjadi paragraf deskriptif tingkat tinggi setelah pengujian selesai, lalu membuang data mentah lapangan. Seorang auditor yang memeriksa paket verifikasi mengharapkan untuk melihat torehan tinta asli, entri berstempel waktu, inisial saksi, dan nomor seri instrumen yang dicatat saat berdiri di lorong aula.

```
+----------------------------------------------------------------------------------------------------+
| TUJUH LEMBAR LAPANGAN MASTER |
+-------+-------------------------------+-------------+------------------+---------------------------+
|LEMBAR | JUDUL & LINGKUP VERIFIKASI | TINGKAT CX | PENANGGUNG JAWAB | WAKTU EKSEKUSI WAJIB |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 01 | QA Statis Pra-Pemberian Energi| Level 2 / 3 | Insinyur Elektro | Sebelum menutup pemutus |
| | & Uji Penahanan Hidrolik | | & Insinyur Mesin | pasokan / membuka fluida. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 02 | Proteksi CDU Otonom & Injeksi | Level 4 FPT | Insinyur Kontrol | Sebelum memasukkan beban |
| | Alarm Fisik | | & Insinyur Mesin | termal ke dalam loop. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 03 | Tangga Termal Bertingkat & Log| Level 5 IST | Pimpinan Uji & | Satu salinan terpisah |
| | Penutupan Panas Entalpi | | Teknisi Uji | per anak tangga termal. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 04 | Kegagalan Transien Dinamis & | Level 5 IST | Pimpinan Uji & | Dieksekusi pd beban 100% |
| | Log Ketahanan Redundansi | | Insinyur Kontrol | saat simulasi gangguan. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 05 | Protokol Pemadaman Energi | Penutupan | Pimpinan Uji & | Dieksekusi urutan ketat |
| | Terkendali & Demobilisasi | Level 6 | Insinyur Elektro | saat pemadaman giliran. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 06 | Kurva Pompa Garis Dasar Dingin| Level 4 / 5 | Insinyur Mesin & | Dieksekusi pd 20°C dgn |
| | & Resistansi Loop Tanpa Panas | | Teknisi Uji | modulasi VFD dikunci mati.|
+-------+-------------------------------+-------------+------------------+---------------------------+
| 07 | Logika Kontrol Otonom CDU & | Level 4 / 5 | Insinyur Kontrol | Dieksekusi seluruh unit |
| | Audit Antarmuka Pengawas | | & Spesialis Vendor| dgn logika vendor terlampir|
+-------+-------------------------------+-------------+------------------+---------------------------+
```

## Aturan Eksekusi di Lantai Kerja

1. **Dua Orang Memegang Perkakas**: Satu insinyur mengoperasikan instrumen pengukuran terkalibrasi; insinyur kedua mencatat nilai terukur dengan tinta. Jangan pernah mencoba membaca layar, mengingat angkanya, dan menuliskannya lima menit kemudian.
2. **Setiap Sel Adalah Kewajiban**: Sel kosong adalah perintah henti otomatis (*automated stop*). Jika suatu parameter tidak termasuk dalam lingkup pengujian spesifik ini, tandai sebagai **"N/A (Di Luar Lingkup per Klaim Rev [X])"** dan bubuhkan paraf pada entri tersebut. Jangan pernah meninggalkan sel dalam keadaan kosong.
3. **Salin Lembar 3 per Tahap Termal**: Lembar 3 bukanlah formulir tunggal. Cetak beberapa salinan. Eksekusi Lembar 3 yang lengkap dan terpisah untuk setiap anak tangga dalam tangga termal (25%, 50%, 75%, 100%, dan 110%). Jangan pernah menggabungkan data dari beberapa langkah beban ke dalam satu lembar.
4. **Lampirkan Checksum Telemetri Mentah**: Catat nama berkas dan *checksum* SHA-256 dari log CSV berfrekuensi tinggi yang sesuai langsung pada tajuk (*header*) setiap lembar.
5. **Tanpa Perubahan Berlaku Surut**: Jika suatu entri salah ditulis, buat satu garis horizontal pada kesalahan tersebut, tuliskan nilai yang benar di sampingnya, dan bubuhkan paraf pada koreksi tersebut. Jangan pernah menggunakan cairan koreksi (*tipp-ex*) atau mencoret-coret tebal di atas entri lapangan.

## Penyusunan Binder Fisik

Atur binder lapangan fisik menjadi tujuh tab khusus yang sesuai dengan ketujuh lembar kerja. Awali setiap tab dengan revisi skrip pengujian yang disetujui dan sertifikat kalibrasi instrumen yang disyaratkan untuk fase tersebut.

Ketika pengujian selesai, binder fisik ini dipindai penuh warna dan membentuk inti permanen dari Laporan Komisioning Akhir Level 6.
