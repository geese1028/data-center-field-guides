#!/usr/bin/env python3
"""
Autonomous Kobo Publishing Script for Volume 3 English
Finish a Liquid Cooling Verification: Seven Sheets for One Load-Bank Test
"""

import base64
import time
import subprocess
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")
EPUB_PATH = ROOT / "books" / "03-run-one-test" / "epub" / "finish-a-liquid-cooling-verification.epub"
COVER_PATH = ROOT / "books" / "03-run-one-test" / "figures" / "cover.jpg"

METADATA = {
    "title": "Finish a Liquid Cooling Verification",
    "subtitle": "Seven Sheets for One Load-Bank Test",
    "series": "Data Center Field Guides",
    "series_number": "3",
    "author": "Tristan",
    "publisher": "Data Center Field Guides",
    "imprint": "Data Center Field Guides",
    "language_code": "en",
    "synopsis": (
        "A load-bank test is not finished because the afternoon was hot. This field guide tells you how to connect an accepted load bank in place of the rack, run the approved scripts, and leave with sheets a stranger can audit.\n\n"
        "Seven sheets: before connect, alarms, one heat step, failures, shutdown, the no-heat pump curve if the script asks for it, and CDU logic. A blank cell is a stop. A number copied from the last hall is not a citation. Certificate Level 1 is factory testing. A static walk-through does not belong in that slot.\n\n"
        "Flow, temperature, and pressure limits stay on the script, cited to the specification then in force. This book does not paste a datasheet, a point list, or a site record.\n\n"
        "Read the first book if the load bank has not been accepted. Read the second if you cannot yet judge the file. This one runs the project."
    )
}

def run_js(js_code):
    escaped = js_code.replace('\\', '\\\\').replace('"', '\\"')
    script = f'''tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "writinglife.kobo.com/v2/ebooks/ebook" then
                    return execute t javascript "{escaped}"
                end if
            end repeat
        end repeat
    end tell'''
    res = subprocess.run(["osascript", "-"], input=script, capture_output=True, text=True)
    return res.stdout.strip()

def activate_kobo_tab():
    script = '''tell application "Google Chrome"
        repeat with w in windows
            repeat with i from 1 to count of tabs of w
                if URL of (tab i of w) contains "writinglife.kobo.com/v2/ebooks/ebook" then
                    set active tab index of w to i
                    set index of w to 1
                    activate
                    return "OK"
                end if
            end repeat
        end repeat
    end tell'''
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip()

def step1_inject_metadata():
    print("[1/5] Injecting Volume 3 metadata & selecting English language...")
    syn_escaped = METADATA['synopsis'].replace('`', '\\`')
    js = f'''
    (function() {{
        function setReactVal(el, val) {{
            if (!el) return false;
            var proto = el instanceof HTMLTextAreaElement ? window.HTMLTextAreaElement.prototype : window.HTMLInputElement.prototype;
            var setter = Object.getOwnPropertyDescriptor(proto, "value").set;
            setter.call(el, val);
            el.dispatchEvent(new Event("input", {{ bubbles: true }}));
            el.dispatchEvent(new Event("change", {{ bubbles: true }}));
            el.dispatchEvent(new Event("blur", {{ bubbles: true }}));
            return true;
        }}

        setReactVal(document.querySelector('[name="metadata.title"]'), "{METADATA['title']}");
        setReactVal(document.querySelector('[name="metadata.subtitle"]'), "{METADATA['subtitle']}");
        setReactVal(document.querySelector('[name="metadata.series"]'), "{METADATA['series']}");
        setReactVal(document.querySelector('[name="metadata.seriesNumber"]'), "{METADATA['series_number']}");
        setReactVal(document.querySelector('[name="metadata.contributors[0].name"]'), "{METADATA['author']}");
        setReactVal(document.querySelector('[name="metadata.publisher"]'), "{METADATA['publisher']}");
        setReactVal(document.querySelector('[name="metadata.imprint"]'), "{METADATA['imprint']}");

        // Public Domain = False
        var pdFalse = document.querySelector('input[name="metadata.publicDomainContent"][value="false"]');
        if (pdFalse) {{ pdFalse.click(); pdFalse.dispatchEvent(new Event("change", {{ bubbles: true }})); }}

        // DRM = True
        var drmTrue = document.querySelector('input[name="metadata.drm"][value="true"]');
        if (drmTrue) {{ drmTrue.click(); drmTrue.dispatchEvent(new Event("change", {{ bubbles: true }})); }}

        // Worldwide rights = True
        var wwTrue = document.querySelector('input[name="ownWorldwideRights"][value="true"]');
        if (wwTrue) {{ wwTrue.click(); wwTrue.dispatchEvent(new Event("change", {{ bubbles: true }})); }}

        // Synopsis Quill Editor
        var ql = document.querySelector(".ql-editor");
        if (ql) {{
            ql.innerText = `{syn_escaped}`;
            ql.dispatchEvent(new Event("input", {{ bubbles: true }}));
        }}

        // Language Dropdown selection via button
        var langBtn = Array.from(document.querySelectorAll("button")).find(b => b.innerText.includes("Select a language"));
        if (langBtn) {{
            langBtn.click();
            setTimeout(() => {{
                var opt = Array.from(document.querySelectorAll("[role=option]")).find(el => el.innerText.trim() === "English");
                if (opt) opt.click();
            }}, 300);
        }}

        return "METADATA_DONE";
    }})()
    '''
    res = run_js(js)
    print("  Result:", res)
    time.sleep(1.5)

def step2_inject_cover():
    print(f"[2/5] Injecting Cover: {COVER_PATH.name} ({COVER_PATH.stat().st_size} bytes)...")
    b64 = base64.b64encode(COVER_PATH.read_bytes()).decode('ascii')
    js = f'''
    (function() {{
        try {{
            var binStr = atob("{b64}");
            var len = binStr.length;
            var bytes = new Uint8Array(len);
            for (var i = 0; i < len; i++) bytes[i] = binStr.charCodeAt(i);
            var blob = new Blob([bytes], {{ type: "image/jpeg" }});
            var file = new File([blob], "cover.jpg", {{ type: "image/jpeg" }});
            
            var fileInputs = document.querySelectorAll("input[type=file]");
            var coverInput = fileInputs[0];
            var dt = new DataTransfer();
            dt.items.add(file);
            coverInput.files = dt.files;
            
            coverInput.dispatchEvent(new Event("input", {{ bubbles: true }}));
            coverInput.dispatchEvent(new Event("change", {{ bubbles: true }}));
            
            var dropzone = coverInput.parentElement;
            var dropEvent = new DragEvent("drop", {{ bubbles: true, cancelable: true, dataTransfer: dt }});
            dropzone.dispatchEvent(dropEvent);
            return "COVER_DISPATCHED";
        }} catch(e) {{
            return "ERROR: " + e.message;
        }}
    }})()
    '''
    res = run_js(js)
    print("  Result:", res)
    time.sleep(2.0)

def step3_inject_epub():
    print(f"[3/5] Injecting EPUB: {EPUB_PATH.name} ({EPUB_PATH.stat().st_size} bytes)...")
    b64 = base64.b64encode(EPUB_PATH.read_bytes()).decode('ascii')
    total_len = len(b64)
    chunk_size = 400000
    num_chunks = (total_len + chunk_size - 1) // chunk_size

    run_js("window.__epub_chunks = [];")
    for i in range(num_chunks):
        chunk = b64[i*chunk_size : (i+1)*chunk_size]
        run_js(f'window.__epub_chunks.push("{chunk}");')
        time.sleep(0.1)

    dispatch_js = '''
    (function() {
        try {
            var fullB64 = window.__epub_chunks.join("");
            var binStr = atob(fullB64);
            var len = binStr.length;
            var bytes = new Uint8Array(len);
            for (var i = 0; i < len; i++) bytes[i] = binStr.charCodeAt(i);
            var blob = new Blob([bytes], { type: "application/epub+zip" });
            var file = new File([blob], "finish-a-liquid-cooling-verification.epub", { type: "application/epub+zip" });
            
            var fileInputs = document.querySelectorAll("input[type=file]");
            var epubInput = fileInputs[1];
            var dt = new DataTransfer();
            dt.items.add(file);
            epubInput.files = dt.files;
            
            epubInput.dispatchEvent(new Event("input", { bubbles: true }));
            epubInput.dispatchEvent(new Event("change", { bubbles: true }));
            
            window.__epub_chunks = null;
            return "EPUB_DISPATCHED";
        } catch(e) {
            return "ERROR: " + e.message;
        }
    })()
    '''
    res = run_js(dispatch_js)
    print("  Result:", res)
    time.sleep(3.0)

def step4_categories_and_price():
    print("[4/5] Setting categories & pricing...")
    js = '''
    (function() {
        // Expand Nonfiction
        var nf = Array.from(document.querySelectorAll("li[role=treeitem]")).find(li => li.innerText.startsWith("Nonfiction"));
        if (nf) {
            var hit = nf.querySelector(".list-item-hit");
            if (hit) hit.click();
        }
        
        setTimeout(() => {
            // Select Hardware
            var cbHardware = Array.from(document.querySelectorAll("[type=checkbox]")).find(cb => {
                var p = cb.closest("li");
                return p && p.innerText.trim().startsWith("Hardware");
            });
            if (cbHardware && !cbHardware.checked) {
                cbHardware.click();
                cbHardware.dispatchEvent(new Event("change", { bubbles: true }));
            }
            
            // Select Computer Engineering
            var cbEng = Array.from(document.querySelectorAll("[type=checkbox]")).find(cb => {
                var p = cb.closest("li");
                return p && p.innerText.trim().startsWith("Computer Engineering");
            });
            if (cbEng && !cbEng.checked) {
                cbEng.click();
                cbEng.dispatchEvent(new Event("change", { bubbles: true }));
            }
            
            // Set base price HK$99.00
            var p = document.querySelector('[name="prices[0]"]');
            if (p) {
                var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
                setter.call(p, "99.00");
                p.dispatchEvent(new Event("input", { bubbles: true }));
                p.dispatchEvent(new Event("change", { bubbles: true }));
                p.dispatchEvent(new Event("blur", { bubbles: true }));
            }
            
            // Click Add all currencies
            var addAllBtn = Array.from(document.querySelectorAll("button")).find(b => b.innerText.includes("Add all currencies"));
            if (addAllBtn) addAllBtn.click();
        }, 500);

        return "CAT_PRICE_SCHEDULED";
    })()
    '''
    res = run_js(js)
    print("  Result:", res)
    time.sleep(2.5)

def main():
    activate_kobo_tab()
    step1_inject_metadata()
    step2_inject_cover()
    step3_inject_epub()
    step4_categories_and_price()
    print("\n[✓] Ingestion sequence dispatched. Waiting for conversion...")

if __name__ == "__main__":
    main()
