Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 3. Layanan yang Anda Jual

Pelanggan tidak membeli tangki bahan bakar diesel Anda, penukar panas pelat titanium Anda, atau dedikasi pribadi Anda. Pelanggan membeli SLA: kontrak layanan yang ditentukan secara matematis yang menjamin ketersediaan listrik, pasokan termal, dan batas waktu eskalasi insiden. Jika Anda tidak dapat mengutip klausul yang tepat dalam perjanjian layanan induk, Anda beroperasi berdasarkan desas-desus.

```
+-----------------------------------------------------------------------------+
| MATRIKS BATAS LAYANAN |
| |
| Parameter Kontrak Batas yang Dijamin Sumber Pengukuran |
| ----------------------- ------------------------- --------------------- |
| Ketersediaan Daya AC 99.999% (Five Nines) Meter Pendapatan PDU |
| Suhu Pasokan Sekunder 25.0°C hingga 32.0°C Sensor RTD Pasokan CDU |
| Air Dingin Primer 12.0°C hingga 18.0°C Aliran/Suhu Header FWS |
| Suhu Udara (Inlet Rak) 18.0°C hingga 27.0°C Sensor Lorong Dingin |
| Waktu Notifikasi Insiden <= 15 Menit dari Deteksi Portal Klien & Telepon |
+-----------------------------------------------------------------------------+
```

## Batas Layanan Kontraktual vs. Batas Rekayasa

Pengoperasian pusat data membutuhkan pembedaan tegas antara tiga batas yang berbeda:
1. **Setpoints Desain**: Kondisi pengoperasian optimal yang diprogram ke dalam urutan kendali otomatis (misalnya, pasokan sekunder CDU pada 28.0°C, udara lorong dingin pada 22.0°C).
2. **Batas Alarm Operasional**: Ambang batas internal fasilitas yang memperingatkan teknisi untuk mengambil tindakan korektif sebelum terjadi dampak pada klien (misalnya, pasokan sekunder mencapai 30.5°C, memicu penyalaan pompa siaga atau penambahan tahap chiller).
3. **Batas Pelanggaran Kontraktual**: Batas hukum yang didefinisikan dalam SLA klien yang memicu penalti kredit layanan dan pemberitahuan wanprestasi (misalnya, pasokan sekunder melebihi 32.0°C selama > 5 menit berturut-turut, atau udara masuk rak melebihi 27.0°C).

Jangan pernah membiarkan perwakilan komersial klien memperlakukan alarm operasional internal sebagai pelanggaran layanan kontraktual. Sebaliknya, jangan pernah membiarkan tim sif Anda mengabaikan penyimpangan suhu yang melintasi ambang SLA hanya karena "suhu hanya melonjak selama tiga menit." Jika kontrak mengukur penyimpangan dalam rata-rata bergerak 60 detik, lonjakan tiga menit adalah pelanggaran SLA. Catat di log.

## Persamaan Ketersediaan

Ketersediaan pusat data (A) dihitung sebagai:

$$A = \frac{\text{Total Menit Periode} - \text{Menit Pemadaman}}{\text{Total Menit Periode}}  \times 100\%$$

Dalam kontrak kolokasi multi-penyewa dan build-to-suit hyperscale modern, "Menit Pemadaman" (Outage Minutes) didefinisikan dengan ketelitian hukum yang luar biasa:
- Apakah pemadaman memerlukan hilangnya daya pada kabel A dan B pada rak 2N sekaligus, atau apakah hilangnya redundansi pada satu kabel sudah merupakan pemadaman fraksional?
- Jika server pelanggan terus berjalan pada kabel B sementara kabel A padam, apakah jam SLA berjalan?
- Jika CDU pendingin cair turun dari pompa ganda N+1 ke operasi pompa tunggal tanpa penurunan suhu (derating), apakah telah terjadi pemadaman?

Manajer tugas harus mengetahui jawaban kontraktual atas pertanyaan-pertanyaan ini sebelum peristiwa terjadi. Saat insiden berlangsung, tidak ada waktu untuk berkonsultasi dengan penasihat hukum eksternal.

## Jam Periode Pemberitahuan

Ketika penyimpangan infrastruktur melintasi ambang SLA, jam mulai berdetik seketika:

$$\Delta t_{\text{notice}} = t_{\text{sent}} - t_{\text{detect}} \le T_{\text{contractual}}$$

Sebagian besar SLA hyperscale memerlukan pemberitahuan insiden resmi dalam waktu **15 menit** sejak deteksi awal (T_contractual ≤ 15 menit).

```
+-------------------------------------------------------------------------+
| JENDELA PEMBERITAHUAN 15 MENIT |
| |
| T = 00:00 Alarm berbunyi pada BMS/EPMS; trip terdeteksi |
| T + 05:00 Duty Manager memverifikasi peristiwa; stabilkan status aman|
| T + 10:00 Draf notifikasi insiden: Gejala, Waktu, Ruang Terdampak |
| T + 14:00 Pemberitahuan dikirim ke kontak teknis klien |
| T + 15:00 Batas waktu pemberitahuan SLA kontraktual kedaluwarsa |
+-------------------------------------------------------------------------+
```

Kegagalan umum di kalangan manajer operasi pemula adalah menunda pemberitahuan pelanggan awal saat teknisi masih menyelidiki akar penyebab masalah. Ini adalah bencana kontraktual. Klien akan memaafkan trip transformator yang berhasil distabilkan dalam beberapa menit; mereka tidak akan pernah memaafkan jika mengetahui server mereka mati dari telemetri mereka sendiri sementara manajer pusat data tetap bungkam selama empat puluh menit.

Kirim pemberitahuan pada menit ke-12. Nyatakan fakta yang teramati: cap waktu peristiwa, bus listrik atau loop pendingin yang terpengaruh, status sistem darurat saat ini, dan cap waktu pembaruan berikutnya. Jauhkan teori akar penyebab dari pesan pertama.

## Apa yang Tidak Boleh Anda Laporkan sebagai Kewajiban

Ukurlah hanya apa yang ditentukan dalam kontrak. Menghasilkan metrik operasional internal—seperti Power Usage Effectiveness (PUE), Carbon Usage Effectiveness (CUE), atau Water Usage Effectiveness (WUE) waktu nyata—sangat penting untuk rekayasa fasilitas dan pelaporan keberlanjutan perusahaan. Namun, jangan menempelkan perhitungan PUE internal ke dalam sertifikat pemenuhan SLA harian kecuali kontrak secara eksplisit menetapkan PUE sebagai parameter SLA yang dapat ditagih.

Jika rasio efisiensi bukan merupakan bagian dari kontrak komersial, mencantumkannya pada log klien harian mengubah aspirasi rekayasa internal menjadi target eksternal yang akan digunakan klien untuk menyengketakan tagihan. Pisahkan log pemenuhan kontraktual secara ketat dari analisis rekayasa internal.

## Keputusan yang Harus Dicatat

- Judul kontrak induk, nomor amandemen, dan pasal yang tepat yang mengatur layanan hari ini.
- ID meter telemetri otoritatif dan sumber jam acuan yang digunakan untuk pencatatan waktu kontraktual.
- Jendela waktu pemberitahuan kontraktual (T_contractual) dalam satuan menit.
- Setiap deviasi SLA yang teramati selama sif, dicatat dengan cap waktu mikrodetik dari perekam urutan peristiwa (SOE).
