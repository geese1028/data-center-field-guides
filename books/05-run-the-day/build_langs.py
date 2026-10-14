#!/usr/bin/env python3
import html
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from build_epub import CSS, blocks_to_xhtml, md_to_blocks

ROOT = Path("/Users/geese/Downloads/book/books/05-run-the-day")
FIG = ROOT / "figures"
FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
FILE = "run-the-data-center-day"

LANGS = {
    "ja": {
        "rtl": False,
        "kdp": "Japanese",
        "title": "データセンターの一日を回す",
        "sub": "交代が終わる前に管理者が署名するもの",
        "copy": "英語版をAI補助で翻訳した。英語版の本文はAI生成である。図中の文字もこの言語である。",
        "note": "これは講習の要約ではない。CDFOM と CDFOS は課程名である。",
        "desc": "部屋が静かだからといって、データセンターの一日が管理されたわけではない。当直の管理者のための現場手引である。何を持ち、誰が触れてよいか、実際に売ったサービス、許された作業、変更と保守の違いを言う。読者は一日のシートを残す。空欄は、まだ管理していない部分である。講習の復唱ではない。規格は標題だけである。",
        "keys": ["データセンター運用", "当直管理者", "作業手順", "変更と保守", "障害の時計", "業者許可", "容量を作らない"],
    },
    "id": {
        "rtl": False,
        "kdp": "Indonesian",
        "title": "Menjalankan Hari Pusat Data",
        "sub": "Yang harus ditandatangani manajer sebelum sif berakhir",
        "copy": "Terjemahan berbantuan AI dari edisi bahasa Inggris. Teks edisi Inggris dihasilkan dengan AI. Tulisan pada gambar juga dalam bahasa ini.",
        "note": "Ini bukan ringkasan kursus. CDFOM dan CDFOS adalah nama kursus.",
        "desc": "Hari pusat data tidak terkelola hanya karena ruangan tampak tenang. Panduan ini untuk manajer yang sedang bertugas. Ia mengatakan apa yang Anda miliki, siapa yang boleh menyentuh instalasi, layanan yang benar-benar Anda jual, pekerjaan yang diizinkan, dan beda perubahan dengan pemeliharaan. Pembaca pergi dengan satu lembar hari. Sel kosong adalah bagian hari yang belum dikelola. Ini bukan ulangan kursus. Standar adalah judul.",
        "keys": ["operasi pusat data", "manajer sif", "prosedur kerja", "perubahan dan rawat", "jam insiden", "izin vendor", "kapasitas tanpa tebakan"],
    },
    "ko": {
        "rtl": False,
        "kdp": "Korean",
        "title": "데이터센터의 하루를 돌리다",
        "sub": "교대가 끝나기 전에 관리자가 서명할 것",
        "copy": "영어판을 AI 보조로 번역했다. 영어판 본문은 AI가 생성했다. 그림 안의 글자도 이 언어이다.",
        "note": "이것은 강좌의 요약이 아니다. CDFOM과 CDFOS는 과정 이름이다.",
        "desc": "방이 고요하다고 데이터센터의 하루가 관리된 것은 아니다. 당직 관리자를 위한 현장 안내이다. 무엇을 소유하는지, 누가 설비를 만져도 되는지, 실제로 판 서비스, 허용된 작업, 변경과 보수의 차이를 말한다. 독자는 하루 시트를 남긴다. 빈 칸은 아직 관리하지 않은 부분이다. 강좌의 복창이 아니다. 규격은 제목뿐이다.",
        "keys": ["데이터센터 운영", "당직 관리자", "작업 절차", "변경과 보수", "장애 시계", "업체 허가", "용량을 만들지 말 것"],
    },
    "th": {
        "rtl": False,
        "kdp": "Thai",
        "title": "ดำเนินวันของศูนย์ข้อมูล",
        "sub": "สิ่งที่ผู้จัดการต้องลงนามก่อนจบกะ",
        "copy": "แปลจากฉบับภาษาอังกฤษโดยมี AI ช่วย ข้อความฉบับภาษาอังกฤษสร้างด้วย AI ตัวอักษรในรูปก็เป็นภาษานี้",
        "note": "นี่ไม่ใช่การสรุปหลักสูตร CDFOM และ CDFOS เป็นชื่อหลักสูตร",
        "desc": "วันของศูนย์ข้อมูลไม่ได้ถูกจัดการเพียงเพราะห้องดูสงบ คู่มือนี้สำหรับผู้จัดการที่เข้าเวร บอกว่าคุณเป็นเจ้าของอะไร ใครแตะโรงงานได้ บริการที่ขายจริง งานที่อนุญาต และความต่างระหว่างการเปลี่ยนแปลงกับการบำรุง ผู้อ่านเหลือแผ่นหนึ่งวัน ช่องว่างคือส่วนของวันที่ยังไม่ได้จัดการ นี่ไม่ใช่การทวนหลักสูตร มาตรฐานเป็นเพียงชื่อเรื่อง",
        "keys": ["ปฏิบัติการศูนย์ข้อมูล", "ผู้จัดการกะ", "ขั้นตอนงาน", "เปลี่ยนกับบำรุง", "นาฬิกาเหตุ", "ใบอนุญาตผู้รับเหมา", "ความจุที่ไม่เดา"],
    },
    "ar": {
        "rtl": True,
        "kdp": "Arabic",
        "title": "تشغيل يوم مركز البيانات",
        "sub": "ما يجب أن يوقّعه المدير قبل انتهاء الوردية",
        "copy": "ترجمة بمساعدة الذكاء الاصطناعي من الطبعة الإنجليزية. نص الطبعة الإنجليزية مولَّد بالذكاء الاصطناعي. الكتابة داخل الرسوم بهذه اللغة أيضًا.",
        "note": "هذا ليس ملخص دورة. CDFOM وCDFOS اسما دورتين.",
        "desc": "يوم مركز البيانات لا يُدار لأن القاعات بدت هادئة. هذا دليل لمدير المناوبة. يقول ما تملك، ومن يجوز له أن يلمس المحطة، والخدمة التي بعتها فعلًا، والعمل المسموح، وفرق التغيير عن الصيانة. يغادر القارئ بورقة يوم. الخانة الفارغة جزء من اليوم لم يُدر بعد. هذا ليس إعادة لدورة. المعايير عناوين.",
        "keys": ["تشغيل مركز البيانات", "مدير الوردية", "إجراء العمل", "التغيير والصيانة", "ساعة الحادث", "تصريح المورد", "سعة بلا تخمين"],
    },
}


def draw_cover(path, lang, title, subtitle):
    im = Image.new("RGB", (1600, 2560), (20, 22, 24))
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FONT, 28)
    ft = ImageFont.truetype(FONT, 52)
    fs = ImageFont.truetype(FONT, 32)
    d.rectangle((70, 160, 86, 2100), fill=(230, 162, 60))
    d.text((140, 200), f"05  /  {lang.upper()}", font=f, fill=(230, 162, 60))
    y = 400
    # char wrap
    cur = ""
    for ch in title:
        trial = cur + ch
        if d.textlength(trial, font=ft) <= 1280:
            cur = trial
        else:
            d.text((140, y), cur, font=ft, fill=(244, 241, 234))
            y += 72
            cur = ch
    if cur:
        d.text((140, y), cur, font=ft, fill=(244, 241, 234))
        y += 80
    cur = ""
    yy = y
    for ch in subtitle:
        trial = cur + ch
        if d.textlength(trial, font=fs) <= 1280:
            cur = trial
        else:
            d.text((140, yy), cur, font=fs, fill=(230, 162, 60))
            yy += 44
            cur = ch
    if cur:
        d.text((140, yy), cur, font=fs, fill=(230, 162, 60))
    d.text((140, 2280), "TRISTAN", font=f, fill=(230, 162, 60))
    d.text((140, 2340), "DATA CENTER FIELD GUIDES", font=ImageFont.truetype(FONT, 26), fill=(244, 241, 234))
    path.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(path, "JPEG", quality=92, optimize=True)


def xhtml(title, body, lang, rtl):
    direction = ' dir="rtl"' if rtl else ""
    return f"""<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang}" lang="{lang}"{direction}>
<head><meta charset="utf-8"/><title>{html.escape(title)}</title>
<link rel="stylesheet" type="text/css" href="styles.css"/></head>
<body>
{body}
</body></html>"""


def build(lang):
    meta = LANGS[lang]
    chapters = sorted((ROOT / "translations" / lang).glob("*.md"))
    if len(chapters) != 13:
        raise SystemExit(f"{lang} {len(chapters)}")
    items, images = [], []
    for path in chapters:
        blocks = md_to_blocks(path.read_text())
        title = next(t for k, t in blocks if k == "h1")
        body, figs = blocks_to_xhtml(blocks)
        images.extend(figs)
        items.append((f"chap-{len(items)+1:02d}.xhtml", title, body))
    cover = FIG / "covers" / f"{lang}.jpg"
    draw_cover(cover, lang, meta["title"], meta["sub"])
    rtl = meta["rtl"]
    nav_items = '<li><a href="copyright.xhtml">Copyright</a></li>\n' + "\n".join(
        f'<li><a href="{n}">{html.escape(t)}</a></li>' for n, t, _ in items
    )
    nav = xhtml("Contents", f'<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>{nav_items}</ol></nav>', lang, rtl)
    colophon = xhtml(
        "Copyright",
        f"""<section epub:type="copyright-page"><h1>{html.escape(meta["title"])}</h1>
<p>Tristan. Data Center Field Guides. 2026.</p>
<p>{html.escape(meta["copy"])}</p>
<p>{html.escape(meta["note"])}</p>
<p>6.99 USD. Not enrolled in an exclusive program.</p></section>""",
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
    used = []
    for name in sorted(set(images)):
        local = FIG / lang / name
        src = local if local.exists() else FIG / name
        if not src.exists():
            raise SystemExit(f"missing {src}")
        used.append((name, src))
        manifest.append(f'<item id="img-{name.replace(".", "-")}" href="images/{name}" media-type="image/png"/>')
    spine = ['<itemref idref="cover"/>', '<itemref idref="copyright"/>', '<itemref idref="nav"/>']
    for i, (name, _t, _) in enumerate(items, 1):
        manifest.append(f'<item id="c{i}" href="{name}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="c{i}"/>')
    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="uid" version="3.0" xml:lang="{lang}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:uuid:book-05-{lang}</dc:identifier>
<dc:title>{html.escape(meta["title"])}</dc:title>
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
</package>"""
    out = ROOT / "epub" / lang / f"{FILE}.{lang}.epub"
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()
    container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>"""

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
        for name, title, body in items:
            add(zf, f"OEBPS/{name}", xhtml(title, body, lang, rtl))
        zf.write(cover, "OEBPS/images/cover.jpg")
        for name, src in used:
            zf.write(src, f"OEBPS/images/{name}")
    pack = ROOT / "publish" / lang / "PACK.md"
    pack.parent.mkdir(parents=True, exist_ok=True)
    keys = "\n".join(f"{i}. {k}" for i, k in enumerate(meta["keys"], 1))
    pack.write_text(
        f"""# Upload pack

New Kindle eBook. Do not replace the English listing. Not KDP Select.

- EPUB: `books/05-run-the-day/epub/{lang}/{FILE}.{lang}.epub`
- Cover: `books/05-run-the-day/figures/covers/{lang}.jpg`
- Figures in this language: `books/05-run-the-day/figures/{lang}/`
- epubcheck: not run.

- Language: {meta["kdp"]}
- Title: {meta["title"]}
- Subtitle: {meta["sub"]}
- Author: Tristan
- Price: 6.99 USD

{meta["desc"]}

{meta["note"]}

## Keywords

{keys}

## AI

Text: AI-generated English, then AI-assisted translation. Figures: text translated. Translation: Yes. Tool: Grok.
""",
        encoding="utf-8",
    )
    print(lang, out.stat().st_size, "images", len(used))


if __name__ == "__main__":
    for lang in LANGS:
        over = [k for k in LANGS[lang]["keys"] if len(k) > 50]
        if over:
            raise SystemExit(over)
        build(lang)
