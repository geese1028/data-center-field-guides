#!/usr/bin/env python3
"""
Generates KDP Auto-Filler Userscript and Local KDP Companion Launchpad.
"""

import json
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")
CATALOG_JSON = ROOT / "catalog" / "kdp_catalog.json"
USERSCRIPT_OUT = ROOT / "scripts" / "kdp_autofill.user.js"
LAUNCHPAD_OUT = ROOT / "scripts" / "kdp_companion.html"

def main():
    if not CATALOG_JSON.exists():
        print("[!] catalog/kdp_catalog.json not found. Run parse_kdp_fill.py first.")
        return

    data = json.loads(CATALOG_JSON.read_text(encoding="utf-8"))
    print(f"Loaded {len(data)} editions.")

    # 1. Generate Userscript (Tampermonkey / Violentmonkey)
    catalog_embedded_js = json.dumps(data, ensure_ascii=False)

    userscript_code = f"""// ==UserScript==
// @name         DCFG KDP 1-Click AutoFiller
// @namespace    https://datacenterfieldguides.com/
// @version      1.0
// @description  Automates KDP title setup, metadata, keywords, DRM, and pricing for Data Center Field Guides.
// @author       Tristan / DCFG Ops
// @match        https://kdp.amazon.com/*/title-setup/*
// @match        https://kdp.amazon.com/title-setup/*
// @match        https://kdp.amazon.com/*/bookshelf*
// @grant        GM_setClipboard
// @grant        GM_setValue
// @grant        GM_getValue
// ==/UserScript==

(function() {{
    'use strict';

    const CATALOG = {catalog_embedded_js};

    function createHUD() {{
        if (document.getElementById('dcfg-kdp-hud')) return;

        const hud = document.createElement('div');
        hud.id = 'dcfg-kdp-hud';
        hud.style.cssText = `
            position: fixed;
            top: 60px;
            right: 20px;
            z-index: 999999;
            background: #0f172a;
            color: #f8fafc;
            border: 2px solid #3b82f6;
            border-radius: 12px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
            padding: 14px 18px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 13px;
            width: 340px;
        `;

        let optionsHtml = CATALOG.map((b, idx) => `
            <option value="${{idx}}">${{b.book_label}} · ${{b.lang_label}} (${{b.language_dropdown}})</option>
        `).join('');

        hud.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; border-bottom:1px solid #334155; padding-bottom:8px;">
                <span style="font-weight:700; color:#60a5fa; font-size:14px;">⚡ DCFG KDP Auto-Pilot</span>
                <span style="font-size:11px; background:#1e293b; color:#94a3b8; padding:2px 6px; border-radius:4px;">${{CATALOG.length}} Editions</span>
            </div>
            
            <div style="margin-bottom:10px;">
                <label style="display:block; font-size:11px; color:#94a3b8; margin-bottom:4px; font-weight:600;">SELECT EDITION:</label>
                <select id="dcfg-book-select" style="width:100%; padding:6px; background:#1e293b; color:#f8fafc; border:1px solid #475569; border-radius:6px; font-size:12px;">
                    ${{optionsHtml}}
                </select>
            </div>

            <div id="dcfg-edition-summary" style="background:#1e293b; padding:8px 10px; border-radius:6px; font-size:11px; margin-bottom:12px; color:#cbd5e1; max-height:80px; overflow-y:auto; line-height:1.4;">
                <!-- dynamic summary -->
            </div>

            <div style="display:flex; flex-direction:column; gap:8px;">
                <button id="dcfg-btn-autofill" style="background:#2563eb; color:#fff; border:none; padding:8px 12px; border-radius:6px; font-weight:700; cursor:pointer; font-size:13px; transition:all 0.2s;">
                    ⚡ 1-Click AutoFill Current Tab
                </button>
                <div style="display:flex; gap:6px;">
                    <button id="dcfg-btn-copy-epub" style="flex:1; background:#334155; color:#cbd5e1; border:none; padding:6px; border-radius:4px; cursor:pointer; font-size:11px;">
                        📋 Copy EPUB Path
                    </button>
                    <button id="dcfg-btn-copy-cover" style="flex:1; background:#334155; color:#cbd5e1; border:none; padding:6px; border-radius:4px; cursor:pointer; font-size:11px;">
                        📋 Copy Cover Path
                    </button>
                </div>
            </div>

            <div id="dcfg-status-msg" style="margin-top:8px; font-size:11px; color:#10b981; min-height:16px; text-align:center;"></div>
        `;

        document.body.appendChild(hud);

        const select = hud.querySelector('#dcfg-book-select');
        const summary = hud.querySelector('#dcfg-edition-summary');
        const statusMsg = hud.querySelector('#dcfg-status-msg');

        function updateSummary() {{
            const cur = CATALOG[select.value];
            summary.innerHTML = `
                <strong style="color:#f8fafc;">${{cur.title || '(No Title)'}}</strong><br>
                <span style="color:#94a3b8;">${{cur.subtitle || ''}}</span><br>
                <span style="color:#38bdf8;">Keywords:</span> ${{cur.keywords.length}} items
            `;
        }}

        select.addEventListener('change', () => {{
            localStorage.setItem('dcfg_kdp_last_selected', select.value);
            updateSummary();
        }});

        const savedIdx = localStorage.getItem('dcfg_kdp_last_selected');
        if (savedIdx && CATALOG[savedIdx]) {{
            select.value = savedIdx;
        }}
        updateSummary();

        // Copy EPUB Path
        hud.querySelector('#dcfg-btn-copy-epub').addEventListener('click', () => {{
            const cur = CATALOG[select.value];
            navigator.clipboard.writeText(cur.manuscript_path).then(() => {{
                statusMsg.textContent = "✓ EPUB Path Copied! (In Mac dialog press Cmd+Shift+G)";
                setTimeout(() => statusMsg.textContent = "", 3000);
            }});
        }});

        // Copy Cover Path
        hud.querySelector('#dcfg-btn-copy-cover').addEventListener('click', () => {{
            const cur = CATALOG[select.value];
            navigator.clipboard.writeText(cur.cover_path).then(() => {{
                statusMsg.textContent = "✓ Cover Path Copied! (In Mac dialog press Cmd+Shift+G)";
                setTimeout(() => statusMsg.textContent = "", 3000);
            }});
        }});

        // AutoFill Button
        hud.querySelector('#dcfg-btn-autofill').addEventListener('click', () => {{
            const cur = CATALOG[select.value];
            runAutoFill(cur, statusMsg);
        }});
    }}

    function triggerEvent(el, eventType) {{
        el.dispatchEvent(new Event(eventType, {{ bubbles: true, cancelable: true }}));
    }}

    function setVal(selector, val) {{
        const el = document.querySelector(selector);
        if (el) {{
            el.value = val;
            triggerEvent(el, 'input');
            triggerEvent(el, 'change');
            return true;
        }}
        return false;
    }}

    function clickEl(selector) {{
        const el = document.querySelector(selector);
        if (el) {{
            el.click();
            triggerEvent(el, 'change');
            return true;
        }}
        return false;
    }}

    function runAutoFill(data, statusMsg) {{
        let filledCount = 0;
        const url = window.location.href;

        // 1. Language Dropdown
        const langSelect = document.querySelector('select[name*="language"], select#data-language, select[id*="language"]');
        if (langSelect) {{
            let targetLang = data.language_dropdown.toLowerCase();
            for (let opt of langSelect.options) {{
                if (opt.text.toLowerCase().includes(targetLang) || opt.value.toLowerCase().includes(targetLang)) {{
                    langSelect.value = opt.value;
                    triggerEvent(langSelect, 'change');
                    filledCount++;
                    break;
                }}
            }}
        }}

        // 2. Title & Subtitle
        if (setVal('input[name*="title"], input#data-title, input[id*="book-title"]', data.title)) filledCount++;
        if (data.subtitle && setVal('input[name*="subtitle"], input#data-subtitle', data.subtitle)) filledCount++;

        // 3. Edition Number
        if (setVal('input[name*="edition"], input#data-edition-number', '1')) filledCount++;

        // 4. Author Name
        if (setVal('input[name*="first_name"], input[name*="author.firstName"], input#data-author-first-name, input[id*="author-first"]', 'Tristan')) filledCount++;
        if (setVal('input[name*="last_name"], input[name*="author.lastName"], input#data-author-last-name, input[id*="author-last"]', '')) filledCount++;

        // 5. Description (Support Textarea & CKEditor/Contenteditable)
        const descTextarea = document.querySelector('textarea[name*="description"], textarea#data-description, textarea[id*="description"]');
        if (descTextarea) {{
            descTextarea.value = data.description;
            triggerEvent(descTextarea, 'input');
            triggerEvent(descTextarea, 'change');
            filledCount++;
        }}
        const richEditor = document.querySelector('.ck-editor__editable, [contenteditable="true"]');
        if (richEditor) {{
            richEditor.innerText = data.description;
            triggerEvent(richEditor, 'input');
            filledCount++;
        }}

        // 6. Publishing Rights (I own copyright)
        const rightsRadio = document.querySelector('input[name*="rights"][value*="copyright"], input[value="non-public-domain"], #data-rights-owner');
        if (rightsRadio) {{ rightsRadio.click(); triggerEvent(rightsRadio, 'change'); filledCount++; }}

        // 7. Adult Content (No)
        const adultNo = document.querySelector('input[name*="adult"][value="false"], input#data-adult-content-false, input[id*="adult-false"]');
        if (adultNo) {{ adultNo.click(); triggerEvent(adultNo, 'change'); filledCount++; }}

        // 8. Primary Marketplace
        const marketSelect = document.querySelector('select[name*="marketplace"], select#data-primary-marketplace');
        if (marketSelect) {{
            for (let opt of marketSelect.options) {{
                if (opt.value.includes('amazon.com') || opt.text.includes('Amazon.com')) {{
                    marketSelect.value = opt.value;
                    triggerEvent(marketSelect, 'change');
                    filledCount++;
                    break;
                }}
            }}
        }}

        // 9. 7 Keywords
        const kwInputs = document.querySelectorAll('input[id*="keyword"], input[name*="keyword"]');
        if (kwInputs && kwInputs.length >= 7) {{
            for (let i = 0; i < 7 && i < data.keywords.length; i++) {{
                kwInputs[i].value = data.keywords[i];
                triggerEvent(kwInputs[i], 'input');
                triggerEvent(kwInputs[i], 'change');
                filledCount++;
            }}
        }}

        // 10. AI Declaration (Yes + Grok)
        const aiYesRadio = document.querySelector('input[name*="ai"][value="true"], input[id*="ai-content-true"]');
        if (aiYesRadio) {{
            aiYesRadio.click();
            triggerEvent(aiYesRadio, 'change');
            filledCount++;
        }}

        // 11. Content Tab: DRM & Publisher
        const drmYes = document.querySelector('input[name*="drm"][value="true"], input#data-drm-true');
        if (drmYes) {{ drmYes.click(); triggerEvent(drmYes, 'change'); filledCount++; }}

        if (setVal('input[name*="publisher"], input#data-publisher, input[id*="publisher"]', 'Data Center Field Guides')) filledCount++;

        // 12. Pricing Tab: KDP Select, Royalty 70%, Price 12.99 USD
        const kdpSelectBox = document.querySelector('input[name*="kdp_select"], input#data-kdp-select');
        if (kdpSelectBox && kdpSelectBox.checked) {{
            kdpSelectBox.click();
            triggerEvent(kdpSelectBox, 'change');
            filledCount++;
        }}

        const worldwideRadio = document.querySelector('input[name*="territory"][value*="worldwide"], input#data-territories-worldwide');
        if (worldwideRadio) {{ worldwideRadio.click(); triggerEvent(worldwideRadio, 'change'); filledCount++; }}

        const royalty70 = document.querySelector('input[name*="royalty"][value="70"], input#data-royalty-70');
        if (royalty70) {{ royalty70.click(); triggerEvent(royalty70, 'change'); filledCount++; }}

        if (setVal('input[name*="price"], input#data-price-usd, input[id*="price-usd"]', '12.99')) filledCount++;

        statusMsg.textContent = `✓ Auto-filled ${{filledCount}} fields! Check & Save.`;
        setTimeout(() => statusMsg.textContent = "", 5000);
    }}

    // Check DOM ready
    window.addEventListener('load', () => {{
        setTimeout(createHUD, 1000);
    }});
    setTimeout(createHUD, 2000);
}})();
"""
    USERSCRIPT_OUT.write_text(userscript_code, encoding="utf-8")
    print(f"Generated Userscript at: {USERSCRIPT_OUT}")

    # 2. Generate Local HTML Companion Launchpad
    cards_html = []
    for idx, b in enumerate(data):
        kw_badges = "".join([f'<span style="background:#1e293b;border:1px solid #334155;color:#94a3b8;font-size:10px;padding:2px 6px;border-radius:4px;margin-right:4px;margin-bottom:4px;display:inline-block;">{kw}</span>' for kw in b["keywords"]])
        cards_html.append(f"""
        <div class="card" id="card-{idx}" style="background:#111827; border:1px solid #1f2937; border-radius:10px; padding:1.25rem; margin-bottom:1rem; transition:border 0.2s;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
                <div>
                    <span style="background:#2563eb; color:#fff; font-size:11px; font-weight:700; padding:2px 8px; border-radius:4px; text-transform:uppercase;">{b["book_label"]}</span>
                    <span style="color:#60a5fa; font-size:12px; font-weight:600; margin-left:0.5rem;">{b["lang_label"]} ({b["language_dropdown"]})</span>
                </div>
                <label style="color:#94a3b8; font-size:12px; cursor:pointer;">
                    <input type="checkbox" onchange="toggleDone({idx})" id="done-{idx}"> Submitted to KDP
                </label>
            </div>
            
            <div style="color:#f9fafb; font-size:1.15rem; font-weight:700; margin-bottom:0.25rem;">{b["title"]}</div>
            <div style="color:#9ca3af; font-size:0.9rem; margin-bottom:0.75rem;">{b["subtitle"]}</div>
            
            <div style="margin-bottom:0.75rem;">{kw_badges}</div>

            <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:0.75rem;">
                <button onclick="copyText(`{b['title']}`, 'Title Copied!')" class="btn">📋 Copy Title</button>
                <button onclick="copyText(`{b['subtitle']}`, 'Subtitle Copied!')" class="btn">📋 Copy Subtitle</button>
                <button onclick="copyDesc({idx})" class="btn">📋 Copy Description</button>
                <button onclick="copyKeywords({idx})" class="btn">📋 Copy 7 Keywords</button>
                <button onclick="copyText(`{b['manuscript_path']}`, 'EPUB Path Copied!')" class="btn btn-blue">📁 Copy EPUB Path</button>
                <button onclick="copyText(`{b['cover_path']}`, 'Cover Path Copied!')" class="btn btn-blue">🖼️ Copy Cover Path</button>
                <a href="https://kdp.amazon.com/en_US/title-setup/kdp/details?titleType=ebook" target="_blank" class="btn btn-green">🚀 Open KDP New eBook &rarr;</a>
            </div>
        </div>
        """)

    companion_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>DCFG KDP 1-Click Launchpad & Operations Hub</title>
    <style>
        body {{
            background: #090d16;
            color: #cbd5e1;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            max-width: 58rem;
            margin: 2rem auto;
            padding: 0 1.5rem 5rem;
        }}
        h1 {{ color: #fff; margin-bottom: 0.25rem; font-size: 1.8rem; }}
        .btn {{
            background: #1e293b;
            color: #cbd5e1;
            border: 1px solid #334155;
            padding: 0.45rem 0.8rem;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            transition: all 0.15s;
        }}
        .btn:hover {{ background: #334155; color: #fff; }}
        .btn-blue {{ background: #1d4ed8; border-color: #2563eb; color: #fff; }}
        .btn-blue:hover {{ background: #2563eb; }}
        .btn-green {{ background: #059669; border-color: #10b981; color: #fff; }}
        .btn-green:hover {{ background: #10b981; }}
        .card.done {{ opacity: 0.45; border-color: #059669; }}
        #toast {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: #10b981;
            color: #fff;
            padding: 0.75rem 1.25rem;
            border-radius: 8px;
            font-weight: 700;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.5);
            display: none;
            z-index: 1000;
        }}
    </style>
</head>
<body>
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:1.5rem; border-bottom:1px solid #1e293b; padding-bottom:1rem;">
        <div>
            <h1>DCFG KDP 1-Click Launchpad</h1>
            <p style="color:#94a3b8; margin:0.25rem 0 0; font-size:0.95rem;">
                All 22 editions indexed with 1-click clipboard payloads & file paths.
            </p>
        </div>
        <div style="text-align:right;">
            <div style="font-size:0.85rem; color:#94a3b8;">Completed: <span id="done-count" style="color:#10b981; font-weight:700;">0</span> / {len(data)}</div>
            <a href="file://{USERSCRIPT_OUT}" target="_blank" style="color:#38bdf8; font-size:0.8rem; text-decoration:none; display:inline-block; margin-top:4px;">⬇️ Install Tampermonkey Script</a>
        </div>
    </div>

    <!-- Quick instructions -->
    <div style="background:#0f172a; border:1px solid #2563eb; border-radius:8px; padding:1rem; margin-bottom:1.5rem; font-size:0.85rem; line-height:1.5;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <strong style="color:#60a5fa; font-size:1rem;">⚡ Kobo Writing Life 1-Click AutoFiller (0 手工填表)</strong>
            <a href="https://writinglife.kobo.com/ebook/create" target="_blank" class="btn btn-green">🚀 Open Kobo Create Page &rarr;</a>
        </div>
        <p style="color:#cbd5e1; margin:0 0 10px;">
            在 Kobo 页面按快捷键 <kbd style="background:#1e293b;padding:2px 5px;border-radius:4px;border:1px solid #475569;">Cmd + Option + J</kbd> 打开控制台，粘贴下方脚本回车，<strong>整页瞬间全自动填好</strong>！
        </p>
        <div style="display:flex; gap:8px;">
            <button onclick="copyKoboEn()" class="btn btn-blue">⚡ 复制 Kobo 第 1 本 (英文版) 填表脚本</button>
            <button onclick="copyKoboJa()" class="btn btn-blue">⚡ 复制 Kobo 第 1 本 (日语版) 填表脚本</button>
        </div>
    </div>

    <div id="cards-container">
        {"".join(cards_html)}
    </div>

    <textarea id="kobo-en-code" style="display:none;">{ROOT.joinpath("scripts/kobo_autofill_en.js").read_text(encoding="utf-8")}</textarea>
    <textarea id="kobo-ja-code" style="display:none;">{ROOT.joinpath("scripts/kobo_autofill_ja.js").read_text(encoding="utf-8")}</textarea>

    <div id="toast"></div>

    <script>
        const CATALOG = {catalog_embedded_js};

        function showToast(msg) {{
            const t = document.getElementById('toast');
            t.textContent = msg;
            t.style.display = 'block';
            setTimeout(() => {{ t.style.display = 'none'; }}, 2500);
        }}

        function copyText(txt, alertMsg) {{
            navigator.clipboard.writeText(txt).then(() => showToast(alertMsg || 'Copied!'));
        }}

        function copyDesc(idx) {{
            copyText(CATALOG[idx].description, 'Description Copied!');
        }}

        function copyKeywords(idx) {{
            copyText(CATALOG[idx].keywords.join('\\n'), 'All 7 Keywords Copied (1 per line)!');
        }}

        function copyKoboEn() {{
            const enCode = document.getElementById('kobo-en-code').value;
            copyText(enCode, 'Kobo 英文自动填表脚本已复制！在 Kobo 控制台粘贴回车即可！');
        }}

        function copyKoboJa() {{
            const jaCode = document.getElementById('kobo-ja-code').value;
            copyText(jaCode, 'Kobo 日语自动填表脚本已复制！在 Kobo 控制台粘贴回车即可！');
        }}

        function toggleDone(idx) {{
            const cb = document.getElementById(`done-${{idx}}`);
            const card = document.getElementById(`card-${{idx}}`);
            if (cb.checked) {{
                card.classList.add('done');
                localStorage.setItem(`kdp_done_${{idx}}`, '1');
            }} else {{
                card.classList.remove('done');
                localStorage.removeItem(`kdp_done_${{idx}}`);
            }}
            updateDoneCount();
        }}

        function updateDoneCount() {{
            let count = 0;
            for (let i = 0; i < CATALOG.length; i++) {{
                if (localStorage.getItem(`kdp_done_${{i}}`) === '1') {{
                    count++;
                    const cb = document.getElementById(`done-${{i}}`);
                    const card = document.getElementById(`card-${{i}}`);
                    if (cb) cb.checked = true;
                    if (card) card.classList.add('done');
                }}
            }}
            document.getElementById('done-count').textContent = count;
        }}

        updateDoneCount();
    </script>
</body>
</html>
"""
    LAUNCHPAD_OUT.write_text(companion_html, encoding="utf-8")
    print(f"Generated Companion Launchpad at: {LAUNCHPAD_OUT}")

if __name__ == "__main__":
    main()
