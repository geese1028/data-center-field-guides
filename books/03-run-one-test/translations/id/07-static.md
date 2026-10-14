Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 7. Statis, Tanpa Energi

Fase verifikasi statis tanpa energi adalah tempat di mana proyek komisioning membangun fondasi keselamatan bagi semua pengujian dinamis berikutnya. Ini juga merupakan fase yang paling sering digoda oleh kontraktor untuk dipadatkan ketika pengiriman peralatan mengalami keterlambatan.

Mengompromikan fase statis untuk mengejar waktu kalender yang hilang adalah risiko operasional yang tidak dapat diterima. Cincin-O sambungan cepat (*quick-disconnect*) yang terpotong, konduktor kabel yang terjepit, kantong udara yang belum dibuang, atau fasa listrik yang terbalik pasti akan memicu pemadaman tak terjadwal selama pengujian dinamis—cara yang jauh lebih berbahaya dan mahal untuk menemukan cacat instalasi.

Dalam hierarki komisioning global, pekerjaan ini merupakan **Level 2 (Pengiriman dan QA Statis)** dan **Level 3 (Pemeriksaan Prafungsional dan Startup)**. Pekerjaan ini harus diarsipkan di bawah tab sertifikat tersebut, dan tidak boleh disalahlabeli sebagai Penerimaan Pabrik Level 1.

![Keseimbangan Manifold Multi-Rak](../figures/fig-04-multi-rack-manifold-hydraulics.png)

## Pembongkaran Peti Kemas, Inspeksi Fisik, dan Fitting Mekanikal

Setiap peralatan yang dikirim ke aula data harus diinventarisasi terhadap daftar pengepakan (*packing list*):
- **Inspeksi Sasis dan Roda Kastor**: Periksa rangka bank beban dari deformasi akibat pengiriman, pengencang struktural yang kendur, atau roda kastor yang rusak yang dapat membahayakan pembebanan lantai.
- **Kopling Lepas-Cepat (*Quick-Disconnect Couplings*)**: Periksa setiap fitting lepas-cepat sekunder (seperti kopling seri Danfoss Hansen FD83 atau kopling *dry-break* ISO 16028). Pastikan kerah pengunci (*locking collar*) terpasang mulus tanpa tergores (*galling*). Periksa segel internal elastomer EPDM di bawah pembesaran dari sobekan, lubang jarum, atau *burr* manufaktur. Jangan pernah menggunakan gemuk berbahan dasar minyak bumi pada segel EPDM; gunakan hanya pelumas berbahan dasar silikon yang disetujui atau yang kompatibel dengan sistem.
- **Rakitan Selang**: Verifikasi label selang. Semua selang sekunder fleksibel harus berupa karet sintetis berkepang kawat atau PTFE bertulang yang memiliki nilai pengenal minimal 1,5× tekanan kerja sekunder maksimum dan disertifikasi untuk operasi terus-menerus pada suhu 70°C. Periksa radius tekukan untuk memastikan tidak ada selang yang tertekuk di bawah radius minimum yang diizinkan oleh pabrikan.

## Isolasi Listrik Tanpa Energi dan Pemeriksaan Keselamatan

Semua verifikasi kelistrikan pada fase ini dilakukan dengan sirkuit pasokan hulu yang terkunci dan terlabeli (*lock-out/tag-out* - LOTO) dan dikonfirmasi tidak berenergi menggunakan detektor tegangan yang disetujui:

### 1. Resistansi Isolasi (Uji Megger)
Menggunakan penguji isolasi terkalibrasi, terapkan 1000V DC selama 60 detik antara:
- Fasa A ke Fasa B, Fasa B ke Fasa C, Fasa C ke Fasa A.
- Setiap konduktor fasa individual ke Pentanahan Peralatan (PE).
- Konduktor netral (jika ada) ke Pentanahan Peralatan.

**Standar Penerimaan**: Resistansi isolasi harus melebihi batas minimum 100 MΩ. Pembacaan apa pun di bawah 20 MΩ menunjukkan masuknya kelembapan atau isolasi yang terkompromikan dan berlaku sebagai larangan mutlak untuk pemberian energi.

### 2. Uji Ikatan Kontinuitas Pentanahan
Menggunakan mikro-ohmmeter terkalibrasi, ukur resistansi antara terminal pentanahan sasis bank beban, rangka elemen pemanas internal, dan *Main Grounding Busbar* (MGB) fasilitas.

**Standar Penerimaan**: Resistansi ikatan pentanahan tidak boleh melebihi 0,1 Ω. Sambungan tanah yang buruk menciptakan bahaya tegangan sentuh (*touch-potential*) yang mematikan jika terjadi kegagalan isolasi selama pengujian multi-megawatt.

### 3. Verifikasi Urutan dan Rotasi Fasa
Sebelum menyambungkan kabel daya bank beban ke PDU fasilitas atau kotak sadapan *busway*, ukur rotasi fasa pada stopkontak pasokan menggunakan indikator urutan fasa yang disetujui.

**Standar Penerimaan**: Rotasi fasa harus benar-benar searah jarum jam ($L_1 \to L_2 \to L_3$ / $A \to B \to C$).

> **CATATAN KESELAMATAN KRITIS POMPA**: Di aula pusat data berpendingin cairan, pompa sekunder CDU biasanya merupakan pompa sentrifugal motor kaleng hermetik (*canned motor centrifugal pumps*). Jika urutan fasa terbalik ($A \to C \to B$) diterapkan, motor pompa akan berputar terbalik. Impeler sentrifugal yang berputar mundur menghasilkan *head* dinamis mendekati nol, menyebabkan pergolakan fluida yang parah dan kavitasi, serta dapat menghancurkan bantalan dorong (*thrust bearing*) dalam hitungan menit. Sel rotasi fasa pada Lembar 1 harus mencatat rotasi searah jarum jam yang terverifikasi; jika kosong, pemberian energi dilarang keras.

## Pembilasan Sekunder Mekanikal, Penahanan Tekanan Hidrostatik, dan Pembuangan Udara

*Loop* fluida yang menghubungkan CDU, manifold distribusi, dan bank beban harus menjalani persiapan pra-komisioning yang ketat:

### 1. Pembilasan Pipa Pra-Komisioning (Standar BSRIA BG 29/2020)
Jangan pernah mengalirkan fluida melalui *loop* sekunder yang baru dipasang langsung ke dalam saluran pemanas bank beban atau penukar panas CDU. *Loop* sekunder harus dibilas terlebih dahulu melalui *loop bypass* sementara pada kecepatan penggerusan minimum 1,5 m/s untuk melepaskan kerak konstruksi, terak las, dan kotoran pipa. Bersihkan saringan (*strainer*) pipa secara berulang hingga hitungan partikulat memenuhi standar kebersihan ISO 4406 (biasanya 16/14/11).

### 2. Penahanan Tekanan Hidrostatik
Setelah dibilas dan disambungkan, sirkuit sekunder—termasuk semua manifold, selang fleksibel, dan penukar panas internal bank beban—diberi tekanan dengan air atau Propylene Glycol 25% hingga **1,5× Tekanan Operasi Maksimum yang Diizinkan (*Maximum Allowable Operating Pressure* - MAOP)** (biasanya 6,0 bar hingga 9,0 bar untuk sirkuit sekunder pusat data standar).

**Standar Penerimaan**:
- Tekanan harus ditahan terus-menerus selama **minimum 2,0 jam**.
- Pencatatan tekanan digital terkalibrasi harus menunjukkan nol penurunan tekanan yang terukur (ΔP ≤ 0,0 bar), dengan memperhitungkan ekspansi termal fluida.
- Setiap sambungan mekanikal, adaptor berulir, dan kopling lepas-cepat harus menjalani inspeksi visual dengan kertas penyerap putih bersih. Laju kebocoran yang diizinkan adalah **nol tetes per menit**.

### 3. Pembuangan Udara Menyeluruh dan Deaerasi Vakum
Gelembung mikro udara yang terperangkap adalah penyebab utama anomali komisioning. Udara yang terperangkap di dalam saluran penukar panas membentuk lapisan isolasi yang secara semu menurunkan koefisien perpindahan panas, sementara gelembung yang melewati pengukur aliran ultrasonik mengganggu sinyal akustik *transit-time*.

Aktifkan katup pembuangan udara otomatis di titik-titik tertinggi dan jalankan deaerator vakum sekunder hingga kaca intip (*sight glass*) visual menunjukkan nol busa dan kadar oksigen terlarut turun dalam batas spesifikasi.

## Audit Volume Fluida

Hitung dan dokumentasikan inventaris fluida sekunder pasti dari sistem pengujian pada Lembar 1:

$$V_{\text{total}} = V_{\text{CDU\_internal}} + \sum (V_{\text{manifold}}) + \sum (V_{\text{hoses}}) + \sum (V_{\text{load\_banks}})$$

Mendokumentasikan massa fluida fisik (M_fluid = ρ · V_total) sangat penting untuk memvalidasi perhitungan inersia termal yang diperlukan selama pengujian sistem terintegrasi Level 5.

## Koordinasi Proteksi Listrik Hulu

Lacak jalur distribusi listrik ke atas dari kotak sadapan bank beban ke PDU baris dan transformator gardu induk hulu. Audit pengaturan unit trip pemutus arus:
- Pastikan unit trip elektronik (LSIG) memiliki pengambilan seketika (*instantaneous pickup* - I_i) dan penundaan waktu singkat (*short-time delay* - I_sd) yang terkoordinasi di atas karakteristik arus masuk transformator internal bank beban atau pengontrol pemanas SCR.
- Konfirmasikan bahwa ambang batas alarm gangguan tanah diatur dengan benar sehingga arus bocor filter kapasitif residual tidak memicu trip pada pemutus sub-pasokan utama selama langkah pemanasan awal.

## Gerbang Prasyarat Statis

Tahap statis ditutup dengan tinjauan formal Lembar 1. Setiap kotak centang harus ditandai **LULUS** (*PASS*) dengan tinta, atau disertai dengan butir daftar cacat rekayasa formal. Jika ada cacat yang belum terselesaikan pada isolasi listrik, ikatan pentanahan, rotasi fasa, atau penahanan tekanan hidrostatik, gerbang proyek tertutup. Pemberian energi dinamis tidak dapat dilanjutkan.

## Keputusan yang Harus Dicatat Sebelum Mulai Pengujian

- Log inspeksi pembongkaran peti kemas, mencatat semua jumlah fitting dan audit segel fisik.
- Nilai resistansi isolasi megger dan pentanahan yang disertifikasi, ditandatangani oleh Insinyur Elektro.
- Urutan fasa searah jarum jam yang terverifikasi, ditandatangani dengan tinta.
- Sertifikat uji tekanan hidrostatik yang disaksikan (tekanan uji, durasi penahanan, penurunan nol).
- Total volume fluida sekunder yang dihitung (V_total).
- Pengaturan trip pemutus arus PDU hulu dan audit koordinasi proteksi.
