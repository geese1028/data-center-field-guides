Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 6. Putaran Inspeksi Sif

Dasbor telemetri bisa berbohong. Transduser tekanan Building Management System (BMS) dapat mengalami pergeseran kalibrasi; detektor asap optik dapat menumpuk debu dan tetap melaporkan kondisi bersih; sensor suhu RTD dapat rusak pada nilai tinggi dan tertahan oleh filter perangkat lunak yang salah.

Putaran inspeksi fisik sif adalah verifikasi mutlak bahwa realitas fisik pusat data sesuai dengan model matematis di ruang kendali.

| **TOPOLOGI INSPEKSI FISIK PUTARAN SIF** |
| :--- |
| [STASIUN 1] Gardu & Switchgear MV (35kV/10kV Gas SF6, Pegas, Relai) |
| ↓ |
| [STASIUN 2] Ruang Transformator (Suhu Belitan, Dengung Akustik, Lug Kabel) |
| ↓ |
| [STASIUN 3] Ruang UPS & Baterai (Tegangan Float DC, Suhu Deret, Buang Udara) |
| ↓ |
| [STASIUN 4] Instalasi Chiller Sentral (Suhu Pendekatan, Tekanan Minyak) |
| ↓ |
| [STASIUN 5] Stasiun CDU Cairan (0.15-0.90 MPa, Refraktometer, Baki Kering) |
| ↓ |
| [STASIUN 6] Whitespace AI & Rak NVL72 (Termal IR, Delta-P, Kopling FD83) |

![Shift Round Inspection Topology](../figures/fig-03-shift-round-inspection-topology.png)

Teknisi yang menjalankan putaran inspeksi bukanlah pesuruh yang sekadar mencentang kotak pada papan klip. Teknisi dalam putaran inspeksi adalah instrumen diagnostik multi-sensorik aktif.

## Disiplin Inspeksi Multi-Sensorik

Setiap meter persegi pusat data produksi harus diaudit melalui empat saluran sensorik:
1. **Visual**: Periksa peralatan dari tetesan cairan, noda, perubahan warna, karat, pengencang yang kendor, kapasitor yang menggembung, cat melepuh yang mengindikasikan panas ekstrem, dan verifikasi jarum pengukur analog mekanis terhadap pembacaan telemetri digital.
2. **Akustik**: Dengarkan kavitasi pada rumah pompa (terdengar seperti memompa kerikil), dengung harmonik pada transformator yang mengindikasikan laminasi kendor atau saturasi inti, derit bantalan pada motor kipas, dan siulan kebocoran udara di sekitar pintu pembendungan lorong.
3. **Termal**: Gunakan kamera inframerah (IR) genggam yang terkalibrasi untuk memindai sambungan busbar listrik, terminal pemutus sirkuit, lug kabel, dan bantalan mekanis. Setiap sambungan yang menunjukkan suhu > 70°C atau perbedaan antarfase ΔT > 10 K merupakan cacat Kategori 1 seketika.
4. **Olfaktori**: Cium aroma tajam dari isolasi listrik yang terbakar (ozon dan resin fenolik yang terlalu panas), aroma manis propilen glikol yang menguap dari kebocoran mikro, atau bau belerang dari baterai timbal-asam yang melepaskan gas.

## Enam Stasiun Inspeksi Kritis

Mengikuti standar operasional yang diuraikan dalam OpenViking (`ALZJ-YW-2.6XZ02` untuk IT Whitespace dan `ALZJ-YW-2.6XZ10` untuk Infrastruktur Pendinginan Cair), putaran inspeksi sif melintasi enam stasiun wajib:

**METRIK INSPEKSI STASIUN KRITIS**

| Stasiun / Sistem Paramet | er Standar Ambang Batas P | enolakan |
| :--- | :--- | :--- |
| Switchgear Tegangan Men. | Tekanan Gas SF6 Nominal | Alarm Tekanan Rendah |
| Transformator Suhu Belit | an < 90°C Suhu >= 110°C ( | Alarm) |
| Ruang Baterai UPS Suhu A | mbien 20°C - 25°C Suhu > | 28°C / Baterai Melembung |
| Instalasi Chiller Pendek | atan Kondenser <1.5K Pend | ekatan >= 2.5 K |
| Loop Sekunder CDU Tekana | n 0.15 - 0.90 MPa Tekanan | < 0.12 MPa |
| Campuran Glikol CDU 25.0 | % PG (+/- 1.0%) PG < 23% | atau > 27% |
| Lorong Whitespace TI Del | ta-P Bawah Lantai >=5Pa D | elta-P < 2.5 Pa (Kurang Udara) |
| Rak Cairan (NVL72) Kopli | ng FD83/UQD Kering Ada Te | tesan Cairan Aktif |

![CDU Shift Inspection Checklist](../figures/fig-05-liquid-cdu-shift-inspection-checklist.png)

### Stasiun 1: Gardu Induk & Switchgear Tegangan Menengah
- Periksa indikator pengisian pegas pemutus sirkuit 35kV dan 10kV (verifikasi status terisi).
- Periksa indikator tekanan gas SF6 pada gas-insulated switchgear (GIS); pastikan jarum berada di zona hijau.
- Verifikasi tegangan pengisi daya baterai bus kontrol DC (125 VDC ± 2%) dan pastikan nol alarm gangguan tanah pada sistem kontrol DC tanpa arde.

### Stasiun 2: Ruang Transformator
- Verifikasi indikator suhu belitan digital pada transformator tipe kering (kisaran operasi normal: 60°C - 85°C; ambang batas alarm pada 110°C; trip otomatis pada 130°C).
- Periksa kipas pendingin udara paksa dari halangan fisik dan getaran bantalan.
- Periksa transformator berisi minyak untuk level minyak tangki, warna desikan silika gel (biru tua; merah muda menunjukkan saturasi kelembapan yang memerlukan penggantian segera), dan periksa sambungan tangki dari rembesan minyak.

### Stasiun 3: Ruang UPS & Baterai
- Catat tegangan float bus DC dan arus pengisian baterai di semua modul UPS statis.
- Audit suhu ambien ruang baterai (pertahankan ketat antara 20°C dan 25°C; umur desain baterai timbal-asam menurun 50% untuk setiap kenaikan 8 K di atas 25°C).
- Periksa secara visual wadah baterai VRLA individual dari pembengkakan, korosi terminal, atau kebocoran elektrolit; untuk sistem ion litium, verifikasi bahwa Battery Management System (BMS) melaporkan nol ketidakseimbangan tegangan sel (> 50 mV).
- Konfirmasikan pengoperasian kipas pembuangan hidrogen dengan merasakan aliran udara pada louver intake.

### Stasiun 4: Instalasi Chiller Sentral & Pompa
- Audit log operasi chiller: verifikasi bahwa suhu pendekatan air kondenser adalah ≤ 1.5 K (ΔT_approach = T_cond, leaving - T_tower, entering). Suhu pendekatan > 2.5 K menunjukkan pengotoran atau kerak pipa yang parah yang memerlukan penyikatan kimiawi.
- Periksa level oli kompresor, tekanan oli, dan suhu kembali oli.
- Audit tekanan diferensial pompa air dingin (ΔP) dan verifikasi bahwa penggerak kecepatan variabel (VFD) sekunder memodulasi dengan benar tanpa fluktuasi berlebih (hunting).

### Stasiun 5: Unit Distribusi Pendingin Sekunder (CDU)
Berdasarkan OpenViking `ALZJ-YW-2.6XZ10`, CDU adalah jantung mekanis kluster AI berdensitas tinggi:
- **Rentang Tekanan**: Verifikasi tekanan pasokan sistem air fasilitas primer (FWS) dan tekanan pasokan sistem pendingin teknologi sekunder (TCS) tetap berada di antara 0.15 MPa dan 0.90 MPa. Verifikasi bahwa tekanan diferensial pompa adalah < 1.0 bar.
- **Kinerja Termal**: Verifikasi bahwa suhu pendekatan penukar panas pelat (ΔT_approach = T_TCS, supply - T_FWS, supply) tidak melebihi 8.0 K. Pendekatan > 8.0 K menunjukkan pengotoran biologis atau penyumbatan partikel pada permukaan pelat.
- **Kimia Cairan**: Gunakan refraktometer optik terkalibrasi untuk menguji cairan pendingin sekunder. Konsentrasi propilen glikol harus berukuran tepat **25.0% berat** (± 1.0%), memberikan perlindungan beku hingga -11.5°C dan perlindungan pecah hingga -22.0°C. Konduktivitas cairan pendingin harus < 10 μ S/ cm, dengan pH dipertahankan antara 7.5 dan 9.0.
- **Integritas Fisik**: Periksa baki penampung internal CDU dan rangka dasar dari kelembapan. Verifikasi bahwa sensor pendeteksi kebocoran kabel kontinu benar-benar kering dan diposisikan dengan benar. Periksa tekanan pra-pengisian nitrogen pada tangki ekspansi termal (P_0 = P_fill - 0.2 bar).

### Stasiun 6: Whitespace AI & Rak NVL72
Berdasarkan OpenViking `ALZJ-YW-2.6XZ02`:
- **Distribusi Daya**: Periksa remote power panel (RPP) dan unit distribusi daya (PDU). Pindai pemutus sirkuit dan terminal dengan kamera inframerah untuk mendeteksi terminasi yang kendor.
- **Pembendungan Aliran Udara**: Audit pembendungan lorong dingin (CAC) atau lorong panas (HAC). Verifikasi bahwa tekanan diferensial melintasi lantai panggung atau penghalang penahan tetap ≥ 5.0 Pa. Verifikasi bahwa semua unit rak yang kosong dipasangi blanking panel; satu panel 1U yang hilang memungkinkan 25 L/s udara dingin memotong jalur, menciptakan titik panas lokal.
- **Manifold Pendingin Cair & Kopling**: Audit manifold distribusi vertikal tingkat rak. Periksa semua kopling pemutus cepat (Danfoss FD83 atau Universal Quick Disconnects) yang melayani baki komputasi dan baki sakelar NVLink. Tanda rembesan cairan, pengkristalan, atau pembentukan tetesan merupakan kondisi Stop Work langsung yang memerlukan isolasi baki. Pastikan baki tetesan di bawah manifold rak bersih dan kering.

## Aturan Pencatatan Cacat Seketika

Jika Anda menemukan cacat selama putaran inspeksi sif, cacat tersebut harus dimasukkan ke dalam sistem manajemen pemeliharaan terkomputerisasi (CMMS) lokasi atau register cacat fisik **sebelum Anda meninggalkan ruangan tersebut**.

Mengambil foto di ponsel pribadi dengan niat mencatat masalah pada akhir sif tidak dapat diterima:
- Cacat yang dimasukkan ke dalam register memiliki cap waktu fisik, ID aset, klasifikasi prioritas, dan pemilik yang ditugaskan.
- Foto di ponsel cerdas adalah catatan pribadi yang tidak terkelola yang terlupakan saat alarm berbunyi tiga puluh menit kemudian.

Jika cacat tersebut mengganggu redundansi peralatan atau menyebabkan parameter operasional melintasi ambang batas SLA, putaran sif segera dihentikan, manajer tugas diberitahu melalui radio, dan tiket insiden dibuat di tempat. Jangan pernah menyelesaikan putaran dan dengan santai menyebutkan pompa CDU yang bocor saat makan siang.

## Keputusan yang Harus Dicatat

- Rute inspeksi fisik diselesaikan, dengan cap waktu mulai dan selesai serta tanda tangan teknisi.
- Parameter operasional spesifik dicatat di keenam stasiun inspeksi.
- Pengukuran refraktometer genggam, konduktivitas, dan pH dicatat untuk loop pendingin sekunder.
- Semua cacat dimasukkan ke dalam register resmi lokasi sebelum keluar dari setiap ruangan, atau pernyataan eksplisit tentang nol cacat yang ditemukan.

## Batas Demarkasi Fisik dan Protokol Audit Sif Kuantitatif

Manajer operasional sif wajib menjaga titik demarkasi fisik (`DEMARC`) di seluruh empat cincin fasilitas (Ring 1: Utilitas & Perimeter, Ring 2: Ruang Mekanikal/Elektrikal Utama, Ring 3: Distribusi Whitespace & CDU Sekunder, Ring 4: Interior Rak Penyewa) dan mencatat matriks tolok ukur kuantitatif berikut pada Lembar Hari (Day Sheet):

| Area Audit Sif | Parameter Pemantauan & Metrologi | Amplop Operasi Normal | Ambang Intervensi / Hentikan Pekerjaan (Stop Work) |
| :--- | :--- | :--- | :--- |
| **Batas Beban Redundansi Listrik 2N** | Utilisasi tunak Bus A / Bus B ($P_{\text{bus}} / P_{\text{rated}}$) | $\le 45.0\%$ (Saat gagal 1 jalur $\le 90.0\%$) | Tolak segera penambahan beban rak jika utilisasi $> 45.0\%$ |
| **Hidraulik & Kimiawi CDU Sekunder** | Tekanan pasokan $P_{\text{sup}}$, pendekatan $\Delta T_{\text{PHE}}$, kadar PG | $0.15\sim 0.90\,\text{MPa}$, $\Delta T_{\text{PHE}} \le 8.0\,\text{K}$, PG $25.0\% \pm 1.0\%$ | $\Delta P > 1.0\,\text{bar}$, konduktivitas $> 10\,\mu\text{S/cm}$, atau tetesan kopling |
| **Izin Kerja (PTW) & Energi-Nol LOTO** | Kunci LOTO, pelepasan muatan kapasitor, katup pintas | 100% didampingi host situs; tutup sebelum kedaluwarsa | Penyimpangan dari MOP tertulis atau pekerjaan tambahan spontan |
| **Jam Insiden & Notifikasi SLA** | Deteksi ($T_0$), kondisi aman EOP, pemberitahuan klien | P1: Kirim fakta terverifikasi dalam $\le 15\,\text{menit}$ | Dilarang mencantumkan hipotesis/spekulasi pada notifikasi |
