Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 9. Kapasitas, Tanpa Angka Rekaan

Tugas kapasitas harian manajer fasilitas diatur oleh tiga pertanyaan mendasar:
1. Kapasitas apa yang Anda jual secara kontraktual kepada pelanggan?
2. Kapasitas apa yang digunakan secara fisik pada detik ini?
3. Kapasitas apa yang akan bertahan jika komponen tunggal terbesar Anda gagal sekarang?

```
+-----------------------------------------------------------------------------+
| PLAFON REDUNDANSI KAPASITAS 2N |
| |
| 100% +----------------------------------------------------------------+ |
| | ZONA BAHAYA TAK TERPAKAI | |
| | Jika Bus A trip, Bus B langsung kelebihan beban & padam total | |
| 90% +================================================================+ |
| | BEBAN SURVIVAL MAKSIMUM (90%) | |
| | | |
| 50% + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+ |
| | ATURAN 45%: BATAS MAKSIMUM TUNAK YANG DIIZINKAN | |
| 45% +----------------------------------------------------------------+ |
| | | |
| | RENTANG OPERASI 2N YANG AMAN | |
| | Beban Bus A <= 45% | Beban Bus B <= 45% | |
| 0 +----------------------------------------------------------------+ |
+-----------------------------------------------------------------------------+
```

![2N Power Redundancy Ceiling](../figures/fig-04-2n-power-capacity-and-redundancy-ceiling.png)

Jika Anda tidak dapat menjawab ketiga pertanyaan tersebut dengan kepastian matematis dari catatan pengukuran yang terverifikasi, Anda tidak tahu apakah pemeliharaan atau penyebaran server yang diusulkan hari ini aman.

## Matematika Redundansi 2N: Aturan 45%

Mitos operasional yang paling luas dan mematikan dalam manajemen pusat data adalah keyakinan bahwa dalam arsitektur listrik redundan 2N, setiap jalur daya dapat dioperasikan secara aman hingga **50% dari kapasitas nameplate terukurnya**.

Ini adalah jebakan matematis yang telah menyebabkan pemadaman beruntun multi-megawatt yang katastrofik di seluruh industri:

$$P_{\text{total}} = P_{\text{Bus A}} + P_{\text{Bus B}}$$

Pertimbangkan busbar listrik 2N berkapasitas 2000 kVA. Manajer operasi mengamati bahwa Bus A memikul 1040 kVA (beban 52%) dan Bus B memikul 1020 kVA (beban 51%). Manajer berasumsi bahwa karena tidak ada busbar yang kelebihan beban, sistem beroperasi dengan nyaman dalam batas keamanannya.

Sekarang, transformator hulu yang memberi makan Bus A mengalami trip.
Dalam hitungan milidetik, semua catu daya server TI berkabel ganda yang terpasang pada Bus A memindahkan beban listriknya ke Bus B.

Beban total seketika yang dibebankan pada Bus B menjadi:

$$P_{\text{Bus B, transien}} = 1040\,\text{kVA} + 1020\,\text{kVA} = 2060\,\text{kVA} \quad (103\% \text{ dari kapasitas terukur})$$

Bus B seketika mengalami kelebihan beban. Pemutus sirkuit utama untuk Bus B merasakan arus lebih berkelanjutan dan trip setelah kurva penundaan waktu yang singkat, menjerumuskan seluruh ruang data ke dalam kegelapan total. Fasilitas yang dirancang untuk toleransi kesalahan 2N lengkap mengalami pemadaman total 100% akibat kegagalan komponen tunggal.

Untuk mencegah trip kaskade, setiap jalur distribusi listrik 2N harus mematuhi **Aturan Pembebanan 45%** secara ketat:

$$P_{\text{steady-state}} \le 0.45  \times P_{\text{rated}}$$

Di bawah aturan 45%:
- Bus A memikul ≤ 45% (900 kVA).
- Bus B memikul ≤ 45% (900 kVA).
- Jika Bus A trip, Bus B yang bertahan mewarisi beban total 900 + 900 = 1800 kVA (90% dari kapasitas terukur).
- Bus B beroperasi secara stabil dengan penyangga keamanan 10%, jauh di bawah ambang batas trip termal-magnetik, memungkinkan teknisi mengelola kontinjensi dengan aman.

Setiap manajer sif yang mengizinkan busbar listrik 2N melebihi pemanfaatan tunak 45% telah mengompromikan redundansi fasilitas dan beroperasi dalam kondisi berisiko tinggi tanpa peringkat resmi.

## Kapasitas Hidrolik Loop Pendingin Sekunder

Di ruang data AI berpendingin cair yang menampung rak komputasi densitas tinggi (seperti arsitektur NVIDIA NVL72 yang mengonsumsi hingga 132 kW per rak), tata kelola kapasitas hidrolik sama pentingnya dengan kapasitas listrik:

```
+-----------------------------------------------------------------------------+
| PLAFON KAPASITAS HIDROLIK CDU |
| |
| Parameter Batas Desain Terukur Batas Redundansi Operasi |
| ------------------ ------------------------ --------------------------- |
| Pembuangan Panas 1200 kW per CDU <= 1000 kW (83% kap PHE) |
| Laju Aliran Sekund. 1440 LPM (24 LPS) <= 1200 LPM (Pompa Tunggal N)|
| Suhu Pasokan 25.0°C - 32.0°C (W3/W4) <= 30.0°C (Ambien Maksimum) |
| Konfigurasi Pompa N+1 Pompa VFD Ganda 1 Pompa Jalan / 1 Siaga Auto |
| Tekanan Loop 0.15 - 0.90 MPa Penurunan Tekanan < 1.0 bar |
+-----------------------------------------------------------------------------+
```

Saat mengevaluasi permintaan pelanggan untuk memasang rak berpendingin cair densitas tinggi tambahan, duty manager harus mengevaluasi kendala hidrolik:
1. **Ketersediaan Aliran Total**: Verifikasi bahwa pompa sekunder dapat mengalirkan laju aliran volumetrik yang diperlukan (q_v) untuk mempertahankan aliran turbulen cold plate:

$$q_v = \frac{Q}{\rho \cdot c_p \cdot \Delta T}$$

Di mana:
- Q adalah total disipasi panas termal ( kW).
- $
- ρ adalah massa jenis propilen glikol 25% (1026\, kg/m^3pada30°C$).
- c_p adalah kapasitas panas spesifik (3.92 kJ/( kg· K)).
- ΔT adalah kenaikan suhu fluida melintasi manifold rak (biasanya 10.0 K).

2. **Ketidakseimbangan Hidrolik dan Kelaparan Aliran Direct-Return**: Saat rak tambahan dihubungkan ke manifold distribusi sekunder, kerugian gesekan (ΔP_f) meningkat secara kuadratik terhadap kecepatan aliran (v):

$$\Delta P_f = f \cdot \frac{L}{D} \cdot \frac{\rho v^2}{2}$$

Jika manifold dipasang dalam konfigurasi direct-return alih-alih loop reverse-return (Tichelmann), penambahan beban ke ujung baris yang jauh akan membuat rak indeks kekurangan aliran fluida, menyebabkan pelambatan termal (thermal throttling) instan pada GPU.

Jangan pernah menyetujui penambahan beban cairan berdasarkan jaminan lisan dari pelanggan bahwa "pompanya terlihat cukup besar." Tuntut simulasi aliran hidrolik bersertifikat dan perhitungan penurunan tekanan sebelum menerbitkan izin penyambungan.

## Mitos "Mencoba" Beban

Ketika pelanggan atau tim instalasi proyek meminta izin untuk memberi daya pada rak server tambahan yang melebihi batas kapasitas yang dihitung, mereka sering menyarankan:
> *"Mari kita nyalakan saja raknya dan perhatikan meternya selama dua puluh menit untuk melihat apakah pemutusnya bertahan."*

Ini adalah padanan operasional dari menguji ketebalan es danau dengan mengendarai truk tiga puluh ton ke atasnya.

Menyalakan peralatan "untuk melihat apakah bertahan":
- Menghadapkan busbar listrik dan transformator pada arus inrush masif dan kejutan termal.
- Berisiko men-trip relai proteksi hulu, memicu pemadaman instan untuk pelanggan yang aktif di sebelahnya.
- Menggantikan rekayasa matematis yang ketat dengan perjudian yang ceroboh.

Jika penambahan beban yang diminta melebihi alokasi kontraktual atau plafon redundansi 45%, Duty Manager harus segera menolak otorisasi. Hentikan penyalaan daya. Pelanggan harus menyerahkan studi rekayasa formal dan menegosiasikan amandemen kontrak sebelum satu pemutus sirkuit tambahan ditutup.

## Keputusan yang Harus Dicatat

- Kapasitas kontraktual yang dijual, dikutip berdasarkan klausul kontrak pelanggan dan ID rak.
- Beban listrik aktif yang dicatat per busbar, memverifikasi kepatuhan terhadap aturan redundansi 45%.
- Laju aliran loop sekunder hidrolik, suhu pasokan, dan tekanan diferensial yang dicatat per CDU.
- Sisa kapasitas setelah kegagalan komponen tunggal terburuk: diverifikasi melalui studi rekayasa bernama, atau dicatat sebagai tidak diketahui.
- Setiap permintaan yang melebihi kapasitas operasional yang aman ditolak secara tertulis; nol pemberian daya "untuk mencoba."
