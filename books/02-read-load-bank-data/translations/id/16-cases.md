Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 16. Buku Kasus Diagnostik: Cara Menangani Pemicu Algoritmik

Algoritma deteksi titik perubahan (*changepoint*) yang dijelaskan pada bab sebelumnya menghasilkan stempel waktu. Bab terakhir ini menyajikan buku kasus diagnostik praktis mengenai apa yang harus dilakukan secara fisik oleh seorang insinyur, operator, dan auditor pihak ketiga ketika algoritma mengeluarkan suatu pemicu (*hit*).

Skenario-skenario yang disajikan di sini adalah studi kasus operasional gabungan (*composite*) yang diambil dari kampanye komisioning nyata pada instalasi pendinginan cair berdensitas tinggi kelas multi-megawatt. Jika ada kasus yang terasa sangat akrab, hal itu dikarenakan moda kegagalan ini terus berulang di seluruh industri setiap kali tim berupaya terburu-buru dalam pengujian bank beban.

## Kasus 1: Pemicu Cocok dengan Langkah Beban yang Diperintahkan

### Bukti Operasional
Focus atau FLOC memicu peringatan pada pukul `14:15:02 UTC`. Log Operator mengonfirmasi bahwa langkah beban yang diperintahkan dari 25% (30 kW) ke 50% (60 kW) diinisiasi pada pukul `14:15:00 UTC`. Daya listrik aktif melangkah secara bersih dalam waktu 1,2 detik, dan suhu cairan pendingin kembali mulai mengalami kenaikan eksponensial yang mulus (τ ≈ 45 s).

### Penentuan Diagnostik
- **Klasifikasi Manusia**: **LANGKAH TERDUGA (*EXPECTED STEP*)**.
- **Tindakan**: Pemicu didokumentasikan di dalam log audit berdampingan dengan stempel waktu perintah (Δt = +2{,}0 s, berada jauh di dalam batas penundaan kendali yang diizinkan sebesar 5 detik).
- **Jebakan yang Harus Dihindari**: Jangan menyimpulkan bahwa detektor "terlalu sensitif" lalu mencoba menaikkan ambang batas deteksi agar langkah beban berikutnya tidak bersuara! Detektor yang diam pada langkah beban yang diperintahkan adalah bukti bahwa detektor Anda tuli. Algoritma yang jujur *seharusnya* menyadari langkah beban yang diperintahkan. Catat kejadian tersebut dan lanjutkan.

## Kasus 2: Pemicu Tanpa Perintah di Dalam Penahanan Tunak

### Bukti Operasional
Bank beban telah berjalan tujuh menit di dalam rencana penahanan jeda tunak 15 menit pada beban 100% (120 kW). Daya listrik yang diperintahkan tidak berubah. Pada pukul `14:37:18 UTC`, FLOC memicu peringatan pada saluran suhu cairan kembali.

Setelah memeriksa blok data langsung, Operator mengamati:
- Daya listrik aktif tetap konstan sempurna pada 120{,}1 kW.
- Laju aliran volumetrik pada Kabinet 2 telah berhanyut turun dari 176{,}4 LPM menjadi 142{,}1 LPM.
- Suhu cairan pendingin kembali pada Kabinet 2 merayap naik dari 45{,}1°C menjadi 48{,}9°C (ΔT melebar dari 10,0 K menjadi 13,8 K).

### Penentuan Diagnostik
- **Klasifikasi Manusia**: **PATAHAN TENGAH-PENAHANAN TANPA PERINTAH (ANOMALI HIDROLIK) / *UNCOMMANDED MID-HOLD BREAK (HYDRAULIC ANOMALY)***.
- **Akar Penyebab Fisik**: Aktuator katup modulasi penyeimbang tergelincir di bawah tekanan fluida, saringan *bypass* segaris 50 μm mulai tersumbat oleh serpihan kotoran konstruksi (*construction swarf*), atau seorang operator secara tidak sengaja menyenggol katup bola manual pada manifold sekunder.
- **Tindakan**:
 1. Jika aturan keselamatan yang dinyatakan sebelumnya menetapkan bahwa hanyutan suhu di atas 48,0°C mewajibkan penghentian, matikan pemanas seketika.
 2. Jika larian selesai tanpa pemadaman darurat, **PISAHKAN MASA JEDA (*SPLIT THE DWELL*)** pada pukul `14:37:18 UTC`. Tujuh menit pertama sebelum patahan dapat berdiri sebagai bukti kondisi tunak parsial. Delapan menit terakhir **GAGAL (*FAIL*)** dalam kriteria stabilitas jeda dan tidak dapat digunakan untuk pengesahan kapasitas 100%.
 3. Dalam keadaan apa pun, seorang insinyur tidak boleh merata-ratakan seluruh jendela 15 menit menjadi satu dataran tinggi sintetis tunggal! Merata-ratakan aliran yang memburuk ke dalam aliran sehat sebelumnya menciptakan fiksi yang menutupi degradasi hidrolik.

## Kasus 3: Dua Detektor Daring Tidak Sepakat

### Bukti Operasional
Selama masa jeda 15 menit, FLOC memicu peringatan pada pukul `15:10:14 UTC`. Focus memicu peringatan delapan belas detik kemudian, pada pukul `15:10:32 UTC`. Log perintah Operator benar-benar hening tanpa aktivitas.

### Penentuan Diagnostik
- **Klasifikasi Manusia**: **PERIKSA SEBARAN MENTAH (*INSPECT RAW SCATTER*)**.
- **Tindakan**:
 1. **Larangan Keras terhadap Perataan**: Jangan pernah merata-ratakan kedua stempel waktu tersebut (`15:10:23 UTC`)! Stempel waktu rata-rata adalah artefak imajiner.
 2. Periksa sampel mentah 1 detik di seluruh jendela 60 detik yang mencakup kedua pemicu tersebut.
 3. Sering kali, FLOC (yang mengevaluasi rasio varians lokal) menyala lebih dulu karena turbulensi konvektif mulai melebar, sementara Focus (yang mengevaluasi pergeseran jumlah kumulatif) menyala kedua setelah suhu rata-rata berhanyut melampaui ambang batas kemungkinannya (*likelihood threshold*).
 4. Kedua stempel waktu dicatat dalam tabel titik perubahan sebagai batas kandidat untuk satu jendela gangguan terus-menerus: `[15:10:14 hingga 15:10:32 UTC]`. Auditor manusia mengevaluasi penyebab fisik di dalam kurung waktu tersebut.

## Kasus 4: Detektor Diam, tetapi Saluran Basi

### Bukti Operasional
Masa jeda 15 menit pada beban 100% selesai. Baik Focus maupun FLOC tidak mengeluarkan satu pun peringatan. Seorang teknisi junior melaporkan bahwa larian pengujian berlangsung "luar biasa stabil".

Saat memeriksa berkas CSV mentah, Orang Asing melihat bahwa Sensor Suhu Kembali RTD-102 melaporkan nilai tepat 45{,}000000°C selama 900 detik berturut-turut. Varians sampel terhitung di sepanjang masa jeda adalah $σ² \equiv 0{,}000000 K²$.

### Penentuan Diagnostik
- **Klasifikasi Manusia**: **KECURANGAN DATA BASI / PEMBEKUAN BUFFER (*STALE DATA / BUFFER FREEZE FRAUD*)**.
- **Realitas Fisik**: Detektor terdiam karena masukannya telah mati! Algoritma titik perubahan mengevaluasi deviasi dalam deret numerik; jika deret tersebut berupa konstanta datar, algoritma melihat nol deviasi dan tetap diam.
- **Tindakan**:
 1. Ketiadaan suara dari detektor adalah bukti kegagalan telemetri, bukan stabilitas proses.
 2. Dataran tinggi beban tersebut ditandai **GAGAL (*FAIL*)** pada gerbang mutu data.
 3. *Thread* komunikasi *edge gateway* atau *driver* ADC harus didiagnosis dan dihidupkan ulang, dan seluruh langkah beban harus dijalankan ulang dari awal.

## Kasus 5: CPOP Luring Menandai Patahan Kemiringan pada Awal Penahanan

### Bukti Operasional
Larian pengujian selesai, berkas ditutup, dan CPOP dieksekusi pada masa jeda beban 100%. CPOP mengidentifikasi perubahan kemiringan pada Menit ke-02 dari penahanan 15 menit tersebut. Daya listrik yang diperintahkan konstan di sepanjang waktu.

### Penentuan Diagnostik
- **Klasifikasi Manusia**: **KETIDAKSESUAIAN KOTAK TRANSIEN (*TRANSIENT BOX MISALIGNMENT*)**.
- **Akar Penyebab Fisik**: Operator menggambar kotak evaluasi kondisi tunak terlalu dini! Dua menit pertama dari masa jeda merupakan transien pemanasan termal fisik dari *loop* fluida dan selongsong bejana baja tahan karat yang berat (τ ≈ 45 s). Selama dua menit tersebut, suhu fluida masih melengkung naik menuju batas asimtotnya. CPOP dengan benar mengidentifikasi transisi dari transien pemanasan melengkung menuju dataran tinggi tunak horizontal.
- **Tindakan**:
 1. Jangan mengklaim bahwa "dataran tinggi tersebut gagal dalam CPOP".
 2. Sesuaikan kotak evaluasi analitis pada lembar proyek agar dimulai pada Menit ke-04 (t ≥ 4τ).
 3. Jalankan ulang CPOP pada jendela yang dipotong `[Menit ke-04 hingga Menit ke-15]`. Jika CPOP sekarang mencocokkan sisa 11 menit sebagai satu kemiringan horizontal bersih tunggal (|m| ≤ 0{,}001 K/s), dataran tinggi kondisi tunak terverifikasi secara matematis.
 4. Dokumentasikan konstanta waktu termal (τ = 45 s) di dalam laporan sebagai justifikasi rekayasa untuk batas jendela evaluasi.

## Kasus 6: CPOP Mendeteksi Patahan Kemiringan di Tengah Penahanan Saat Daya Datar

### Bukti Operasional
Pada berkas yang telah ditutup, CPOP menganalisis masa jeda 15 menit dan menempatkan patahan kemiringan yang tidak ambigu pada Menit ke-09. Daya listrik aktif berupa satu kemiringan horizontal tunggal (P_elec = 120{,}1 kW ± 0{,}1 kW). Aliran volumetrik juga datar. Namun kemiringan suhu bertransisi dari 0{,}000 K/s (horizontal) menjadi +0{,}008 K/s (merayap naik).

### Penentuan Diagnostik
- **Klasifikasi Manusia**: **HANYUTAN PENDINGINAN FASILITAS PRIMER (*PRIMARY FACILITY COOLING DRIFT*)**.
- **Akar Penyebab Fisik**: Karena daya listrik dan aliran sekunder konstan, kenaikan suhu kembali tidak mungkin disebabkan oleh bank beban. Hal itu disebabkan oleh ***loop* air dingin primer fasilitas**: pabrik *chiller* sentral fasilitas mengalami penurunan tahap kipas menara pendingin, menyebabkan cairan pendingin pasokan sekunder yang memasuki bank beban (T_in) menghangat dari 35,0°C menjadi 37,2°C.
- **Tindakan**:
 1. Verifikasi saluran suhu pasokan: jika T_in mencerminkan kemiringan T_out, kenaikan suhu internal bank beban (ΔT = T_out - T_in) tetap datar sempurna pada 10,04 K.
 2. Tulis kalimat batas yang jujur yang mengatribusikan kenaikan suhu pada hanyutan pasokan fasilitas primer (Peralatan Eksternal - Baris CDU).
 3. Kapasitas termal bank beban tetap terverifikasi; stabilitas *loop* primer fasilitas dicatat sebagai sebuah batasan.

## Kasus 7: CPOP Bersih, tetapi Tanda Termal Salah

### Bukti Operasional
CPOP mencocokkan masa jeda beban penuh 15 menit dengan satu kemiringan horizontal tunggal yang tanpa cela (K = 0, varians nol). Namun suhu pasokan terukur adalah 45{,}1°C dan suhu kembali adalah 35{,}0°C.

### Penentuan Diagnostik
- **Klasifikasi Manusia**: **SAMBUNGAN HIDROLIK TERBALIK (*REVERSED HYDRAULIC CONNECTION*)**.
- **Realitas Fisik**: Kru penguji menghubungkan selang pasokan ke port kembali bank beban dan selang kembali ke port pasokan! Fluida masuk dalam keadaan panas dari penukar panas tetangga dan keluar lebih dingin, atau label saluran perangkat lunak terbalik dalam tabel translasi Modbus.
- **Tindakan**:
 1. Algoritma tidak memahami arti fisik dari "pasokan" dan "kembali"; algoritma hanya mencocokkan angka. Kemiringan bersih dengan tanda yang salah tetap merupakan kegagalan fatal pada pemeriksaan tanda (*sign check*).
 2. Larian tersebut seketika dinyatakan **GAGAL (*FAIL*)**.
 3. Dalam keadaan apa pun, seorang insinyur tidak boleh menerapkan fungsi nilai mutlak untuk membalikkan tanda pada salindia presentasi akhir! Perbaiki jalur selang atau perbaiki label saluran di lantai uji, dan ulangi larian tersebut secara terang-terangan.

## Kasus 8: Seseorang Menuntut Angka Tunggal untuk Salindia Eksekutif

### Bukti Operasional
Seorang manajer proyek atau eksekutif mendatangi meja pengujian sebelum laporan formal disusun dan menuntut: *"Beri saya satu angka tunggal saja untuk titik perubahan pada Kabinet 3 agar saya bisa menempelkannya ke salindia presentasi pagi ini."*

Anda memiliki log Operator yang menunjukkan perintah langkah pada `14:20:00`, pemicu FLOC pada `14:20:03`, pemicu Focus pada `14:20:18`, dan transisi kemiringan CPOP pada `14:23:45`.

### Penentuan Diagnostik
- **Tanggapan Insinyur**:
 1. **Tolak Memberikan Angka Rata-Rata**: Anda tidak boleh menghitung $\frac{14:20:00 + 14:20:03 + 14:20:18 + 14:23:45}{4}$ lalu menyerahkan stempel waktu buatan `14:21:01.5`!
 2. **Sajikan Tabel yang Dapat Diaudit**: Berikan tabel terstruktur:
 - *Waktu Langkah yang Diperintahkan*: `14:20:00 UTC`
 - *Jendela Deteksi Daring*: `14:20:03 hingga 14:20:18 UTC`
 - *Cakrawala Penstabilan Termal (CPOP)*: `14:23:45 UTC` (Waktu penstabilan Δt = 225 s)
 - *Klasifikasi Manusia*: **LANGKAH BEBAN TERDUGA (LULUS)**
 3. Jika eksekutif tersebut menolak menampilkan tabel, salindia tersebut hanya berhak mendapatkan penilaian manusia dan waktu perintah. Salindia tidak boleh mendapatkan angka perantara hasil karangan.

## Ringkasan: Prosedur Standar pada Hari Pelaksanaan

Ikuti protokol kronologis yang tepat ini selama setiap kampanye pengujian:

1. **Sebelum Pemanasan**: Verifikasi jalur pencatatan CSV mentah yang tidak dapat diubah (*immutable*). Konfirmasikan bahwa ambang batas Focus, FLOC, dan CPOP telah dibekukan pada lembar kerja. Jalankan Uji Bukti Data Basi Pra-Pemanasan (cabut satu sensor dan buktikan bahwa *pipeline* mencatat adanya celah data).
2. **Selama Jendela Aktif**: Pantau aliran telemetri langsung. Untuk setiap pemicu kandidat daring, segera catat stempel waktunya di samping log perintah Operator. Terapkan aturan yang telah ditulis sebelumnya: tandai atau hentikan. Jangan pernah memperpanjang masa jeda hanya untuk "melihat apakah pemicu tersebut menghilang".
3. **Setelah Penutupan Berkas**: Buat *hash* kriptografis berkas CSV mentah (SHA-256). Jalankan CPOP luring pada kotak-kotak masa jeda tunak (dengan mengecualikan jendela pemanasan awal 4τ).
4. **Susun Tabel Audit**: Sejajarkan semua pemicu kandidat terhadap peristiwa log perintah. Bubuhkan paraf pada klasifikasi manusia untuk setiap baris (*Langkah Terduga*, *Inspeksi / Pisahkan Penahanan*, *Tidak Berdampak*).
5. **Tegakkan Lima Kelulusan**: Pindahkan temuan yang telah diverifikasi ke halaman pertama laporan kilat. Tandatangani Kalimat Penerimaan atau ajukan Kalimat Penolakan yang eksplisit.
