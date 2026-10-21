#!/usr/bin/env python3
"""
Build complete 18-book Kobo Publishing Queue.
Strategy updated per user directive (2026-10-21):
- Phase 1: All 9 English editions published first (1 book/day cadence).
- Phase 2: All 9 Japanese editions parked awaiting Gemini 4 quota reset for full technical audit.
"""

import os
import json
from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book")
QUEUE_FILE = ROOT / "catalog" / "kobo_queue.json"

VOLUMES = [
    {
        "vol": 1,
        "dir": "01-liquid-load-bank",
        "en_title": "Design and Build a Liquid Load Bank for NVL72 Racks",
        "en_sub": "A Field Guide to Interface Boundaries, P&ID Hydraulics, Thermal Envelopes, and Prototype Acceptance",
        "ja_title": "NVL72級ラック向け液冷負荷装置を设计し、作る",
        "ja_sub": "要求シートと试作の合格判定",
    },
    {
        "vol": 2,
        "dir": "02-read-load-bank-data",
        "en_title": "Read and Use Load Bank Data",
        "en_sub": "A Field Guide to Hydraulic Telemetry, Thermal Transients, and Refusal Signatures",
        "ja_title": "負荷試験データを読み、使う",
        "ja_sub": "水力テレメトリと過渡熱応答の判定シート",
    },
    {
        "vol": 3,
        "dir": "03-run-one-test",
        "en_title": "Finish a Liquid Cooling Verification",
        "en_sub": "A Field Guide to Level 0–6 Commissioning Scripts, Primary Heat Rejection, and Handover Gates",
        "ja_title": "液冷検証プロジェクトを完遂する",
        "ja_sub": "レベル0〜6コミッショニングと受入判定",
    },
    {
        "vol": 4,
        "dir": "04-judge-a-cfd",
        "en_title": "Judge a Data Hall CFD Model",
        "en_sub": "A Field Guide to Boundary Conditions, Thermal Bypass, and Computational Refusal",
        "ja_title": "データホールCFDモデルを判定する",
        "ja_sub": "境界条件、熱バイパス、計算受入の拒绝",
    },
    {
        "vol": 5,
        "dir": "05-run-the-day",
        "en_title": "Run the Data Center Day",
        "en_sub": "A Field Guide to Mission-Critical Shift Operations, Incident Cascades, and 2N Isolation",
        "ja_title": "データセンターの一日を運用する",
        "ja_sub": "ミッションクリティカル交替勤務と2N隔離手順",
    },
    {
        "vol": 6,
        "dir": "06-when-a-monitor-may-speak",
        "en_title": "When a Monitor May Speak",
        "en_sub": "A Field Guide to BMS/EPMS Telemetry, Alarm Suppression, and Trip Verification",
        "ja_title": "監視システムが警報を発する基準",
        "ja_sub": "BMS/EPMS遠隔測定、アラーム抑制、トリップ検証",
    },
    {
        "vol": 7,
        "dir": "07-refuse-the-handover",
        "en_title": "Refuse the Handover",
        "en_sub": "A Field Guide to Punch Lists, Incomplete Verification, and Non-Negotiable Refusal Gates",
        "ja_title": "引き渡しを拒否する基準",
        "ja_sub": "残項目リスト、未完了検証、譲れない署名拒否の門",
    },
    {
        "vol": 8,
        "dir": "08-judge-a-corrosion-coupon",
        "en_title": "Judge a Corrosion Coupon",
        "en_sub": "A Field Guide to ANSI/ISA-71.04 Severity Levels, Gas Contamination, and Silver Corrosion",
        "ja_title": "腐食クーポンを判定する",
        "ja_sub": "ANSI/ISA-71.04環境基準、ガス状汚染物質、銀腐食",
    },
    {
        "vol": 9,
        "dir": "09-walk-a-tdd",
        "en_title": "Walk a Technical Due Diligence",
        "en_sub": "A Field Guide to Site Power Allocation, Substation Redundancy, and Title Red Flags",
        "ja_title": "技術デューデリジェンスを歩く",
        "ja_sub": "受電容量、変電所冗長性、用地買収の重大リスク",
    }
]

def build_queue():
    queue = []
    
    # 1. Volume 1 English (Submitted and in progress on Kobo)
    v1_dir = ROOT / "books" / "01-liquid-load-bank"
    queue.append({
        "id": "vol01-en",
        "vol": 1,
        "lang": "en",
        "lang_name": "English",
        "title": VOLUMES[0]["en_title"],
        "subtitle": VOLUMES[0]["en_sub"],
        "epub": str(v1_dir / "epub" / "design-and-build-a-liquid-load-bank.epub"),
        "cover": str(v1_dir / "figures" / "cover.jpg"),
        "status": "published",
        "published_at": "2026-10-21",
        "product_id": "abe1c1fa-14ef-4fcf-a1da-d1c23004386b",
        "isbn": "1990000032332",
        "kobo_url": "https://www.kobo.com/search?query=1990000032332",
        "partner_url": "https://writinglife.kobo.com/v2/ebooks/ebook/abe1c1fa-14ef-4fcf-a1da-d1c23004386b"
    })

    # 2. Volumes 2-9 English (Prioritized 1 book per day)
    for v in VOLUMES[1:]:
        vdir = ROOT / "books" / v["dir"]
        en_epub = [f for f in (vdir / "epub").glob("*.epub") if not f.name.endswith(".ja.epub") and not f.name.endswith(".ko.epub") and not f.name.endswith(".ar.epub") and not f.name.endswith(".id.epub") and not f.name.endswith(".th.epub")]
        en_epub_path = str(en_epub[0]) if en_epub else ""
        en_cover = str(vdir / "figures" / "cover.jpg")
        
        queue.append({
            "id": f"vol{v['vol']:02d}-en",
            "vol": v["vol"],
            "lang": "en",
            "lang_name": "English",
            "title": v["en_title"],
            "subtitle": v["en_sub"],
            "epub": en_epub_path,
            "cover": en_cover,
            "status": "queued",
            "cadence": "1 book / day"
        })

    # 3. Japanese editions (Volumes 1-9 Parked for Gemini 4 Quota Reset & Audit)
    for v in VOLUMES:
        vdir = ROOT / "books" / v["dir"]
        ja_epub = list((vdir / "epub" / "ja").glob("*.epub"))
        ja_epub_path = str(ja_epub[0]) if ja_epub else ""
        ja_cover = str(vdir / "figures" / "covers" / "ja.jpg")
        
        queue.append({
            "id": f"vol{v['vol']:02d}-ja",
            "vol": v["vol"],
            "lang": "ja",
            "lang_name": "Japanese",
            "title": v["ja_title"],
            "subtitle": v["ja_sub"],
            "epub": ja_epub_path,
            "cover": ja_cover,
            "status": "parked_audit_pending",
            "audit_note": "Parked awaiting Gemini 4 quota reset for full technical audit before release"
        })

    QUEUE_FILE.write_text(json.dumps(queue, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[✓] Compiled {len(queue)} items into {QUEUE_FILE}")
    print(f"    - English: 1 Published, 8 Queued")
    print(f"    - Japanese: 9 Parked (Audit Pending)")

if __name__ == "__main__":
    build_queue()
