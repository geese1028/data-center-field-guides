Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 15. Analisis Algoritmik: Detektor Daring dan CPOP Luring

Kelima kelulusan skenario tetap menjadi penilaian manusia yang mutlak dalam pengujian bank beban. Sebuah algoritma tidak berhak memegang pena penilaian.

Namun, dalam kampanye komisioning modern yang melibatkan beberapa kluster paralel kelas megawatt, deteksi anomali algoritmik bertindak sebagai "penggaris" objektif yang sangat berharga. Algoritma mengidentifikasi transisi fisik halus yang mungkin terlewatkan oleh mata manusia—katup hidrolik tanpa perintah yang merayap menutup selama masa jeda yang tampak stabil, satu elemen pemanas yang terbakar di dalam selongsong imersi, atau pengalihan aliran cairan pendingin sekunder yang disebabkan oleh manuver katup fasilitas yang tidak tercatat.

Bab ini mendefinisikan batasan operasional ketat yang mengatur dua kerangka kerja deteksi titik perubahan (*changepoint*) daring (**Focus** dan **FLOC**) serta satu metode pencocokan linear searah potongan (*piecewise-linear*) luring (**CPOP**).

(Lihat Gambar 05 untuk bentuk gelombang uji beban multitaraf, linimasa pemicu daring, segmentasi linear searah potongan luring, dan protokol klasifikasi kandidat algoritmik).

## Daring versus Luring: Perbedaan Mendasar

Laporan kilat (*flash report*) menegakkan perbedaan mutlak antara metode daring (*online*) dan luring (*offline*):

- **Metode Daring (Focus, FLOC)**: Berjalan secara berurutan dan *real-time* saat telemetri tiba detik demi detik selama jendela pengujian aktif. Metode ini dapat mengeluarkan bendera kejadian kandidat saat mesin sedang beroperasi. Metode ini dirancang untuk kesadaran situasional langsung (*live situational awareness*).
- **Metode Luring (CPOP)**: Berjalan secara ketat *setelah berkas ekspor dihentikan, ditutup, dan di-hash secara kriptografis*. Metode ini menganalisis seluruh deret waktu historis secara global.

### Dua Aturan Protokol Utama:
1. **Jangan pernah menjalankan metode luring pada berkas aktif yang masih bertambah lalu menyebut hasilnya sebagai "daring".** Algoritma luring mengasumsikan bahwa ia memiliki akses ke kumpulan data lengkap; menjalankannya pada aliran data yang belum ditutup menghasilkan artefak tepi yang tidak stabil yang memicu alarm palsu.
2. **Jangan pernah menjalankan detektor daring pada berkas yang telah diedit, dibersihkan, atau difilter, lalu menyebut hasilnya sebagai sebuah "penemuan".** Detektor daring harus mengevaluasi aliran data mentah secara *real-time*. Menjalankannya pada CSV yang telah diedit setelah pengujian selesai hanyalah mencocokkan kurva pada suatu *fait accompli* (fakta yang sudah terjadi).

## Detektor Daring 1: Focus

**Focus** (*Fast Online Changepoint Detection for Poisson and Gaussian streams*) memantau satu saluran telemetri kontinu tunggal untuk mendeteksi pergeseran nilai rata-rata atau varians tanpa mengharuskan berkas data berakhir terlebih dahulu.

Metode matematis ini didokumentasikan dalam literatur yang ditinjau sejawat oleh Romano, Ward, Fan, Rigaill, Runge, Eckley, dan Fearnhead (*arXiv:2607.19961*, 2026). Jika Anda menggunakan Focus dalam *pipeline* komisioning Anda, sitasi makalah tersebut berdasarkan judulnya; jangan mereproduksi penurunannya di dalam laporan kilat.

### Aturan Operasional untuk Focus
- **Pemantauan Saluran Tunggal**: Focus harus diterapkan pada **satu saluran fisik mentah pada satu waktu**—khususnya suhu cairan pendingin kembali (T_out), aliran volumetrik (Q_v), atau daya aktif (P_elec). Menerapkannya pada indeks komposit gabungan (seperti "indeks kinerja pendinginan" buatan) akan mengaburkan akar penyebab fisik dari pergeseran yang terdeteksi.
- **Ambang Batas yang Dinyatakan Sebelumnya**: Ambang batas deteksi anomali (λ) harus dihitung dan dituliskan pada lembar persyaratan *sebelum jendela pengujian dibuka*.
- **Larangan Penyetelan Ulang Pasca-Kejadian (*Post-Hoc*)**: Jika Focus memicu peringatan selama masa jeda penahanan beban, Anda dilarang keras menurunkan sensitivitas atau menggeser ambang batas untuk membungkam peringatan tersebut! Mengubah ambang batas setelah melihat data adalah pengakuan bahwa proses tersebut tidak stabil. Catat stempel waktu kandidat tersebut dan lanjutkan.

## Detektor Daring 2: FLOC

**FLOC (*Fast Localized Online Changepoints*)** adalah detektor daring komplementer yang dirancang untuk melacak rasio varians lokal dan pergeseran tren jangka pendek di seluruh jendela geser yang berdekatan (misalnya, membandingkan jendela tertinggal 30 detik terhadap garis dasar historis 120 detik).

### Arti dari Pemicu (*Hit*) Daring
Ketika Focus atau FLOC memicu peringatan selama pengujian aktif, pemicu tersebut adalah **stempel waktu kandidat**. Itu bukan penilaian otomatis.

Operator dan Pencatat harus menangani stempel waktu kandidat tersebut melalui protokol perbandingan yang ketat:
1. **Bandingkan Pemicu Terhadap Log Perintah Operator**:
 - Jika pemicu kandidat terjadi pada pukul `14:30:02 UTC`, dan log perintah Operator mengonfirmasi bahwa langkah beban dari 60 kW ke 90 kW diperintahkan pada pukul `14:30:00 UTC`, pemicu tersebut diklasifikasikan sebagai **LANGKAH TERDUGA (*EXPECTED STEP*)**. Detektor hanya melihat transisi skenario yang memang Anda perintahkan.
 - Jika pemicu kandidat terjadi pada pukul `14:42:15 UTC`—dua belas menit di dalam masa jeda tunak 15 menit di mana tidak ada perintah yang dikeluarkan—pemicu tersebut diklasifikasikan sebagai **PATAHAN TENGAH-PENAHANAN TANPA PERINTAH (*UNCOMMANDED MID-HOLD BREAK*)**.
2. **Tindakan Manusia untuk Patahan Tengah-Penahanan**:
 - Pencatat menandai dataran tinggi beban untuk inspeksi segera.
 - Jika protokol pengujian yang dinyatakan sebelumnya mewajibkan pembatalan untuk patahan tanpa perintah, pemanasan segera dimatikan.
 - Jika protokol mengizinkan penyelesaian, masa jeda diselesaikan, namun penahanan kondisi tunak **DIPISAHKAN (*SPLIT*)** pada stempel waktu pemicu tersebut. Periode sebelum pemicu boleh dievaluasi untuk kepatuhan parsial; periode setelah pemicu tidak otomatis mewarisi kelulusan.

### Larangan Merata-ratakan Pemicu yang Tidak Sepakat
Jika FLOC memicu peringatan pada pukul `14:42:10 UTC` dan Focus memicu peringatan pada pukul `14:42:25 UTC`, **jangan pernah merata-ratakan kedua stempel waktu tersebut** (`14:42:17.5 UTC`) lalu menyebutnya sebagai titik perubahan! Merata-ratakan dua keluaran algoritmik menciptakan stempel waktu sintetis yang tidak berkorespondensi dengan apa pun dalam realitas fisik. Catat kedua waktu kandidat tersebut secara berdampingan dalam laporan, dan biarkan auditor manusia memeriksa sampel mentah 1 detik di sekitar kedua titik tersebut.

## Metode Luring: CPOP (Partisi Optimal Linear Searah Potongan Kontinu)

Setelah kampanye pengujian selesai, berkas ekspor dihentikan, dan *hash* SHA-256 disegel, tim rekayasa dapat menerapkan **CPOP** untuk menganalisis penahanan kondisi tunak.

Didokumentasikan oleh Fearnhead, Maidstone, dan Letchford (*Journal of Computational and Graphical Statistics*, 2019, DOI: 10.1080/10618600.2018.1512868), CPOP mencocokkan model linear searah potongan (*piecewise-linear*) kontinu ke deret waktu, mengidentifikasi momen-momen tepat di mana kemiringan (*slope*) fisik data berubah sembari meminimalkan biaya pencocokan L2 dengan penalti β pada jumlah perubahan kemiringan:

$$\text{Biaya} = \min_{K, \tau} \sum_{k=0}^K \sum_{i=\tau_k+1}^{\tau_{k+1}} (y_i - f_k(i))^2 + \beta \cdot K$$

di mana K adalah jumlah titik perubahan, f_k adalah segmen linear, dan β adalah parameter penalti yang dinyatakan sebelumnya.

### Hal yang Dievaluasi CPOP
CPOP diterapkan secara eksklusif pada bagian penahanan kondisi tunak dari masa jeda, dengan sengaja mengecualikan transien pemanasan termal yang telah diketahui (t ≥ 4τ).
- **Satu Kemiringan Bersih Tunggal (K = 0)**: Jika CPOP mencocokkan penahanan sebagai satu garis horizontal tunggal dengan kemiringan mendekati nol (|m| ≤ 0,001 K/s), hal ini memberikan konfirmasi matematis bahwa dataran tinggi tersebut mencapai keseimbangan termal sejati.
- **Patahan Kemiringan di Tengah Penahanan (K ≥ 1)**: Jika CPOP mendeteksi titik perubahan di tengah-tengah penahanan tunak, hal ini mengindikasikan bahwa telah terjadi pergeseran fisik:
 - Jika daya listrik datar, tetapi kemiringan suhu fluida tiba-tiba berbelok ke atas, CPOP telah mendeteksi pembatasan aliran hidrolik (seperti pergeseran katup tanpa perintah atau penyumbatan saringan).
 - Jika kemiringan suhu fluida tiba-tiba berbelok ke bawah, ini mengungkap kebocoran katup *bypass* yang mencampurkan fluida dingin ke dalam aliran kembali.

### Hal yang Tidak Dapat Dinyatakan oleh CPOP
- CPOP tidak dapat menyatakan bahwa dataran tinggi beban tersebut telah lulus.
- CPOP tidak dapat memverifikasi bahwa kenaikan suhu cocok dengan daya listrik.
- CPOP tidak dapat mengonfirmasi bahwa diferensial suhu memiliki tanda yang benar (T_out > T_in). Satu kemiringan tunggal yang terpasang dengan indah yang mewakili cairan dingin masuk panas dan keluar lebih dingin tetaplah sebuah pemeriksaan tanda yang gagal!

CPOP adalah penggaris yang mengukur kemiringan geometris. Lembar persyaratan dan insinyur manusialah yang memberikan penilaiannya.

## Keputusan yang Harus Dicatat

Di bagian analisis algoritmik pada laporan kilat, dokumentasikan:

- Nama implementasi perangkat lunak dan nomor versi untuk Focus, FLOC, dan CPOP.
- Ambang batas anomali yang dinyatakan sebelumnya λ dan penalti luring β yang ditulis sebelum penyerapan data.
- Tabel lengkap dari semua stempel waktu pemicu kandidat, berdampingan dengan stempel waktu log perintah Operator.
- Klasifikasi manusia untuk setiap kandidat: *Langkah Terduga (Expected Step)*, *Inspeksi / Pisahkan Penahanan (Inspect / Split Hold)*, atau *Tidak Berdampak (No Impact)*.
- Paraf Orang Asing yang mengesahkan bahwa alat algoritmik digunakan semata-mata sebagai penggaris diagnostik dan tidak mengeluarkan penilaian otomatis.
