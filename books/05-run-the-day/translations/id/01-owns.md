Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 1. Apa yang Dimiliki Manajer Hari Ini

Seorang manajer yang mencoba memiliki desain fasilitas, perangkat lunak aplikasi pelanggan, dan garansi pabrik vendor sekaligus pada akhirnya tidak memiliki satu pun dari hal-hal tersebut. Hari ini Anda memiliki kondisi operasional fasilitas, orang-orang yang diizinkan menyentuhnya, dan catatan yang tidak dapat diubah mengenai apa yang telah dilakukan.

Bukan urusan Anda apakah basis data terdistribusi milik pelanggan berhasil melakukan sharding data dengan benar di seluruh kluster server. Yang Anda miliki adalah apakah pasokan daya ganda, laju aliran loop pendingin, dan perimeter keamanan fisik yang Anda jual kepada mereka disalurkan secara ketat dalam parameter yang ditandatangani secara kontraktual. Jika kontrak tidak mengatur suatu hal, jangan mengarang janji di dalam log operasi harian. Direktur teknis pelanggan yang berteriak di panggilan konferensi bukanlah klausul kontrak baru.

Anda tidak memiliki wewenang untuk mendesain ulang instalasi. Perubahan yang mengubah mode kegagalan switchgear listrik atau loop pendingin sekunder adalah proyek modal rekayasa (CAPEX), yang memerlukan tinjauan sejawat, studi koordinasi relai proteksi, dan persetujuan eksekutif. Tim operasi harian boleh mengusulkannya. Tim operasi harian tidak boleh menyelundupkannya ke dalam jendela pemeliharaan rutin dan menyebutnya sebagai "penyesuaian operasional biasa". Jika pekerjaan tersebut mengharuskan diagram satu garis listrik (SLD) atau diagram perpipaan dan instrumentasi (P&ID) digambar ulang, itu bukan pemeliharaan hari ini. Hentikan alat kerja seketika.

Anda tidak memiliki sertifikat berbingkai di dinding resepsionis. Plakat ISO 9001, sertifikat desain Uptime Institute Tier IV, atau penghargaan keberlanjutan perusahaan bukanlah bukti bahwa sif hari ini beroperasi secara kompeten. Bukti nyata adalah lembar hari: nama-nama operator berkualifikasi di lokasi, izin kerja aktif, inspeksi fisik yang tercatat, dan insiden yang Anda tolak untuk sembunyikan.

## Setengah Jam Pertama

Periksa empat hal berikut sebelum Anda membuka dasbor telemetri, memeriksa email, atau meminum kopi Anda:

1. **Kondisi gangguan/penurunan (Impairments) yang dibawa dari sif sebelumnya**: Generator yang dikunci dari mode mulai otomatis, zona kebakaran yang dinonaktifkan pada panel VESDA, unit distribusi pendingin (CDU) sekunder yang beroperasi pada bypass pompa tunggal, atau UPS yang berjalan pada static bypass.
2. **Izin kerja yang masih terbuka, dan menit tepat berakhirnya masing-masing izin**: Izin Kerja (Permit to Work: PTW) adalah sewa sementara atas risiko. Jika izin kedaluwarsa pada pukul 06:00 dan vendor masih berada di dalam ruang switchgear tegangan menengah, fasilitas beroperasi dalam status tidak sah.
3. **Insiden yang masih terbuka, dan siapa pemilik tiket teknisnya**: Jika insiden terjadi pada malam hari, ketahui siapa penanggung jawab teknisnya dan kondisi aman (safe state) apa yang telah ditetapkan.
4. **Perubahan yang jadwal eksekusinya hari ini, dan siapa yang secara resmi menerima risikonya**: Verifikasi bahwa setiap perubahan terjadwal memiliki Prosedur Pelaksanaan (Method of Procedure: MOP) yang disetujui dengan rencana pemulihan/pembatalan (back-out plan) yang jelas.

```
+-------------------------------------------------------------------------+
| EMPAT PEMERIKSAAN WAJIB PRA-SIF |
| |
| [1] Gangguan Aktif --> Pemadam mati, katup bypass, UPS N-1 |
| [2] Izin Terbuka --> Lokasi, lingkup kerja, cap waktu kedaluwarsa |
| [3] Insiden Aktif --> Tingkat keparahan, kondisi aman, pemilik nama|
| [4] Perubahan Hari Ini--> MOP disetujui, penerima risiko, rencana batal|
+-------------------------------------------------------------------------+
```

Jika salah satu dari keempat hal ini hilang dari log serah terima, proses serah terima dinyatakan gagal. Jangan terima radio komunikasi. Jangan tanda tangani log serah terima. Manajer fasilitas yang menandatangani serah terima yang tidak lengkap mewarisi setiap cacat tersembunyi, setiap interlock keselamatan yang dinonaktifkan, dan setiap trip peralatan tanpa catatan yang terjadi selama dua belas jam sebelumnya.

Setelah keempat hal diperiksa, berjalanlah ke lokasi fisik tempat pekerjaan hari ini akan dilakukan sebelum vendor atau kontraktor tiba di gerbang keamanan. Periksa panel listrik yang dituju, katup isolasi, dan koridor servis. Jika kondisi fisik di lapangan membuat peralatan mustahil diisolasi secara aman sesuai prosedur tertulis, dokumen prosedurnya salah. Batalkan pekerjaan. Jangan sampai Anda baru menyadari bahwa katup isolasi manual macet atau pemutus bypass digembok saat peralatan sudah telanjur dibongkar.

Tulis satu kalimat mengikat untuk hari ini sebelum kesibukan pagi dimulai. Di fasilitas profesional, kalimat itu sengaja dibuat membosankan dan lugas:
> *"Infrastruktur daya dan pendingin kritis beroperasi sepenuhnya dalam batas SLA kontraktual; semua pekerjaan pemeliharaan resmi diselesaikan di bawah MOP yang disetujui tanpa gangguan layanan; tidak ada gangguan atau penurunan sistem yang tidak tercatat di lokasi."*

Jika Anda tidak dapat menandatangani kalimat tersebut pada akhir sif dengan jujur, hari tersebut merupakan kegagalan operasional, meskipun dasbor eksekutif menyala hijau terang.

## Apa yang Tidak Boleh Anda Delegasikan

Anda boleh mendelegasikan tugas memutar handel katup, menarik keluar (rack-out) pemutus sirkuit 480V, atau mencatat pembacaan tekanan diferensial pada filter udara. Anda tidak boleh sekali pun mendelegasikan:
- Keputusan bahwa fasilitas masih beroperasi dalam batas SLA kontraktual.
- Otorisasi untuk membuka jendela perubahan yang berdampak kritis.
- Keputusan untuk menerbitkan pemberitahuan insiden resmi kepada pelanggan.

Ketiga tanggung jawab ini melekat secara eksklusif pada manajer operasi berlisensi yang sedang bertugas, atau kepada wakil yang ditunjuk secara resmi dan tertulis pada daftar penugasan sif. Grup obrolan daring bukanlah wakil yang sah.

## Keputusan yang Harus Dicatat

- Standar layanan operasi, dikutip berdasarkan judul kontrak dan nomor pasal yang tepat.
- Hal-hal yang secara tegas tidak akan Anda janjikan kepada klien hari ini.
- Empat pemeriksaan serah terima: diverifikasi ada, atau ditandai hilang/kurang.
- Kalimat penutup mengikat yang Anda berniat menandatanganinya pada akhir sif.
