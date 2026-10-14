Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 11. Daftar Cacat

Cacat instalasi atau kegagalan kinerja yang tidak dicatat dalam Log Masalah Komisioning (*Commissioning Issues Log*) resmi secara hukum dianggap tidak pernah ada. Meskipun kelalaian ini mungkin menguntungkan bagi kontraktor yang terburu-buru melakukan demobilisasi, hal ini menghadirkan bahaya operasional yang tidak dapat diterima bagi tim operasi fasilitas yang harus mengoperasikan aula begitu beban TI aktif tiba.

Daftar cacat master (*master punch list*) ditetapkan selama Rapat Perdana Komisioning, bukan setelah kebocoran cairan pendingin sekunder pertama ditemukan. Setiap entri yang dicatat harus memuat deskripsi yang tegas dan jelas yang dapat dipahami oleh auditor eksternal: label peralatan spesifik, referensi P&ID yang mengatur, nomor langkah skrip yang gagal, mode kegagalan, kontraktor yang ditugaskan, tindakan remediasi yang diperlukan, dan kriteria pengujian ulang spesifik yang disyaratkan untuk penutupan. Entri log yang samar seperti "masalah CDU" sama sekali tidak dapat diterima.

![Matriks Tata Kelola Daftar Cacat](../figures/fig-07-punchlist-governance-matrix.png)

## Tiga Tingkat Keparahan Cacat

Setiap temuan yang dicatat dalam Log Masalah harus diklasifikasikan ke dalam salah satu dari tiga tingkat keparahan standar:

```
+----------------------------------------------------------------------------------------------------+
| KLASIFIKASI KEPARAHAN CACAT |
+------------+-------------------------------+-------------------------------------------------------+
| TINGKAT | DEFINISI & CONTOH | DAMPAK INTERLOCK TAHAP KOMISIONING |
+------------+-------------------------------+-------------------------------------------------------+
| KATEGORI 1 | Kritis Keselamatan / Blokir: | PENGHENTIAN TOTAL MUTLAK. Melarang kelanjutan ke level|
| | Kebocoran aktif > 0 tetes/mnt;| komisioning berikutnya. Pemberian energi termal Lv 5 |
| | fasa terbalik; gagal E-Stop; | dilarang secara hukum selama ada butir Kat 1 terbuka. |
| | batas waktu pompa > 1,5 s; | |
| | isolasi < 100 MOhm. | |
+------------+-------------------------------+-------------------------------------------------------+
| KATEGORI 2 | Deviasi Operabilitas Utama: | KELANJUTAN BERSYARAT. Kelanjutan diizinkan hanya jika |
| | Penutupan entalpi < 97,0%; | Insinyur Pemilik menandatangani pelepasan deviasi dgn |
| | variasi aliran rak CV > 5,0%; | mitigasi operasional. Resolusi 14 hari kalender. |
| | sensor hanyut > 0,5 K; | Pengujian ulang wajib disyaratkan. |
| | katup kontrol berburu. | |
+------------+-------------------------------+-------------------------------------------------------+
| KATEGORI 3 | Kosmetik / Dokumen Minor: | TANPA INTERLOCK. Tidak menghambat pengujian dinamis |
| | Panah aliran pipa terbalik; | atau sertifikat tonggak capaian. Diverifikasi melalui |
| | lecet cat baki kabel; | bukti foto dalam waktu 30 hari pasca-serah terima. |
| | label kalibrasi tercoreng. | |
+------------+-------------------------------+-------------------------------------------------------+
```

## Interlock Tahap dan Protokol Pelepasan Tanggung Jawab (Waiver)

Aturan mendasar yang mengatur komisioning pusat data adalah bahwa **tidak ada proyek yang boleh melangkah melewati batas tonggak capaian selama cacat Kategori 1 yang terbuka belum terselesaikan**.

Daftar cacat adalah tempat di mana para kontraktor sering kali berusaha bernegosiasi untuk menyiasati aturan ini. Permohonan kontraktor yang menyatakan, "Kami paham katup searah primer bocor sedikit saat aliran balik, tetapi izinkan kami melanjutkan langkah pengujian panas 100% dan kami akan memperbaiki katup tersebut selama demobilisasi," harus ditolak mentah-mentah. Memulai pengujian termal beban tinggi dengan katup searah yang cacat berisiko memicu kavitasi pompa akibat aliran balik, kejutan hidrolik parah, dan terbakarnya motor pompa secara katastropik.

Jika pemilik fasilitas memutuskan untuk tetap melanjutkan pengujian meskipun terdapat deviasi operabilitas Kategori 2 yang masih terbuka demi memenuhi tenggat waktu bisnis yang kaku, keputusan tersebut harus diformalkan melalui **Pelepasan Tanggung Jawab Deviasi** (*Deviation Waiver*) yang ditandatangani. Pelepasan tersebut harus menguraikan:
1. Kekurangan teknis pasti dan klausul spesifikasi yang mengatur.
2. Penilaian risiko operasional dan potensi mode kegagalan.
3. Kontrol keselamatan kompensasi spesifik yang diterapkan selama jendela pengujian.
4. Komitmen kontrak dan jadwal remediasi serta pengujian ulang yang disaksikan.

Kesepakatan lisan atau pesan teks kasual sepenuhnya tidak sah. Pelepasan tanpa dokumen tertulis hanyalah kesepakatan untuk dikejutkan oleh kegagalan operasional di kemudian hari.

## Tata Kelola Remediasi dan Pengujian Ulang (Retest)

Pembagian tanggung jawab selama penyelesaian daftar cacat harus dipertahankan secara ketat:
- **Kontraktor Pelaksana**: Melakukan perbaikan fisik di bawah izin kerja fasilitas formal.
- **Pihak Verifikasi**: Mengaudit perbaikan, memeriksa pekerjaan fisik, mengarahkan skrip pengujian ulang, dan mencatat data baru. Tim verifikasi tidak pernah memperbaiki instalasi mekanikal atau elektrikal, karena melakukan hal tersebut akan merusak postur audit independen mereka.
- **Pemilik Fasilitas**: Menyaksikan pengujian ulang dan menandatangani bersama entri penutupan.

Suatu butir daftar cacat tidak dapat ditutup hanya dengan kontraktor mengirimkan email yang menyatakan, "Teknisi telah menyesuaikan parameter katup." Menutup suatu butir butuh tingkat bukti rekayasa yang sama persis dengan yang dituntut oleh skrip asli: lembar data pengujian ulang yang dieksekusi penuh dan disaksikan, yang membuktikan bahwa parameter tersebut telah memenuhi spesifikasi.

## Lingkup Pengujian Ulang dan Batasan Komersial

Pengujian ulang yang disaksikan menimbulkan biaya nyata dalam bentuk jam kerja rekayasa, daya utilitas fasilitas, dan sewa peralatan sementara. Rencana Komisioning harus secara eksplisit mendefinisikan di awal apakah pengujian ulang tercakup dalam lingkup dasar proyek atau memerlukan perintah perubahan kontrak (*change order*) formal.

Menetapkan batasan komersial ini sejak dini mencegah perselisihan ketika pengujian yang kompleks harus diulang akibat instalasi kontraktor yang cacat. Namun demikian, negosiasi komersial tidak boleh mengorbankan standar teknis: pengujian ulang tanpa izin yang dieksekusi tanpa revisi skrip formal bukanlah verifikasi yang sah; itu hanyalah siklus operasional peralatan yang tidak tercatat.

## Cacat Meja Kerja Pasca-Demobilisasi (Desktop Defects)

Cacat tertentu baru terlihat setelah demobilisasi, ketika log telemetri berfrekuensi tinggi dan berkas CSV meteran daya dianalisis di stasiun kerja rekayasa.

Jika perhitungan keseimbangan panas entalpi mengungkapkan bahwa rasio penutupan turun menjadi 92,0% selama jam termal terakhir, atau jika analisis frekuensi mendeteksi perburuan (*hunting*) VFD beramplitudo rendah, temuan tersebut harus dicatat secara formal dalam Log Masalah master dengan tanggal penemuannya saat pasca-pemrosesan.

Pimpinan Pengujian harus membedakan secara cermat antara:
- **Cacat Akuisisi Data**: Seperti jam NTP yang tidak sinkron, format CSV yang rusak, atau transduser arus yang tidak terkalibrasi.
- **Kegagalan Instalasi Fisik**: Seperti sabuk pompa yang selip, kerak pada pelat penukar panas, atau modul thyristor yang melemah.

Mencampuradukkan kesalahan akuisisi data dengan cacat instalasi fisik membuang-buang sumber daya kontraktor untuk menginvestigasi peralatan yang sehat; sebaliknya, melabeli kegagalan instalasi fisik sebagai gangguan telemetri semata memungkinkan sistem pendinginan yang cacat diserahterimakan ke operasi TI aktif.

## Persyaratan Penutupan (Closeout)

Ketika setiap cacat Kategori 1 dan Kategori 2 yang dicatat di seluruh level komisioning yang dieksekusi telah diselesaikan sepenuhnya dan diverifikasi melalui pengujian ulang yang disaksikan, Otoritas Komisioning dapat menyertifikasi penutupan. Kesepakatan lisan selama rapat penutupan akhir bahwa "semuanya sudah beres" tidak memiliki kekuatan hukum. Log Masalah master yang telah selesai harus dicetak, ditinjau, dan ditandatangani dengan tinta oleh ketiga pihak.

## Keputusan yang Harus Dicatat Sebelum Mulai Pengujian

- Lokasi, keamanan *hosting*, dan platform perangkat lunak untuk Log Masalah master.
- Individu yang disebutkan namanya yang berwenang mencatat cacat, mengeksekusi perbaikan, menyaksikan pengujian ulang, dan menutup entri.
- Templat Pelepasan Tanggung Jawab Deviasi formal, termasuk penilaian risiko wajib dan rencana mitigasi.
- Kesepakatan komersial yang mengatur biaya pengujian ulang dan alokasi jadwal.
- Log Masalah master yang dicetak dan ditandatangani dengan semua butir diverifikasi tertutup sebelum serah terima Level 6.
