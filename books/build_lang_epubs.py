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
    "04": {
        "slug": "04-judge-a-cfd",
        "en_title": "Judge a CFD Model for Data Centers",
        "file": "judge-a-cfd-model-for-data-centers",
        "build": ROOT / "04-judge-a-cfd" / "build_epub.py",
    },
    "05": {
        "slug": "05-run-the-day",
        "en_title": "Run the Data Center Day: What the manager must sign before the shift ends",
        "file": "run-the-data-center-day",
        "build": ROOT / "05-run-the-day" / "build_epub.py",
    },
    "06": {
        "slug": "06-when-a-monitor-may-speak",
        "en_title": "When a Monitor May Speak: Telemetry, Alarms, and SOE Governance",
        "file": "when-a-monitor-may-speak",
        "build": ROOT / "06-when-a-monitor-may-speak" / "build_epub.py",
    },
    "07": {
        "slug": "07-refuse-the-handover",
        "en_title": "Refuse the Handover: Commissioning Punchlists, Retainage, and Custody Transfer",
        "file": "refuse-the-handover",
        "build": ROOT / "07-refuse-the-handover" / "build_epub.py",
    },
    "08": {
        "slug": "08-judge-a-corrosion-coupon",
        "en_title": "Judge a Corrosion Coupon: ANSI/ISA-71.04-2013 Reactivity & Filtration Audit",
        "file": "judge-a-corrosion-coupon",
        "build": ROOT / "08-judge-a-corrosion-coupon" / "build_epub.py",
    },
    "09": {
        "slug": "09-walk-a-tdd",
        "en_title": "Walk a TDD: Technical Due Diligence Physical Site Audit",
        "file": "walk-a-tdd",
        "build": ROOT / "09-walk-a-tdd" / "build_epub.py",
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
            "04": "データセンターのCFDモデルを審査する",
            "05": "データセンターの1日を回す",
            "06": "監視画面が人を起こしてよいとき",
            "07": "引渡しを拒否する",
            "08": "腐食クーポンを判定する",
            "09": "技術デューデリジェンス（TDD）で現地を歩く",
        },
        "subs": {
            "01": "要求シートと試作の合格判定",
            "02": "速報の現場手引",
            "03": "1回の負荷試験のための7枚のシート",
            "04": "実測ベンチマーク、境界条件監査、ASHRAE熱指標による不受理基準",
            "05": "シフトが終わる前に管理者が署名すべきこと",
            "06": "BMS/EPMSテレメトリ、SOE時刻同期、アラームストーム抑制の現場規律",
            "07": "パンチリスト分類、200%留保金エスクロー、赤入れ竣工図と管理権移管",
            "08": "ANSI/ISA-71.04-2013反応性監視、ケミカルフィルタ破過、鉛フリー基板防護",
            "09": "変電所系統冗長性、500年確率洪水、NVL72床荷重、致命的欠陥の現地監査",
        },
        "desc": {
            "01": "液冷負荷装置は、NVL72級ラックの代わりになる試験器である。冷却器でも図面でもない。この現場手引は、金属を切る前に何を書き、試作を完成と呼ぶ前にどの門を通すかを示す。残るのは、見知らぬ人に渡せる二つの文書である。要求シートと、試作の受入シート。流量、温度、圧力、ダンフォスFD83継手、ダーシー・ワイスバッハ圧力損失の数値は、その時点で有効な仕様を引用するまで空欄のままである。",
            "02": "曲線が穏やかだからといって、負荷装置の試験が有効なのではない。この現場手引は、運転を見知らぬ人が監査できる速報にする方法を示す。速報は五行で開く。事前試験、勾配、過負荷、ステップ変化、単路故障。1秒テレメトリ、欠測判定、熱収支平衡を厳格に監査する。試みた行がすべて合格でなければ、総括は合格ではない。",
            "03": "液冷検証プロジェクトは、支えてよい文を誰も書かないとき、最初の週に失敗する。「液冷は働く」は工学的な主張ではない。願望である。この現場手引は、1回の負荷試験を監査可能な引渡しにするための7枚の検証シートを提供する。ASHRAEガイドライン0/202のレベル1からレベル5までの関門、冷水ポンプ曲線、CDU冗長切替論理、そしてダンフォスFD83継手の受入基準を網羅する。",
            "04": "色彩豊かなCFD（数値流体力学）コンター図は、物理計測で校正されるまでは営業パンフレットに過ぎない。本書は3高さラック吸気計測、フリーアクセスフロア開孔漏れ、RANS乱流モデル残差、SHI/RHI/RCI熱指標、およびNVL72ハイブリッド液冷・空冷熱収支の監査手順を定義する。",
            "05": "管理者が今日持つのは、設備の運転状態、それに触れてよい人、そしてなされたことの改ざん不能な記録である。この現場手引は、30分の対面引継ぎ、SOP/MOP/EOP手順の統治、2N電源の定常負荷上限（0.45 P_rated）、500年確率洪水の防護、そして6箇所の現場巡回点検を定義する。シフトの終わりに残るのは、署名された日次完了シートである。",
            "06": "監視ポイントが当直エンジニアを深夜に起こしてよいのは、そのポイントが4つの必須要素（物理単位付き数値、発生源タイムスタンプ、ハードウェアURI、品質ビットマスク）を備え、断線強制試験に合格している場合のみである。PTP/NTP時刻同期、デッドバンド、アラームストーム抑制を体系化する。",
            "07": "引渡し署名は儀礼ではなく法的な境界文である。カテゴリーA重大欠陥の判定、200%留保金エスクロー、竣工赤入れ図（Redline）の現地照合、LOTO鍵管理権の移管まで、運営側が署名前に拒否すべき条件とマスター拒否シートを提供する。",
            "08": "データホール内の空気腐食は目に見えないまま鉛フリー（RoHS）実装基板を破壊する。ANSI/ISA-71.04-2013に基づく銅・銀クーポンのオングストローム膜厚判定（G1〜GX）、陽圧20 Pa封止、気相ケミカルフィルタの破過試験と検査報告書監査を網羅する。",
            "09": "技術デューデリジェンス（TDD）はコミッショニングではなく、投資家・買主のための致命的欠陥（Fatal Flaw）監査である。特別高圧変電所の物理的異経路検証、500年確率洪水と燃料・水72時間自立性、NVL72級ラックの床荷重（25 kN/m²）とマスターTDDスコアカードを収録する。",
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
            "04": "Menilai Model CFD untuk Pusat Data",
            "05": "Menjalankan Hari Operasional Pusat Data",
            "06": "Kapan Monitor Boleh Berbicara",
            "07": "Menolak Serah Terima (Refuse the Handover)",
            "08": "Menilai Kupon Korosi Pusat Data",
            "09": "Menjalankan Audit Lapangan Uji Tuntas Teknis (TDD)",
        },
        "subs": {
            "01": "Lembar persyaratan dan penerimaan purwarupa",
            "02": "Panduan laporan kilat",
            "03": "Tujuh lembar kerja untuk satu uji bank beban",
            "04": "Tolok ukur pengukuran fisik, audit kondisi batas, dan indeks termal ASHRAE",
            "05": "Apa yang harus ditandatangani manajer sebelum shift berakhir",
            "06": "Tata kelola telemetri BMS/EPMS, sinkronisasi SOE, dan peredaman badai alarm",
            "07": "Daftar cacat komisioning, retensi escrow 200%, audit gambar as-built, dan transfer kustodi",
            "08": "Pemantauan reaktivitas ANSI/ISA-71.04-2013, filtrasi kimia, dan perlindungan RoHS",
            "09": "Diversitas gardu induk, hidrologi banjir 500 tahun, beban lantai NVL72, dan gerbang Fatal Flaw",
        },
        "desc": {
            "01": "Bank beban cair adalah alat uji yang menggantikan rak kelas NVL72. Bukan pendingin, dan bukan gambar fabrikasi. Panduan ini menyatakan apa yang harus ditulis sebelum logam dipotong, dan gerbang mana yang harus lulus sebelum purwarupa disebut selesai. Yang tersisa adalah dua dokumen yang dapat diserahkan kepada orang asing: lembar persyaratan dan lembar penerimaan. Angka aliran, suhu, tekanan, fitting Danfoss FD83, dan penurunan tekanan Darcy-Weisbach tetap kosong sampai Anda mengutip spesifikasi yang berlaku.",
            "02": "Uji bank beban tidak sah hanya karena kurvanya tenang. Panduan ini menunjukkan cara mengubah satu jalan menjadi laporan kilat yang dapat diaudit orang asing. Laporan dibuka dengan lima baris: uji awal, gradien, beban lebih, perubahan langkah, dan gangguan satu jalur. Memeriksa telemetri 1 detik, celah polling, dan keseimbangan termal. Lulus keseluruhan hanya jika setiap baris yang dicoba lulus.",
            "03": "Proyek verifikasi pendinginan cair gagal pada minggu pertama saat tidak ada yang menuliskan pernyataan yang dapat diaudit. 'Pendinginan cair bekerja' bukan klaim teknik; itu adalah angan-angan. Panduan lapangan ini menyediakan 7 lembar verifikasi untuk mengubah satu uji bank beban menjadi serah terima yang siap diaudit. Mencakup gerbang ASHRAE Guideline 0/202 Level 1 hingga 5, kurva pompa dingin, logika kaskade CDU, dan kriteria kopling Danfoss FD83.",
            "04": "Visualisasi warna CFD bukanlah bukti rekayasa sampai dikalibrasi terhadap instrumen fisik di lapangan. Panduan ini menetapkan protokol pengukuran 3-tingkat rak, aerodinamika kebocoran lorong, konvergensi residual RANS, indeks termal SHI/RHI/RCI ASHRAE TC 9.9, serta matriks penolakan model CFD.",
            "05": "Hari ini manajer menguasai kondisi operasional fasilitas, siapa yang boleh menyentuhnya, dan catatan yang tidak dapat diubah dari apa yang telah dikerjakan. Panduan lapangan ini menetapkan serah terima shift 30 menit, tata kelola prosedur SOP/MOP/EOP, batas beban tunak daya 2N (0.45 P_rated), mitigasi banjir 500 tahun, dan 6 stasiun inspeksi fisik. Shift berakhir dengan lembar penutupan manajer yang ditandatangani.",
            "06": "Titik pemantauan hanya boleh membangunkan insinyur jika memiliki empat elemen wajib (nilai berunit teknik, stempel waktu sumber UTC, URI perangkat keras, dan bitmask kualitas) serta lulus uji gagal-paksa. Mencakup sinkronisasi PTP mikrodetik, histeresis deadband, dan peredaman badai alarm.",
            "07": "Tanda tangan serah terima adalah kalimat hukum yang mengikat. Panduan ini mengatur pemisahan cacat Kategori A/B/C, penahanan dana escrow 200%, audit forensik gambar redline as-built, transfer kunci LOTO, dan lembar penolakan serah terima resmi.",
            "08": "Gas korosif menyerang papan sirkuit bebas timbal (RoHS) secara diam-diam. Panduan ini merinci klasifikasi laju korosi tembaga dan perak ANSI/ISA-71.04-2013 (Kelas G1–GX), tekanan positif +20 Pa, pengujian tembus media scrubber kimia, dan protokol kupon blanko kontrol.",
            "09": "Uji Tuntas Teknis (TDD) adalah audit risiko fisik bagi pemberi pinjaman dan pembeli. Mencakup verifikasi jalur transmisi gardu induk, hidrologi banjir 500 tahun, otonomi bahan bakar dan air 72 jam, kapasitas struktural lantai 25 kN/m² untuk rak NVL72, dan kartu skor Fatal Flaw.",
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
            "04": "데이터센터 CFD 모델을 심사하다",
            "05": "데이터센터의 하루를 운영하다",
            "06": "모니터가 경보를 울려도 좋을 때",
            "07": "인수인계를 거부하다",
            "08": "부식 쿠폰을 판정하다",
            "09": "기술 실사(TDD) 현장을 걷다",
        },
        "subs": {
            "01": "요구 시트와 시제품 인수",
            "02": "속보를 위한 현장 안내",
            "03": "단 한 번의 로드뱅크 시험을 위한 일곱 장의 시트",
            "04": "현장 계측 벤치마킹, 경계 조건 감사 및 ASHRAE 열 지수 판정 기준",
            "05": "교대 근무가 끝나기 전 관리자가 반드시 서명해야 하는 것들",
            "06": "BMS/EPMS 텔레메트리, SOE 시각 동기화 및 알람 폭주 억제 거버넌스",
            "07": "커미셔닝 펀치리스트, 200% 유보금 에스크로, 준공 레드라인 도면 및 관리권 이관",
            "08": "ANSI/ISA-71.04-2013 반응성 모니터링, 케미컬 필터 파과 및 무연 RoHS 기판 보호",
            "09": "변전소 계통 이중화, 500년 빈도 홍수 수문학, NVL72 바닥 하중 및 치명적 결함 감사",
        },
        "desc": {
            "01": "액랭 로드뱅크는 NVL72급 랙을 대신하는 시험 장치이다. 냉각기도 아니고 제작 도면도 아니다. 이 현장 안내는 금속을 자르기 전에 무엇을 적는지, 시제품을 끝났다고 부르기 전에 어느 문을 통과하는지를 말한다. 남는 것은 낯선 사람에게 건넬 수 있는 두 문서이다. 요구 시트와 인수 시트. 유량, 온도, 압력, 댄포스 FD83 커플링, 다르시-바이스바흐 압력 강하는 그때 유효한 규격을 인용하기 전까지 비워 둔다.",
            "02": "곡선이 잔잔하다고 해서 로드뱅크 시험이 유효한 것은 아니다. 이 안내는 한 번의 운전을 낯선 사람이 감사할 수 있는 속보로 만드는 방법을 말한다. 속보는 다섯 줄로 시작한다. 사전 시험, 구배, 과부하, 스텝 변화, 단로 고장. 1초 텔레메트리, 폴링 결측 감지, 열 평형 검증을 수행한다. 시도한 줄이 모두 합격이 아니면 총괄은 합격이 아니다.",
            "03": "액랭 검증 프로젝트는 감사 가능한 문장을 아무도 쓰지 않을 때 첫 주에 실패한다. '액랭이 작동한다'는 공학적 주장이 아니라 희망 사항일 뿐이다. 이 현장 안내서는 한 번의 로드뱅크 시험을 완벽한 인수인계로 전환하는 7장의 검증 시트를 제공한다. ASHRAE 가이드라인 0/202 레벨 1~5 관문, 냉수 펌프 곡선, CDU 다중 펌프 캐스케이드 로직, 댄포스 FD83 퀵 커플링 인수 기준을 체계화한다.",
            "04": "화려한 CFD 온도 분포도는 보정된 현장 계측기로 검증되기 전까지는 마케팅 그림에 불과하다. 본 지침서는 3단 랙 흡기 온도 계측, 이중마루 개구부 누기 역학, RANS 난류 모델 수렴 감사, SHI/RHI/RCI 열 지수, NVL72 하이브리드 액랭·공랭 열 분할 검증 및 CFD 보고서 반려 매트릭스를 제시한다.",
            "05": "오늘 관리자가 통제하는 것은 플랜트의 운전 상태, 플랜트를 건드릴 수 있는 사람, 그리고 수행된 작업에 대한 변경 불가능한 기록이다. 이 현장 지침은 30분 대면 교대 인수인계, SOP/MOP/EOP 절차 피라미드, 2N 전력 정상상태 부하 한도(0.45 P_rated), 500년 빈도 홍수 방호, 그리고 6대 순회 점검 구역을 규정한다. 교대 근무의 끝에는 서명된 일일 마감 시트가 남는다.",
            "06": "관제 포인트가 당직 엔지니어를 깨울 수 있는 것은 4대 필수 속성(공학 단위 값, UTC 원천 타임스탬프, 하드웨어 URI, 품질 비트마스크)을 갖추고 강제 단선 시험을 통과했을 때뿐이다. IEEE 1588v2 PTP 마이크로초 SOE 동기화, 데드밴드 히스테리시스, 위상 기반 알람 폭주 억제를 다룬다.",
            "07": "인수 서명은 의례가 아니라 법적 책임을 이관하는 문장이다. 카테고리 A/B/C 결함 분류, 미해결 결함에 대한 200% 유보금 에스크로, 현장 배관과 준공 레드라인 도면의 대조 감사, LOTO 열쇠 인계 및 마스터 인수 거부 시트를 수록한다.",
            "08": "데이터홀 내부의 부식성 가스는 무연(RoHS) 서버 기판을 소리 없이 파괴한다. ANSI/ISA-71.04-2013 구리·은 쿠폰의 옹스트롬 반응률 판정(G1~GX 등급), +20 Pa 양압 기밀 유지, 화학 필터 파과 시험 및 실험실 쿠폰 성적서 반려 기준을 제공한다.",
            "09": "기술 실사(TDD)는 커미셔닝이 아니라 대주단과 매수인을 위한 치명적 결함(Fatal Flaw) 현장 감사이다. 변전소 인입선 물리적 이원화, 500년 빈도 홍수 수문학, 연료 및 냉각수 72시간 자립 운전, NVL72 고밀도 랙 바닥 구조 하중(25 kN/m²) 및 마스터 TDD 스코어카드를 제공한다.",
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
            "04": "ตัดสินแบบจำลอง CFD สำหรับดาต้าเซ็นเตอร์",
            "05": "บริหารจัดการวันปฏิบัติงานของดาต้าเซ็นเตอร์",
            "06": "เมื่อใดที่หน้าจอมอนิเตอร์ได้รับอนุญาตให้แจ้งเตือน",
            "07": "ปฏิเสธการรับมอบงาน (Refuse the Handover)",
            "08": "ตัดสินผลการตรวจวัดแผ่นคูปองการกัดกร่อน",
            "09": "เดินตรวจประเมินสถานะทางเทคนิคภาคสนาม (TDD)",
        },
        "subs": {
            "01": "แผ่นข้อกำหนดและการตรวจรับต้นแบบ",
            "02": "คู่มือรายงานฉับพลัน",
            "03": "เจ็ดแผ่นงานสำหรับการทดสอบโหลดแบงก์หนึ่งครั้ง",
            "04": "การเทียบมาตรฐานการวัดจริง การตรวจสอบเงื่อนไขขอบเขต และดัชนีความร้อน ASHRAE",
            "05": "สิ่งที่ผู้จัดการต้องลงนามก่อนสิ้นสุดกะการทำงาน",
            "06": "การกำกับดูแลเทเลเมทรี BMS/EPMS การซิงค์เวลา SOE และการระงับพายุสัญญาณเตือน",
            "07": "รายการข้อบกพร่อง เงินประกันผลงาน 200% การตรวจสอบแบบ As-Built และการโอนย้ายการควบคุม",
            "08": "การเฝ้าระวังปฏิกิริยาตาม ANSI/ISA-71.04-2013 สารกรองเคมี และการปกป้องแผงวงจร RoHS",
            "09": "ความหลากหลายของสายส่งสถานีไฟฟ้าย่อย อุทกวิทยาน้ำท่วมรอบ 500 ปี น้ำหนักบรรทุกพื้น NVL72 และเกณฑ์ Fatal Flaw",
        },
        "desc": {
            "01": "โหลดแบงก์ของเหลวเป็นเครื่องมือทดสอบที่แทนแร็คระดับ NVL72 ไม่ใช่เครื่องทำความเย็น และไม่ใช่แบบสำหรับการผลิต คู่มือนี้บอกว่าต้องเขียนอะไรก่อนตัดโลหะ และต้องผ่านประตูใดก่อนจะเรียกต้นแบบว่าเสร็จ สิ่งที่เหลือคือเอกสารสองฉบับที่มอบให้คนแปลกหน้าได้ แผ่นข้อกำหนด และแผ่นตรวจรับ ตัวเลขอัตราไหล อุณหภูมิ ความดัน ข้อต่อ Danfoss FD83 และความดันลด Darcy-Weisbach เว้นว่างจนกว่าจะอ้างข้อกำหนดที่มีผลในขณะนั้น",
            "02": "การทดสอบโหลดแบงก์ไม่ถูกต้องเพียงเพราะเส้นโค้งดูสงบ คู่มือนี้บอกวิธีเปลี่ยนการเดินเครื่องหนึ่งครั้งให้เป็นรายงานฉับพลันที่คนแปลกหน้าตรวจสอบได้ รายงานเปิดด้วยห้าบรรทัด การทดสอบก่อน การไต่โหลด โอเวอร์โหลด การเปลี่ยนขั้น และความผิดพลาดของแหล่งจ่ายเดียว ตรวจสอบเทเลเมทรี 1 วินาที ช่องว่างข้อมูล และสมดุลความร้อน ผ่านโดยรวมได้ก็ต่อเมื่อทุกบรรทัดที่ลองผ่าน",
            "03": "โครงการตรวจสอบระบบระบายความร้อนด้วยของเหลวล้มเหลวตั้งแต่สัปดาห์แรกหากไม่มีใครเขียนประโยคอ้างสิทธิ์ที่ตรวจสอบได้ 'ระบบระบายความร้อนด้วยของเหลวทำงานได้' ไม่ใช่ข้ออ้างทางวิศวกรรม แต่เป็นเพียงความปรารถนา คู่มือภาคสนามนี้นำเสนอแผ่นงานการตรวจสอบ 7 แผ่น ครอบคลุมประตู ASHRAE Guideline 0/202 ระดับ 1 ถึง 5, เส้นโค้งปั๊มน้ำเย็น, ตรรกะ CDU และเกณฑ์ข้อต่อ Danfoss FD83",
            "04": "ภาพสีจำลอง CFD เป็นเพียงแผ่นพับการขายจนกว่าจะได้รับการปรับเทียบด้วยเครื่องมือวัดจริงในสนาม คู่มือนี้กำหนดโปรโตคอลการวัดอุณหภูมิหน้าแร็ค 3 ระดับ สมการการรั่วไหลของพื้นยก การลู่เข้าของสมการปั่นป่วน RANS ดัชนีความร้อน SHI/RHI/RCI ของ ASHRAE TC 9.9 และตารางปฏิเสธรายงาน CFD",
            "05": "วันนี้ผู้จัดการเป็นเจ้าของสถานะการทำงานของโรงงาน คนที่ได้รับอนุญาตให้สัมผัสอุปกรณ์ และบันทึกสิ่งที่ทำไปแล้ว คู่มือภาคสนามนี้กำหนดกระบวนการส่งมอบกะ 30 นาที, ลำดับขั้นขั้นตอน SOP/MOP/EOP, ขีดจำกัดโหลดคงที่ระบบไฟ 2N (0.45 P_rated), การป้องกันน้ำท่วมรอบ 500 ปี และ 6 สถานีตรวจการณ์ประจำกะ จบกะด้วยแผ่นงานปิดกะที่มีลายมือชื่อ",
            "06": "จุดตรวจวัดจะได้รับอนุญาตให้ปลุกวิศวกรเวรได้ก็ต่อเมื่อมีองค์ประกอบครบ 4 ประการ (ค่าพร้อมหน่วยวิศวกรรม เวลาต้นทาง UTC ที่อยู่ฮาร์ดแวร์ URI และบิตมาสก์คุณภาพ) และผ่านการทดสอบบังคับสายขาด ครอบคลุมการซิงค์เวลา PTP ระดับไมโครวินาที ฮิสเทอรีซิสเดดแบนด์ และการสกัดพายุสัญญาณเตือน",
            "07": "ลายมือชื่อรับมอบงานคือประโยคผูกพันทางกฎหมาย คู่มือนี้กำหนดการจำแนกข้อบกพร่องประเภท A/B/C การหักเงินประกันเอสโครว์ 200% การตรวจสอบแบบแก้ไข Redline As-Built การส่งมอบกุญแจ LOTO และใบปฏิเสธการรับมอบงานหลัก",
            "08": "ก๊าซกัดกร่อนในอากาศทำลายแผงวงจรไร้สารตะกั่ว (RoHS) อย่างเงียบเชียบ คู่มือนี้ระบุเกณฑ์อัตราการเกิดปฏิกิริยาของคูปองทองแดงและเงินตามมาตรฐาน ANSI/ISA-71.04-2013 (คลาส G1–GX) การอัดความดันบวก +20 Pa การทดสอบการทะลุผ่านของสารกรองเคมี และโปรโตคอลคูปองอ้างอิง",
            "09": "การตรวจสอบสถานะทางเทคนิค (TDD) คือการตรวจหาความเสี่ยงร้ายแรง (Fatal Flaw) สำหรับผู้ให้กู้และผู้ซื้อ ครอบคลุมการตรวจสอบสายส่งสถานีไฟฟ้าย่อยแยกอิสระ อุทกวิทยาน้ำท่วมรอบ 500 ปี ความสามารถพึ่งตนเองของเชื้อเพลิงและน้ำ 72 ชั่วโมง น้ำหนักบรรทุกพื้น 25 kN/m² สำหรับแร็ค NVL72 และตารางคะแนน TDD หลัก",
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
            "04": "تقييم نموذج ديناميكا الموائع الحسابية (CFD) لمراكز البيانات",
            "05": "إدارة يوم مركز البيانات",
            "06": "متى يُسمح للشاشة أن تتكلم",
            "07": "رفض استلام المنشأة (Refuse the Handover)",
            "08": "تقييم قسيمة التآكل الجوي في مراكز البيانات",
            "09": "إجراء الفحص الميداني للعناية الواجبة التقنية (TDD)",
        },
        "subs": {
            "01": "ورقة المتطلبات وقبول النموذج",
            "02": "دليل التقرير العاجل",
            "03": "سبع أوراق لاختبار بنك حمل واحد",
            "04": "القياس الميداني المرجعي، وتدقيق شروط الحدود، ومؤشرات ASHRAE الحرارية",
            "05": "ما يجب أن يوقعه المدير قبل انتهاء الوردية",
            "06": "حوكمة القياس عن بُعد BMS/EPMS، وتزامن أحداث SOE، وكبح عواصف الإنذار",
            "07": "قوائم العيوب، واحتجاز الضمان بنسبة 200%، وتدقيق مخططات التنفيذ الفعلي ونقل العهدة",
            "08": "مراقبة التفاعلية وفق ANSI/ISA-71.04-2013، والترشيح الكيميائي، وحماية لوحات RoHS",
            "09": "تنوع المحطات الفرعية، وهيدرولوجيا فيضان 500 عام، وأحمال أرضيات NVL72، وبوابات العيوب القاتلة",
        },
        "desc": {
            "01": "بنك الحمل السائل أداة اختبار تقوم مقام رف من فئة NVL72. ليس مبردًا، وليس رسم تصنيع. يبيّن هذا الدليل ما يُكتب قبل قطع المعدن، وأي بوابات يجب أن تجتاز قبل أن يُسمى النموذج منتهيًا. ما يبقى وثيقتان يمكن تسليمهما لغريب: ورقة المتطلبات وورقة القبول. تبقى أرقام التدفق والحرارة والضغط ووصلات Danfoss FD83 وهبوط ضغط دارسي-فايسباخ فارغة حتى تستشهد بالمواصفة النافذة.",
            "02": "اختبار بنك الحمل ليس صالحًا لأن المنحنى يبدو هادئًا. يبيّن هذا الدليل كيف تحوّل تشغيلًا واحدًا إلى تقرير عاجل يستطيع غريب أن يدققه. يفتح التقرير بخمسة أسطر: الاختبار المسبق، والتدرج، والحمل الزائد، وتغير الخطوة، وعطل مسار واحد. فحص قياس عن بُعد بدقة ثانية واحدة، وفجوات الاستطلاع، والتوازن الحراري. لا تنجح النتيجة الإجمالية إلا إذا نجح كل سطر جُرّب.",
            "03": "يفشل مشروع التحقق من التبريد السائل في أسبوعه الأول عندما لا يكتب أحد جملة ادعاء قابلة للتدقيق. 'التبريد السائل يعمل' ليست ادعاءً هندسيًا بل مجرد أمنية. يقدّم هذا الدليل الميداني 7 أوراق تحقق لتحويل اختبار بنك الحمل إلى تسليم معتمد. يغطي بوابات ASHRAE Guideline 0/202 من المستوى 1 إلى 5، ومنحنيات المضخات الباردة، ومنطق تتابع CDU، ومعايير وصلات Danfoss FD83.",
            "04": "لوحات الألوان في تقارير CFD ليست سوى كتيب تسويقي حتى تتم معايرتها بأدوات قياس فيزيائية في الموقع. يحدد هذا الدليل بروتوكول القياس ثلاثي المستويات، وديناميكا تسرب الأرضيات المرتفعة، وتقارب بواقي معادلات RANS، ومؤشرات SHI/RHI/RCI الحرارية، ومصفوفة رفض تقارير CFD.",
            "05": "ما يمتلكه المدير اليوم هو الحالة التشغيلية للمنشأة، ومن يُسمح له بلمسها، والسجل غير القابل للتغيير لما تم إنجازه. يحدد هذا الدليل الميداني تسليم الوردية وجهًا لوجه لمدة 30 دقيقة، وهرم إجراءات SOP/MOP/EOP، وسقف الحمل المستقر لمنظومة 2N الكهربائية (0.45 P_rated)، والحماية من فيضان 500 عام، و6 محطات للجولة التفتيشية. تنتهي الوردية بورقة إغلاق موقعة.",
            "06": "لا يُسمح لنقطة المراقبة بإيقاظ المهندس المناوب إلا إذا امتلكت العناصر الأربعة الإلزامية (قيمة بوحدة هندسية، وطابع زمني UTC من المصدر، ومعرّف عتاد URI، وقناع بتات الجودة) واجتازت اختبار القطع القسري. يغطي تزامن PTP بدقة الميكروثانية، ونطاق التخلف الميت، وكبح عواصف الإنذار.",
            "07": "توقيع الاستلام ليس مجاملة بل جملة التزام قانوني. يحدد هذا الدليل تصنيف عيوب الفئات A/B/C، واحتجاز ضمان مالي بنسبة 200%، والتدقيق الجنائي لمخططات التنفيذ الفعلي (Redline As-Built)، ونقل عهدة أقفال LOTO، وورقة رفض الاستلام الرئيسية.",
            "08": "تهاجم الغازات المسببة للتآكل اللوحات الإلكترونية الخالية من الرصاص (RoHS) بصمت. يفصّل هذا الدليل تصنيف معدلات تآكل النحاس والفضة وفق معيار ANSI/ISA-71.04-2013 (الفئات G1–GX)، والضغط الإيجابي (+20 Pa)، واختبار اختراق وسائط الترشيح الكيميائي، وبروتوكول القسائم المرجعية.",
            "09": "العناية الواجبة التقنية (TDD) ليست اختبار تشغيل بل تدقيق مخاطر ميداني للمقرضين والمشترين. يغطي التحقق من التنوع الفيزيائي لمغذيات المحطات الفرعية، وهيدرولوجيا فيضان 500 عام، واستقلالية الوقود والمياه لمدة 72 ساعة، وقدرة تحمل الأرضيات (25 kN/m²) لأرفف NVL72، وبطاقة الأداء الرئيسية.",
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


from epub_renderer import (
    SHARED_CSS,
    blocks_to_xhtml,
    fig_html,
    inline_format,
    md_to_blocks,
)


def book1_figures():
    return {
        "01-": [
            ("fig-01-boundary-architecture.png", "Figure 01. Primary CDU Facility Loop vs. Secondary Rack-Side Load Bank Boundary & 80:20 Sensible Heat Split."),
        ],
        "02-": [
            ("fig-07-sandbox-calculation-model.png", "Figure 07. Educational Reference Sandbox: 120 kW Virtual Rack Thermodynamic & Hydraulic Derivation Model."),
        ],
        "03-": [
            ("fig-02-loadbank-pid.png", "Figure 02. Liquid Load Bank Piping & Instrumentation Diagram (P&ID) with Danfoss FD83 Couplings & 50 μm Bypass Flushing Loop."),
        ],
        "05-": [
            ("fig-03-sensor-installation.png", "Figure 03. Sensor Installation Metrology: Core Stream Immersion vs. Dead-Leg Stub Pitfalls."),
        ],
        "06-": [
            ("fig-04-electrical-interlock-2n.png", "Figure 04. 2N Dual-Feeder Electrical Distribution & Class-1 Hardwired Emergency Trip Loop."),
        ],
        "07-": [
            ("fig-06-gate-statemachine.png", "Figure 06. Sequential Prototype Acceptance Gate State Machine & Hard Waiver Protocols."),
        ],
        "15-": [
            ("fig-05-timeseries-diagnostics.png", "Figure 05. Four-Quadrant Time-Series Diagnostic Signatures: Valid Plateaus vs. Stale Data, Bypass Leak, and Water Hammer."),
        ],
    }


def book2_figures():
    out = {}
    try:
        mod = load_module(BOOKS["02"]["build"], "b2")
        if hasattr(mod, "FIGS"):
            for prefix, _heading, filename, caption, *_rest in mod.FIGS:
                if filename.startswith("fig-0"):
                    out.setdefault(prefix, []).append((filename, caption))
    except Exception:
        pass
    return out


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


CSS = SHARED_CSS.replace('@font-face { font-family: "DejaVu Sans"; src: url("fonts/DejaVuSans.ttf"); }\n@font-face { font-family: "DejaVu Sans"; src: url("fonts/DejaVuSans-Bold.ttf"); font-weight: bold; }\n', "")



def build_one(book_key, lang):
    book = BOOKS[book_key]
    meta = LANGS[lang]
    slug = book["slug"]
    src = ROOT / slug / "translations" / lang
    chapters = sorted(src.glob("*.md"))
    if len(chapters) < 9:
        raise SystemExit(f"missing chapters {slug} {lang} {len(chapters)}")

    fig_map = {}
    if book_key == "01":
        fig_map = book1_figures()
    elif book_key == "02":
        fig_map = book2_figures()

    fig_dir = ROOT / slug / "figures"
    items = []
    used_images = {}
    seen_images = set()

    for path in chapters:
        raw_md = path.read_text(encoding="utf-8")
        lines = raw_md.splitlines()
        if lines and lines[0].strip() == meta["note"]:
            lines = lines[1:]
            while lines and not lines[0].strip():
                lines = lines[1:]
            raw_md = "\n".join(lines)
        blocks = md_to_blocks(raw_md, path.parent)
        title = next((t for k, t in blocks if k == "h1"), path.stem)

        extra_figs = []
        for prefix, rows in fig_map.items():
            if path.name.startswith(prefix):
                for filename, caption in rows:
                    if filename not in seen_images:
                        extra_figs.append((filename, caption))
                        p = fig_dir / filename
                        if p.exists():
                            used_images[filename] = p

        body, found_imgs = blocks_to_xhtml(blocks, extra_figs, seen_images=seen_images)
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

    spine_attr = ' page-progression-direction="rtl"' if rtl else ""
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
<spine{spine_attr}>
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
    for book_key in sorted(BOOKS.keys()):
        slug = BOOKS[book_key]["slug"]
        for lang in LANGS:
            src = ROOT / slug / "translations" / lang
            if src.exists() and len(list(src.glob("*.md"))) >= 9:
                build_one(book_key, lang)


if __name__ == "__main__":
    main()
