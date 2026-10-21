#!/usr/bin/env python3
"""
Fully Autonomous Apple Books Publisher for Data Center Field Guides
Automates Step 1 (EPUB & Cover), Step 2 (Title & Description), Step 3 (Category & Language), and Step 4 (Publishing Details).
"""

import sys
import time
import base64
import subprocess
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")
EPUB_PATH = ROOT / "books" / "01-liquid-load-bank" / "epub" / "design-and-build-a-liquid-load-bank.epub"
COVER_PATH = ROOT / "books" / "01-liquid-load-bank" / "figures" / "cover.jpg"

def run_js(js_code):
    escaped = js_code.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
    script = f'''tell application "Google Chrome"
        repeat with w in windows
            repeat with i from 1 to count of tabs of w
                if URL of (tab i of w) contains "authors.apple.com" then
                    return execute (tab i of w) javascript "{escaped}"
                end if
            end repeat
        end repeat
    end tell'''
    res = subprocess.run(["osascript", "-"], input=script, capture_output=True, text=True)
    return res.stdout.strip()

def activate_apple_tab():
    script = '''tell application "Google Chrome"
        activate
        repeat with w in windows
            repeat with i from 1 to count of tabs of w
                if URL of (tab i of w) contains "authors.apple.com" then
                    set active tab index of w to i
                    set index of w to 1
                    return "OK"
                end if
            end repeat
        end repeat
    end tell'''
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip()

def main():
    print("=" * 70)
    print("  AUTONOMOUS APPLE BOOKS PUBLISHER // VOL 1")
    print("=" * 70)
    
    activate_apple_tab()
    time.sleep(0.5)

    # 1. Reset / Navigate clean to epub-upload start
    print("[1/5] Navigating to clean start...")
    nav_script = '''tell application "Google Chrome"
        repeat with w in windows
            repeat with i from 1 to count of tabs of w
                if URL of (tab i of w) contains "authors.apple.com" then
                    set URL of (tab i of w) to "https://authors.apple.com/epub-upload/start#new-upload"
                    return "NAVIGATED"
                end if
            end repeat
        end repeat
    end tell'''
    subprocess.run(["osascript", "-e", nav_script])
    time.sleep(4.0)

    # Click Submit a New Book -> Continue
    init_js = """
    (function() {
        var newBookBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Submit a New Book'));
        if (newBookBtn) newBookBtn.click();
        var contBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Continue'));
        if (contBtn && !contBtn.disabled) {
            contBtn.click();
            return "STARTED_NEW_BOOK";
        }
        return "WAITING_INIT";
    })()
    """
    res = run_js(init_js)
    print("  Init result:", res)
    time.sleep(3.0)

    # 2. Step 1: Upload EPUB & Cover
    print("[2/5] Step 1: Uploading EPUB & Cover via DataTransfer...")
    with open(EPUB_PATH, "rb") as f:
        epub_b64 = base64.b64encode(f.read()).decode("ascii")
    with open(COVER_PATH, "rb") as f:
        cover_b64 = base64.b64encode(f.read()).decode("ascii")

    upload_js = f"""
    (function() {{
        function b64ToUint8Array(b64) {{
            var bin = atob(b64);
            var len = bin.length;
            var bytes = new Uint8Array(len);
            for (var i = 0; i < len; i++) {{
                bytes[i] = bin.charCodeAt(i);
            }}
            return bytes;
        }}

        // EPUB
        var epubBytes = b64ToUint8Array("{epub_b64}");
        var epubBlob = new Blob([epubBytes], {{ type: 'application/epub+zip' }});
        var epubFile = new File([epubBlob], '{EPUB_PATH.name}', {{ type: 'application/epub+zip' }});
        var dtEpub = new DataTransfer();
        dtEpub.items.add(epubFile);
        var epubInp = document.getElementById('epub-upload-input');
        if (epubInp) {{
            epubInp.files = dtEpub.files;
            epubInp.dispatchEvent(new Event('input', {{ bubbles: true }}));
            epubInp.dispatchEvent(new Event('change', {{ bubbles: true }}));
        }}

        // Cover
        var coverBytes = b64ToUint8Array("{cover_b64}");
        var coverBlob = new Blob([coverBytes], {{ type: 'image/jpeg' }});
        var coverFile = new File([coverBlob], '{COVER_PATH.name}', {{ type: 'image/jpeg' }});
        var dtCover = new DataTransfer();
        dtCover.items.add(coverFile);
        var coverInp = document.getElementById('cover-image-upload-input');
        if (coverInp) {{
            coverInp.files = dtCover.files;
            coverInp.dispatchEvent(new Event('input', {{ bubbles: true }}));
            coverInp.dispatchEvent(new Event('change', {{ bubbles: true }}));
        }}

        var contBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Continue'));
        if (contBtn && !contBtn.disabled) {{
            contBtn.click();
            return "STEP1_SUBMITTED";
        }}
        return "STEP1_WAIT_BUTTON";
    }})()
    """
    res = run_js(upload_js)
    print("  Step 1 upload result:", res)
    time.sleep(4.0)

    # 3. Step 2: Title, Description, Metadata
    print("[3/5] Step 2: Injecting Title, Subtitle, Author, Series & Synopsis...")
    step2_js = """
    (function() {
        function setVal(el, val) {
            if (!el) return false;
            var proto = el instanceof HTMLTextAreaElement ? window.HTMLTextAreaElement.prototype : window.HTMLInputElement.prototype;
            var setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
            if (setter) setter.call(el, val); else el.value = val;
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
            el.dispatchEvent(new Event('blur', { bubbles: true }));
            return true;
        }

        setVal(document.querySelector('input[placeholder="Title*"]'), "Design and Build a Liquid Load Bank for NVL72 Racks");
        setVal(document.querySelector('input[placeholder="Subtitle"]'), "A Field Guide to Interface Boundaries, P&ID Hydraulics, Thermal Envelopes, and Prototype Acceptance");
        setVal(document.querySelector('input[placeholder="Series name"]'), "Data Center Field Guides");
        setVal(document.querySelector('input[placeholder="Series number"]'), "1");
        setVal(document.querySelector('input[placeholder="First and last name*"]'), "Tristan");
        
        var desc = `A liquid load bank replaces the rack-side thermal load and liquid conditions of NVL72-class AI hardware. It is not a CDU, and not a fabrication drawing.

This field guide states what to write before metal is cut, and which engineering gates must pass before a prototype can be called complete. The reader leaves with two clean handover documents: the liquid load bank requirement sheet and the prototype acceptance sheet. Flow, temperature, pressure, and coupling numbers remain blank until cited against the vendor specification then in force.

Key engineering coverage:
- Manifold and quick-disconnect (QDC) interface boundaries
- Flow rate vs. differential pressure (ΔP) hydraulic curves
- Step-load thermal rejection and CDU hunting prevention
- Non-negotiable field verification and refuse-to-sign gates`;

        setVal(document.querySelector('textarea'), desc);

        var contBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Continue'));
        if (contBtn && !contBtn.disabled) {
            contBtn.click();
            return "STEP2_SUBMITTED";
        }
        return "STEP2_WAIT_BUTTON";
    })()
    """
    res = run_js(step2_js)
    print("  Step 2 result:", res)
    time.sleep(3.0)

    # 4. Step 3: Category & Language
    print("[4/5] Step 3: Setting Category (Computers / Hardware / General) & Language...")
    step3_cat_js = """
    (function() {
        var cat1 = document.querySelectorAll('select')[0];
        if (cat1) {
            cat1.selectedIndex = Array.from(cat1.options).findIndex(o => o.value === 'Computers');
            cat1.dispatchEvent(new Event('change', { bubbles: true }));
        }
        return "CAT1_SET";
    })()
    """
    run_js(step3_cat_js)
    time.sleep(1.0)

    step3_sub_js = """
    (function() {
        var subSel = document.querySelectorAll('select')[1];
        if (subSel) {
            subSel.selectedIndex = Array.from(subSel.options).findIndex(o => o.value === 'COM067000');
            subSel.dispatchEvent(new Event('change', { bubbles: true }));
        }
        var contBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Continue'));
        if (contBtn && !contBtn.disabled) {
            contBtn.click();
            return "STEP3_SUBMITTED";
        }
        return "STEP3_WAIT_BUTTON";
    })()
    """
    res = run_js(step3_sub_js)
    print("  Step 3 result:", res)
    time.sleep(3.0)

    # 5. Step 4: Publishing Details & Upload
    print("[5/5] Step 4: Setting Publisher & Submitting to iTunes Connect...")
    step4_js = """
    (function() {
        function setVal(el, val) {
            if (!el) return false;
            var proto = window.HTMLInputElement.prototype;
            var setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
            if (setter) setter.call(el, val); else el.value = val;
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
            el.dispatchEvent(new Event('blur', { bubbles: true }));
            return true;
        }

        var pubInp = document.querySelector('input[placeholder="Publisher name*"]');
        setVal(pubInp, "Data Center Field Guides");

        var uploadBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Upload Book to iTunes Connect'));
        var disabled = uploadBtn ? uploadBtn.disabled : null;
        
        return JSON.stringify({
            pubVal: pubInp ? pubInp.value : null,
            uploadBtnDisabled: disabled
        });
    })()
    """
    res = run_js(step4_js)
    print("  Step 4 state:", res)

    # Check legend steps icons
    check_legend_js = """
    (function() {
        var steps = Array.from(document.querySelectorAll('.legend-step-container')).map(c => ({
            title: c.innerText.trim(),
            hasCheckmark: c.innerHTML.includes('Checkmark'),
            hasError: c.innerHTML.includes('Error')
        }));
        return JSON.stringify(steps, null, 2);
    })()
    """
    legend_res = run_js(check_legend_js)
    print("\n[+] Verification of 4 Steps:\n", legend_res)

if __name__ == "__main__":
    main()
