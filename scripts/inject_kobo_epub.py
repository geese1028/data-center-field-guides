#!/usr/bin/env python3
"""
Chunked Base64 EPUB Ingestion for Kobo Writing Life
"""

import base64
import subprocess
import time
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")
EPUB_PATH = ROOT / "books" / "02-read-load-bank-data" / "epub" / "read-and-use-load-bank-data.epub"

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

def main():
    print(f"[+] Loading EPUB: {EPUB_PATH.name} ({EPUB_PATH.stat().st_size} bytes)...")
    b64 = base64.b64encode(EPUB_PATH.read_bytes()).decode('ascii')
    total_len = len(b64)
    chunk_size = 400000  # 400KB per chunk
    num_chunks = (total_len + chunk_size - 1) // chunk_size
    print(f"[+] Total b64 length: {total_len} chars across {num_chunks} chunks.")

    # Reset chunks array in Chrome
    run_js("window.__epub_chunks = [];")

    for i in range(num_chunks):
        chunk = b64[i*chunk_size : (i+1)*chunk_size]
        print(f"    Sending chunk {i+1}/{num_chunks} ({len(chunk)} chars)...")
        # Use simple string literal
        js = f'window.__epub_chunks.push("{chunk}");'
        res = run_js(js)
        time.sleep(0.1)

    print("[+] Assembling and dispatching EPUB File object in Kobo DOM...")
    dispatch_js = '''
    (function() {
        try {
            var fullB64 = window.__epub_chunks.join("");
            var binStr = atob(fullB64);
            var len = binStr.length;
            var bytes = new Uint8Array(len);
            for (var i = 0; i < len; i++) {
                bytes[i] = binStr.charCodeAt(i);
            }
            var blob = new Blob([bytes], { type: "application/epub+zip" });
            var file = new File([blob], "read-and-use-load-bank-data.epub", { type: "application/epub+zip" });
            
            var fileInputs = document.querySelectorAll("input[type=file]");
            var epubInput = fileInputs[1];
            if (!epubInput) return "EPUB_INPUT_NOT_FOUND";
            
            var dt = new DataTransfer();
            dt.items.add(file);
            epubInput.files = dt.files;
            
            epubInput.dispatchEvent(new Event("input", { bubbles: true }));
            epubInput.dispatchEvent(new Event("change", { bubbles: true }));
            
            // Clean up memory
            window.__epub_chunks = null;
            
            return "EPUB_DISPATCHED_SUCCESSFULLY: " + epubInput.files[0].name + " (" + epubInput.files[0].size + " bytes)";
        } catch(e) {
            return "ERROR: " + e.message;
        }
    })()
    '''
    res = run_js(dispatch_js)
    print("[✓] Dispatch result:", res)

if __name__ == "__main__":
    main()
