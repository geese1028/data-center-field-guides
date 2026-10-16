Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 2. Sebelum Pemanasan

Laporan kilat (*flash report*) bank beban cair dibuka dengan blok persiapan wajib. Blok ini dievaluasi sebagai lulus atau gagal jauh sebelum kilowatt panas pertama dinyalakan. Gerbang persiapan yang gagal tidak dapat berubah menjadi anomali ringan yang dapat diterima selama tahap gradien berikutnya; kegagalan tersebut harus segera menghentikan kampanye pengujian. Mengklaim bahwa pengujian termal berhasil padahal persiapan pra-pemanasan gagal merupakan kontradiksi rekayasa.

Dalam pendinginan cair berdensitas tinggi, fase pra-pemanasan menetapkan garis dasar nol (*zero-baseline*) dari seluruh semesta termodinamika. Jika garis dasar Anda terkontaminasi oleh gelembung udara, deviasi (*offset*) sensor yang tidak terkalibrasi, atau penyulang listrik yang belum diverifikasi, setiap perhitungan keseimbangan energi berikutnya pada dasarnya akan rusak.

## Empat Gerbang Persiapan

Sebelum perintah pemanasan apa pun diberikan ke kontaktor, tim penguji harus memverifikasi dan membubuhkan paraf pada empat gerbang persiapan yang berurutan:

### Gerbang 1: Semua unit terisi, dide-aerasi, dan diventilasi
Bank beban cair tidak dapat mentoleransi udara yang terperangkap. Di dalam bejana pemanas imersi, kantong udara menciptakan zona mati lokal tempat cairan tidak dapat bersirkulasi. Saat daya listrik dialirkan, selongsong elemen yang terpapar udara akan mengalami pelarian termal pembakaran kering (*dry-fire thermal runaway*) yang cepat, membuat selongsong Incoloy melepuh, menghanguskan segel penyekat (*baffle*) internal, dan memicu sakelar sentak (*snap switches*) suhu tinggi dalam hitungan detik.

Blok persiapan membutuhkan bukti fisik bahwa:
- Seluruh sirkuit yang terbasahi—termasuk bejana pemanas internal, *loop bypass* pra-komisioning 50 μm, selang penurunan (*drop hoses*) manifold, dan kopling sambung-cepat Danfoss FD83—telah terisi penuh dengan fluida perpindahan panas yang ditentukan (misalnya, PG25).
- Semua katup pembuang udara manual di titik tertinggi dan ventilasi udara otomatis (AAV) telah dibuka, diventilasi hingga mengeluarkan cairan bebas gelembung secara terus-menerus, lalu ditutup rapat kembali.
- Kaca pengamat (*sight glass*) visual atau ruang de-aerasi memastikan ketiadaan busa atau penjebakan gelembung mikro (*micro-bubble entrainment*) di bawah tekanan pompa sirkulasi penuh.

### Gerbang 2: Pasokan daya listrik diverifikasi terhadap spesifikasi rekayasa
Penyulang listrik yang menyalurkan daya ke bank beban harus cocok dengan dasar desain yang dinyatakan, bukan sambungan darurat sementara yang diharapkan diabaikan oleh orang lain.
- Verifikasi tegangan saluran-ke-saluran (*line-to-line*) di semua fasa (V_AB, V_BC, V_CA) dengan multimeter digital terkalibrasi pada terminal pemutus arus utama bank beban. Ketidakseimbangan fasa harus memenuhi V_unbalance ≤ 1,0%.
- Verifikasi rotasi fasa searah jarum jam yang benar (A-B-C) untuk mencegah putaran terbalik pada *blower* ventilasi bantu internal.
- Ukur impedansi *loop* pembumian dan verifikasi bahwa konduktor pembumian peralatan (EGC) terikat ke bus pembumian fasilitas dengan kepatuhan ketat terhadap NFPA 70 (NEC Pasal 250) atau IEC 60364-5-54.
- Lakukan pengujian operasional langsung pada sakelar pemutus utama yang dapat digembok (*lockable main disconnect switch*) untuk membuktikan bahwa unit dapat dimatikan sepenuhnya dan dikunci secara mekanis (*lockout*) dalam keadaan darurat.

### Gerbang 3: Uji mandiri unit komprehensif lulus
Setiap kabinet bank beban dalam kluster uji harus mengeksekusi urutan uji mandiri bawaan (*built-in self-test* - BIST):
- PLC supervisi harus menguji siklus semua relai kendali dan memverifikasi bahwa kontaktor imersi utama beroperasi bebas tanpa hambatan mekanis, pantulan kontak yang berlebihan, atau dengungan.
- *Loop* keselamatan berkabel keras (*hardwired*) Kelas 1 harus diverifikasi: menekan tombol jamur henti darurat (*E-stop*) pada panel depan harus memutus semua koil kendali kontaktor dalam waktu kurang dari 20 milidetik.
- Tali pendeteksi kebocoran internal atau sensor pelampung optik di bak penampung bawah harus diuji untuk memastikan ia memicu pemadaman berkabel keras seketika.
- Semua saluran komunikasi digital (Modbus-TCP / MQTT) harus melaporkan nol bendera (*flag*) alarm aktif, dan *Bitmask* Kualitas 16-bit harus terinisialisasi ke kondisi sehat (`0x0001` - `0x0007`).

### Gerbang 4: Larian garis dasar beban nol sepuluh menit yang stabil
Setelah Gerbang 1 hingga 3 selesai, seluruh kluster uji harus mensirkulasikan cairan pendingin pada aliran terukur penuh dengan semua elemen pemanas benar-benar dimatikan (diperintahkan ke nol watt).

Larian beban nol ini harus dipertahankan selama durasi terus-menerus setidaknya **sepuluh menit** (atau durasi garis dasar spesifik yang dinyatakan sebelumnya pada lembar persyaratan Anda). Tujuan dari penahanan ini adalah untuk memungkinkan *loop* dingin mencapai keseimbangan hidrolik serta mengekspos hanyutan sensor, putusnya komunikasi, atau saluran mati sebelum derau termal memasuki aliran data.

Jika seorang operator menjadi tidak sabar dan menyalakan "hanya sedikit panas" (misalnya, 5 kW) untuk menghangatkan ruangan, periode tersebut tidak dapat digunakan sebagai garis dasar persiapan. Memerintahkan pemanasan parsial selama garis dasar akan menghancurkan referensi nol. Jika panas dinyalakan secara prematur, hentikan pengujian, matikan pemanas, dan mulai ulang hitungan waktu sepuluh menit penuh dari awal.

## Apa yang Anda Catat Selama Garis Dasar

Selama menit terakhir dari larian stabilisasi beban nol sepuluh menit, catat blok garis dasar satu menit terus-menerus. Blok ini harus merekam:
- **Saluran Listrik**: Daya aktif P_elec harus terbaca tepat 0,0 kW di semua kabinet (daya *blower* parasitik bantu, biasanya 0,8 kW, harus dicatat pada baris terpisah dan tidak digabungkan dengan daya pemanas).
- **Saluran Hidrolik**: Suhu pendingin pasokan (T_in), suhu pendingin kembali (T_out), laju aliran volumetrik (Q_v), tekanan statis pasokan (P_in), dan tekanan statis kembali (P_out).
- **Saluran Udara Pendamping**: Suhu udara masuk ambien (T_air,in) dan suhu udara buang (T_air,out).

Pada garis dasar beban nol yang sehat, perbedaan suhu di seluruh inti pemanas (ΔT = T_out - T_in) biasanya akan bernilai sedikit positif—sekitar +0,05 K hingga +0,15 K—sepenuhnya disebabkan oleh daya pemompaan mekanis yang diubah menjadi kalor gesekan viskos di dalam pemipaan dan impeler pompa CDU (P_friction = Q_v · ΔP). Mendokumentasikan deviasi kecil ini sangatlah penting: hal ini mencegah auditor di kemudian hari salah menafsirkan kalor gesekan pompa sebagai kesalahan kalibrasi listrik selama langkah beban rendah.

Setiap saluran sensor yang akan muncul dalam blok data gradien berikutnya harus sudah ada, terbaca, dan sehat selama menit garis dasar ini. Sensor yang tiba-tiba "muncul" dalam ekspor di tengah pengujian gradien berarti belum diverifikasi selama persiapan. Datanya tidak dapat digunakan untuk membuktikan kepatuhan.

## Garis Dasar Resistansi Hidrolik: Kurva Impedansi Dingin

Jika lembar persyaratan Anda mencakup tugas untuk mewakili kurva resistansi hidrolik rak fisik (hubungan k_v atau C_v antara aliran dan penurunan tekanan), fase persiapan adalah tempat klaim tersebut dikalibrasi.

Pendingin dingin (misalnya, PG25 pada 35,0°C) memiliki viskositas kinematik yang lebih tinggi ($\nu ≈ 2,85 cSt$) daripada pendingin panas pada 45,0°C ($\nu ≈ 2,15 cSt$). Akibatnya, penurunan tekanan garis dasar dingin di seluruh bank beban akan sedikit lebih tinggi daripada penurunan kondisi tunak saat panas.

Selama larian persiapan beban nol:
1. Ukur tekanan diferensial di seluruh port pasokan dan kembali manifold (ΔP = P_in - P_out) pada aliran terukur (176,5 LPM).
2. Jika bank beban dilengkapi katup penyeimbang manual yang dapat disetel (seperti katup penyeimbang fungsi ganda / *triple-duty* terkalibrasi), sesuaikan tuas penyetel hingga ΔP yang terukur cocok dengan kurva impedansi rak virtual yang disitasi (misalnya, 112,0 kPa ± 3,0 kPa).
3. Kunci posisi katup penyeimbang dengan penghenti memori mekanis atau segel bukti perusakan (*tamper-evident seal*).
4. Catat posisi katup akhir, suhu fluida dingin, dan ΔP yang terukur pada lembar persiapan.

Penyetelan ini adalah garis dasar penyiapan fisik. Ini bukan hasil eksperimen. Anda tidak menulis "LULUS" untuk resistansi hidrolik selama persiapan; Anda mencatat fakta penyiapan tersebut sehingga ketika gradien termal 120 kW dijalankan nantinya, setiap perubahan dalam tekanan diferensial dapat diatribusikan secara jujur pada pergeseran viskositas yang bergantung pada suhu, bukan pada pengubahan katup tanpa izin yang tidak tercatat.

## Keputusan yang Harus Dicatat

Sebelum memberikan perintah untuk menaikkan beban ke langkah beban pertama, catat fakta-fakta berikut di bagian persiapan laporan kilat:

- Paraf teknisi yang mengonfirmasi ventilasi udara dan de-aerasi untuk setiap kabinet.
- Tegangan saluran-ke-saluran yang terukur dan resistansi *loop* pembumian untuk Penyulang A dan Penyulang B.
- Waktu pemutusan terkonfirmasi (< 20 ms) dari sirkuit henti darurat Kelas 1.
- Stempel waktu mulai dan berhenti yang tepat dari larian stabilisasi beban nol 10 menit.
- Nilai rata-rata aritmatika dari semua saluran listrik, hidrolik, dan udara selama menit garis dasar akhir.
- Posisi terkunci dari katup penyeimbang hidrolik dan ΔP dingin yang terukur.
- Tanda tangan Pemilik Lembar yang mengesahkan bahwa keempat gerbang persiapan telah meraih LULUS (*PASS*).
