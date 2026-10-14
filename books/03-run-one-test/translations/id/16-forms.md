Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 16. Lembar-Lembar Kerja

Salin formulir-formulir rekayasa master ini ke dalam binder proyek Anda. Isi setiap sel dengan tinta di lantai kerja aula data. Satu insinyur mengukur dengan instrumen terkalibrasi; insinyur kedua mencatat pembacaannya. Sel yang kosong adalah perintah henti otomatis (*automated stop*). Angka yang disalin dari ingatan adalah cacat (*defect*).

---

## Lembar 1. QA Statis Pra-Pemberian Energi & Verifikasi Hidrolik (Level 2 / Level 3)

**Nama Proyek**: __________________________ **ID Aula Data / Ruangan**: __________________________ 
**Unit Uji (ID CDU / Baris)**: ________________ **Tanggal Verifikasi**: __________________________ 
**Pimpinan Insinyur Elektro**: ____________________ **Pimpinan Insinyur Mesin**: __________________________ 
**Teknisi Pengukuran**: ______________________ **Teknisi Pencatat Tinta**: __________________________ 

### 1. Pembongkaran Peti Kemas Fisik, Inspeksi Struktural & Kopling
- [ ] Rangka bank beban diperiksa dari kerusakan pengiriman, retak las, atau deformasi roda kastor: **LULUS / GAGAL**
- [ ] Kopling lepas-cepat diperiksa (Danfoss Hansen FD83 / ISO 16028): **LULUS / GAGAL**
- [ ] Segel elastomer internal EPDM diperiksa di bawah pembesaran (nol sobekan, robekan, atau burr): **LULUS / GAGAL**
- [ ] Selang fleksibel sekunder bertekanan tinggi diperiksa (berkepang kawat, teruji ≥ 1,5× MAOP): **LULUS / GAGAL**
- [ ] Perutean selang diverifikasi: nol tekukan tajam, semua radius tekukan melebihi batas minimum yang diizinkan: **LULUS / GAGAL**
- [ ] Pengikatan seismik dan struktur penyangga pedestal lantai terangkat diverifikasi terhadap gambar PE struktural: **LULUS / GAGAL**

### 2. Uji Isolasi Listrik Tanpa Energi & Keselamatan (LOTO Ditegakkan)
- **Model & Nomor Seri Penguji Resistansi Isolasi**: ____________________ **Kedaluwarsa Kalibrasi**: ____________ 
- **Tegangan Uji Diterapkan**: 1000V DC selama 60 detik kontinu 
 - Fasa A ke Fasa B: __________ MΩ (Batas: ≥ 100,0 MΩ) — **LULUS / GAGAL** 
 - Fasa B ke Fasa C: __________ MΩ (Batas: ≥ 100,0 MΩ) — **LULUS / GAGAL** 
 - Fasa C ke Fasa A: __________ MΩ (Batas: ≥ 100,0 MΩ) — **LULUS / GAGAL** 
 - Fasa A ke Tanah (PE): ______ MΩ (Batas: ≥ 100,0 MΩ) — **LULUS / GAGAL** 
 - Fasa B ke Tanah (PE): ______ MΩ (Batas: ≥ 100,0 MΩ) — **LULUS / GAGAL** 
 - Fasa C ke Tanah (PE): ______ MΩ (Batas: ≥ 100,0 MΩ) — **LULUS / GAGAL** 
- **Kontinuitas Ikatan Pentanahan**: Sasis ke Busbar Pentanahan Utama Fasilitas: __________ Ω (Batas: ≤ 0,10 Ω) — **LULUS / GAGAL** 
- **Indikator Urutan & Rotasi Fasa**: Diuji pada kotak sadapan pasokan: **SEARAH JARUM JAM (A-B-C) / BERLAWANAN JARUM JAM** 
 *(KRITIS: Jika urutan fasa tidak searah jarum jam, JANGAN beri energi. Rotasi terbalik akan menghancurkan bantalan pompa kaleng.)*

### 3. Pembilasan Hidrolik Sekunder, Penahanan Hidrostatik & Audit Volume
- [ ] Pembilasan kimiawi loop sekunder selesai sesuai BSRIA BG 29/2020 (kecepatan penggerusan ≥ 1,5 m/s): **TERLAMPIR** 
- [ ] Saringan diperiksa dan dibersihkan; sertifikat kebersihan fluida ISO 4406: **TERLAMPIR** 
- **Penahanan Tekanan Hidrostatik**: 
 - Tekanan Operasi Maksimum yang Diizinkan (*MAOP*): __________ bar 
 - Tekanan Uji Penahanan Diterapkan (1,5× MAOP): __________ bar 
 - Stempel Waktu Mulai: ____________________ Stempel Waktu Selesai: ____________________ (Durasi: ≥ 2,0 jam) 
 - Tekanan Mulai: __________ bar Tekanan Selesai: __________ bar Penurunan Tekanan (ΔP): __________ bar 
 - Standar Penerimaan: ΔP ≤ 0,0 bar (memperhitungkan stabilisasi termal). Laju kebocoran: **NOL TETES / MENIT** 
 - Penilaian Verifikasi: **LULUS / GAGAL** 
- [ ] Deaerasi vakum dan pembuangan udara menyeluruh selesai; kaca intip bersih dari gelembung mikro: **LULUS / GAGAL** 
- **Perhitungan Inventaris Fluida Sekunder**: 
 - Volume Internal CDU: __________ L 
 - Volume Distribusi Manifold: __________ L 
 - Volume Selang Fleksibel: __________ L 
 - Volume Internal Bank Beban: __________ L 
 - **Total Inventaris Fluida Sekunder (V_total)**: __________ L 
- **Garis Dasar Kimia Fluida**: Konsentrasi PG Refraktometer: __________ % (Target: 25,0% ± 0,5%) 

### 4. Audit Koordinasi Proteksi Hulu
- Peringkat Bingkai Pemutus Arus PDU Hulu: __________ A Peringkat Plug Trip: __________ A 
- Pengaturan Elektronik LSIG: Long Time: ______ s Short Time Pickup: ______ x Instantaneous: ______ x 
- [ ] Kurva koordinasi proteksi diverifikasi terhadap karakteristik arus masuk bank beban: **LULUS / GAGAL** 

**PENILAIAN GERBANG LEMBAR 1**: [ ] **TAHAP LULUS — DIIZINKAN UNTUK LEVEL 4** [ ] **TAHAP DIBLOKIR (CACAT TERBUKA)** 
**Tanda Tangan Pimpinan Insinyur Elektro**: ________________________ **Tanggal**: __________________ 
**Tanda Tangan Pimpinan Insinyur Mesin**: ________________________ **Tanggal**: __________________ 

---

## Lembar 2. Proteksi CDU Otonom & Injeksi Alarm Fisik (Level 4 FPT)

**Nama Proyek**: __________________________ **ID Aula Data / Ruangan**: __________________________ 
**Label Aset CDU**: __________________________ **Revisi Firmware / Perangkat Lunak**: ______________________ 
**Pimpinan Insinyur Kontrol**: ______________________ **Insinyur Mesin**: ______________________________ 
**Saksi Operasi Fasilitas**: ____________________ **Tanggal & Giliran Kerja Uji**: ____________________________ 

*Setiap baris alarm harus diinjeksikan secara fisik pada sensor atau kabel lapangan. Simulasi setpoint perangkat lunak dilarang.*

| DESKRIPSI ALARM | METODE INJEKSI FISIK | SUARA / SUAR LOKAL | ANUNSIATOR HMI CDU | STEMPEL WAKTU BMS PENGAWAS | TINDAKAN TRIP INTERLOCK | PENILAIAN AUDIT (LULUS / GAGAL / TIDAK DIDEMONSTRASIKAN) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Aliran Rendah Sekunder** | Cekik katup penyeimbang pasokan hingga aliran turun di bawah setpoint rendah (<90 m³/h) | [ ] Suara [ ] Visual | [ ] Peringatan dicatat | [ ] Dicatat: ________ | Menjatuhkan relai interlock bank beban | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Suhu Pasokan Sekunder Tinggi** | Berikan penangas termal terkalibrasi / jembatan resistor ke probe imersi PT100 (>45,0°C) | [ ] Suara [ ] Visual | [ ] Peringatan dicatat | [ ] Dicatat: ________ | Memicu pelepasan beban panas bertahap | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Tekanan Rendah Sekunder** | Buang sebagian blok isolasi pemancar tekanan hingga P < 100 kPa | [ ] Suara [ ] Visual | [ ] Peringatan dicatat | [ ] Dicatat: ________ | Mengunci pemanas listrik (lock-out) | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Level Rendah Tangki Ekspansi**| Gerakkan tangkai uji pelampung magnetik manual ke batas pemutus level rendah | [ ] Suara [ ] Visual | [ ] Peringatan dicatat | [ ] Dicatat: ________ | Memerintahkan pompa pengisi otomatis MENYALA | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Aliran Rendah Air Primer** | Cekik katup isolasi FWS primer hingga aliran < 50 m³/h | [ ] Suara [ ] Visual | [ ] Peringatan dicatat | [ ] Dicatat: ________ | Memodulasi TCV ke 100% terbuka penuh | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Suhu Pasokan Primer Tinggi**| Naikkan suhu air primer atau injeksikan offset sensor (> 35,0°C) | [ ] Suara [ ] Visual | [ ] Peringatan dicatat | [ ] Dicatat: ________ | Peringatan dicatat; menandai PUE fasilitas | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Trip Inverter VFD Pompa Utama**| Lepaskan input gangguan digital atau buka pemutus daya kontrol VFD | [ ] Suara [ ] Visual | [ ] Peringatan dicatat | [ ] Dicatat: ________ | Menyalakan Pompa Siaga dlm ≤ 1,5 s | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Kebocoran Baki Penampung Internal** | Berikan 5 mL air demineralisasi melintasi sensor optik / pelampung baki penampung | [ ] Suara [ ] Visual | [ ] Peringatan dicatat | [ ] Dicatat: ________ | Mengisolasi CDU; trip kontaktor bank beban | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Kebocoran Tali Pengindera Eksternal**| Basahi tali pengindera perimeter eksternal di sepanjang baki manifold sekunder | [ ] Suara [ ] Visual | [ ] Peringatan dicatat | [ ] Dicatat: ________ | Menunjukkan lokasi pasti; memicu peringatan | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Tombol Penghentian Darurat (E-Stop)**| Tekan tombol fisik E-Stop jamur merah pada pintu depan CDU | [ ] Suara [ ] Visual | [ ] Peringatan dicatat | [ ] Dicatat: ________ | Menjatuhkan bus 24V; putus relai pompa & pemanas | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |

### Waktu Interlock Perangkat Keras dan Failover Siaga
- Keterlambatan Terukur Auto-Start Pompa Siaga: __________ ms (Batas: ≤ 500 ms) 
- Waktu Terukur Pemulihan Aliran Sekunder: ______ s (Batas: ≤ 1,5 s) 
- Tekanan Loop Sekunder Minimum Saat Failover: ______ kPa (Batas: ≥ 100 kPa) 
- Keterlambatan Terukur Pemutusan Daya E-Stop Fisik: ______ ms (Batas: ≤ 50 ms) 

**PENILAIAN GERBANG LEMBAR 2**: [ ] **LEVEL 4 LULUS — DIIZINKAN UNTUK LEVEL 5** [ ] **LEVEL 4 DIBLOKIR (CACAT TERBUKA)** 
**Tanda Tangan Pimpinan Insinyur Kontrol**: ________________________ **Tanggal**: __________________ 
**Saksi Operasi Fasilitas**: ________________________ **Tanggal**: __________________ 

---

## Lembar 3. Tangga Termal Bertingkat & Log Penutupan Panas Entalpi (Level 5 IST)

*Eksekusi satu salinan khusus dari Lembar 3 untuk setiap anak tangga langkah termal: 25%, 50%, 75%, 100%, dan 110%.*

**Nomor Langkah**: Langkah _____ dari 5 **Target Beban Termal**: __________ kW (______ % dari Kapasitas Pengenal) 
**Stempel Waktu Mulai Langkah**: ____________________ **Stempel Waktu Keseimbangan**: ____________________ 
**Total Durasi Waktu Tunggu**: __________ menit (Persyaratan minimum: ≥ 45 menit; perendaman 100% ≥ 4,0 jam) 
**Nama Berkas CSV Frekuensi Tinggi**: __________________________ **Checksum SHA-256**: ________________________ 

### 1. Telemetri Keseimbangan Panas Termodinamika & Entalpi

| PARAMETER | BATAS SPESIFIKASI SKRIP | NILAI TERUKUR (REF LAPANGAN) | LOG TELEMETRI / BMS | DELTA AUDIT |
| :--- | :--- | :--- | :--- | :--- |
| **Daya Aktif 3-Fasa (P_elec)** | Target: _____ kW ± 1,5% | __________ kW (Kelas 0,2) | __________ kW | ______ % |
| **Suhu Pasokan Primer ($T_pri\_sup$)** | Nominal: 30,0°C ± 1,0 K | __________ °C | __________ °C | ______ K |
| **Suhu Balik Primer ($T_pri\_ret$)** | Diharapkan: ≤ 36,5°C | __________ °C | __________ °C | ______ K |
| **Aliran Volumetrik Primer (Q_pri)** | Maksimum: ≤ 180 m³/h | __________ m³/h | __________ m³/h | ______ % |
| **Tekanan Diferensial Primer (ΔP_pri)**| Desain: ≤ 120 kPa melintasi PHE | __________ kPa | __________ kPa | ______ kPa |
| **Suhu Pasokan Sekunder ($T_sec\_sup$)** | Setpoint: 40,0°C ± 0,5 K | __________ °C (Ref PT100) | __________ °C | ______ K |
| **Suhu Balik Sekunder ($T_sec\_ret$)** | Diharapkan: ≤ 50,5°C | __________ °C (Ref PT100) | __________ °C | ______ K |
| **Delta-T Fluida Sekunder (ΔT_sec)** | Desain: 10,0 K ± 0,5 K | __________ K | __________ K | ______ K |
| **Aliran Volumetrik Sekunder (Q_sec)** | Desain: 115,0 m³/h ± 3,0% | __________ m³/h (Ultrasonik) | __________ m³/h | ______ % |
| **Frekuensi VFD Pompa Sekunder** | Rentang operasi: 30,0 hingga 50,0 Hz | __________ Hz | __________ Hz | ______ Hz |
| **Diferensial Tekanan Pompa Sekunder (ΔP_pump)**| Desain: 220 kPa ± 10 kPa | __________ kPa | __________ kPa | ______ kPa |
| **Posisi Katup TCV Primer** | Pelacakan modulasi (0-100%) | __________ % terbuka | __________ % terbuka | ______ % |

### 2. Perhitungan Keseimbangan Panas Entalpi & Keseimbangan Termal
- **Laju Stabilisasi Termal**: $\left|\frac{dT_{\text{supply}}}{dt}\right| = \text{__________ K / 10 menit}$ (Batas Penerimaan: ≤ 0,20 K / 10 menit) — **LULUS / GAGAL** 
- **Ekstraksi Panas Cairan Sekunder**: 
 $$Q_{\text{liquid}} = \dot{m} \cdot c_p \cdot (T_{\text{return}} - T_{\text{supply}}) = \text{__________ kW}$$ 
 *(Evaluasi ρ dan c_p untuk Propylene Glycol 25% pada suhu ruah: $T_{\text{bulk}} = \frac{T_{\text{sup}} + T_{\text{ret}}}{2}$)* 
- **Rasio Penutupan Panas Entalpi**: 
 $$\eta = \frac{Q_{\text{liquid}}}{P_{\text{elec}}} \times 100\% = \text{__________ \%} \quad (\text{Rentang Penerimaan: } 97,0\% \le \eta \le 101,5\%)$$ — **LULUS / GAGAL** 
- **Margin Titik Embun**: 
 - Suhu Ambien Aula Data: ______ °C Kelembapan Relatif: ______ % Titik Embun Terhitung: ______ °C 
 - Margin: $T_sec\_sup - T_dew = __________ K$ (Batas Penerimaan: ≥ 2,0 K) — **LULUS / GAGAL** 

### 3. Pemindaian Termografi Inframerah (IR) Listrik (Menit ke-30 pada Tahap Beban)
- Model & Nomor Seri Kamera Pencitraan Termal: ____________________ Kedaluwarsa Kalibrasi: ____________ 
- Suhu Terminal Puncak Tercatat: __________ °C (Batas Penerimaan: ≤ 75,0°C) — **LULUS / GAGAL** 
- Lokasi Fisik Terminal Terpanas: __________________________________________________ 
- Delta-T Antarfasa Maksimum: __________ K (Batas Penerimaan: ≤ 5,0 K) — **LULUS / GAGAL** 

### 4. Survei Distribusi Aliran Sekunder Multi-Rak (10 Bank Beban)

| ID RAK | NOMOR SERI BANK BEBAN | ALIRAN VOLUMETRIK (LPM) | DELTA DARI RATA-RATA (%) | dP RAK (kPa) | LULUS / GAGAL |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rak 01** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] LULUS [ ] GAGAL |
| **Rak 02** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] LULUS [ ] GAGAL |
| **Rak 03** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] LULUS [ ] GAGAL |
| **Rak 04** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] LULUS [ ] GAGAL |
| **Rak 05** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] LULUS [ ] GAGAL |
| **Rak 06** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] LULUS [ ] GAGAL |
| **Rak 07** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] LULUS [ ] GAGAL |
| **Rak 08** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] LULUS [ ] GAGAL |
| **Rak 09** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] LULUS [ ] GAGAL |
| **Rak 10** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] LULUS [ ] GAGAL |
| **STATISTIK BARIS**| **Aliran Rata-Rata: _______ LPM** | **Deviasi Standar (σ): _______** | **CV ($\frac{\sigma}{\mu}\times 100\%$): _______ %** | Batas: ≤ 5,0% | **LULUS / GAGAL** |

**PENILAIAN LANGKAH LEMBAR 3**: [ ] **TAHAP TERMAL DITERIMA** [ ] **TAHAP GAGAL / TIDAK STABIL** 
**Pimpinan Uji Berwenang (Otoritas Perintah)**: ____________________ **Tanda Tangan**: __________________ 
**Tanda Tangan Pimpinan Insinyur Elektro**: ________________________ **Tanggal**: __________________ 
**Tanda Tangan Pimpinan Insinyur Mesin**: ________________________ **Tanggal**: __________________ 

---

## Lembar 4. Kegagalan Transien Dinamis & Log Ketahanan Redundansi (Level 5 IST)

**Nama Proyek**: __________________________ **ID Aula Data / Ruangan**: __________________________ 
**Label Aset CDU**: __________________________ **Beban Dasar Saat Pengujian**: 1200 kW (100% Beban Desain) 
**Tanda Tangan Pimpinan Pengujian**: ____________________ **Tanda Tangan Insinyur Kontrol**: ________________________ 
**Saksi Pemilik Fasilitas**: ____________________ **Stempel Waktu Tanggal & Giliran Kerja**: ______________________ 

*Kurva pemulihan tunak bukan tanda kelulusan. Catat garis dasar pra-kejadian, defleksi transien puncak, dan durasi pemulihan.*

### Skenario 1: Trip Pompa Sekunder & Pergantian Otomatis (Pertukaran VFD N+1)
- Pompa Beroperasi Pra-Kejadian: Pompa P-1A (Kecepatan: 50,0 Hz, Aliran: 115,0 m³/h, dP: 220 kPa) 
- Metode Injeksi Trip Simulasi: Pemicu gangguan digital inverter pada stempel waktu: ____________________ 
- Auto-Start Pompa Siaga P-1B Terdeteksi: __________ ms (Batas: ≤ 500 ms) 
- dP Sekunder Minimum Tercatat: __________ kPa (Batas: ≥ 100,0 kPa; tanpa kavitasi) 
- Puncak Denyut Tekanan Palu Air: __________ kPa (Batas: ≤ ± 50,0 kPa) 
- Aliran Sekunder Pulih ke ≥ 95% Desain: __________ s (Batas: ≤ 1,5 detik) 
- Interlock Termal Bank Beban Jatuh/Trip?: **YA (GAGAL) / TIDAK (LULUS)** 
- Penilaian Skenario 1: **LULUS / GAGAL** 

### Skenario 2: Kehilangan Pengumpan Listrik Primer 2N Jalur A / Transfer Bus ATS
- Pemutus Jalur A Jatuh (*Tripped*) pada Stempel Waktu: ____________________ 
- Durasi Transisi Sakelar Transfer Bus: __________ ms (Batas: ≤ 16,0 ms) 
- Tegangan Minimum Bus Kontrol 24V DC CDU: __________ V DC (Batas: ≥ 22,0 V DC; nol penurunan) 
- Reboot Pengontrol PLC CDU Teramati?: **YA (GAGAL KRITIS) / TIDAK (LULUS)** 
- Ketahanan / Pemulihan VFD Pompa Sekunder: __________ s (Batas: ≤ 3,0 s) 
- Tegangan Tunak Jalur B: __________ V Arus: __________ A 
- Penilaian Skenario 2: **LULUS / GAGAL** 

### Skenario 3: Gangguan Pasokan Air Dingin Primer (Ketahanan Inersia Termal)
- Katup Isolasi FWS Primer Diperintahkan Tertutup pada Stempel Waktu: ____________________ 
- Suhu Pasokan Sekunder Pra-Trip: 40,0 °C Beban Dipertahankan: 1200 kW 
- Laju Kenaikan Suhu Sekunder: $\frac{dT}{dt} = \text{__________ K / s}$ 
- Waktu Penyangga ke Alarm Suhu Tinggi (45,0°C): __________ s (Batas: t_buffer ≥ 40,0 s) 
- Pelepasan Beban Otomatis Dimulai oleh Peringatan CDU?: **YA / TIDAK** 
- Trip Suhu Kritis Darurat Bekerja (50,0°C): Stempel Waktu: ____________________ 
- Semua Pemanas Bank Beban Dimatikan Energinya Seketika?: **YA / TIDAK** (Suhu fluida puncak: ______ °C) 
- Penilaian Skenario 3: **LULUS / GAGAL** 

### Skenario 4: Pemutusan Komunikasi BMS (Aman-Gagal Lokal Otonom)
- Kabel Ethernet Modbus-TCP / BACnet Diputus pada Stempel Waktu: ____________________ 
- PLC Lokal CDU Beralih ke Mode Mandiri Otonom?: **YA / TIDAK** 
- Osilasi Kecepatan Pompa Sekunder / Perburuan Teramati?: **YA (GAGAL) / TIDAK (LULUS)** 
- Hanyutan / Perburuan Katup Modulasi TCV-101 Teramati?: **YA (GAGAL) / TIDAK (LULUS)** 
- Suhu Pasokan Sekunder Dipertahankan pada 40,0°C ± 0,5 K selama 30 Menit: **LULUS / GAGAL** 
- Penilaian Skenario 4: **LULUS / GAGAL** 

### Skenario 5: Kejutan Perubahan Bertahap Termal Cepat ($100% \to 30% \to 100%$)
- Penurunan Beban dari 1200 kW ke 360 kW pada Stempel Waktu: ____________________ 
 - Penurunan Suhu Pasokan Sekunder Minimum (*Undershoot*): __________ °C (Batas: ≥ 38,5°C) 
 - Waktu Stabilisasi Respons TCV-101: __________ s (Batas: ≤ 45 s) 
- Kenaikan Beban dari 360 kW ke 1200 kW pada Stempel Waktu: ____________________ 
 - Lonjakan Suhu Pasokan Sekunder Maksimum (*Overshoot*): __________ °C (Batas: ≤ 41,5°C) 
 - Aliran Fluida Sekunder Dipertahankan Stabil ± 2,0%: **LULUS / GAGAL** 
- Penilaian Skenario 5: **LULUS / GAGAL** 

**PENILAIAN DINAMIS LEMBAR 4**: [ ] **SELURUH UJI TRANSIEN LULUS** [ ] **KEGAGALAN TRANSIEN DICATAT** 
**Tanda Tangan Pimpinan Pengujian**: ________________________ **Tanggal**: __________________ 
**Saksi Pemilik Fasilitas**: ________________________ **Tanggal**: __________________ 

---

## Lembar 5. Protokol Pemadaman Energi Terkendali, Pendinginan & Demobilisasi

**Nama Proyek**: __________________________ **ID Aula Data / Ruangan**: __________________________ 
**Label Aset Unit Uji**: ____________________ **Tanggal & Waktu Giliran Kerja**: ____________________________ 
**Pimpinan Pengujian (Mengarahkan Pemadaman)**: ________ **Pimpinan Insinyur Elektro**: __________________________ 
**Pimpinan Insinyur Mesin**: ____________________ **Pimpinan Keselamatan**: ________________________________ 

*Setiap langkah pemadaman harus dieksekusi dan dicentang dalam urutan kronologis yang ketat. Membalikkan langkah membatalkan lembar ini.*

### 1. Langkah Pemutusan Energi Sekuensial Wajib

- [ ] **LANGKAH 01: Lepaskan Beban Termal Aktif ke 0 kW** 
 *Perintahkan semua tahap pemanas bank beban ke 0 kW melalui pengontrol. Pastikan semua pulsa penyalaan thyristor SCR berhenti dan kontaktor magnetik terbuka. Daya aktif terverifikasi 0,0 kW.* 
 Stempel Waktu: ____________________ Paraf: ________ 

- [ ] **LANGKAH 02: Buka & Kunci Pemutus Daya Bank Beban (LOTO)** 
 *Buka pemutus arus sirkuit cabang bank beban pada PDU atau kotak sadapan atas. Pasang gembok pengunci dan label bahaya. Buktikan sirkuit telah mati tegangan dengan detektor tegangan terkalibrasi.* 
 Stempel Waktu: ____________________ Paraf: ________ 

- [ ] **LANGKAH 03: Perendaman Pendinginan Sirkulasi Fluida 10 Menit** 
 *KRITIS: Pertahankan pompa sekunder CDU tetap beroperasi pada 50,0 Hz selama minimum 10 menit dengan pemanas mati. Ini membuang panas laten dari selubung pemanas dan mencegah pendidihan fluida lokal.* 
 Waktu Mulai: ____________________ Waktu Selesai: ____________________ (Suhu Fluida Sekunder: ______ °C) 
 Paraf: ________ 

- [ ] **LANGKAH 04: Pemadaman Terkendali Pompa Sekunder CDU** 
 *Hentikan pompa sekunder CDU hanya setelah suhu fluida turun di bawah 30,0°C. Pastikan tekanan diferensial meluruh mulus ke 0,0 kPa.* 
 Stempel Waktu: ____________________ Paraf: ________ 

- [ ] **LANGKAH 05: Isolasi Manifold Sekunder & Lepaskan Selang** 
 *Tutup katup isolasi manual pasokan dan balik sekunder. Buang tekanan head statis residual melalui katup pembuangan ke ember penampung. Lepaskan kopling lepas-cepat.* 
 *(KRITIS: Jika langkah ini dicentang sebelum Langkah 04, lembar ini seketika BATAL.)* 
 Stempel Waktu: ____________________ Paraf: ________ 

### 2. Verifikasi Arsip Data Kriptografis
- [ ] Telemetri CSV mentah 1 detik bank beban diekspor dan diverifikasi: **YA / TIDAK** 
- [ ] Log tren BMS / PLC 1 detik diekspor di semua stempel waktu pengujian: **YA / TIDAK** 
- [ ] Tangkapan termografi inframerah beresolusi tinggi dan foto digital diarsipkan: **YA / TIDAK** 
- Lokasi Penyimpanan Aman Primer: __________________________________________________ 
- Lokasi Offline Redundan Sekunder: ____________________________________________ 
- Checksum SHA-256 Arsip Master: ________________________________________________ 

### 3. Inventaris Demobilisasi & Pemulihan Fasilitas
- [ ] Semua kopling lepas-cepat dan selang dihitung terhadap inventaris Lembar 1: **NOL HILANG** 
- [ ] Tutup debu pelindung berperingkat tekanan dipasang pada semua port pasokan dan balik manifold: **YA / TIDAK** 
- [ ] Katup fasilitas permanen, pemutus arus, dan setpoint BMS dipulihkan ke garis dasar: **YA / TIDAK** 
- [ ] Ubin lantai terangkat aula data, stringer pedestal, dan baki kabel diperiksa kebersihannya: **YA / TIDAK** 

**PENILAIAN PENUTUPAN LEMBAR 5**: [ ] **PEMADAMAN DIEKSEKUSI DALAM KEPATUHAN KETAT** 
**Tanda Tangan Pimpinan Pengujian Berwenang**: ________________________ **Tanggal**: __________________ 
**Tanda Tangan Pimpinan Insinyur Elektro**: ________________________ **Tanggal**: __________________ 

---

## Lembar 6. Kurva Pompa Garis Dasar Dingin & Resistansi Loop Tanpa Panas

**Nama Proyek**: __________________________ **ID Aula Data / Ruangan**: __________________________ 
**Label Aset CDU**: __________________________ **Label Pompa (A/B)**: ______________________________ 
**Pimpinan Insinyur Mesin**: ____________________ **Teknisi Pengukuran**: __________________________ 
**Kimia Fluida Sekunder**: 25,0% PG **Suhu Fluida Terukur**: __________ °C (Target: 20,0°C ± 1,0 K) 

*Perintah panas harus di-interlock ke 0 kW. Frekuensi VFD harus dikunci dalam penggantian manual pada 50,0 Hz (atau 60,0 Hz).*

### 1. Verifikasi Kontrol Garis Dasar Prasyarat
- [ ] Pemanas listrik diverifikasi terkunci mati (*lock-out*); beban listrik aktif adalah 0,0 kW: **TERKONFIRMASI** 
- [ ] Modulasi tekanan diferensial VFD otomatis dinonaktifkan: **PENGUNCIAN MANUAL TERKONFIRMASI** 
- [ ] Frekuensi VFD operasi ditetapkan dan diverifikasi melalui takometer/register terkalibrasi: **50,0 Hz** 
- [ ] Konsentrasi glikol sekunder terkonfirmasi refraktometer: **25,0% ± 0,5% PG** 

### 2. Data Hidrolik Pencekikan Katup Empat Titik

| LANGKAH PENCEKIKAN | POSISI PERINTAH KATUP | ALIRAN TERUKUR Q (m³/h) | ALIRAN TERUKUR Q (LPM) | HEAD POMPA ΔP_pump (kPa) | dP MANIFOLD ΔP_man (kPa) | ARUS MOTOR (A) | DAYA VFD (kW) | MODULASI KONTROL MATI? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Titik 1: Aliran Maks** | 100% Terbuka Penuh | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YA (Terkunci) |
| **Titik 2: Aliran 80%** | Dicekik (~80%) | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YA (Terkunci) |
| **Titik 3: Aliran 60%** | Dicekik (~60%) | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YA (Terkunci) |
| **Titik 4: Aliran 40%** | Dicekik (~40%) | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YA (Terkunci) |

### 3. Audit Penerimaan Kurva Hidrolik
- Referensi Kurva Pompa Pengajuan Bersertifikat Vendor: ID Dokumen: ____________________ Rev: ______ 
- Deviasi Head vs Aliran Titik 1 dari Kurva Bersertifikat: __________ % (Batas: ≤ ± 5,0%) 
- Deviasi Head vs Aliran Titik 2 dari Kurva Bersertifikat: __________ % (Batas: ≤ ± 5,0%) 
- Deviasi Head vs Aliran Titik 3 dari Kurva Bersertifikat: __________ % (Batas: ≤ ± 5,0%) 
- Deviasi Head vs Aliran Titik 4 dari Kurva Bersertifikat: __________ % (Batas: ≤ ± 5,0%) 
- Kenaikan Suhu Fluida Sekunder Maksimum Selama Pengujian: __________ K (Batas: ≤ 0,5 K) 

**PENILAIAN GARIS DASAR LEMBAR 6**: [ ] **KURVA POMPA DINGIN DITERIMA & DIARSIPKAN** [ ] **KURVA DI LUAR TOLERANSI** 
**Tanda Tangan Pimpinan Insinyur Mesin**: ________________________ **Tanggal**: __________________ 
**Tanda Tangan Teknisi Pengujian**: ____________________________ **Tanggal**: __________________ 

---

## Lembar 7. Logika Kontrol Otonom CDU & Audit Antarmuka Pengawas

**Nama Proyek**: __________________________ **ID Aula Data / Ruangan**: __________________________ 
**Label Aset CDU**: __________________________ **Ref Dokumen Logika Vendor**: __________________________ 
**Pimpinan Insinyur Kontrol**: ______________________ **Insinyur Komisioning Vendor**: ________________ 

*Pengajuan logika kontrol vendor harus dilampirkan pada lembar ini. Jika dokumentasi tidak ada, tandai TIDAK DIDEMONSTRASIKAN.*

### 1. Mode Kegagalan Logika Kontrol Otonom

| SKENARIO KONTROL | SPESIFIKASI LOGIKA VENDOR YANG DIHARAPKAN | HASIL SIMULASI FISIK | PENILAIAN AUDIT |
| :--- | :--- | :--- | :--- |
| **Sensor Suhu Kontrol Primer Terputus** | Pengontrol mendeteksi loop sirkuit terbuka; menghasilkan alarm kritis; menolak sensor dan secara otomatis beralih ke sensor imersi sekunder redundan. | Pengontrol memberi alarm seketika; beralih ke TT-202; nol perburuan katup teramati. | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Jalur Sensor Tekanan Diferensial Primer Putus**| Pengontrol menandai hilangnya sinyal pemancar (4-20mA di luar rentang); mengunci VFD pada frekuensi stabil terakhir; mencegah pompa runout. | Alarm ditampilkan; VFD mempertahankan 48,2 Hz stabil; tekanan diferensial terjaga. | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Daya Pengontrol PLC Operasi Terputus** | Sistem memasuki kondisi aman-gagal perangkat keras: katup modulasi primer gagal 100% terbuka; pompa sekunder yang berjalan berlanjut pada frekuensi jala-jala maksimum. | TCV kembali dengan pegas ke 100% terbuka; pompa terus bersirkulasi; tidak ada trip termal. | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Gangguan Beban Lebih Inverter Internal VFD Pompa**| Output inverter trip; kontak bantu memberi sinyal ke PLC CDU; pompa siaga menyala dan mencapai tekanan dalam ≤ 1,5 s. | Pompa siaga P-1B menyala dalam 1,1 detik; tekanan loop tertahan ≥ 120 kPa. | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Kabel Komunikasi Drive Modbus-RTU Putus** | Drive kehilangan sinyal detak jantung komunikasi serial; menahan kecepatan terakhir yang diperintahkan; CDU mencatat alarm kehilangan komunikasi tanpa menghentikan loop. | Drive mempertahankan 50,0 Hz; alarm komunikasi dicatat pada HMI; aliran fluida berlanjut. | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Jaringan Master Kontrol-Grup Putus** | Unit mendeteksi hilangnya token master grup; pengontrol lokal otonom mengambil alih pelacakan loop PID mandiri secara mulus. | Unit bertransisi ke mode lokal dalam 800 ms; suhu pasokan sekunder dipertahankan 40,0°C. | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Kehilangan Daya 24V Aktuator Listrik** | Pegas pengembali internal aktuator atau superkapasitor menggerakkan mekanisme katup ke posisi 100% terbuka penuh. | Katup digerakkan secara mekanis ke 100% terbuka; air dingin primer maksimum tersedia. | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |
| **Trip Pelepasan Tekanan Tinggi Tangki Ekspansi**| Katup pelepas terbuka pada 6,0 bar; sakelar tekanan tinggi trip; CDU menghentikan pompa pengisi dan mengirim alarm prioritas tinggi. | Sakelar trip pada 5,8 bar; pompa pengisi terkunci; alarm diterima oleh BMS. | [ ] LULUS [ ] GAGAL [ ] TIDAK DIDEMONSTRASIKAN |

### 2. Isolasi Bagian Header Ring (Hanya jika Sekunder Berupa Topologi Ring)
- [ ] Katup isolasi cabang sekunder terdekat ditutup dan dibuka kembali: 
 *Stabilitas termal bank beban dipertahankan: **YA / TIDAK** Tekanan pasokan CDU stabil: **YA / TIDAK*** 
- [ ] Katup isolasi cabang sekunder terjauh ditutup dan dibuka kembali: 
 *Stabilitas termal bank beban dipertahankan: **YA / TIDAK** Tekanan pasokan CDU stabil: **YA / TIDAK*** 

### 3. Audit Konsistensi Register Telemetri BMS Pengawas

| PARAMETER TELEMETRI | LABEL TITIK BMS | TAMPILAN LOKAL CDU | REF LAPANGAN TERKALIBRASI | DISKREPANSI TELEMETRI | BATAS AUDIT | PENILAIAN |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Suhu Pasokan Sekunder** | `CDU01_TCS_SUP_T` | 40,10 °C | 40,08 °C | 0,02 K | ≤ ± 0,30 K | **LULUS / GAGAL** |
| **Suhu Balik Sekunder** | `CDU01_TCS_RET_T` | 50,15 °C | 50,12 °C | 0,03 K | ≤ ± 0,30 K | **LULUS / GAGAL** |
| **Laju Aliran Sekunder** | `CDU01_TCS_FLOW` | 115,8 m³/h | 116,1 m³/h | 0,26 % | ≤ ± 2,0% | **LULUS / GAGAL** |
| **Tekanan Pasokan Sekunder**| `CDU01_TCS_SUP_P` | 282,0 kPa | 280,5 kPa | 1,5 kPa | ≤ ± 10,0 kPa| **LULUS / GAGAL** |
| **Posisi TCV Primer** | `CDU01_TCV_POS` | 64,0 % | 64,5 % (Langkah) | 0,5 % | ≤ ± 2,0% | **LULUS / GAGAL** |

**PENILAIAN LOGIKA LEMBAR 7**: [ ] **LOGIKA OTONOM CDU TERSERTIFIKASI** [ ] **KEKURANGAN LOGIKA DICATAT** 
**Tanda Tangan Pimpinan Insinyur Kontrol**: ________________________ **Tanggal**: __________________ 
**Insinyur Komisioning Vendor**: ____________________ **Tanggal**: __________________ 
