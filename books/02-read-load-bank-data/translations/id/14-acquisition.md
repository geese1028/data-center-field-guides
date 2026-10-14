Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 14. Akuisisi Telemetri, Pipeline Modbus-TCP, dan MQTT

Laporan kilat (*flash report*) atau grafik otomatis hanya sejujur *pipeline* telemetri digital yang mengisi sel-selnya.

Dalam pengujian pusat data berskala megawatt modern, telemetri tidak muncul secara ajaib di dalam basis data. Data tersebut menempuh serangkaian lompatan (*hops*) fisik dan digital yang diskret: dari elemen RTD imersi yang terbasahi fluida, melalui pengonversi analog-ke-digital (ADC) lokal, melintasi *fieldbus* Modbus-TCP industri, melalui *gateway* pengumpul *edge*, dan melintasi *broker* pesan MQTT menuju penyimpanan deret waktu yang tidak dapat diubah (*immutable*).

Jika ada satu lompatan saja dalam rantai tersebut yang gagal secara diam-diam—misalnya *poller edge* membubuhkan stempel waktu baru pada *buffer* memori yang belum diperbarui, atau jika *broker* MQTT mempublikasikan pesan "tertahan (*retained*)" yang tersimpan di *cache* dari kemarin—maka laporan kilat yang dihasilkan murni sebuah fiksi belaka.

Bab ini mendefinisikan spesifikasi teknis dari setiap lompatan, memerinci struktur register Modbus yang tepat, konvensi urutan *byte* (*byte-ordering*), arsitektur *Bitmask* Kualitas, dan skema muatan (*payload*) JSON yang disyaratkan untuk menjamin integritas data.

(Lihat Gambar 02 untuk arsitektur lompatan telemetri menyeluruh dari ujung ke ujung, jebakan pertukaran *word* IEEE-754, register *Bitmask* Kualitas 16-bit, dan skema muatan JSON terstandarisasi).

## Lompatan 1 & 2: Dari Sensor Fisik ke Pemancar Lokal

Perjalanan dimulai pada batas proses fisik:
- **Suhu**: Elemen RTD Pt100 Kelas A 4-kawat yang terendam langsung ke dalam inti aliran pusat ($1/3 \sim 1/2 D$) dari pipa penurunan manifold, dipadatkan dengan senyawa termal seng oksida di dalam selongsong termal (*thermowell*) bersudut 45°.
- **Aliran Volumetrik**: Pengukur aliran pelepasan pusaran (*vortex shedding flow meter*) segaris (*inline*) yang menyediakan keluaran frekuensi digital pulsa atau frekuensi tinggi, yang kebal terhadap pergeseran viskositas fluida di seluruh rentang suhu operasi.
- **Tekanan Diferensial**: Pemancar tekanan statis piezoresistif yang terhubung ke titik sadapan statis yang rata, dipoles, dan dibor tegak lurus terhadap dinding pipa.

Pada unit pemancar, ADC Sigma-Delta 24-bit berakurasi tinggi mengambil sampel jembatan fisik pada frekuensi 1 kHz, menerapkan filter rata-rata bergerak digital lokal untuk mengeluarkan pembacaan terkalibrasi sekali per detik (**1 Hz**).

## Lompatan 3: Arsitektur Fieldbus Modbus-TCP

Pengendali internal bank beban mengekspos parameter operasionalnya melalui **Modbus-TCP (Port Ethernet 502)** standar industri atau Modbus-RTU (bus serial RS-485 yang beroperasi pada 115.200 baud, 8-N-1):

- **Koil Diskret (*Discrete Coils*, Fungsi 0x01 / 0x05)**: Status kendali biner—posisi katup solenoid (V-101 buka/tutup), status umpan balik kontaktor pemanas imersi, kontinuitas sirkuit henti darurat, dan status relai tali pendeteksi kebocoran.
- **Register Masukan (*Input Registers*, 30001+, Fungsi 0x04)**: Pengukuran sensor hanya-baca yang dihasilkan langsung oleh saluran ADC perangkat keras lokal.
- **Register Penahan (*Holding Registers*, 40001+, Fungsi 0x03 / 0x06 / 0x10)**: Nilai setelan beban yang diperintahkan, konfigurasi mode operasi, dan ambang batas alarm.

### Jebakan Urutan Byte Pecahan 32-bit IEEE-754
Satu register Modbus 16-bit tunggal tidak dapat menyimpan kuantitas rekayasa titik kambang (*floating-point*) 32-bit (seperti pembacaan suhu 45{,}12°C). Nilai titik kambang memerlukan dua register 16-bit berturut-turut (total 4 *byte*).

Arsitektur mikrokontroler yang berbeda menerapkan konvensi urutan *word* yang berbeda. Jika *gateway edge* mengasumsikan urutan *word* yang salah, angka akan rusak total:
- **CDAB (Big-Endian dengan Pertukaran Word)**: Standar industri untuk nilai pecahan Modbus.
 - Reg 40001 = `0x4234`, Reg 40002 = `0x0000` $\implies$ Terevaluasi secara benar menjadi **45{,}00°C**.
- **ABCD (Big-Endian Langsung)**:
 - Reg 40001 = `0x0000`, Reg 40002 = `0x4234` $\implies$ Terevaluasi menjadi **1{,}87 × 10^{-38}** (Sampah mikroskopis!).
- **BADC (Little-Endian dengan Pertukaran Byte)**: Terevaluasi menjadi nilai arbitrer yang sama sekali berbeda.

Lembar penyiapan kerja laporan kilat harus mencitasi konvensi urutan *word* yang tepat yang digunakan oleh *firmware* pengendali. Suhu yang tiba-tiba melompat drastis antar musim selama komisioning bukanlah keajaiban lingkungan; itu adalah kesalahan penguraian (*parsing*) pertukaran *word* yang belum diverifikasi. Perbaiki penguraian dalam konfigurasi *gateway edge*; jangan menimpa *byte* heksadesimal mentah yang masuk.

### Register Bitmask Kualitas 16-bit Wajib (Reg 40050)
Angka mentah tanpa bendera kualitas adalah penegasan yang belum terverifikasi. Pengendali bank beban harus memelihara **Register Bitmask Kualitas 16-bit (Register 40050)** khusus yang diperbarui secara *real-time* oleh diagnostik *firmware* internal:

- **Bit 0 (`0x0001`)**: `SUPPLY_TEMP_VALID` (1 = Sehat, 0 = Gangguan/Sirkuit Terbuka)
- **Bit 1 (`0x0002`)**: `RETURN_TEMP_VALID` (1 = Sehat, 0 = Gangguan/Sirkuit Terbuka)
- **Bit 2 (`0x0004`)**: `FLOW_METER_VALID` (1 = Sehat, 0 = Gangguan/Kehilangan Pulsa)
- **Bit 4 (`0x0010`)**: `SENSOR_STALE_ALERT` (Aktif jika ADC mengulang nilai identik selama > 3 detik)
- **Bit 5 (`0x0020`)**: `COMM_TIMEOUT` (Aktif jika bus pemancar internal *timeout* > 250 ms)
- **Bit 6 (`0x0040`)**: `OUT_OF_RANGE` (Aktif jika resistansi RTD melanggar batas fisik)

Jika Register 40050 mengaktifkan Bit 4, 5, atau 6, *gateway edge* harus segera mengklasifikasikan pembacaan tersebut sebagai **GANGGUAN (*FAULT*)** dan mencatat celah data yang hilang, daripada mempublikasikan angka yang rusak tersebut ke hilir.

## Lompatan 4: Polling Aktif Gateway Edge

*Gateway edge* menjalankan *loop polling* deterministik 1 Hz yang meminta data dari pengendali Modbus bank beban:
- *Poller* meminta data register masukan dan kualitas setiap 1.000 milidetik.
- **Kebijakan Batas Waktu Habis (*Timeout*)**: Jika *slave* Modbus gagal merespons dalam 250 milidetik, *poller* mencatat **BATAS WAKTU KOMUNIKASI HABIS** untuk detik tersebut.
- **Larangan Keras terhadap Pencatatan Maju Palsu (*Painting Forward*)**: *Gateway edge* dilarang keras menyimpan pembacaan terakhir yang berhasil ke dalam *cache* lalu mencapnya dengan stempel waktu detik baru! Mencatat maju pembacaan sebelumnya untuk mencegah sel kosong adalah fabrikasi data yang disengaja. *Poll* yang gagal harus dicatat sebagai `NaN` atau `MISSING`. Jika tiga *poll* berturut-turut gagal, dataran tinggi beban ditandai **TIDAK VALID (*INVALID*)**.

## Lompatan 5: Broker Telemetri MQTT dan Skema JSON

*Gateway edge* mengemas telemetri 1 detik langsung dan mempublikasikannya ke *broker* pesan MQTT lokal:
- **Hierarki Topik**: Harus mengikuti topologi aset yang bersih dan berjenjang:
 `dc/[hall_id]/[rack_id]/telemetry` (misalnya, `dc/hall-03/lb-01/telemetry`)
- **Kualitas Layanan (*Quality of Service*)**: Harus menggunakan **QoS 1 (Pengiriman Setidaknya Sekali / *At Least Once Delivery*)** dengan *buffer* persistensi lokal guna menjamin bahwa kendala sakelar jaringan tidak menyebabkan paket hilang.

### Skema Telemetri JSON
Setiap pesan yang dipublikasikan ke *broker* harus mematuhi skema JSON terstandarisasi yang memuat blok stempel waktu, listrik, hidrolik, dan kualitas:

```json
{
 "timestamp": "2026-10-14T14:22:15.000Z",
 "rack_id": "LB-NVL72-01",
 "run_id": "RUN-2026-OCT-CX01",
 "commanded_kw": 120.0,
 "electrical": {
 "feeder_a_kw": 60.1,
 "feeder_b_kw": 59.9,
 "total_kw": 120.0,
 "voltage_v": 415.2,
 "current_a": 167.1,
 "pf": 0.999
 },
 "hydraulics": {
 "flow_lpm": 176.4,
 "supply_c": 35.08,
 "return_c": 45.12,
 "delta_t_k": 10.04,
 "dp_kpa": 112.5,
 "thermal_kw": 98.6
 },
 "companion_air": {
 "inlet_c": 24.2,
 "outlet_c": 38.5,
 "air_kw": 18.9
 },
 "quality": {
 "mask": "0x0007",
 "stale_flag": false,
 "raw_samples": 60
 }
}
```

### Dua Kebiasaan Mematikan MQTT yang Harus Dilarang
1. **Jebakan Pesan Tertahan (*Retained Message Trap*)**: Dalam protokol MQTT, pihak penerbit (*publisher*) dapat menandai pesan sebagai "tertahan (*retained*)", yang menyebabkan *broker* menyimpannya dan langsung mengirimkannya ke setiap pelanggan (*subscriber*) baru yang terhubung di kemudian hari. Jika skrip laporan kilat otomatis terhubung ke *broker* dan menyerap pesan tertahan, skrip tersebut mungkin menyerap pembacaan yang dipublikasikan tiga hari lalu selama pengujian di bengkel! Rencana pengujian harus mewajibkan: **Semua penerbit telemetri harus menyetel `retained = false`**.
2. **Salah Tafsir *Last-Will-and-Testament***: Pesan *Last-Will-and-Testament* (LWT) dari *broker* (yang dipublikasikan saat *gateway edge* terputus secara tidak terduga) harus mempublikasikan muatan kematian yang eksplisit (`{"status": "OFFLINE", "quality": "DEAD"}`). Mesin pelaporan harus segera mengenali muatan ini dan menghentikan pewaktu jeda (*dwell timers*).

## Uji Bukti Data Basi Pra-Pemanasan

Sebelum memerintahkan pemanasan pada hari pengujian, tim penguji harus mengeksekusi **Uji Bukti Data Basi Pra-Pemanasan**:
1. Dengan *pipeline* data berjalan dan mencatat data garis dasar tanpa beban, seorang operator secara fisik mencabut kabel sinyal Sensor Suhu Kembali RTD-102 (atau mencabut kabel Ethernet Modbus dari Kabinet 2).
2. Pencatat memantau dasbor langsung dan berkas CSV yang diekspor.
3. **Bukti Kepatuhan**: Ekspor harus seketika mencatat `NaN`, `GAP`, atau `DISCONNECTED` dalam waktu 1 detik, dan *Bitmask* Kualitas harus bertransisi ke `0x0040` (Gangguan Sensor).
4. **Bukti Kegagalan**: Jika dasbor atau ekspor terus menampilkan 35{,}0°C dengan stempel waktu yang terus berjalan maju, *pipeline* tersebut bersalah karena mencatat maju data basi secara palsu. Pengujian harus segera dihentikan. Anda tidak boleh menambahkan panas sampai *pipeline* telemetri membuktikan bahwa ia mampu melaporkan sensor yang mati secara jujur.

## Keputusan yang Harus Dicatat

Di bagian akuisisi pada laporan kilat, dokumentasikan:

- Revisi peta register Modbus yang terkonfirmasi dan format urutan *byte* pecahan yang terverifikasi (CDAB / *Big-Endian Word Swap*).
- Interval *polling* yang tepat (1.000 ms) dan ambang batas *timeout* yang terkonfirmasi (250 ms).
- *Endpoint broker* MQTT, *string* topik, dan konfirmasi bahwa pesan tertahan telah dinonaktifkan.
- Eksekusi tersertifikasi dari Uji Bukti Data Basi Pra-Pemanasan, mencatat detik tepat saat sensor dicabut dan detik saat *pipeline* mencatat adanya celah tersebut.
