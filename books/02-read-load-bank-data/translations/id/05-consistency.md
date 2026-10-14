Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 5. Konsistensi dan Keseragaman Multikabinet

Satu sensor tunggal dapat melaporkan angka yang tampak masuk akal dan menarik, namun sebenarnya terputus sama sekali dari realitas fisik. Di aula data berdensitas tinggi tempat beberapa bank beban paralel menyimulasikan seluruh barisan kluster AI, mengevaluasi setiap unit secara terisolasi adalah tindakan yang tidak memadai.

Laporan kilat (*flash report*) mewajibkan pengujian matematis yang ketat terhadap konsistensi multikabinet: apakah instrumen dan mesin yang diklaim sebagai kembar identik pada manifold sekunder yang sama benar-benar berperilaku layaknya kembar identik di bawah beban penuh?

Dalam panduan lapangan ini, konsistensi bukanlah kesan informal atau penilaian visual atas grafik-grafik paralel. Konsistensi didefinisikan oleh metrik matematis yang ketat: **Koefisien Variasi (*Coefficient of Variation* - CV)**.

$$\text{CV} = \left( \frac{\sigma}{\mu} \right) \times 100\% = \left[ \frac{\sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2}}{\mu} \right] \times 100\%$$

di mana N adalah jumlah kabinet bank beban paralel di dalam kluster, μ adalah rata-rata aritmatika kelompok, dan σ adalah deviasi standar sampel.

(Lihat Gambar 03 untuk skema distribusi hidrolik multikabinet, gradien tekanan manifold, dan studi kasus komparatif antara kluster yang seimbang vs. yang mengalami kelaparan aliran).

## Di Mana Metrik CV Diterapkan

Laporan kilat menghitung CV di empat dimensi fisik selama masa jeda kondisi tunak (*steady-state dwell*) pada setiap langkah beban:

### 1. Keseragaman daya aktif listrik (CV ≤ 1{,}0%)
Di seluruh kabinet bank beban paralel, penarikan daya listrik aktif harus seimbang dalam batas koridor 1,0%. Resistor yang difabrikasi dari paduan Nikel-Kromium (NiCr 80/20) bermutu tinggi memiliki toleransi resistansi yang ketat (± 2{,}0% saat dingin, menyempit menjadi ± 1{,}0% pada konfigurasi delta 3-fasa yang seimbang).
- Jika empat kabinet paralel diperintahkan ke 120 kW, dan tiga kabinet menarik 120,2 kW sedangkan Kabinet 4 hanya menarik 108,5 kW, nilai CV listrik melonjak menjadi 4{,}8%.
- CV listrik yang melebihi 1,0% mengindikasikan sepatu kabel (*terminal lug*) yang longgar, sekring cabang yang putus, SSR yang terbakar, atau transduser arus (CT) yang tidak terkalibrasi. Kondisi ini seketika menggagalkan baris konsistensi listrik.

### 2. Keseragaman laju aliran volumetrik cairan pendingin (CV ≤ 5{,}0%)
Dalam jaringan distribusi pendinginan sekunder yang seimbang dengan benar, setiap rak IT paralel harus menerima bagian aliran cairan yang identik dari aliran total.
- Untuk empat unit 120 kW yang beroperasi pada manifold bersama dengan pasokan total sebesar 706 LPM, aliran cabang yang ideal adalah 176{,}5 LPM per unit.
- Laju aliran cairan di seluruh kabinet aktif harus memenuhi **CV ≤ 5{,}0%**.
- CV aliran yang melebihi 5,0% mengungkap terjadinya maldistribusi hidrolik—biasanya disebabkan oleh panjang selang cabang yang tidak sama, tekukan tajam 90°, katup searah (*check valve*) internal kopling sambung-cepat yang dudukannya tidak tepat, atau katup penyeimbang cabang yang belum disetel.

### 3. Keseragaman kenaikan suhu cairan pendingin kembali (CV ≤ 3{,}0%)
Jika daya listrik seragam (CV ≤ 1{,}0%) dan aliran cairan seragam (CV ≤ 5{,}0%), hukum termodinamika menetapkan bahwa kenaikan suhu cairan pendingin kembali (ΔT = T_out - T_in) juga harus seragam.
- Di seluruh kabinet, kenaikan suhu harus memenuhi **CV ≤ 3{,}0%**.
- Jika Kabinet 1 sampai 3 menunjukkan ΔT = 10{,}0 K sementara Kabinet 4 menunjukkan ΔT = 14{,}5 K, Kabinet 4 mengalami konsentrasi panas lokal (sering kali dipicu oleh aliran rendah). Sebaliknya, jika Kabinet 4 menunjukkan ΔT = 2{,}1 K, unit tersebut mengalami hubungan pendek fluida (*fluid short-circuiting*) di sekitar inti pemanasnya.

### 4. Keseragaman tekanan diferensial manifold (CV ≤ 5{,}0%)
Tekanan diferensial yang diukur di seluruh port pasokan dan kembali dari setiap kabinet individual harus memenuhi **CV ≤ 5{,}0%**. Hal ini memverifikasi bahwa semua sasis memberikan impedansi hidrolik yang identik terhadap pompa CDU fasilitas.

## Bahaya Hidrolik: Manifold Direct-Return vs. Reverse-Return

Bab konsistensi mengungkap cacat pemipaan yang paling umum ditemui dalam instalasi bank beban cair sementara: **kelaparan aliran akibat manifold *direct-return***.

Sebagaimana diilustrasikan dalam Gambar 03:
- Pada manifold **Kembali Langsung (*Direct-Return* / Pertama-Masuk, Pertama-Keluar)**, bank beban pertama (Rak 1) berada paling dekat dengan pasokan primer sekaligus pengumpul kembali primer. Rak 1 mengalami sirkuit hidrolik terpendek dan tekanan diferensial (ΔP) tertinggi yang tersedia. Unit terjauh (Rak 4) berada di ujung buntu hidrolik, di mana tekanan pasokan telah merosot akibat gesekan pipa dan tekanan balik (*back-pressure*) saluran kembali telah menumpuk.
- Tanpa katup penyeimbang pada masing-masing cabang, Rak 4 menerima aliran yang terdegradasi secara signifikan (misalnya, 124{,}0 LPM vs 192{,}0 LPM pada Rak 1). Hal ini menghasilkan CV aliran bencana sebesar **18{,}25%**!
- Dalam upaya menutupi kegagalan ini, tim yang belum berpengalaman akan menghitung "aliran rata-rata kluster" (168{,}25 LPM) dan menyatakan pengujian telah lulus. Sementara itu, di Rak 4, kecepatan fluida telah anjlok, suhu selongsong pemanas melonjak mendekati batas *trip* 85°C, dan pompa CDU beroperasi di wilayah yang tidak stabil.
- Pada *loop* pemipaan **Kembali Terbalik (*Reverse-Return* / Tichelmann)**, unit pertama yang dialiri adalah unit terakhir yang dikembalikan cairannya, memastikan bahwa total panjang pipa ekuivalen adalah identik di keempat cabang. CV aliran yang dihasilkan dengan mudah turun menjadi **0{,}33%**, menjamin fidelitas hidrolik yang sebenarnya.

Laporan kilat mewajibkan CV aliran untuk dihitung dan dicetak di halaman pertama. CV yang tinggi akan langsung mengekspos kelaparan aliran akibat *direct-return* sebelum perangkat keras komputasi nyata diterapkan.

## Aturan Jendela Evaluasi

Analisis konsistensi harus dilakukan pada **jendela evaluasi lima menit** terus-menerus yang diambil selama bagian akhir yang tunak dari masa jeda beban 15 menit.
- Jendela tersebut harus disampel pada **1 Hz** (satu pembacaan langsung per detik per saluran).
- Jendela tersebut harus secara ketat dibatasi pada kondisi tunak. Jendela tidak boleh melintasi transisi langkah beban atau penyetelan katup oleh operator. Memasukkan langkah daya ke dalam jendela evaluasi akan menggelembungkan varians secara artifisial, menyebabkan sekelompok kabinet yang sebenarnya baik menjadi gagal dalam perhitungan.
- Jika langkah beban hanya ditahan selama 3 menit, Anda tidak memiliki data kondisi tunak yang cukup untuk menghitung CV. Dalam kasus tersebut, Anda harus menandai baris konsistensi **TIDAK DIJALANKAN** (*NOT RUN*) atau mengulangi langkah tersebut dengan masa jeda yang tepat. Anda tidak boleh menarik jendela evaluasi ke belakang hingga memasuki fase pemanasan transien hanya demi mengumpulkan cukup titik data.

## Hal yang Tidak Dapat Diungkapkan CV: Kecurangan Varians Nol

CV yang rendah membuktikan bahwa kluster tersebut konsisten dengan dirinya sendiri. Hal itu tidak membuktikan bahwa kluster tersebut benar.

Pertimbangkan dua moda kegagalan berbahaya yang menghasilkan nilai CV rendah yang menipu:
1. **Seragam di Luar Spesifikasi**: Keempat kabinet menerima aliran identik sebesar 130{,}0 LPM terhadap batas bawah yang disyaratkan sebesar 170{,}0 LPM. Deviasi standarnya adalah nol, dan CV aliran yang dihitung bernilai sempurna 0{,}00%. Namun, seluruh kluster tersebut sebenarnya mengalami kelaparan aliran secara seragam! Kondisi ini meluluskan baris konsistensi, tetapi menggagalkan baris Prates tanpa syarat. Kegagalan yang seragam tetaplah sebuah kegagalan.
2. **Kecurangan Data Basi / Beku**: Jika *thread* komunikasi *edge gateway* mengalami *crash*, atau jika *poller* Modbus berulang kali mencatat nilai dalam *cache* tanpa membaca register langsung, nilai yang tercatat di keempat kabinet akan tetap beku secara matematis. Kelompok yang mati akan melaporkan deviasi standar σ = 0{,}000 dan CV terhitung sebesar **0{,}00%**!

CV yang tepat bernilai 0{,}00% bukanlah tanda kesempurnaan rekayasa; dalam *loop* fluida turbulen, hal itu adalah bukti fisik dari kecurangan telemetri. Konveksi turbulen nyata selalu menghasilkan fluktuasi (*jitter*) termal dan tekanan mikroskopis secara langsung.

Oleh karena itu, sebelum nilai CV yang dihitung dapat diterima dalam laporan kilat:
- Sistem supervisi harus memverifikasi bahwa **varians sampel σ² > 0** di semua saluran.
- *Bitmask* Kualitas 16-bit harus mengonfirmasi bahwa tidak ada saluran yang bit "BASI / BEKU (*STALE / FROZEN*)"-nya aktif.

Jika varians bernilai nol atau bit kualitas bermasalah, nilai CV yang dihitung hanyalah ilusi semata. Nyatakan baris tersebut gagal.

## Keputusan yang Harus Dicatat

Di bagian konsistensi pada laporan kilat, catat fakta-fakta berikut:

- Batas ambang CV yang dinyatakan sebelumnya untuk daya listrik (≤ 1{,}0%), aliran cairan (≤ 5{,}0%), kenaikan suhu (≤ 3{,}0%), dan tekanan diferensial (≤ 5{,}0%).
- Jendela waktu 5 menit yang tepat (stempel waktu mulai dan selesai hingga hitungan detik) yang digunakan untuk perhitungan kondisi tunak.
- Rata-rata aritmatika (μ), deviasi standar sampel (σ), dan CV terhitung untuk setiap parameter di seluruh kabinet paralel.
- Pemeriksaan varians bukan-nol tersertifikasi (σ² > 0) yang mengonfirmasi bahwa *jitter* turbulen langsung hadir pada setiap saluran.
- Penilaian lulus/gagal bertanda tangan untuk konsistensi multikabinet, yang diparaf oleh Orang Asing.
