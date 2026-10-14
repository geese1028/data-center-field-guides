#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
ROOT = Path("/Users/geese/Downloads/book/books/05-run-the-day/figures")
W = 1400

# filename -> list of (title, paragraphs) per language
TEXT = {
    "ja": {
        "fig-first.png": (
            "ダッシュボードの前に、この四つを読め。",
            [
                "一つでも欠けていれば、引き継ぎは失敗である。比率から一日を始めるな。",
                "1. 持ち越した異常。何が平常でないか。触れてはならないものは何か。無ければ、引き継いだプラントが分からない。",
                "2. まだ開いている許可。それぞれの失効時刻。失効した許可は停止である。無ければ、誰かが死んだ許可の上で作業しているかもしれない。",
                "3. まだ開いている障害。所有者と、サービスが回復したか。警報が消えたことは、障害のクローズではない。",
                "4. 今日が窓の変更。リスクを誰が窓の前に受け入れたか。戻し方は書いてあるか。業者の出張日を、リスク受入れにするな。",
                "その後、カバーを開ける前に、今日の作業場所を歩け。",
                "レンチは委譲できる。委譲できないのは、サービスがまだ保たれているという判断、変更窓の開始、顧客への通知である。",
            ],
        ),
        "fig-papers.png": (
            "紙は三種類。許可証はその上に乗る。四つ目の名前を作るな。",
            [
                "定常手順。毎回同じ作業。手順、止める限度、誰がやってよいか。作業点で見つからなければ、習慣と同じである。",
                "個別作業。その日の一つの仕事。工具の前に承認する。何を隔離し、その間プラントはどうし、どう戻し、失敗したらどう戻すか。作業中に書いた紙は物語である。日付を遡らせるな。",
                "緊急手順。個別作業の紙を待てないとき。停止、呼び出し、最初の安全状態。それから止まれ。修理は新しい個別作業である。修理が二十ページなら、分割せよ。",
                "許可証。この作業、この場所、この時間、この人々。失効は継続の提案ではない。延長は、レンチを持つ人のため息ではなく、新しい決定である。",
                "その作業が無いと開始を拒む予備品が無いなら、作業を始めるな。",
                "講習の配布物や規格の附録を手順に貼るな。標題を引け。プラントの手順は自分で書け。",
            ],
        ),
        "fig-incident.png": (
            "障害の時計。分を書け。原因はまだ書くな。",
            [
                "障害とは、負っているサービスを離れたこと、または人が危険なことである。うるさい警報は、警報でしかないことがある。",
                "知った分。見たことを書く。原因の推測は書かない。",
                "安全な分。緊急手順の安全状態に達した。それから止まれ。修理は新しい作業紙である。",
                "呼んだ分。シートにある名前と、応答した分。好きな人を、シートの名前の代わりにするな。",
                "知らせた分。時刻と症状。契約が定める時計。時計は、知ったときに始まる。確信のない原因は、第一報に入れない。仮説として別に置け。",
                "閉じた分。サービスが回復し、通知が契約と一致する。警報消去でも、部品を替えたという言葉でもない。",
                "その後。手順、巡回、予備品、資格のどれか一つを変える。変えないなら、なぜかを書け。恐怖の再話だけの会議は、レビューではない。",
            ],
        ),
        "fig-capacity.png": (
            "容量の三つの問い。未知は許される。見せかけることは許されない。",
            [
                "何を売ったか。契約の条項から答えよ。スライドと違えば、契約で運転し、スライドは返せ。昨年のパンフレットから答えるな。",
                "何が使われているか。名前と日付のある測定または割当から答えよ。部屋が忙しそうだという感じから答えるな。忙しい週はキロワットではない。",
                "一つの故障のあと、何が残るか。このプラントの、名前と日付のある検討から答えよ。または未知と書け。その後変えたプラントの古い検討、絵、銘板から答えるな。",
                "売った量を超える、または一つの故障のあと残る量を超える依頼は、待て。試すために回路を入れるな。",
                "効率の比率をここに印刷し、健全さと呼ぶな。定義と計器を引くか、黙れ。",
            ],
        ),
    },
    "id": {
        "fig-first.png": (
            "Baca empat hal ini sebelum dasbor apa pun.",
            [
                "Jika satu hilang, serah terima gagal. Jangan mulai hari dari sebuah rasio.",
                "1. Gangguan yang dibawa. Apa yang tidak normal. Apa yang tidak boleh disentuh. Jika kosong, Anda tidak tahu instalasi yang diwarisi.",
                "2. Izin yang masih terbuka. Jam masing-masing mati. Kedaluwarsa berarti berhenti. Jika kosong, seseorang mungkin masih bekerja di atas izin yang mati.",
                "3. Insiden yang masih terbuka. Pemilik, dan apakah layanan sudah pulih. Alarm yang padam bukan insiden yang ditutup.",
                "4. Perubahan yang jendelanya hari ini. Siapa menerima risiko sebelum jendela. Rencana kembali tertulis. Jangan jadikan hari perjalanan vendor sebagai penerimaan risiko.",
                "Lalu jalanilah tempat kerja hari ini, sebelum penutup dibuka.",
                "Kunci Inggris boleh diwakilkan. Yang tidak boleh: layanan masih terpenuhi, mulai jendela perubahan, memberitahu pelanggan.",
            ],
        ),
        "fig-papers.png": (
            "Tiga kertas. Izin duduk di atasnya. Jangan membuat nama keempat.",
            [
                "Prosedur tetap. Tugas yang sama setiap kali. Langkah, batas yang menghentikan tugas, siapa yang boleh. Jika satu-satunya salinan adalah kebiasaan, atau tidak ditemukan di panel, itu bukan prosedur.",
                "Pekerjaan khusus. Satu pekerjaan, satu hari. Disetujui sebelum alat keluar. Apa yang diisolasi, apa yang dilakukan instalasi, bagaimana kembali, bagaimana mundur. Kertas yang ditulis saat kerja adalah cerita. Jangan mundurkan tanggalnya.",
                "Prosedur darurat. Ketika kertas pekerjaan tidak bisa ditunggu. Berhenti. Panggil. Keadaan aman pertama. Lalu berhenti. Perbaikan adalah kertas pekerjaan baru. Jika darurat berisi dua puluh halaman perbaikan, pecah.",
                "Izin. Pekerjaan ini, tempat ini, waktu ini, orang-orang ini. Kedaluwarsa bukan saran untuk lanjut. Memperpanjang adalah keputusan baru, bukan desahan orang yang memegang kunci.",
                "Jika suku cadang yang membuat pekerjaan menolak mulai tidak ada, jangan mulai.",
                "Jangan menempelkan selebaran kursus atau lampiran standar ke dalam prosedur. Kutip judulnya. Tulis langkah instalasi Anda sendiri.",
            ],
        ),
        "fig-incident.png": (
            "Jam insiden. Tulis menitnya. Jangan tulis penyebabnya dulu.",
            [
                "Insiden adalah layanan yang meninggalkan yang Anda hutangkan, atau orang dalam bahaya. Alarm yang berisik bisa hanya alarm.",
                "Menit tahu. Tulis yang dilihat. Jangan tulis tebakan akar masalah.",
                "Menit aman. Keadaan aman dari kertas darurat tercapai. Lalu berhenti. Perbaikan adalah kertas pekerjaan baru.",
                "Menit memanggil. Nama di lembar, dan menit mereka menjawab. Jangan mengganti nama di lembar dengan orang yang Anda suka.",
                "Menit memberitahu. Waktu dan gejala. Jam yang disebut kontrak. Jam mulai saat Anda tahu. Penyebab yang belum pasti tidak masuk pemberitahuan pertama. Simpan sebagai hipotesis.",
                "Menit tutup. Layanan pulih, dan pemberitahuan sesuai kontrak. Alarm padam, atau vendor bilang suku cadang diganti, bukan itu.",
                "Sesudahnya: satu perubahan pada prosedur, ronde, suku cadang, atau kualifikasi. Atau tulis tidak ada, dan mengapa. Rapat yang hanya mengulang rasa takut bukan tinjauan.",
            ],
        ),
        "fig-capacity.png": (
            "Tiga pertanyaan kapasitas. Tidak tahu boleh. Berpura-pura tidak boleh.",
            [
                "Apa yang Anda jual? Dari klausul kontrak. Jika slide berbeda, operasikan menurut kontrak dan kembalikan slidenya. Bukan dari brosur tahun lalu.",
                "Apa yang terpakai? Dari pengukuran atau alokasi yang bernama dan bertanggal. Bukan dari rasa bahwa ruangan sibuk. Minggu yang sibuk bukan kilowatt.",
                "Apa yang tersisa setelah satu kegagalan? Dari kajian instalasi ini, bernama dan bertanggal. Atau tulis tidak diketahui. Bukan dari kajian instalasi yang sudah Anda ubah, bukan dari gambar, bukan dari pelat nama.",
                "Permintaan yang melebihi yang terjual, atau yang masih tertanggung setelah satu kegagalan, menunggu. Sif tidak menerimanya dengan menghidupkan sirkuit hanya untuk mencoba.",
                "Jangan mencetak rasio efisiensi di sini dan menyebutnya kesehatan. Kutip definisi dan meter, atau diam.",
            ],
        ),
    },
    "ko": {
        "fig-first.png": (
            "어떤 대시보드보다 먼저 이 네 가지를 읽어라.",
            [
                "하나가 없으면 인계는 실패한 것이다. 비율로 하루를 시작하지 마라.",
                "1. 넘어온 이상. 무엇이 정상이 아닌지. 무엇을 만지면 안 되는지. 없으면, 인계받은 설비를 모르는 것이다.",
                "2. 아직 열린 허가. 각각의 만료 시각. 만료는 정지이다. 없으면, 누군가 죽은 허가 위에서 일하고 있을 수 있다.",
                "3. 아직 열린 장애. 담당자와, 서비스가 회복되었는지. 경보가 꺼진 것은 장애의 종료가 아니다.",
                "4. 오늘이 창인 변경. 창이 열리기 전에 누가 위험을 인수했는지. 되돌리기가 적혀 있는지. 업체 출장일을 위험 인수로 삼지 마라.",
                "그다음, 덮개를 열기 전에 오늘 작업할 장소를 걸어라.",
                "렌치는 위임할 수 있다. 위임할 수 없는 것: 서비스가 아직 유지된다는 판단, 변경 창의 시작, 고객 통지.",
            ],
        ),
        "fig-papers.png": (
            "문서는 세 가지. 허가증은 그 위에 얹힌다. 네 번째 이름을 만들지 마라.",
            [
                "상시 절차. 매번 같은 작업. 단계, 작업을 멈추는 한계, 누가 해도 되는지. 유일한 사본이 습관이거나 패널에서 찾지 못하면 절차가 아니다.",
                "개별 작업. 그날의 한 작업. 도구를 꺼내기 전에 승인. 무엇을 격리하고, 그동안 설비는 어떻게 되며, 어떻게 되돌리고, 실패하면 어떻게 물러나는지. 작업 중에 쓴 문서는 이야기이다. 날짜를 되돌리지 마라.",
                "비상 절차. 개별 작업 문서를 기다릴 수 없을 때. 정지. 호출. 첫 안전 상태. 그다음 멈춰라. 수리는 새 작업 문서이다. 수리가 스무 페이지면 나눠라.",
                "허가. 이 작업, 이 장소, 이 시간, 이 사람들. 만료는 계속하라는 제안이 아니다. 연장은 렌치를 든 사람의 한숨이 아니라 새 결정이다.",
                "그 작업이 없으면 시작을 거부하는 예비품이 없으면, 시작하지 마라.",
                "교육 유인물이나 규격의 부록을 절차에 붙이지 마라. 제목을 인용하라. 설비의 단계는 직접 써라.",
            ],
        ),
        "fig-incident.png": (
            "장애 시계. 시각을 써라. 원인은 아직 쓰지 마라.",
            [
                "장애는 져야 할 서비스를 벗어난 것, 또는 사람이 위험할 때이다. 시끄러운 경보는 경보일 뿐이다.",
                "안 시각. 본 것을 쓴다. 원인 추측은 쓰지 않는다.",
                "안전 시각. 비상 절차의 안전 상태에 도달. 그다음 멈춘다. 수리는 새 작업 문서이다.",
                "호출 시각. 시트에 있는 이름과, 응답한 시각. 좋아하는 사람으로 시트의 이름을 바꾸지 마라.",
                "통지 시각. 시각과 증상. 계약이 정한 시계. 시계는 안 때부터 시작한다. 확신 없는 원인은 첫 통지에 넣지 마라. 가설로 따로 둬라.",
                "종료 시각. 서비스가 회복되고, 통지가 계약과 맞다. 경보 소거나 부품을 바꿨다는 말은 그것이 아니다.",
                "그 후. 절차, 순찰, 예비품, 자격 중 하나를 바꾼다. 바꾸지 않으면 이유를 써라. 공포만 다시 말하는 회의는 검토가 아니다.",
            ],
        ),
        "fig-capacity.png": (
            "용량의 세 질문. 모름은 허용된다. 가장은 허용되지 않는다.",
            [
                "무엇을 팔았는가. 계약 조항에서 답하라. 슬라이드와 다르면 계약대로 운영하고 슬라이드는 돌려보내라. 작년 안내문이 아니다.",
                "무엇이 쓰이고 있는가. 이름과 날짜가 있는 측정 또는 할당에서 답하라. 방이 바빠 보인다는 느낌이 아니다. 바쁜 한 주는 킬로와트가 아니다.",
                "고장 하나 뒤에 무엇이 남는가. 이 설비에 대한, 이름과 날짜가 있는 검토에서 답하라. 또는 모름이라고 써라. 그 후 바꾼 설비의 옛 검토, 그림, 명판에서 답하지 마라.",
                "판 양을 넘거나, 고장 하나 뒤에 남는 양을 넘는 요청은 기다린다. 시험 삼아 회로를 넣지 마라.",
                "효율 비율을 여기에 인쇄하고 건강이라고 부르지 마라. 정의와 계기를 인용하거나, 침묵하라.",
            ],
        ),
    },
    "th": {
        "fig-first.png": (
            "อ่านสี่อย่างนี้ก่อนแดชบอร์ดใด ๆ",
            [
                "ถ้าขาดอย่างหนึ่ง การส่งมอบกะล้มเหลว อย่าเริ่มวันจากอัตราส่วน",
                "1. ความผิดปกติที่รับมา อะไรไม่ปกติ อะไรห้ามแตะ ถ้าว่าง แปลว่าไม่รู้โรงงานที่รับมา",
                "2. ใบอนุญาตที่ยังเปิด เวลาที่แต่ละใบหมดอายุ หมดอายุคือหยุด ถ้าว่าง อาจมีคนยังทำงานบนใบที่ตายแล้ว",
                "3. เหตุที่ยังเปิด เจ้าของ และบริการกลับมาหรือยัง สัญญาณเตือนดับไม่ใช่การปิดเหตุ",
                "4. การเปลี่ยนแปลงที่หน้าต่างคือวันนี้ ใครรับความเสี่ยงก่อนเปิดหน้าต่าง มีทางถอยหรือไม่ อย่าให้วันเดินทางของผู้รับเหมาเป็นการรับความเสี่ยง",
                "จากนั้นเดินจุดที่จะทำงานวันนี้ ก่อนเปิดฝา",
                "ประแจมอบหมายได้ สิ่งที่มอบหมายไม่ได้: บริการยังอยู่ การเปิดหน้าต่างเปลี่ยนแปลง การบอกลูกค้า",
            ],
        ),
        "fig-papers.png": (
            "กระดาษสามชนิด ใบอนุญาตอยู่ข้างบน อย่าตั้งชื่อที่สี่",
            [
                "ขั้นตอนประจำ งานเดิมทุกครั้ง ขั้นตอน ขีดที่ทำให้หยุด ใครทำได้ ถ้ามีแต่ความเคยชิน หรือหาไม่เจอที่แผง นั่นไม่ใช่ขั้นตอน",
                "งานเฉพาะ งานหนึ่งในวันหนึ่ง อนุมัติก่อนหยิบเครื่องมือ จะแยกอะไร ระหว่างนั้นโรงงานทำอย่างไร กลับอย่างไร ถอยอย่างไร กระดาษที่เขียนระหว่างทำงานคือเรื่องเล่า อย่าลงวันที่ย้อนหลัง",
                "ขั้นตอนฉุกเฉิน เมื่อรอเอกสารงานเฉพาะไม่ได้ หยุด เรียก สถานะปลอดภัยแรก แล้วหยุด การซ่อมคือเอกสารงานใหม่ ถ้าเอกสารฉุกเฉินเป็นการซ่อมยาว ให้แยก",
                "ใบอนุญาต งานนี้ สถานที่นี้ เวลานี้ คนเหล่านี้ หมดอายุไม่ใช่คำแนะนำให้ทำต่อ การขยายเวลาคือการตัดสินใจใหม่ ไม่ใช่การถอนหายใจของคนถือประแจ",
                "ถ้าอะไหล่ที่งานนี้ปฏิเสธจะเริ่มถ้าไม่มี ไม่อยู่ อย่าเริ่ม",
                "อย่าแปะเอกสารหลักสูตรหรือภาคผนวกมาตรฐานลงในขั้นตอน อ้างชื่อเรื่อง เขียนขั้นตอนของโรงงานเอง",
            ],
        ),
        "fig-incident.png": (
            "นาฬิกาเหตุ เขียนนาที อย่าเขียนสาเหตุตอนนี้",
            [
                "เหตุคือบริการออกจากสิ่งที่คุณเป็นหนี้ หรือคนตกอยู่ในอันตราย สัญญาณที่ดังอาจเป็นเพียงสัญญาณ",
                "นาทีที่รู้ เขียนสิ่งที่เห็น อย่าเขียนการเดาสาเหตุ",
                "นาทีที่ปลอดภัย ถึงสถานะปลอดภัยตามเอกสารฉุกเฉิน แล้วหยุด การซ่อมคือเอกสารงานใหม่",
                "นาทีที่โทร ชื่อบนแผ่น และนาทีที่รับสาย อย่าเปลี่ยนชื่อบนแผ่นเป็นคนที่คุณชอบ",
                "นาทีที่บอก เวลาและอาการ นาฬิกาที่สัญญากำหนด นาฬิกาเริ่มเมื่อคุณรู้ สาเหตุที่ยังไม่แน่ไม่เข้าประกาศแรก เก็บเป็นสมมติฐาน",
                "นาทีที่ปิด บริการกลับมา และการแจ้งตรงตามสัญญา สัญญาณดับ หรือผู้ขายบอกว่าเปลี่ยนชิ้นส่วนแล้ว ไม่ใช่สิ่งนั้น",
                "หลังจากนั้น เปลี่ยนขั้นตอน การเดินตรวจ อะไหล่ หรือคุณสมบัติ อย่างใดอย่างหนึ่ง หรือเขียนว่าไม่เปลี่ยน และเหตุผล การประชุมที่เล่าความกลัวซ้ำไม่ใช่การทบทวน",
            ],
        ),
        "fig-capacity.png": (
            "คำถามความจุสามข้อ ไม่รู้ได้ แกล้งรู้ไม่ได้",
            [
                "ขายอะไรไว้ ตอบจากข้อสัญญา ถ้าสไลด์ไม่ตรง ให้เดินเครื่องตามสัญญาแล้วส่งสไลด์คืน ไม่ใช่จากโบรชัวร์ปีที่แล้ว",
                "ใช้อยู่เท่าไร ตอบจากการวัดหรือการจัดสรรที่มีชื่อและวันที่ ไม่ใช่จากความรู้สึกว่าห้องยุ่ง สัปดาห์ที่ยุ่งไม่ใช่กิโลวัตต์",
                "หลังความล้มเหลวหนึ่งครั้ง เหลืออะไร ตอบจากการศึกษาของโรงงานนี้ที่มีชื่อและวันที่ หรือเขียนว่าไม่รู้ ไม่ใช่จากการศึกษาโรงงานที่คุณเปลี่ยนไปแล้ว ไม่ใช่จากรูป หรือป้ายชื่อ",
                "คำขอที่เกินของที่ขาย หรือเกินของที่ยังรับไหวหลังความล้มเหลวหนึ่งครั้ง ให้รอ กะไม่รับโดยการจ่ายไฟวงจรแค่เพื่อลอง",
                "อย่าพิมพ์อัตราส่วนประสิทธิภาพที่นี่แล้วเรียกว่าสุขภาพ อ้างนิยามและมิเตอร์ หรือเงียบ",
            ],
        ),
    },
    "ar": {
        "fig-first.png": (
            "اقرأ هذه الأربعة قبل أي لوحة.",
            [
                "إذا غاب واحد، فالتسليم فشل. لا تبدأ اليوم من نسبة.",
                "1. الأعطال المنقولة. ما الذي ليس طبيعيًا. ما الذي لا يُمس. إن غاب، فأنت لا تعرف المحطة التي ورثتها.",
                "2. التصاريح المفتوحة. ساعة انتهاء كل واحد. الانتهاء يعني التوقف. إن غاب، فقد يعمل أحد على تصريح ميت.",
                "3. الحوادث المفتوحة. المالك، وهل عادت الخدمة. إطفاء الإنذار ليس إغلاق الحادث.",
                "4. التغييرات التي نافذتها اليوم. من قبل الخطر قبل النافذة. هل كُتب التراجع. لا تجعل يوم سفر المورد قبولًا للخطر.",
                "ثم امشِ مكان عمل اليوم قبل فتح الغطاء.",
                "المفتاح يُفوَّض. ما لا يُفوَّض: أن الخدمة ما زالت قائمة، وبدء نافذة التغيير، وإبلاغ العميل.",
            ],
        ),
        "fig-papers.png": (
            "ثلاث أوراق. التصريح فوقها. لا تخترع اسمًا رابعًا.",
            [
                "إجراء دائم. المهمة نفسها كل مرة. الخطوات، والحد الذي يوقف المهمة، ومن يجوز له. إن كانت النسخة الوحيدة عادة، أو لا تُوجد عند اللوحة، فليست إجراءً.",
                "عمل محدد. عمل واحد في يوم واحد. يُعتمد قبل الأدوات. ما يُعزل، وما تفعله المحطة، وكيف تعود، وكيف تتراجع. الورقة التي تُكتب أثناء العمل قصة. لا تؤرخها رجوعًا.",
                "إجراء طوارئ. حين لا يمكنك انتظار ورقة العمل. توقف. اتصل. أول حالة آمنة. ثم توقف. الإصلاح ورقة عمل جديدة. إن كان الطوارئ عشرين صفحة إصلاح، فاقسمه.",
                "تصريح. هذا العمل، هذا المكان، هذا الوقت، هؤلاء الناس. الانتهاء ليس اقتراحًا للمتابعة. التمديد قرار جديد، لا تنهيدة من يحمل المفتاح.",
                "إن غاب الاحتياطي الذي يرفض العمل أن يبدأ من دونه، فلا تبدأ.",
                "لا تلصق نشرة دورة أو ملحق معيار في الإجراء. اذكر العنوان. اكتب خطوات محطتك.",
            ],
        ),
        "fig-incident.png": (
            "ساعة الحادث. اكتب الدقيقة. لا تكتب السبب بعد.",
            [
                "الحادث هو خروج الخدمة عما تدين به، أو شخص في خطر. الإنذار الصاخب قد يكون إنذارًا فقط.",
                "دقيقة العلم. اكتب ما رأيت. لا تكتب تخمين السبب.",
                "دقيقة الأمان. بلغت الحالة الآمنة في ورقة الطوارئ. ثم توقف. الإصلاح ورقة عمل جديدة.",
                "دقيقة الاتصال. الاسم على الورقة، ودقيقة الرد. لا تستبدل الاسم على الورقة بمن تحب.",
                "دقيقة الإبلاغ. الوقت والعرض. الساعة التي يسميها العقد. تبدأ الساعة حين علمت. السبب غير المؤكد لا يدخل الإخطار الأول. أبقه فرضية.",
                "دقيقة الإغلاق. عادت الخدمة، والإخطار يطابق العقد. إطفاء الإنذار، أو قول المورد إن القطعة استُبدلت، ليس ذلك.",
                "بعد ذلك: تغيير واحد في إجراء أو جولة أو احتياطي أو تأهيل. أو اكتب لا شيء، ولماذا. اجتماع يعيد الخوف ليس مراجعة.",
            ],
        ),
        "fig-capacity.png": (
            "ثلاثة أسئلة للسعة. المجهول مسموح. الادعاء ليس مسموحًا.",
            [
                "ماذا بعت؟ من بند العقد. إن خالف العرض، شغّل بالعقد وأعد العرض. ليس من كراسة العام الماضي.",
                "ماذا يُستخدم؟ من قياس أو تخصيص له اسم وتاريخ. ليس من شعور أن القاعة مزدحمة. أسبوع مزدحم ليس كيلوواط.",
                "ماذا يبقى بعد عطل واحد؟ من دراسة لهذه المحطة لها اسم وتاريخ. أو اكتب مجهول. ليس من دراسة محطة غيّرتها بعد ذلك، ولا من صورة، ولا من لوحة اسم.",
                "الطلب الذي يتجاوز المبيع، أو ما يبقى بعد عطل واحد، ينتظر. الوردية لا تقبله بتشغيل الدائرة لمجرد التجربة.",
                "لا تطبع نسبة كفاءة هنا وتسمها صحة. اذكر التعريف والعداد، أو اصمت.",
            ],
        ),
    },
}


def font(size, bold=False):
    return ImageFont.truetype(FONT, size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        cur = ""
        # character wrap works for all these scripts
        for ch in para:
            trial = cur + ch
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = ch
        if cur:
            lines.append(cur)
    return lines


def render(lang, name, title, paras):
    scratch = Image.new("RGB", (W, 100), "white")
    d = ImageDraw.Draw(scratch)
    tf, bf = font(26, True), font(20)
    lines = wrap(d, title, tf, W - 80)
    body = []
    for p in paras:
        body.extend(wrap(d, p, bf, W - 80))
        body.append("")
    h = 40 + len(lines) * 36 + 16 + len(body) * 30 + 36
    im = Image.new("RGB", (W, max(h, 400)), "white")
    d = ImageDraw.Draw(im)
    y = 32
    for line in lines:
        d.text((40, y), line, font=tf, fill=(17, 17, 17))
        y += 36
    y += 8
    d.line((40, y, W - 40, y), fill=(17, 17, 17), width=2)
    y += 16
    for line in body:
        if line:
            d.text((40, y), line, font=bf, fill=(17, 17, 17))
        y += 30
    out = ROOT / lang
    out.mkdir(parents=True, exist_ok=True)
    im.save(out / name, "PNG")


def main():
    for lang, figs in TEXT.items():
        for name, (title, paras) in figs.items():
            render(lang, name, title, paras)
            print(lang, name)


if __name__ == "__main__":
    main()
