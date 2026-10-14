Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 13. Sumber Publik dan Integritas Sitasi

Sebuah sel laporan kilat (*flash report*) atau dokumen komisioning boleh mencitasi standar publik yang telah mapan atau pedoman rekayasa yang telah dipublikasikan. Namun, sel tersebut tidak boleh digantikan oleh standar tersebut.

Dalam rekayasa *mission-critical* modern, disiplin sitasi melindungi ketelitian teknis sekaligus integritas hukum. Mencitasi standar industri membuktikan bahwa metodologi verifikasi Anda bertumpu pada konsensus rekayasa yang dapat dipertahankan dan telah ditinjau sejawat (*peer-reviewed*). Namun, menyalin tabel berhak cipta dari buku panduan vendor privat atau menempelkan skema kepemilikan rahasia milik pelanggan ke dalam laporan publik mengundang liabilitas pelanggaran hak cipta dan pelanggaran perjanjian kerahasiaan (NDA) seketika.

Bab ini mendefinisikan aturan ketat yang mengatur sitasi, batasan kekayaan intelektual, dan sumber rekayasa publik yang dapat diterima.

## Hal yang Boleh dan Tidak Boleh Dilakukan oleh Sitasi

Sitasi adalah penunjuk ke otoritas eksternal yang mendukung metode rekayasa, definisi keselamatan, atau klasifikasi lingkungan.

### Hal yang Boleh Dilakukan oleh Sitasi:
- **Menetapkan Kelas Lingkungan**: Sitasi ke ASHRAE TC 9.9 dapat mendukung kalimat: *"Suhu pasokan cairan pendingin loop sekunder diaudit terhadap koridor Kelas Pendinginan Cair W4 ASHRAE (32°C hingga 45°C)."*
- **Mendefinisikan Aturan Dasar Listrik**: Sitasi ke IEC 60204-1 atau NFPA 70 dapat mendukung kalimat: *"Pemutus sirkuit utama dan interlock henti darurat diverifikasi sesuai dengan IEC 60204-1, Bagian 9.2 (Kategori Penghentian 0: Penghentian tak terkendali dengan pelepasan daya seketika ke aktuator mesin)."*
- **Menjangkarkan Terminologi Proses Komisioning**: Sitasi ke Pedoman ASHRAE 0-2019 dapat mendukung hierarki komisioning lima tingkat (dari Uji Saksi Pabrik Tingkat 1 hingga Pengujian Sistem Terintegrasi Tingkat 5).
- **Mereferensikan Metode Algoritmik**: Sitasi ke Romano et al. (arXiv:2607.19961) dan Fearnhead et al. (DOI:10.1080/10618600.2018.1512868) menetapkan tinjauan sejawat matematis dari algoritma titik perubahan (*changepoint*) Focus dan CPOP.

### Hal yang TIDAK Boleh Dilakukan oleh Sitasi:
- **Sitasi Tidak Dapat Mengisi Sel Pengukuran**: Mencitasi *white paper* pemasaran NVIDIA GB200 NVL72 tidak menggugurkan kewajiban untuk mengukur suhu cairan kembali secara langsung di lantai uji. Sel yang teramati memerlukan pembacaan teramati dari sensor fisik yang terkalibrasi.
- **Sitasi Tidak Dapat Mengabaikan Baris yang Hilang**: Anda tidak boleh menuliskan *"Uji gangguan pasokan tunggal dihilangkan sesuai praktik industri"* dan mencitasi buku panduan komisioning umum. Buku panduan tidak dapat menghapuskan skenario pengujian yang diwajibkan secara kontraktual.
- **Sitasi Tidak Boleh Berupa Tempelan (*Paste*)**: Anda tidak boleh memfotokopi atau menempelkan kurva vendor kepemilikan (*proprietary*), denah lantai pelanggan yang bersifat rahasia, atau teks standar berhak cipta ke dalam laporan Anda. Sitasi dokumen tersebut berdasarkan judul formal, badan penerbit, nomor revisi, dan tahun publikasi.

## Referensi Rekayasa Publik yang Terotorisasi

Metodologi panduan lapangan ini selaras dengan standar publik non-kepemilikan dan badan industri berikut:

1. **Pedoman ASHRAE 0-2019**: *The Commissioning Process*. Mendefinisikan proses komisioning berfokus mutu yang terstandarisasi untuk fasilitas, termasuk Persyaratan Proyek Pemilik (OPR), Dasar Desain (BOD), dan Daftar Periksa Verifikasi.
2. **Pedoman ASHRAE 1.1-2007**: *HVAC&R Technical Requirements for The Commissioning Process*. Mengatur protokol pengujian kinerja fungsional untuk *loop* penanganan fluida primer dan sekunder.
3. **ASHRAE TC 9.9**: *Thermal Guidelines for Data Processing Environments (Edisi ke-5, 2021)*. Mendefinisikan klasifikasi lingkungan pendinginan cair (Kelas W1 hingga W5) dan batas titik embun ambien fasilitas untuk pengendalian kondensasi.
4. **IEC 60204-1 (Edisi 6.0, 2016)**: *Safety of Machinery – Electrical Equipment of Machines – Part 1: General Requirements*. Mengatur isolasi listrik, proteksi arus lebih, *loop* berkabel keras (*hardwired*) henti darurat, dan uji ketahanan dielektrik untuk mesin industri.
5. **NFPA 70 (National Electrical Code, Edisi 2023)**: Pasal 645 (*Information Technology Equipment*) dan Pasal 250 (*Grounding and Bonding*).
6. **Pedoman Pendinginan Cair Open Compute Project (OCP)**: Standar terbuka yang mengatur kebersihan *loop* fluida sekunder, kompatibilitas material (metalurgi yang terbasahi fluida), dan klasifikasi kopling sambung-cepat—yang secara eksplisit membedakan kopling buta tingkat bilah (*blind mates*, UQD) dari kopling uji manifold aliran-penuh (seperti Danfoss FD83).
7. **ISA-5.1-2009**: *Instrumentation Symbols and Identification*. Mengatur pembuatan draf terstandarisasi untuk Diagram Perpipaan & Instrumentasi (P&ID) pada *loop* pendinginan cair.

## Menangkis Penghindaran Proposal Vendor

Taktik umum yang sering digunakan oleh pemasok peralatan yang kurang siap selama rapat komisioning adalah menyajikan *white paper* umum atau draf pracetak akademis untuk menanggapi sel pengujian yang gagal.

Jika sebuah kabinet bank beban gagal dalam masa jeda 15 menit akibat kelaparan aliran yang parah, dan vendor menyerahkan makalah yang dipublikasikan yang menunjukkan bahwa "pelat dingin saluran mikro tingkat lanjut dapat mentoleransi pendidihan sementara", tolak pengajuan tersebut seketika.
- *White paper* tersebut adalah dokumen akademis yang menjelaskan eksperimen laboratorium dalam kondisi terkendali.
- Pengujian Anda adalah verifikasi penerimaan atas mesin khusus yang dikontrakkan yang bertindak sebagai pengganti rak produksi kelas NVL72.
- Laporan kilat mencatat apa yang dilakukan oleh mesin fisik di lantai uji terhadap revisi spesifikasi yang disitasi. Dokumen ini tidak memperdebatkan kemungkinan-kemungkinan akademis.

Pertahankan batasannya. Tegaskan bahwa sitasi tetap berada di baris bibliografi, sementara sel-sel pengujian tetap menjadi milik Anda.

## Keputusan yang Harus Dicatat

Di bagian kepatuhan dan sitasi pada laporan kilat, dokumentasikan:

- Judul formal, organisasi penerbit, edisi, dan revisi dari setiap standar eksternal yang disitasi dalam laporan.
- Sertifikasi bahwa tidak ada teks vendor kepemilikan, data rahasia pelanggan, atau skema berhak cipta yang ditempelkan ke dalam dokumen.
- Pernyataan bertanda tangan yang mengonfirmasi bahwa semua batas teknis dievaluasi terhadap revisi spesifikasi proyek yang dibekukan yang berlaku saat itu.
