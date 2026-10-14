Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 1. Klaim

Proyek verifikasi pendinginan cair gagal pada minggu pertamanya ketika tidak ada seorang pun yang menuliskan kalimat pasti yang harus dibuktikannya. "Pendinginan cair bekerja" bukanlah klaim rekayasa; itu adalah angan-angan belaka. Kalimat klaim yang berstandar audit menyebutkan fasilitas fisik, tugas elektrik dan hidrolik yang disimulasikan oleh bank beban, kondisi batas pasokan air fasilitas (*facility water supply* - FWS), dan keputusan komersial pasti yang akan diambil oleh pemilik fasilitas ketika paket pengujian diserahkan.

Pada proyek-proyek aula data AI yang menjadi dasar panduan lapangan ini, keputusan komersial tersebut adalah apakah infrastruktur pendinginan fasilitas secara hukum dan mekanis dapat diterima untuk penempatan TI produksi (*IT deployment*). Keputusan itu bukan tentang apakah chip komputasi terakselerasi akan berhasil menjalankan beban kerja pelatihan model terdistribusi. Keputusan itu juga bukan tentang apakah purwarupa bank beban cair memenuhi standar litbang manufaktur. Klaim-klaim tersebut milik lingkup rekayasa lain, bangku uji lain, dan tanda tangan lain.

```
+----------------------------------------------------------------------------------------------------+
| BATAS KALIMAT KLAIM PROYEK |
+------------------------------------+---------------------------------------------------------------+
| APA YANG DIBUKTIKAN KLAIM HUKUM | APA YANG TIDAK DAPAT DIBUKTIKAN OLEH KLAIM |
+------------------------------------+---------------------------------------------------------------+
| • Perpindahan panas CDU beban 1,2MW| • Efisiensi komputasi silikon atau performa tensor |
| • Kecepatan failover pompa sekunder| • Laju korosi galvanik jangka panjang sambungan cepat (QD) |
| N+1 | • Nilai PUE pendinginan bebas musiman instalasi chiller pusat |
| • Keseimbangan reverse-return | • Ketahanan manufaktur elemen pemanas purwarupa bank beban |
| manifold | • Kepatuhan beban angin struktural selubung bangunan gedung |
| • Penutupan panas entalpi >= 97,0% | |
| • Penanganan transfer daya 2N | |
+------------------------------------+---------------------------------------------------------------+
```

## Merumuskan Klaim Proyek

Susun kalimat tersebut sebelum Anda mulai menghitung bank beban. Jumlah mesin yang dibutuhkan dan topologi kelistrikan merupakan konsekuensi dari kalimat tersebut, bukan titik awalnya. Jika klaim dibatasi pada satu unit distribusi pendingin (*Coolant Distribution Unit* - CDU) *in-row* 1,2 MW yang melayani sepuluh tapak (*footprint*) rak 120 kW, Anda tidak boleh mengerahkan empat puluh bank beban di sepanjang satu baris hanya karena kontraktor utama menyewanya selama sebulan. Jika klaim mencakup selubung ruang putih (*white space envelope*)—termasuk unit CRAH atau dinding kipas (*fan walls*) yang menangkap sisa 15% hingga 20% beban udara konvektif yang lolos dari pelat dingin (*cold plates*) cairan—maka batas termal sisi udara harus dinyatakan secara eksplisit dalam kalimat klaim, atau pengujian tersebut secara struktural tidak valid.

Dalam komisioning fasilitas lengkap, Persyaratan Proyek Pemilik (*Owner’s Project Requirements* - OPR) adalah dokumen kontrak yang sangat tebal. Pada verifikasi pendinginan cair yang dimulai setelah struktur fasilitas dan pemipaan mekanis telah terpasang, Anda memerlukan tata kelola yang sama yang disarikan ke dalam satu halaman yang mengikat:
1. Metrik operasional apa yang harus didemonstrasikan sebelum server produksi diizinkan untuk dikirim?
2. Sistem fisik mana yang berada di dalam batas verifikasi?
3. Sistem instalasi mana yang secara eksplisit dikecualikan?

Jika pemilik telah memiliki halaman OPR yang disetujui, audit dokumen tersebut terhadap pemipaan fisik di lantai aula. Jangan secara diam-diam mengubahnya di margin skrip pengujian lapangan. Jika pemilik belum memiliki dokumen ini, klaim satu halaman adalah dokumen prasyarat yang Anda susun dan tandatangani dengan tinta sebelum membongkar satu pun kotak peralatan. Klaim yang tidak ditandatangani menjamin bahwa rapat penutupan akhir akan merosot menjadi perselisihan mengenai apa yang sebenarnya dibayar kepada pihak penguji untuk dibuktikan.

## Mengaudit Dasar Desain (Basis of Design - BOD)

Dasar Desain (*Basis of Design* - BOD) adalah dokumen pendamping. Dokumen ini menguraikan asumsi rekayasa, koefisien perpindahan panas, dan logika kontrol yang dimaksudkan untuk memenuhi klaim pemilik. Anda mengaudit BOD terhadap aula data fisik sebagaimana adanya, bukan terhadap gambar desain awal.

Anda tidak boleh merata-ratakan perbedaan antara gambar dan instalasi terpasang. Jika BOD menetapkan *header* sekunder *reverse-return* DN150 dengan fluida 25% Propylene Glycol (PG25), dan instalasi terbangun (*as-built*) adalah manifold *direct-return* DN100 yang diisi dengan air demineralisasi dan inhibitor korosi, diskrepansi tersebut bukanlah "penyesuaian lapangan" yang dapat diterima. Itu adalah deviasi desain kritis yang harus dicatat pada sampul klaim sebelum siapa pun memplot kurva pompa atau menyatakan sistem tersebut "patuh" (*compliant*).

Apa yang tidak dapat dibuktikan oleh verifikasi harus tercantum di halaman yang sama dengan apa yang dibuktikannya. Verifikasi ini tidak menjamin garansi produsen server. Verifikasi ini tidak menerima bank beban cair itu sendiri; penerimaan tersebut telah dilakukan di bawah protokol pabrik pada Buku 01, atau memang belum, dan verifikasi ini tidak akan diam-diam melakukan pengujian penerimaan pabrik (*factory acceptance testing*) dengan kedok komisioning lokasi (*site commissioning*). Verifikasi ini tidak memvalidasi kopling lepas-cepat (*quick-disconnect*) yang tidak terdaftar, kimia biosida yang belum diverifikasi, atau batas aliran minimum yang gagal dikuantifikasi oleh spesifikasi proyek. Sel-sel data tersebut tetap kosong sampai skrip pengujian mengutip dokumen yang mengaturnya. Sel kosong adalah perintah henti yang disengaja. Angka yang tidak diverifikasi yang diingat dari memori adalah cacat yang menyamar sebagai data.

Akhirnya, klaim menetapkan status operasional aula:
- **Verifikasi Aula Kosong**: Dilakukan sebelum perangkat keras TI produksi atau *fabric* jaringan aktif diberi energi di dalam ruangan.
- **Jendela Pemadaman Pemeliharaan**: Dilakukan pada *loop* yang diisolasi selama pemadaman fasilitas terjadwal.
- **Kedekatan Aula Aktif (*Live Hall*)**: Dilakukan pada instalasi mekanis bersama di mana baris yang berdekatan menopang beban kerja produksi aktif.

Pernyataan metode yang ditulis untuk aula data kosong yang diterapkan pada fasilitas aktif tanpa mitigasi risiko eksplisit adalah insiden tak berizin yang menunggu untuk memicu pemadaman klien. Jika fasilitas dalam kondisi aktif, Prosedur Operasi Standar (*Standard Operating Procedures* - SOP) dan protokol Metode Prosedur (*Method of Procedure* - MOP) lokasi menggantikan buku ini, dan nomor dokumen yang mengaturnya harus memuncaki lembar klaim.

## Keputusan yang Harus Dicatat Sebelum Mulai Pengujian

- Kalimat klaim proyek yang telah ditandatangani, ditandatangani bersama oleh Insinyur Profesional Pemilik (*Owner PE*) dan Pimpinan Komisioning (*Cx Lead*).
- Inventaris peralatan fisik di dalam lingkup kerja, dan daftar instalasi yang dikecualikan.
- Revisi spesifik Dasar Desain (*Basis of Design* - BOD) yang diaudit, termasuk semua deviasi fisik yang dicatat.
- Keputusan komersial konkret yang akan diambil pemilik dari paket pengujian yang terverifikasi.
- Status operasional fasilitas (kosong, pemadaman terencana, atau aturan aula data aktif).
