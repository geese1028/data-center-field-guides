#!/usr/bin/env python3
"""
Generates Kobo Writing Life 1-Click AutoFiller (Console Snippet & Bookmarklet).
"""

import json
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")

BOOK_1_EN = {
    "title": "Design and Build a Liquid Load Bank for NVL72 Racks",
    "subtitle": "A Field Guide to Interface Boundaries, P&ID Hydraulics, Thermal Envelopes, and Prototype Acceptance",
    "series": "Data Center Field Guides",
    "series_number": "1",
    "author": "Tristan",
    "publisher": "Data Center Field Guides",
    "imprint": "Data Center Field Guides",
    "language": "English",
    "price": "12.99",
    "epub": "/Users/geese/Downloads/book/books/01-liquid-load-bank/epub/design-and-build-a-liquid-load-bank.epub",
    "cover": "/Users/geese/Downloads/book/books/01-liquid-load-bank/figures/cover.jpg",
    "synopsis": """A liquid load bank replaces the rack-side thermal load and liquid conditions of NVL72-class AI hardware. It is not a CDU, and not a fabrication drawing.

This field guide states what to write before metal is cut, and which engineering gates must pass before a prototype can be called complete. The reader leaves with two clean handover documents: the liquid load bank requirement sheet and the prototype acceptance sheet. Flow, temperature, pressure, and coupling numbers remain blank until cited against the vendor specification then in force.

Key engineering coverage:
- Manifold and quick-disconnect (QDC) interface boundaries
- Flow rate vs. differential pressure (ΔP) hydraulic curves
- Step-load thermal rejection and CDU hunting prevention
- Non-negotiable field verification and refuse-to-sign gates"""
}

BOOK_1_JA = {
    "title": "NVL72級ラック向け液冷負荷装置を設計し、作る",
    "subtitle": "要求シートと試作の合格判定",
    "series": "Data Center Field Guides",
    "series_number": "1",
    "author": "Tristan",
    "publisher": "Data Center Field Guides",
    "imprint": "Data Center Field Guides",
    "language": "Japanese",
    "price": "12.99",
    "epub": "/Users/geese/Downloads/book/books/01-liquid-load-bank/epub/ja/design-and-build-a-liquid-load-bank.ja.epub",
    "cover": "/Users/geese/Downloads/book/books/01-liquid-load-bank/figures/covers/ja.jpg",
    "synopsis": """液冷負荷装置は、NVL72級ラックの代わりになる試験器である。冷却器でも図面でもない。この現場手引は、金属を切る前に何を書き、試作を完成と呼ぶ前にどの門を通すかを示す。残るのは、見知らぬ人に渡せる二つの文書である。要求シートと、試作の受入シート。流量、温度、圧力、継手の数値は、その時点で有効な仕様を引用するまで空欄のままである。"""
}

def generate_js(book_data):
    b_json = json.dumps(book_data, ensure_ascii=False)
    return f"""// == Kobo Writing Life 1-Click AutoFiller ==
// Usage: Open Chrome DevTools Console (Cmd+Option+J) on writinglife.kobo.com, paste this and press Enter!
(function() {{
    const b = {b_json};
    console.log('[+] Starting Kobo 1-Click AutoFill for:', b.title);

    function trigger(el) {{
        el.dispatchEvent(new Event('input', {{ bubbles: true }}));
        el.dispatchEvent(new Event('change', {{ bubbles: true }}));
        el.dispatchEvent(new Event('blur', {{ bubbles: true }}));
    }}

    function setVal(selectors, val) {{
        for (let sel of selectors) {{
            const el = document.querySelector(sel);
            if (el) {{
                el.focus();
                el.value = val;
                trigger(el);
                console.log('  [✓] Set', sel);
                return true;
            }}
        }}
        return false;
    }}

    // 1. Title & Subtitle
    setVal(['input[name*="Title"]', 'input[id*="title"]', '#eBookTitle', '#Title', 'input[placeholder*="Title"]'], b.title);
    setVal(['input[name*="Subtitle"]', 'input[id*="subtitle"]', '#eBookSubtitle', '#Subtitle', 'input[placeholder*="Subtitle"]'], b.subtitle);

    // 2. Series
    setVal(['input[name*="Series"]', 'input[id*="series"]', '#SeriesName', 'input[placeholder*="Series"]'], b.series);
    setVal(['input[name*="SeriesNumber"]', 'input[id*="seriesNumber"]', '#SeriesNumber', 'input[placeholder*="Number"]'], b.series_number);

    // 3. Author / Contributor
    setVal(['input[name*="Contributor"]', 'input[name*="Author"]', 'input[id*="contributor"]', 'input[id*="author"]', 'input[placeholder*="Author"]'], b.author);

    // 4. Publisher & Imprint
    setVal(['input[name*="Publisher"]', 'input[id*="publisher"]', '#PublisherName', 'input[placeholder*="Publisher"]'], b.publisher);
    setVal(['input[name*="Imprint"]', 'input[id*="imprint"]', '#ImprintName', 'input[placeholder*="Imprint"]'], b.imprint);

    // 5. Language
    const langSelect = document.querySelector('select[name*="Language"], select[id*="language"], #Language');
    if (langSelect) {{
        for (let opt of langSelect.options) {{
            if (opt.text.toLowerCase().includes(b.language.toLowerCase()) || opt.value.toLowerCase().includes(b.language.toLowerCase())) {{
                langSelect.value = opt.value;
                trigger(langSelect);
                console.log('  [✓] Set Language to', opt.text);
                break;
            }}
        }}
    }}

    // 6. Synopsis (Textarea or Rich Editor)
    const synTextarea = document.querySelector('textarea[name*="Synopsis"], textarea[id*="synopsis"], textarea[name*="description"], #Synopsis');
    if (synTextarea) {{
        synTextarea.value = b.synopsis;
        trigger(synTextarea);
        console.log('  [✓] Set Synopsis textarea');
    }}
    const richEditor = document.querySelector('.ck-editor__editable, [contenteditable="true"]');
    if (richEditor) {{
        richEditor.innerText = b.synopsis;
        trigger(richEditor);
        console.log('  [✓] Set Synopsis rich editor');
    }}

    // 7. Pricing & DRM (If on Pricing step)
    setVal(['input[name*="Price"]', 'input[id*="price"]', '#Price', 'input[placeholder*="0.00"]'], b.price);
    
    // Checkboxes / Radios
    const drmRadio = document.querySelector('input[name*="drm"][value*="true"], input[id*="drm-yes"]');
    if (drmRadio) {{ drmRadio.click(); trigger(drmRadio); }}
    
    const koboPlus = document.querySelector('input[name*="koboPlus"], input[id*="koboPlus"]');
    if (koboPlus && !koboPlus.checked) {{ koboPlus.click(); trigger(koboPlus); }}

    // Notification toast
    const toast = document.createElement('div');
    toast.style.cssText = 'position:fixed;top:20px;right:20px;background:#10b981;color:#fff;padding:12px 20px;border-radius:8px;font-weight:bold;z-index:999999;box-shadow:0 10px 25px rgba(0,0,0,0.4);font-family:sans-serif;';
    toast.innerHTML = '⚡ Kobo AutoFill Complete!<br><span style="font-size:12px;font-weight:normal;">EPUB: ' + b.epub.split('/').pop() + '</span>';
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 6000);
}})();
"""

def main():
    en_js = generate_js(BOOK_1_EN)
    ja_js = generate_js(BOOK_1_JA)

    (ROOT / "scripts" / "kobo_autofill_en.js").write_text(en_js, encoding="utf-8")
    (ROOT / "scripts" / "kobo_autofill_ja.js").write_text(ja_js, encoding="utf-8")
    print("[✓] Generated kobo_autofill_en.js and kobo_autofill_ja.js")

if __name__ == "__main__":
    main()
