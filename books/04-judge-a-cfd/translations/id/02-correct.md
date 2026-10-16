Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 2. Bagaimana Pengukuran Diizinkan Mengubah Model

## Prinsip Verifikasi Pengukuran Lapangan terhadap Model Numerik

Dalam evaluasi dinamika fluida komputasi (CFD) untuk aliran udara dan termal pusat data, **Indeks Konvergensi Grid (GCI), pemilihan model turbulensi RANS, dan kalibrasi kondisi batas berbasis bukti fisik** merupakan disiplin rekayasa inti yang menentukan keandalan fasilitas. Laporan simulasi yang diserahkan tanpa tolok ukur instrumen fisik terkalibrasi hanyalah hipotesis matematis di atas kertas dan tidak boleh ditandatangani sebagai bukti penerimaan operasional.

![2. Bagaimana Pengukuran Diizinkan Mengubah Model](../figures/fig-01-cfd-audit-lifecycle.png)

$$\text{MAE} = \frac{1}{N} \sum_{i=1}^{N} \left| T_{\text{sim}, i} - T_{\text{meas}, i} \right|$$

Tim verifikasi lapangan wajib mengambil data Galat mutlak rata-rata $\text{MAE} \le 1.0\,\text{K}$, $\text{RMSE} \le 1.5\,\text{K}$, dan deviasi lokal maksimum $|\Delta T_{\max}| \le 2.0\,\text{K}$ secara serentak dan mencocokkannya satu per satu dengan koordinat probe numerik di dalam solver ($\pm 50\,\text{mm}$). Memeriksa kecocokan suhu saja tanpa memverifikasi laju aliran udara dan tekanan diferensial ($\Delta P$) akan menyembunyikan cacat model di mana daya panas dan aliran udara sama-sama diremehkan.

> *"Laporan CFD tanpa tolok ukur pengukuran fisik lapangan (Sheet 1) dan keterbukaan kondisi batas numerik (Sheet 2) harus diperlakukan sebagai hipotesis desain yang belum terverifikasi dan tidak boleh menjadi dasar persetujuan kapasitas."*

## Persamaan Pengatur Termohidraulik dan Toleransi Metrologi

Pada klaster AI kepadatan tinggi dan ruang hibrida (pendinginan cair + udara), hanya sisa panas sensibel ($Q_{\text{air}}$) setelah mengurangi penyerapan entalpi loop cairan sekunder ($Q_{\text{liquid}}$) dari daya listrik aktif ($P_{\text{elec}}$) yang masuk ke udara ruangan. Memasukkan angka pelat nama PSU secara langsung akan menyuntikkan 40% hingga 80% panas semu ke dalam simulasi.

$$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \left( T_{\text{sim}, i} - T_{\text{meas}, i} \right)^2}$$

| Parameter Audit | Instrumen Fisik / Indeks Numerik | Kriteria Lulus (Toleransi) | Pemicu Penolakan (Gagal) |
| :--- | :--- | :--- | :--- |
| **Suhu Hisap Rak (Pohon 3-Tingkat)** | $T_1 (0.3\,\text{m}), T_2 (1.2\,\text{m}), T_3 (1.8\,\text{m})$ | $\text{MAE} \le 1.0\,\text{K}, \text{RMSE} \le 1.5\,\text{K}$ | Deviasi lokal $|\Delta T_{\max}| > 2.0\,\text{K}$ atau sensor tunggal |
| **Aliran Ubin & Tekanan Bawah Lantai** | $Q_{\text{tile}}$ dan $\Delta P_{\text{plenum}}$ | Sesuai balometer terkompensasi $\pm 10\%$ | Aliran balik Venturi ($\Delta P_{\text{tile}} \le 0\,\text{Pa}$) diabaikan |
| **Batas Beban Panas (Hibrida)** | $Q_{\text{air}} = P_{\text{elec}} - Q_{\text{liquid}}$ | Catatan serentak meter PDU 0.5S & kalor CDU | Penggunaan langsung angka pelat nama (Nameplate W) |
| **Indeks Aerodinamika Nir-Dimensi** | $\text{SHI}, \text{RHI}, \text{RCI}_{\text{HI}}$ | $\text{SHI} < 0.15, \text{RHI} > 0.85, \text{RCI}_{\text{HI}} \ge 96\%$ | Manipulasi rentang warna untuk menyembunyikan titik panas |

Selain itu, di dekat hembusan CRAH dengan kecepatan horizontal bawah lantai $v_{\text{plenum}} > 4.5\,\text{m/s}$, kenaikan tekanan dinamis ($\frac{1}{2}\rho v^2$) menurunkan tekanan statis lokal sehingga ubin pertama menyedot udara hangat lorong ke bawah lantai. Tegakkan aturan **Larangan manipulasi koefisien lokal (fudge factor) yang hanya bertujuan menyembunyikan titik panas pada satu rak** secara ketat pada setiap tinjauan.

## Respons Transien, Independensi Grid, dan Protokol Audit

Gambar kontur kondisi tunak (steady-state) saja tidak dapat membuktikan waktu bertahan termal ($t_{\text{ride}}$) saat kegagalan pendingin. Simulasi transien kegagalan CRAH $N-1$ atau mulai ulang chiller ($180\sim 300\,\text{s}$) wajib menggabungkan kapasitas panas efektif sasis server dan lonjakan kecepatan kipas internal server (hukum pangkat tiga $P_{\text{fan}} \propto N^3$).

$$\text{NMBE} = \frac{\sum_{i=1}^{N} \left( T_{\text{sim}, i} - T_{\text{meas}, i} \right)}{N \cdot \bar{T}_{\text{meas}}} \times 100\%$$

1. **Kalibrasi Instrumen & Kunci Koordinat**: Catat nomor sertifikat kalibrasi aktif untuk semua probe Pt100, mikromanometer, dan balometer pada Sheet 1, serta selaraskan tanggal revisi CAD dengan waktu pengukuran.
2. **Verifikasi Indeks Konvergensi Grid (GCI)**: Pastikan perubahan suhu hisap utama antara grid kasar dan halus kurang dari $0.25\,\text{K}$ pada Sheet 2.
3. **Tanda Tangan Keputusan Bersyarat**: Nyatakan batas beban dan aliran udara yang terverifikasi secara tertulis dan tolak setiap permintaan untuk melewati komisioning fisik.

$$\Delta_{\max} = \max_{1 \le i \le N} \left| T_{\text{sim}, i} - T_{\text{meas}, i} \right|$$

$$\text{MAE}_T = \frac{1}{N} \sum_{i=1}^{N} \left| T_{i,\text{sim}} - T_{i,\text{meas}} \right| \le 1.5\,\text{K}$$

$$\text{RMSE}_T = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \left( T_{i,\text{sim}} - T_{i,\text{meas}} \right)^2} \le 2.0\,\text{K}$$

$$\text{MBE}_T = \frac{1}{N} \sum_{i=1}^{N} \left( T_{i,\text{sim}} - T_{i,\text{meas}} \right) \in [-0.8\,\text{K}, \, +0.8\,\text{K}]$$

$$\varepsilon_{Q,\text{CRAH}} = \frac{\left| \sum Q_{\text{CRAH, sim}} - \sum Q_{\text{CRAH, meas}} \right|}{\sum Q_{\text{CRAH, meas}}} \le 5.0\%$$

$$\text{GCI}_{\text{fine}} = \frac{1.25 \cdot \left| \frac{T_{\text{fine}} - T_{\text{coarse}}}{T_{\text{fine}}} \right|}{r^p - 1} \le 2.0\%$$

$$\text{Ri} = \frac{g \beta \Delta T L_{\text{char}}}{v_{\text{char}}^2}$$

$$\Delta P_{\text{chassis}} = \left( \alpha_i \mu v + \frac{1}{2} \beta_i \rho v^2 \right) L_{\text{chassis}}$$

## Keputusan yang Harus Dicatat

- Pencatatan fokus audit ruang data (Indeks Konvergensi Grid (GCI), pemilihan model turbulensi RANS, dan kalibrasi kondisi batas berbasis bukti fisik) dan tanggal pembekuan geometri CAD.
- Verifikasi galat antara pengukuran lapangan (Galat mutlak rata-rata $\text{MAE} \le 1.0\,\text{K}$, $\text{RMSE} \le 1.5\,\text{K}$, dan deviasi lokal maksimum $|\Delta T_{\max}| \le 2.0\,\text{K}$) dan probe numerik CFD (MAE $\le 1.0\,\text{K}$).
- Bukti perhitungan pengurangan daya CDU cair dari daya aktif PDU pada rak hibrida.
- Penolakan langsung bila ditemukan kondisi gagal (Larangan manipulasi koefisien lokal (fudge factor) yang hanya bertujuan menyembunyikan titik panas pada satu rak) serta penandatanganan Sheet 1 dan Sheet 2.
