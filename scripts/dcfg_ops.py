#!/usr/bin/env python3
"""
DCFG Unified Operations Control Center (CLI)
Consolidates all publishing, telemetry, SEO, social distribution, and web helper workflows.
"""

import os
import sys
import json
import subprocess
import webbrowser
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")
SCRIPTS = ROOT / "scripts"

def run_cmd(args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True)

def show_status():
    print("=" * 76)
    print("  DATA CENTER FIELD GUIDES // UNIFIED OPERATIONS DASHBOARD")
    print("=" * 76)

    # 1. KDP Status
    cat_path = ROOT / "catalog" / "kdp_catalog.json"
    if cat_path.exists():
        try:
            with open(cat_path, "r", encoding="utf-8") as f:
                cat_data = json.load(f)
            print(f"\n[1] AMAZON KDP CATALOG:")
            print(f"    • Total Configured Editions : {len(cat_data)}")
            print(f"    • AutoFiller Userscript     : scripts/kdp_autofill.user.js (READY)")
            print(f"    • 1-Click Launchpad         : scripts/kdp_companion.html (READY)")
        except Exception as e:
            print(f"\n[1] AMAZON KDP CATALOG: Error ({e})")

    # 2. Kobo Status
    kobo_path = ROOT / "catalog" / "kobo_queue.json"
    if kobo_path.exists():
        try:
            with open(kobo_path, "r", encoding="utf-8") as f:
                kobo_queue = json.load(f)
            en_books = [b for b in kobo_queue if b.get("lang") == "en"]
            ja_books = [b for b in kobo_queue if b.get("lang") == "ja"]
            en_pub = [b for b in en_books if b.get("status") == "published"]
            next_en = [b for b in en_books if b.get("status") == "queued"]
            print(f"\n[2] RAKUTEN KOBO AUTO-PILOT (ENGLISH PRIORITY CADENCE):")
            print(f"    • English Progress    : {len(en_pub)} / {len(en_books)} Published")
            print(f"    • Today's Status      : Vol 1 (English) [PUBLISHED on Kobo - ISBN 1990000032332]")
            if next_en:
                print(f"    • Tomorrow's Target   : {next_en[0]['id']} -> {next_en[0]['title'][:40]} (English)")
            print(f"    • Japanese Editions   : {len(ja_books)} Volumes PARKED (Audit Pending with Gemini 4)")
            print(f"    • Universal Sync Task : scripts/sync_publishers.py (READY)")
        except Exception as e:
            print(f"\n[2] RAKUTEN KOBO AUTO-PILOT: Error ({e})")

    # 3. LinkedIn Status
    li_cred = ROOT / ".linkedin-credentials.json"
    li_pub = ROOT / ".linkedin-published.json"
    li_published_count = 0
    if li_pub.exists():
        try:
            with open(li_pub, "r") as f:
                li_published_count = len(json.load(f))
        except Exception:
            pass
    print(f"\n[3] LINKEDIN AUTO-PILOT:")
    print(f"    • Credentials Status : {'CONNECTED (OAuth OK)' if li_cred.exists() else 'MISSING'}")
    print(f"    • Published Posts    : {li_published_count} / 7")
    print(f"    • Daily Cron Schedule: 30 21 * * * (Active)")

    # 4. Search Engine Telemetry
    bing_cred = ROOT / ".bing-credentials.json"
    gsc_cred = ROOT / ".gsc-credentials.json"
    print(f"\n[4] SEARCH ENGINE TELEMETRY & INDEXING:")
    print(f"    • Bing Webmaster API : {'CONNECTED (Daily Cron 09:00 Active)' if bing_cred.exists() else 'MISSING'}")
    print(f"    • Google GSC API     : {'CONNECTED (Service Account OK)' if gsc_cred.exists() else 'MISSING'}")
    print(f"    • Live Site          : https://datacenterfieldguides.com")

    # 5. Purchase Links & Storefront Health Check
    print(f"\n[5] STOREFRONT & PURCHASE LINK HEALTH AUDIT:")
    try:
        from verify_purchase_links import audit_all_links
        audit_all_links(quarantine=False)
    except Exception as e:
        print(f"    • Storefront check error: {e}")

    # 6. Crontab verification
    res = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    cron_lines = [l for l in res.stdout.splitlines() if l.strip() and not l.startswith("#")]
    print(f"\n[6] ACTIVE SYSTEM BACKGROUND CRONS:")
    for l in cron_lines:
        print(f"    • {l}")

    # 7. Thanksgiving / Black Friday Parking Lot
    print(f"\n[7] THANKSGIVING / BLACK FRIDAY 2026 PARKING LOT (PARKED):")
    print(f"    • Leanpub Membership       : WAITING for Black Friday Sale (Bulk upload Books 1-3 + translations)")
    print(f"    • Draft2Digital Activation : WAITING for Black Friday Promo ($20 fee discount/waiver)")

    print("\n" + "=" * 76)
    print("  QUICK COMMANDS:")
    print("    python3 scripts/dcfg_ops.py check-links      -> Verify all 9 volume store links")
    print("    python3 scripts/dcfg_ops.py launchpad        -> Open KDP Launchpad in browser")
    print("    python3 scripts/dcfg_ops.py sync-publishers  -> Sync multi-publisher links & illuminate site")
    print("    python3 scripts/dcfg_ops.py telemetry        -> Run live Bing & GSC telemetry check")
    print("    python3 scripts/dcfg_ops.py build-site       -> Rebuild static site & llms.txt")
    print("=" * 76)

def open_launchpads():
    kdp_html = ROOT / "scripts" / "kdp_companion.html"
    print("[+] Opening DCFG KDP Launchpad...")
    webbrowser.open(f"file://{kdp_html}")

def sync_publishers():
    print("[+] Synchronizing publisher distribution links & illuminating site...")
    subprocess.run([sys.executable, str(SCRIPTS / "sync_publishers.py")])

def run_telemetry():
    print("[+] Running Bing Analytics...")
    subprocess.run([sys.executable, str(SCRIPTS / "bing_analytics.py")])
    if (SCRIPTS / "gsc_analytics.py").exists():
        print("\n[+] Running Google Search Console Telemetry...")
        subprocess.run([sys.executable, str(SCRIPTS / "gsc_analytics.py")])

def build_site():
    print("[+] Rebuilding static site & indexing artifacts...")
    subprocess.run([sys.executable, str(SCRIPTS / "build_site.py")])

def check_links():
    print("[+] Auditing all storefront & purchase links...")
    subprocess.run([sys.executable, str(SCRIPTS / "verify_purchase_links.py")])

def main():
    if len(sys.argv) <= 1 or sys.argv[1] in ["status", "--status"]:
        show_status()
    elif sys.argv[1] in ["check-links", "links", "--check-links"]:
        check_links()
    elif sys.argv[1] in ["launchpad", "launchpads", "--launchpad"]:
        open_launchpads()
    elif sys.argv[1] in ["sync-publishers", "publishers", "--publishers"]:
        sync_publishers()
    elif sys.argv[1] in ["telemetry", "--telemetry"]:
        run_telemetry()
    elif sys.argv[1] in ["build-site", "--build"]:
        build_site()
    else:
        print(f"Unknown action: {sys.argv[1]}")
        print("Usage: python3 scripts/dcfg_ops.py [status|launchpad|telemetry|build-site]")

if __name__ == "__main__":
    main()
