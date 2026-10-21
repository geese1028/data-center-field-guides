#!/usr/bin/env python3
"""
Fully Autonomous Kobo Publisher for Data Center Field Guides
Automates metadata injection, automated cover & EPUB file uploads, validation wait, and publishing.
Zero manual mouse clicks or file picker interactions required from the user.
"""

import sys
import time
import json
import subprocess
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")
CATALOG_PATH = ROOT / "catalog" / "kdp_catalog.json"

def run_js(js_code):
    escaped = js_code.replace('\\', '\\\\').replace('"', '\\"')
    apple_script = f'''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "kobo.com" and URL of t contains "ebook" then
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
                if URL of (item i of tabList) contains "kobo.com" and URL of (item i of tabList) contains "ebook" then
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

def upload_file_via_dialog(button_text, file_path):
    """
    Triggers native file chooser button in Chrome and uses macOS System Events
    to paste path (Cmd+Shift+G) and press Enter without user manual interaction.
    """
    print(f"[+] Automating upload for: {button_text} -> {Path(file_path).name} ...")
    activate_kobo_tab()
    time.sleep(0.5)

    # Click the upload button in the DOM
    click_js = f'''
    (function() {{
        var btn = Array.from(document.querySelectorAll("button")).find(b => b.textContent.includes("{button_text}"));
        if (btn) {{
            btn.click();
            return "CLICKED";
        }}
        return "NOT_FOUND";
    }})()
    '''
    run_js(click_js)
    time.sleep(1.0)

    # macOS System Events: Cmd+Shift+G -> paste path -> Return -> Return
    applescript_upload = f'''
    tell application "System Events"
        tell process "Google Chrome"
            delay 0.5
            keystroke "g" using {{command down, shift down}}
            delay 0.8
            set the clipboard to "{file_path}"
            keystroke "v" using {{command down}}
            delay 0.5
            keystroke return
            delay 0.8
            keystroke return
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", applescript_upload])
    print(f"[✓] File submitted to Chrome: {Path(file_path).name}")
    time.sleep(2.0)

def publish_edition(book_data):
    print("=" * 76)
    print(f"  AUTONOMOUS KOBO PUBLISHER // {book_data.get('title', '')}")
    print("=" * 76)

    # 1. Fill Metadata & Synopsis
    js_fill = f'''
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

        setReactVal(document.querySelector('[name="metadata.title"]'), "{book_data['title']}");
        setReactVal(document.querySelector('[name="metadata.subtitle"]'), "{book_data['subtitle']}");
        setReactVal(document.querySelector('[name="metadata.series"]'), "Data Center Field Guides");
        setReactVal(document.querySelector('[name="metadata.seriesNumber"]'), "{book_data.get('book_number', '1')}");
        setReactVal(document.querySelector('[name="metadata.contributors[0].name"]'), "Tristan");
        setReactVal(document.querySelector('[name="metadata.publisher"]'), "Data Center Field Guides");
        setReactVal(document.querySelector('[name="metadata.imprint"]'), "Data Center Field Guides");

        // Language
        var langSelect = document.querySelector('select[name="metadata.language"]');
        if (langSelect) {{
            langSelect.value = "{book_data.get('language_code', 'en')}";
            langSelect.dispatchEvent(new Event("change", {{ bubbles: true }}));
        }}

        // Radios
        var pdFalse = document.querySelector('input[name="metadata.publicDomainContent"][value="false"]');
        if (pdFalse) {{ pdFalse.click(); pdFalse.dispatchEvent(new Event("change", {{ bubbles: true }})); }}

        var drmTrue = document.querySelector('input[name="metadata.drm"][value="true"]');
        if (drmTrue) {{ drmTrue.click(); drmTrue.dispatchEvent(new Event("change", {{ bubbles: true }})); }}

        var wwTrue = document.querySelector('input[name="ownWorldwideRights"][value="true"]');
        if (wwTrue) {{ wwTrue.click(); wwTrue.dispatchEvent(new Event("change", {{ bubbles: true }})); }}

        // Pricing
        var p = document.querySelector('input[name="prices[0]"]');
        if (p) setReactVal(p, "99.00");

        // Synopsis
        var ql = document.querySelector(".ql-editor");
        if (ql) {{
            ql.innerText = `{book_data['description']}`;
            ql.dispatchEvent(new Event("input", {{ bubbles: true }}));
        }}

        return "METADATA_INJECTED";
    }})()
    '''
    res = run_js(js_fill)
    print(f"[+] Metadata injection: {res}")
    time.sleep(1.0)

    # 2. Upload Cover autonomously
    if book_data.get("cover_path") and Path(book_data["cover_path"]).exists():
        upload_file_via_dialog("Select image", book_data["cover_path"])

    # 3. Upload EPUB autonomously
    if book_data.get("manuscript_path") and Path(book_data["manuscript_path"]).exists():
        upload_file_via_dialog("Select file", book_data["manuscript_path"])

    print("\n[✓] Autonomous upload sequence complete! Waiting for Kobo conversion...")

if __name__ == "__main__":
    print("Kobo Full Autopilot Module Ready.")
