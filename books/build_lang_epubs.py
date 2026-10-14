#!/usr/bin/env python3
"""
Multilingual EPUB Builder for Data Center Field Guides
Supports Books 01, 02, 03, 05 across 5 languages:
- ja: Japanese (日本語)
- id: Indonesian (Bahasa Indonesia)
- ko: Korean (한국어)
- th: Thai (ภาษาไทย)
- ar: Arabic (العربية - RTL layout)

Parses headings, lists, tables, code blocks, and flagship diagrams.
Generates publication-ready EPUB 3.0, covers, and KDP upload packs.
"""

import html
import importlib.util
import re
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books")
FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
BG = (30, 30, 30)
BLUE = (0, 102, 255)
CYAN = (0, 255, 255)
GRID = (42, 42, 42)
TEXT = (255, 255, 255)

BOOKS = {
    "01": {
        "slug": "01-liquid-load-bank",
        "en_title": "Design and Build a Liquid Load Bank for NVL72 Racks",
        "file": "design-and-build-a-liquid-load-bank",
        "build": ROOT / "01-liquid-load-bank" / "build_epub.py",
    },
    "02": {
        "slug": "02-read-load-bank-data",
        "en_title": "Read and Use Load Bank Data",
        "file": "read-and-use-load-bank-data",
        "build": ROOT / "02-read-load-bank-data" / "build_epub.py",
    },
    "03": {
        "slug": "03-run-one-test",
        "en_title": "Finish a Liquid Cooling Verification: Seven sheets for one load-bank test",
        "file": "finish-a-liquid-cooling-verification",
        "build": ROOT / "03-run-one-test" / "build_epub.py",
    },
    "05": {
        "slug": "05-run-the-day",
        "en_title": "Run the Data Center Day: What the manager must sign before the shift ends",
        "file": "run-the-data-center-day",
        "build": ROOT / "05-run-the-day" / "build_epub.py",
    },
}

LANGS = {
    "ja": {
        "name": "Japanese",
        "rtl": False,
        "kdp": "Japanese",
        "titles": {
            "01": "NVL72級ラック向け液冷負荷装置を設計し、作る",
            "02": "ロードバンクのデータを読み、使う",
            "03": "液冷検証を完了する",
            "05": "データセンターの1日を回す",
        },
        "subs": {
            "01": "要求シートと試作の合格判定",
            "02": "速報の現場手引",
            "03": "1回の負荷試験のための7枚のシート",
            "05": "シフトが終わる前に管理者が署名すべきこと",
        },
        "desc": {
            "01": "液冷負荷装置は、NVL72級ラックの代わりになる試験器である。冷却器でも図面でもない。この現場手引は、金属を切る前に何を書き、試作を完成と呼ぶ前にどの門を通すかを示す。残るのは、見知らぬ人に渡せる二つの文書である。要求シートと、試作の受入シート。流量、温度、圧力、ダンフォスFD83継手、ダーシー・ワイスバッハ圧力損失の数値は、その時点で有効な仕様を引用するまで空欄のままである。",
            "02": "曲線が穏やかだからといって、負荷装置の試験が有効なのではない。この現場手引は、運転を見知らぬ人が監査できる速報にする方法を示す。速報は五行で開く。事前試験、勾配、過負荷、ステップ変化、単路故障。1秒テレメトリ、欠測判定、熱収支平衡を厳格に監査する。試みた行がすべて合格でなければ、総括は合格ではない。",
            "03": "液冷検証プロジェクトは、支えてよい文を誰も書かないとき、最初の週に失敗する。「液冷は働く」は工学的な主張ではない。願望である。この現場手引は、1回の負荷試験を監査可能な引渡しにするための7枚の検証シートを提供する。ASHRAEガイドライン0/202のレベル1からレベル5までの関門、冷水ポンプ曲線、CDU冗長切替論理、そしてダンフォスFD83継手の受入基準を網羅する。",
            "05": "管理者が今日持つのは、設備の運転状態、それに触れてよい人、そしてなされたことの改ざん不能な記録である。この現場手引は、30分の対面引継ぎ、SOP/MOP/EOP手順の統治、2N電源の定常負荷上限（0.45 P_rated）、500年確率洪水の防護、そして6箇所の現場巡回点検を定義する。シフトの終わりに残るのは、署名された日次完了シートである。",
        },
        "copy": "英語版をAI補助で翻訳した。英語版の本文と図はAI生成である。",
        "note": "図中の文字は英語版のままである。",
    },
    "id": {
        "name": "Indonesian",
        "rtl": False,
        "kdp": "Indonesian",
        "titles": {
            "01": "Merancang dan Membangun Bank Beban Cair untuk Rak Kelas NVL72",
            "02": "Membaca dan Menggunakan Data Bank Beban",
            "03": "Menyelesaikan Verifikasi Pendinginan Cair",
            "05": "Menjalankan Hari Operasional Pusat Data",
        },
        "subs": {
            "01": "Lembar persyaratan dan penerimaan purwarupa",
            "02": "Panduan laporan kilat",
            "03": "Tujuh lembar kerja untuk satu uji bank beban",
            "05": "Apa yang harus ditandatangani manajer sebelum shift berakhir",
        },
        "desc": {
            "01": "Bank beban cair adalah alat uji yang menggantikan rak kelas NVL72. Bukan pendingin, dan bukan gambar fabrikasi. Panduan ini menyatakan apa yang harus ditulis sebelum logam dipotong, dan gerbang mana yang harus lulus sebelum purwarupa disebut selesai. Yang tersisa adalah dua dokumen yang dapat diserahkan kepada orang asing: lembar persyaratan dan lembar penerimaan. Angka aliran, suhu, tekanan, fitting Danfoss FD83, dan penurunan tekanan Darcy-Weisbach tetap kosong sampai Anda mengutip spesifikasi yang berlaku.",
            "02": "Uji bank beban tidak sah hanya karena kurvanya tenang. Panduan ini menunjukkan cara mengubah satu jalan menjadi laporan kilat yang dapat diaudit orang asing. Laporan dibuka dengan lima baris: uji awal, gradien, beban lebih, perubahan langkah, dan gangguan satu jalur. Memeriksa telemetri 1 detik, celah polling, dan keseimbangan termal. Lulus keseluruhan hanya jika setiap baris yang dicoba lulus.",
            "03": "Proyek verifikasi pendinginan cair gagal pada minggu pertama saat tidak ada yang menuliskan pernyataan yang dapat diaudit. 'Pendinginan cair bekerja' bukan klaim teknik; itu adalah angan-angan. Panduan lapangan ini menyediakan 7 lembar verifikasi untuk mengubah satu uji bank beban menjadi serah terima yang siap diaudit. Mencakup gerbang ASHRAE Guideline 0/202 Level 1 hingga 5, kurva pompa dingin, logika kaskade CDU, dan kriteria kopling Danfoss FD83.",
            "05": "Hari ini manajer menguasai kondisi operasional fasilitas, siapa yang boleh menyentuhnya, dan catatan yang tidak dapat diubah dari apa yang telah dikerjakan. Panduan lapangan ini menetapkan serah terima shift 30 menit, tata kelola prosedur SOP/MOP/EOP, batas beban tunak daya 2N (0.45 P_rated), mitigasi banjir 500 tahun, dan 6 stasiun inspeksi fisik. Shift berakhir dengan lembar penutupan manajer yang ditandatangani.",
        },
        "copy": "Terjemahan berbantuan AI dari edisi bahasa Inggris. Teks dan gambar edisi Inggris dihasilkan dengan AI.",
        "note": "Label pada gambar tetap dalam bahasa Inggris.",
    },
    "ko": {
        "name": "Korean",
        "rtl": False,
        "kdp": "Korean",
        "titles": {
            "01": "NVL72급 랙을 위한 액랭 로드뱅크의 설계와 제작",
            "02": "로드뱅크 데이터를 읽고 쓰기",
            "03": "액랭 검증을 끝내다",
            "05": "데이터센터의 하루를 운영하다",
        },
        "subs": {
            "01": "요구 시트와 시제품 인수",
            "02": "속보를 위한 현장 안내",
            "03": "단 한 번의 로드뱅크 시험을 위한 일곱 장의 시트",
            "05": "교대 근무가 끝나기 전 관리자가 반드시 서명해야 하는 것들",
        },
        "desc": {
            "01": "액랭 로드뱅크는 NVL72급 랙을 대신하는 시험 장치이다. 냉각기도 아니고 제작 도면도 아니다. 이 현장 안내는 금속을 자르기 전에 무엇을 적는지, 시제품을 끝났다고 부르기 전에 어느 문을 통과하는지를 말한다. 남는 것은 낯선 사람에게 건넬 수 있는 두 문서이다. 요구 시트와 인수 시트. 유량, 온도, 압력, 댄포스 FD83 커플링, 다르시-바이스바흐 압력 강하는 그때 유효한 규격을 인용하기 전까지 비워 둔다.",
            "02": "곡선이 잔잔하다고 해서 로드뱅크 시험이 유효한 것은 아니다. 이 안내는 한 번의 운전을 낯선 사람이 감사할 수 있는 속보로 만드는 방법을 말한다. 속보는 다섯 줄로 시작한다. 사전 시험, 구배, 과부하, 스텝 변화, 단로 고장. 1초 텔레메트리, 폴링 결측 감지, 열 평형 검증을 수행한다. 시도한 줄이 모두 합격이 아니면 총괄은 합격이 아니다.",
            "03": "액랭 검증 프로젝트는 감사 가능한 문장을 아무도 쓰지 않을 때 첫 주에 실패한다. '액랭이 작동한다'는 공학적 주장이 아니라 희망 사항일 뿐이다. 이 현장 안내서는 한 번의 로드뱅크 시험을 완벽한 인수인계로 전환하는 7장의 검증 시트를 제공한다. ASHRAE 가이드라인 0/202 레벨 1~5 관문, 냉수 펌프 곡선, CDU 다중 펌프 캐스케이드 로직, 댄포스 FD83 퀵 커플링 인수 기준을 체계화한다.",
            "05": "오늘 관리자가 통제하는 것은 플랜트의 운전 상태, 플랜트를 건드릴 수 있는 사람, 그리고 수행된 작업에 대한 변경 불가능한 기록이다. 이 현장 지침은 30분 대면 교대 인수인계, SOP/MOP/EOP 절차 피라미드, 2N 전력 정상상태 부하 한도(0.45 P_rated), 500년 빈도 홍수 방호, 그리고 6대 순회 점검 구역을 규정한다. 교대 근무의 끝에는 서명된 일일 마감 시트가 남는다.",
        },
        "copy": "영어판을 AI 보조로 번역한 것이다. 영어판의 본문과 그림은 AI가 생성했다.",
        "note": "그림 안의 글자는 영어판 그대로이다.",
    },
    "th": {
        "name": "Thai",
        "rtl": False,
        "kdp": "Thai",
        "titles": {
            "01": "ออกแบบและสร้างโหลดแบงก์ของเหลวสำหรับแร็คระดับ NVL72",
            "02": "อ่านและใช้ข้อมูลโหลดแบงก์",
            "03": "การตรวจสอบความถูกต้องของระบบระบายความร้อนด้วยของเหลวให้เสร็จสมบูรณ์",
            "05": "บริหารจัดการวันปฏิบัติงานของดาต้าเซ็นเตอร์",
        },
        "subs": {
            "01": "แผ่นข้อกำหนดและการตรวจรับต้นแบบ",
            "02": "คู่มือรายงานฉับพลัน",
            "03": "เจ็ดแผ่นงานสำหรับการทดสอบโหลดแบงก์หนึ่งครั้ง",
            "05": "สิ่งที่ผู้จัดการต้องลงนามก่อนสิ้นสุดกะการทำงาน",
        },
        "desc": {
            "01": "โหลดแบงก์ของเหลวเป็นเครื่องมือทดสอบที่แทนแร็คระดับ NVL72 ไม่ใช่เครื่องทำความเย็น และไม่ใช่แบบสำหรับการผลิต คู่มือนี้บอกว่าต้องเขียนอะไรก่อนตัดโลหะ และต้องผ่านประตูใดก่อนจะเรียกต้นแบบว่าเสร็จ สิ่งที่เหลือคือเอกสารสองฉบับที่มอบให้คนแปลกหน้าได้ แผ่นข้อกำหนด และแผ่นตรวจรับ ตัวเลขอัตราไหล อุณหภูมิ ความดัน ข้อต่อ Danfoss FD83 และความดันลด Darcy-Weisbach เว้นว่างจนกว่าจะอ้างข้อกำหนดที่มีผลในขณะนั้น",
            "02": "การทดสอบโหลดแบงก์ไม่ถูกต้องเพียงเพราะเส้นโค้งดูสงบ คู่มือนี้บอกวิธีเปลี่ยนการเดินเครื่องหนึ่งครั้งให้เป็นรายงานฉับพลันที่คนแปลกหน้าตรวจสอบได้ รายงานเปิดด้วยห้าบรรทัด การทดสอบก่อน การไต่โหลด โอเวอร์โหลด การเปลี่ยนขั้น และความผิดพลาดของแหล่งจ่ายเดียว ตรวจสอบเทเลเมทรี 1 วินาที ช่องว่างข้อมูล และสมดุลความร้อน ผ่านโดยรวมได้ก็ต่อเมื่อทุกบรรทัดที่ลองผ่าน",
            "03": "โครงการตรวจสอบระบบระบายความร้อนด้วยของเหลวล้มเหลวตั้งแต่สัปดาห์แรกหากไม่มีใครเขียนประโยคอ้างสิทธิ์ที่ตรวจสอบได้ 'ระบบระบายความร้อนด้วยของเหลวทำงานได้' ไม่ใช่ข้ออ้างทางวิศวกรรม แต่เป็นเพียงความปรารถนา คู่มือภาคสนามนี้นำเสนอแผ่นงานการตรวจสอบ 7 แผ่น ครอบคลุมประตู ASHRAE Guideline 0/202 ระดับ 1 ถึง 5, เส้นโค้งปั๊มน้ำเย็น, ตรรกะ CDU และเกณฑ์ข้อต่อ Danfoss FD83",
            "05": "วันนี้ผู้จัดการเป็นเจ้าของสถานะการทำงานของโรงงาน คนที่ได้รับอนุญาตให้สัมผัสอุปกรณ์ และบันทึกสิ่งที่ทำไปแล้ว คู่มือภาคสนามนี้กำหนดกระบวนการส่งมอบกะ 30 นาที, ลำดับขั้นขั้นตอน SOP/MOP/EOP, ขีดจำกัดโหลดคงที่ระบบไฟ 2N (0.45 P_rated), การป้องกันน้ำท่วมรอบ 500 ปี และ 6 สถานีตรวจการณ์ประจำกะ จบกะด้วยแผ่นงานปิดกะที่มีลายมือชื่อ",
        },
        "copy": "แปลจากฉบับภาษาอังกฤษโดยมี AI ช่วย ข้อความและรูปของฉบับอังกฤษสร้างด้วย AI",
        "note": "ตัวอักษรในรูปยังเป็นภาษาอังกฤษ",
    },
    "ar": {
        "name": "Arabic",
        "rtl": True,
        "kdp": "Arabic",
        "titles": {
            "01": "تصميم وبناء بنك حمل سائل لأرفف من فئة NVL72",
            "02": "قراءة بيانات بنك الحمل واستخدامها",
            "03": "إتمام التحقق من التبريد السائل",
            "05": "إدارة يوم مركز البيانات",
        },
        "subs": {
            "01": "ورقة المتطلبات وقبول النموذج",
            "02": "دليل التقرير العاجل",
            "03": "سبع أوراق لاختبار بنك حمل واحد",
            "05": "ما يجب أن يوقعه المدير قبل انتهاء الوردية",
        },
        "desc": {
            "01": "بنك الحمل السائل أداة اختبار تقوم مقام رف من فئة NVL72. ليس مبردًا، وليس رسم تصنيع. يبيّن هذا الدليل ما يُكتب قبل قطع المعدن، وأي بوابات يجب أن تجتاز قبل أن يُسمى النموذج منتهيًا. ما يبقى وثيقتان يمكن تسليمهما لغريب: ورقة المتطلبات وورقة القبول. تبقى أرقام التدفق والحرارة والضغط ووصلات Danfoss FD83 وهبوط ضغط دارسي-فايسباخ فارغة حتى تستشهد بالمواصفة النافذة.",
            "02": "اختبار بنك الحمل ليس صالحًا لأن المنحنى يبدو هادئًا. يبيّن هذا الدليل كيف تحوّل تشغيلًا واحدًا إلى تقرير عاجل يستطيع غريب أن يدققه. يفتح التقرير بخمسة أسطر: الاختبار المسبق، والتدرج، والحمل الزائد، وتغير الخطوة، وعطل مسار واحد. فحص قياس عن بُعد بدقة ثانية واحدة، وفجوات الاستطلاع، والتوازن الحراري. لا تنجح النتيجة الإجمالية إلا إذا نجح كل سطر جُرّب.",
            "03": "يفشل مشروع التحقق من التبريد السائل في أسبوعه الأول عندما لا يكتب أحد جملة ادعاء قابلة للتدقيق. 'التبريد السائل يعمل' ليست ادعاءً هندسيًا بل مجرد أمنية. يقدّم هذا الدليل الميداني 7 أوراق تحقق لتحويل اختبار بنك الحمل إلى تسليم معتمد. يغطي بوابات ASHRAE Guideline 0/202 من المستوى 1 إلى 5، ومنحنيات المضخات الباردة، ومنطق تتابع CDU، ومعايير وصلات Danfoss FD83.",
            "05": "ما يمتلكه المدير اليوم هو الحالة التشغيلية للمنشأة، ومن يُسمح له بلمسها، والسجل غير القابل للتغيير لما تم إنجازه. يحدد هذا الدليل الميداني تسليم الوردية وجهًا لوجه لمدة 30 دقيقة، وهرم إجراءات SOP/MOP/EOP، وسقف الحمل المستقر لمنظومة 2N الكهربائية (0.45 P_rated)، والحماية من فيضان 500 عام، و6 محطات للجولة التفتيشية. تنتهي الوردية بورقة إغلاق موقعة.",
        },
        "copy": "ترجمة بمساعدة الذكاء الاصطناعي من الطبعة الإنجليزية. نص الطبعة الإنجليزية ورسومها مولَّدة بالذكاء الاصطناعي.",
        "note": "تبقى الكتابة داخل الرسوم بالإنجليزية.",
    },
}


def font(size, bold=False):
    return ImageFont.truetype(FONT, size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        if " " in para:
            words = para.split()
            cur = ""
            for word in words:
                trial = word if not cur else cur + " " + word
                if draw.textlength(trial, font=fnt) <= width:
                    cur = trial
                else:
                    if cur:
                        lines.append(cur)
                    cur = word
            if cur:
                lines.append(cur)
        else:
            cur = ""
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


def new_canvas(w, h):
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, w, 40):
        d.line((x, 0, x, h), fill=GRID, width=1)
    for y in range(0, h, 40):
        d.line((0, y, w, y), fill=GRID, width=1)
    d.rectangle((18, 18, w - 19, h - 19), outline=BLUE, width=2)
    return im, d


def draw_cover(path, kicker, title, subtitle):
    im, d = new_canvas(1600, 2560)
    d.rectangle((70, 160, 90, 2100), fill=CYAN)
    d.text((140, 180), kicker, font=font(28), fill=CYAN)
    y = 360
    display = font(64)
    for line in wrap(d, title, display, 1280):
        d.text((140, y), line, font=display, fill=TEXT)
        y += 90
    d.line((140, y + 20, 900, y + 20), fill=CYAN, width=2)
    yy = y + 50
    for line in wrap(d, subtitle, font(32), 1280):
        d.text((140, yy), line, font=font(32), fill=CYAN)
        yy += 48
    d.text((140, 2280), "TRISTAN", font=font(36), fill=CYAN)
    d.text((140, 2360), "DATA CENTER FIELD GUIDES", font=font(28), fill=TEXT)
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path.with_suffix(".png"), "PNG")
    im.convert("RGB").save(path, "JPEG", quality=95, optimize=True)
    return path


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def book1_figures():
    base = {
        "01-": [("fig-functions.png", "Figure 4. Drop a function only by writing the reduction.")],
        "02-": [("fig-duty.png", "Figure 5. A missing quantity can imitate a healthy value of another.")],
        "03-": [
            ("fig-boundary.png", "Figure 1. The load bank sits on the rack side of the heat exchanger."),
            ("fig-ports.png", "Figure 6. Isolation, spare, and hose routing are acceptance items."),
        ],
        "04-": [
            ("fig-authority.png", "Figure 7. If A, B, and C are the same valve, say so."),
            ("fig-safe.png", "Figure 8. Command zero and kill control power are separate tests."),
        ],
        "05-": [
            ("fig-exit.png", "Figure 9. A platform that can show and cannot export has not finished."),
            ("fig-command.png", "Figure 2. A script must be able to reach the load switch."),
        ],
        "06-": [
            ("fig-stops.png", "Figure 10. Each stop needs a failed-sensor behavior."),
            ("fig-electrical.png", "Figure 13. The hall code and the unit standard are not the same citation."),
        ],
        "07-": [
            ("fig-gates.png", "Figure 3. Do not start a later gate to save a failed earlier one."),
            ("fig-steps.png", "Figure 11. Sit on each step. The overload visit is not one of these sits."),
        ],
        "08-": [("fig-file.png", "Figure 12. Weight is not a file. These six items are.")],
    }
    try:
        mod = load_module(BOOKS["01"]["build"], "b1")
        if hasattr(mod, "EXTRA"):
            for prefix, _heading, filename, caption, *_rest in mod.EXTRA:
                base.setdefault(prefix, []).append((filename, caption))
    except Exception:
        pass
    return base


def book2_figures():
    out = {}
    try:
        mod = load_module(BOOKS["02"]["build"], "b2")
        if hasattr(mod, "FIGS"):
            for prefix, _heading, filename, caption, *_rest in mod.FIGS:
                out.setdefault(prefix, []).append((filename, caption))
    except Exception:
        pass
    return out


def md_to_blocks(text, base_dir):
    lines = text.replace("\r\n", "\n").split("\n")
    blocks = []
    buf = []
    list_buf = []
    table = []
    code_buf = []
    in_code = False

    def flush_p():
        if buf:
            blocks.append(("p", " ".join(buf).strip()))
            buf.clear()

    def flush_list():
        if list_buf:
            blocks.append(("ul", list(list_buf)))
            list_buf.clear()

    def flush_table():
        if table:
            rows = []
            for raw in table:
                cells = [c.strip() for c in raw.strip().strip("|").split("|")]
                if cells and not all(set(c) <= set("-: ") for c in cells):
                    rows.append(cells)
            if rows:
                blocks.append(("table", rows))
            table.clear()

    def flush_code():
        if code_buf:
            blocks.append(("pre", "\n".join(code_buf)))
            code_buf.clear()

    img_re = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_p()
            flush_list()
            flush_table()
            if in_code:
                in_code = False
                flush_code()
            else:
                in_code = True
            continue

        if in_code:
            code_buf.append(line)
            continue

        if stripped.startswith("|"):
            flush_p()
            flush_list()
            table.append(stripped)
            continue
        flush_table()

        if stripped.startswith("# "):
            flush_p()
            flush_list()
            blocks.append(("h1", stripped[2:].strip()))
        elif stripped.startswith("## "):
            flush_p()
            flush_list()
            blocks.append(("h2", stripped[3:].strip()))
        elif stripped.startswith("### "):
            flush_p()
            flush_list()
            blocks.append(("h3", stripped[4:].strip()))
        elif stripped.startswith("> "):
            flush_p()
            flush_list()
            blocks.append(("blockquote", stripped[2:].strip()))
        elif stripped.startswith("- ") or stripped.startswith("* "):
            flush_p()
            list_buf.append(stripped[2:].strip())
        elif img_re.fullmatch(stripped):
            flush_p()
            flush_list()
            alt, src = img_re.fullmatch(stripped).groups()
            path = (base_dir / src).resolve()
            blocks.append(("img", (alt or path.stem, path.name, path)))
        elif stripped == "":
            flush_p()
            flush_list()
        else:
            flush_list()
            buf.append(stripped)
    flush_p()
    flush_list()
    flush_table()
    flush_code()
    return blocks


def fig_html(src, caption):
    return (
        f'<figure><img src="images/{src}" alt="{html.escape(caption)}"/>'
        f"<figcaption>{html.escape(caption)}</figcaption></figure>"
    )


def inline_format(text):
    safe = html.escape(text)
    safe = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", safe)
    safe = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", safe)
    safe = re.sub(r"`([^`]+)`", r"<code>\1</code>", safe)
    safe = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"<a href=\"\\2\">\\1</a>", safe)
    return safe


def blocks_to_xhtml(blocks, extra_figures=None):
    parts = []
    found_images = []
    inserted_extra = False
    for kind, data in blocks:
        if kind == "h1":
            parts.append(f"<h1>{html.escape(data)}</h1>")
        elif kind == "h2":
            parts.append(f"<h2>{html.escape(data)}</h2>")
            if not inserted_extra and extra_figures:
                for src, cap in extra_figures:
                    parts.append(fig_html(src, cap))
                inserted_extra = True
        elif kind == "h3":
            parts.append(f"<h3>{html.escape(data)}</h3>")
        elif kind == "blockquote":
            parts.append(f"<blockquote><p>{inline_format(data)}</p></blockquote>")
        elif kind == "pre":
            parts.append(f"<pre><code>{html.escape(data)}</code></pre>")
        elif kind == "p":
            parts.append(f"<p>{inline_format(data)}</p>")
        elif kind == "ul":
            items = "".join(f"<li>{inline_format(item)}</li>" for item in data)
            parts.append(f"<ul>{items}</ul>")
        elif kind == "img":
            alt, name, path = data
            found_images.append((name, path))
            parts.append(fig_html(name, alt))
        elif kind == "table":
            rows = []
            for i, cells in enumerate(data):
                tag = "th" if i == 0 else "td"
                inner = "".join(f"<{tag}>{inline_format(c)}</{tag}>" for c in cells)
                rows.append(f"<tr>{inner}</tr>")
            parts.append("<table>" + "".join(rows) + "</table>")
    if not inserted_extra and extra_figures:
        for src, cap in extra_figures:
            parts.append(fig_html(src, cap))
    return "\n".join(parts), found_images


def xhtml(title, body, lang, rtl):
    direction = ' dir="rtl"' if rtl else ""
    return f"""<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang}" lang="{lang}"{direction}>
<head>
<meta charset="utf-8"/>
<title>{html.escape(title)}</title>
<link rel="stylesheet" type="text/css" href="styles.css"/>
</head>
<body>
{body}
</body>
</html>
"""


CSS = """
body { line-height: 1.5; margin: 1.2em 8%; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
h1 { font-size: 1.5em; line-height: 1.25; margin-top: 0; color: #111; }
h2 { font-size: 1.2em; margin-top: 1.5em; color: #222; }
h3 { font-size: 1.05em; margin-top: 1.2em; color: #333; }
p { margin: 0.7em 0; }
figure { margin: 1.4em 0; text-align: center; }
img { max-width: 100%; height: auto; border: 1px solid #ddd; }
figcaption { font-size: 0.85em; margin-top: 0.4em; color: #555; }
nav ol { line-height: 1.6; }
blockquote { border-left: 3px solid #0066ff; margin: 1em 0; padding-left: 1em; color: #444; }
pre { background: #f4f4f4; padding: 0.8em; overflow-x: auto; font-size: 0.88em; }
code { font-family: monospace; }
table { width: 100%; border-collapse: collapse; margin: 1.2em 0; font-size: 0.9em; }
th, td { border: 1px solid #ccc; padding: 6px 10px; text-align: left; }
th { background-color: #eee; font-weight: bold; }
"""


def build_one(book_key, lang):
    book = BOOKS[book_key]
    meta = LANGS[lang]
    slug = book["slug"]
    src = ROOT / slug / "translations" / lang
    chapters = sorted(src.glob("*.md"))
    if len(chapters) < 10:
        raise SystemExit(f"missing chapters {slug} {lang} {len(chapters)}")

    fig_map = {}
    if book_key == "01":
        fig_map = book1_figures()
    elif book_key == "02":
        fig_map = book2_figures()

    fig_dir = ROOT / slug / "figures"
    items = []
    used_images = {}

    for path in chapters:
        blocks = md_to_blocks(path.read_text(encoding="utf-8"), path.parent)
        title = next((t for k, t in blocks if k == "h1"), path.stem)

        extra_figs = []
        for prefix, rows in fig_map.items():
            if path.name.startswith(prefix):
                for filename, caption in rows:
                    extra_figs.append((filename, caption))
                    p = fig_dir / filename
                    if p.exists():
                        used_images[filename] = p

        body, found_imgs = blocks_to_xhtml(blocks, extra_figs)
        for name, p in found_imgs:
            if p.exists():
                used_images[name] = p
            elif (fig_dir / name).exists():
                used_images[name] = fig_dir / name

        items.append((f"chap-{len(items)+1:02d}.xhtml", title, body))

    title = meta["titles"][book_key]
    rtl = meta["rtl"]
    nav_items = '<li><a href="copyright.xhtml">Copyright</a></li>\n' + "\n".join(
        f'<li><a href="{name}">{html.escape(t)}</a></li>' for name, t, _ in items
    )
    nav = xhtml("Contents", f'<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>{nav_items}</ol></nav>', lang, rtl)
    colophon = xhtml(
        "Copyright",
        f"""<section epub:type="copyright-page">
<h1>{html.escape(title)}</h1>
<p>Tristan. Data Center Field Guides. 2026.</p>
<p>{html.escape(meta["copy"])}</p>
<p>{html.escape(meta["note"])}</p>
<p>6.99 USD. Not enrolled in an exclusive program.</p>
</section>""",
        lang,
        rtl,
    )
    cover_doc = xhtml("Cover", '<section epub:type="cover"><img src="images/cover.jpg" alt="Cover"/></section>', lang, rtl)
    cover_path = ROOT / slug / "figures" / "covers" / f"{lang}.jpg"
    draw_cover(cover_path, f"{book_key}  /  {lang.upper()}", title, meta["subs"][book_key])

    out = ROOT / slug / "epub" / lang / f"{book['file']}.{lang}.epub"
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()

    manifest = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="css" href="styles.css" media-type="text/css"/>',
        '<item id="cover-img" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>',
        '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>',
        '<item id="copyright" href="copyright.xhtml" media-type="application/xhtml+xml"/>',
    ]
    for name in used_images:
        safe_id = name.replace(".", "-").replace("/", "-")
        manifest.append(f'<item id="{safe_id}" href="images/{name}" media-type="image/png"/>')

    spine = ['<itemref idref="cover"/>', '<itemref idref="copyright"/>', '<itemref idref="nav"/>']
    for i, (name, _t, _) in enumerate(items, 1):
        manifest.append(f'<item id="c{i}" href="{name}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="c{i}"/>')

    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="uid" version="3.0" xml:lang="{lang}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:uuid:{slug}-{lang}</dc:identifier>
<dc:title>{html.escape(title)}</dc:title>
<dc:language>{lang}</dc:language>
<dc:creator>Tristan</dc:creator>
<dc:rights>{html.escape(meta["copy"])}</dc:rights>
<meta property="dcterms:modified">2026-10-14T00:00:00Z</meta>
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine>
{chr(10).join(spine)}
</spine>
</package>
"""

    def add(zf, arc, data):
        zf.writestr(arc, data.encode("utf-8") if isinstance(data, str) else data)

    with zipfile.ZipFile(out, "w") as zf:
        info = zipfile.ZipInfo("mimetype")
        info.compress_type = zipfile.ZIP_STORED
        zf.writestr(info, "application/epub+zip")
        add(zf, "META-INF/container.xml", """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles>
<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
</rootfiles>
</container>
""")
        add(zf, "OEBPS/content.opf", opf)
        add(zf, "OEBPS/styles.css", CSS)
        add(zf, "OEBPS/nav.xhtml", nav)
        add(zf, "OEBPS/cover.xhtml", cover_doc)
        add(zf, "OEBPS/copyright.xhtml", colophon)
        for name, _t, body in items:
            add(zf, f"OEBPS/{name}", xhtml(title, body, lang, rtl))
        zf.write(cover_path, "OEBPS/images/cover.jpg")
        for name, path in used_images.items():
            zf.write(path, f"OEBPS/images/{name}")

    pack = ROOT / slug / "publish" / lang / "PACK.md"
    pack.parent.mkdir(parents=True, exist_ok=True)
    pack.write_text(
        f"""# Upload pack

Owner uploads after the store restriction ends. Do not enroll in KDP Select.

## Files

- EPUB: `{out.relative_to(ROOT.parent)}`
- Cover: `{cover_path.relative_to(ROOT.parent)}`
- epubcheck: not run. Java is not installed.

## Listing

- Language: {meta["kdp"]}
- Title: {title}
- Subtitle: {meta["subs"][book_key]}
- Author: Tristan
- Original: {book["en_title"]}
- Price: 6.99 USD
- Not KDP Select

## Description

{meta["desc"][book_key]}

{meta["note"]}

## AI disclosure

- Text: AI-generated English, then AI-assisted translation
- Images: AI-generated
- Translation: Yes

## Do not

Do not log into KDP from this workspace. Do not buy reviews. Do not place ads.
""",
        encoding="utf-8",
    )
    print(f"[{book_key}] {lang}: {out.name} ({out.stat().st_size:,} bytes, {len(used_images)} figs)")


def main():
    for book_key in ("01", "02", "03", "05"):
        for lang in LANGS:
            build_one(book_key, lang)


if __name__ == "__main__":
    main()
