#!/usr/bin/env python3
"""
Bing Webmaster Tools API // Daily Telemetry & Crawl Health Monitor
Author: Tristan (Data Center Field Guides)

Queries Bing Webmaster Tools API for:
1. Daily URL / IndexNow submission quota
2. Bingbot Crawl Issues (4xx, 5xx, DNS, Robots blocks)
3. Query Search Performance (Impressions, Clicks, CTR, Position)
4. Page Performance across the 83 indexed endpoints
"""

import json
import sys
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path("/Users/geese/Downloads/book")
CRED_PATH = ROOT_DIR / ".bing-credentials.json"
SITE_URL = "https://datacenterfieldguides.com"
API_BASE = "https://ssl.bing.com/webmaster/api.svc/json"


def load_credentials():
    if not CRED_PATH.exists():
        return None
    try:
        with open(CRED_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Error reading {CRED_PATH}: {e}")
        return None


def bing_api_call(action, api_key, params=None):
    if params is None:
        params = {}
    params["apikey"] = api_key
    if "siteUrl" not in params:
        params["siteUrl"] = SITE_URL

    query_str = urllib.parse.urlencode(params)
    url = f"{API_BASE}/{action}?{query_str}"
    
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "DCFG-Bing-Monitor/1.0",
            "Accept": "application/json",
        },
        method="GET"
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data.get("d", data)


def run_monitor():
    creds = load_credentials()
    if not creds or not creds.get("api_key"):
        print("========================================================================")
        print("  BING WEBMASTER TOOLS API // DAILY MONITOR SETUP REQUIRED")
        print("========================================================================")
        print("Missing credentials file: .bing-credentials.json")
        print("\nTo activate daily Bing automated monitoring:")
        print("1. Log in to Bing Webmaster Tools: https://www.bing.com/webmasters")
        print("2. Click Settings ⚙️ (top-right) -> 'API Access' -> 'API Key'")
        print("3. Click 'Generate Key' and copy your API Key.")
        print(f"4. Save to {CRED_PATH}:")
        print('   {\n     "api_key": "YOUR_BING_API_KEY",\n     "site_url": "https://datacenterfieldguides.com"\n   }')
        return False

    api_key = creds["api_key"]
    site_url = creds.get("site_url", SITE_URL)

    print("========================================================================")
    print("  BING WEBMASTER TOOLS API // LIVE TELEMETRY REPORT")
    print(f"  Target: {site_url} | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("========================================================================")

    # 1. URL Submission Quota
    print("\n--- 1. BINGBOT & INDEXNOW SUBMISSION QUOTA ---")
    try:
        quota = bing_api_call("GetUrlSubmissionQuota", api_key, {"siteUrl": site_url})
        daily_remain = quota.get("DailyQuotaRemaining", "N/A")
        monthly_remain = quota.get("MonthlyQuotaRemaining", "N/A")
        print(f"  Daily IndexNow / URL Quota Remaining   : {daily_remain}")
        print(f"  Monthly IndexNow / URL Quota Remaining : {monthly_remain}")
    except Exception as e:
        print(f"  [!] Error fetching submission quota: {e}")

    # 2. Crawl Issues (404, 500, blocked, DNS)
    print("\n--- 2. BINGBOT CRAWL HEALTH & EDGE ISSUES ---")
    try:
        issues = bing_api_call("GetCrawlIssues", api_key, {"siteUrl": site_url})
        if not issues:
            print("  ✓ Zero crawl issues detected by Bingbot! Clean edge pass.")
        else:
            print(f"  [!] {len(issues)} crawl issues detected:")
            for issue in issues[:10]:
                issue_type = issue.get("IssueType", "Unknown")
                url = issue.get("Url", "")
                code = issue.get("HttpCode", "")
                date = issue.get("Date", "")
                print(f"    - [{issue_type} HTTP {code}] {url} (Logged: {date})")
    except Exception as e:
        print(f"  [!] Error fetching crawl issues: {e}")

    # 3. Query Performance
    print("\n--- 3. TOP BING SEARCH QUERIES ---")
    try:
        queries = bing_api_call("GetQueryStats", api_key, {"siteUrl": site_url})
        if not queries:
            print("  (Bing performance data is aggregating. Impressions will appear as Bingbot indexes URLs.)")
        else:
            for q in queries[:15]:
                name = q.get("Query", "")
                clicks = q.get("Clicks", 0)
                impr = q.get("Impressions", 0)
                pos = q.get("AvgImpressionPosition", 0) / 10.0
                ctr = (clicks / impr * 100) if impr > 0 else 0.0
                print(f"  Query: {name:<45} | Clicks: {clicks:<3} | Impr: {impr:<4} | CTR: {ctr:.1f}% | Pos: {pos:.1f}")
    except Exception as e:
        print(f"  [!] Error fetching query stats: {e}")

    # 4. Top Pages
    print("\n--- 4. TOP BING PAGES ---")
    try:
        pages = bing_api_call("GetPageStats", api_key, {"siteUrl": site_url})
        if not pages:
            print("  (Page-level stats will appear as Bing search traffic accumulates.)")
        else:
            for p in pages[:15]:
                url = p.get("Query", p.get("Url", "")).replace(site_url, "")
                clicks = p.get("Clicks", 0)
                impr = p.get("Impressions", 0)
                print(f"  Page: {url:<55} | Clicks: {clicks:<3} | Impr: {impr:<4}")
    except Exception as e:
        print(f"  [!] Error fetching page stats: {e}")

    return True


if __name__ == "__main__":
    run_monitor()
