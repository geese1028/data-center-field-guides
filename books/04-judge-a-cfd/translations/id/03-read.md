Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 3. Aerodinamika dan Cara Membaca Laporan CFD

## Prinsip Verifikasi Pengukuran Lapangan terhadap Model Numerik

Dalam evaluasi dinamika fluida komputasi (CFD) untuk aliran udara dan termal pusat data, **Indeks panas pasokan ($\text{SHI} < 0.15$), indeks panas balik ($\text{RHI} > 0.85$), indeks pendinginan rak ($\text{RCI}_{\text{HI}} \ge 96\%$), dan bilangan Archimedes ($\text{Ar}$)** merupakan disiplin rekayasa inti yang menentukan keandalan fasilitas. Laporan simulasi yang diserahkan tanpa tolok ukur instrumen fisik terkalibrasi hanyalah hipotesis matematis di atas kertas dan tidak boleh ditandatangani sebagai bukti penerimaan operasional.

![3. Aerodinamika dan Cara Membaca Laporan CFD](../figures/fig-02-underfloor-plenum-hydraulics.png)

$$P_{\text{total}} = P_{\text{static}} + \frac{1}{2} \rho v^2$$

Tim verifikasi lapangan wajib mengambil data Interaksi kurva kipas server $P$-$Q$ dengan tekanan diferensial lorong ($+2.5\,\text{Pa}$ hingga $+12.0\,\text{Pa}$) secara serentak dan mencocokkannya satu per satu dengan koordinat probe numerik di dalam solver ($\pm 50\,\text{mm}$). Memeriksa kecocokan suhu saja tanpa memverifikasi laju aliran udara dan tekanan diferensial ($\Delta P$) akan menyembunyikan cacat model di mana daya panas dan aliran udara sama-sama diremehkan.

> *"Laporan CFD tanpa tolok ukur pengukuran fisik lapangan (Sheet 1) dan keterbukaan kondisi batas numerik (Sheet 2) harus diperlakukan sebagai hipotesis desain yang belum terverifikasi dan tidak boleh menjadi dasar persetujuan kapasitas."*

## Persamaan Pengatur Termohidraulik dan Toleransi Metrologi

Pada klaster AI kepadatan tinggi dan ruang hibrida (pendinginan cair + udara), hanya sisa panas sensibel ($Q_{\text{air}}$) setelah mengurangi penyerapan entalpi loop cairan sekunder ($Q_{\text{liquid}}$) dari daya listrik aktif ($P_{\text{elec}}$) yang masuk ke udara ruangan. Memasukkan angka pelat nama PSU secara langsung akan menyuntikkan 40% hingga 80% panas semu ke dalam simulasi.

![3. Aerodinamika dan Cara Membaca Laporan CFD](../figures/fig-03-containment-leakage-aerodynamics.png)

$$\left| \frac{\sum \dot{m}_{\text{supply}} - \sum \dot{m}_{\text{exhaust}}}{\sum \dot{m}_{\text{supply}}} \right| \times 100\% \le 0.10\%$$

| Parameter Audit | Instrumen Fisik / Indeks Numerik | Kriteria Lulus (Toleransi) | Pemicu Penolakan (Gagal) |
| :--- | :--- | :--- | :--- |
| **Suhu Hisap Rak (Pohon 3-Tingkat)** | $T_1 (0.3\,\text{m}), T_2 (1.2\,\text{m}), T_3 (1.8\,\text{m})$ | $\text{MAE} \le 1.0\,\text{K}, \text{RMSE} \le 1.5\,\text{K}$ | Deviasi lokal $|\Delta T_{\max}| > 2.0\,\text{K}$ atau sensor tunggal |
| **Aliran Ubin & Tekanan Bawah Lantai** | $Q_{\text{tile}}$ dan $\Delta P_{\text{plenum}}$ | Sesuai balometer terkompensasi $\pm 10\%$ | Aliran balik Venturi ($\Delta P_{\text{tile}} \le 0\,\text{Pa}$) diabaikan |
| **Batas Beban Panas (Hibrida)** | $Q_{\text{air}} = P_{\text{elec}} - Q_{\text{liquid}}$ | Catatan serentak meter PDU 0.5S & kalor CDU | Penggunaan langsung angka pelat nama (Nameplate W) |
| **Indeks Aerodinamika Nir-Dimensi** | $\text{SHI}, \text{RHI}, \text{RCI}_{\text{HI}}$ | $\text{SHI} < 0.15, \text{RHI} > 0.85, \text{RCI}_{\text{HI}} \ge 96\%$ | Manipulasi rentang warna untuk menyembunyikan titik panas |

Selain itu, di dekat hembusan CRAH dengan kecepatan horizontal bawah lantai $v_{\text{plenum}} > 4.5\,\text{m/s}$, kenaikan tekanan dinamis ($\frac{1}{2}\rho v^2$) menurunkan tekanan statis lokal sehingga ubin pertama menyedot udara hangat lorong ke bawah lantai. Tegakkan aturan **Deteksi manipulasi skala legenda warna ($15^\circ\text{C}\sim 45^\circ\text{C}$) yang menyamarkan pelanggaran batas ASHRAE** secara ketat pada setiap tinjauan.

## Respons Transien, Independensi Grid, dan Protokol Audit

Gambar kontur kondisi tunak (steady-state) saja tidak dapat membuktikan waktu bertahan termal ($t_{\text{ride}}$) saat kegagalan pendingin. Simulasi transien kegagalan CRAH $N-1$ atau mulai ulang chiller ($180\sim 300\,\text{s}$) wajib menggabungkan kapasitas panas efektif sasis server dan lonjakan kecepatan kipas internal server (hukum pangkat tiga $P_{\text{fan}} \propto N^3$).

![3. Aerodinamika dan Cara Membaca Laporan CFD](../figures/fig-04-hybrid-liquid-air-thermal-split.png)

$$\text{SHI} = \frac{\delta Q}{Q + \delta Q} = \frac{\sum_{j} \sum_{i} \dot{m}_{i,j}^{\text{rack}} c_p \left( T_{\text{in}, i,j}^{\text{rack}} - T_{\text{ref}}^{\text{supply}} \right)}{\sum_{j} \sum_{i} \dot{m}_{i,j}^{\text{rack}} c_p \left( T_{\text{out}, i,j}^{\text{rack}} - T_{\text{ref}}^{\text{supply}} \right)}$$

1. **Kalibrasi Instrumen & Kunci Koordinat**: Catat nomor sertifikat kalibrasi aktif untuk semua probe Pt100, mikromanometer, dan balometer pada Sheet 1, serta selaraskan tanggal revisi CAD dengan waktu pengukuran.
2. **Verifikasi Indeks Konvergensi Grid (GCI)**: Pastikan perubahan suhu hisap utama antara grid kasar dan halus kurang dari $0.25\,\text{K}$ pada Sheet 2.
3. **Tanda Tangan Keputusan Bersyarat**: Nyatakan batas beban dan aliran udara yang terverifikasi secara tertulis dan tolak setiap permintaan untuk melewati komisioning fisik.

$$\text{RHI} = \frac{Q}{Q + \delta Q} = 1 - \text{SHI}$$

$$\text{RCI}_{\text{HI}} = \left[ 1 - \frac{\sum_{i=1}^{N} \max\left(0, \, T_{\text{in}, i} - T_{\text{max, rec}}\right)}{N \cdot \left( T_{\text{max, allow}} - T_{\text{max, rec}} \right)} \right] \times 100\%$$

$$\text{RCI}_{\text{LO}} = \left[ 1 - \frac{\sum_{i=1}^{N} \max\left(0, \, T_{\text{min, rec}} - T_{\text{in}, i}\right)}{N \cdot \left( T_{\text{min, rec}} - T_{\text{min, allow}} \right)} \right] \times 100\%$$

$$\text{CI}_{\text{cold}, i} = \frac{\sum_{t} \dot{m}_{i, t}^{\text{tile}\to\text{rack}}}{\dot{m}_i^{\text{rack}}}, \qquad \text{CI}_{\text{hot}, i} = \frac{\sum_{c} \dot{m}_{i, c}^{\text{rack}\to\text{CRAH}}}{\dot{m}_i^{\text{rack}}}$$

$$\Delta P_{\text{CAC}} = \frac{\rho_{\text{air}}}{2} \left( \frac{\sum Q_{\text{CRAH}} - \sum Q_{\text{server}}}{C_d \cdot A_{\text{containment\_leak}}} \right)^2 \in [+1.5\,\text{Pa}, \, +5.0\,\text{Pa}]$$

## Keputusan yang Harus Dicatat

- Pencatatan fokus audit ruang data (Indeks panas pasokan ($\text{SHI} < 0.15$), indeks panas balik ($\text{RHI} > 0.85$), indeks pendinginan rak ($\text{RCI}_{\text{HI}} \ge 96\%$), dan bilangan Archimedes ($\text{Ar}$)) dan tanggal pembekuan geometri CAD.
- Verifikasi galat antara pengukuran lapangan (Interaksi kurva kipas server $P$-$Q$ dengan tekanan diferensial lorong ($+2.5\,\text{Pa}$ hingga $+12.0\,\text{Pa}$)) dan probe numerik CFD (MAE $\le 1.0\,\text{K}$).
- Bukti perhitungan pengurangan daya CDU cair dari daya aktif PDU pada rak hibrida.
- Penolakan langsung bila ditemukan kondisi gagal (Deteksi manipulasi skala legenda warna ($15^\circ\text{C}\sim 45^\circ\text{C}$) yang menyamarkan pelanggaran batas ASHRAE) serta penandatanganan Sheet 1 dan Sheet 2.
