Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 9. Jendela Beban Panas

Jendela beban panas termal adalah fase yang paling banyak difoto oleh para pemangku kepentingan. Ini bukan keseluruhan proyek; ini adalah puncak yang diperoleh melalui eksekusi disiplin dari bab-bab sebelumnya.

Dalam kerangka kerja komisioning global, ini adalah **Pengujian Sistem Terintegrasi (IST) Level 5**. Tanggung jawab Anda selama jendela ini adalah mengeksekusi skrip pengujian dinamis yang disetujui dalam urutan ketat, mempertahankan durasi waktu tunggu (*dwell*) yang disiplin, mencatat telemetri berpresisi tinggi, dan menegakkan kriteria penghentian (*stop criteria*) seketika saat ambang batas terlanggar. Ini bukan kesempatan untuk mengimprovisasi prosedur pengujian baru secara mendadak.

![Kurva Pompa Dingin vs Panas](../figures/fig-03-pump-curves-cold-vs-hot.png)

## Skrip 07: Kurva Pompa Garis Dasar Dingin Tanpa Panas

Sebelum memperkenalkan energi termal, Anda harus mengeksekusi Skrip 07 untuk menetapkan garis dasar resistansi hidrolik dari *loop* sekunder.

### Mengapa Garis Dasar Sebelum Panas?
Fluida perpindahan panas sekunder—biasanya 25% Propylene Glycol (PG25) atau air demineralisasi yang diolah—menunjukkan pergeseran viskositas yang signifikan di seluruh rentang suhu operasinya:
- Pada suhu 20,0°C, viskositas kinematik PG25 adalah $\nu ≈ 2,45 mm²/s$ (μ ≈ 2,50 cP).
- Pada suhu 50,0°C, viskositas kinematiknya turun lebih dari 50% menjadi $\nu ≈ 1,15 mm²/s$ (μ ≈ 1,10 cP).

Penurunan viskositas ini mengurangi tegangan geser dinding pipa dan resistansi gesekan turbulen. Untuk laju aliran volumetrik yang identik, penurunan tekanan melintasi manifold sekunder dan fitting lepas-cepat berkurang secara signifikan pada suhu 50°C dibandingkan pada 20°C.

Jika Anda gagal menetapkan garis dasar resistansi hidrolik pada kondisi dingin, Anda tidak dapat memisahkan antara efek resistansi gesekan pemipaan dan efek penipisan viskositas fluida akibat suhu. Jika anomali aliran terjadi di kemudian hari di bawah beban panas penuh, auditor tidak dapat menentukan apakah anomali tersebut berasal dari keausan impeler pompa, penyumbatan pipa, atau penipisan viskositas fluida.

### Protokol Eksekusi untuk Lembar 6
1. **Kunci Mati Modulasi VFD**: Kunci pompa sekunder CDU dalam mode penggantian frekuensi manual (*manual frequency override*) pada 50,0 Hz (atau 60,0 Hz desain nominal). Pelacakan tekanan diferensial otomatis harus diverifikasi telah dinonaktifkan.
2. **Profil Pencekikan Empat Titik**: Cekik katup penyeimbang sekunder utama secara bertahap untuk menetapkan empat titik operasi hidrolik yang berbeda:
 - Titik 1: 100% Terbuka Penuh (Aliran Maksimum)
 - Titik 2: *Setpoint* Aliran Setara 80%
 - Titik 3: *Setpoint* Aliran Setara 60%
 - Titik 4: *Setpoint* Aliran Setara 40%
3. **Catat Head vs Aliran**: Di setiap titik, catat aliran volumetrik Q menggunakan meteran ultrasonik, dan tekanan diferensial ΔP melintasi pompa serta manifold sekunder.
4. **Standar Penerimaan**: Kurva dingin yang terukur harus cocok dengan kurva pompa bersertifikat pabrikan dalam batas ± 5,0%. Suhu fluida harus tetap stabil dalam batas ± 0,5 K di sepanjang pengujian.

![Tangga Termal Terintegrasi dan Waktu Tunggu](../figures/fig-05-thermal-ladder-and-dwell.png)

## Skrip 08: Tangga Beban Panas Termal Bertingkat

Setelah garis dasar hidrolik dingin disetujui, pembebanan termal dimulai di bawah Skrip 08. Tangga termal adalah urutan progresif yang dirancang untuk memverifikasi bahwa distribusi daya fasilitas, penukar panas CDU, *loop* air primer, dan manajemen udara ruang putih (*whitespace*) stabil pada setiap kenaikan beban.

**PARAMETER TAHAPAN TANGGA TERMAL**

| TAHAP | BEBAN TERMAL | kW DESAIN | WAKTU TUNGGU MIN | TUJUAN STABILISASI | LEMBAR REFERENSI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Tahap 25% | 300 kW | 45 menit | Pelacakan TCV awal | Lembar 3 (Salinan 1) |
| 2 | Tahap 50% | 600 kW | 45 menit | Keseimbangan parsial | Lembar 3 (Salinan 2) |
| 3 | Tahap 75% | 900 kW | 45 menit | Audit geser hidrolik | Lembar 3 (Salinan 3) |
| 4 | Tahap 100% | 1200 kW | Perendaman 4,0 jam | Keseimbangan penuh | Lembar 3 (Salinan 4) |
| 5 | Tahap 110% | 1320 kW | 60 menit | Uji stres beban lebih | Lembar 3 (Salinan 5) |

### Kriteria Waktu Tunggu Keseimbangan Termal
Jangan pernah melangkah ke tahap beban berikutnya hanya berdasarkan waktu yang berlalu. Suatu tahap beban dianggap selesai hanya jika sistem telah mencapai **keseimbangan termal** yang terverifikasi:

$$\left| \frac{dT_{\text{supply}}}{dt} \right| \le 0,20\,\text{K} \text{ selama jendela kontinu 10 menit}$$

Jika suhu pasokan sekunder masih naik atau berosilasi akibat katup kontrol yang berburu (*hunting*), waktu tunggu harus diperpanjang. Melangkah ke anak tangga termal yang lebih tinggi dengan *loop* kontrol yang tidak stabil akan melipatgandakan ketidakstabilan termal dan berisiko memicu trip keselamatan suhu tinggi.

### Rekonsiliasi Keseimbangan Panas Entalpi
Pada setiap langkah termal, rekonsiliasikan energi listrik aktif yang dikonsumsi terhadap panas termal yang diserap oleh fluida sekunder:

$$Q_{\text{liquid}} = \dot{m} \cdot c_p(T_{\text{bulk}}) \cdot (T_{\text{return}} - T_{\text{supply}})$$

Di mana:
- ṁ = ρ · Q adalah laju aliran massa (kg/s).
- c_p adalah kapasitas panas spesifik PG25 yang dievaluasi pada suhu fluida ruah (*bulk fluid temperature*) (kJ/kg·K).
- P_elec adalah daya aktif 3-fasa yang diukur oleh meter referensi Kelas 0,2 (kW).

**Standar Penerimaan**: Rasio penutupan keseimbangan panas $\eta = \frac{Q_{\text{liquid}}}{P_{\text{elec}}}$ harus mempertahankan:

$$97,0\% \le \eta \le 101,5\%$$

Rasio penutupan di bawah 97,0% mengindikasikan kesalahan pengukuran yang signifikan (seperti densitas fluida yang tidak akurat, konsentrasi glikol yang salah, atau flowmeter yang tidak disetel) atau pelepasan panas konvektif yang berlebihan ke udara ruang putih. Rasio penutupan yang melebihi 101,5% secara termodinamika tidak mungkin dan menandakan adanya kesalahan kalibrasi.

### Inspeksi Termografi Inframerah (IR)
Pada menit ke-30 saat waktu tunggu beban penuh 100%, lakukan survei termografi inframerah pada semua peralatan distribusi listrik:
- Pindai semua *lug* pemutus arus PDU hulu, sambungan kotak sadapan *busway*, terminal kontaktor, dan stopkontak daya bank beban.
- **Standar Penerimaan**: Tidak ada terminal listrik yang boleh melebihi suhu absolut **75,0°C**, dan ketidakseimbangan suhu antarfasa melintasi terminasi yang identik tidak boleh melebihi **5,0 K**. Terminal kendur yang menghasilkan titik panas termal dicatat pada Lembar 3 sebagai cacat kelistrikan.

### Langkah Beban Lebih dan Transien Skrip 08
- **Uji Margin Beban Lebih 110%**: Mengoperasikan sistem pada 1320 kW selama 60 menit untuk mendemonstrasikan bahwa pemutus arus fasilitas, *busbar*, dan kapasitas pendinginan primer mempertahankan margin operasional yang aman di atas kapasitas pengenal.
- **Uji Kejutan Termal Perubahan Bertahap**: Memulai pelepasan beban mendadak dari $100% \to 30%$ dalam satu langkah, menahannya selama 30 menit, dan kemudian menaikkannya kembali secara tiba-tiba dari $30% \to 100%$. Ini memvalidasi bahwa katup modulasi primer CDU (TCV-101) dapat mengikuti ayunan beban kerja komputasi yang cepat tanpa berburu (*hunting*) atau menyebabkan lonjakan suhu pasokan sekunder yang berlebihan (ΔT_overshoot ≤ 1,5 K).

## Keseragaman Aliran Sekunder Multi-Rak

Selama waktu tunggu beban penuh 100%, ukur laju aliran melalui setiap bank beban individual di sepanjang baris manifold. Sebagaimana diperlihatkan pada Gambar 04, sistem pemipaan *direct-return* cenderung membuat rak terjauh kelaparan aliran, sedangkan *loop* *reverse-return* (Tichelmann) mempertahankan penurunan tekanan yang seragam.

**Standar Penerimaan**:
1. Penyimpangan aliran bank beban individual dari nilai rata-rata tidak boleh melebihi **± 7,5%**.
2. Koefisien Variasi di seluruh baris (*Coefficient of Variation* - $CV = \frac{\sigma}{\mu} \cdot 100\%$) di seluruh sepuluh bank beban harus memenuhi:

$$CV \le 5,0\%$$

## Penegakan Margin Titik Embun (Dew Point)

Di sepanjang semua pengujian termal, pantau kelembapan relatif dan suhu bola kering (*dry-bulb temperature*) aula data sekitar. Hitung titik embun udara secara *real-time* (T_dew).

**Standar Penerimaan**: Suhu pasokan sekunder T_supply harus terus-menerus melebihi titik embun ruangan minimal sebesar **2,0 K**:

$$T_{\text{supply}} - T_{\text{dew}} \ge 2,0\,\text{K}$$

Jika suhu pasokan sekunder turun mendekati titik embun, logika katup pencampur CDU mengalami kerusakan, yang menciptakan bahaya kondensasi langsung di sepanjang pemipaan manifold yang tidak berinsulasi.

## Keputusan yang Harus Dicatat Sebelum Mulai Pengujian

- Kurva pompa garis dasar dingin tanpa panas yang disaksikan, diarsipkan pada Lembar 6.
- Log tangga termal bertingkat yang lengkap (Lembar 3-1 hingga 3-5).
- Rasio penutupan keseimbangan panas entalpi yang dihitung di setiap langkah (≥ 97,0%).
- Log survei termografi inframerah, mencatat suhu terminasi puncak.
- Perhitungan keseragaman aliran multi-rak (CV ≤ 5,0%).
- Verifikasi terus-menerus bahwa suhu pendingin sekunder tetap ≥ 2,0 K di atas titik embun aula.
