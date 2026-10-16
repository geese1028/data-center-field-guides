Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 0. Cara Menggunakan Buku Ini

Buku ini ditujukan bagi orang yang mengelola hari di pusat data. Ini adalah tentang sif kerja, pekerjaan yang diizinkan terjadi, hal yang mengalami kegagalan, dan kalimat yang masih dapat Anda pertanggungjawabkan secara sah di penghujung hari.

Ini bukan kursus operasi fasilitas pusat data. Buku ini bukan pengganti untuk mengikuti kursus tersebut. Certified Data Centre Facilities Operations Manager (CDFOM) dan Certified Data Centre Facilities Operations Specialist (CDCS) adalah nama-nama program sertifikasi. Buku ini tidak mengulang slide presentasi, latihan pilihan ganda, atau ujian mereka. Jika Anda memerlukan kredensial tersebut untuk matriks kualifikasi vendor klien Anda, ikutilah kursus resmi dari organisasi pemiliknya.

Ini juga bukan salinan dari pustaka manajemen layanan, standar keamanan, standar desain, atau kode keselamatan kerja. ITIL, ISO/IEC 20000, ISO 22301, ISO 55001, NFPA 70E, dan OSHA 1910 memiliki judul dan edisi resminya masing-masing. Rujuklah dokumen-dokumen itu. Jangan menjiplaknya mentah-mentah. Seorang manajer yang menempelkan enam puluh halaman teks formalitas korporat ke dalam map sif belum mengoperasikan fasilitas; mereka hanya membangun dinding kertas untuk bersembunyi saat chiller trip.

Buku-buku sebelumnya dalam seri panduan lapangan ini berhenti pada mesin, berkas, pengujian, atau model:
- Buku 01 merakit bank beban cair dan memasang instrumentasi pada manifold.
- Buku 02 membaca laporan kilas termal dan hidrolik.
- Buku 03 mengeksekusi tujuh lembar verifikasi komisioning.
- Buku 04 mengaudit model dinamika fluida komputasi (CFD) terhadap pengukuran fisik.

Buku ini dimulai ketika para agen komisioning telah mengemas koper pelican mereka, bank beban sementara telah dinaikkan ke truk bak datar, server TI telah beroperasi aktif di bawah beban nyata, dan seseorang akan disalahkan jika ruang data mendadak gelap gulita.

| **SIKLUS HIDUP SIF PUSAT DATA** |
| :--- |
| [07:00] Pemeriksaan Fisik Bersama Sif Masuk & Keluar (30 mnt, 6 stasiun) |
| ↓ |
| [07:30] Gerbang Serah Terima Sif (Tanda Tangan Lembar Hari: Cacat, PTW, MOP) |
| ↓ |
| [08:00] Telemetri Dasar Pagi & Inspeksi Baki Penampung / Kebocoran |
| ↓ |
| [10:00] Jendela Pemeliharaan Resmi (Eksekusi MOP, LOTO, Pengawalan Aktif) |
| ↓ |
| [14:00] Putaran Mendalam Siang (Akustik, Termal IR, Refraktometer, Delta-P) |
| ↓ |
| [18:30] Audit Pra-Tutup: Penyelesaian Izin, Verifikasi Konfigurasi Normal |
| ↓ |
| [19:00] Kalimat Penutup: Pernyataan tunggal yang mengikat secara operasional |

![Shift Lifecycle and Handover Architecture](../figures/fig-01-shift-lifecycle-and-handover.png)

Ketika Anda menyelesaikan setiap hari kerja, Anda harus mampu menyerahkan satu lembar hari (day sheet). Lembar ini mencantumkan siapa yang bertugas pada sif tersebut, pekerjaan apa yang diizinkan, apa yang berubah, apa yang telah Anda periksa secara fisik, apa yang gagal, dan apa yang tidak akan Anda janjikan. Formatnya ada di Bab 10 dan di `sheets/day.md`. Jika Anda adalah manajer yang baru masuk besok pagi, mulailah dari sana.

## Apa yang Boleh Anda Salin

Anda boleh menyalin judul-judul kolom lembar kerja ini ke dalam buku log operasi atau perangkat lunak manajemen fasilitas Anda sendiri. Anda tidak boleh menempelkan kalimat dari buku ini ke dalam Perjanjian Tingkat Layanan (SLA) pelanggan dan menyebutnya sebagai aturan operasional mereka. Fasilitas mereka memiliki izin operasi sendiri, batas waktu pemberitahuan kontraktual sendiri, dan jalur eskalasi darurat sendiri. Buku ini memberi tahu Anda apa yang harus ditegakkan oleh dokumen-dokumen tersebut. Buku ini tidak menggantikannya.

## Keputusan yang Harus Dicatat

- Kalimat mengikat tunggal yang diizinkan untuk didukung oleh hari tersebut.
- Standar, kode keselamatan, atau kontrak yang akan Anda kutip berdasarkan judul dan edisi, bukan disalin-tempel.
- Lembar hari yang akan Anda tandatangani secara fisik sebelum Anda menyerahkan radio komunikasi ke sif berikutnya.

## Batas Demarkasi Fisik dan Protokol Audit Sif Kuantitatif

Manajer operasional sif wajib menjaga titik demarkasi fisik (`DEMARC`) di seluruh empat cincin fasilitas (Ring 1: Utilitas & Perimeter, Ring 2: Ruang Mekanikal/Elektrikal Utama, Ring 3: Distribusi Whitespace & CDU Sekunder, Ring 4: Interior Rak Penyewa) dan mencatat matriks tolok ukur kuantitatif berikut pada Lembar Hari (Day Sheet):

| Area Audit Sif | Parameter Pemantauan & Metrologi | Amplop Operasi Normal | Ambang Intervensi / Hentikan Pekerjaan (Stop Work) |
| :--- | :--- | :--- | :--- |
| **Batas Beban Redundansi Listrik 2N** | Utilisasi tunak Bus A / Bus B ($P_{\text{bus}} / P_{\text{rated}}$) | $\le 45.0\%$ (Saat gagal 1 jalur $\le 90.0\%$) | Tolak segera penambahan beban rak jika utilisasi $> 45.0\%$ |
| **Hidraulik & Kimiawi CDU Sekunder** | Tekanan pasokan $P_{\text{sup}}$, pendekatan $\Delta T_{\text{PHE}}$, kadar PG | $0.15\sim 0.90\,\text{MPa}$, $\Delta T_{\text{PHE}} \le 8.0\,\text{K}$, PG $25.0\% \pm 1.0\%$ | $\Delta P > 1.0\,\text{bar}$, konduktivitas $> 10\,\mu\text{S/cm}$, atau tetesan kopling |
| **Izin Kerja (PTW) & Energi-Nol LOTO** | Kunci LOTO, pelepasan muatan kapasitor, katup pintas | 100% didampingi host situs; tutup sebelum kedaluwarsa | Penyimpangan dari MOP tertulis atau pekerjaan tambahan spontan |
| **Jam Insiden & Notifikasi SLA** | Deteksi ($T_0$), kondisi aman EOP, pemberitahuan klien | P1: Kirim fakta terverifikasi dalam $\le 15\,\text{menit}$ | Dilarang mencantumkan hipotesis/spekulasi pada notifikasi |

$$\text{3. Change Window Safety}: \quad t_{\text{cutoff}} = T_{\text{window\_end}} - \left( t_{\text{rollback}} + t_{\text{verification}} \right)$$

$$\text{4. Staffing Coverage}: \quad N_{\text{licensed\_techs}}(t) \ge 2 \quad \forall t \in [t_{\text{shift\_start}}, \, t_{\text{shift\_end}}]$$
