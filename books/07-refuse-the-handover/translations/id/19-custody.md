Terjemahan berbantuan AI dari edisi bahasa Inggris.

# 19. Pengalihan Penguasaan Fisik (Custody) Bukanlah Basa-Basi

## Dasar Rekayasa Hak Penolakan pada Gerbang Serah Terima

Dalam proyek pembangunan pusat data baru atau ekspansi kapasitas, serah terima (Handover) dari tim konstruksi dan komisioning kepada tim operasi merupakan garis batas satu arah yang mengalihkan risiko serta tanggung jawab hukum secara permanen. Fokus bab ini pada **Pencabutan kunci master konstruksi, pengaturan ulang akses pintu (ACL), dan pengalihan penuh otoritas LOTO** adalah disiplin pertahanan mutlak agar tim operasi tidak mewarisi instalasi cacat yang belum teruji.

![19. Pengalihan Penguasaan Fisik (Custody) Bukanlah Basa-Basi](../figures/fig-06-custody-transfer-and-loto-handover.png)

$$N_{\text{spares\_on\_shelf}} \ge N_{\text{critical\_BOM}}, \quad \text{Access}_{\text{contractor}} = \text{Revoked}$$

Kontraktor dan manajer proyek konstruksi sering menekan demi target jadwal, namun begitu manajer operasi menandatangani berita acara serah terima, setiap pelanggaran SLA, titik kegagalan tunggal, dan kesalahan koordinasi relai menjadi beban operasi. Jika satu lembar bukti saja hilang, letakkan pena Anda dan **TOLAK (REFUSE)** serah terima secara resmi.

> *"Tanda tangan serah terima bukanlah ucapan terima kasih kepada kontraktor, melainkan pernyataan hukum bahwa Anda mempertaruhkan lisensi profesional Anda bahwa fasilitas ini mampu menjaga SLA 100% saat terjadi kegagalan komponen tunggal."*

## Bukti Komisioning L1–L5 dan Matriks Audit Penerimaan

Seluruh lima tingkat komisioning sesuai ASHRAE Guideline 0 / Standard 202 dan NETA ATS (L1: Uji Pabrik FAT, L2: Instalasi & Flushing, L3: Penyalaan Awal, L4: Uji Kinerja Fungsional FPT, L5: Uji Sistem Terintegrasi IST) wajib dilengkapi rekaman gelombang mentah dan sertifikat kalibrasi aktif.

| Gerbang Audit Serah Terima | Bukti Rekayasa Wajib | Kriteria Lulus (Ambang) | Pemicu Penolakan Segera (Refusal) |
| :--- | :--- | :--- | :--- |
| **Gate A: Verifikasi Gambar As-Built** | SLD, P&ID, dan diagram logika sesuai garis merah lapangan | 100% cocok dengan tag katup & setelan relai nyata | Gambar desain lama yang hanya diganti nama berkasnya |
| **Gate B: Uji Beban Terpadu L4/L5 (IST)** | Keseimbangan termal beban 100% ($\ge 8\,\text{jam}$) & Black-Start | Waktu pindah daya 2N $t_{\text{transfer}} \le 10\,\text{ms}$ | Mengganti uji beban fisik dengan gambar simulasi CFD |
| **Gate C: Kebersihan Loop Cair & Kimia** | Sertifikat flushing $50\,\mu\text{m}$, uji tekan hidrostatik, kimia PG | Konduktivitas $< 10\,\mu\text{S/cm}$, PG $25.0\% \pm 1.0\%$, nol tetesan | Saringan belum dibuka atau kupon korosi belum dipasang |
| **Gate D: Punch-List & Kesiapan Staf** | Buku cacat, uji buta LOTO/EOP teknisi, gudang suku cadang | **Item Punch Tipe A (Keselamatan/SLA/Redundansi) = 0** | Menyembunyikan cacat Tipe A sebagai item 'Minor' |

Jangan pernah mengizinkan penghapusan pengujian atas dasar kemiripan dengan aula sebelah (similarity waiver). Verifikasi **Pencabutan kunci master konstruksi, pengaturan ulang akses pintu (ACL), dan pengalihan penuh otoritas LOTO** secara fisik 100% di lapangan.

## Protokol Rapat Serah Terima dan Penerbitan Lembar Penolakan

Bekukan seluruh paket dokumen serah terima (Turnover Dossier) minimal 72 jam sebelum rapat tinjauan dan jalankan tiga langkah audit berikut:

1. **Uji Silang Dokumen vs Fisik**: Pilih secara acak 20 pemutus sirkuit, katup isolasi, dan sensor dari berkas PDF lalu cocokkan langsung dengan setelan fisik di ruangan serta nilai mentah BMS.
2. **Inspeksi Kabel Jumper & Paksaan Perangkat Lunak**: Pastikan nol kabel jumper sementara di panel kontrol, nol bit Forced pada PLC, dan nol alarm yang ditangguhkan (Shelved) pada BMS.
3. **Penerbitan Lembar Penolakan (Refusal Sheet)**: Berikan kode penolakan tertulis untuk setiap temuan dan tolak menerima kunci penguasaan fisik maupun otoritas LOTO hingga pengujian ulang selesai.

## Keputusan yang Harus Dicatat

- Verifikasi kelengkapan bukti rekayasa pada gerbang audit (Pencabutan kunci master konstruksi, pengaturan ulang akses pintu (ACL), dan pengalihan penuh otoritas LOTO).
- Pencocokan fisik 100% antara gambar As-Built, setelan relai proteksi, dan tag katup di lapangan.
- Bukti nol item punch-list Tipe A serta bebas dari kabel jumper sementara dan bit paksa PLC.
- Penandatanganan Lembar Penolakan (Refusal Sheet) bila ditemukan cacat dan penetapan syarat uji ulang.
