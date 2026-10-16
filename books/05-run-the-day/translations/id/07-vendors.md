Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 7. Vendor dan Kontraktor

Vendor pihak ketiga atau teknisi pabrikan peralatan yang bekerja di dalam pusat data Anda adalah sepasang tangan yang beroperasi di bawah izin hukum Anda. Mereka bukanlah entitas otonom yang dapat Anda tinggalkan tanpa pengawasan di dalam ruang peralatan listrik.

| **GERBANG TATA KELOLA VENDOR** |
| :--- |
| [GATE 1] Lingkup Pra-Kedatangan: Tugas spesifik, MOP disetujui, daftar alat |
| ↓ |
| [GATE 2] Briefing Keamanan & Keselamatan: Lencana, LOTO terverifikasi, APD |
| ↓ |
| [GATE 3] Pengawalan Aktif: Teknisi resmi ditugaskan; tidak pernah sendirian |
| ↓ |
| [GATE 4] Penegakan Batas Lingkup: Stop Work jika menyimpang dari MOP |
| ↓ |
| [GATE 5] Penutupan Teknis: Audit fisik pekerjaan, suku cadang lama, bersih |
| ↓ |
| [GATE 6] Pemisahan Komersial: Tanda tangan teknis != Penerimaan faktur |

Seorang manajer yang menandatangani lencana pengunjung, menunjuk ke arah ruang baterai, dan kembali ke kantornya telah melepaskan kendali atas fasilitas tersebut. Jika vendor tersebut menjatuhkan kunci pas di atas busbar 480V atau membuka katup isolasi yang salah, pemadaman yang terjadi adalah milik manajer, bukan milik vendor.

## Definisi Lingkup Pra-Kedatangan

Sebelum vendor melewati pintu putar keamanan, lingkup operasional mereka harus ditentukan secara tertulis dengan batasan yang jelas:
- Tag peralatan persis mana yang diizinkan untuk mereka sentuh (misalnya, *"Hanya rakitan filter oli kompresor Chiller Sentrifugal CH-02"*).
- Peralatan mana yang dilarang keras untuk mereka sentuh (misalnya, *"Dilarang menyentuh katup isolasi air kondenser atau panel kontrol chiller CH-01 di sebelahnya"*).
- Definisi "Selesai": Pengujian fisik, pembacaan tekanan, atau tonggak operasional spesifik apa yang harus diverifikasi sebelum peralatan dianggap diperbaiki.
- Hasil kerja yang diperlukan sebelum keberangkatan: Laporan servis lapangan pabrik, log pengujian alat terkalibrasi, nomor seri semua komponen pengganti yang dipasang, dan penyerahan fisik semua suku cadang yang rusak untuk analisis akar penyebab.

Perintah kerja vendor yang berbunyi *"Pemeliharaan preventif tahunan pada sistem UPS"* adalah undangan menuju bencana. Dokumen itu tidak menentukan batasan, batas pengujian, dan kendala operasional. Jika vendor tidak memberikan MOP terperinci langkah demi langkah tujuh puluh dua jam sebelumnya, batalkan kunjungan lokasi tersebut.

## Tuan Rumah Lokasi Khusus (Site Host)

Setiap vendor yang bekerja di area listrik kritis, mekanis, atau ruang data harus didampingi oleh tuan rumah lokasi (site host) yang berdedikasi dan berkualifikasi dari tim sif operasional Anda.

Tuan rumah lokasi tidak melakukan pekerjaan fisik vendor. Tugas tuan rumah adalah:
1. **Penegakan Batas Lingkup**: Mengamati tindakan vendor secara terus-menerus. Jika teknisi meraih kubikel switchgear di sebelahnya atau mulai membuka katup yang tidak tercantum dalam MOP, tuan rumah segera memerintahkan Stop Work.
2. **Reaksi Darurat**: Jika terjadi arc-flash, percikan bahan kimia, atau trip peralatan, tuan rumah memulai Prosedur Operasi Darurat (EOP) lokasi, memanggil bantuan medis, dan mengarahkan isolasi kondisi aman.
3. **Kendali Pengawalan**: Memastikan vendor tetap berada dalam batas kerja fisik yang diizinkan dan tidak pernah berkeliaran di lorong produksi tanpa pengawasan.

### Menghilangkan Perluasan Lingkup Spontan ("Mumpung Kami di Sini")

Kata-kata paling berbahaya dalam operasi pusat data adalah ketika teknisi vendor berkata:
> *"Mumpung penutup panelnya terbuka, apakah Anda ingin saya sekalian menyetel sensitivitas relai gangguan tanah ini?"*

Jawabannya selalu dan tanpa kompromi adalah **"Tidak."**

Tugas bermanfaat yang ditemukan saat peralatan terbuka bukanlah bantuan yang baik; itu adalah perubahan rekayasa tanpa tinjauan dan tanpa izin:
- Tidak memiliki MOP yang disetujui.
- Belum menjalani penilaian risiko Change Advisory Board.
- Tidak memiliki rencana pembatalan dan pemulihan yang diperhitungkan.
- Ruang kendali belum mencatat instalasi dalam kondisi operasi abnormal.

Jika vendor mengidentifikasi cacat tak terduga atau penyesuaian yang disarankan selama pekerjaan mereka, catat temuan tersebut ke dalam register cacat lokasi. Hal itu akan dijadwalkan, ditinjau, dan dieksekusi selama jendela pemeliharaan resmi di masa mendatang di bawah izinnya sendiri. Jangan pernah membiarkan perluasan lingkup spontan di fasilitas yang sedang beroperasi aktif.

## Penerimaan Teknis vs. Penagihan Komersial

Jangan pernah membiarkan urgensi komersial dari siklus penagihan vendor mengompromikan penerimaan teknis.

Penerimaan teknis adalah verifikasi rekayasa ketat bahwa peralatan telah dipulihkan ke kemampuan operasional penuh:
- Peralatan telah beroperasi di bawah beban termal atau listrik penuh tanpa getaran abnormal, penyimpangan suhu, atau kebocoran fluida.
- Semua saluran komunikasi digital (Modbus, BACnet, SNMP) antara peralatan dan BMS/EPMS pusat telah dipulihkan dan diverifikasi.
- Area kerja telah dibersihkan, semua puing, sisa pengikat kabel (zip tie), dan potongan kawat disingkirkan, dan semua penutup panel fisik, pelindung dead-front, dan interlock keselamatan dipasang kembali.
- Semua komponen lama yang rusak (kontaktor terbakar, mechanical seal aus, kapasitor terdegradasi) telah diberi label, dikemas, dan dipindahkan ke ruang penyimpanan karantina lokasi untuk inspeksi forensik.

Dokumen yang Anda tandatangani pada akhir kunjungan vendor secara eksklusif adalah **Verifikasi Layanan Lapangan atas Pekerjaan yang Dilakukan**. Dokumen ini hanya memverifikasi bahwa vendor berada di lokasi dan melakukan langkah-langkah bernomor dalam MOP.

Dokumen ini bukan merupakan penerimaan komersial atas faktur, dan tidak melepaskan hak pemilik fasilitas untuk mengajukan klaim garansi jika cacat laten muncul selama operasi berikutnya. Jika perwakilan komersial mendesak Anda untuk menandatangani sertifikat penyelesaian komersial tanpa syarat sebelum pengujian beban fungsional selesai, cantumkan catatan pada lembar tersebut: *"Pekerjaan yang dilakukan diverifikasi secara visual; penerimaan teknis fungsional menunggu pengujian beban nyata selama 24 jam."*

## Keputusan yang Harus Dicatat

- Lingkup kerja vendor yang telah disetujui sebelumnya dan nomor registri MOP terlampir.
- Nama tuan rumah lokasi khusus yang ditugaskan kepada vendor.
- Pemeriksaan batas lingkup: Dikonfirmasi nol penyimpangan dari MOP tertulis, atau catatan perintah Stop Work.
- Penerimaan teknis ditandatangani hanya setelah inspeksi fisik dan verifikasi pengujian beban nyata.
- Nomor seri komponen yang dipasang dan lokasi kotak karantina dari komponen yang rusak.

## Batas Demarkasi Fisik dan Protokol Audit Sif Kuantitatif

Manajer operasional sif wajib menjaga titik demarkasi fisik (`DEMARC`) di seluruh empat cincin fasilitas (Ring 1: Utilitas & Perimeter, Ring 2: Ruang Mekanikal/Elektrikal Utama, Ring 3: Distribusi Whitespace & CDU Sekunder, Ring 4: Interior Rak Penyewa) dan mencatat matriks tolok ukur kuantitatif berikut pada Lembar Hari (Day Sheet):

| Area Audit Sif | Parameter Pemantauan & Metrologi | Amplop Operasi Normal | Ambang Intervensi / Hentikan Pekerjaan (Stop Work) |
| :--- | :--- | :--- | :--- |
| **Batas Beban Redundansi Listrik 2N** | Utilisasi tunak Bus A / Bus B ($P_{\text{bus}} / P_{\text{rated}}$) | $\le 45.0\%$ (Saat gagal 1 jalur $\le 90.0\%$) | Tolak segera penambahan beban rak jika utilisasi $> 45.0\%$ |
| **Hidraulik & Kimiawi CDU Sekunder** | Tekanan pasokan $P_{\text{sup}}$, pendekatan $\Delta T_{\text{PHE}}$, kadar PG | $0.15\sim 0.90\,\text{MPa}$, $\Delta T_{\text{PHE}} \le 8.0\,\text{K}$, PG $25.0\% \pm 1.0\%$ | $\Delta P > 1.0\,\text{bar}$, konduktivitas $> 10\,\mu\text{S/cm}$, atau tetesan kopling |
| **Izin Kerja (PTW) & Energi-Nol LOTO** | Kunci LOTO, pelepasan muatan kapasitor, katup pintas | 100% didampingi host situs; tutup sebelum kedaluwarsa | Penyimpangan dari MOP tertulis atau pekerjaan tambahan spontan |
| **Jam Insiden & Notifikasi SLA** | Deteksi ($T_0$), kondisi aman EOP, pemberitahuan klien | P1: Kirim fakta terverifikasi dalam $\le 15\,\text{menit}$ | Dilarang mencantumkan hipotesis/spekulasi pada notifikasi |
