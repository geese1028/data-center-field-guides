#!/usr/bin/env python3
"""
Direct Chrome DOM Injector via macOS AppleScript
Allows Antigravity Agent to directly inspect, fill, and control the active Kobo / KDP browser tab.
"""

import json
import subprocess
import sys
import time

def run_js(js_code):
    # Escape quotes for AppleScript string
    escaped_js = js_code.replace('\\', '\\\\').replace('"', '\\"')
    apple_script = f'''
    tell application "Google Chrome"
        tell active tab of front window
            execute javascript "{escaped_js}"
        end tell
    end tell
    '''
    res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
    if res.returncode != 0:
        return {"error": res.stderr.strip()}
    return {"result": res.stdout.strip()}

def get_tab_info():
    script = '''
    tell application "Google Chrome"
        tell active tab of front window
            return (get URL) & "|||" & (get title)
        end tell
    end tell
    '''
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    if res.returncode == 0 and "|||" in res.stdout:
        url, title = res.stdout.strip().split("|||", 1)
        return {"url": url, "title": title}
    return None

def inject_book_1_english():
    js = """
    (function() {
        var b = {
            title: "Design and Build a Liquid Load Bank for NVL72 Racks",
            subtitle: "A Field Guide to Interface Boundaries, P&ID Hydraulics, Thermal Envelopes, and Prototype Acceptance",
            series: "Data Center Field Guides",
            series_number: "1",
            author: "Tristan",
            publisher: "Data Center Field Guides",
            imprint: "Data Center Field Guides",
            language: "English",
            price: "12.99",
            synopsis: "A liquid load bank replaces the rack-side thermal load and liquid conditions of NVL72-class AI hardware. It is not a CDU, and not a fabrication drawing.\\n\\nThis field guide states what to write before metal is cut, and which engineering gates must pass before a prototype can be called complete. The reader leaves with two clean handover documents: the liquid load bank requirement sheet and the prototype acceptance sheet. Flow, temperature, pressure, and coupling numbers remain blank until cited against the vendor specification then in force.\\n\\nKey engineering coverage:\\n- Manifold and quick-disconnect (QDC) interface boundaries\\n- Flow rate vs. differential pressure (ΔP) hydraulic curves\\n- Step-load thermal rejection and CDU hunting prevention\\n- Non-negotiable field verification and refuse-to-sign gates"
        };

        function setReactVal(el, val) {
            if (!el) return false;
            var setter = (el instanceof HTMLTextAreaElement ? Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value") : Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value")).set;
            setter.call(el, val);
            el.dispatchEvent(new Event("input", { bubbles: true }));
            el.dispatchEvent(new Event("change", { bubbles: true }));
            el.dispatchEvent(new Event("blur", { bubbles: true }));
            return true;
        }

        var report = [];

        // 1. Title & Subtitle
        ['input[name*="Title"]', 'input[id*="title"]', '#eBookTitle', '#Title', 'input[placeholder*="Title"]'].forEach(sel => {
            var el = document.querySelector(sel);
            if (el && !el.value) { setReactVal(el, b.title); report.push("Title set"); }
        });

        ['input[name*="Subtitle"]', 'input[id*="subtitle"]', '#eBookSubtitle', '#Subtitle'].forEach(sel => {
            var el = document.querySelector(sel);
            if (el && !el.value) { setReactVal(el, b.subtitle); report.push("Subtitle set"); }
        });

        // 2. Series
        ['input[name*="Series"]', 'input[id*="series"]', '#SeriesName'].forEach(sel => {
            var el = document.querySelector(sel);
            if (el && !el.value) { setReactVal(el, b.series); report.push("Series set"); }
        });
        ['input[name*="SeriesNumber"]', 'input[id*="seriesNumber"]', '#SeriesNumber'].forEach(sel => {
            var el = document.querySelector(sel);
            if (el && !el.value) { setReactVal(el, b.series_number); report.push("SeriesNum set"); }
        });

        // 3. Author & Publisher
        ['input[name*="Contributor"]', 'input[name*="Author"]', 'input[id*="contributor"]'].forEach(sel => {
            var el = document.querySelector(sel);
            if (el && !el.value) { setReactVal(el, b.author); report.push("Author set"); }
        });

        ['input[name*="Publisher"]', 'input[id*="publisher"]', '#PublisherName'].forEach(sel => {
            var el = document.querySelector(sel);
            if (el && !el.value) { setReactVal(el, b.publisher); report.push("Publisher set"); }
        });

        ['input[name*="Imprint"]', 'input[id*="imprint"]', '#ImprintName'].forEach(sel => {
            var el = document.querySelector(sel);
            if (el && !el.value) { setReactVal(el, b.imprint); report.push("Imprint set"); }
        });

        // 4. Synopsis
        var syn = document.querySelector('textarea[name*="Synopsis"], textarea[id*="synopsis"], textarea[name*="description"], #Synopsis');
        if (syn && !syn.value) {
            setReactVal(syn, b.synopsis);
            report.push("Synopsis set");
        }
        var rich = document.querySelector('.ck-editor__editable, [contenteditable="true"]');
        if (rich && !rich.innerText.trim()) {
            rich.innerText = b.synopsis;
            rich.dispatchEvent(new Event("input", { bubbles: true }));
            report.push("Rich synopsis set");
        }

        // 5. Language
        var lang = document.querySelector('select[name*="Language"], select[id*="language"], #Language');
        if (lang) {
            for (var opt of lang.options) {
                if (opt.text.toLowerCase().includes("english") || opt.value.toLowerCase().includes("en")) {
                    lang.value = opt.value;
                    lang.dispatchEvent(new Event("change", { bubbles: true }));
                    report.push("Language English set");
                    break;
                }
            }
        }

        return report.length > 0 ? "INJECTED: " + report.join(", ") : "NO_EMPTY_FIELDS_FOUND";
    })()
    """
    return run_js(js)

if __name__ == "__main__":
    tab = get_tab_info()
    print("Current Active Chrome Tab:", tab)
    if tab and "kobo.com" in tab.get("url", ""):
        res = inject_book_1_english()
        print("Injection Result:", res)
    else:
        print("Chrome front window is not on kobo.com")
