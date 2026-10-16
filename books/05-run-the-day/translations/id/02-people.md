Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 2. Orang-Orang dalam Sif

Pusat data tidak berjalan di atas telemetri perangkat lunak semata. Pusat data berjalan di atas kompetensi, lisensi resmi, dan disiplin fisik dari para teknisi yang memeriksa lantai instalasi. Jika Anda tidak mengetahui kualifikasi pasti dari orang-orang yang memegang kunci utama fasilitas, Anda tidak mengendalikan instalasi tersebut.

**MATRIKS KUALIFIKASI SIF & OTORISASI**

| Peran Sertifikasi y | ang Diperlukan Lingkup Otoris | asi |
| :--- | :--- | :--- |
| Duty Manager CDFOM | / Lisensi Operasi SLA Keselur | uhan & Izin |
| Teknisi Listrik Uta | ma Lisensi Tegangan Tinggi/Re | ndah Switchgear, Trafo |
| Spesialis Pendingin | Lisensi Tata Udara / Refrige | rasi Chiller, CDU, Glikol |
| Teknisi Sif Sertifi | kasi Fasilitas Data Ctr Putar | an, Telemetri, Log |
| Pengawal/Keselamata | n K3 / Pertolongan Pertama / | CPR Pengawasan Vendor, LOTO |

## Persyaratan Lisensi dan Regulasi

Di pusat data AI berdensitas tinggi yang menampung pendinginan cair skala megawatt dan gardu listrik multi-megavolt-ampere, teknisi fasilitas umum adalah liabilitas eksistensial. Tugas-tugas operasional memerlukan sertifikasi resmi:
- **Operasi Kelistrikan**: Setiap peralihan (switching), penarikan/pemasangan pemutus (racking), atau pengujian bertegangan pada switchgear tegangan menengah (10kV/35kV) atau tegangan rendah (400V/480V) harus dilakukan secara eksklusif oleh teknisi listrik bersertifikat yang memegang lisensi pemerintah yang sah.
- **Operasi Pendinginan & Kimia**: Mengoperasikan chiller sentrifugal, menara pendingin industri, dan stasiun pompa primer/sekunder memerlukan teknisi refrigerasi berlisensi yang tersertifikasi dalam penanganan refrigeran bertekanan dan pengolahan air industri.

Berdasarkan panduan operasional OpenViking (`ALZJ-YW-2.6XZ10`), operasi pendinginan cair yang melibatkan unit distribusi sekunder (CDU), sistem air fasilitas primer (FWS), dan manifold tingkat rak memerlukan pelatihan teknis terverifikasi mengenai biosida kimia, pengukuran konsentrasi glikol, dan protokol penanganan kebocoran.

Jika seorang teknisi pada sif tidak memiliki lisensi resmi untuk manuver tegangan tinggi, nama mereka tidak boleh tercantum pada tiket manuver listrik. Jika kontraktor tanpa lisensi ditemukan membuka pintu panel listrik, pekerjaan harus segera dihentikan seketika.

## Aturan Dua Orang (Two-Person Rule)

Tidak ada operasi manuver kritis, racking pemutus tegangan tinggi, atau isolasi katup pada loop pendingin primer yang boleh dilakukan oleh teknisi tunggal.

Aturan dua orang mewajibkan:
1. **Pelaksana (The Performer)**: Teknisi bersertifikat yang memegang Prosedur Pelaksanaan (MOP) yang disetujui, yang menyentuh sakelar kendali, handel pemutus sirkuit, atau katup isolasi secara fisik.
2. **Pemeriksa (The Checker)**: Teknisi dengan kualifikasi setara yang berdiri tepat di belakang pelaksana, memegang dokumen prosedur fisik, membacakan setiap langkah dengan lantang, memverifikasi label peralatan (misalnya memastikan label pemutus `SWG-01-4A` cocok dengan tiket sebelum racking), dan mempertahankan kewaspadaan penghentian darurat.

Tugas tunggal pemeriksa selama operasi adalah verifikasi dan keselamatan. Jika pelaksana mulai meraih handel pemutus yang salah atau memutar katup dalam urutan yang keliru, pemeriksa memiliki wewenang mutlak untuk menghentikan operasi secara instan.

| **ATURAN DUA ORANG** |
| :--- |
| PEMERIKSA \| \| PELAKSANA |
| Pegang lembar MOP \| \| Sentuh sakelar |
| Baca langkah keras\| -----→ \| Tunjuk label ID |
| Verifikasi tag ID \| \| Eksekusi aksi |
| Punya Kuasa Stop \| \| Laporkan status |

## Otoritas Penghentian Pekerjaan (Stop Work Authority: SWA)

Setiap individu yang memasuki fasilitas—mulai dari direktur operasi senior hingga pekerja penarik kabel magang—memiliki Otoritas Penghentian Pekerjaan (SWA) penuh dan tanpa syarat.

Stop Work Authority wajib dipicu apabila:
- Kondisi fisik di lapangan menyimpang dari asumsi yang tertulis di dalam MOP.
- Alarm tak terduga berbunyi pada Building Management System (BMS) atau Electrical Power Monitoring System (EPMS).
- Tetesan air, genangan cairan, atau bau kimiawi abnormal terdeteksi di dekat peralatan listrik.
- Barikade keselamatan yang diwajibkan, alat pelindung diri (APD), atau gembok Lockout/Tagout (LOTO) hilang atau terganggu.
- Operator mengalami keraguan atau ketidakpastian mengenai langkah prosedural berikutnya.

Ketika Stop Work diaktifkan:
1. Peralatan segera ditempatkan pada kondisi aman terdekat yang ditentukan dalam prosedur.
2. Alat kerja diletakkan; tidak ada lagi katup atau sakelar yang digerakkan.
3. Manajer tugas (duty manager) dipanggil ke lokasi kerja.
4. Pekerjaan hanya dilanjutkan setelah ketidakjelasan diselesaikan dan didokumentasikan secara tertulis pada izin kerja.

Tidak ada teknisi atau kontraktor yang boleh ditegur, dihukum, atau diinterogasi karena menggunakan Stop Work dengan itikad baik. Budaya fasilitas di mana teknisi ragu menyerukan Stop Work karena tekanan jadwal adalah fasilitas yang sedang menunggu pemadaman listrik multi-megawatt.

## Pemeriksaan Fisik Bersama 30 Menit

Jangan pernah melakukan serah terima sif sambil duduk di belakang meja ruang kendali. Serah terima yang diselesaikan sambil minum kopi adalah pelepasan tanggung jawab.

Manajer tugas yang masuk dan manajer tugas yang akan keluar wajib menyelesaikan pemeriksaan fisik bersama selama 30 menit di enam zona fasilitas kritis sebelum menandatangani Lembar Hari:
1. **Gardu Tegangan Menengah**: Periksa switchgear 35kV/10kV, indikator pengisian pegas pemutus, pengukur tekanan gas SF6, dan status pengisi daya baterai DC.
2. **Ruang Transformator**: Periksa suhu belitan transformator tipe kering/minyak (pastikan T < 90°C), pengoperasian kipas pendingin, dan dengarkan apakah ada dengung harmonik akustik abnormal.
3. **Ruang UPS & Baterai**: Verifikasi tegangan apung (float) bus DC, suhu deret baterai individu (T < 25°C), periksa korosi terminal atau pembengkakan wadah baterai, dan pastikan aliran udara kipas pembuangan hidrogen.
4. **Instalasi Chiller Sentral & Pompa**: Periksa suhu pendekatan (approach temperature) kondenser chiller (ΔT_approach ≤ 1.5 K), tekanan kepala kondenser, frekuensi variable frequency drive (VFD), dan getaran akustik.
5. **Stasiun Cairan CDU**: Verifikasi tekanan primer/sekunder (0.15 - 0.90 MPa), tekanan diferensial pompa (ΔP < 1.0 bar), level cairan tangki ekspansi, dan periksa baki penampung dari kelembapan.
6. **Ruang AI Whitespace**: Telusuri lorong panas dan dingin, periksa unit distribusi daya (PDU) untuk titik panas termal, verifikasi tekanan diferensial ubin lantai (ΔP ≥ 5 Pa), dan periksa kopling cepat (FD83/UQD) dari tanda rembesan.

Kedua manajer harus menelusuri seluruh rute bersama-sama berdampingan. Jika manajer yang akan keluar menolak untuk memeriksa lantai fasilitas, manajer yang baru masuk menganggap semua peralatan berada dalam status tidak terverifikasi dan mencatat penolakan tersebut di log serah terima.

## Keputusan yang Harus Dicatat

- Nama seluruh personel sif, nomor lisensi terverifikasi, dan tanggal kedaluwarsanya.
- Konfirmasi bahwa operasi listrik tegangan tinggi dan fluida kritis mematuhi aturan dua orang.
- Setiap penggunaan Stop Work Authority selama sif, merinci penyebab dan penyelesaiannya.
- Berita acara pemeriksaan fisik bersama 30 menit yang ditandatangani oleh manajer masuk dan keluar.

## Batas Demarkasi Fisik dan Protokol Audit Sif Kuantitatif

Manajer operasional sif wajib menjaga titik demarkasi fisik (`DEMARC`) di seluruh empat cincin fasilitas (Ring 1: Utilitas & Perimeter, Ring 2: Ruang Mekanikal/Elektrikal Utama, Ring 3: Distribusi Whitespace & CDU Sekunder, Ring 4: Interior Rak Penyewa) dan mencatat matriks tolok ukur kuantitatif berikut pada Lembar Hari (Day Sheet):

| Area Audit Sif | Parameter Pemantauan & Metrologi | Amplop Operasi Normal | Ambang Intervensi / Hentikan Pekerjaan (Stop Work) |
| :--- | :--- | :--- | :--- |
| **Batas Beban Redundansi Listrik 2N** | Utilisasi tunak Bus A / Bus B ($P_{\text{bus}} / P_{\text{rated}}$) | $\le 45.0\%$ (Saat gagal 1 jalur $\le 90.0\%$) | Tolak segera penambahan beban rak jika utilisasi $> 45.0\%$ |
| **Hidraulik & Kimiawi CDU Sekunder** | Tekanan pasokan $P_{\text{sup}}$, pendekatan $\Delta T_{\text{PHE}}$, kadar PG | $0.15\sim 0.90\,\text{MPa}$, $\Delta T_{\text{PHE}} \le 8.0\,\text{K}$, PG $25.0\% \pm 1.0\%$ | $\Delta P > 1.0\,\text{bar}$, konduktivitas $> 10\,\mu\text{S/cm}$, atau tetesan kopling |
| **Izin Kerja (PTW) & Energi-Nol LOTO** | Kunci LOTO, pelepasan muatan kapasitor, katup pintas | 100% didampingi host situs; tutup sebelum kedaluwarsa | Penyimpangan dari MOP tertulis atau pekerjaan tambahan spontan |
| **Jam Insiden & Notifikasi SLA** | Deteksi ($T_0$), kondisi aman EOP, pemberitahuan klien | P1: Kirim fakta terverifikasi dalam $\le 15\,\text{menit}$ | Dilarang mencantumkan hipotesis/spekulasi pada notifikasi |

$$\text{FTE}_{\text{per\_post}} = \frac{365\,\text{days} \times 24\,\text{h/day}}{\left( 52\,\text{weeks} \times 40\,\text{h/week} \right) - H_{\text{leave}} - H_{\text{training}} - H_{\text{sick}}} = \frac{8,760\,\text{h}}{2,080 - 160 - 80 - 64} \approx 4.93\,\text{FTE}$$
