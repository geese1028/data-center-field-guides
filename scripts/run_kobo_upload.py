#!/usr/bin/env python3
"""
Dedicated Kobo Publisher Runner for Volume 2 English
"""

import time
import subprocess
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")

BOOK_DATA = {
    "title": "Read and Use Load Bank Data",
    "subtitle": "A Field Guide to Hydraulic Telemetry, Thermal Transients, and Refusal Signatures",
    "series": "Data Center Field Guides",
    "series_number": "2",
    "author": "Tristan",
    "publisher": "Data Center Field Guides",
    "imprint": "Data Center Field Guides",
    "language_code": "en",
    "language_name": "English",
    "price": "12.99",
    "cover_path": str(ROOT / "books" / "02-read-load-bank-data" / "figures" / "cover.jpg"),
    "epub_path": str(ROOT / "books" / "02-read-load-bank-data" / "epub" / "read-and-use-load-bank-data.epub"),
    "synopsis": (
        "A load-bank test is not valid because the curve looks calm. This field guide tells you how to turn a run into a flash report a stranger can audit.\n\n"
        "The report opens with five lines: pretest, gradient, overload, step change, and single-feed fault. Overall pass requires every line you attempted. Not run is not a pass. The book covers the preparation block, the pretest cells, consistency, how a plotted point is made from raw samples, the data block on every step, and the sentence you are allowed to write.\n\n"
        "It also covers the automatic charts, the hop from sensor to Modbus poll to MQTT message, and what an online hit from FLOC or Focus is allowed to mean. A hit is a time. CPOP waits until the file is closed. None of them write pass.\n\n"
        "Flow, temperature, and pressure limits stay on your sheet, cited to the document then in force. This book does not paste a datasheet, a register map, or a site record.\n\n"
        "Read the first book before this one if the prototype has not been accepted. The next book runs the load-bank test and leaves seven sheets. This one stops at the file."
    )
}

def run_js(js_code):
    escaped = js_code.replace('\\', '\\\\').replace('"', '\\"')
    apple_script = f'''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "writinglife.kobo.com/v2/ebooks/ebook" then
                    return execute t javascript "{escaped}"
                end if
            end repeat
        end repeat
    end tell
    '''
    res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
    return res.stdout.strip()

def activate_kobo_tab():
    script = '''
    tell application "Google Chrome"
        repeat with w in windows
            set tabList to tabs of w
            repeat with i from 1 to count of tabList
                if URL of (item i of tabList) contains "writinglife.kobo.com/v2/ebooks/ebook" then
                    set active tab index of w to i
                    set index of w to 1
                    activate
                    return "OK"
                end if
            end repeat
        end repeat
    end tell
    '''
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip()

def inject_metadata():
    print("[1/4] Injecting Book 2 metadata into Kobo form...")
    syn_escaped = BOOK_DATA['synopsis'].replace('`', '\\`')
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

        setReactVal(document.querySelector('[name="metadata.title"]'), "{BOOK_DATA['title']}");
        setReactVal(document.querySelector('[name="metadata.subtitle"]'), "{BOOK_DATA['subtitle']}");
        setReactVal(document.querySelector('[name="metadata.series"]'), "{BOOK_DATA['series']}");
        setReactVal(document.querySelector('[name="metadata.seriesNumber"]'), "{BOOK_DATA['series_number']}");
        setReactVal(document.querySelector('[name="metadata.contributors[0].name"]'), "{BOOK_DATA['author']}");
        setReactVal(document.querySelector('[name="metadata.publisher"]'), "{BOOK_DATA['publisher']}");
        setReactVal(document.querySelector('[name="metadata.imprint"]'), "{BOOK_DATA['imprint']}");

        // Language select
        var langSelect = document.querySelector('select[name="metadata.language"]');
        if (langSelect) {{
            langSelect.value = "{BOOK_DATA['language_code']}";
            langSelect.dispatchEvent(new Event("change", {{ bubbles: true }}));
        }}

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

        return "METADATA_INJECTED_SUCCESSFULLY";
    }})()
    '''
    res = run_js(js)
    print(f"[✓] Metadata injection result: {res}")

def upload_file_dialog(button_text, file_path):
    print(f"[+] Automating file upload for '{button_text}' -> {Path(file_path).name}...")
    activate_kobo_tab()
    time.sleep(0.8)

    click_js = f'''
    (function() {{
        var btn = Array.from(document.querySelectorAll("button")).find(b => b.textContent.trim().includes("{button_text}"));
        if (btn) {{
            btn.scrollIntoView();
            btn.click();
            return "CLICKED";
        }}
        return "NOT_FOUND";
    }})()
    '''
    res = run_js(click_js)
    print(f"    Button click status: {res}")
    time.sleep(1.5)

    applescript_upload = f'''
    tell application "System Events"
        tell process "Google Chrome"
            delay 0.5
            keystroke "g" using {{command down, shift down}}
            delay 1.0
            set the clipboard to "{file_path}"
            keystroke "v" using {{command down}}
            delay 0.8
            keystroke return
            delay 1.0
            keystroke return
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", applescript_upload])
    print(f"[✓] Submitted path to file chooser: {file_path}")
    time.sleep(3.0)

def main():
    activate_kobo_tab()
    inject_metadata()
    time.sleep(1.0)
    upload_file_dialog("Select image", BOOK_DATA["cover_path"])
    time.sleep(2.0)
    upload_file_dialog("Select file", BOOK_DATA["epub_path"])
    print("\n[✓] Volume 2 upload triggered! Monitoring page status...")

if __name__ == "__main__":
    main()
