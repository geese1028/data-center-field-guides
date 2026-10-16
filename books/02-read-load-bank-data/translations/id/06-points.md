Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 6. Bagaimana Titik Data Terbentuk

Sebuah titik data yang diplot pada grafik laporan kilat (*flash report*) bukanlah pengukuran mentah, dan pengukuran mentah bukanlah berkas coretan sementara yang bebas dibuang.

Dalam komisioning *mission-critical*, grafik rekayasa yang tidak dapat menunjukkan data deret waktu (*time-series*) mentah yang mendasarinya bukanlah sebuah analisis; itu hanyalah ilustrasi grafis. Jika Anda membuang data mentah dan hanya menyimpan rata-rata per menit, Anda kehilangan kemampuan untuk mendeteksi pembentukan busur api kontaktor (*contactor arcing*), gumpalan kavitasi (*cavitation slugs*) pada pengukur aliran, dan batas waktu habis komunikasi (*communication timeouts*). Sebaliknya, jika Anda menyajikan sebaran mentah tak teragregasi sebanyak enam puluh ribu titik per jam kepada auditor, mata pengamat akan tenggelam dalam derau visual dan melewatkan hanyutan (*drift*) termodinamika jangka panjang.

Laporan kilat profesional mempertahankan keduanya: sistem mengakuisisi sampel mentah frekuensi tinggi, mengarsipkannya dalam penyimpanan deret waktu yang tidak dapat diubah (*immutable*), dan menyusun setiap titik yang diplot melalui agregasi statistik yang ketat dan dapat diaudit.

(Lihat Gambar 04 untuk perbandingan metrologis antara fluktuasi turbulen langsung secara fisik vs. kecurangan garis datar akibat pembekuan *buffer*).

## Akuisisi Mentah pada 1 Hz, Kemudian Rata-Rata Enam Puluh Detik

Laju akuisisi standar untuk semua saluran primer dalam panduan lapangan ini adalah **1 Hz (satu sampel per detik per saluran)**.
- **Mengapa 1 Hz Diwajibkan**: Laju pengambilan sampel 1 Hz menangkap fenomena fisik sub-menit yang kritis: lonjakan arus masuk (*inrush current*) cepat saat tahap pemanas dinyalakan, waktu pemutusan kontaktor 14 milidetik selama uji penurunan pasokan tunggal, dan lonjakan tekanan dinamis akibat pergerakan katup yang cepat. Mengambil sampel sekali setiap 10 atau 30 detik bertindak sebagai filter lolos-rendah (*low-pass filter*) parah yang membutakan pengamat dari transien yang berbahaya.
- **Rata-Rata Enam Puluh Detik**: Setiap titik formal yang diplot pada grafik deret waktu laporan kilat mewakili **rata-rata aritmatika dari enam puluh sampel mentah 1 detik berturut-turut**:
 $$\mu_t = \frac{1}{60} \sum_{i=1}^{60} x_i$$
 di mana setiap titik diberi stempel waktu dengan waktu mulai yang tepat dari interval enam puluh detik tersebut (misalnya, `14:22:00.000Z`).
- **Aturan Sampel Hilang**: Jika *edge gateway* atau *poller* Modbus mengalami putus komunikasi selama menit tersebut, menghasilkan hanya 52 sampel valid dari yang seharusnya 60 sampel, menit tersebut ditandai **PARSIAL (*PARTIAL*)** dalam blok data. Dalam keadaan apa pun, skrip pelaporan tidak boleh menyalin rata-rata menit sebelahnya atau mengarang interpolasi linear demi "menjaga kurva tetap terlihat mulus". Kurva mulus yang menutupi terputusnya komunikasi adalah kebohongan audit.

## Gerbang Varians: Menangkap Kecurangan Data Basi

Enam puluh sampel mentah yang merupakan salinan identik dari satu nilai pecahan (*float*) tunggal dalam *cache* bukanlah rata-rata 60 sampel. Itu adalah satu nilai tunggal yang mengenakan enam puluh stempel waktu.

Dalam aliran fluida turbulen yang mengalirkan 176,5 LPM cairan melalui diameter pipa 1,5 inci (DN39), bilangan Reynolds dengan mudah melampaui Re ≈ 28.000. Aliran fluida dalam rezim ini sangatlah turbulen. Pusaran mikro (*micro-eddies*) konvektif, pelepasan pusaran (*vortex shedding*) lapisan batas, dan frekuensi lintasan sudu impeler pompa secara konstan menghasilkan fluktuasi termal dan tekanan mikroskopis.
- RTD imersi fisik asli dalam fluida langsung akan selalu menunjukkan varians sampel bukan-nol:
 $$\sigma_t^2 = \frac{1}{60} \sum_{i=1}^{60} (x_i - \mu_t)^2 > 0$$
 Biasanya, aliran suhu 1 detik yang sehat menunjukkan deviasi standar sebesar σ ≈ 0,05 K hingga 0,20 K (σ² ≈ 0,0025 hingga 0,0400 K²).
- **Tanda Garis Datar Kecurangan**: Jika *thread* komunikasi *edge gateway* terkunci, atau jika *driver* ADC macet dan terus menggemakan register terakhir yang diketahui dari memori RAM, nilai yang tercatat akan menjadi datar secara matematis. Setiap sampel selama rentang lima menit terbaca tepat 45,000000°C hingga ke bit paling tidak signifikan (*least significant bit*). Varians sampel terhitung runtuh menjadi:
 $$\sigma_t^2 \equiv 0,000000\,\text{K}^2$$

Dalam *loop* pendinginan cair yang aktif, varians yang tepat bernilai nol adalah hal yang mustahil secara fisik. Itu adalah bukti nyata tak terbantahkan (*smoking gun*) dari **kecurangan data basi (*stale data fraud*)**.

Mesin penyerapan data otomatis laporan kilat harus menjalankan pemeriksaan varians terus-menerus:
$$\text{Jika } \sigma_t^2 \le 1,0 \times 10^{-4}\,\text{K}^2 \text{ selama lebih dari 3 menit berturut-turut, aktifkan bendera } CHANNEL\_FROZEN\_STALE.$$
Ketika bendera ini aktif, mesin pelaporan harus menolak blok menit tersebut, membunyikan peringatan yang dapat didengar, dan menolak menghitung nilai rata-rata yang patuh. Pengulangan data basi secara otomatis menggagalkan dataran tinggi langkah beban.

## Persyaratan Empat Ringkasan pada Setiap Langkah

Setiap kali blok data langkah disusun untuk laporan kilat, melaporkan rata-rata aritmatika sederhana saja dilarang keras. Nilai rata-rata semata dapat menyembunyikan lonjakan lokal yang berbahaya.

Setiap blok data langkah harus melaporkan **empat kuantitas statistik wajib** untuk setiap saluran aktif di sepanjang masa jeda kondisi tunak:
1. **Nilai Minimum ($\min$)**: Pembacaan mentah 1 detik terendah yang tercatat selama masa jeda.
2. **Nilai Maksimum ($\max$)**: Pembacaan mentah 1 detik tertinggi yang tercatat selama masa jeda.
3. **Rata-Rata Aritmatika (μ)**: Nilai garis dasar pusat di seluruh sampel yang valid.
4. **Deviasi Standar Sampel (σ)**: Ukuran turbulensi fisik dan stabilitas kendali.

### Mengapa Nilai Maksimum Sangat Penting
Pertimbangkan langkah beban 120 kW dengan suhu pendingin rata-rata sebesar 45,0°C. Jika pompa sempat mengalami kavitasi sejenak atau gelembung udara melewati bejana pemanas selama 10 detik, suhu fluida lokal mungkin telah melonjak ke 68,5°C sebelum kembali pulih.
- Dalam rata-rata 15 menit dari 900 titik data, lonjakan 10 detik sebesar 68,5°C tersebut hanya akan menaikkan rata-rata sebesar 0,26 K yang dapat diabaikan—pergeseran yang akan dianggap remeh oleh auditor mana pun sebagai kesalahan pembulatan.
- Namun melaporkan nilai maksimum langsung mengekspos puncak tersebut: $\max = 68,5°C$. Hal ini seketika memperingatkan tim rekayasa bahwa batas suhu selang EPDM telah dilanggar dan bahwa kavitasi telah terjadi.

Laporan yang menghilangkan nilai maksimum adalah upaya untuk mengubur kondisi operasional ekstrem di dalam rata-rata yang tampak nyaman. Wajibkan keempat angka ini pada setiap baris.

## Aturan Matematis untuk Jumlah Cabang dan Total

Saat menjumlahkan aliran dan daya di beberapa kabinet paralel, aturan aritmatika harus menghormati pemipaan fisik dan topologi listrik:

- **Aliran Volumetrik Total**: Harus dihitung secara ketat dari penjumlahan masing-masing pengukur aliran pusaran (*vortex flow meter*) cabang individual:
 $$Q_{\text{total}} = \sum_{k=1}^N Q_{\text{branch},k}$$
 Jangan menjumlahkan pengukur aliran ultrasonik *header* utama dan pengukur cabang individual secara bersamaan lalu mengklaim bahwa *loop* tersebut mengalirkan cairan dua kali lipat!
- **Aturan Pengukur Hilang**: Jika pengukur aliran Kabinet 3 gagal atau putus komunikasi, Q_total menjadi tidak lengkap. Laporan kilat harus melaporkan: *"Aliran total: TIDAK LENGKAP (pengukur Kabinet 3 offline)."* Dalam keadaan apa pun, skrip otomatis tidak boleh memperkirakan aliran Kabinet 3 dengan merata-ratakan Kabinet 1, 2, dan 4! Angka perkiraan dalam suatu penjumlahan adalah fabrikasi rekayasa yang curang.
- **Daya Listrik Total**: Harus dihitung dari daya fasa diskret dari setiap penyulang cabang:
 $$P_{\text{total}} = \sum_{k=1}^N \left( P_{A,k} + P_{B,k} \right)$$
 Jangan melaporkan pembacaan daya transformator gardu induk di hulu dan menyebutnya sebagai beban bank beban. Transformator hulu mencakup rugi-rugi kabel, pencahayaan, dan daya pompa *chiller* bantu yang tidak ada hubungannya dengan bank beban cair.

## Memberi Anotasi pada Transisi Langkah Dinamis

Untuk skenario Perubahan Langkah Mendadak dan Beban Lebih, grafik deret waktu harus secara eksplisit menganotasi detik tepat saat perintah dikeluarkan:
- Penanda garis putus-putus merah vertikal harus mengindikasikan t_command.
- Penanda biru vertikal kedua harus mengindikasikan t_settled, yaitu saat suhu fluida dan daya mencapai dataran tinggi tunak barunya.
- Label grafik harus menyatakan waktu naik teramati (Δt_rise) dan denyut tekanan transien puncak (ΔP_surge).

Lonjakan tanpa anotasi pada grafik akan ditafsirkan sebagai kesalahan fatal oleh pihak yang skeptis dan sebagai fitur operasional yang brilian oleh pihak yang optimis. Hanya stempel waktu yang presisi dan berlabel yang dapat mencegah perdebatan subjektif.

## Keputusan yang Harus Dicatat

Di bagian metrologi pada laporan kilat, catat fakta-fakta berikut:

- Frekuensi pengambilan sampel 1 Hz yang terverifikasi dari perekam data *edge* dan lokasi arsip CSV mentah yang tidak dapat diubah (*immutable*).
- Varians sampel terhitung (σ²) untuk setiap saluran di sepanjang jeda tunak, yang mengesahkan bahwa σ² > 0.
- Tabel Empat Ringkasan (Min, Max, Mean, StdDev) untuk setiap parameter yang dipantau pada setiap langkah beban.
- Daftar tersertifikasi dari pengukur aliran cabang yang disertakan dalam penjumlahan aliran total.
- Stempel waktu beranotasi yang tepat untuk semua transisi perintah langkah beban dan pemutusan pemutus arus.
