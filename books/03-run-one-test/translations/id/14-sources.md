Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 14. Sumber Publik, dan Baris Hak Cipta

Panduan lapangan ini mengartikulasikan metodologi operasional untuk mengeksekusi dan mengaudit pengujian verifikasi pendinginan cairan. Buku ini tidak mencerna, menyalin, atau menduplikasi kode industri berpemilik, standar, desain rekayasa rahasia vendor, atau templat kontrak berhak cipta.

Standar rekayasa yang dapat dibeli dari badan standar penerbit bukanlah dokumen yang boleh direproduksi dalam teks eksternal. Mengutip suatu standar berdasarkan judul, tahun, dan nomor bagian spesifik untuk menetapkan toleransi pengujian hukum adalah praktik rekayasa standar; mereproduksi bagian-bagian ekstensif dari standar tersebut di dalam manual yang dibuat oleh AI adalah tindakan yang tidak pantas.

**STANDAR INDUSTRI NORMATIF YANG DISITASI**

| PANDUAN ASHRAE 0 | "The Commissioning Process" (Edisi 2019). Prinsip-prinsip dasar untuk lingkup komisioning, Persyaratan Proyek Pemilik (OPR), dan audit BOD. |
| :--- | :--- |
| PANDUAN ASHRAE 1.1 | "HVAC&R Technical Requirements for The Commissioning Process" (2007/2014). Metodologi untuk daftar periksa prafungsional dan kinerja fungsional. |
| PANDUAN ACG | AABC Commissioning Group "Commissioning Guideline for Building Systems". Protokol verifikasi pihak ketiga independen dan standar penyaksian. |
| BSRIA BG 29/2020 | "Pre-Commission Cleaning of Pipework Systems" (Edisi ke-6). Kriteria ketat kecepatan penggerusan, pembilasan kimiawi, dan hitungan partikulat padat. |
| NFPA 70 / IEC 60364 | National Electrical Code (NEC) dan standar International Electrotechnical Commission untuk proteksi sirkuit cabang, pentanahan, dan LOTO. |
| ISA-5.1 | "Instrumentation Symbols and Identification". Simbologi P&ID standar untuk diagram alir proses, pemancar (TT, PT, FT), dan katup kontrol (TCV). |

## Penerapan Standar Normatif

Kedua belas produk rekayasa yang diartikulasikan dalam Bab 2 mewakili urutan struktural yang disyaratkan oleh tata kelola komisioning modern. Produk-produk tersebut diturunkan dari metodologi industri standar (termasuk Panduan ASHRAE 0 dan publikasi ACG) yang diadaptasi secara khusus untuk verifikasi pendinginan cairan *mission-critical*.

Hierarki sertifikat penyelesaian (Level 0 hingga 6) mencerminkan standar yang diakui di seluruh rekayasa pusat data global:
- Level 0: Desain & Perencanaan
- Level 1: Pengujian Penerimaan Pabrik (*Factory Acceptance Testing* - FAT)
- Level 2: Pengiriman Komponen & QA Penerimaan
- Level 3: Pemeriksaan Prafungsional (*Pre-Functional Checks* - PFC) & Startup
- Level 4: Pengujian Kinerja Fungsional (*Functional Performance Testing* - FPT)
- Level 5: Pengujian Sistem Terintegrasi (*Integrated System Testing* - IST)
- Level 6: Penutupan & Pelimpahan Operasi

Terminologi "tiga tahap" lokal yang sering digunakan oleh para kontraktor di lantai kerja adalah singkatan lapangan regional. Istilah tersebut tidak menggantikan tingkat sertifikat komisioning global. Ketika mengadopsi salah satu kerangka kerja, Rencana Komisioning harus secara eksplisit mendefinisikan pada halaman pertama tanda tangan hukum mana yang diizinkan untuk didukung oleh dokumentasi yang dihasilkan.

## Kepatuhan Kode Listrik dan Mekanikal

Pemeriksaan keselamatan listrik—termasuk ambang batas resistansi isolasi 100 MΩ dan batas kontinuitas pentanahan 0,1 Ω—diturunkan dari NFPA 70 (NEC Pasal 250 dan Pasal 645 untuk Peralatan Teknologi Informasi) dan standar internasional IEC 60204-1 (*Safety of Machinery - Electrical Equipment of Machines*). Skrip pengujian lapangan tidak boleh mencoba menyalin pasal-pasal kode kelistrikan yang ekstensif ke dalam prosedurnya; skrip tersebut cukup mengutip nomor pasal yang mengatur, dan Inspektur Listrik Berwenang (*Authority Having Jurisdiction* - AHJ) setempat yang menegakkan adopsi yang mengikat tersebut.

Persiapan fluida sekunder, penahanan tekanan hidrostatik, dan deaerasi sistem mengikuti prinsip-prinsip BSRIA BG 29/2020 dan ASME B31.3 (*Process Piping*). Kecepatan pembilasan penggerusan (≥ 1,5 m/s) dan persyaratan penahanan hidrostatik (1,5× MAOP selama 2 jam tanpa penurunan tekanan) adalah standar rekayasa mesin yang mapan untuk pemipaan hidronik.

## Garis Dasar Referensi Non-Hak Milik (Non-Proprietary)

Untuk memberikan tolok ukur numerik yang konkret dan bermakna tanpa mengungkapkan kekayaan intelektual (IP) produsen yang berpemilik atau data rahasia klien, buku ini menggunakan arsitektur referensi non-hak milik:
- **Tapak Komputasi (*Compute Footprint*)**: Rak komputasi virtual standar 120 kW yang mensimulasikan arsitektur terakselerasi berdensitas tinggi (seperti tapak rak kelas NVL72).
- **Unit Pendingin (*Cooling Unit*)**: Coolant Distribution Unit (CDU) 1,2 MW *in-row* atau tersentralisasi menggunakan pompa sentrifugal kaleng N+1 ganda dan penukar panas pelat titanium.
- **Kimia Pendinginan (*Cooling Chemistry*)**: Propylene Glycol 25% (PG25) dengan inhibitor korosi, beroperasi antara pasokan 40,0°C dan balik 50,0°C.

Pengajuan pabrikan yang spesifik, algoritma kontrol PLC berpemilik, skema jaringan rahasia klien, dan dimensi sambungan lepas-cepat berpemilik harus disimpan dalam arsip aman proyek di bawah Perjanjian Kerahasiaan (*Non-Disclosure Agreements* - NDA) yang ditandatangani. Rincian tersebut tidak boleh dipublikasikan dalam panduan referensi terbuka.

## Keputusan yang Harus Dicatat Sebelum Mulai Pengujian

- Daftar lengkap kode, standar, dan pedoman yang mengatur yang disitasi dalam Rencana Komisioning, beserta tahun penerbitannya.
- Nomor dokumen kontrak yang mendukung setiap nilai toleransi.
- Penegasan kembali bahwa IP vendor berpemilik dan gambar rahasia lokasi tetap disimpan secara aman di dalam berkas proyek lokal.
