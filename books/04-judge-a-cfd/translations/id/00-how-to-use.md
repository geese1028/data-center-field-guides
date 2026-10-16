Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 0. Cara Menggunakan Buku Ini

## Prinsip Verifikasi Pengukuran Lapangan terhadap Model Numerik

Dalam evaluasi dinamika fluida komputasi (CFD) untuk aliran udara dan termal pusat data, **Dua lembar audit CFD pusat data (Sheet 1: Tolok Ukur Pengukuran Lapangan & Sheet 2: Audit Batas Numerik) dan batas keputusan operasional** merupakan disiplin rekayasa inti yang menentukan keandalan fasilitas. Laporan simulasi yang diserahkan tanpa tolok ukur instrumen fisik terkalibrasi hanyalah hipotesis matematis di atas kertas dan tidak boleh ditandatangani sebagai bukti penerimaan operasional.

$$\nabla \cdot (\rho \vec{u}) = 0$$

Tim verifikasi lapangan wajib mengambil data Pohon suhu hisap 3-tingkat terkalibrasi ($0.3, 1.2, 1.8\,\text{m}$), daya aktif PDU ($\text{kW}$), dan tekanan diferensial ubin ($\Delta P_{\text{tile}}$) secara serentak dan mencocokkannya satu per satu dengan koordinat probe numerik di dalam solver ($\pm 50\,\text{mm}$). Memeriksa kecocokan suhu saja tanpa memverifikasi laju aliran udara dan tekanan diferensial ($\Delta P$) akan menyembunyikan cacat model di mana daya panas dan aliran udara sama-sama diremehkan.

> *"Laporan CFD tanpa tolok ukur pengukuran fisik lapangan (Sheet 1) dan keterbukaan kondisi batas numerik (Sheet 2) harus diperlakukan sebagai hipotesis desain yang belum terverifikasi dan tidak boleh menjadi dasar persetujuan kapasitas."*

## Persamaan Pengatur Termohidraulik dan Toleransi Metrologi

Pada klaster AI kepadatan tinggi dan ruang hibrida (pendinginan cair + udara), hanya sisa panas sensibel ($Q_{\text{air}}$) setelah mengurangi penyerapan entalpi loop cairan sekunder ($Q_{\text{liquid}}$) dari daya listrik aktif ($P_{\text{elec}}$) yang masuk ke udara ruangan. Memasukkan angka pelat nama PSU secara langsung akan menyuntikkan 40% hingga 80% panas semu ke dalam simulasi.

$$\rho (\vec{u} \cdot \nabla)\vec{u} = -\nabla p + \nabla \cdot \left[ (\mu + \mu_t) \left( \nabla \vec{u} + (\nabla \vec{u})^T \right) \right] + \rho \vec{g} \beta (T - T_{\text{ref}})$$

| Parameter Audit | Instrumen Fisik / Indeks Numerik | Kriteria Lulus (Toleransi) | Pemicu Penolakan (Gagal) |
| :--- | :--- | :--- | :--- |
| **Suhu Hisap Rak (Pohon 3-Tingkat)** | $T_1 (0.3\,\text{m}), T_2 (1.2\,\text{m}), T_3 (1.8\,\text{m})$ | $\text{MAE} \le 1.0\,\text{K}, \text{RMSE} \le 1.5\,\text{K}$ | Deviasi lokal $|\Delta T_{\max}| > 2.0\,\text{K}$ atau sensor tunggal |
| **Aliran Ubin & Tekanan Bawah Lantai** | $Q_{\text{tile}}$ dan $\Delta P_{\text{plenum}}$ | Sesuai balometer terkompensasi $\pm 10\%$ | Aliran balik Venturi ($\Delta P_{\text{tile}} \le 0\,\text{Pa}$) diabaikan |
| **Batas Beban Panas (Hibrida)** | $Q_{\text{air}} = P_{\text{elec}} - Q_{\text{liquid}}$ | Catatan serentak meter PDU 0.5S & kalor CDU | Penggunaan langsung angka pelat nama (Nameplate W) |
| **Indeks Aerodinamika Nir-Dimensi** | $\text{SHI}, \text{RHI}, \text{RCI}_{\text{HI}}$ | $\text{SHI} < 0.15, \text{RHI} > 0.85, \text{RCI}_{\text{HI}} \ge 96\%$ | Manipulasi rentang warna untuk menyembunyikan titik panas |

Selain itu, di dekat hembusan CRAH dengan kecepatan horizontal bawah lantai $v_{\text{plenum}} > 4.5\,\text{m/s}$, kenaikan tekanan dinamis ($\frac{1}{2}\rho v^2$) menurunkan tekanan statis lokal sehingga ubin pertama menyedot udara hangat lorong ke bawah lantai. Tegakkan aturan **Penolakan segera atas persetujuan kapasitas yang hanya didasarkan pada gambar kontur warna CFD tanpa verifikasi fisik** secara ketat pada setiap tinjauan.

## Respons Transien, Independensi Grid, dan Protokol Audit

Gambar kontur kondisi tunak (steady-state) saja tidak dapat membuktikan waktu bertahan termal ($t_{\text{ride}}$) saat kegagalan pendingin. Simulasi transien kegagalan CRAH $N-1$ atau mulai ulang chiller ($180\sim 300\,\text{s}$) wajib menggabungkan kapasitas panas efektif sasis server dan lonjakan kecepatan kipas internal server (hukum pangkat tiga $P_{\text{fan}} \propto N^3$).

$$\rho c_p (\vec{u} \cdot \nabla T) = \nabla \cdot \left( (k + k_t) \nabla T \right) + q'''_{\text{source}}$$

1. **Kalibrasi Instrumen & Kunci Koordinat**: Catat nomor sertifikat kalibrasi aktif untuk semua probe Pt100, mikromanometer, dan balometer pada Sheet 1, serta selaraskan tanggal revisi CAD dengan waktu pengukuran.
2. **Verifikasi Indeks Konvergensi Grid (GCI)**: Pastikan perubahan suhu hisap utama antara grid kasar dan halus kurang dari $0.25\,\text{K}$ pada Sheet 2.
3. **Tanda Tangan Keputusan Bersyarat**: Nyatakan batas beban dan aliran udara yang terverifikasi secara tertulis dan tolak setiap permintaan untuk melewati komisioning fisik.

$$\left| \frac{\partial T_{\text{return, CRAH}}}{\partial t} \right| \le 0.15\,\text{K / 15 min}, \qquad \left| \frac{\partial P_{\text{PDU, total}}}{\partial t} \right| \le 2.0\% \text{ / 15 min}$$

## Keputusan yang Harus Dicatat

- Pencatatan fokus audit ruang data (Dua lembar audit CFD pusat data (Sheet 1: Tolok Ukur Pengukuran Lapangan & Sheet 2: Audit Batas Numerik) dan batas keputusan operasional) dan tanggal pembekuan geometri CAD.
- Verifikasi galat antara pengukuran lapangan (Pohon suhu hisap 3-tingkat terkalibrasi ($0.3, 1.2, 1.8\,\text{m}$), daya aktif PDU ($\text{kW}$), dan tekanan diferensial ubin ($\Delta P_{\text{tile}}$)) dan probe numerik CFD (MAE $\le 1.0\,\text{K}$).
- Bukti perhitungan pengurangan daya CDU cair dari daya aktif PDU pada rak hibrida.
- Penolakan langsung bila ditemukan kondisi gagal (Penolakan segera atas persetujuan kapasitas yang hanya didasarkan pada gambar kontur warna CFD tanpa verifikasi fisik) serta penandatanganan Sheet 1 dan Sheet 2.
