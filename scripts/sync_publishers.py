#!/usr/bin/env python3
"""
DCFG Universal Publisher Distribution & Store Synchronization Engine
=====================================================================
Automated task for managing multi-publisher availability across all 9 volumes:
- Rakuten Kobo, Amazon Kindle, Leanpub, Google Play Books, Apple Books.
- Automatically syncs newly published titles from catalog/kobo_queue.json.
- Lights up published books on the homepage (site/index.html) and buy page (site/buy.html).
- Updates platform store buttons with authentic branding & direct destination URLs.
- Updates the Series Progress Roadmap bar.
- Rebuilds all static pages, volume pillar pages, blog ribbons, and schema markup.

Usage:
  python3 scripts/sync_publishers.py                     # Sync from queue & rebuild site
  python3 scripts/sync_publishers.py --status            # View distribution matrix
  python3 scripts/sync_publishers.py --set-kobo 1 <url>  # Set Kobo URL for Volume 1
  python3 scripts/sync_publishers.py --publisher <pub> --book <vol> --url <url>
"""

import sys
import json
import argparse
import subprocess
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")
CATALOG_DIR = ROOT / "catalog"
PUBLISHER_LINKS_FILE = CATALOG_DIR / "publisher_links.json"
KOBO_QUEUE_FILE = CATALOG_DIR / "kobo_queue.json"
BUILD_SITE_SCRIPT = ROOT / "scripts" / "build_site.py"

def load_publisher_data():
    if not PUBLISHER_LINKS_FILE.exists():
        return {"publishers": {}, "books": {}}
    try:
        with open(PUBLISHER_LINKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Error loading {PUBLISHER_LINKS_FILE}: {e}")
        return {"publishers": {}, "books": {}}

def save_publisher_data(data):
    PUBLISHER_LINKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PUBLISHER_LINKS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[✓] Saved updated publisher distribution map: {PUBLISHER_LINKS_FILE}")

def sync_from_kobo_queue():
    """Reads catalog/kobo_queue.json and syncs published Kobo books into publisher_links.json."""
    if not KOBO_QUEUE_FILE.exists():
        print(f"[!] Kobo queue file not found: {KOBO_QUEUE_FILE}")
        return False

    with open(KOBO_QUEUE_FILE, "r", encoding="utf-8") as f:
        queue = json.load(f)

    data = load_publisher_data()
    books = data.setdefault("books", {})
    changed = False

    for item in queue:
        # We only link English main editions to the primary English storefront
        if item.get("lang") == "en" and item.get("status") == "published":
            vol = str(item.get("vol"))
            kobo_url = item.get("kobo_url") or ""
            isbn = item.get("isbn") or ""
            if not kobo_url and isbn:
                kobo_url = f"https://www.kobo.com/search?query={isbn}"
            
            if kobo_url:
                book_entry = books.setdefault(vol, {})
                old_url = book_entry.get("kobo", "")
                if old_url != kobo_url:
                    book_entry["kobo"] = kobo_url
                    changed = True
                    print(f"[+] Synced Kobo link for Volume {vol}: {kobo_url}")

    if changed:
        save_publisher_data(data)
    else:
        print("[-] No new Kobo store URLs found in queue.")
    return changed

def set_publisher_link(publisher: str, vol: int, url: str):
    """Sets or updates a specific store link for a volume."""
    data = load_publisher_data()
    books = data.setdefault("books", {})
    vol_str = str(vol)
    book_entry = books.setdefault(vol_str, {})
    book_entry[publisher] = url
    save_publisher_data(data)
    print(f"[✓] Updated {publisher.upper()} link for Volume {vol}: {url}")

def show_status():
    data = load_publisher_data()
    publishers = data.get("publishers", {})
    books = data.get("books", {})

    print("=" * 80)
    print("  DATA CENTER FIELD GUIDES // MULTI-PUBLISHER DISTRIBUTION MATRIX")
    print("=" * 80)
    pub_keys = ["amazon", "kobo", "leanpub", "google", "apple"]
    
    header = f"{'Vol':<4} | {'Amazon':<10} | {'Rakuten Kobo':<14} | {'Leanpub':<10} | {'Google':<8} | {'Apple':<8}"
    print(header)
    print("-" * 80)

    for i in range(1, 10):
        v = str(i)
        b = books.get(v, {})
        amz = "✓ LIVE" if b.get("amazon") else "—"
        kobo = "✓ LIVE" if b.get("kobo") else "—"
        lean = "✓ LIVE" if b.get("leanpub") else "—"
        goog = "✓ LIVE" if b.get("google") else "—"
        appl = "✓ LIVE" if b.get("apple") else "—"
        print(f"V{i:02d}  | {amz:<10} | {kobo:<14} | {lean:<10} | {goog:<8} | {appl:<8}")

    print("=" * 80)

def rebuild_site():
    print("\n[+] Triggering full site rebuild to update all storefront buttons & badges...")
    res = subprocess.run([sys.executable, str(BUILD_SITE_SCRIPT)], capture_output=True, text=True)
    if res.returncode == 0:
        print("[✓] Site successfully rebuilt and illuminated!")
        for line in res.stdout.splitlines():
            if "Generated" in line or "Site build complete" in line:
                print(f"    {line}")
    else:
        print(f"[!] Site rebuild failed:\n{res.stderr}")

def verify_store_buttons_and_links(test_http=True):
    """
    Verifies that all active publisher links are properly illuminated in the static HTML
    and tests live HTTP reachability for destination URLs.
    """
    import urllib.request
    import urllib.error
    from html.parser import HTMLParser

    data = load_publisher_data()
    books = data.get("books", {})
    buy_html_path = ROOT / "site" / "buy.html"
    
    if not buy_html_path.exists():
        print(f"[!] {buy_html_path} does not exist. Rebuilding site first...")
        rebuild_site()

    with open(buy_html_path, "r", encoding="utf-8") as f:
        buy_html = f.read()

    print("\n" + "=" * 80)
    print("  STORE BUTTON ILLUMINATION & DESTINATION LINK VERIFICATION")
    print("=" * 80)
    print(f"{'Vol':<4} | {'Publisher':<12} | {'DOM Button':<14} | {'HTTP Status':<20} | {'Store URL'}")
    print("-" * 80)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    for vol_str in sorted(books.keys(), key=lambda x: int(x)):
        vol = int(vol_str)
        stores = books[vol_str]
        for pub, url in stores.items():
            if not url:
                continue

            # 1. DOM Check
            # Check if active button exists in buy.html with the URL
            dom_ok = (url in buy_html) and (f"platform-btn is-active {pub}" in buy_html)
            dom_status = "✓ ILLUMINATED" if dom_ok else "✗ MISSING"

            # 2. HTTP Check
            http_status = "SKIPPED"
            if test_http:
                try:
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req, timeout=8) as resp:
                        http_status = f"✓ HTTP {resp.status}"
                except urllib.error.HTTPError as e:
                    if e.code == 403:
                        http_status = "⚠ 403 (Bot Guard)"
                    elif e.code == 404:
                        http_status = "⏳ 404 (In Review)"
                    else:
                        http_status = f"! HTTP {e.code}"
                except Exception as e:
                    http_status = "ERR: Connect"

            print(f"V{vol:02d}  | {pub.capitalize():<12} | {dom_status:<14} | {http_status:<20} | {url[:45]}...")

    print("=" * 80)

def main():
    parser = argparse.ArgumentParser(description="DCFG Multi-Publisher Sync Engine")
    parser.add_argument("--status", action="store_true", help="Show publisher distribution status matrix")
    parser.add_argument("--verify", action="store_true", help="Verify DOM button illumination and test live destination links")
    parser.add_argument("--publisher", type=str, help="Publisher name (e.g. kobo, amazon, google, apple, leanpub)")
    parser.add_argument("--book", type=int, help="Volume number (1-9)")
    parser.add_argument("--url", type=str, help="Destination store URL for the book")
    parser.add_argument("--set-kobo", nargs=2, metavar=("VOL", "URL"), help="Quick-set Kobo URL for volume: --set-kobo 1 <url>")
    parser.add_argument("--no-rebuild", action="store_true", help="Skip rebuilding the site after sync")

    args = parser.parse_args()

    if args.status:
        show_status()
        return

    if args.verify:
        verify_store_buttons_and_links(test_http=True)
        return

    if args.set_kobo:
        vol = int(args.set_kobo[0])
        url = args.set_kobo[1]
        set_publisher_link("kobo", vol, url)
        if not args.no_rebuild:
            rebuild_site()
            verify_store_buttons_and_links(test_http=False)
        return

    if args.publisher and args.book and args.url is not None:
        set_publisher_link(args.publisher, args.book, args.url)
        if not args.no_rebuild:
            rebuild_site()
            verify_store_buttons_and_links(test_http=False)
        return

    # Default action: sync from queue and rebuild
    print("[*] Running automated publisher sync from catalog queues...")
    sync_from_kobo_queue()
    show_status()
    if not args.no_rebuild:
        rebuild_site()
        verify_store_buttons_and_links(test_http=False)

if __name__ == "__main__":
    main()
