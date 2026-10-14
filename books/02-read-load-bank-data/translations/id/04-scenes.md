Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 4. Fungsi-Fungsi Skenario

Setelah gerbang prates meraih predikat LULUS (*PASS*), laporan kilat mengeksekusi skenario-skenario operasional aktif. Sebuah skenario bukanlah peninjauan santai di lapangan, demonstrasi peralatan tanpa batas waktu, atau pemutaran kenop kendali secara acak hingga penonton merasa puas.

Sebuah skenario adalah pengujian kinerja fungsional formal yang berbatas waktu dengan waktu mulai yang eksplisit, penahanan jeda (*dwell hold*) wajib, gangguan fisik yang terdefinisi, dan kriteria lulus/gagal kuantitatif. Masing-masing skenario menguji kemampuan operasional yang berbeda dari bank beban cair dan pabrik pendingin CDU fasilitas terkait.

Verifikasi bank beban cair standar terdiri dari lima skenario inti:
1. **Gradien Bertahap** (Kapasitas kondisi tunak dan linearitas termal);
2. **Kunjungan Beban Lebih** (Margin desain dan ketahanan darurat);
3. **Perubahan Langkah Mendadak** (Respons kendali dinamis dan stabilitas hidrolik);
4. **Uji Penurunan Kehilangan Pasokan Tunggal 2N** (Redundansi listrik dan imunitas telemetri);
5. **Otoritas Katup Modulasi & Verifikasi Langkah (*Stroke*)** (Kendali penyeimbang hidrolik).

(Lihat Gambar 07 untuk osilogram elektromekanis dan kendali terperinci dari Uji Penurunan Kehilangan Pasokan Tunggal 2N).

## Skenario 1: Gradien (Larian Kapasitas Bertahap)

Skenario gradien memverifikasi bahwa bank beban dapat bertahan secara stabil pada dataran tinggi (*plateau*) beban yang berbeda di seluruh koridor operasinya tanpa fluktuasi liar (*hunting*), degradasi elemen, atau *bypass* fluida yang berlebihan.

Pengujian standar mengikuti empat fraksi beban yang berbeda:
- **Langkah 1 (25% Beban Nominal)**: Beban listrik aktif 30{,}0 kW (24{,}6 kW cairan, 4{,}8 kW udara pendamping).
- **Langkah 2 (50% Beban Nominal)**: Beban listrik aktif 60{,}0 kW (49{,}3 kW cairan, 9{,}6 kW udara pendamping).
- **Langkah 3 (75% Beban Nominal)**: Beban listrik aktif 90{,}0 kW (74{,}0 kW cairan, 14{,}4 kW udara pendamping).
- **Langkah 4 (100% Beban Nominal Penuh)**: Beban listrik aktif 120{,}0 kW (98{,}6 kW cairan, 19{,}2 kW udara pendamping).

### Aturan Jam Jeda (*Dwell Clock*)
Pada setiap dataran tinggi, perintah beban harus ditahan konstan selama jeda terus-menerus **setidaknya 15 menit** (atau interval penahanan spesifik yang dinyatakan dalam kontrak pengujian).

Hitungan waktu 15 menit ini tidak dapat ditawar karena *loop* cairan fisik memiliki massa. Sebuah bank beban imersi industri yang memuat 150 kg logam bejana baja tahan karat 316, 20 liter fluida, rel tembaga (*busbar*) internal yang berat, dan *header* terinsulasi tebal memiliki konstanta waktu termal sebesar τ ≈ 45 detik.
- 3 hingga 5 menit pertama dari setiap langkah beban merupakan **jendela transien termal**, di mana panas diserap secara aktif oleh dinding logam yang dingin sebelum kenaikan suhu fluida stabil.
- Perhitungan keseimbangan panas yang dicoba selama jendela transien ini akan secara keliru melaporkan bahwa pemanas mengalami defisiensi daya.
- Jendela evaluasi kondisi tunak (*steady-state*) baru dimulai setelah empat konstanta waktu (t ≥ 4τ ≈ 3 menit) berlalu. 10 menit terakhir dari masa jeda 15 menit mewakili dataran tinggi kondisi tunak yang sebenarnya.

Untuk meluluskan skenario gradien, keempat langkah harus berhasil ditahan, dan kenaikan suhu fluida yang teramati (ΔT = T_out - T_in) harus meningkat secara linear terhadap daya listrik yang diperintahkan dalam rentang ± 2{,}0% dari nilai teoretis.

## Skenario 2: Beban Lebih (Kunjungan Berbatas)

Skenario beban lebih memverifikasi bahwa elemen pemanas, relai keadaan padat (*solid-state relays* - SSR) internal, kontaktor, rakitan kabel, dan gasket pipa memiliki margin keselamatan yang memadai di atas kapasitas nominal 100%.

Untuk unit garis dasar 120 kW, langkah beban lebih memerintahkan daya sebesar **110% dari daya nominal (132{,}0 kW)**.
- **Aturan Kunjungan**: Skenario beban lebih secara ketat didefinisikan sebagai **kunjungan** yang disengaja, biasanya berlangsung tepat selama **5 menit**. Ini bukan peringkat operasi permanen.
- **Mengapa Harus Berhenti di Lima Menit**: Elemen pemanas imersi yang beroperasi pada beban 110% mengalami densitas watt selongsong yang mendekati 15 W/cm². Meskipun aman untuk pemeriksaan komisioning singkat di bawah aliran cairan berkecepatan tinggi, operasi berkepanjangan pada fluks tinggi ini akan mendegradasi inhibitor korosi fluida (seperti toliltriazol) dan mempercepat pengerasan termal gasket EPDM.
- **Kriteria Lulus/Gagal**: Skenario beban lebih lulus jika unit memasuki daya 132 kW secara bersih, mempertahankan penahanan 5 menit tanpa memicu sakelar sentak panas lebih (*overtemperature snap-switches*), tidak menunjukkan getaran kontaktor atau asap pada blok terminal, dan melepaskan beban kembali ke beban nominal atau nol sesuai perintah secara bersih.
- **Kecurangan Promosi Peringkat**: Jika kru uji melihat bahwa unit beroperasi dengan lancar pada 132 kW lalu mencoba memasarkan atau melabeli ulang mesin tersebut sebagai "bank beban kontinu 132 kW", tolak klaim tersebut seketika. Kunjungan yang berhasil bertahan bukanlah peringkat daya kontinu.

## Skenario 3: Perubahan Langkah (Kendali Dinamis & Imunitas Lonjakan)

Skenario perubahan langkah menguji kelincahan dinamis sistem selama ayunan daya yang drastis—menyimulasikan peluncuran *batch* inferensi AI yang tersinkronisasi atau pembatasan (*throttle*) kluster GPU darurat.

Skenario ini mengeksekusi lompatan langkah seketika:
1. Bank beban ditahan stabil pada beban 25% (30 kW).
2. Skrip supervisi otomatis atau operator manual memerintahkan langkah seketika ke beban 100% (120 kW).
3. Unit ditahan pada beban 100% selama 10 menit.
4. Pelepasan beban seketika dari 100% kembali ke 25% diperintahkan.

### Hal yang Dievaluasi
- **Pelacakan Listrik**: Kontaktor atau pengontrol daya tiristor harus beralih dan menstabilkan langkah daya dalam waktu kurang dari 1{,}5 detik.
- **Waktu Penstabilan Loop Kendali**: Katup pendingin modulasi (TCV) CDU fasilitas harus menyesuaikan aliran cairan pendingin atau suhu pasokan sekunder untuk menstabilkan fluks panas baru dalam waktu 120 detik, dengan lonjakan melampaui batas (*overshoot*) kurang dari 5{,}0%.
- **Peredaman Palu Air Hidrolik**: Ketika tahap pemanas besar dilepaskan atau katup modulasi mencekik aliran, pergeseran aliran yang cepat dapat memicu pulsa tekanan akustik. Sensor tekanan diferensial manifold harus memverifikasi bahwa lonjakan tekanan puncak tidak melampaui ΔP_surge ≤ 15{,}0 kPa. Jika pergerakan katup yang cepat menyebabkan guncangan pipa yang keras, benturan pada penopang pipa, atau lonjakan tekanan yang melampaui 50 kPa, skenario perubahan langkah seketika dinyatakan GAGAL (*FAIL*).

## Skenario 4: Pasokan Tunggal (Uji Penurunan Kehilangan Pasokan 2N)

Di aula data AI berdensitas tinggi, distribusi daya ke tingkat rak dikonfigurasikan sebagai 2N (jalur ganda penyulang A dan B) atau redundan terdistribusi. Bank beban cair yang menggantikan rak NVL72 harus mereplikasi topologi listrik jalur ganda ini.

### Pelaksanaan Pengujian
Dengan kluster bank beban beroperasi pada kapasitas nominal 100% (120{,}0 kW per kabinet, dengan 60{,}0 kW ditarik dari Penyulang A dan 60{,}0 kW ditarik dari Penyulang B):
1. Operator secara manual memutus pemutus arus penyulang utama yang menyuplai Penyulang A.
2. Logika kendali kontaktor untuk Bank 1 dan Bank 2 (yang ditenagai oleh Penyulang A) harus segera mati.
3. Kontak bantu harus terbuka dalam waktu **< 20 milidetik**, melepaskan tepat 50% dari beban aktif (60{,}0 kW) secara bersih.
4. Penyulang B harus memikul Bank 3 dan Bank 4 secara mulus tanpa memicu pemutus arus di hulunya sendiri atau mengalami transien arus masuk yang melebihi 115% dari arus nominal.
5. **Persyaratan Penurunan Tegangan Nol pada Bus Kendali**: Bus catu daya supervisi 24 VDC (yang memberi daya pada PLC, sensor, dan gerbang komunikasi Modbus/MQTT) harus digabungkan secara *diode-OR* di kedua penyulang (lihat Gambar 07). Pemutusan Penyulang A harus menghasilkan **penurunan tegangan nol (*zero brownout dip*)** (riak tegangan < 50 mV). Jika kehilangan Penyulang A menyebabkan PLC me-*reboot*, memutuskan sambungan jaringan, atau membekukan pembacaan sensor, bank beban tersebut gagal dalam uji pasokan tunggal tanpa syarat.
6. Setelah penurunan Penyulang A divalidasi, Penyulang A dipulihkan kembali, unit kembali ke kondisi tunak 100%, dan pengujian serupa diulangi dengan memutus Penyulang B. Kedua penyulang harus diuji sebagai jalur yang mengalami kegagalan.

## Skenario 5: Otoritas Katup Modulasi & Verifikasi Langkah (*Stroke*)

Jika bank beban dilengkapi dengan katup penyeimbang modulasi (TCV) terintegrasi yang digunakan untuk mengatur tekanan diferensial sisi rak atau impedansi aliran, otoritas mekanis katup tersebut harus diverifikasi.

Pengujian ini membandingkan jendela tunak 5 menit sebelum pergerakan katup terhadap jendela tunak 5 menit setelah perubahan posisi katup:
- **Verifikasi Langkah (*Stroke*)**: Aktuator katup harus bergerak dari 100% terbuka menjadi 50% tercekik saat diperintahkan tanpa hambatan mekanis, *hunting*, atau motor macet (*stalling*).
- **Otoritas Hidrolik**: Mencekik katup hingga langkah 50% harus menghasilkan pergeseran yang terukur dan dapat diulang pada tekanan diferensial cabang (ΔP) tanpa tersedak ke dalam rezim derau kavitasi yang parah.
- Laporan yang hanya mencatat "katup bergerak" tidak dapat diaudit. Laporan harus menyatakan persentase langkah yang diperintahkan, perubahan aliran yang terukur (Δ Q_v), dan pergeseran tekanan diferensial manifold yang dihasilkan.

## Keputusan yang Harus Dicatat

Untuk setiap skenario aktif yang dilaksanakan selama kampanye pengujian, catat hal-hal berikut dalam laporan kilat:

- Waktu mulai kronologis yang tepat, waktu stabilisasi, dan waktu selesai untuk setiap dataran tinggi gradien.
- Durasi yang dinyatakan sebelumnya dan tingkat daya dari kunjungan beban lebih.
- Waktu penstabilan terukur dan lonjakan tekanan hidrolik puncak (ΔP_surge) selama lonjakan perubahan langkah.
- Waktu pemutusan kontaktor (< 20 ms) dan kontinuitas tanpa penurunan tegangan (*zero-dip*) yang terkonfirmasi dari bus kendali 24 VDC selama uji pemutusan Penyulang A dan Penyulang B.
- Pengukuran aliran dan tekanan sebelum/sesudah untuk pengujian langkah katup penyeimbang modulasi.
- Tanda tangan Pencatat dan Operator yang mengonfirmasi bahwa semua transisi skenario dilaksanakan sesuai ketat dengan jadwal pengujian.
