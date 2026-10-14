Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 1. Lima Kelulusan

Laporan kilat (*flash report*) yang ketat tidak dibuka dengan narasi, ringkasan eksekutif yang penuh prosa optimis, atau foto pilihan berisi LED status berwarna hijau. Laporan ini dibuka dengan lima baris eksplisit yang disusun dalam tabel yang tidak dapat diubah di bagian paling atas halaman pertama:

1. **Prates (*Pretest*)**: Apakah mesin dan *loop* hidronik yang terhubung layak untuk diuji sebelum panas apa pun ditambahkan?
2. **Gradien (*Gradient*)**: Apakah sistem menunjukkan dataran tinggi (*plateau*) yang stabil dan dapat dikenali di seluruh langkah beban yang diperintahkan?
3. **Beban Lebih (*Overload*)**: Apakah kunjungan di atas kapasitas terukur nominal dimasuki secara aman, diverifikasi, dan diakhiri dengan bersih?
4. **Perubahan Langkah (*Step Change*)**: Apakah peningkatan dan penurunan beban mendadak terjadi sebagai langkah sejati tanpa memicu osilasi kendali atau palu air (*water hammer*)?
5. **Gangguan Pasokan Tunggal (*Single-Feed Fault*)**: Apakah satu penyulang (*feeder*) listrik independen terputus (*trip*) secara bersih tanpa mendestabilkan pasokan sekunder atau mematikan daya kendali?

Masing-masing dari kelima baris ini harus dicatat sebagai **LULUS** (*PASS*), **GAGAL** (*FAIL*), atau **TIDAK DIJALANKAN** (*NOT RUN*). (Lihat Gambar 01 untuk tata letak laporan kilat satu halaman yang definitif dan tabel audit lima kelulusan).

Penilaian pengujian keseluruhan adalah **LULUS** jika, dan hanya jika, setiap baris yang Anda coba ditandai **LULUS**. Jika ada baris yang dicoba ditandai **GAGAL**, pengujian keseluruhan dinyatakan **GAGAL**. Jika suatu baris dihilangkan dari jadwal hari itu, baris tersebut dicatat sebagai **TIDAK DIJALANKAN**, dan klaim keseluruhan menyusut secara ketat hanya pada cakupan baris-baris yang benar-benar Anda laksanakan. Dalam keadaan apa pun, baris yang tidak dicoba tidak boleh dihilangkan secara diam-diam demi menampilkan kesan verifikasi penuh yang palsu.

## Mengapa Lima Baris

Satu kurva deret waktu tunggal dapat terlihat tenang secara menipu sembari menyembunyikan cacat operasional yang membawa bencana. Jika seorang insinyur yang belum berpengalaman hanya melihat bentangan datar 30 menit dari suhu cairan kembali, mereka mungkin menyimpulkan bahwa "pengujian telah lulus." Namun dalam satu jam yang sama:

- Aliran hidrolik awal mungkin berada di bawah batas bawah kavitasi (*cavitation floor*) dari pabrikan sebelum panas dinyalakan (menggagalkan baris **Prates**);
- Langkah beban perantara antara nol dan kapasitas penuh mungkin menunjukkan lonjakan termal (*thermal overshoot*) atau fluktuasi liar (*hunting*) yang parah (menggagalkan baris **Gradien**);
- Bank beban mungkin mengalami *trip* akibat pelarian termal (*thermal runaway*) dalam waktu 30 detik setelah menyentuh beban lebih 110% (menggagalkan baris **Beban Lebih**);
- Pelepasan langkah beban darurat mungkin menyebabkan solenoid tanpa *ramp* menutup dengan keras, memicu lonjakan palu air akustik yang membebani selongsong (*ferrules*) manifold (menggagalkan baris **Perubahan Langkah**);
- Atau terputusnya Penyulang A mungkin menyebabkan catu daya internal 24 VDC mengalami *brownout*, yang me-*reboot* pengendali supervisi dan menghilangkan telemetri selama tiga menit (menggagalkan baris **Gangguan Pasokan Tunggal**).

Struktur lima baris ini menghilangkan ambiguitas tersebut. Struktur ini memisahkan berbagai kompetensi rekayasa yang berlainan—hidrolika, kapasitas termal kondisi tunak, ketahanan beban lebih, respons kendali dinamis, dan redundansi listrik—menjadi gerbang-gerbang verifikasi terpisah yang tidak dapat ditawar.

Anda boleh mempersempit cakupan pengujian sebelum hari pelaksanaan dimulai: jika kendala utilitas lokasi mencegah pelaksanaan kunjungan beban lebih, tuliskan pengurangan tersebut di halaman pertama rencana pengujian dengan tinta, dan ditandatangani oleh Pemilik Lembar. Namun pengurangan yang baru diakui saat memeriksa grafik setelah larian selesai bukanlah optimasi editorial yang cerdik. Itu adalah baris yang gagal yang sedang berusaha disembunyikan seseorang.

## Definisi Teknis Masing-Masing Baris

### 1. Prates (*Pretest*)
Baris prates mengaudit kondisi hidrolik dan listrik dingin garis dasar (*baseline*) dari sistem selama jendela stabilisasi beban nol wajib selama 10 menit. Baris ini mengevaluasi tiga sel spesifik terhadap spesifikasi rekayasa yang disitasi:
- **Laju aliran volumetrik per kabinet**: Harus melampaui batas bawah pendinginan minimum (misalnya, Q_v ≥ 170{,}0 LPM untuk unit virtual 120 kW kelas NVL72) guna memastikan elemen pemanas tetap terendam sepenuhnya dalam rezim konvektif berkecepatan tinggi.
- **Suhu pasokan pendingin**: Harus berada di dalam batas koridor komisioning fasilitas yang dinyatakan (misalnya, 35{,}0°C ± 1{,}5 K) dan mempertahankan margin keselamatan setidaknya 2{,}0 K di atas titik embun aula data (T_in ≥ T_dp + 2{,}0 K).
- **Tekanan diferensial manifold**: Harus tetap berada di bawah impedansi hidrolik rak maksimum yang diizinkan (misalnya, ΔP = P_in - P_out ≤ 115{,}0 kPa).

Jika salah satu dari ketiga parameter prates ini berada di luar batas, mesin tidak layak untuk diuji. Menyalakan panas dengan aliran yang tidak memadai atau suhu pasokan yang di luar spesifikasi akan merusak seluruh fisika perpindahan panas di hilir.

### 2. Gradien (*Gradient*)
Baris gradien mengevaluasi apakah bank beban dapat bertahan pada dataran tinggi (*plateau*) termal yang berbeda dan dapat dikenali di seluruh rentang operasinya. Gradien standar melangkah melalui perempat beban terukur nominal: 25% (30 kW), 50% (60 kW), 75% (90 kW), dan 100% (120 kW).

Untuk meluluskan baris gradien, setiap dataran tinggi harus memenuhi tiga kriteria:
- **Durasi jeda yang memadai**: Penahanan harus berlangsung setidaknya 15 menit terus-menerus pada setiap dataran tinggi, memungkinkan massa termal *loop* fluida dan logam bejana yang terbasahi fluida (τ ≈ 45 s) untuk stabil sepenuhnya.
- **Penutupan kalor termodinamika**: Kalor yang diserap oleh aliran cairan (Q_liquid = ṁ C_p ΔT) harus cocok dengan daya listrik aktif yang diperintahkan dalam rentang ± 3{,}0% setelah dikurangi beban udara pendamping dan kehilangan kalor permukaan (*skin losses*) yang terverifikasi.
- **Stabilitas dan ketiadaan hanyutan**: Kenaikan suhu pendingin (ΔT) tidak boleh menunjukkan hanyutan ke atas yang monoton (*monotonic upward drift*) selama 5 menit terakhir masa jeda.

### 3. Beban Lebih (*Overload*)
Baris beban lebih memverifikasi margin desain termal dan listrik sistem dengan menguji ekskursi sementara di atas nilai nominal 100%—biasanya 110% (132 kW untuk garis dasar 120 kW) yang ditahan selama durasi ketat yang dinyatakan sebelumnya yaitu 5 menit.

Baris beban lebih secara eksplisit didefinisikan sebagai **kunjungan**, bukan sebagai peringkat operasi permanen. Baris ini lulus jika unit memasuki tingkat beban lebih dengan mulus, mempertahankan penahanan tanpa memicu sakelar panas lebih (*thermal overtemperature switches*), tidak mengalami getaran kontaktor (*contactor chattering*) atau panas lebih pada kabel, dan keluar dengan bersih kembali ke beban terukur atau nol. Baris ini gagal jika ada sakelar proteksi yang terangkat, jika cairan mendidih pada batas selongsong pemanas, atau jika kru uji memperpanjang kunjungan di luar batas jendela yang telah dinyatakan sebelumnya hanya untuk menyombongkan kinerja.

### 4. Perubahan Langkah (*Step Change*)
Baris perubahan langkah memeriksa respons dinamis transien dari bank beban cair dan *loop* kendali CDU fasilitas terkait selama transisi daya mendadak beramplitudo besar. Verifikasi standar mencakup lompatan seketika dari beban rendah (25%) ke beban penuh (100%), diikuti oleh pelepasan beban seketika kembali ke beban rendah.

Perubahan langkah lulus jika:
- Daya listrik yang diperintahkan bertransisi secara bersih dalam waktu kurang dari 1,5 detik tanpa memicu pemutus arus (*breaker*) di hulu;
- Katup kendali pendinginan modulasi (TCV) melacak lonjakan secara mulus tanpa *hunting*, pantulan katup (*valve bounce*), atau osilasi siklus batas (*limit-cycle oscillation*) yang berkelanjutan;
- Aktuasi katup yang cepat tidak menghasilkan palu air hidrolik yang merusak (lonjakan tekanan statis manifold harus memenuhi ΔP_surge ≤ 15{,}0 kPa).

### 5. Gangguan Pasokan Tunggal (*Single-Feed Fault*)
Baris gangguan pasokan tunggal mengaudit arsitektur distribusi listrik 2N. Di pusat data *mission-critical* modern, rak IT diberi daya melalui dua penyulang independen (Penyulang A dan Penyulang B). Bank beban cair yang bertindak sebagai pengganti rak NVL72 harus mereplikasi arsitektur daya dua jalur ini.

Selama pengujian pasokan tunggal, dengan unit beroperasi pada kapasitas nominal 100%, seorang operator memutus secara manual pemutus arus untuk Penyulang A. Untuk lulus:
- Logika bantu kontaktor harus seketika (< 20 ms) melepaskan elemen pemanas Bank 1 & 2;
- Penyulang B harus memikul Bank 3 & 4 (50% beban nominal) secara mulus tanpa mengalami transien arus masuk (*inrush transients*) yang memicu pemutus arus di hulu;
- Yang terpenting, bus kendali supervisi 24 VDC, PLC, sensor imersi, dan mesin telemetri Modbus/MQTT harus mengalami **penurunan tegangan nol (*zero brownout dip*)**. Jika kehilangan Penyulang A menyebabkan PLC me-*reboot*, komunikasi terputus, atau ekspor data membeku, unit tersebut langsung gagal pada baris gangguan pasokan tunggal.

## "Tidak Dijalankan" Bukanlah Gagal, dan Bukan Pula Lulus

Terdapat perbedaan mendasar antara pengujian yang gagal dan pengujian yang tidak dilaksanakan:
- **TIDAK DIJALANKAN (*NOT RUN*)** berarti jadwal pengujian, keterbatasan lokasi, atau cakupan kontraktual secara sengaja mengecualikan skenario tersebut. Laporan menandai baris tersebut "TIDAK DIJALANKAN" dan secara jelas mencatat batasannya. Baris-baris selebihnya tetap dapat berdiri sebagai bukti rekayasa yang valid untuk klaim spesifiknya.
- **GAGAL (*FAIL*)** berarti skenario telah dicoba, dan satu atau lebih kriteria penerimaan gagal memenuhi spesifikasi yang disitasi.

Dalam keadaan apa pun, skenario yang tidak dilaksanakan tidak boleh diubah menjadi kelulusan dengan menghapus baris tersebut dari laporan, dan larian yang gagal tidak boleh dihaluskan secara eufemistis menjadi "TIDAK DIJALANKAN" dengan menghapus stempel waktu yang bermasalah. Stempel waktu dalam ekspor CSV mentah menyediakan rantai lacak (*chain of custody*) yang dapat diaudit. Menghapus rentang waktu untuk menyembunyikan langkah yang dibatalkan adalah perubahan curang terhadap rekaman rekayasa.

## Aturan Penilaian Keseluruhan

Tempatkan kelima baris dalam kotak ringkasan yang menonjol di bagian paling atas laporan kilat, tepat di bawah blok metadata. Seorang eksekutif, insinyur perwakilan pemilik, atau auditor pihak ketiga yang hanya membaca halaman pertama ini harus dapat langsung memahami status sebenarnya dari kampanye pengujian.

Penilaian keseluruhan dapat berupa:
- **LULUS KESELURUHAN (*OVERALL PASS*)**: Setiap baris dari kelima baris telah dicoba, dan setiap baris meraih predikat LULUS (*PASS*).
- **LULUS BERSYARAT / PARSIAL (*CONDITIONAL / PARTIAL PASS*)**: Baris-baris tertentu yang disepakati sebelumnya TIDAK DIJALANKAN (misalnya, Beban Lebih dikecualikan karena kendala utilitas lokasi), namun semua baris yang dicoba meraih LULUS (*PASS*). Narasi harus secara eksplisit menyatakan: *"Kelulusan Keseluruhan dibatasi hanya pada Prates, Gradien, Perubahan Langkah, dan Pasokan Tunggal; Beban Lebih tidak dievaluasi."*
- **GAGAL KESELURUHAN (*OVERALL FAIL*)**: Satu atau lebih baris yang dicoba menghasilkan GAGAL (*FAIL*). Laporan harus menyatakan moda kegagalan yang tepat, waktu kejadian, dan tindakan korektif yang disyaratkan sebelum pengujian ulang diizinkan.

Kurva yang elok dari larian tunak 15 menit tidak memenangkan suara atas prates yang tidak dijalankan atau pengujian pasokan tunggal yang gagal. Kelima baris tersebut berdiri bersama.

## Keputusan yang Harus Dicatat

Sebelum memulai pencatatan data untuk laporan kilat, tim penguji harus mencatat:

- Skenario mana dari kelima skenario yang akan dicoba oleh larian pengujian spesifik ini.
- Judul dokumen dan revisi yang tepat yang mengatur kriteria lulus/gagal untuk setiap baris.
- Waktu jeda yang dinyatakan sebelumnya untuk dataran tinggi gradien dan kunjungan beban lebih.
- Rumusan kalimat yang disepakati sebelumnya untuk pernyataan penilaian keseluruhan jika semua baris yang dicoba lulus.
- Prosedur penghentian yang ditentukan jika ada satu skenario yang memicu GAGAL (*FAIL*).
