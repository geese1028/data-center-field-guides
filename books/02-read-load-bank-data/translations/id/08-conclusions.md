Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 8. Peralatan Eksternal dan Batasan Fasilitas

Sebuah bank beban cair bukanlah sebuah pulau yang terisolasi, dan pengujian komisioning tidak berlangsung di dalam ruang hampa udara yang abstrak. Bank beban terhubung langsung ke infrastruktur fasilitas yang aktif: ke Unit Distribusi Pendingin (*Coolant Distribution Unit* - CDU), ke catu daya bebas gangguan (*uninterruptible power supply* - UPS) atau sakelar transfer otomatis (*automatic transfer switch* - ATS), dan ke pengondisi udara ruang komputer (*computer room air handler* - CRAH).

Moda kegagalan yang sering terjadi dalam pelaporan komisioning adalah kekacauan batasan (*confusion of boundaries*):
- Ketika pompa sirkulasi CDU fasilitas mengalami *trip* akibat gangguan inverter internal, tim yang belum berpengalaman mungkin menyalahkan bank beban karena "gagal mempertahankan aliran".
- Sebaliknya, ketika sakelar keselamatan suhu tinggi bank beban mengalami *trip* akibat elemen pemanas yang terendam secara buruk, pihak vendor mungkin mencoba menyalahkan CDU fasilitas karena "beroperasi terlalu hangat".

Laporan kilat (*flash report*) harus menarik garis batas fisik dan operasional yang tegas antara bank beban (mesin yang sedang diuji) dan peralatan fasilitas eksternal (lingkungan inang). Kegagalan peralatan fasilitas eksternal adalah peristiwa operasional; hal tersebut tidak serta merta menjadi kegagalan dari bank beban. Namun, hal itu harus didokumentasikan dengan presisi mutlak sehingga penyebab sebenarnya dari masa jeda yang terganggu dapat terlihat jelas dan transparan bagi auditor mana pun di masa depan.

## Empat Baris Peralatan Eksternal

Laporan kilat menyertakan bagian Peralatan Eksternal dengan empat baris eksplisit, yang dievaluasi sebelum, selama, dan setelah setiap larian pengujian:

### Baris 1: Unit Distribusi Pendingin (*Coolant Distribution Unit* - CDU)
CDU bertanggung jawab untuk mensirkulasikan cairan pendingin sekunder melalui bank beban dan mentransfer panas ke *loop* air dingin primer fasilitas melalui penukar panas internal tipe pelat terpatri (*brazed plate*) atau selongsong-dan-tabung (*shell-and-tube*).

Laporan kilat memantau empat metrik antarmuka CDU:
- **Suhu Pasokan Loop Sekunder (T_CDU,sup)**: Suhu fluida yang keluar dari penukar panas CDU sebelum memasuki manifold pasokan bank beban. Laporan memverifikasi bahwa CDU mempertahankan nilai setelan (*setpoint*) pasokannya yang dinyatakan (misalnya, 35,0°C ± 1,0 K). Jika air primer fasilitas menghangat, menyebabkan T_CDU,sup berhanyut ke atas hingga 42,0°C, hanyutan tersebut dicatat sebagai **ekskursi kondisi batas CDU**, bukan sebagai kesalahan pemanasan bank beban.
- **Tekanan Penyaluran Sekunder & Kurva Pompa**: Tekanan statis yang tersedia yang disalurkan oleh pompa CDU pada aliran kluster terukur nominal. Jika kecepatan pompa CDU berfluktuasi (*hunting*) atau mengalami kavitasi akibat tekanan hisap yang buruk, fluktuasi aliran yang dihasilkan akan dicatat pada baris CDU.
- **Suhu Pendekatan (*Approach Temperature*) CDU**: Selisih suhu antara fluida kembali sekunder dan air pasokan primer fasilitas (Pendekatan = T_sec,ret - T_pri,sup). Peningkatan suhu pendekatan seiring waktu mengindikasikan pengotoran (*fouling*) pada pelat penukar panas CDU, bukan degradasi elemen pada bank beban.

### Baris 2: Catu Daya Bebas Gangguan (UPS) & Sakelar Transfer Otomatis (ATS)
Daya listrik yang menyuplai bank beban berasal dari papan hubung distribusi fasilitas, sering kali didukung oleh modul UPS statis atau peralatan ATS generator diesel.

Laporan kilat memantau:
- **Stabilitas Tegangan & Distorsi Harmonik**: Penurunan tegangan (*voltage sag*) saluran selama pengaktifan beban penuh bertahap. Jika transformator fasilitas mengalami penurunan dari 415 V menjadi 380 V di bawah beban penuh 480 kW, daya aktif elemen resistif akan turun hampir 16% ($P \propto V²$). Laporan harus mendokumentasikan bahwa penurunan beban didorong oleh penurunan tegangan utilitas fasilitas, bukan oleh pelepasan kontaktor dini.
- **Imunitas Transfer ATS**: Jika pengujian sistem terintegrasi (IST) menginisiasi transfer daya di hulu, durasi gangguan transisi terbuka (*open-transition interruption*) harus diukur waktunya. Jika gangguan tersebut melampaui waktu penahanan *buffer* kendali 24 VDC bank beban (biasanya 40 ms), unit akan mati dengan aman, yang harus diatribusikan pada transien transfer fasilitas.

### Baris 3: Unit Distribusi Daya (PDU) dan Saluran Bus (*Busways*)
Jalur daya fisik dari papan panel listrik melalui kotak sadapan (*tap-off box*) saluran bus dan kabel penurunan (*drop cables*) ke terminal bank beban:
- **Kenaikan Suhu Terminal (ΔT_terminal)**: Pemantauan termografi inframerah atau termokopel terkalibrasi pada sepatu kabel dan terminal kontaktor. Suhu terminal tidak boleh melampaui 70°C (atau peringkat spesifik dari konduktor RHW-2 90°C).
- **Penurunan Tegangan Saluran Bus**: Penurunan tegangan di sepanjang kabel penyulang sementara harus dibatasi ≤ 2,0%.

### Baris 4: Pengondisi Udara Ruang Komputer (CRAH / CRAC / Fan Wall)
Unit penanganan udara fasilitas yang bertanggung jawab menyerap 16% hingga 20% kalor sensibel udara pendamping yang dibuang oleh *blower* bank beban:
- **Diferensial Udara Masuk/Keluar**: Memverifikasi bahwa penahanan lorong panas (*hot-aisle containment* - HAC) aula data mempertahankan tekanan negatif yang tepat relatif terhadap lorong dingin, mencegah resirkulasi termal ke barisan server yang berdekatan.
- **Respons Katup Air Dingin CRAH**: Mengonfirmasi bahwa koil pendingin CRAH membuka secara modulasi dengan mulus dalam merespons beban udara pendamping tanpa menyebabkan bak penampung kondensat meluap.

## Cara Menulis Kalimat Batas yang Jujur

Ketika terjadi anomali atau interupsi selama larian pengujian, Pencatat harus menulis kalimat batas yang jujur (*honest boundary sentence*).

Kalimat batas yang jujur mematuhi tiga aturan tata bahasa yang ketat:
1. **Menyebutkan parameter fisik pasti yang melanggar ambang batas.**
2. **Menyebutkan sisi batas spesifik tempat pelanggaran tersebut terjadi.**
3. **Menyatakan konsekuensi terhadap skenario pengujian tanpa memberikan tuduhan spekulatif.**

### Contoh Kalimat Batas yang Jujur
> *"Pada pukul 15:42:18 UTC, selama Langkah 4 (jeda 120 kW), suhu pasokan pendingin sekunder dari CDU fasilitas naik menjadi 39,8°C (melampaui batas prates yang disitasi sebesar 36,5°C). Bank beban mempertahankan beban listrik nominal (120,1 kW) dan aliran normal (176,4 LPM), tetapi suhu kembali mencapai 49,9°C, memicu alarm supervisi suhu tinggi otomatis. Masa jeda dihentikan pada Menit ke-11 atas perintah operator. Penilaian untuk Langkah 4: TIDAK VALID akibat ekskursi suhu pasokan CDU fasilitas; pelacakan listrik dan hidrolik bank beban tetap patuh sepenuhnya."*

### Contoh Kalimat yang Tidak Jujur
> *"Pengujian mengalami beberapa masalah dengan air gedung, tetapi bank beban pada dasarnya lulus."*

Kalimat yang tidak jujur tersebut menyediakan nol data, tidak mencitasi stempel waktu, tidak menyebutkan suhu, dan mencoba mengklaim kelulusan yang tidak sah. Seorang auditor akan langsung menolaknya. Kalimat yang jujur menyajikan angka yang presisi, mengidentifikasi ekskursi batas CDU, mencatat penghentian masa jeda, dan mempertahankan integritas teknis dari perangkat keras bank beban untuk pengujian ulang.

## Status Lulus/Gagal Peralatan Eksternal

Pada lembar ringkasan laporan kilat, masing-masing dari keempat baris peralatan eksternal diberi status independen:
- **NORMAL**: Beroperasi di dalam batas koridor desain yang disitasi selama keseluruhan larian.
- **EKSKURSI (*EXCURSION*)**: Melanggar batas koridor operasi, dengan stempel waktu dan parameter yang terpengaruh didokumentasikan secara tepat.
- **TIDAK BERLAKU (*NOT APPLICABLE* / N/A)**: Peralatan dikecualikan dari batas pengujian berdasarkan kesepakatan yang dinyatakan sebelumnya.

Ekskursi CDU fasilitas tidak merusak reputasi bank beban yang direkayasa dengan baik, dan bank beban yang bersih tidak dapat menjadi alasan untuk memaafkan pabrik fasilitas yang gagal. Laporan merekam keduanya secara terang benderang, terpisah oleh batas fisik manifold.

## Keputusan yang Harus Dicatat

Di bagian peralatan eksternal pada laporan kilat, catat:

- Nomor seri, model, dan versi *firmware* dari CDU fasilitas serta suhu air dingin *loop* primernya.
- Tegangan bus transformator / UPS di hulu dan keseimbangan fasa selama langkah beban maksimum.
- Suhu terminal sepatu kabel maksimum yang teramati selama masa jeda beban penuh.
- Status operasional unit CRAH fasilitas dan integritas penahanan lorong panas.
- Kalimat batas yang jujur yang menjelaskan setiap jeda pengujian atau penghentian masa jeda, yang ditandatangani oleh Operator dan Orang Asing.
