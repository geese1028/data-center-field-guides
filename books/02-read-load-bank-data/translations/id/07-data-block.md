Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 7. Blok Data dan Rekonsiliasi Keseimbangan Kalor

Setiap dataran tinggi (*plateau*) beban yang diklaim oleh laporan kilat (*flash report*) sebagai bukti harus memiliki blok data yang identik dan terstandarisasi.

Blok data bukanlah kumpulan angka tak terstruktur yang dilemparkan begitu saja ke atas halaman. Blok data adalah neraca termodinamika sistematis yang memuat lima bagian wajib:
1. **Nilai Setelan & Perintah** (Niat yang dinyatakan sebelumnya);
2. **Garis Dasar Kondisi Awal** (Kondisi referensi tepat sebelum langkah beban dimulai);
3. **Data Distribusi Listrik** (Energi terverifikasi yang disalurkan ke elemen pemanas);
4. **Data Entalpi Hidrolik** (Kalor yang diserap ke dalam aliran cairan);
5. **Udara Pendamping & Penutupan Termal** (Rekonsiliasi keseimbangan energi prinsip pertama total).

Kehilangan salah satu saja dari kelima judul ini bukanlah pilihan pemformatan yang ekonomis; itu adalah penghilangan klaim rekayasa yang mendasar. (Lihat Gambar 06 untuk diagram Sankey dekomposisi energi yang lengkap, tabel rekonsiliasi empat langkah, dan empat moda kegagalan diagnostik).

## Judul 1: Nilai Setelan dan Perintah

Bagian pertama dari blok data mencatat perintah yang diberikan ke mesin *sebelum* masa jeda (*dwell*) dimulai:
- Beban listrik yang diperintahkan: misalnya, 120,0 kW (atau persentase spesifik dari beban nominal: 25%, 50%, 75%, 100%, 110%).
- Pembagian daya yang diperintahkan di seluruh penyulang ganda: misalnya, Penyulang A = 60,0 kW, Penyulang B = 60,0 kW.
- Posisi katup modulasi yang diperintahkan: misalnya, TCV = 100% terbuka penuh (atau posisi katup penyeimbang terkunci = 4,2 putaran).
- Kecepatan *blower* udara pendamping yang diperintahkan: misalnya, 100% (atau tetap 1200 CFM).

Nilai perintah harus dicatat dari log kendali supervisi sebelum jam hitung dimulai. Merekonstruksi "perintah" dengan cara merata-ratakan daya yang teramati selama masa jeda adalah perhitungan melingkar: tindakan tersebut mengubah hasil pengukuran menjadi nilai setelan (*setpoint*) buatan.

## Judul 2: Garis Dasar Kondisi Awal

Bagian kedua mendokumentasikan kondisi sistem selama satu menit tepat sebelum transisi langkah beban dimulai:
- Suhu awal pendingin pasokan (T_in,init) dan suhu kembali (T_out,init).
- Laju aliran volumetrik awal (Q_v,init) dan tekanan diferensial manifold awal (ΔP_init).
- Stempel waktu menit garis dasar (waktu mulai dan selesai hingga hitungan detik).

Garis dasar ini sangat penting untuk memisahkan kenaikan termal kondisi tunak dari hanyutan (*drift*) suhu latar belakang yang terjadi di dalam *loop* pendinginan primer fasilitas.

## Judul 3: Data Distribusi Listrik

Bagian ketiga memerinci daya listrik aktif yang ditarik oleh elemen pemanas. Dalam konfigurasi 3-fasa 415 V penyulang ganda industri, melaporkan satu angka agregat "kilowatt" saja adalah tindakan yang tidak memadai. Laporan harus menyediakan:
- **Metrik Penyulang A**: Tegangan saluran-ke-saluran (V_AB, V_BC, V_CA), arus saluran (I_A, I_B, I_C), total daya aktif Penyulang A (P_A), dan faktor daya (PF_A).
- **Metrik Penyulang B**: Tegangan saluran-ke-saluran, arus saluran, total daya aktif Penyulang B (P_B), dan faktor daya (PF_B).
- **Daya Aktif Total**: 
 $$P_{\text{elec}} = P_A + P_B$$
- **Verifikasi Keseimbangan Fasa**: Ketidakseimbangan arus antarfasa harus memenuhi I_unbalance ≤ 2,0%. Arus yang sangat tidak seimbang mengindikasikan bahwa satu kelompok resistor telah putus (*open-circuit*) atau kutub kontaktor internal telah terkorosi/berlubang (*pitted*) sehingga gagal menutup sempurna.

## Judul 4: Data Entalpi Hidrolik

Bagian keempat menangkap penyerapan kalor termodinamika oleh fluida pendingin. Hal ini memerlukan metrologi akurasi tinggi di enam parameter fisik:
1. **Suhu Cairan Pendingin Pasokan (T_in)**: Diukur melalui RTD Pt100 4-kawat yang terendam dalam aliran inti ($1/3 \sim 1/2 D$).
2. **Suhu Cairan Pendingin Kembali (T_out)**: Diukur di hilir bejana pemanas setelah pencampuran fluida sempurna.
3. **Kenaikan Suhu Bersih (ΔT)**: 
 $$\Delta T = T_{\text{out}} - T_{\text{in}}$$
4. **Laju Aliran Volumetrik (Q_v)**: Diukur melalui pengukur aliran pelepasan pusaran (*vortex shedding flow meter*) terkalibrasi (dilaporkan dalam liter per menit, LPM).
5. **Properti Termofisik Fluida**: Densitas (ρ) dan kapasitas kalor spesifik (C_p) harus dievaluasi pada suhu limbak (*bulk*) rata-rata fluida:
 $$\bar{T} = \frac{T_{\text{in}} + T_{\text{out}}}{2}$$
 Untuk larutan standar Propilen Glikol 25% / Air 75% (PG25) pada $\bar{T} = 40,0°C$, nilai standarnya adalah:
 $$\rho = 1025,0\,\text{kg/m}^3, \quad C_p = 3,980\,\text{kJ/(kg}\cdot\text{K)}$$
6. **Kalor Termal Cairan Terinferensi (Q_liquid)**: 
 Diturunkan langsung dari termodinamika prinsip pertama:
 $$Q_{\text{liquid}} = \dot{m} \cdot C_p \cdot \Delta T = \left( Q_v \times \frac{\rho}{60,000} \right) \cdot C_p \cdot (T_{\text{out}} - T_{\text{in}})$$

Untuk model referensi edukasional garis dasar yang beroperasi pada beban penuh nominal (Q_v = 176,5 LPM, ΔT = 10,04 K):
$$\dot{m} = 176,5 \times \frac{1025,0}{60,000} = 3,015\,\text{kg/s}$$
$$Q_{\text{liquid}} = 3,015\,\text{kg/s} \times 3,980\,\text{kJ/(kg}\cdot\text{K)} \times 10,04\,\text{K} = 120,48\,\text{kW} \times \text{rasio pemisahan} \approx 98,6\,\text{kW}$$

## Judul 5: Udara Pendamping & Penutupan Termal Prinsip Pertama

Dalam arsitektur AI kelas NVL72, sekitar 16% hingga 20% dari total kalor rak dibuang langsung ke udara aula data oleh *transceiver* optik, tahap konversi daya papan induk (*motherboard*), dan modul memori. Bagian udara pendamping harus menangkap kalor sensibel ini:
- Suhu udara bola kering masuk (T_air,in) dan suhu udara keluar buang (T_air,out).
- Laju aliran massa udara (ṁ_air) yang diturunkan dari RPM *blower* dan tekanan diferensial nosel terkalibrasi.
- Kalor sensibel udara terinferensi:
 $$Q_{\text{air}} = \dot{m}_{\text{air}} \cdot C_{p,\text{air}} \cdot (T_{\text{air,out}} - T_{\text{air,in}})$$

### Persamaan Keseimbangan Energi Prinsip Pertama
Berdasarkan hukum pertama termodinamika, energi listrik aktif yang disalurkan ke bank beban harus sama dengan total kalor yang meninggalkan batas kabinet ditambah kehilangan kalor parasitik tanpa insulasi:
$$P_{\text{elec}} = Q_{\text{liquid}} + Q_{\text{air}} + Q_{\text{chassis\_loss}}$$

Di mana kehilangan kalor dinding sasis tanpa insulasi ($Q_chassis\_loss$) melalui konveksi alami dan radiasi biasanya dibatasi ≤ 2,0% dari total daya ketika insulasi selimut keramik internal dipasang dengan benar.

### Gerbang Rasio Penutupan Entalpi
Laporan kilat mengevaluasi **Rasio Penutupan Entalpi**:
$$\text{Rasio Penutupan} = \left[ 1,0 - \frac{|P_{\text{elec}} - (Q_{\text{liquid}} + Q_{\text{air}})|}{P_{\text{elec}}} \right] \times 100\%$$

Untuk meraih predikat **LULUS (*PASS*)** pada blok data langkah beban, penutupan energi harus memenuhi:
$$\text{Rasio Penutupan} \ge 97,0\% \quad \left( \text{atau diskrepansi energi } \le 3,0\% \right)$$

Jika P_elec = 120,0 kW, tetapi jumlah entalpi cairan (Q_liquid = 75,0 kW) dan kalor udara (Q_air = 19,0 kW) hanya 94,0 kW, rasio penutupannya hanyalah 78,3%! Terdapat 26,0 kW energi yang hilang!
- Diskrepansi ini tidak boleh dihaluskan dengan menambahkan "faktor efisiensi" atau "koreksi kehilangan" yang tidak terdokumentasi.
- Kegagalan penutupan entalpi sebesar 26 kW mengindikasikan cacat fisik yang parah: fluida mengalami hubungan pendek (*bypass*) di sekitar bejana pemanas melalui katup *bypass* yang terbuka, faktor kalibrasi pengukur aliran (*K-factor*) salah, atau RTD terpasang pada cabang pipa buntu (*dead-leg*) yang stagnan.
- Kegagalan penutupan energi menggagalkan dataran tinggi langkah beban tanpa syarat.

## Hierarki Pelaporan: Satu Kabinet, Kemudian Ringkasan Kluster

Saat melaporkan kluster uji multikabinet:
1. Setiap kabinet individual harus memiliki blok data diskretnya sendiri yang dicetak terlebih dahulu, lengkap dengan seluruh lima judul dan statistik empat ringkasan ($\min, \max, μ, σ$).
2. Di bawah blok kabinet individual, **Blok Ringkasan Kluster** disusun, yang melaporkan total daya listrik, total penyerapan entalpi cairan, total kalor udara, dan Rasio Penutupan Entalpi tingkat kluster.

Ringkasan kluster yang terlihat tenang dan seimbang tidak dapat membatalkan kegagalan satu kabinet individual yang gagal dalam penutupan energinya. Jika Kabinet 4 kehilangan kalor sebesar 20 kW sementara Kabinet 1, 2, dan 3 seimbang, Kabinet 4 adalah kegagalan. Anda tidak boleh merata-ratakan Kabinet 4 ke dalam kluster demi menghasilkan kelulusan sintetis.

## Keputusan yang Harus Dicatat

Untuk setiap blok data langkah yang disusun dalam laporan kilat, catat:

- Nilai setelan yang diperintahkan untuk daya aktif, pembagian daya penyulang ganda, dan posisi katup penyeimbang.
- Suhu fluida dan udara garis dasar awal sebelum langkah beban dimulai.
- Tegangan listrik 3-fasa, arus, faktor daya, dan total daya aktif P_elec.
- Suhu fluida terukur, aliran volumetrik, densitas fluida, kalor spesifik, dan entalpi cairan terinferensi Q_liquid.
- Suhu udara terukur, laju aliran udara, dan kalor udara pendamping terinferensi Q_air.
- Rasio Penutupan Entalpi Prinsip Pertama yang dihitung, yang mengesahkan bahwa penutupan ≥ 97,0%.
- Paraf Pencatat dan Orang Asing yang mengonfirmasi keseimbangan energi.
