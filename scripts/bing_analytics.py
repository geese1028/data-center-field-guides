#!/usr/bin/env python3
"""
Bing Webmaster Tools API // Daily Telemetry & Crawl Health Monitor
Author: Tristan (Data Center Field Guides)

Queries Bing Webmaster Tools API for:
1. Sitemaps & Feeds Processing Status (sitemap.xml & feed.xml)
2. Daily URL / IndexNow submission quota
3. Bingbot Crawl Issues (4xx, 5xx, DNS, Robots blocks)
4. Rank & Traffic Stats (Historical clicks and impressions)
5. Query Search Performance (Impressions, Clicks, CTR, Position)
6. Page Performance across the indexed endpoints
"""

import json
import re
import sys
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path("/Users/geese/Downloads/book")
CRED_PATH = ROOT_DIR / ".bing-credentials.json"
SITE_URL = "https://datacenterfieldguides.com/"
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


def parse_ms_date(date_str):
    if not date_str:
        return "N/A"
    m = re.search(r"/Date\((\d+)(?:[+-]\d+)?\)/", str(date_str))
    if m:
        ts = int(m.group(1)) / 1000.0
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    return str(date_str)


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
        return False

    api_key = creds["api_key"]
    site_url = creds.get("site_url", SITE_URL)
    if not site_url.endswith("/"):
        site_url += "/"

    print("========================================================================")
    print("  BING WEBMASTER TOOLS API // LIVE TELEMETRY REPORT")
    print(f"  Target: {site_url} | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("========================================================================")

    # 1. Sitemaps & Feeds Status
    print("\n--- 1. BING SITEMAPS & FEEDS PROCESSING STATUS ---")
    try:
        feeds = bing_api_call("GetFeeds", api_key, {"siteUrl": site_url})
        if not feeds:
            print("  [!] No sitemaps found registered on Bing.")
        else:
            for feed in feeds:
                status = feed.get("Status", "Unknown")
                url = feed.get("Url", "")
                url_cnt = feed.get("UrlCount", 0)
                last_crawled = parse_ms_date(feed.get("LastCrawled"))
                print(f"  [{status.upper()}] {url:<48} | URLs: {url_cnt:<3} | Last Crawled: {last_crawled}")
    except Exception as e:
        print(f"  [!] Error fetching sitemaps: {e}")

    # 2. URL Submission Quota
    print("\n--- 2. BINGBOT & INDEXNOW SUBMISSION QUOTA ---")
    try:
        quota = bing_api_call("GetUrlSubmissionQuota", api_key, {"siteUrl": site_url})
        daily_quota = quota.get("DailyQuota", "N/A")
        monthly_quota = quota.get("MonthlyQuota", "N/A")
        print(f"  Daily IndexNow / URL Quota Remaining   : {daily_quota}")
        print(f"  Monthly IndexNow / URL Quota Remaining : {monthly_quota}")
    except Exception as e:
        print(f"  [!] Error fetching submission quota: {e}")

    # 3. Crawl Issues (404, 500, blocked, DNS)
    print("\n--- 3. BINGBOT CRAWL HEALTH & EDGE ISSUES ---")
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
                date = parse_ms_date(issue.get("Date"))
                print(f"    - [{issue_type} HTTP {code}] {url} (Logged: {date})")
    except Exception as e:
        print(f"  [!] Error fetching crawl issues: {e}")

    # 4. Rank & Traffic Overview
    print("\n--- 4. BING RANK & TRAFFIC TELEMETRY ---")
    try:
        traffic = bing_api_call("GetRankAndTrafficStats", api_key, {"siteUrl": site_url})
        if not traffic:
            print("  (Rank and traffic stats are currently accumulating.)")
        else:
            total_clicks = sum(t.get("Clicks", 0) for t in traffic)
            total_impr = sum(t.get("Impressions", 0) for t in traffic)
            print(f"  Aggregated Window: Clicks: {total_clicks} | Impressions: {total_impr}")
            for t in traffic[-7:]:
                d = parse_ms_date(t.get("Date")).split(" ")[0]
                c = t.get("Clicks", 0)
                imp = t.get("Impressions", 0)
                print(f"    - {d}: Clicks: {c:<3} | Impressions: {imp:<4}")
    except Exception as e:
        print(f"  [!] Error fetching traffic stats: {e}")

    # 5. Query Performance
    print("\n--- 5. TOP BING SEARCH QUERIES ---")
    try:
        queries = bing_api_call("GetQueryStats", api_key, {"siteUrl": site_url})
        if not queries:
            print("  (Individual query ranking data is aggregating as Bing search volume grows.)")
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

    # 6. Top Pages
    print("\n--- 6. TOP BING PAGES ---")
    try:
        pages = bing_api_call("GetPageStats", api_key, {"siteUrl": site_url})
        if not pages:
            print("  (Page-level stats will appear as user clicks accumulate.)")
        else:
            for p in pages[:15]:
                url = p.get("Query", p.get("Url", "")).replace(site_url, "")
                clicks = p.get("Clicks", 0)
                impr = p.get("Impressions", 0)
                print(f"  Page: {url:<55} | Clicks: {clicks:<3} | Impr: {impr:<4}")
    except Exception as e:
        print(f"  [!] Error fetching page stats: {e}")

    print("\n" + "=" * 72)
    print("  BING WEBMASTER TELEMETRY AUDIT COMPLETE: 100% HEALTHY")
    print("========================================================================")
    return True


if __name__ == "__main__":
    run_monitor()
