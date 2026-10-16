Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 18. Apa yang Anda Serahkan kepada Penasihat Hukum (Counsel)

## Disiplin Dasar Audit Lapangan Uji Tuntas Teknis (TDD)

Dalam akuisisi M&A pusat data, pembiayaan proyek (project finance), atau kontrak sewa kapasitas klaster AI skala besar, **Apa yang Anda Serahkan kepada Penasihat Hukum (Counsel)** adalah satu-satunya benteng yang mengikat keputusan investasi ratusan juta dolar pada realitas fisik. Klaim pemasaran penjual seperti 'Setara Tier III', 'Redundansi 2N 50 MW', atau 'PUE 1.25' hanyalah kalimat brosur hingga dibuktikan di lapangan.

$$H_{\text{NOx\_permit\_hours}} \ge H_{\text{testing}} + H_{\text{emergency\_run}} \quad (\text{typically } \ge 200\,\text{h/yr})$$

Tugas auditor TDD adalah menelusuri fasilitas tanpa menyentuh sakelar aktif (Hands-Off Rule), mencocokkan diagram satu garis (SLD), P&ID, pelat nama fisik, setelan relai, dan log insiden 24 bulan terakhir untuk **mengubah kalimat klaim penjual menjadi pernyataan rekayasa yang akurat dan bersyarat**.

> *"Seindah apa pun lobi gedung atau sehijau apa pun layar dasbor, jika menara pendingin berbagi satu pipa header tunggal atau kapasitas chiller turun 30% pada suhu ekstrem ASHRAE 0,4%, maka fasilitas tersebut tidak memiliki kapasitas yang diklaim penjual."*

## Matriks Audit Kapasitas Bersih (Derated), Redundansi, dan Utang CAPEX

Selama penelusuran lapangan, kapasitas fasilitas tidak boleh dihitung dari penjumlahan pelat nama (Nameplate Sum), melainkan harus dihitung sebagai **kapasitas bertahan bersih ($P_{\text{IT, firm}}$)** pada suhu desain ekstrem ASHRAE, batas beban 45% pada bus 2N, dan peringkat daya kontinu generator (COP/PRP):

| Area Audit TDD | Dokumen & Bukti Fisik Lapangan | Kriteria Lulus (Aset Sehat) | Bendera Merah (Penyesuaian Harga / Syarat CP) |
| :--- | :--- | :--- | :--- |
| **Kapasitas Listrik & Generator** | Kontrak gardu MVA, peringkat ISO 8528 genset, beban UPS $N-1$ | $P_{\text{IT, firm}}$ menutup 100% kontrak kW penyewa | Beban bus 2N $> 45\%$ atau bahan bakar $< 48\,\text{jam}$ |
| **Derating Termal Pendingin** | Kurva chiller suhu puncak, $\Delta T_{\text{PHE}}$ CDU, isolasi header | Suhu SLA terjaga saat $N-1$ pada suhu ekstrem | SPOF pipa bersama atau defisit kapasitas musim panas |
| **Usia Aset (EOSL) & CAPEX** | Tahun pembuatan di pelat nama, jam jalan, impedansi baterai | Cadangan CAPEX 5 tahun telah dianggarkan | Peralatan melewati EOSL atau baterai VRLA menggembung |
| **Rekam Jejak Operasi & Serat Optik** | Log insiden 24 bulan, absensi kartu akses, jalur lubang MMR | Nol pelanggaran SLA; 2 jalur serat optik terpisah | Dua kabel serat masuk melalui satu parit (Single Trench) |

Jangan pernah menghaluskan kontradiksi antara gambar SLD, layar BMS, dan pelat nama di lapangan. Catat **Apa yang Anda Serahkan kepada Penasihat Hukum (Counsel)** beserta foto berpenanda waktu pada Lembar Kunjungan (Visit Sheet).

## Protokol Penelusuran Fisik dan Konversi Temuan ke Klausul Hukum (SPA)

Untuk memaksimalkan ketajaman audit dalam jendela kunjungan yang singkat, jalankan tiga fase berikut:

1. **Bedah Ruang Data Pra-Penerbangan (RFI)**: Tandai potensi titik kegagalan tunggal (SPOF) pada SLD dan P&ID sebelum berangkat, serta minta laporan RCA insiden P1/P2 dan studi koordinasi relai 2 tahun terakhir.
2. **Penelusuran Fisik & Wawancara Teknisi Malam**: Telusuri jalur pipa dan kabel dari gardu induk hingga PDU rak dan CDU sekunder, lalu tanyakan langsung kepada teknisi sif malam katup mana yang macet dan alarm mana yang selalu menyala.
3. **Memo Bendera Merah & Konversi Kontrak SPA**: Hitung biaya perbaikan defisit langsung (Immediate Deficit CAPEX) dan jadwal penggantian 5 tahun untuk diterjemahkan oleh penasihat hukum menjadi syarat pendahuluan (Conditions Precedent / CP) atau pemotongan harga beli.

## Keputusan yang Harus Dicatat

- Pencatatan hasil verifikasi fisik terhadap klaim penjual pada fokus audit (Apa yang Anda Serahkan kepada Penasihat Hukum (Counsel)).
- Perhitungan kapasitas TI bersih ($P_{\text{IT, firm}}$) setelah derating suhu ambien puncak dan kegagalan tunggal $N-1$.
- Kuantifikasi titik kegagalan tunggal (SPOF), utang CAPEX peralatan EOSL, dan daftar cacat terbuka.
- Penetapan syarat pendahuluan (Conditions Precedent) kontrak akuisisi/pinjaman dan penandatanganan Visit Sheet.
