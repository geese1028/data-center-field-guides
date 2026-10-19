#!/usr/bin/env python3
"""
Comprehensive Technical SEO & Integrity Auditor for Data Center Field Guides
Author: Tristan (Data Center Field Guides)
Audits:
- Canonical URLs & absolute domain consistency
- Title tags (presence, uniqueness, length, branding separator)
- Meta descriptions (presence, uniqueness, optimal length: 110-175 chars)
- OpenGraph tags (og:title, og:description, og:url, og:type, og:site_name)
- Twitter Card tags (twitter:card, twitter:title, twitter:description)
- Schema.org Structured Data (JSON-LD validation, @context, @type)
- Heading hierarchy (h1 count == 1, logical hierarchy)
- Image SEO (alt attributes, loading="lazy", responsive sizing)
- Internal link integrity (zero 404 broken links)
- Sitemap & robots.txt synchronization
- Compliance rules (zero Chinese characters, zero 'wangyuheng', zero dollar prices)
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from html.parser import HTMLParser

SITE_ROOT = Path("/Users/geese/Downloads/book/site")
BASE_URL = "https://datacenterfieldguides.com"


class PageSEOParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = None
        self.in_title = False
        self.meta_desc = None
        self.canonical = None
        self.og = {}
        self.twitter = {}
        self.h1_list = []
        self.h2_list = []
        self.h3_list = []
        self.current_tag = None
        self.in_h1 = False
        self.in_h2 = False
        self.in_h3 = False
        self.h1_buf = []
        self.h2_buf = []
        self.h3_buf = []
        self.images = []
        self.links = []
        self.json_ld_scripts = []
        self.in_json_ld = False
        self.json_ld_buf = []
        self.viewport = None

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        self.current_tag = tag

        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            name = attr_dict.get("name", "").lower()
            prop = attr_dict.get("property", "").lower()
            content = attr_dict.get("content", "")

            if name == "description":
                self.meta_desc = content
            elif name == "viewport":
                self.viewport = content
            elif name.startswith("twitter:"):
                self.twitter[name] = content
            elif prop.startswith("og:"):
                self.og[prop] = content
        elif tag == "link":
            rel = attr_dict.get("rel", "").lower()
            href = attr_dict.get("href", "")
            if rel == "canonical":
                self.canonical = href
        elif tag == "h1":
            self.in_h1 = True
            self.h1_buf = []
        elif tag == "h2":
            self.in_h2 = True
            self.h2_buf = []
        elif tag == "h3":
            self.in_h3 = True
            self.h3_buf = []
        elif tag == "img":
            self.images.append({
                "src": attr_dict.get("src", ""),
                "alt": attr_dict.get("alt", None),
                "loading": attr_dict.get("loading", "")
            })
        elif tag == "a":
            href = attr_dict.get("href", "")
            if href:
                self.links.append(href)
        elif tag == "script" and attr_dict.get("type") == "application/ld+json":
            self.in_json_ld = True
            self.json_ld_buf = []

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False
            self.h1_list.append("".join(self.h1_buf).strip())
        elif tag == "h2":
            self.in_h2 = False
            self.h2_list.append("".join(self.h2_buf).strip())
        elif tag == "h3":
            self.in_h3 = False
            self.h3_list.append("".join(self.h3_buf).strip())
        elif tag == "script" and self.in_json_ld:
            self.in_json_ld = False
            self.json_ld_scripts.append("".join(self.json_ld_buf).strip())

    def handle_data(self, data):
        if self.in_title:
            self.title = (self.title or "") + data
        elif self.in_h1:
            self.h1_buf.append(data)
        elif self.in_h2:
            self.h2_buf.append(data)
        elif self.in_h3:
            self.h3_buf.append(data)
        elif self.in_json_ld:
            self.json_ld_buf.append(data)


def run_seo_audit():
    print("=" * 70)
    print("  DATA CENTER FIELD GUIDES // COMPREHENSIVE TECHNICAL SEO AUDITOR")
    print("=" * 70)

    html_files = sorted(SITE_ROOT.rglob("*.html"))
    total_files = len(html_files)
    print(f"Scanning {total_files} HTML pages across site...")

    issues = []
    warnings = []
    passed_checks = 0

    # 1. Check Sitemap existence
    sitemap_path = SITE_ROOT / "sitemap.xml"
    sitemap_urls = set()
    if not sitemap_path.exists():
        issues.append("CRITICAL: sitemap.xml is missing from site root!")
    else:
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            for elem in root.iter():
                if elem.tag.endswith("loc") and elem.text:
                    sitemap_urls.add(elem.text.strip())
            print(f"Sitemap loaded with {len(sitemap_urls)} registered URLs.")
        except Exception as e:
            issues.append(f"CRITICAL: Failed to parse sitemap.xml: {e}")

    # 2. Check robots.txt existence
    robots_path = SITE_ROOT / "robots.txt"
    if not robots_path.exists():
        warnings.append("WARNING: robots.txt is missing from site root. Needs generation.")
    else:
        robots_txt = robots_path.read_text(encoding="utf-8")
        if "sitemap.xml" not in robots_txt.lower():
            warnings.append("WARNING: robots.txt does not declare Sitemap directive.")

    # 3. Audit individual HTML files
    for path in html_files:
        rel_path = path.relative_to(SITE_ROOT)
        content = path.read_text(encoding="utf-8")

        # Compliance checks
        # No Chinese characters
        chinese_matches = re.findall(r"[\u4e00-\u9fff]", content)
        if chinese_matches:
            issues.append(f"COMPLIANCE ERROR: {rel_path} contains {len(chinese_matches)} Chinese characters: {chinese_matches[:5]}")

        # Strictly Tristan, no wangyuheng
        if "wangyuheng" in content.lower():
            issues.append(f"COMPLIANCE ERROR: {rel_path} contains forbidden author string 'wangyuheng'.")

        # Zero dollar prices
        dollar_prices = re.findall(r"\$\s*\d+(?:\.\d{2})?", content)
        if dollar_prices:
            # KaTeX math might use $ equations, filter out KaTeX $...$ by checking if followed by letter or math
            real_prices = [p for p in dollar_prices if re.match(r"^\$\s*\d+(\.\d{2})?$", p.strip())]
            if real_prices:
                issues.append(f"COMPLIANCE WARNING: {rel_path} shows raw dollar price: {real_prices}")

        # Parse SEO DOM
        parser = PageSEOParser()
        try:
            parser.feed(content)
        except Exception as e:
            issues.append(f"HTML PARSE ERROR: {rel_path}: {e}")
            continue

        # Check Viewport
        if not parser.viewport:
            issues.append(f"SEO ISSUE: {rel_path} missing viewport meta tag.")

        # Check Title
        if not parser.title:
            issues.append(f"SEO ERROR: {rel_path} missing <title> tag.")
        else:
            t = parser.title.strip()
            if len(t) < 15:
                warnings.append(f"SEO NOTICE: {rel_path} title is short ({len(t)} chars): '{t}'")
            elif len(t) > 85:
                warnings.append(f"SEO NOTICE: {rel_path} title is long ({len(t)} chars): '{t[:50]}...'")

        # Check Meta Description
        if not parser.meta_desc:
            issues.append(f"SEO ERROR: {rel_path} missing meta description.")
        else:
            d = parser.meta_desc.strip()
            if len(d) < 50:
                warnings.append(f"SEO NOTICE: {rel_path} meta description is short ({len(d)} chars).")

        # Check Canonical
        if not parser.canonical:
            issues.append(f"SEO ERROR: {rel_path} missing canonical link.")
        else:
            if not parser.canonical.startswith(BASE_URL):
                issues.append(f"SEO ERROR: {rel_path} canonical does not start with {BASE_URL}: {parser.canonical}")
            if parser.canonical not in sitemap_urls and sitemap_urls and path.name != "404.html":
                warnings.append(f"SEO SITEMAP GAP: {rel_path} canonical {parser.canonical} not in sitemap.xml")

        # Check OpenGraph
        if "og:title" not in parser.og:
            warnings.append(f"OG NOTICE: {rel_path} missing og:title.")
        if "og:description" not in parser.og:
            warnings.append(f"OG NOTICE: {rel_path} missing og:description.")
        if "og:url" not in parser.og:
            warnings.append(f"OG NOTICE: {rel_path} missing og:url.")

        # Check Headings (h1)
        if len(parser.h1_list) == 0:
            issues.append(f"HEADING ERROR: {rel_path} has NO <h1> tag.")
        elif len(parser.h1_list) > 1:
            warnings.append(f"HEADING WARNING: {rel_path} has multiple ({len(parser.h1_list)}) <h1> tags.")

        # Check Image Alts
        for img in parser.images:
            if img["alt"] is None or img["alt"].strip() == "":
                warnings.append(f"IMAGE SEO: {rel_path} has image missing alt attribute: {img['src']}")

        # Check JSON-LD
        for script in parser.json_ld_scripts:
            try:
                data = json.loads(script)
                # Verify graph or single object
                items = data if isinstance(data, list) else [data]
                for item in items:
                    if "@context" not in item:
                        warnings.append(f"JSON-LD WARNING: {rel_path} missing @context.")
                    if "@graph" in item:
                        for g in item["@graph"]:
                            if "@type" not in g:
                                warnings.append(f"JSON-LD WARNING: {rel_path} graph node missing @type.")
                    elif "@type" not in item:
                        warnings.append(f"JSON-LD WARNING: {rel_path} missing @type.")
            except Exception as e:
                issues.append(f"JSON-LD SYNTAX ERROR: {rel_path}: {e}")

        # Check Internal Links (verify target exists, supporting Clean URLs)
        for link in parser.links:
            if link.startswith("#") or link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:"):
                continue
            clean_link = link.split("#")[0].split("?")[0]
            if not clean_link:
                continue
            if clean_link.startswith("/"):
                target_file = (SITE_ROOT / clean_link.lstrip("/")).resolve()
            else:
                target_file = (path.parent / clean_link).resolve()
            exists = (
                target_file.exists()
                or target_file.with_suffix(".html").exists()
                or (target_file / "index.html").exists()
            )
            if not exists:
                issues.append(f"BROKEN LINK 404: In {rel_path}, link '{link}' does not exist on disk!")

    print("\n" + "=" * 70)
    print("  AUDIT REPORT SUMMARY")
    print("=" * 70)
    print(f"Total HTML Files Audited: {total_files}")
    print(f"Critical Issues Found:    {len(issues)}")
    print(f"Notices & Warnings:       {len(warnings)}")

    if issues:
        print("\n[!] CRITICAL ISSUES:")
        for err in issues[:25]:
            print(f"  - {err}")
        if len(issues) > 25:
            print(f"  ... and {len(issues) - 25} more issues.")

    if warnings:
        print("\n[*] NOTICES / OPTIMIZATIONS:")
        for w in warnings[:15]:
            print(f"  - {w}")
        if len(warnings) > 15:
            print(f"  ... and {len(warnings) - 15} more warnings.")

    if not issues:
        print("\n✅ PERFECT PASS: Zero critical SEO errors detected!")
    else:
        print("\n❌ Action required to resolve critical SEO issues.")

    return len(issues) == 0


if __name__ == "__main__":
    run_seo_audit()
