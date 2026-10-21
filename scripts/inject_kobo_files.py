#!/usr/bin/env python3
"""
Direct DataTransfer Ingestion for Kobo Cover & EPUB
"""

import base64
import subprocess
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")
COVER_PATH = ROOT / "books" / "02-read-load-bank-data" / "figures" / "cover.jpg"
EPUB_PATH = ROOT / "books" / "02-read-load-bank-data" / "epub" / "read-and-use-load-bank-data.epub"

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

def inject_cover():
    print(f"[+] Injecting cover image: {COVER_PATH.name} ({COVER_PATH.stat().st_size} bytes)...")
    cover_b64 = base64.b64encode(COVER_PATH.read_bytes()).decode('ascii')
    
    js = f'''
    (function() {{
        try {{
            var b64 = "{cover_b64}";
            var binStr = atob(b64);
            var len = binStr.length;
            var bytes = new Uint8Array(len);
            for (var i = 0; i < len; i++) {{
                bytes[i] = binStr.charCodeAt(i);
            }}
            var blob = new Blob([bytes], {{ type: "image/jpeg" }});
            var file = new File([blob], "cover.jpg", {{ type: "image/jpeg" }});
            
            var fileInputs = document.querySelectorAll("input[type=file]");
            var coverInput = fileInputs[0];
            if (!coverInput) return "COVER_INPUT_NOT_FOUND";
            
            var dt = new DataTransfer();
            dt.items.add(file);
            coverInput.files = dt.files;
            
            coverInput.dispatchEvent(new Event("input", {{ bubbles: true }}));
            coverInput.dispatchEvent(new Event("change", {{ bubbles: true }}));
            return "COVER_DISPATCHED_SUCCESSFULLY: " + coverInput.files.length + " file, size: " + coverInput.files[0].size;
        }} catch(e) {{
            return "ERROR: " + e.message;
        }}
    }})()
    '''
    return run_js(js)

def main():
    res = inject_cover()
    print("Result:", res)

if __name__ == "__main__":
    main()
