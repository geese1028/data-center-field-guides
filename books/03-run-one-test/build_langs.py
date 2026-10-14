#!/usr/bin/env python3
import html
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from build_epub import CSS, blocks_to_xhtml, md_to_blocks

ROOT = Path("/Users/geese/Downloads/book/books/03-run-one-test")
FIG = ROOT / "figures"
FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
BG = (30, 30, 30)
BLUE = (0, 102, 255)
CYAN = (0, 255, 255)
GRID = (42, 42, 42)
TEXT = (255, 255, 255)
FILE = "finish-a-liquid-cooling-verification"

LANGS = {
    "ja": {
        "rtl": False,
        "kdp": "Japanese",
        "title": "液冷の検証を終える",
        "sub": "負荷装置試験のための七枚のシート",
        "copy": "英語版をAI補助で翻訳した。英語版の本文と図はAI生成である。",
        "note": "図中の文字は英語版のままである。",
        "desc": "午後が熱かったからといって、負荷装置試験が終わったわけではない。この現場手引は、受け渡し済みの負荷装置をラックの代わりに接続し、承認されたスクリプトを実行し、見知らぬ人が監査できるシートを残す方法を示す。空欄は停止である。前の現場の数字は引用ではない。証明書の Level 1 は工場試験である。静的な目視をその枠へ綴じてはならない。",
        "keys": ["負荷装置試験", "液冷の検証", "CDU試験シート", "データセンター試運転", "熱負荷の段階", "是正リスト", "ラック液冷試験"],
    },
    "id": {
        "rtl": False,
        "kdp": "Indonesian",
        "title": "Menyelesaikan Verifikasi Pendinginan Cair",
        "sub": "Tujuh lembar untuk satu uji bank beban",
        "copy": "Terjemahan berbantuan AI dari edisi bahasa Inggris. Teks dan gambar edisi Inggris dihasilkan dengan AI.",
        "note": "Label pada gambar tetap dalam bahasa Inggris.",
        "desc": "Uji bank beban tidak selesai hanya karena sore itu panas. Panduan ini menunjukkan cara menyambungkan bank beban yang sudah diterima sebagai pengganti rak, menjalankan skrip yang disetujui, dan meninggalkan lembar yang dapat diaudit orang asing. Sel kosong adalah berhenti. Angka dari aula sebelumnya bukan kutipan. Level 1 pada sertifikat adalah uji pabrik. Pemeriksaan statis tidak masuk ke slot itu.",
        "keys": ["uji bank beban", "verifikasi pendingin cair", "lembar uji CDU", "commissioning pusat data", "langkah beban panas", "daftar cacat", "uji cair rak"],
    },
    "ko": {
        "rtl": False,
        "kdp": "Korean",
        "title": "액랭 검증을 마치다",
        "sub": "로드뱅크 시험 한 번을 위한 일곱 장",
        "copy": "영어판을 AI 보조로 번역했다. 영어판의 글과 그림은 AI가 생성했다.",
        "note": "그림 안의 글자는 영어 그대로이다.",
        "desc": "오후가 뜨거웠다고 로드뱅크 시험이 끝난 것은 아니다. 이 안내는 이미 인수된 로드뱅크를 랙 대신 연결하고, 승인된 스크립트를 실행하고, 낯선 사람이 감사할 수 있는 시트를 남기는 방법을 말한다. 빈 칸은 정지이다. 이전 현장의 숫자는 인용이 아니다. 증명서의 Level 1은 공장 시험이다. 정적 점검을 그 칸에 넣지 않는다.",
        "keys": ["로드뱅크 시험", "액랭 검증", "CDU 시험 시트", "데이터센터 커미셔닝", "열부하 단계", "시정 목록", "랙 액랭 시험"],
    },
    "th": {
        "rtl": False,
        "kdp": "Thai",
        "title": "จบการทวนสอบการหล่อเย็นด้วยของเหลว",
        "sub": "เจ็ดแผ่นสำหรับการทดสอบโหลดแบงก์หนึ่งครั้ง",
        "copy": "แปลจากฉบับภาษาอังกฤษโดยมี AI ช่วย ข้อความและรูปในฉบับภาษาอังกฤษสร้างด้วย AI",
        "note": "ตัวอักษรในรูปยังเป็นภาษาอังกฤษ",
        "desc": "การทดสอบโหลดแบงก์ไม่จบเพียงเพราะช่วงบ่ายร้อน คู่มือนี้บอกวิธีต่อโหลดแบงก์ที่รับแล้วแทนแร็ค เดินสคริปต์ที่อนุมัติ และทิ้งแผ่นที่คนแปลกหน้าตรวจสอบได้ ช่องว่างคือการหยุด ตัวเลขจากไซต์ก่อนไม่ใช่การอ้างอิง Level 1 ของใบรับรองคือการทดสอบโรงงาน การตรวจแบบไม่จ่ายไฟไม่ใช่ช่องนั้น",
        "keys": ["ทดสอบโหลดแบงก์", "ทวนสอบหล่อเย็นของเหลว", "แผ่นทดสอบ CDU", "คอมมิชชันนิงศูนย์ข้อมูล", "ขั้นภาระความร้อน", "รายการแก้ไข", "ทดสอบของเหลวแร็ค"],
    },
    "ar": {
        "rtl": True,
        "kdp": "Arabic",
        "title": "إنهاء التحقق من التبريد السائل",
        "sub": "سبع أوراق لاختبار بنك حمل واحد",
        "copy": "ترجمة بمساعدة الذكاء الاصطناعي من الطبعة الإنجليزية. نص الطبعة الإنجليزية ورسومها مولَّدة بالذكاء الاصطناعي.",
        "note": "تبقى الكتابة داخل الرسوم بالإنجليزية.",
        "desc": "اختبار بنك الحمل لا ينتهي لأن العصر كان حارًا. يبيّن هذا الدليل كيف توصل بنك حمل مقبولًا بدل الرف، وتدير النصوص المعتمدة، وتترك أوراقًا يستطيع غريب أن يدققها. الخانة الفارغة توقف. رقم من قاعة سابقة ليس استشهادًا. المستوى 1 في الشهادة هو اختبار المصنع. الفحص الساكن لا يُودع في ذلك الموضع.",
        "keys": ["اختبار بنك الحمل", "التحقق من التبريد السائل", "أوراق اختبار CDU", "تشغيل مركز البيانات", "خطوات الحمل الحراري", "قائمة العيوب", "اختبار سائل للرف"],
    },
}


def font(size):
    return ImageFont.truetype(FONT, size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        cur = ""
        step = 1 if any("\u0600" <= ch <= "\u06ff" or "\u0e00" <= ch <= "\u0e7f" or "\u3040" <= ch <= "\u30ff" or "\u4e00" <= ch <= "\u9fff" or "\uac00" <= ch <= "\ud7af" for ch in para) else 0
        if step:
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
        else:
            for word in para.split():
                trial = word if not cur else cur + " " + word
                if draw.textlength(trial, font=fnt) <= width:
                    cur = trial
                else:
                    if cur:
                        lines.append(cur)
                    cur = word
            if cur:
                lines.append(cur)
    return lines


def draw_cover(path, lang, title, subtitle):
    im = Image.new("RGB", (1600, 2560), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, 1600, 40):
        d.line((x, 0, x, 2560), fill=GRID)
    for y in range(0, 2560, 40):
        d.line((0, y, 1600, y), fill=GRID)
    d.rectangle((18, 18, 1581, 2541), outline=BLUE, width=2)
    d.rectangle((70, 160, 90, 2100), fill=CYAN)
    d.text((140, 180), f"03  /  {lang.upper()}", font=font(28), fill=CYAN)
    y = 360
    display = font(60)
    for line in wrap(d, title, display, 1280):
        d.text((140, y), line, font=display, fill=TEXT)
        y += 84
    d.line((140, y + 24, 980, y + 24), fill=CYAN, width=2)
    yy = y + 56
    for line in wrap(d, subtitle, font(32), 1280):
        d.text((140, yy), line, font=font(32), fill=CYAN)
        yy += 48
    d.text((140, 2280), "TRISTAN", font=font(36), fill=CYAN)
    d.text((140, 2360), "DATA CENTER FIELD GUIDES", font=font(28), fill=TEXT)
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path.with_suffix(".png"), "PNG")
    im.convert("RGB").save(path, "JPEG", quality=95, optimize=True)


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


def build(lang):
    meta = LANGS[lang]
    src = ROOT / "translations" / lang
    chapters = sorted(src.glob("*.md"))
    if len(chapters) != 17:
        raise SystemExit(f"{lang} chapters {len(chapters)}")
    items = []
    images = {}
    for path in chapters:
        blocks = md_to_blocks(path.read_text(), ROOT / "chapters")
        title = next((t for k, t in blocks if k == "h1"), path.stem)
        body, figs = blocks_to_xhtml(blocks)
        for name, fig in figs:
            images[name] = fig
        items.append((f"chap-{len(items)+1:02d}.xhtml", title, body))
    rtl = meta["rtl"]
    title = meta["title"]
    cover_path = FIG / "covers" / f"{lang}.jpg"
    draw_cover(cover_path, lang, title, meta["sub"])
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
    manifest = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="css" href="styles.css" media-type="text/css"/>',
        '<item id="cover-img" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>',
        '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>',
        '<item id="copyright" href="copyright.xhtml" media-type="application/xhtml+xml"/>',
    ]
    spine = ['<itemref idref="cover"/>', '<itemref idref="copyright"/>', '<itemref idref="nav"/>']
    for name in sorted(images):
        manifest.append(f'<item id="img-{name.replace(".", "-")}" href="images/{name}" media-type="image/png"/>')
    for i, (name, _t, _) in enumerate(items, 1):
        manifest.append(f'<item id="c{i}" href="{name}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="c{i}"/>')
    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="uid" version="3.0" xml:lang="{lang}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:uuid:book-03-{lang}</dc:identifier>
<dc:title>{html.escape(title)}</dc:title>
<dc:language>{lang}</dc:language>
<dc:creator>Tristan</dc:creator>
<dc:rights>{html.escape(meta["copy"])}</dc:rights>
<meta property="dcterms:modified">2026-10-11T00:00:00Z</meta>
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine>
{chr(10).join(spine)}
</spine>
</package>
"""
    out = ROOT / "epub" / lang / f"{FILE}.{lang}.epub"
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()
    container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles>
<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
</rootfiles>
</container>
"""

    def add(zf, arc, data):
        zf.writestr(arc, data.encode("utf-8") if isinstance(data, str) else data)

    with zipfile.ZipFile(out, "w") as zf:
        info = zipfile.ZipInfo("mimetype")
        info.compress_type = zipfile.ZIP_STORED
        zf.writestr(info, "application/epub+zip")
        add(zf, "META-INF/container.xml", container)
        add(zf, "OEBPS/content.opf", opf)
        add(zf, "OEBPS/styles.css", CSS)
        add(zf, "OEBPS/nav.xhtml", nav)
        add(zf, "OEBPS/cover.xhtml", cover_doc)
        add(zf, "OEBPS/copyright.xhtml", colophon)
        for name, chap_title, body in items:
            add(zf, f"OEBPS/{name}", xhtml(chap_title, body, lang, rtl))
        zf.write(cover_path, "OEBPS/images/cover.jpg")
        for name, path in images.items():
            if not path.exists():
                raise SystemExit(f"missing {path}")
            zf.write(path, f"OEBPS/images/{name}")
    pack = ROOT / "publish" / lang / "PACK.md"
    pack.parent.mkdir(parents=True, exist_ok=True)
    keys = "\n".join(f"{i}. {k}" for i, k in enumerate(meta["keys"], 1))
    pack.write_text(
        f"""# Upload pack

Owner uploads. Do not enroll in KDP Select. New Kindle eBook. Do not replace the English listing.

## Files

- EPUB: `books/03-run-one-test/epub/{lang}/{FILE}.{lang}.epub`
- Cover: `books/03-run-one-test/figures/covers/{lang}.jpg`
- epubcheck: not run. Java is not installed.

## Listing

- Language: {meta["kdp"]}
- Title: {title}
- Subtitle: {meta["sub"]}
- Author: Tristan
- Price: 6.99 USD
- Not KDP Select

## Description

{meta["desc"]}

{meta["note"]}

## Keywords

{keys}

## AI

Text: AI-generated English, then AI-assisted translation. Images: AI-generated. Translation: Yes. Tool: Grok.
""",
        encoding="utf-8",
    )
    z = zipfile.ZipFile(out)
    first = z.namelist()[0]
    print(lang, out.stat().st_size, "chapters", len(items), "images", len(images), "mimetype", first, z.read(first))


if __name__ == "__main__":
    for lang in LANGS:
        over = [k for k in LANGS[lang]["keys"] if len(k) > 50]
        if over:
            raise SystemExit(over)
        build(lang)
