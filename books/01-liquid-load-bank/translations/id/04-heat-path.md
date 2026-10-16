Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 4. Jalur kalor dan modul

Kalor adalah produk. Jalur cair hanya membawanya. Perlakukan sebagai desain terpisah yang harus setuju pada titik beban kerja. Manifold yang indah dengan pemanas yang hanya dapat mati atau nyala adalah rakitan katup. Pemanas besar tanpa jalur yang jujur bagi kalor ke dalam cairan yang bergerak adalah pemanas ruangan yang kebetulan punya sambungan.

Bab ini memutuskan bagaimana kalor dibagi, bagaimana ia dilangkah, bagaimana kenaikan mendadak bekerja, bagaimana modul keluar, dan bagaimana gangguan tetap lokal. Ia tidak memutuskan peta kilowatt modul dari prototipe mana pun yang pernah Anda lihat. Peta itu sisa proyek. Polanya tidak.

## Ke mana kalor harus pergi

Setiap watt yang Anda perintahkan punya tujuan. Ke dalam aliran cairan yang sedang Anda ukur. Ke dalam logam yang kemudian akan mengembalikan kalor, yang adalah simpanan, bukan penyerahan. Ke dalam ruangan, melalui selungkup. Ke dalam kantong cairan yang tidak ada di debit yang diukur. Penerimaan peduli pada yang pertama. Yang lain adalah galat, tunda, atau rugi. Anda tidak membutuhkan laboratorium kalorimeter untuk menghormati pembedaan itu. Anda membutuhkan kebiasaan, yang sudah dinyatakan di bab beban kerja, membandingkan daya listrik dengan kisah kalor di cairan setelah penahanan.

Desain mengikuti kebiasaan itu. Permukaan yang menghasilkan kalor harus melihat aliran yang Anda ukur, bukan cabang samping, bukan tangki yang bercampur lambat, bukan pelat yang menghadap udara di satu sisi dan tetesan di sisi lain. Jika geometri tidak dapat menaruh permukaan di aliran, ubah geometri sebelum Anda berdebat tentang kendali. Kendali tidak dapat mendorong kalor ke dalam cairan yang tidak ada.

Massa termal bukan realisme gratis. Blok berat akan membuat setiap langkah terlihat lambat dan akan membuat beban lebih terlihat aman untuk sementara, karena logam menyerap apa yang belum diambil cairan. Jika pengganti Anda seharusnya menyajikan kalor dengan segera, massa adalah distorsi. Jika pengganti Anda seharusnya menyerupai inersia termal rak, massa adalah klaim, dan ia harus ditulis sebagai klaim dengan alasan. Jangan biarkan massa terjadi karena vendor elemen menjual rakitan tebal. Tulis apakah tanggapan cepat atau inersia adalah tujuan. Untuk bank beban yang pekerjaannya melatih rantai pendinginan, cepat dan terukur biasanya mengalahkan inersia yang tidak disengaja. Inersia yang tidak disengaja menyembunyikan debit yang gagal.

## Neraca daya termal dan kalor jenis fluida: PG25 vs. air DI

Kebenaran termodinamika mendasar dari bank beban adalah persamaan neraca daya termal tertutup:

$$Q = \dot{m} \cdot C_p \cdot \Delta T = \rho \cdot Q_v \cdot C_p \cdot (T_{\text{kembali}} - T_{\text{pasok}})$$

Di mana:
- Q adalah kalor termal yang dipindahkan ke dalam aliran cairan (kW).
- ṁ adalah laju aliran massa (kg/s), dan Q_v adalah laju aliran volumetrik (m³/s atau L/min).
- ρ adalah massa jenis cairan pendingin (kg/m³).
- C_p adalah kapasitas kalor jenis (kJ/(kg·K)).
- ΔT = T_kembali - T_pasok adalah kenaikan suhu melintasi bank beban (K).

Sifat fisik cairan pendingin menentukan rezim aliran yang diperlukan untuk menyerap daya nominal. Dalam pendinginan cair pusat data, loop sekunder sebagian besar mengedarkan Propilen Glikol 25% berdasarkan volume (PG25) atau air Deionisasi (DI) yang diolah:
- **Cairan Pendingin PG25 (@ rata-rata curah 40°C)**: Massa jenis ρ = 1025 kg/m³, Kalor Jenis C_p = 3.980 kJ/(kg·K).
- **Air DI (@ rata-rata curah 40°C)**: Massa jenis ρ = 992 kg/m³, Kalor Jenis $C_p = 4,179\,\text{kJ/(kg}\cdot\text{K)}$.

Karena PG25 memiliki kapasitas kalor jenis sekitar 5% lebih rendah daripada air murni, penyerapan beban termal 120,0 kW pada ΔT sebesar 10,0 K membutuhkan laju aliran massa 3,015 kg/s (176,5 L/min untuk PG25) dibandingkan dengan 2,871 kg/s (172,2 L/min untuk air DI).

Jika seorang operator uji mengasumsikan konstanta air murni (4,18 kJ/(kg·K)) saat mengedarkan PG25, kalor termal yang dihitung akan menaksir terlalu tinggi kenyataan sebesar ~5%, menghasilkan diskrepansi buatan dalam neraca listrik-ke-termal. Setiap perhitungan pada lembar penerimaan harus mencantumkan campuran fluida tertentu dan sifat-sifatnya yang bergantung pada suhu.

## Langkah adalah dataran, bukan kenop

Anda membutuhkan kalor berlangkah. Komisioning dan penerimaan sama-sama perlu melihat mesin bergerak melalui pecahan titik beban kerja dan duduk di sana cukup lama untuk dipercaya. Namai dataran di lembar sebelum siapa pun mengukur kontaktor: langkah rendah, langkah tengah, langkah tinggi, penuh, dan nol. Anda boleh menambah satu lagi jika uji yang nyata membutuhkannya. Anda tidak boleh menambah sepuluh karena pengendali punya medan persentase.

Setiap dataran membutuhkan definisi yang tidak bergantung pada suasana layar. Lebih baik: dataran ini adalah daya listrik yang diperintahkan, dan ia sah hanya ketika himpunan cair berada di dalam pita yang Anda sitasi untuk dataran itu. Jika Anda belum punya pita, dataran tetap daya yang diperintahkan yang ditahan selama penahanan, dan himpunan cair dicatat alih-alih dinilai. Mencatat tanpa menilai dapat diterima lebih awal. Menilai tanpa mencatat tidak. Menyebut posisi kenop sebagai dataran bukan keduanya.

Masa tinggal milik dataran. Nyatakan. Masa tinggal yang berakhir ketika seseorang bosan akan pendek pada hari truk menunggu dan panjang ketika demonstrasi berjalan baik. Tidak satu pun adalah pengukuran.

Kembali ke nol adalah dataran tersendiri. Perintah kalor pada nol, debit masih dapat dibaca, suhu turun karena alasan yang dapat Anda lihat. Unit yang tidak dapat duduk pada nol tanpa dimatikan seluruhnya mungkin masih dapat diterima, tetapi lalu "nol" berarti "mati aman," dan lembar harus mengatakan bahwa nol terencana dan henti darurat adalah keadaan yang sama. Jika mereka sama, Anda tidak dapat mengambil pembacaan hidraulik beban nol tanpa susunan khusus. Tulis batasan itu atau beri diri Anda keadaan kalor-nol yang sejati dengan pompa dan katup masih dalam kondisi uji.

## Kenaikan mendadak

Dataran membuktikan Anda dapat menahan. Kenaikan mendadak membuktikan Anda dapat bergerak tanpa landaian rahasia yang tidak dapat dilewati operator. Kendali pendinginan pada uji yang nyata mungkin dinilai dari cara mereka bereaksi terhadap perubahan. Bank beban yang hanya merayap tidak akan pernah menyajikan perubahan itu. Spesifikasi satu kenaikan, dari dataran bernama ke dataran bernama yang lebih tinggi, dengan perintah yang cepat relatif terhadap tanggapan termal yang Anda pedulikan. Anda tidak harus menerbitkan milidetik. Anda harus mengatakan "bukan landaian lambat," dan Anda harus mengatakan apa arti lambat di lembar Anda: misalnya, perintah mencapai nilai baru sebelum suhu cairan selesai bergerak. Jika perintah itu sendiri memakan waktu selama pengendapan termal, Anda tidak membeli kenaikan mendadak. Anda membeli landaian kedua.

Kenaikan mendadak bukan undangan untuk membanting unit ke dalam trip demi olahraga. Dataran tujuan harus yang boleh Anda tahan. Jika Anda menginginkan pulsa di atas nilai terukur, itu kunjungan beban lebih, dengan penahanan dan jalan keluar, bukan bantingan tanpa nama.

Kepatuhan semu: penggeser perangkat lunak dengan animasi, sementara kontaktor menyala bertahap dalam jeda panjang yang tidak didokumentasikan siapa pun. Penahapan dapat menjadi praktik listrik yang baik. Penahapan tersembunyi adalah landaian. Dokumentasikan waktu tahap. Jika jumlah waktu tahap adalah skala waktu termal, sebut landaian dan berhenti menyebutnya mendadak.

Bukti: ekspor menunjukkan perintah meloncat, lalu daya, lalu suhu, pada satu garis waktu. Jika ketiganya berada di berkas berbeda dengan jam yang tidak tersinkron, Anda tidak punya bukti. Anda punya tiga kisah.

## Modul

Modul adalah cara Anda mendapat langkah, redundansi, dan servis tanpa satu elemen yang hanya dapat nyala atau mati. Aturan yang penting adalah servis dan pengurungan gangguan. Merek tidak penting. Label kilowatt dari unit sebelumnya tidak penting.

Modul harus dapat keluar tanpa menggerakkan tetangganya dan tanpa mengeringkan seluruh manifold jika Anda mengklaim keterlayanannya. Jika pelepasan mensyaratkan pengeringan, katakan demikian, dan taruh prosedur drain di berkas. Persyaratan drain tersembunyi adalah cara modul tidak pernah dilepas dan elemen gagal dibiarkan dalam hitungan. Penerimaan mencakup pelepasan satu modul, atau padanan yang didemonstrasikan jika modul berada di belakang sambungan yang boleh Anda putus, dilakukan sekali, dengan jangkauan dari bab cair masih benar sesudahnya. Jika Anda merakit kembali dan satu jangkauan hilang, demonstrasi servis gagal.

Gangguan pada satu modul tidak boleh menjadi gangguan pada loop. Kegagalan elemen terbuka harus melepaskan kalor modul itu, bukan menghubung-singkat umpan ke tetangganya. Kebocoran pada sambungan modul harus dapat diisolasi jika Anda mengklaim isolasi, atau harus menjadi peristiwa "keringkan unit" yang dinyatakan jika Anda tidak. Yang tidak boleh Anda miliki adalah hal ketiga yang tidak diuraikan, di mana kebocoran memaksa pilihan yang tidak ditulis siapa pun sementara pemanas tetap menyala.

Bias desain adalah menuju keadaan aman. Hilangnya kendali melepaskan kalor. Ia tidak mengunci kalor menyala. Hilangnya komunikasi modul melepaskan kalor modul itu. Ia tidak meninggalkan perintah terakhir terkunci kecuali kunci itu keadaan lokal yang disengaja, terlihat, yang telah diuji penerimaan. Kalor terkunci dengan pengendali mati adalah mode kegagalan yang harus Anda tulis ujinya, atau rancang keluar. Lebih baik rancang keluar.

Berapa banyak modul. Cukup untuk membangun dataran yang Anda namai tanpa bergantung pada satu elemen untuk beban penuh, kecuali Anda secara eksplisit menerima bahwa kegagalan satu elemen adalah kehilangan total kalor dan Anda tetap dapat berhenti dengan aman. Beban penuh satu elemen lebih sederhana dan rapuh. Beberapa elemen lebih banyak untuk dikabel dan lebih mudah dilangkah. Pilih terhadap dataran dan aturan keadaan aman, bukan terhadap foto interior orang lain.

Keseimbangan antar modul penting ketika mereka berbagi jalur cair. Jika satu modul mengambil sebagian besar debit dan yang lain mengambil sedikit, daya listrik yang sama adalah suhu permukaan yang tidak sama. Modul yang kelaparan trip atau menurun sementara suhu header terlihat baik. Ini masalah distribusi tidak merata dari bab beban kerja, dilihat dari sisi kalor. Entah rancang cabang agar berbagi melintasi pita debit, atau ukur cabang, atau jangan mengklaim bahwa pembacaan header menggambarkan kesehatan modul. Klaim yang tidak dapat Anda ukur adalah batasan. Tulis. Jangan menemukannya sebagai bau terbakar.

## Pengelompokan dan apa yang harus dijawab uji kemudian

Satu loop yang mewakili seluruh rak itu sederhana. Ia juga buta terhadap distribusi tidak merata di dalam rak yang tidak benar-benar Anda uji. Beberapa loop yang mewakili kelompok jalur sekunder mengatakan lebih banyak dan menghabiskan lebih banyak katup, meter, dan selang. Pilih terhadap pertanyaan yang harus dijawab uji kemudian.

Jika buku proyek hanya membutuhkan "permintaan sisi rak hadir di manifold," satu loop yang berinstrumen baik mungkin cukup. Membangun enam loop agar terasa serius adalah cara anggaran hilang ke sambungan. Jika proyek harus menunjukkan bahwa manifold mengumpan lebih dari satu jalur, dan bahwa jalur itu dapat dibebani secara berbeda, bank beban harus menyajikan lebih dari satu jalur, dengan kewenangan kalor dan debit pada setiap jalur yang akan Anda perintahkan secara independen. Manifold sumbat boneka bukan beban multi-jalur. Ia kostum.

Tulis pertanyaan dalam satu kalimat di puncak seksi jalur kalor berkas Anda. "Unit ini harus membiarkan kami memerintahkan dua kalor berbeda pada dua cabang yang berbagi masukan." Atau, "Unit ini adalah satu cabang, dan klaim apa pun tentang distribusi internal rak berada di luar lingkup." Keduanya sah. Keadaan yang tidak sah adalah tiga cabang di render dan satu pemanas di sasis.

Setiap cabang yang akan Anda perintahkan secara independen membutuhkan enam fungsi, atau subset tertulis. Cabang dengan kalor dan tanpa pembacaan debit adalah cabang yang akan Anda ceritakan kisahnya dengan salah. Jika subset menjatuhkan fungsi, kejatuhan itu batasan pada cabang itu, dan hasil uji mana pun dari cabang itu mewarisi batasan. Hasil tidak mengungguli lembar.

## Bypass, trim, dan siapa yang boleh menggerakkan debit

Kalor dan debit bertemu pada kewenangan. Bank beban yang hanya dapat mengurangi debit dengan menutup satu-satunya jalur akan melawan CDU, atau akan membuat pompa buntu, atau akan trip pada suhu karena katup yang sama yang men-trim debit juga memerangkap kalor. Katakan, dalam prosa, apa yang boleh bergerak.

Katup trim pada bank beban, seri dengan seksi kalor, dengan bypass di sekitar seksi kalor sehingga debit total pada antarmuka rak dapat tetap tinggi sementara debit seksi kalor diredam. Ini desain yang nyata, dan ia membutuhkan dua kisah debit atau pernyataan yang jelas bahwa Anda hanya mengukur satu dari mereka. Jika Anda hanya mengukur debit total, Anda tidak tahu debit yang menyentuh pemanas. Jika Anda hanya mengukur debit pemanas, Anda tidak tahu apa yang dilihat manifold. Himpunan beban kerja harus mengatakan debit mana yang adalah debit pengganti. Lebih baik ukur keduanya jika keduanya dapat bergerak.

Bypass yang tetap, tidak dikendalikan, adalah jalur bocor bagi kalor. Ia akan membuat kenaikan suhu terlihat kecil. Ia dapat diterima hanya jika digambar, diukur dengan sengaja, dan dimasukkan ke dalam kisah kalor.

Permintaan kembali ke CDU untuk mengubah debit. Diizinkan sebagai metode proyek. Tidak diizinkan sebagai ketergantungan tersembunyi prototipe. Jika unit tidak dapat mencapai pita debit tanpa perintah CDU yang tidak Anda miliki, unit tidak punya debit yang dapat diatur. CDU yang punya. Taruh itu di batasan atau ubah unit.

Tanpa trim sama sekali, debit disetel oleh loop eksternal, kalor disetel oleh Anda. Juga diizinkan, dan sering lebih sederhana, asalkan loop eksternal pada hari penerimaan benar-benar dapat menyetel debit, dan asalkan Anda tidak mengklaim pengaturan debit yang tidak dimiliki unit. Daftar persyaratan di bab 1 meminta debit yang dapat diatur. Jika Anda sekarang memutuskan pengaturan tinggal di luar unit, revisi baris itu. Jangan meninggalkan kedua klaim berlaku.

Tulis kalimat kewenangan: "Debit pada antarmuka disetel oleh A. Debit melalui seksi kalor disetel oleh B. Kalor disetel oleh C." Jika A, B, dan C adalah katup yang sama, katakan demikian, dan terima penggandengan sebagai batasan. Kewenangan tergandeng berarti Anda tidak dapat berjalan kalor dan debit secara independen. Beberapa uji perlu berjalan secara independen. Jika milik Anda demikian, satu katup adalah desain yang salah.

## Mode kegagalan yang layak ditulis

Daya listrik penuh, kenaikan suhu sedikit. Entah debit jauh di atas titik yang Anda kira, atau kalor tidak ada di cairan, atau sensor suhu tidak ada di aliran. Tanggapannya bukan menambah daya. Tanggapannya adalah memeriksa himpunan: debit, lokasi sensor, dan apakah bypass mencuri kenaikan. Penerimaan menggagalkan dataran jika kisah kalor tidak cocok dan tidak seorang pun dapat menjelaskan tujuan watt.

Kenaikan suhu dengan debit yang runtuh. Sumbatan, tekukan, katup yang tidak berada di tempat Anda kira, saringan yang Anda lupakan, udara. Kalor harus lepas jika debit runtuh di bawah titik yang Anda namai sebagai minimum untuk kalor yang aman. Minimum itu perlindungan, bukan sasaran kinerja. Namai atau sitasi. Unit yang mempertahankan kalor penuh ke dalam debit yang runtuh sedang mendaki menuju henti suhu berlebih, dan ia mungkin kalah dalam perlombaan.

Satu modul panas, tetangga diam, daya total "benar." Distribusi di dalam unit. Pembacaan header tidak akan melihatnya kecuali sensor modul atau debit cabang ada. Jika Anda tidak punya keduanya, Anda tidak dapat mengklaim kesehatan modul. Mode kegagalan lalu adalah: Anda akan berjalan seperti ini selama berjam-jam. Perbaikannya adalah sensor atau batasan yang melarang beban penuh tanpa pengawasan. Lebih baik sensor jika beban penuh adalah produk.

Trip tanpa alarm. Anda kehilangan uji dan alasan bersama. Sudah dilarang di persyaratan. Diulang di sini karena desain jalur kalor sering mengimplementasikan trip di kontaktor dan alarm di perangkat lunak yang tidak melihat kontaktor. Kabelkan alarm ke hal yang benar-benar melepaskan kalor, atau terima bahwa alarm adalah rumor.

Kalor menyala, perintah mati. Kontaktor yang dilas, relai terkunci, susunan daya kendali yang mengumpan balik. Ini uji keadaan aman. Perintahkan nol dan matikan daya kendali secara terpisah. Keduanya harus berakhir dengan kalor mati. Jika mematikan daya kendali menyalakan kalor, berhenti. Unit itu bukan prototipe yang boleh Anda selesaikan dengan menulis prosedur. Ubah sirkuit.

Kebocoran lambat kalor ke ruangan. Kisah cair hampir cocok, dan ruangan menjadi panas, dan seseorang "mengoreksi" neraca kalor dengan faktor. Faktor dapat menjadi suku rugi yang jujur jika Anda mengukurnya. Faktor yang diketik agar lembar lajur tertutup adalah kecurangan terhadap diri sendiri. Entah ukur rugi selungkup atau jaga pita cukup lebar sehingga Anda tidak berpura-pura pada ketelitian yang dicuri selungkup. Jangan menerbitkan efisiensi palsu.

Langkah yang tidak rata. Dataran tengah tidak berada di antara rendah dan tinggi, karena modul tidak sama atau karena tahap gagal dan pengendali tetap mengatakan persentase. Bukti adalah daya terukur, bukan medan persentase. Taruh daya terukur di ekspor. Persentase tanpa watt adalah permintaan, bukan hasil.

## Kendali, hanya sejauh yang disyaratkan kalor

Kendali di bab ini punya satu pekerjaan: membuat dataran dan kenaikan mendadak benar, dan membuat keadaan aman benar. Bab berikutnya akan berbicara tentang data. Jangan membangun sistem kendali yang membutuhkan bab data agar dapat mematikan kalor. Lokal, membosankan, dan dapat diuji mengalahkan berjaringan dan cerdik untuk jalur henti. Jaringan boleh meminta dataran. Jaringan tidak boleh menjadi satu-satunya hal yang menahan kontaktor terbuka. Jika kalimat itu bentrok dengan produk yang disukai vendor Anda, produk tidak memenuhi persyaratan. Tulis bentrok itu. Jangan biarkan demo dasbor menyelesaikannya.

Mode manual penting. Orang di lantai harus dapat memerintahkan nol tanpa masuk ke apa pun. Henti lokal yang hanya menghentikan layar bukan henti. Labeli kendali lokal dengan dataran yang benar-benar Anda miliki, atau dengan mati dan permintaan untuk jarak jauh. Tombol tidak berlabel menjadi folklor.

Interlock yang berada di sini: tidak ada kalor jika debit di bawah minimum yang Anda namai, tidak ada kalor jika katup isolasi tertutup, tidak ada kalor jika sensor cair yang disyaratkan untuk perlindungan gagal. Setiap interlock membutuhkan perilaku ketika sensor yang mengumpannya gagal. Sensor debit yang gagal harus melepaskan kalor, bukan melewati interlock. Interlock yang dilewati adalah jumper. Jumper bukan mode. Jika pemeliharaan membutuhkan jumper, ia kekalahan terkendali, tercatat, kalor dihambat atau dibatasi ketat, dan tidak mungkin dibiarkan di tempat tanpa tanda yang terlihat. Penerimaan mencoba meninggalkan kekalahan terpasang dan memeriksa bahwa unit menolak terlihat normal.

## Apa yang tidak digambar

Jangan menaruh gambar fabrikasi di berkas serah dan menyebutnya dasar desain. Gambar akan membekukan ukuran lubang dan tidak akan membekukan kalimat kewenangan. Kalimat kewenangan lebih penting. Jangan menerbitkan peta modul kilowatt listrik yang disalin dari unit lain. Jangan menerbitkan skema kendali sebagai pengganti uji keadaan aman. Skema dapat salah dengan cara yang penting, yaitu cara kabel benar-benar berjalan. Uji adalah kewenangan. Skema adalah kemudahan jika ia cocok dengan uji.

Jangan menggambar CDU di dalam jalur kalor Anda agar gambar terlihat seperti sistem. Saat CDU berada di dalam gambar Anda, orang akan menugaskan Anda kegagalannya. Pertahankan batas.

## Komposit: persentase yang berbohong

Pengendali menawarkan satu persen sampai seratus. Penerimaan duduk di setengah karena skrip mengatakan lima puluh. Daya listrik terukur tidak berada di dekat setengah dari penuh, karena setengah di perangkat lunak adalah setengah modul diaktifkan, dan dua dari modul itu gagal terbuka, dan perangkat lunak tidak menghitung watt. Kenaikan suhu cairan setuju dengan daya yang lebih kecil, bukan dengan persentase. Unit tidak harus tidak aman. Definisi dataran salah. Perbaiki definisi ke daya terukur, perbaiki modul yang gagal, dan berhenti menulis skrip dalam persen sampai persen punya kalibrasi watt yang telah Anda periksa.

## Komposit: pertarungan dengan pengumpan

Unit men-trim debit dengan katup yang sama yang mengumpan pemanas, dan tidak punya bypass. Di ujung debit tinggi jendela yang disitasi katup hampir terbuka dan tidak berguna sebagai trim. Di ujung debit rendah ia hampir tertutup dan pemanas trip. Tim menambahkan landaian perangkat lunak untuk "menstabilkan." Landaian menyembunyikan fakta bahwa kendali independen atas kalor dan debit tidak pernah mungkin. Kalimat kewenangan, ditulis lebih awal, akan memaksa bypass atau revisi klaim debit yang dapat diatur. Perangkat lunak tidak akan menciptakan jalur hidraulik.

## Sumber publik untuk bab ini

Uraian publik NVIDIA menaruh kalor kelas rak ini di rak berpendingin cairan, bukan di sasis berpendingin udara yang dapat Anda tiru dengan pemanas ruangan. Itu menopang kalimat pengelompokan: unit menjadi pengganti kalor sisi rak. Ia tidak menopang peta modul, pecahan kilowatt, atau klaim bahwa susunan pemanas Anda cocok dengan milik mereka. Jangan membuka datasheet dan menyalin angka daya ke daftar dataran. Daftar dataran adalah daya terukur yang akan Anda duduki, disitasi atau dipilih. Bahan ASHRAE tentang desain peralatan IT dan tentang teknologi pendinginan dapat memberi tahu apakah massa dan tanggapan Anda adalah klaim atau kecelakaan. Sitasi judul. Jangan menceritakan ulang bab. Kalimat kewenangan tetap milik Anda. Tidak ada kertas putih yang akan menulisnya untuk Anda.

## Keputusan yang dicatat

- Ke mana kalor yang diperintahkan disyaratkan pergi, dan apakah massa termal adalah klaim atau kecelakaan.
- Dataran, penahanan, dan definisi dataran yang sah.
- Uji kenaikan mendadak, terpisah dari landaian dan dari beban lebih.
- Servis modul dan gangguan yang harus tetap lokal.
- Pertanyaan satu kalimat yang harus dijawab pengelompokan.
- Kalimat kewenangan untuk debit antarmuka, debit seksi kalor, dan kalor.
- Uji keadaan aman: perintahkan nol, dan matikan daya kendali.
- Interlock, dan perilaku ketika sensor mereka gagal.
