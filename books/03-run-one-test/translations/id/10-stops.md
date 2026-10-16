Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 10. Penghentian Darurat, dan Urutan Keluar

Penghentian darurat (*emergency stop*) di aula pusat data bukanlah sekadar saran di dalam manual tanggap darurat. Itu adalah sirkuit keselamatan fisik yang dikabelkan untuk mematikan energi peralatan secara cepat dan aman.

Buku pertama telah menetapkan bahwa penghentian keselamatan internal bank beban beroperasi secara otonom dan mampu bertahan dari hilangnya jaringan pengawas. Buku ini mengatur siapa yang berwenang mengaktifkan penghentian tersebut, dan siapa yang diizinkan untuk mengabaikannya (*override*).

Aturan operasionalnya mutlak: **Tidak seorang pun boleh mengabaikan penghentian darurat setelah diserukan.** Jika seorang teknisi, asisten, atau pengamat menyerukan penghentian karena mencurigai adanya kebocoran, anomali listrik, atau kekhawatiran keselamatan pribadi, pengujian harus dihentikan seketika. Seorang Pimpinan Pengujian yang menanggapi dengan, "Tunggu sebentar, biarkan saya mengamati kurva termal selama tiga puluh detik," telah melakukan pelanggaran keselamatan yang sangat fatal. Sejak detik itu, sesi tersebut bukan lagi pengujian rekayasa; itu telah menjadi investigasi insiden formal.

![Osilogram Mode Kegagalan Dinamis](../figures/fig-06-transient-failure-scenarios.png)

## Skrip 09: Verifikasi Kegagalan Transien Dinamis

Pengujian terintegrasi di bawah Skrip 09 memvalidasi bahwa sistem pendinginan aula pusat data dapat bertahan dari gangguan fasilitas yang parah tanpa membahayakan perangkat keras komputasi. Pengujian ini mensimulasikan mode kegagalan dunia nyata dan mencatat kurva pemulihan transien yang dihasilkan pada Lembar 4:

### 1. Trip Pompa Sekunder dan Pergantian Otomatis
Dengan sistem yang beroperasi pada beban termal penuh 100% (1,2 MW), jatuhkan (*trip*) secara fisik pompa sekunder yang sedang beroperasi (Pompa P-1A):
- **Kriteria Penerimaan**: Pompa siaga (Pompa P-1B) harus mendeteksi hilangnya tekanan diferensial, menyala secara otomatis, dan memulihkan aliran *loop* desain dalam waktu ≤ 1,5 detik.
- Puncak denyut tekanan palu air (*water hammer*) saat penutupan katup searah tidak boleh melebihi ± 50 kPa.
- Tekanan diferensial *loop* sekunder tidak boleh turun di bawah batas minimum kavitasi (100 kPa).

### 2. Kehilangan Pengumpan Listrik Primer 2N Jalur A / Transfer ATS
Dengan CDU yang beroperasi di bawah distribusi daya 2N jalur ganda, jatuhkan (*trip*) pemutus arus Pengumpan Primer Jalur A (*Feeder A*):
- **Kriteria Penerimaan**: Sakelar Transfer Statis (*Static Transfer Switch* - STS) atau Sakelar Transfer Otomatis (*Automatic Transfer Switch* - ATS) harus mentransfer daya ke Pengumpan Jalur B dalam waktu ≤ 16 milidetik (kurang dari satu siklus AC).
- Bus kontrol 24V DC CDU harus mempertahankan tegangan konstan tanpa turun di bawah ambang batas pelepasan (*dropout threshold*) PLC.
- Pengontrol CDU **tidak boleh melakukan reboot**. *Reboot* pengontrol selama transfer bus listrik adalah kegagalan langsung dari pengujian Level 5.
- VFD pompa sekunder harus mampu bertahan melewati transfer bus secara mulus atau memulihkan frekuensi operasi penuh dalam waktu < 3,0 detik.

### 3. Gangguan Pasokan Air Dingin Primer Fasilitas (Kehilangan FWS)
Dengan *loop* sekunder yang beroperasi pada beban termal 100%, simulasikan kehilangan total pasokan air pendingin primer fasilitas dengan menutup katup isolasi pasokan primer secara cepat:
- Pengujian ini mengukur **inersia termal hidrolik** dari sirkuit sekunder.
- Saat ekstraksi panas primer turun ke nol, energi termal yang diinjeksikan oleh bank beban diserap seluruhnya oleh kapasitas panas sensibel dari massa fluida sekunder:

$$\frac{dT_{\text{supply}}}{dt} = \frac{P_{\text{load}}}{M_{\text{fluid}} \cdot c_p}$$

- **Kriteria Penerimaan**:
 - Waktu yang diperlukan bagi suhu pasokan sekunder untuk naik dari nominal 40,0°C ke ambang batas Alarm Suhu Tinggi 45,0°C harus minimal **40 detik** (t_buffer ≥ 40 s).
 - Setelah mencapai 45,0°C, CDU harus secara otomatis mengeluarkan Peringatan Suhu Tinggi (*High-Temp Warning*) dan memulai pelepasan beban bertahap.
 - Jika suhu mencapai Batas Kritis Darurat sebesar **50,0°C**, sirkuit interlock darurat harus menjatuhkan seluruh kontaktor daya bank beban seketika, menghentikan masukan panas sebelum terjadi pendidihan fluida atau kegagalan segel mekanikal.

### 4. Pemutusan Komunikasi BMS
Dengan *loop* yang berjalan di bawah beban termal penuh, lepaskan kabel jaringan Modbus-TCP dan BACnet secara fisik yang menghubungkan PLC CDU ke BMS fasilitas pusat:
- **Kriteria Penerimaan**: Pengontrol lokal CDU harus terus beroperasi secara otonom tanpa gangguan. Kecepatan pompa sekunder dan posisi katup modulasi harus tetap stabil di bawah pelacakan *setpoint* PID lokal. CDU tidak boleh berburu (*hunting*), berosilasi, atau gagal membuka akibat hilangnya koneksi pengawas eksternal.

## Urutan Keluar Terkendali (Lembar 5)

Demobilisasi dari pengujian termal multi-megawatt membutuhkan disiplin operasional yang sama tingginya dengan saat memulainya. Urutan pemadaman dan pemutusan energi harus dieksekusi dalam urutan yang ketat dan tidak dapat dibalik.

**URUTAN EKSEKUSI PENGHENTIAN WAJIB**

| LANG | PERINTAH TINDAKAN | ALASAN REKAYASA KESELAMATAN |
| :--- | :--- | :--- |
| 01 | LEPASKAN BEBAN TERMAL KE 0kW | Putus seluruh kontaktor pemanas/SCR. Jangan pernah menghentikan sirkulasi fluida saat 1,2 MW panas listrik aktif! |
| 02 | BUKA PEMUTUS ARUS BANK BEBAN | LOTO seluruh pengumpan listrik primer. Buktikan sirkuit telah mati tegangan menggunakan detektor tegangan terkalibrasi. |
| 03 | PENDINGINAN FLUIDA 10 MENIT | Pertahankan sirkulasi pompa sekunder selama 10 menit utk membuang sisa panas elemen & mencegah pendidihan lokal. |
| 04 | HENTIKAN POMPA SEKUNDER CDU | Matikan pompa hanya setelah suhu fluida turun aman di bawah 30,0°C. Konfirmasikan tekanan diferensial 0 kPa. |
| 05 | ISOLASI & LEPAS SELANG | Tutup katup isolasi manifold, buang head statis residual, dan lepaskan kopling lepas-cepat ke ember penampung cairan. |

> **PERINGATAN KRITIS PEMBALIKAN URUTAN**: Jangan pernah membalik Langkah 1 dan 4! Menghentikan sirkulasi fluida saat megawatt panas listrik masih aktif akan menyebabkan fluida yang tergenang di dalam saluran pemanas mendidih menjadi uap dalam hitungan detik. Ekspansi uap yang sangat cepat akan menciptakan lonjakan tekanan eksplosif yang akan merobek klem selang, menghancurkan diafragma sensor, dan menghadirkan bahaya lepuh panas yang mematikan bagi personel di lorong. Lembar 5 mewajibkan setiap langkah dicentang dalam urutan kronologis yang ketat; centang yang tidak berurutan membatalkan seluruh lembar kerja.

## Keamanan Data dan Pencadangan Ganda Seketika

Sebelum satu kabel atau instrumen pun dikemas ke dalam peti pengiriman, semua data pengujian harus dicadangkan dengan aman:
- Ekspor semua log CSV mentah berfrekuensi tinggi dari bank beban, penganalisis kualitas daya, dan pengukur aliran ultrasonik.
- Ekspor semua log tren 1 detik dari PLC lokal CDU dan BMS fasilitas pusat.
- Arsipkan semua tangkapan pencitraan termal beresolusi tinggi dan foto digital dari lembar master fisik.

Buat dua cadangan independen pada media penyimpanan fisik yang terpisah (misalnya, satu di stasiun kerja lokasi yang aman, dan yang kedua di drive eksternal terenkripsi). Drive penyimpanan yang dikemas ke dalam peti pengiriman bukanlah cadangan yang dapat diakses. Jika peti tersebut tertunda atau hilang dalam perjalanan, kampanye komisioning tidak dapat disertifikasi, dan seluruh pengujian multi-minggu harus diulang.

## Demobilisasi dan Pemulihan Lokasi

Demobilisasi ditutup dengan audit inventaris:
- Hitung setiap kopling lepas-cepat, selang fleksibel, adaptor, dan tutup penutup (*blanking cap*) terhadap inventaris pembongkaran peti kemas yang dicatat pada Lembar 1.
- Pasang tutup debu pelindung berperingkat tekanan pada semua port pasokan dan balik manifold.
- Periksa ubin lantai aula data, baki kabel, dan dinding dari lecet transportasi, tetesan cairan, atau serpihan sisa.
- Pulihkan semua katup fasilitas permanen, pemutus arus listrik, dan *loop* kontrol BMS ke konfigurasi operasional garis dasar aslinya.

Catatan Giliran Kerja Harian untuk hari terakhir menyatakan bahwa pengujian telah selesai, mendokumentasikan lokasi fisik arsip data, dan merangkum butir-butir daftar cacat yang masih terbuka. Catatan tersebut tidak menyatakan bahwa fasilitas telah "lulus." Sertifikasi akhir hanya terjadi setelah laporan komisioning formal diaudit dan disetujui.

## Keputusan yang Harus Dicatat Sebelum Mulai Pengujian

- Uji penghentian darurat yang disaksikan, mengonfirmasi bahwa sirkuit penghentian fisik memutus panas seketika.
- Log uji transien dinamis yang dicatat pada Lembar 4 (trip pompa, kehilangan daya 2N, pemutusan FWS, pemutusan BMS).
- Log urutan penghentian yang ditandatangani pada Lembar 5, dieksekusi dalam urutan kronologis yang ketat.
- Lokasi penyimpanan fisik dan *checksum* kriptografis dari cadangan data ganda.
- Inventaris demobilisasi yang telah selesai, mengonfirmasi tidak ada fitting yang hilang atau modifikasi sementara yang tertinggal.
