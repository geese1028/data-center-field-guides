Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 8. Saat Terjadi Kegagalan

Insiden adalah setiap peristiwa di mana infrastruktur kritis gagal menyalurkan batas layanan kontraktual, di mana nyawa manusia terancam, atau di mana fasilitas memasuki kondisi tidak stabil yang akan segera menyebabkan salah satu dari kedua hasil tersebut.

| **LINIMASA ESKALASI INSIDEN** |
| :--- |
| [T = 00:00] PENEMUAN PERISTIWA (Trip telemetri, alarm akustik, visual) |
| ↓ |
| [T + 02:00] BERHENTI & NILAI: Matikan klakson; identifikasi subsistem |
| ↓ |
| [T + 05:00] EKSEKUSI EOP: Stabilkan status aman terdekat; isolasi bahaya |
| ↓ |
| [T + 10:00] PANGGIL KOMANDO INSIDEN: Buka log insiden; tetapkan peran |
| ↓ |
| [T + 15:00] PEMBERITAHUAN SLA KLIEN: Kirim fakta (TANPA HIPOTESIS) |
| ↓ |
| [T + 60:00] PENGENDALIAN TEKNIS: Terapkan perbaikan MOP; pembaruan berkala |
| ↓ |
| [PASCA-ACARA] ANALISIS AKAR PENYEBAB (RCA): 5-Whys, 1 tindakan bertuan |

![Incident Escalation and SLA Timeline](../figures/fig-06-incident-escalation-and-sla-timeline.png)

Alarm bising yang tidak mengancam penyampaian layanan atau keselamatan manusia hanyalah gangguan. Jangan mengangkatnya menjadi keadaan darurat. Sebaliknya, jangan pernah menurunkan tingkat degradasi layanan nyata hanya karena ruang peralatan tampak tenang dan hening. Satu-satunya ukuran insiden adalah penyampaian layanan dan keselamatan personel.

## Klasifikasi Tingkat Keparahan Insiden

Setiap peristiwa abnormal harus diklasifikasikan ke dalam salah satu dari tiga tingkat keparahan yang ketat dalam waktu dua menit sejak penemuan:

**KLASIFIKASI KEPARAHAN INSIDEN**

| Tingkat | Klasifikasi | Dampak Operasional Pemberitahu | an Klien |
| :--- | :--- | :--- | :--- |
| P1 Krit | is Kehilangan | total daya/pendingin <= 15 Mn | t; Per Jam |
| pada be | ban TI; kesel | amatan jiwa |  |
| P2 Mayo | r Kehilangan | redundansi sistem <= 30 Mnt; T | iap 2 Jam |
| (status | N-1); pering | atan suhu |  |
| P3 Mino | r Kegagalan k | omponen tunggal Log Ringkasan | Sif |
| tanpa d | ampak redunda | nsi |  |

## Satu Jam Pertama: Jam Insiden

Selama insiden langsung berlangsung, ingatan manusia menurun dengan cepat di bawah pengaruh adrenalin. Teknisi mengingat tindakan di luar urutan; manajer memampatkan dua puluh menit keraguan menjadi lima menit ketegasan yang diingat.

Duty manager wajib membuka **Log Kronologi Insiden** yang tidak dapat diubah dan bertanda waktu pada menit yang tepat saat peristiwa dimulai:

| **LOG KRONOLOGI INSIDEN** |
| :--- |
| [09:14:22] EPMS lapor Pemutus B-SWG-02 trip seketika pada penyulang B |
| [09:16:00] Duty Manager memulai EOP-E-04 (Kehilangan Penyulang 2N B) |
| [09:18:45] Teknisi Chen konfirmasi Bus A pikul 82% beban total |
| [09:21:10] Kondisi Aman 1 tercapai: Beban TI stabil pada satu sumber |
| [09:24:00] Pemberitahuan SLA Klien 1 dikirim via portal (T+10 menit) |
| [09:32:00] Pemindaian IR switchgear Bus A tunjukkan 58°C; stabil |
| [09:45:00] Vendor switchgear dihubungi; tiket #84920 dibuka |

Catat setiap peristiwa dengan cap waktu yang tepat:
- Menit saat alarm terdeteksi di konsol pemantauan.
- Apa yang diamati secara tepat pada instrumen fisik, bukan apa yang diasumsikan seseorang telah terjadi.
- EOP persis yang dieksekusi, kondisi aman yang dicapai, dan menit saat kondisi tersebut dikonfirmasi.
- Nama semua individu yang dipanggil ke dalam tim insiden.
- Menit saat pemberitahuan klien dikirimkan, dan teks persis yang dikirim.
- Tindakan apa yang sengaja ditolak atau ditunda untuk melindungi sistem yang masih beroperasi normal.

## Kondisi Aman Refleks Otot vs. Pemecahan Masalah Heroik

Ketika alarm berbunyi dan peralatan trip, reaksi naluriah teknisi yang tidak terlatih adalah mulai membalik sakelar, mereset pemutus sirkuit yang trip, atau membuka katup bypass dalam upaya putus asa untuk memulihkan unit yang mati.

"Pemecahan masalah heroik" ini adalah cara bagaimana trip komponen tunggal minor meningkat menjadi pemadaman total seluruh fasilitas yang katastrofik:
- Pemutus sirkuit yang trip karena arus lebih seketika mungkin telah membersihkan hubung singkat mati antarfase yang katastrofik. Mereset pemutus tersebut tanpa pengujian akan menyebabkan ledakan arc-flash yang menghancurkan seluruh deretan switchgear.
- Pompa CDU sekunder yang trip karena tekanan hisap rendah mungkin mengindikasikan tangki ekspansi kosong atau pipa pecah. Memaksa pompa siaga untuk mulai tanpa penyelidikan akan membuat mechanical seal bekerja kering dan membakar motor.

Aturan operasional mutlak selama insiden adalah:
1. **Eksekusi Prosedur Operasi Darurat (EOP)** untuk menetapkan Kondisi Aman (Safe State) terdekat yang telah dirancang sebelumnya.
2. **Berhenti (Stop)**. Lepaskan tangan Anda dari alat kendali.
3. Verifikasi bahwa sistem redundan yang bertahan memikul beban dengan stabil.
4. Mulai penyelidikan forensik sistematis di bawah MOP yang disetujui.

Pahlawan yang mencoba memperbaiki peralatan bertegangan saat sirene meraung-raung adalah milik film laga, bukan pusat data industri. Di pusat data industri, kita menghargai teknisi berdisiplin yang menstabilkan fasilitas, berdiri mundur, dan mematuhi prosedur.

## Menjauhkan Hipotesis dari Pemberitahuan Klien Pertama

Saat menyusun draf pemberitahuan insiden awal kepada pelanggan, patuhi aturan kaku ini: **Laporkan hanya fakta fisik yang telah dikonfirmasi; jauhkan hipotesis sama sekali dari pemberitahuan.**

| **DISIPLIN PEMBERITAHUAN KLIEN** |
| :--- |
| [PEMBERITAHUAN FAKTUAL YANG DIIZINKAN] |
| "Pada pukul 09:14 UTC, Penyulang Listrik B mengalami trip otomatis. |
| Semua ruang TI kritis tetap berdaya penuh melalui Penyulang A |
| yang redundan. Fasilitas saat ini beroperasi dalam status N-1. |
| Tim operasi sedang menyelidiki penyebab trip Penyulang B. |
| Pembaruan resmi berikutnya akan diberikan pada pukul 10:15 UTC." |
| [PEMBERITAHUAN SPEKULATIF YANG DILARANG] |
| "Kami menduga kontraktor menyenggol relai pada Penyulang B, atau |
| mungkin ada sambaran petir pada jaringan listrik PLN di dekat sini. |
| Kami sedang mereset pemutus sekarang dan berharap normal 10 menit lagi" |

Jika Anda mengirimkan teori spekulatif dalam pemberitahuan pertama Anda dan analisis forensik rekayasa selanjutnya membuktikan bahwa teori tersebut salah:
- Anda menghancurkan kepercayaan pelanggan terhadap kompetensi operasional Anda.
- Anda memberi tim hukum pelanggan amunisi untuk mengklaim kelalaian berat.
- Anda memaksa tim Anda menghabiskan waktu berjam-jam untuk menjelaskan mengapa cerita awal berubah, alih-alih berfokus pada pemulihan teknis.

Sampaikan gejalanya, cap waktunya, sistem yang terpengaruh, status pembendungan saat ini, dan waktu pembaruan berikutnya. Jangan katakan hal lain.

## Tindakan Korektif Bertuan Tunggal (RCA Pasca-Insiden)

Insiden belum ditutup ketika peralatan diberi tegangan kembali dan alarm mereda. Insiden hanya ditutup ketika Analisis Akar Penyebab (RCA) formal dilakukan dan menghasilkan **satu tindakan operasional konkret, memiliki pemilik nama tunggal, dan bertanggal tenggat**.

Rapat peninjauan pasca-insiden di mana para manajer berkumpul untuk saling berkeluh kesah, menceritakan kembali kecemasan mereka, dan menyimpulkan bahwa *"teknisi harus lebih berhati-hati"* adalah pemborosan waktu total. "Lebih berhati-hati" bukanlah kendali rekayasa.

Tindakan korektif pasca-insiden yang autentik mengubah:
- Desain rekayasa (misalnya memasang relai isolasi interposing untuk menghilangkan sirkuit trip mode umum).
- Prosedur pemeliharaan (misalnya merevisi MOP untuk mewajibkan pemeriksaan torsi ganda pada lug kabel 480V).
- Putaran inspeksi (misalnya menambahkan pengambilan sampel refraktometer harian ke daftar periksa sif CDU).
- Alat fisik atau suku cadang (misalnya pengadaan skid pengisian vakum terkalibrasi untuk menghilangkan perangkap udara dalam loop pendingin).

Tindakan korektif harus memiliki pemilik nama tunggal dan tenggat penyelesaian yang mengikat. Jika peninjauan pasca-insiden mengusulkan lima rekomendasi yang samar, tidak ada satu pun yang akan diterapkan. Pilih satu perbaikan struktural yang paling berdampak, tetapkan pemiliknya, dan lacak penyelesaiannya pada log serah terima harian.

## Keputusan yang Harus Dicatat

- Klasifikasi insiden (P1 / P2 / P3) dan cap waktu penemuan yang tepat.
- Log kronologi yang merinci semua tindakan, status aman yang dicapai, dan personel yang terlibat.
- Salinan pemberitahuan klien awal, memverifikasi nol hipotesis spekulatif yang disertakan.
- Konfirmasi pemulihan teknis yang ditandatangani di bawah kondisi beban tunak.
- Satu tindakan korektif bertuan dan bertanggal yang dihasilkan dari Analisis Akar Penyebab.

## Batas Demarkasi Fisik dan Protokol Audit Sif Kuantitatif

Manajer operasional sif wajib menjaga titik demarkasi fisik (`DEMARC`) di seluruh empat cincin fasilitas (Ring 1: Utilitas & Perimeter, Ring 2: Ruang Mekanikal/Elektrikal Utama, Ring 3: Distribusi Whitespace & CDU Sekunder, Ring 4: Interior Rak Penyewa) dan mencatat matriks tolok ukur kuantitatif berikut pada Lembar Hari (Day Sheet):

| Area Audit Sif | Parameter Pemantauan & Metrologi | Amplop Operasi Normal | Ambang Intervensi / Hentikan Pekerjaan (Stop Work) |
| :--- | :--- | :--- | :--- |
| **Batas Beban Redundansi Listrik 2N** | Utilisasi tunak Bus A / Bus B ($P_{\text{bus}} / P_{\text{rated}}$) | $\le 45.0\%$ (Saat gagal 1 jalur $\le 90.0\%$) | Tolak segera penambahan beban rak jika utilisasi $> 45.0\%$ |
| **Hidraulik & Kimiawi CDU Sekunder** | Tekanan pasokan $P_{\text{sup}}$, pendekatan $\Delta T_{\text{PHE}}$, kadar PG | $0.15\sim 0.90\,\text{MPa}$, $\Delta T_{\text{PHE}} \le 8.0\,\text{K}$, PG $25.0\% \pm 1.0\%$ | $\Delta P > 1.0\,\text{bar}$, konduktivitas $> 10\,\mu\text{S/cm}$, atau tetesan kopling |
| **Izin Kerja (PTW) & Energi-Nol LOTO** | Kunci LOTO, pelepasan muatan kapasitor, katup pintas | 100% didampingi host situs; tutup sebelum kedaluwarsa | Penyimpangan dari MOP tertulis atau pekerjaan tambahan spontan |
| **Jam Insiden & Notifikasi SLA** | Deteksi ($T_0$), kondisi aman EOP, pemberitahuan klien | P1: Kirim fakta terverifikasi dalam $\le 15\,\text{menit}$ | Dilarang mencantumkan hipotesis/spekulasi pada notifikasi |
