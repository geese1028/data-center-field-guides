Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 3. Sel-Sel Prates

Gerbang prates (*pretest*) mengajukan pertanyaan langsung dan tanpa kompromi: apakah kluster bank beban ini, pada hari khusus ini, beroperasi di dalam batas-batas hidrolik, termal, dan listrik yang didefinisikan oleh spesifikasi rekayasa yang disitasi?

Prates bukanlah gradien termal. Prates adalah penjaga gerbang yang mengizinkan pengujian gradien diakui keabsahannya. Jika ada satu sel prates yang berada di luar batas, Anda tidak boleh melanjutkan ke pengujian beban bertahap. Mencoba menjalankan uji panas 120 kW pada *loop* hidronik yang tidak mampu menyalurkan laju aliran volumetrik terukurnya atau yang masuk pada suhu di luar spesifikasi hanya akan menghasilkan keseimbangan panas yang tidak valid dan tidak dapat diulang, yang membuang-buang waktu operasional fasilitas selama berjam-jam.

## Sel-Sel Prates Cairan

Untuk *loop* cairan sekunder yang menyimulasikan kluster AI berdensitas tinggi, bagian prates dari laporan kilat memerlukan tiga sel hidrolik yang berbeda, dievaluasi per kabinet dan di seluruh manifold:

### 1. Laju aliran volumetrik per kabinet (Q_v)
Spesifikasi harus menyatakan batas bawah aliran minimum (misalnya, Q_floor ≥ 170,0 LPM untuk model referensi kelas NVL72 120 kW edukasional yang beroperasi pada ΔT = 10,0 K).

- **Parameter yang Diaudit**: Laju aliran volumetrik terukur yang memasuki setiap kabinet paralel di bawah sirkulasi penuh CDU fasilitas.
- **Mengapa Sel Ini Gagal**: Jika aliran turun di bawah batas bawah (misalnya, terbaca 155,0 LPM akibat katup penyeimbang yang belum terbuka penuh, selongsong selang yang terlalu kecil, atau saringan yang tersumbat sebagian), kecepatan cairan di seluruh elemen pemanas akan anjlok. Pada kecepatan yang lebih rendah, koefisien perpindahan panas konvektif menurun, suhu selongsong lapisan batas melonjak tajam, dan fluida mengalami ekspansi termal lokal yang berlebihan.
- **Per-Kabinet vs. Jumlah Total Header**: Baris prates harus mencatat aliran untuk *setiap kabinet individual*, bukan hanya total aliran *header* *loop* sekunder. Aliran *header* sebesar 700 LPM di empat kabinet dapat terlihat sangat sehat namun menyembunyikan ketidakseimbangan hidrolik yang fatal: Kabinet 1, 2, dan 3 mungkin masing-masing menerima 200 LPM, sementara Kabinet 4 mengalami kelaparan aliran (*starvation*) pada 100 LPM. Jika Kabinet 4 kelaparan aliran, Kabinet 4 seketika menggagalkan baris prates.

### 2. Suhu pasokan pendingin (T_in)
Cairan pendingin pasokan *loop* sekunder yang disalurkan oleh CDU fasilitas harus berada tepat di dalam koridor komisioning yang dinyatakan (biasanya 35,0°C ± 1,5 K untuk arsitektur air hangat ASHRAE W4/W5).

- **Parameter yang Diaudit**: Suhu pasokan cairan primer yang diukur oleh RTD Pt100 4-kawat imersi yang menembus aliran inti berkecepatan tinggi ($1/3 \sim 1/2 D$) dari pipa penurunan (*drop*) manifold.
- **Batas Bawah Keselamatan Titik Embun**: Selain pita nilai setelan (*setpoint band*) nominal, prates harus memverifikasi bahwa suhu pasokan memenuhi aturan mutlak non-kondensasi:
 $$T_{\text{in}} \ge T_{\text{dp}} + 2,0\,\text{K}$$
 di mana T_dp adalah titik embun langsung yang dihitung dari suhu bola kering (*dry-bulb*) dan kelembapan relatif aula data. Jika pendingin dingin masuk pada 18,0°C sementara titik embun aula data adalah 21,5°C, kopling sambung-cepat tanpa insulasi dan selang EPDM akan berkeringat deras (*sweating*), meneteskan air langsung ke rak baki kabel listrik di bawahnya. Itu adalah GAGAL (*FAIL*) prates seketika.
- **Penyesuaian Aliran Tergantung Suhu**: Jika *loop* fasilitas beroperasi lebih dingin daripada desain nominal (misalnya, masuk pada 25,0°C pada pagi hari tanpa pengondisian udara), viskositas fluida meningkat hampir 30%. Batas bawah aliran harus mencitasi suhu tempat ia dikalibrasi. Batas bawah aliran yang disalin dari pengujian 40,0°C tidak dapat langsung diterapkan pada fluida 20,0°C tanpa koreksi hidrolik.

### 3. Tekanan diferensial manifold (ΔP)
Impedansi hidrolik di seluruh bank beban harus cocok dengan kurva penurunan tekanan tersertifikasi dari rak IT fisik dalam toleransi yang dinyatakan sebelumnya (biasanya ΔP_rated = 112,0 kPa ± 5,0 kPa pada 176,5 LPM).

- **Parameter yang Diaudit**: Tekanan diferensial statis yang diukur antara titik sadapan (*tap*) manifold pasokan masuk dan manifold kembali keluar (ΔP = P_in - P_out).
- **Inspeksi Sadapan Curang**: Prates harus memverifikasi bahwa titik sadapan tekanan bersih, telah dihaluskan dari sisa potongan geram (*deburred*), tegak lurus terhadap dinding pipa, dan dilengkapi dengan katup peredam kejut (*snubber valves*) untuk menghilangkan derau turbulensi frekuensi tinggi. Pembacaan tekanan diferensial yang diambil melintasi katup bola isolasi yang tercekik (*throttled*) atau adaptor yang restriktif hanya mengukur gesekan pipa, bukan impedansi rak.

## Sel-Sel Prates Udara Pendamping

Jika kampanye pengujian Anda menyertakan beban pendamping berpendingin udara (yang wajib saat memverifikasi pemisahan kalor sensibel 80:20 atau 85:15 pada arsitektur kelas NVL72), bagian prates harus mencakup dua sel udara khusus:

1. **Suhu Udara Masuk (T_air,in)**: Udara bola kering ambien yang masuk ke perforasi depan bank beban harus berada dalam rentang desain fasilitas (biasanya 22,0°C hingga 27,0°C sesuai dengan Pedoman Termal ASHRAE TC 9.9). Jika udara kembali dari pengujian sebelumnya yang tidak terisolasi mengalami sirkuit pendek ke saluran masuk, meningkatkan T_air,in hingga 42,0°C, bagian udara akan mengalami pembatasan termal (*thermal throttling*) dini.
2. **Kecepatan Aliran Udara Blower Bantu**: Kecepatan udara di seluruh tahap pemanasan bantu harus dikonfirmasi menggunakan anemometer kawat-panas (*hot-wire anemometer*) terkalibrasi atau sensor tekanan diferensial di seluruh kisi-kisi filter saluran masuk, memastikan bahwa aliran udara memenuhi ambang batas konvektif minimum (Q_air ≥ 1200 CFM per modul udara 20 kW) untuk mencegah panas berlebih pada elemen pemanas.

Jika beban pendamping udara dikecualikan dari cakupan kontrak, sel tersebut harus secara eksplisit ditandai **TIDAK BERLAKU (*NOT APPLICABLE* / N/A)** dengan tinta sebelum larian dimulai. Anda tidak boleh menyadari di tengah prates bahwa alat pengukur kecepatan udara terlupa, lalu secara retroaktif mengklaim bahwa pengujian udara "tidak berlaku".

## Cocokkan dengan Dokumen, Jangan Menjadi Dokumennya

Jebakan umum dalam laporan komisioning adalah menyalin halaman-halaman lembar data pemasaran vendor ke dalam lampiran dan mengklaim bahwa pengujian tersebut "sesuai dengan lembar data".

Lembar data vendor adalah proposal komersial. Itu bukan verifikasi rekayasa. Laporan kilat harus mempertahankan pemisahan profesional yang ketat:
- Lembar persyaratan mendefinisikan batas yang disitasi (misalnya, *"DOC-NVL72-SPEC Rev 2.4, Tabel 3: Aliran sekunder minimum = 170,0 LPM"*).
- Tabel prates mencatat angka aktual teramati yang diukur oleh instrumen terkalibrasi di lantai uji (misalnya, *"Kabinet #01 = 176,4 LPM pada 14:02:15 UTC"*).
- Kolom penilaian mencatat perbandingan matematis: **LULUS** (dalam toleransi) atau **GAGAL** (di luar toleransi).

Pembaca harus dapat melihat batas yang disitasi, nilai yang terukur, stempel waktu, dan penilaian secara berdampingan dalam satu halaman. Jika tim audit tidak dapat melacak angka yang terukur ke tag instrumen nyata, atau tidak dapat melacak nilai batas ke revisi dokumen yang dibekukan, sel tersebut berstatus terbuka. Sel yang terbuka berarti baris prates adalah **GAGAL** (*FAIL*).

## Keputusan yang Harus Dicatat

Sebelum menandatangani bagian prates dari laporan kilat, verifikasi bahwa butir-butir berikut telah didokumentasikan sepenuhnya:

- Judul dokumen spesifikasi yang disitasi, tanda revisi, dan tanggal penerbitan untuk semua batas hidrolik.
- Laju aliran volumetrik terukur untuk setiap kabinet individual dalam kluster paralel.
- Suhu pasokan pendingin yang terverifikasi dan margin titik embun aula data yang dihitung.
- Tekanan diferensial manifold ΔP terukur pada titik sadapan yang bersih dan bebas sisa geram.
- Suhu dan kecepatan udara masuk pendamping (atau pengurangan cakupan bertanda tangan N/A).
- Penentuan lulus/gagal akhir untuk gerbang prates, diparaf oleh Pemilik Lembar dan Operator.
