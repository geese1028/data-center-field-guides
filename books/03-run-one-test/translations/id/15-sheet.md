Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 15. Lembar Mana yang Harus Dipegang

Bab 16 menyediakan tujuh lembar rekaman rekayasa master. Cetak lembar-lembar ini di atas kertas tahan air, susun dalam binder lapangan khusus, dan bawalah ke lantai kerja aula data.

Jangan mencoba meringkas kisi-kisi ini menjadi paragraf deskriptif tingkat tinggi setelah pengujian selesai, lalu membuang data mentah lapangan. Seorang auditor yang memeriksa paket verifikasi mengharapkan untuk melihat torehan tinta asli, entri berstempel waktu, inisial saksi, dan nomor seri instrumen yang dicatat saat berdiri di lorong aula.

**TUJUH LEMBAR LAPANGAN MASTER**

| LEMBAR | JUDUL & LINGKUP VERIFIKASI | TINGKAT CX | PENANGGUNG JAWAB | WAKTU EKSEKUSI WAJIB |
| :--- | :--- | :--- | :--- | :--- |
| 01 | QA Statis Pra-Pemberian Energi & Uji Penahanan Hidrolik | Level 2 / 3 | Insinyur Elektro & Insinyur Mesin | Sebelum menutup pemutus pasokan / membuka fluida. |
| 02 | Proteksi CDU Otonom & Injeksi Alarm Fisik | Level 4 FPT | Insinyur Kontrol & Insinyur Mesin | Sebelum memasukkan beban termal ke dalam loop. |
| 03 | Tangga Termal Bertingkat & Log Penutupan Panas Entalpi | Level 5 IST | Pimpinan Uji & Teknisi Uji | Satu salinan terpisah per anak tangga termal. |
| 04 | Kegagalan Transien Dinamis & Log Ketahanan Redundansi | Level 5 IST | Pimpinan Uji & Insinyur Kontrol | Dieksekusi pd beban 100% saat simulasi gangguan. |
| 05 | Protokol Pemadaman Energi Terkendali & Demobilisasi | Penutupan Level 6 | Pimpinan Uji & Insinyur Elektro | Dieksekusi urutan ketat saat pemadaman giliran. |
| 06 | Kurva Pompa Garis Dasar Dingin & Resistansi Loop Tanpa Panas | Level 4 / 5 | Insinyur Mesin & Teknisi Uji | Dieksekusi pd 20°C dgn modulasi VFD dikunci mati. |
| 07 | Logika Kontrol Otonom CDU & Audit Antarmuka Pengawas | Level 4 / 5 | Insinyur Kontrol & Spesialis Vendor | Dieksekusi seluruh unit dgn logika vendor terlampir |

## Aturan Eksekusi di Lantai Kerja

1. **Dua Orang Memegang Perkakas**: Satu insinyur mengoperasikan instrumen pengukuran terkalibrasi; insinyur kedua mencatat nilai terukur dengan tinta. Jangan pernah mencoba membaca layar, mengingat angkanya, dan menuliskannya lima menit kemudian.
2. **Setiap Sel Adalah Kewajiban**: Sel kosong adalah perintah henti otomatis (*automated stop*). Jika suatu parameter tidak termasuk dalam lingkup pengujian spesifik ini, tandai sebagai **"N/A (Di Luar Lingkup per Klaim Rev [X])"** dan bubuhkan paraf pada entri tersebut. Jangan pernah meninggalkan sel dalam keadaan kosong.
3. **Salin Lembar 3 per Tahap Termal**: Lembar 3 bukanlah formulir tunggal. Cetak beberapa salinan. Eksekusi Lembar 3 yang lengkap dan terpisah untuk setiap anak tangga dalam tangga termal (25%, 50%, 75%, 100%, dan 110%). Jangan pernah menggabungkan data dari beberapa langkah beban ke dalam satu lembar.
4. **Lampirkan Checksum Telemetri Mentah**: Catat nama berkas dan *checksum* SHA-256 dari log CSV berfrekuensi tinggi yang sesuai langsung pada tajuk (*header*) setiap lembar.
5. **Tanpa Perubahan Berlaku Surut**: Jika suatu entri salah ditulis, buat satu garis horizontal pada kesalahan tersebut, tuliskan nilai yang benar di sampingnya, dan bubuhkan paraf pada koreksi tersebut. Jangan pernah menggunakan cairan koreksi (*tipp-ex*) atau mencoret-coret tebal di atas entri lapangan.

## Penyusunan Binder Fisik

Atur binder lapangan fisik menjadi tujuh tab khusus yang sesuai dengan ketujuh lembar kerja. Awali setiap tab dengan revisi skrip pengujian yang disetujui dan sertifikat kalibrasi instrumen yang disyaratkan untuk fase tersebut.

Ketika pengujian selesai, binder fisik ini dipindai penuh warna dan membentuk inti permanen dari Laporan Komisioning Akhir Level 6.
