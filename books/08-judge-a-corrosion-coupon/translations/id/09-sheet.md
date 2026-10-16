Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 9. Lembar Kupon Utama (The Coupon Sheet)

## Dasar Rekayasa Audit Korosi Atmosferik ISA-71.04-2013

Di dalam ruang data yang menampung server AI kepadatan tinggi dan sakelar jaringan inti, **Buku besar pencatatan nomor seri, koordinat rak, hari paparan, dan rincian film ($\text{Cu}_2\text{O}, \text{CuO}, \text{Cu}_2\text{S}, \text{Ag}_2\text{S}, \text{AgCl}$)** adalah satu-satunya metode kuantitatif untuk mencegah korosi rambat (creep corrosion akibat pertumbuhan kristal $\text{Cu}_2\text{S}$ dan $\text{Ag}_2\text{S}$) yang menghancurkan papan sirkuit tercetak (PCB).

![9. Lembar Kupon Utama (The Coupon Sheet)](../figures/fig-07-master-corrosion-coupon-sheet-and-refusal.png)

$$d_{\text{net}} = \max\left(0, \, d_{\text{exposed}} - d_{\text{travel\_blank}}\right)$$

Persyaratan garansi pabrikan server (OEM) mewajibkan udara ruang server selalu berada pada **Kelas Keparahan G1 (Mild)** menurut ANSI/ISA-71.04-2013. Anda tidak dapat mengklaim kepatuhan G1 tanpa menggantung pasangan kupon tembaga (Cu) dan perak (Ag) selama 30 hari serta menganalisis ketebalan film reaksi ($\text{\AA}/30\,\text{hari}$) melalui reduksi kulometri.

> *"Laporan korosi yang hanya menggunakan kupon tembaga tanpa kupon perak, atau menyembunyikan fluktuasi kelembapan relatif (RH), akan gagal mendeteksi uap belerang unsur ($\text{S}_8$) dan klorin sehingga wajib ditolak seketika."*

## Klasifikasi Reaktivitas Kupon Cu/Ag dan Kriteria Desain Filtrasi Kimia (GPA)

Ketebalan film terukur $d_{\text{raw}}$ selama $t_{\text{days}}$ hari dinormalisasi ke basis 30 hari ($d_{30} = d_{\text{raw}} \cdot (30 / t_{\text{days}})^n$) dan dikurangi ketebalan kupon kontrol perjalanan ($d_{\text{blank}}$). Penyegelan ruang dan unit filtrasi fase gas (GPA) wajib memenuhi matriks berikut:

| Parameter Audit Korosi | Indikator Fisik / ISA-71.04 | Kriteria Lulus Kelas G1 | Pemicu Penolakan / Tindakan Darurat (G2/G3/GX) |
| :--- | :--- | :--- | :--- |
| **Ketebalan Film Tembaga (Cu) 30 Hari** | $d_{\text{Cu}, 30}$ ($\text{Cu}_2\text{O} + \text{CuO} + \text{Cu}_2\text{S}$) | $< 300\,\text{\AA} / 30\,\text{hari}$ | $\ge 300\,\text{\AA}$ (Kehadiran $\text{Cu}_2\text{S}$ menandakan gas saluran/luar) |
| **Ketebalan Film Perak (Ag) 30 Hari** | $d_{\text{Ag}, 30}$ ($\text{Ag}_2\text{S} + \text{AgCl}$) | $< 200\,\text{\AA} / 30\,\text{hari}$ | $\ge 200\,\text{\AA}$ atau kupon perak tidak dipasang |
| **Tekanan Positif & Kendali RH** | $\Delta P_{\text{room}}$ dan Kelembapan Relatif $\text{RH}$ | $\Delta P \ge +12.5\,\text{Pa}$, $\text{RH} < 50\%$, $\Delta\text{RH}/\Delta t < 6\%/\text{jam}$ | Tekanan negatif atau perangkap drainase lantai kering |
| **Waktu Kontak & Sisa Umur Media GPA** | $\text{EBCT} = V_{\text{media}}/Q$ & Uji ASTM D6646 | $\text{EBCT} \ge 0.25\,\text{s}$, sisa oksidan $\ge 20\%$ | Menilai kejenuhan media hanya dari warna luar pelet |

Sebelum membeli mesin scrubber kimia, rapatkan seluruh penetrasi kabel, isi perangkap drainase P-trap dengan cairan penyegel, dan catat **Buku besar pencatatan nomor seri, koordinat rak, hari paparan, dan rincian film ($\text{Cu}_2\text{O}, \text{CuO}, \text{Cu}_2\text{S}, \text{Ag}_2\text{S}, \text{AgCl}$)** pada Lembar Kupon.

## Protokol Paparan 30 Hari dan Tindakan Kontainmen Saat Gagal G1

Siklus pemasangan, pengambilan, analisis laboratorium, hingga verifikasi perbaikan dijalankan melalui tiga langkah ketat:

1. **Penanganan Bebas Kontaminasi**: Gunakan sarung tangan nitril bebas bedak untuk memasang pasangan kupon Cu/Ag beserta logger RH/T pada intake udara luar (OA), plenum pasokan, dan bezel depan rak (U24), serta simpan satu Travel Blank tertutup.
2. **Audit Kurva Reduksi Kulometri**: Periksa sertifikat laboratorium terakreditasi ISO/IEC 17025 untuk memisahkan ketebalan oksida jinak ($\text{Cu}_2\text{O}$) dari sulfida agresif ($\text{Cu}_2\text{S}, \text{Ag}_2\text{S}$) dan klorida ($\text{AgCl}$).
3. **Respons Sif Darurat & Uji Ulang**: Jika hasil melampaui batas G1, segera kurangi udara luar, turunkan $\text{RH} < 45\%$, segel jalur infiltrasi, dan **gantung kupon baru selama 30 hari** untuk membuktikan pemulihan G1.

## Keputusan yang Harus Dicatat

- Pencatatan fokus audit (Buku besar pencatatan nomor seri, koordinat rak, hari paparan, dan rincian film ($\text{Cu}_2\text{O}, \text{CuO}, \text{Cu}_2\text{S}, \text{Ag}_2\text{S}, \text{AgCl}$)), nomor seri kupon, koordinat rak, dan durasi paparan pada Coupon Sheet.
- Verifikasi rincian film kulometri tembaga ($< 300\,\text{\AA}$) dan perak ($< 200\,\text{\AA}$) setelah dikurangi Travel Blank.
- Verifikasi tekanan positif ruangan ($\ge +12.5\,\text{Pa}$), segel P-trap, dan uji sisa media GPA (ASTM D6646).
- Pelaksanaan penurunan RH darurat, penyegelan celah, dan uji ulang kupon 30 hari apabila kelas G1 terlampaui.
