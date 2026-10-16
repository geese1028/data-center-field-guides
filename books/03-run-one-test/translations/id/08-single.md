Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 8. Satu Sistem dalam Satu Waktu

Verifikasi dinamis dengan beberapa sistem yang saling terhubung di bawah beban termal adalah fase terintegrasi berikutnya. Fase ini didedikasikan untuk memvalidasi satu mesin dalam satu waktu, mengeksekusi logika operasional yang presisi sebagaimana didefinisikan dalam skrip pengujian mandirinya sementara semua sistem yang berdekatan tetap dalam keadaan diam (*quiet*).

Dalam hierarki komisioning global, ini adalah **Pengujian Kinerja Fungsional (FPT) Level 4**. Ini memvalidasi proteksi otonom, *loop* kontrol modulasi, dan alarm fisik dari masing-masing mesin individual sebelum dikenai stres termal multi-megawatt. Mengarsipkan pengujian sistem tunggal di bawah Pengujian Sistem Terintegrasi Level 5 hanya karena peralatan tersebut secara fisik berada di dalam aula data adalah kesalahan dokumentasi yang serius.

![Arsitektur P&ID Hidrolik CDU](../figures/fig-02-cdu-hydraulic-pandid.png)

## Verifikasi Unit Distribusi Pendingin (CDU) Otonom

Unit Distribusi Pendingin (*Coolant Distribution Unit* - CDU) adalah antarmuka hidrolik kritis yang memisahkan sistem air fasilitas primer (*facility water system* - FWS) dari sistem pendinginan teknologi sekunder (*technology cooling system* - TCS). Sebelum beban termal apa pun diterapkan oleh bank beban, CDU harus membuktikan kemampuannya untuk mengontrol sirkulasi fluida secara otonom di bawah Skrip 04 dan Skrip 05.

### 1. Startup Pompa, Modulasi VFD, dan Soft-Start
Beri energi pada pompa sekunder CDU dengan *loop* fasilitas primer terisolasi. Eksekusi siklus *start* dan *stop* yang terkendali:
- Pastikan Penggerak Frekuensi Variabel (*Variable Frequency Drives* - VFD) menaikkan kecepatan pompa sentrifugal tipe kaleng (*canned centrifugal pumps*) secara mulus di sepanjang kurva akselerasi yang dikonfigurasi (biasanya 10 hingga 15 detik) tanpa menyebabkan lonjakan arus listrik atau kejutan hidrolik.
- Verifikasi penggantian (*override*) frekuensi manual: jalankan VFD di seluruh rentang operasinya (30,0 Hz hingga 50,0/60,0 Hz) dan catat arus motor, faktor daya, serta tanda getaran bantalan (*bearing vibration signatures*).
- Tetapkan garis dasar kurva pompa dingin (*cold pump curve baseline*): perhitungkan pergeseran densitas fluida dan viskositas antara fluida dingin dan panas. Untuk campuran 25% Propylene Glycol (PG25), densitas pada kondisi dingin 20°C adalah sebesar 1030 kg/m³ (dengan viskositas kinematik lebih tinggi), bergeser menjadi 1018 kg/m³ pada suhu operasi 45°C. Pergeseran densitas ini memengaruhi daya poros pompa dan pengukuran *head* hidrolik garis dasar yang harus dicatat secara cermat.

### 2. Pergantian Otomatis Pompa Sekunder N+1 (Auto-Changeover)
CDU berdensitas tinggi modern menggunakan konfigurasi pemompaan sekunder N+1 (misalnya, pompa berkapasitas ganda 100%, P-1A *Lead* dan P-1B *Standby*). Logika pergantian otomatis harus diverifikasi melalui simulasi trip fisik:
- Operasikan Pompa P-1A pada kecepatan nominal 100% dengan *loop* pada aliran operasi desain.
- Simulasikan trip elektrikal dengan membuka pemutus arus sirkuit kontrol ke inverter P-1A atau memicu input gangguan digitalnya.
- **Kriteria Penerimaan**:
 - Pengontrol CDU lokal harus mendeteksi gangguan, mencatat alarm kritis, dan mengeluarkan perintah *start* ke Pompa Siaga P-1B dalam waktu ≤ 500 ms.
 - Pompa Siaga P-1B harus berakselerasi ke kecepatan operasi penuh dan memulihkan tekanan diferensial sekunder dalam waktu ≤ 1,5 detik.
 - Katup searah (*non-return check valve*) pada pelepasan Pompa P-1A harus menutup rapat tanpa hantaman hidrolik (*hydraulic slam*) yang keras (puncak denyut palu air / *water hammer* tidak boleh melebihi ± 50 kPa).
 - Tekanan diferensial *loop* sekunder tidak boleh turun di bawah batas minimum kavitasi (100 kPa), memastikan aliran terus-menerus melalui bank beban tanpa memicu trip termal palsu.

### 3. Pelacakan Katup Kontrol Suhu (TCV) Modulasi
Katup Kontrol Suhu *loop* primer (TCV-101, biasanya katup *globe* modulasi 2-arah atau 3-arah dengan aktuator elektronik) mengatur aliran air dingin fasilitas primer melalui Penukar Panas Pelat (*Plate Heat Exchanger* - PHE-101) untuk mempertahankan suhu pasokan sekunder:
- Gerakkan aktuator melalui rentang kontrol penuhnya menggunakan sumber kalibrasi 0–10V DC atau 4–20 mA.
- Verifikasi waktu buka dan tutup langkah penuh (*full-stroke*) terhadap pengajuan pabrikan (biasanya τ ≤ 30 detik).
- Verifikasi posisi aman-gagal (*fail-safe*) saat kehilangan daya kontrol: TCV-101 harus gagal dalam kondisi terbuka mekanis (100% aliran primer) atau menahan posisi terakhir tergantung pada maksud desain fasilitas.
- Verifikasi integritas kebocoran dudukan (*seat leakage*): dengan katup diperintahkan 100% tertutup, konfirmasikan bahwa aliran primer turun ke nol (kelas kebocoran ANSI/FCI 70-2 Kelas IV atau lebih baik).

### 4. Katup Bypass Tekanan Diferensial Sekunder (BPV)
Periksa katup bypass modulasi BPV-201, yang dipasang di antara *header* pasokan dan balik sekunder. Pastikan bahwa ketika katup penyeimbang manifold hilir dicekik, BPV membuka secara mulus untuk mempertahankan *head* pompa yang konstan, mencegah impeler beroperasi pada kondisi aliran tertutup (*dead-heading*).

## Telemetri BMS dan Pemeriksaan Titik-ke-Titik Instrumen Lapangan

Jangan pernah mengasumsikan bahwa nilai yang ditampilkan pada layar Sistem Manajemen Bangunan (*Building Management System* - BMS) atau antarmuka mesin-manusia (*Human-Machine Interface* - HMI) CDU mencerminkan kenyataan fisik. Setiap titik telemetri yang didefinisikan dalam klaim proyek harus menjalani pemeriksaan silang fisik titik-ke-titik terhadap instrumen referensi lapangan yang terkalibrasi:

**AUDIT KALIBRASI TELEMETRI TITIK-KE-TITIK**

| TITIK TELEMETRI | PEMBACAAN BMS/HMI | REF TERKALIBRASI LAP | DELTA DIIZINKAN | KEPUTUSAN AUDIT |
| :--- | :--- | :--- | :--- | :--- |
| Suhu Pasokan Sekun | 40,12 °C | 40,08 °C (PT100) | +/- 0,30 K | LULUS |
| Suhu Balik Sekunder | 50,25 °C | 50,15 °C (PT100) | +/- 0,30 K | LULUS |
| Laju Aliran Sekunder | 115,4 m³/h | 116,1 m³/h (Ultrason | +/- 2,0% | LULUS |
| Tekanan Pasokan Sek | 285,0 kPa | 282,5 kPa (Manometer | +/- 10,0 kPa | LULUS |
| Tekanan Balik Sek | 115,0 kPa | 118,0 kPa (Manometer | +/- 10,0 kPa | LULUS |
| Level Tangki Ekspans | 68,0 % | 67,5 % (Kaca Intip) | +/- 3,0 % | LULUS |

Jika diskrepansi melebihi toleransi yang diizinkan, *offset* sensor harus dikalibrasi ulang atau sensor diganti. Jangan pernah menyesuaikan rentang toleransi yang dapat diterima hanya untuk mencocokkan sensor yang mengalami pergeseran (*drifting*).

## Injeksi Alarm Perangkat Keras Fisik

Alarm harus divalidasi melalui injeksi perangkat keras fisik. Mensimulasikan alarm dengan mengubah *setpoint* perangkat lunak dalam berkas konfigurasi atau mengubah suatu bit di stasiun kerja rekayasa sama sekali tidak dapat diterima. Simulasi perangkat lunak membuktikan bahwa perangkat lunak dapat membaca suatu variabel; itu tidak membuktikan bahwa sensor fisik, pengkabelan lapangan, dan logika relai berfungsi dalam kondisi dunia nyata.

Eksekusi pengujian alarm fisik di bawah Skrip 06:
- **Alarm Aliran Rendah Sekunder**: Cekik katup isolasi manual pada *header* pasokan sekunder secara bertahap hingga pengukur aliran elektromagnetik mencatat aliran yang turun di bawah ambang batas trip aliran rendah. Konfirmasikan bahwa pengontrol CDU membunyikan klakson alarm lokal, menyalakan suar merah, mentransmisikan alarm Modbus/BACnet mendesak ke BMS pusat, dan menjatuhkan relai interlock bank beban.
- **Level Cairan Rendah Tangki Ekspansi**: Tekan tuas uji pada sakelar pelampung magnetik tangki ekspansi secara manual. Pastikan bahwa CDU memperingatkan operator, mengunci pemanas listrik (*lock-out*), dan memerintahkan pompa air pengisi otomatis (*makeup water pump*) untuk menyala.
- **Deteksi Kebocoran Cairan Loop Sekunder**: Teteskan 5 mL air demineralisasi melintasi tali penginderaan deteksi kebocoran eksternal yang ditempatkan di bawah sambungan pipa CDU dan baki manifold. Pastikan pengontrol deteksi kebocoran terpicu dalam waktu < 2,0 detik, menampilkan lokasi jarak kebocoran yang tepat, dan mengirimkan alarm mengunci (*latching alarm*) kritis ke BMS pengawas.

**TIGA KEPUTUSAN AUDIT YANG MUNGKIN UNTUK SUATU ALARM**

| 1. LULUS (PASS) | Alarm diinjeksi fisik pd sensor; penampil lokal aktif; BMS mencatat peristiwa dgn stempel waktu & deskripsi benar; interlock dieksekusi bersih. |
| :--- | :--- |
| 2. GAGAL (FAIL) | Alarm diinjeksi tapi sensor gagal mendeteksi; penundaan melebihi toleransi; relai interlock gagal lepas; langsung dicatat pd Log Cacat Master. |
| 3. TIDAK DIDEMONSTRASIKAN | Peralatan tdk memiliki sensor fisik, kabel, atau register perangkat lunak utk memicu alarm ini. Dicatat sbg "TIDAK DIDEMONSTRASIKAN" di Lembar 2. |

Jika alarm tertentu tidak dapat didemonstrasikan karena perangkat kerasnya dihilangkan selama konstruksi, baris pada Lembar 2 harus dicatat sebagai **TIDAK DIDEMONSTRASIKAN** (*NOT DEMONSTRATED*). Mencatat alarm yang belum diuji sebagai "LULUS" hanya karena "vendor berjanji logikanya bekerja" adalah pelanggaran profesional yang serius.

## Gerbang Prasyarat Level 4

Pengujian kinerja fungsional Level 4 ditutup ketika semua skrip sistem tunggal telah dieksekusi dan ditandatangani sepenuhnya. Setiap injeksi alarm yang gagal, sensor yang tidak terkalibrasi, atau katup kontrol yang berosilasi (*hunting*) harus diselesaikan secara formal dan diuji ulang sebelum fasilitas melangkah ke pengujian termal multisistem.

## Keputusan yang Harus Dicatat Sebelum Mulai Pengujian

- Log *soft-start* pompa CDU dan pelacakan frekuensi VFD.
- Rekaman kondisi transien pergantian otomatis pompa sekunder N+1 yang disaksikan (keterlambatan peralihan ≤ 1,5 s).
- Log kalibrasi telemetri titik-ke-titik di semua titik pemantauan kritis.
- Log injeksi alarm fisik, mencatat semua butir Lulus, Gagal, dan Tidak Didemonstrasikan.
- Konfirmasi bahwa semua prasyarat Level 4 telah ditandatangani sebelum membuka Level 5.
