#!/usr/bin/env python3
"""
Automated Google Search Console (GSC) Analytics & Indexing Inspector
for Data Center Field Guides (datacenterfieldguides.com)
"""

import json
import time
import base64
import urllib.request
import urllib.parse
import urllib.error
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime, timedelta

CRED_PATH = Path("/Users/geese/Downloads/book/.gsc-credentials.json")
SITE_URL = "sc-domain:datacenterfieldguides.com"
FALLBACK_SITE_URL = "https://datacenterfieldguides.com/"


def b64url(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")


def get_access_token():
    with open(CRED_PATH, "r", encoding="utf-8") as f:
        cred = json.load(f)

    now = int(time.time())
    header = b64url(json.dumps({"alg": "RS256", "typ": "JWT"}))
    payload = b64url(json.dumps({
        "iss": cred["client_email"],
        "scope": "https://www.googleapis.com/auth/webmasters",
        "aud": cred["token_uri"],
        "exp": now + 3600,
        "iat": now,
    }))
    signing_input = f"{header}.{payload}"

    with tempfile.NamedTemporaryFile("w", delete=False) as kf:
        kf.write(cred["private_key"])
        key_path = kf.name

    sig = subprocess.check_output(
        ["openssl", "dgst", "-sha256", "-sign", key_path],
        input=signing_input.encode("utf-8"),
    )
    Path(key_path).unlink(missing_ok=True)
    jwt = f"{signing_input}.{b64url(sig)}"

    data = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt,
    }).encode("utf-8")

    req = urllib.request.Request(cred["token_uri"], data=data)
    resp = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
    return resp["access_token"]


def api_request(token, method, url, body=None):
    headers = {"Authorization": f"Bearer {token}"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def query_analytics(token, site, dimensions, start_date="2026-10-01", end_date=None, row_limit=100, data_state="all"):
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    enc = urllib.parse.quote(site, safe="")
    url = f"https://searchconsole.googleapis.com/webmasters/v3/sites/{enc}/searchAnalytics/query"
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dimensions,
        "rowLimit": row_limit,
        "dataState": data_state,
    }
    return api_request(token, "POST", url, body)


def inspect_url(token, site, inspection_url):
    url = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
    body = {
        "inspectionUrl": inspection_url,
        "siteUrl": site,
        "languageCode": "en-US",
    }
    return api_request(token, "POST", url, body)


def submit_sitemap(token, site, feedpath="https://datacenterfieldguides.com/sitemap.xml"):
    enc_site = urllib.parse.quote(site, safe="")
    enc_feed = urllib.parse.quote(feedpath, safe="")
    url = f"https://searchconsole.googleapis.com/webmasters/v3/sites/{enc_site}/sitemaps/{enc_feed}"
    return api_request(token, "PUT", url)


def submit_indexnow():
    import xml.etree.ElementTree as ET
    sitemap_file = Path("/Users/geese/Downloads/book/site/sitemap.xml")
    urls = []
    if sitemap_file.exists():
        tree = ET.parse(sitemap_file)
        for loc in tree.getroot().findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
            if loc.text:
                urls.append(loc.text.strip())
    extra_endpoints = [
        "https://datacenterfieldguides.com/llms.txt",
        "https://datacenterfieldguides.com/llms-full.txt",
        "https://datacenterfieldguides.com/SKILL.md",
        "https://datacenterfieldguides.com/feed.xml",
        "https://datacenterfieldguides.com/feed.json",
    ]
    raw_dir = Path("/Users/geese/Downloads/book/site/raw")
    if raw_dir.exists():
        for md_file in sorted(raw_dir.glob("*.md")):
            extra_endpoints.append(f"https://datacenterfieldguides.com/raw/{md_file.name}")
    for ep in extra_endpoints:
        if ep not in urls:
            urls.append(ep)

    indexnow_key = "dcfg7a9e4b2c8f1d6e3a5b9c0d2e4f6a"
    payload = {
        "host": "datacenterfieldguides.com",
        "key": indexnow_key,
        "keyLocation": f"https://datacenterfieldguides.com/{indexnow_key}.txt",
        "urlList": urls,
    }
    encoded_payload = json.dumps(payload).encode("utf-8")
    last_status = 200
    for endpoint in ["https://api.indexnow.org/indexnow", "https://www.bing.com/indexnow"]:
        req = urllib.request.Request(
            endpoint,
            data=encoded_payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            last_status = resp.status
    return last_status, len(urls)


def main():
    import sys
    token = get_access_token()
    sites_resp = api_request(token, "GET", "https://searchconsole.googleapis.com/webmasters/v3/sites")
    entries = sites_resp.get("siteEntry", [])
    print("=" * 72)
    print("  GOOGLE SEARCH CONSOLE API // LIVE TELEMETRY REPORT")
    print("=" * 72)
    if not entries:
        print("[!] No sites authorized yet for gsc-bot@gen-lang-client-0695695294.iam.gserviceaccount.com")
        print("    Please add this email in GSC -> Settings -> Users and permissions.")
        return

    for e in entries:
        print(f"Authorized Property: {e.get('siteUrl')} (Permission: {e.get('permissionLevel')})")

    active_site = entries[0]["siteUrl"]

    # --- ACCELERATED INDEXING ENGINE (DAILY EXECUTION) ---
    skip_push = "--no-push" in sys.argv
    if not skip_push:
        print("\n[+] Triggering Accelerated Indexing Protocol...")
        # 1. Resubmit Sitemaps to Google
        for feedpath in [
            "https://datacenterfieldguides.com/sitemap.xml",
            "https://datacenterfieldguides.com/feed.xml",
        ]:
            try:
                submit_sitemap(token, active_site, feedpath)
                print(f"[✓] GSC Ping: Resubmitted {feedpath}")
            except Exception as e:
                print(f"[!] GSC Sitemap Ping Error ({feedpath}): {e}")

        # 2. Push full catalog + LLM endpoints to IndexNow (Bing / Copilot / ChatGPT)
        try:
            status_code, count = submit_indexnow()
            print(f"[✓] IndexNow Push: {count} URLs actively pinged to Bing/Copilot/ChatGPT Search (HTTP {status_code})")
        except Exception as e:
            print(f"[!] IndexNow Error: {e}")

        # 3. Google URL Inspection for priority newly deployed/trending articles
        priority_urls = [
            "https://datacenterfieldguides.com/blog/tier-3-data-center-audit-checklist",
            "https://datacenterfieldguides.com/blog/data-center-cfd-verification-guide",
            "https://datacenterfieldguides.com/blog/eop-stops",
            "https://datacenterfieldguides.com/blog/data-center-facility-location-due-diligence",
            "https://datacenterfieldguides.com/blog/nvl72-liquid-load-bank-testing-guide",
        ]
        print("\n--- GOOGLE URL INSPECTION (REAL-TIME CRAWL & INDEX CHECK) ---")
        for u in priority_urls:
            try:
                res = inspect_url(token, active_site, u)
                cov = res.get("inspectionResult", {}).get("indexStatusResult", {}).get("coverageState", "Unknown")
                verdict = res.get("inspectionResult", {}).get("indexStatusResult", {}).get("verdict", "Unknown")
                slug = u.split("/")[-1]
                print(f"  [{verdict}] {slug:<45} -> {cov}")
            except Exception as e:
                print(f"  [!] Inspection Error ({u}): {e}")

    # 1. Sitemaps status
    enc = urllib.parse.quote(active_site, safe="")
    try:
        sitemaps = api_request(token, "GET", f"https://searchconsole.googleapis.com/webmasters/v3/sites/{enc}/sitemaps")
        print("\n--- SITEMAP STATUS ---")
        for sm in sitemaps.get("sitemap", []):
            print(f"Path: {sm.get('path')} | Last Submitted: {sm.get('lastSubmitted')} | Last Downloaded: {sm.get('lastDownloaded')} | Errors: {sm.get('errors')} | Warnings: {sm.get('warnings')}")
            for c in sm.get("contents", []):
                print(f"  -> Type: {c.get('type')} | Submitted: {c.get('submitted')} | Indexed: {c.get('indexed')}")
    except Exception as ex:
        print(f"Sitemap check error: {ex}")

    # 2. Overall Totals (including fresh/hourly dataState='all')
    print("\n--- TOP QUERIES (dataState='all', including fresh data) ---")
    q_res = query_analytics(token, active_site, ["query"])
    for r in q_res.get("rows", []):
        k = r["keys"][0]
        print(f"  Query: {k:<55} | Clicks: {r['clicks']} | Impr: {r['impressions']} | CTR: {r['ctr']*100:.1f}% | Pos: {r['position']:.1f}")

    # 3. Top Pages
    print("\n--- TOP PAGES (dataState='all') ---")
    p_res = query_analytics(token, active_site, ["page"])
    for r in p_res.get("rows", []):
        k = r["keys"][0]
        print(f"  Page: {k:<65} | Clicks: {r['clicks']} | Impr: {r['impressions']} | CTR: {r['ctr']*100:.1f}% | Pos: {r['position']:.1f}")

    # 4. Cross-Dimensional Query x Page x Country x Device
    print("\n--- 4D CROSS-MATRIX: QUERY x PAGE x COUNTRY x DEVICE ---")
    cross_res = query_analytics(token, active_site, ["query", "page", "country", "device"])
    for r in cross_res.get("rows", []):
        q, p, c, d = r["keys"]
        short_p = p.replace("https://datacenterfieldguides.com", "")
        print(f"  [{c.upper()}/{d}] '{q}' -> {short_p} (Impr: {r['impressions']}, Pos: {r['position']:.1f})")

    # 5. Countries Breakdown
    print("\n--- COUNTRIES BREAKDOWN ---")
    c_res = query_analytics(token, active_site, ["country"])
    for r in c_res.get("rows", []):
        k = r["keys"][0]
        print(f"  Country: {k.upper():<10} | Clicks: {r['clicks']} | Impr: {r['impressions']} | Pos: {r['position']:.1f}")

    # 6. Devices Breakdown
    print("\n--- DEVICES BREAKDOWN ---")
    d_res = query_analytics(token, active_site, ["device"])
    for r in d_res.get("rows", []):
        k = r["keys"][0]
        print(f"  Device: {k:<12} | Clicks: {r['clicks']} | Impr: {r['impressions']} | Pos: {r['position']:.1f}")

    # 7. Search Appearance (Rich Results / AI / FAQ)
    print("\n--- SEARCH APPEARANCE ---")
    sa_res = query_analytics(token, active_site, ["searchAppearance"])
    for r in sa_res.get("rows", []):
        k = r["keys"][0]
        print(f"  Appearance: {k:<25} | Clicks: {r['clicks']} | Impr: {r['impressions']} | Pos: {r['position']:.1f}")


if __name__ == "__main__":
    main()

