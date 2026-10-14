Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 2. Beban kerja yang harus ia lewati

Bank beban dapat memenuhi setiap fungsi di bab sebelumnya dan tetap menjadi mesin yang salah. Fungsi mengatakan ia dapat diatur dan dibaca. Beban kerja mengatakan apa yang harus dapat ia jadi. Itu berbeda. Pemanas laboratorium dengan meter debit dapat diatur dan dibaca. Ia tetap mungkin tidak menjadi pengganti rak kelas NVL72, karena masalah cair rak bukan "sedikit kalor, sedikit air." Perubahan yang penting adalah rezim debit di sisi rak.

Debit sisi rak yang tinggi adalah inti kelas pendinginan cair ini. Bank beban harus dapat hidup di rezim itu, bukan di loop yang lebih lembut yang kebetulan memakai kata yang sama, pendingin. Unit yang diukur untuk kenaikan suhu kecil pada debit sedang akan terlihat sangat baik di bangku uji dan tidak berguna di manifold, atau sebaliknya: ia akan menuntut kenaikan suhu yang tidak akan pernah ditunjukkan rak, dan semua orang akan menyimpulkan rak "terlalu dingin" ketika rak hanya menggerakkan lebih banyak cairan.

Buku ini tidak akan menerbitkan jendela debit, tekanan, atau suhu vendor yang sekarang. Angka itu milik dokumen dengan revisi. Lembar beban kerja Anda menyitasi dokumen itu. Ketika revisi berubah, lembar berubah. Logamnya mungkin tidak, dan itu keputusan proyek, bukan fakta yang dapat dibekukan buku ini.

## Kalor bukan pelat nama

Daya listrik ke dalam elemen dan kalor ke dalam cairan bukan besaran yang sama. Mereka dekat ketika unit dibangun dengan baik, tunak, dan tidak membuang kalor ke ruangan atau ke massa yang belum menghangat. Mereka tidak dekat selama menit pertama sebuah langkah, atau ketika kabinet terbuka, atau ketika sebagian daya hilang di penggerak dan suplai yang tidak menyentuh cairan. Jika penerimaan Anda memperlakukan kilowatt pelat nama sebagai kalor ke dalam loop, Anda akan menerima unit yang tidak dapat melakukan pekerjaan termal, atau Anda akan menolak unit yang dapat, karena menit pertama terlihat pendek.

Tulis kedua angka di lembar, dengan nama yang berbeda. Daya listrik yang diperintahkan. Kalor tersimpul ke dalam cairan. Penyimpulan membutuhkan debit dan kedua suhu, dan itulah sebab pembacaan itu bukan hiasan opsional. Penyimpulan juga membutuhkan Anda mengatakan apakah Anda berada dalam keadaan tunak. Langkah yang belum ditahan bukan pengukuran kalor. Ia transien. Transien penting, tetapi mereka baris yang berbeda.

Anda tidak membutuhkan rumus terbitan dengan tetapan pinjaman untuk memakai ini. Anda membutuhkan kebiasaan bertanya, pada setiap dataran: apakah kenaikan suhu, kali debit, menceritakan kisah yang cocok dengan daya listrik di dalam pita yang tidak mempermalukan kesimpulan. Jika Anda tidak dapat membentuk kisah itu, Anda belum diizinkan mengatakan bank beban membebani loop. Anda diizinkan mengatakan kontaktor menutup.

## Kotak pasir dasar pendidikan: Penurunan rak virtual 120 kW

Untuk memastikan buku ini memberikan tolok ukur numerik yang konkret tanpa melanggar perjanjian kerahasiaan vendor atau membekukan lembar data berpemilik, kami menetapkan model referensi pendidikan non-proprietari. (Lihat Gambar 07 untuk lembar penurunan prinsip pertama yang lengkap).

Asumsikan rak AI virtual acuan yang beroperasi dalam loop cairan sekunder di bawah kondisi pengujian standar:
- **Beban Termal Nominal**: P_thermal = 120.0 kW
- **Media Pendingin Sekunder**: Campuran 25% Propilen Glikol / 75% Air berdasarkan volume (PG25)
- **Sifat Fisik Cairan Pendingin (@ 40°C suhu ruah rata-rata)**: Densitas ρ = 1025 kg/m³, Kalor Jenis C_p = 3.980 kJ/(kg·K)
- **Delta-T Termal Desain**: Suplai T_suplai = 35.0°C, Balik T_balik = 45.0°C (ΔT = 10.0 K)

Dari termodinamika prinsip pertama (P = ṁ · C_p · ΔT), laju aliran massa yang dibutuhkan adalah:
$$\dot{m} = \frac{120.0\,\text{kW}}{3.980\,\text{kJ/(kg}\cdot\text{K)} \times 10.0\,\text{K}} = 3.015\,\text{kg/s}$$

Mengonversi aliran massa ke laju aliran volumetrik ($Q_v = \frac{\dot{m}}{\rho}$):
$$Q_v = \frac{3.015\,\text{kg/s}}{1025\,\text{kg/m}^3} \times 60 \times 1000 = \mathbf{176.5\,\text{L/min}} \quad (\approx 46.6\,\text{GPM})$$

Sekarang lakukan verifikasi kecepatan fluida pipa hidraulik. Melintasi pipa baja tahan karat sanitasi DN32 standar (diameter dalam d_i = 32.0 mm, luas penampang A = 8.04 × 10^{-4} m²):
$$v = \frac{Q_v}{A} = \frac{0.00294\,\text{m}^3\text{/s}}{8.04 \times 10^{-4}\,\text{m}^2} = \mathbf{2.45\,\text{m/s}}$$
Kecepatan ini berada aman di bawah ambang batas erosi fluida standar 3.0 m/s untuk pipa baja tahan karat dan selang EPDM, mencegah resonansi akustik, kavitasi, dan keausan partikulat.

Terakhir, tetapkan target resistansi hidraulik. Pengganti harus cocok dengan kurva penurunan tekanan rak (ΔP = k · Q_v²). Pada aliran terukur 176.5 L/min, tekanan diferensial nominal ditargetkan pada ΔP_nominal = 115 kPa (1.15 bar), dengan pita penerimaan prototipe yang diizinkan sebesar ± 10% (103.5 kPa hingga 126.5 kPa).

Dengan persamaan kotak pasir yang tepat ini, lembar proyek Anda memiliki dasar yang tertutup secara matematis. Jika spesifikasi antarmuka yang dikutip di kemudian hari menuntut 140 kW pada 190 LPM, Anda menyesuaikan variabel-variabel tersebut secara terbuka. Metode perhitungannya tetap identik.

## Himpunan, bukan daftar

Empat besaran cair dan satu besaran listrik berjalan bersama. Kalor ke dalam cairan. Debit. Tekanan diferensial. Suhu suplai. Suhu balik. Daya listrik duduk di samping mereka sebagai sarana, bukan sebagai pengganti.

Jika satu saja hilang, yang lain dapat menceritakan kisah palsu yang terlihat seperti rekayasa.

Kalor tanpa debit: Anda mungkin memanaskan volume terperangkap, cabang buntu, atau unit yang mulai mendidih di tempat yang tidak Anda maksudkan. Suhu akan bergerak. Gerakan itu akan menakutkan dan tidak informatif.

Debit tanpa suhu: debit tinggi dapat berarti pengganti itu realistis atau bahwa kalor mati. Anda tidak dapat membedakan. Debit rendah dapat berarti langkah terkurangi yang realistis atau sumbatan. Anda tidak dapat membedakan.

Suhu tanpa debit: kenaikan kecil dapat berarti debit tinggi, yang mungkin memang Anda inginkan, atau pemanas gagal, yang adalah kebalikannya. Kenaikan besar dapat berarti kondisi seperti rak atau selang yang sedang menuju tekukan. Kenaikan sendiri tidak tahu.

Tekanan tanpa debit: Anda dapat melihat loop tertekan dan tidak tahu apakah Anda berada pada debit beban kerja atau pada tetesan melalui katup yang setengah tertutup. Stres pada debit yang salah bukan resistansi rak. Ia kecelakaan dengan manometer.

Debit dan suhu tanpa tekanan diferensial: Anda dapat menyeimbangkan kalor dan tetap menyajikan CDU dengan kejutan hidraulik. CDU lalu akan bergerak dari titik operasi yang Anda kira sedang diuji, dan buku data kemudian akan mencoba menjelaskan reaksi kendali yang bermula dari kelalaian Anda.

Daya listrik tanpa himpunan cair: Anda dapat membuktikan pengumpan menghangat dan tidak membuktikan pendingin demikian.

Jadi lembar beban kerja adalah satu titik operasi, ditulis sebagai himpunan, ditambah rentang di sekitarnya yang harus dikunjungi penerimaan. Daftar lima harapan yang tidak berhubungan adalah cara Anda mendapat unit yang dapat mencapai setiap angka pada sore yang berbeda.

## Apa yang dikandung titik operasi

Untuk setiap besaran dalam himpunan, jawab tiga pertanyaan saja.

Mengapa ia diukur. Jika jawabannya "layar punya kanal cadangan," hapus atau turunkan menjadi opsional. Besaran memperoleh tempatnya dengan mengubah keputusan: tahan langkah, hentikan langkah, atau tolak menyebut titik itu sah.

Di sisi batas mana ia diukur. Sisi rak, sisi bank beban, dan sisi CDU tidak dapat saling ditukar. Suhu suplai di keluaran CDU sudah melewati pompa dan selang. Suhu suplai di masukan bank beban adalah cairan yang dilihat pemanas. Pilih sisi yang cocok dengan kalimat yang sedang Anda coba buat benar. Lalu, jika uji kemudian membutuhkan sisi yang lain, tambahkan sebagai titik kedua alih-alih memakai ulang nama.

Kisah palsu apa yang diceritakan pembacaan yang buruk. Tulis kalimatnya. "Kenaikan suhu yang rendah akan dilaporkan sebagai kinerja tinggi ketika pemanas sebenarnya mati." Kalimat itu adalah alasan meter debit dan pembacaan daya harus duduk di samping suhu. Jika Anda tidak dapat menulis kisah palsu, Anda belum memahami titik itu. Biarkan ditandai tidak diketahui. Jangan mengisinya dengan satuan yang masuk akal dan akurasi yang dikarang.

## Nominal, langkah, dan beban lebih

Titik beban kerja adalah pengganti nominal: himpunan yang Anda maksud ketika Anda mengatakan unit dapat mewakili rak pada kondisi yang Anda pedulikan. Di sekitarnya, penerimaan mengunjungi langkah terkurangi, langkah tengah, penuh, dan nol. Setelah itu bersih, ia mengunjungi beban lebih (overload) pendek yang tingkat dan penahanannya didefinisikan di lembar penerimaan, bukan dikarang di ruangan.

Jangan menyalin tingkat itu dari laporan prototipe yang pernah Anda lihat. Persentase yang benar untuk satu susunan elemen adalah takhayul untuk yang lain. Aturannya prosedural. Lembar harus menamai tingkat dan penahanan sebelum hari itu. Tingkat harus berupa pecahan titik beban kerja yang dapat Anda sitasi, atau nilai yang secara eksplisit Anda tanggung jawabnya karena belum ada sitasi. Tanggung jawab diizinkan. Berpura-pura angka itu datang dari standar tidak.

Masa tinggal adalah bagian dari titik. Debit yang Anda sentuh lalu tinggalkan bukan debit yang Anda tahan. Nyatakan penahanan dalam waktu, atau nyatakan kriteria yang mengakhiri penahanan: suhu tidak lagi berubah dengan cara yang akan mengubah kisah kalor. Bentuk kedua lebih sulit dicurangi dan lebih sulit ditulis. Pakai jika Anda dapat mengatakan apa arti "mengubah kisah kalor" di ekspor. Jika tidak dapat, pakai jam dan jujur bahwa jam itu kemudahan.

Beban lebih bukan pelat nama kedua. Ia kunjungan pendek di atas himpunan terukur untuk melihat apakah unit tetap stabil dan apakah kalor masih pergi melalui jalur yang Anda rancang. Ia bukan izin untuk menerbitkan nilai terukur kontinu yang lebih tinggi. Halaman batasan harus mengatakan beban lebih adalah titik penerimaan transien, bukan nominal baru, kecuali Anda benar-benar merancang untuk beban kerja kontinu di sana. Sebagian besar prototipe tidak. Katakan demikian.

## Debit tinggi sebagai penggerak desain

Mengapa rezim debit mengubah mesin, bukan hanya mengubah setpoint.

Pada debit yang lebih tinggi, kalor yang sama menghasilkan kenaikan suhu yang lebih kecil. Sensor dan catatan yang memadai untuk kenaikan besar menjadi argumen tentang derau. Anda mungkin membutuhkan metode pemeriksaan, interval, dan penahanan yang lebih ketat, bukan karena buku ini menyatakan kelas akurasi baru, tetapi karena kisah yang sedang Anda coba ceritakan menjadi lebih kecil. Tulis risiko itu di lembar: "kenaikan suhu pada debit beban kerja mungkin kecil; jangan menerima titik itu berdasarkan suhu saja."

Pada debit yang lebih tinggi, sambungan, belokan, dan katup yang setengah tertutup mendominasi tekanan diferensial. Unit yang "jatuh tekanan rendah" pada debit lembut dapat menjadi resistansi dominan pada debit rak, atau dapat berkavitasi, menarik udara, atau meruntuhkan selang yang terlihat baik ketika kosong. Bab jalur cair adalah tempat Anda merancang untuk itu. Bab beban kerja adalah tempat Anda mengakuinya. Taruh "pita debit yang dimaksud" di lembar bahkan ketika angkanya masih sitasi. Pita kosong adalah pengingat. Baris yang hilang adalah cara bengkel mengukur untuk pemanas dan lupa air.

Pada debit yang lebih tinggi, distribusi tidak merata di dalam unit lebih penting. Jalur paralel yang berbagi dengan baik pada debit rendah tidak akan berbagi dengan baik ketika satu jalur punya sedikit selang tambahan. Bab jalur kalor membahas modul dan cabang. Di sini, akibat tugasnya adalah: jika Anda mengklaim satu pembacaan debit mewakili unit, Anda harus mengatakan bahwa jalur internal tidak dibebani secara terpisah, atau Anda harus mengukur cabang yang akan Anda bebani secara terpisah. Satu meter pada header adalah meter header. Ia bukan meter modul.

Tidak satu pun dari ini mengharuskan Anda menyisipkan angka liter per menit dari kertas atau salindia. Ia mengharuskan lembar beban kerja memperlakukan debit sebagai penggerak pilihan sensor, kewenangan katup, dan apa arti "satu pembacaan." Jika lembar Anda punya kilowatt tebal dan debit di catatan kaki, Anda telah membangun pemanas lembut lagi, dalam prosa.

## Jendela dan titik

Jendela spesifikasi adalah wilayah: debit, suhu, dan tekanan yang boleh dilihat sisi rak. Titik operasi adalah tempat di dalam atau pada wilayah itu tempat Anda akan duduk. Penerimaan mengunjungi beberapa tempat. Ia tidak "menutupi jendela" dengan melambaikannya.

Pilih tempat karena alasan. Nominal, karena itu klaimnya. Debit terkurangi, karena kewenangan katup dan perilaku meter berubah di sana, dan karena beberapa uji akan memintanya. Debit tinggi di dalam jendela yang disitasi, jika nominal belum berada di sana, karena itu rezim yang Anda takuti. Suhu suplai di ujung dingin dan, jika jendelanya lebar, di ujung hangat, karena massa jenis, viskositas, dan suhu permukaan pemanas tidak identik melintasi jendela. Jika Anda tidak tahu apakah jendelanya lebar, sitasi belum selesai. Jangan mengarang suhu kedua agar terlihat teliti.

Tulis kolom bernama "mengapa tempat ini." Jika satu-satunya jawaban adalah "agar ada lebih banyak baris," hapus baris itu. Baris tambahan menghabiskan waktu penahanan dan menciptakan gagal palsu.

## Apa yang berubah ketika revisi berubah

Spesifikasi antarmuka bergerak. Panduan lapangan yang menanamkan jendela tahun lalu akan menjadi kebohongan yang diam. Proses Anda harus cukup membosankan untuk bertahan atas itu.

Ketika revisi yang disitasi berubah, seseorang membaca ulang himpunan beban kerja dan menandai setiap sel: masih di dalam apa yang kita bangun, tidak lagi di dalam, atau tidak diketahui. Sel yang tidak lagi di dalam tidak memperbarui diri. Unit tidak menumbuhkan pipa yang lebih besar karena PDF berubah. Anda menerima batasan ("unit ini mewakili jendela sebelumnya, bukan yang sekarang"), atau Anda mengubah unit dan menerima ulang Gate yang terpengaruh, atau Anda berhenti mengklaim pengganti. Ketiganya terhormat. Berpura-pura penerimaan lama masih menutupi jendela baru tidak.

Catat revisi di lembar beban kerja itu sendiri, bukan di surel. Catatan penerimaan menyitasi revisi lembar. Dua lompatan cukup untuk merekonstruksi sejarah. Tiga lompatan, melalui log obrolan, adalah cara Anda kehilangan.

## Loop yang Anda sambungkan pada hari itu

Beban kerja adalah tentang unit. Unit tidak dapat menunjukkan beban kerja jika loop pada hari itu tidak dapat menyerapnya. Loop bangku uji dengan reservoir kecil dan pompa yang lelah akan terlalu panas atau kehabisan debit dan Anda akan menghukum prototipe. Tulis, di lembar penerimaan, minimum yang harus disediakan loop sementara: ia harus menyerap kalor penahanan terpanjang, dan ia harus dapat menyalurkan debit yang hendak Anda minta, pada tekanan yang boleh dilihat unit. Itu persyaratan penyiapan. Mereka bukan bank beban kedua. Mereka menghentikan Anda menjalankan Gate 3 terhadap loop yang membuat uji tidak mungkin.

Jika Anda belum tahu loop sementara, tandai tidak diketahui dengan tanggal. Jangan meninggalkannya tersirat. Loop tersirat selalu dianggap memadai, dan jarang demikian.

## Komposit: pelat nama yang mengesankan

Sebuah bengkel membangun unit yang pelat nama listriknya besar. Di bangku uji mereka menjalankannya pada debit sedang karena pompa bangku uji sedang. Kenaikan suhu mudah dilihat. Semua orang rileks. Berbulan-bulan kemudian unit diminta mengikuti debit sisi rak yang beberapa kali debit bangku uji. Kenaikan suhu menyusut ke dalam derau sensor. Tekanan diferensial melintasi jalur internal yang restriktif naik. Orang yang sama mengatakan spesifikasi rak tidak realistis. Unit diterima terhadap himpunan yang salah. Pelat nama melakukan persis apa yang dilakukan pelat nama: ia menggambarkan pemanas, bukan pengganti.

Perbaikannya bukan kata sifat yang lebih baik pada pelat nama. Perbaikannya adalah titik beban kerja yang ditulis sebagai himpunan, disitasi, dan dikunjungi pada himpunan itu sebelum siapa pun menyebut prototipe selesai.

## Komposit: jendela pinjaman

Tim lain menempelkan tabel debit dan suhu dari salindia ke lembar beban kerja dan menghapus judul salindia. Angka itu sekarang "standar." Revisi kemudian dari dokumen antarmuka yang nyata menggeser sebuah batas. Lembar masih punya angka lama, dan tidak seorang pun dapat mengatakan dari mana mereka datang. Penerimaan lulus terhadap suvenir. Sambungan nyata yang pertama gagal pada batas yang tidak lagi cocok dengan suvenir.

Perbaikannya adalah kolom sitasi. Angka tanpa judul dan revisi bukan beban kerja. Mereka rumor. Jika Anda tidak diizinkan menyalin angka ke dalam buku, Anda juga tidak diizinkan menyalinnya ke dalam lembar tanpa sitasi. Izin memakainya pada proyek bukan izin yang sama dengan izin melepaskannya dari sumbernya.

## Beban kerja listrik, singkat

Umpan listrik harus dapat menopang langkah tertinggi yang akan Anda perintahkan, termasuk penahanan beban lebih jika beban lebih itu listrik dan bukan hanya termal. Catat tegangan dan frekuensi sebagai sitasi terhadap apa yang benar-benar akan disediakan aula, atau bangku uji. Catat apakah perlindungan unit menganggap ada netral, pembumian, atau perilaku pemutus tertentu hanya sejauh asumsi yang salah akan membuat bab keadaan aman menjadi salah. Jangan mengubah ini menjadi studi sistem daya. Perhatikan kecurangan yang umum: penerimaan termal dijalankan dari umpan sementara yang tidak dimiliki aula. Jika unit yang diserahkan membutuhkan umpan yang berbeda, baris antarmuka daya tidak diterima.

## Keadaan tunak, langkah, dan trip

Beri lembar beban kerja tiga jenis baris, agar orang berhenti berdebat jenis apa suatu angka.

Baris tunak adalah himpunan pada dataran, setelah kriteria penahanan. Baris langkah adalah perintah untuk bergerak, dan apa yang harus benar selama gerakan: tidak ada trip, tidak ada data usang, debit tidak runtuh kecuali langkah itu adalah langkah debit. Baris trip bukan beban kerja dalam arti keluaran. Mereka kondisi di mana beban kerja harus berakhir. Taruh penunjuk ke bab keselamatan alih-alih mengarang nilai trip di sini. Jika nilai trip ada di spesifikasi yang disitasi, sitasi. Jika itu pilihan Anda, labeli sebagai pilihan Anda.

Pemisahan ini menjaga beban lebih agar tidak dipakai sebagai nilai terukur tunak, dan menjaga setpoint trip agar tidak dipakai sebagai sasaran kinerja. Sasaran dan batas adalah arah yang berbeda. Unit yang berjalan paling baik pada titik tripnya adalah unit yang tidak Anda pahami.

## Apa yang NVIDIA terbitkan di situs pusat data

Dibaca pada 11 Oktober 2026 dari https://www.nvidia.com/en-us/data-center/ dan halaman produk yang tertaut darinya. Ini halaman NVIDIA. Kalimat di bawah adalah ekstrak pendek fakta konfigurasi yang berkenaan dengan bank beban. Mereka bukan salinan halaman, dan bukan spesifikasi antarmuka.

Situs itu katalog. Ia menggambarkan komputasi terakselerasi, pabrik AI, jaringan, dan produk rak. Ia tidak, pada halaman yang dibaca untuk draf ini, menerbitkan debit pendingin, suhu suplai, tekanan diferensial, atau keluarga sambungan yang harus dipenuhi bank beban. Sel-sel itu tetap kosong sampai datasheet atau spesifikasi rak yang saat itu berlaku mengisinya. Jangan mengarangnya dari katalog.

Dua halaman rak adalah yang dapat dipakai buku ini.

GB200 NVL72, halaman produk https://www.nvidia.com/en-us/data-center/gb200-nvl72/. NVIDIA menggambarkannya sebagai berskala rak dan berpendingin cairan. Konfigurasi yang diterbitkan adalah 36 CPU Grace dan 72 GPU Blackwell, satu domain NVLink. Tabel spesifikasi di halaman yang sama, yang harus Anda baca ulang daripada memercayai kalimat ini jika halaman telah berpindah, mencantumkan 13.4 TB HBM3E, 17 TB LPDDR5X, 130 TB/s lebar pita NVLink, dan 2,592 inti Arm Neoverse V2. Datasheet tertaut dari halaman itu. Kelipatan kinerja terhadap H100 ada di halaman. Mereka bukan beban kerja. Mereka tidak masuk ke dataran.

GB300 NVL72, halaman produk https://www.nvidia.com/en-us/data-center/gb300-nvl72/. NVIDIA menggambarkannya sebagai berpendingin cairan sepenuhnya dan berskala rak: 72 GPU Blackwell Ultra dan 36 CPU Grace. Blok spesifikasi di halaman itu mencantumkan lebar pita NVLink 130 TB/s, memori cepat 37 TB, memori GPU 20 TB, LPDDR5X 17 TB, dan 2,592 inti Arm yang sama. Datasheet Blackwell Ultra tertaut dari halaman itu. Angka 50x dan 30x di halaman itu adalah klaim kinerja yang diproyeksikan. Mereka bukan kalor, debit, atau tekanan.

Vera Rubin NVL72 tercantum di katalog yang sama sebagai produk berskala rak yang kemudian. Sitasi hanya jika itu generasi yang sedang Anda gantikan. Jangan menganggap antarmuka cairnya cocok dengan GB200 karena namanya masih mengatakan NVL72.

Apa yang dilakukan ini terhadap lembar beban kerja itu sempit. Pengganti itu cair, bukan udara. Unit mewakili satu rak dari generasi yang Anda sitasi, bukan gedung, bukan jaringan, dan bukan FLOPS GPU. Lebar pita memori dan lebar pita NVLink bukan debit pendingin. Bank beban yang dapat menyamai angka FLOPS yang diterbitkan dan tidak dapat mengatakan debit dan kedua suhu belum memenuhi bab ini. Tulis nama generasi dan tanggal halaman di kepala beban kerja. Biarkan debit, suhu, dan tekanan diferensial untuk revisi datasheet yang boleh Anda pakai.

Tautan lain di katalog, dan mengapa mereka tinggal di luar kisah kalor: kartu lini GPU pusat data, katalog sistem yang memenuhi syarat, dan NVIDIA-Certified Systems, untuk mengidentifikasi server, bukan untuk mengukur selang. MLPerf, untuk tolok ukur beban kerja, bukan untuk dataran termal. Mission Control, untuk perangkat lunak operasi pabrik, bukan untuk henti lokal. Spectrum-X, Quantum InfiniBand, dan BlueField, untuk jaringan, yang tidak diterima buku ini. MGX, sebagai acuan server modular, hanya jika pemilik antarmuka mengatakan rak yang akan Anda sambungkan adalah varian MGX berpendingin cairan. DSX, sebagai kisah biaya per megawatt, bukan kilowatt ke dalam cairan Anda.

## Sumber publik untuk bab ini

Himpunan beban kerja tetap kosong sampai revisi yang disitasi mengisinya. Halaman publik NVIDIA menetapkan kelas: berpendingin cairan, berskala rak, bukan beban udara yang lembut. Datasheet yang tertaut dari halaman itu adalah tempat angka antarmuka akan berada, jika Anda diizinkan memakainya pada proyek. Jangan menyalin kelipatan pemasaran dari halaman ke dalam sel. Faktor terhadap platform yang lebih lama bukan debit dan bukan suhu. Panduan termal ASHRAE, dalam edisi mana pun yang Anda lisensi untuk dibaca, adalah tempat kelas dan lingkungan yang dianjurkan didefinisikan. Kelas itu tidak dicetak ulang di sini. Jika beban kerja Anda menyitasi kelas ASHRAE, sitasi mencakup edisi, dan jendela numerik tinggal di lembar proyek. ANSI/ASHRAE 90.4 adalah standar energi untuk pusat data. Ia tidak menetapkan dataran bank beban. Jangan biarkan klaim energi aula berpindah ke himpunan beban kerja ini.

## Keputusan yang dicatat

- Himpunan nominal: kalor ke dalam cairan, debit, tekanan diferensial, suhu suplai, suhu balik, daya listrik. Setiap sel disitasi atau ditandai tidak diketahui.
- Mengapa setiap tempat yang akan Anda kunjungi ada di lembar, termasuk penahanan beban lebih.
- Di sisi batas mana setiap besaran cair dibaca.
- Kisah palsu yang akan diceritakan setiap besaran yang hilang.
- Apa yang harus diserap dan disalurkan loop sementara pada hari penerimaan.
- Aturan perubahan revisi: batasan, modifikasi, atau hentikan klaim.
