Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 13. Pagi Hari Setelahnya: Audit Alarm Malam dan Daftar Shelving

## Integritas Telemetri dan Prinsip 'Bungkam (SILENT)'

Di dalam sistem pemantauan dan kendali pusat data (BMS / EPMS / SCADA / DCIM), **Audit pagi wajib atas seluruh alarm malam, titik yang ditangguhkan (shelved), dan nilai yang dipaksa (forced)** adalah benteng pertahanan pertama terhadap alarm palsu maupun kegagalan tersembunyi. Garis tren atau ubin hijau di layar bukanlah realitas fisik itu sendiri, melainkan klaim perangkat lunak yang melewati rantai komunikasi.

Setiap titik pemantauan wajib memenuhi Aturan melarang penangguhan alarm sementara bertahan lebih dari 24 jam tanpa tiket perbaikan perangkat keras secara ketat. Apabila salah satu dari empat elemen—nilai rekayasa ($V$), waktu UTC tersinkronisasi ($t_{\text{UTC}}$), alamat perangkat keras ($\text{URI}_{\text{source}}$), atau bit kualitas ($Q$)—hilang, rusak, atau basi (Stale), maka titik tersebut wajib menjadi **BUNGKAM (SILENT)** seketika.

> *"Titik data yang tidak memiliki bukti asal perangkat keras, tidak tersinkronisasi waktu, atau tidak berstatus GOOD dilarang membunyikan sirene, dilarang menggerakkan katup otomatis, dan dilarang menutup tiket insiden."*

## Kriteria Kuantitatif Kualitas Sinyal, Histeresis, dan Peredaman Topologi

Di sepanjang jalur akuisisi data dari sensor lapangan hingga basis data pusat, faktor skala rekayasa hanya boleh diterapkan tepat satu kali dengan tetap menyimpan nilai cacah mentah (Raw Counts). Untuk mencegah alarm berkedip (flapping) dan banjir alarm (alarm flood), parameter matematis berikut wajib ditegakkan pada Master Point Sheet:

| Parameter Tata Kelola | Definisi Matematis & Fisik | Kriteria Lulus (Amplop Normal) | Pemicu Isolasi / Penolakan |
| :--- | :--- | :--- | :--- |
| **Tupel 4-Elemen Titik** | $P = \{V, t_{\text{UTC}}, \text{URI}_{\text{source}}, Q\}$ | Lacak penuh hingga terminal P&ID | Titik yatim tanpa alamat atau `Q != GOOD` |
| **Akurasi Jam (SOE / Telemetri)** | IEEE 1588 PTP / Stratum-1 NTP | Relai listrik $\le 1\,\text{ms}$, termal $\le 100\,\text{ms}$ | Waktu sumber ditimpa oleh waktu tiba basis data |
| **Ambang Waktu Basi (Stale)** | $t_{\text{now}} - t_{\text{last\_good}} > 3 T_{\text{poll}}$ | Lepas tahanan nilai lama; ubah ke `0x01 STALE` | Menampilkan nilai lama sebagai hijau saat kabel putus |
| **Histeresis & Waktu Tunggu** | $H = T_{\text{trip}} - T_{\text{clear}} \ge 4\sigma_n$ | Penundaan $\tau_{\text{on}}, \tau_{\text{off}}$ tercatat | Alarm berisik melebihi $\lambda_{\text{alarm}} > 6\,\text{jam}^{-1}$ |

Selain itu, saat menerapkan model analitik pada menara pendingin atau chiller, batasan monotonisitas fisik ($\partial T_{\text{leave}} / \partial N_{\text{fan}} \le 0$) dan aturan nilai minimum seri ($S_{\text{plant}} = \min_k s_k$) wajib dikunci di tingkat PLC. Tegakkan **Siklus pembersihan harian agar jaringan pemantauan tidak mengakumulasi titik buta dari sif ke sif** tanpa kompromi.

## Uji Terima Loop Lapangan (SAT) dan Protokol Audit Harian

Penerimaan sistem pemantauan tidak pernah sah hanya melalui demonstrasi proyektor di ruang rapat, melainkan harus dibuktikan dengan injeksi sinyal fisik dan pemutusan kawat di blok terminal lapangan.

1. **Verifikasi Loop Fisik**: Simulasikan putus kawat ($< 3.6\,\text{mA}$) dan hubung singkat ($> 21.0\,\text{mA}$) pada loop 4–20 mA di sensor, lalu pastikan konsol menampilkan status `BAD / FAULT` dalam 3 siklus polling.
2. **Peredaman Topologi & Shelving Pemeliharaan**: Pastikan trip pemutus induk meredam ratusan alarm hilir ke satu simpul induk, dan pastikan pengatur waktu shelving otomatis pulih saat izin kerja habis.
3. **Audit Pagi Hari**: Setiap pergantian sif pagi, audit seluruh titik Stale, Shelved, dan Forced selama 24 jam terakhir agar tidak ada titik buta yang diwariskan.

## Keputusan yang Harus Dicatat

- Pencatatan fokus tata kelola (Audit pagi wajib atas seluruh alarm malam, titik yang ditangguhkan (shelved), dan nilai yang dipaksa (forced)) serta pendaftaran URI perangkat keras dan tag P&ID.
- Verifikasi lapangan atas sinkronisasi waktu, faktor skala tunggal, dan bit kualitas (Aturan melarang penangguhan alarm sementara bertahan lebih dari 24 jam tanpa tiket perbaikan perangkat keras).
- Pencatatan lebar histeresis $H \ge 4\sigma_n$, waktu tunggu $\tau_{\text{dwell}}$, dan pohon induk peredaman alarm.
- Penegakan aturan penolakan (Siklus pembersihan harian agar jaringan pemantauan tidak mengakumulasi titik buta dari sif ke sif) dan penandatanganan Master Point Sheet.
