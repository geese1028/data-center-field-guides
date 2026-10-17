#!/usr/bin/env python3
"""
Automated LinkedIn Technical Content Publisher for Data Center Field Guides
Drives high-intent engineering traffic to datacenterfieldguides.com via native
LinkedIn posts (crisp field hooks + 1800x1100 architectural diagrams + Clean URLs).
Zero salesy book pitches in the feed; pure first-principles engineering insights.
"""

import json
import sys
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path("/Users/geese/Downloads/book")
CRED_PATH = ROOT_DIR / ".linkedin-credentials.json"
FIGURES_DIR = ROOT_DIR / "site" / "blog" / "figures" / "flagship"

# Wave 1 Flagship Campaign Queue (7 Cornerstone Articles + Native Diagrams)
WAVE_1_QUEUE = [
    {
        "id": "01-facility-location-tdd",
        "slug": "data-center-facility-location-due-diligence",
        "title": "Facility Location Due Diligence Checklist: Grid, Land & Environmental Veto Gates",
        "image": str(FIGURES_DIR / "fig-facility-location-due-diligence-matrix.png"),
        "post_text": (
            "A cheap land parcel with a non-binding utility 'will-serve' letter is not a data center site. It is a stranded capital trap.\n\n"
            "When evaluating a greenfield campus or brownfield shell during Facility Location Due Diligence, high-gloss broker flyers routinely mask four fatal veto gates:\n\n"
            "1. Power & Grid Reality: A distribution planner's feasibility letter does not allocate megawatts. Without an executed Facility Study (FS), a signed Large Generator / Load Interconnection Agreement, and verified N-1 substation transformer bay positions, your '24-month delivery' is a 60-to-84-month transmission upgrade queue.\n"
            "2. Water & Thermal Boundary: Designing cooling loops around mean summer temperatures guarantees chiller high-head pressure trips during a 20-year ASHRAE n-year extreme wet-bulb event.\n"
            "3. Fiber Physical Diversity: Three carriers entering through two manholes on the same municipal bridge sharing a single highway right-of-way is a single point of failure (SPOF). Always audit KMZ splice-closure coordinates.\n"
            "4. Acoustic & Permitting Envelopes: Diesel generator acoustical propagation (dBA at the property boundary under nocturnal thermal inversion) and Title V air-quality runtime caps can legally lock out your commissioning load bank tests.\n\n"
            "We compiled the field verification rules, artifact audits, and immediate walk-away red flags into a single engineering protocol:\n\n"
            "🔗 Full protocol & checklist: https://datacenterfieldguides.com/blog/data-center-facility-location-due-diligence\n\n"
            "#DataCenter #TechnicalDueDiligence #SiteSelection #CriticalInfrastructure #MissionCritical #GridInterconnection #Hyperscale"
        ),
    },
    {
        "id": "02-nvl72-liquid-load-bank",
        "slug": "nvl72-liquid-load-bank-testing-guide",
        "title": "Why You Cannot Test an NVIDIA GB200 NVL72 Loop with Air Heaters",
        "image": str(FIGURES_DIR / "fig-01-boundary-architecture.png"),
        "post_text": (
            "You cannot commission a 120 kW direct-to-chip liquid cooling manifold with a floor-standing resistive air heater.\n\n"
            "Yet on site after site, teams wheel 100 kW air load banks into a whitespace designed for high-density AI racks, heat up the room air, watch the CRAHs spin up, and sign off on 'Integrated Systems Testing.'\n\n"
            "Here is what an air load bank never tests on a liquid-cooled rack row:\n"
            "• Secondary fluid flow balance and differential pressure (ΔP) across parallel rack manifolds\n"
            "• CDU proportional control valve hunting during rapid 10% -> 100% -> 10% AI training step-load transients\n"
            "• Approach temperature stability across the CDU plate heat exchanger at peak design propylene glycol flow\n"
            "• Blind-mate quick-disconnect (QDC) thermal expansion seating under design supply temperature (Ts) and return ΔT\n\n"
            "If the thermal rejection path splits at the rack manifold, your commissioning boundary must split there too.\n\n"
            "🔗 Full commissioning boundary protocol: https://datacenterfieldguides.com/blog/nvl72-liquid-load-bank-testing-guide\n\n"
            "#DataCenter #LiquidCooling #NVL72 #Commissioning #AIClusters #MissionCritical #ThermalEngineering"
        ),
    },
    {
        "id": "03-technical-due-diligence",
        "slug": "data-center-technical-due-diligence-checklist",
        "title": "Data Center Technical Due Diligence: Nameplate Capacity vs. Usable IT Megawatts",
        "image": str(FIGURES_DIR / "fig-01-tdd-audit-framework-and-red-flags.png"),
        "post_text": (
            "In data center Technical Due Diligence (TDD), nameplate megawatts are fiction. Only synchronous, thermally rejected, N-1 surviving IT megawatts count.\n\n"
            "When auditing an existing colocation or hyperscale asset, a '20 MW facility' routinely shrinks to 13.5 MW of usable IT load once you trace the physical cascade:\n\n"
            "• Utility MV feeder thermal derating in underground duct banks\n"
            "• Diesel generator ambient/altitude derating and ISO-8528-1 step-load recovery limits\n"
            "• UPS output power factor (pf) and battery end-of-discharge (EOD) voltage sag at Year 4\n"
            "• Parasitic mechanical cooling load at the ASHRAE 20-year extreme wet-bulb temperature\n"
            "• Stranded whitespace power where cooling airflow cannot physically reach high-density racks\n\n"
            "Never underwrite a single-line diagram (SLD) without reconciling it against the Level 4/5 IST heat-rejection trend logs.\n\n"
            "🔗 Full TDD audit checklist & waterfall breakdown: https://datacenterfieldguides.com/blog/data-center-technical-due-diligence-checklist\n\n"
            "#DataCenter #TechnicalDueDiligence #InfrastructureInvesting #MissionCritical #MEP #PowerSystems"
        ),
    },
    {
        "id": "04-sop-mop-eop",
        "slug": "sop-mop-eop",
        "title": "SOP vs. MOP vs. EOP: Why Mixing Operating Procedures Causes Human-Error Outages",
        "image": str(FIGURES_DIR / "fig-02-sop-mop-eop-governance-pyramid.png"),
        "post_text": (
            "Most human-error outages in critical facilities happen because an engineer tried to improvise a back-out inside a procedure that never defined one.\n\n"
            "In data center operations, SOP, MOP, and EOP are not interchangeable paperwork—they govern three distinct plant states:\n\n"
            "1. SOP (Standard Operating Procedure): Steady-state, repeatable actions that do NOT alter redundancy or topology (e.g., shift rounds, reading logs).\n"
            "2. MOP (Method of Procedure): Step-by-step state-change scripts that intentionally alter redundancy (e.g., switching a UPS to maintenance bypass). Every MOP requires an explicit Point of No Return (PONR) and a pre-verified Back-Out section.\n"
            "3. EOP (Emergency Operating Procedure): Immediate reflex stabilization when an unscheduled fault occurs. No troubleshooting, no root-cause debate—just isolate and stabilize.\n\n"
            "When an MOP goes off-script, you do not 'troubleshoot on the fly.' You execute the MOP back-out—or, if plant limits are breached, transition immediately to the EOP.\n\n"
            "🔗 Full state-machine architecture & field rules: https://datacenterfieldguides.com/blog/sop-mop-eop\n\n"
            "#DataCenter #CriticalOperations #MOP #SOP #EOP #Uptime #FacilityManagement"
        ),
    },
    {
        "id": "05-commissioning-levels",
        "slug": "commissioning-levels-0-to-6",
        "title": "Data Center Commissioning Levels (L0 to L6): The Gate-Check Architecture",
        "image": str(FIGURES_DIR / "fig-levels.png"),
        "post_text": (
            "Running Level 5 Integrated Systems Testing (IST) before Level 3 startup and point-to-point verification are 100% closed is the fastest way to burn a commissioning schedule.\n\n"
            "Every open L2/L3 punch-list item carried into L5 IST turns an integrated facility blackout test into an expensive, multi-vendor troubleshooting session:\n\n"
            "• L0: Design & Coordination Review (breaker selectivity, protective relay settings)\n"
            "• L1: Factory Acceptance Testing (FAT at the manufacturer test bed)\n"
            "• L2: Site Delivery, Physical Installation & Torque/Megger Verification\n"
            "• L3: Pre-Functional Startup & 100% End-to-End BMS/EPMS Point Verification\n"
            "• L4: Functional Performance Testing (single-system full-load and component failure)\n"
            "• L5: Integrated Systems Testing (multi-system failure under 100% thermal + electrical load)\n\n"
            "A conditional signature at L3 is not progress—it is a hidden fault waiting for utility breaker pull day.\n\n"
            "🔗 Complete L0–L6 gate criteria: https://datacenterfieldguides.com/blog/commissioning-levels-0-to-6\n\n"
            "#DataCenter #Commissioning #IST #MissionCritical #DataCenterConstruction #MEP"
        ),
    },
    {
        "id": "06-corrosion-coupon-isa",
        "slug": "data-center-corrosion-coupon-isa-71-04-guide",
        "title": "Data Center Corrosion Coupon Testing: Why Copper Alone Misses Silver Sulfide Creep",
        "image": str(FIGURES_DIR / "fig-02-isa-71-04-severity-classification-matrix.png"),
        "post_text": (
            "A clean copper coupon does not clear a data center whitespace for ANSI/ISA-71.04 Severity Level G1.\n\n"
            "Since the RoHS lead-free transition, modern servers rely heavily on immersion silver (ImAg) surface finishes and miniature surface-mount resistors. Copper coupons are relatively insensitive to elemental sulfur (S8) and low-ppb hydrogen sulfide (H2S) spikes—the exact contaminants that drive silver sulfide (Ag2S) creep corrosion and dead motherboards.\n\n"
            "When auditing an air-side economizer or high-humidity facility:\n"
            "• Always deploy paired Copper (Cu) + Silver (Ag) coupons for a 30-day exposure window\n"
            "• Verify laboratory coulometric reduction separates Cu2S, Cu2O, Ag2S, and AgCl film thicknesses (Å / 30 days)\n"
            "• Place coupons at the CRAH supply discharge and cold-aisle rack inlets—not on the NOC wall\n"
            "• Include an unexposed field blank coupon from the same batch to catch transit contamination\n\n"
            "🔗 Full ANSI/ISA-71.04 field protocol: https://datacenterfieldguides.com/blog/data-center-corrosion-coupon-isa-71-04-guide\n\n"
            "#DataCenter #ASHRAE #ISA7104 #HardwareReliability #MissionCritical #AirQuality"
        ),
    },
    {
        "id": "07-alarm-suppression-handover",
        "slug": "data-center-alarm-suppression-and-handover-refusal",
        "title": "Data Center Alarm Suppression & Handover Refusal: When Operations Must Refuse the Keys",
        "image": str(FIGURES_DIR / "fig-01-handover-gatekeeper-architecture.png"),
        "post_text": (
            "A green BMS summary screen on handover day means nothing if 400 nuisance points are sitting in 'Shelved' or 'Out-of-Service' tables.\n\n"
            "Before the resident operations team signs the turnover certificate and accepts the keys from Construction/Commissioning, there are four non-negotiable audit gates:\n\n"
            "1. Zero Unaudited Shelved Alarms: Export the raw BMS/EPMS point database and filter for suppressed, overridden, or forced-manual points.\n"
            "2. Clock Synchronization Across Recorders: Verify NTP/PTP time alignment across PLC, BMS, and protective relays—if timestamps drift by 12 seconds, your first root-cause analysis (RCA) is already broken.\n"
            "3. As-Built Single-Line & Redline Accuracy: You cannot execute an emergency switching procedure using 'For Construction' drawings.\n"
            "4. Full L4/L5 IST Thermal & Electrical Proof: No 'commercial waivers' for untested redundancy paths.\n\n"
            "Once Operations signs, construction defects become operational incidents.\n\n"
            "🔗 Full handover refusal checklist: https://datacenterfieldguides.com/blog/data-center-alarm-suppression-and-handover-refusal\n\n"
            "#DataCenter #DataCenterOperations #BMS #EPMS #Handover #CriticalFacilities"
        ),
    },
]


def load_credentials():
    if not CRED_PATH.exists():
        return None
    with open(CRED_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_credentials(data):
    with open(CRED_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    CRED_PATH.chmod(0o600)


def api_json(token, method, url, body=None, extra_headers=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Restli-Protocol-Version": "2.0.0",
    }
    if extra_headers:
        headers.update(extra_headers)
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        raw = resp.read().decode("utf-8")
        resp_headers = dict(resp.info())
        return (json.loads(raw) if raw else {}), resp_headers


def get_author_urn(token, cred):
    if cred.get("author_urn"):
        return cred["author_urn"]
    # Try OpenID Connect /v2/userinfo first
    try:
        info, _ = api_json(token, "GET", "https://api.linkedin.com/v2/userinfo")
        sub = info.get("sub")
        if sub:
            urn = f"urn:li:person:{sub}"
            cred["author_urn"] = urn
            cred["profile_name"] = info.get("name", "")
            save_credentials(cred)
            return urn
    except Exception:
        pass
    # Fallback to /v2/me
    info, _ = api_json(token, "GET", "https://api.linkedin.com/v2/me")
    person_id = info.get("id")
    if not person_id:
        raise RuntimeError("Could not determine LinkedIn Person URN from /v2/userinfo or /v2/me.")
    urn = f"urn:li:person:{person_id}"
    cred["author_urn"] = urn
    save_credentials(cred)
    return urn


def upload_image(token, author_urn, image_path):
    """Registers an image upload with LinkedIn v2 assets API and uploads the binary PNG."""
    reg_body = {
        "registerUploadRequest": {
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
            "owner": author_urn,
            "serviceRelationships": [
                {
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent",
                }
            ],
        }
    }
    reg_resp, _ = api_json(
        token,
        "POST",
        "https://api.linkedin.com/v2/assets?action=registerUpload",
        reg_body,
    )
    val = reg_resp["value"]
    asset_urn = val["asset"]
    upload_url = val["uploadMechanism"][
        "com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"
    ]["uploadUrl"]

    with open(image_path, "rb") as f:
        img_bytes = f.read()

    put_req = urllib.request.Request(
        upload_url,
        data=img_bytes,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "image/png",
        },
        method="PUT",
    )
    with urllib.request.urlopen(put_req) as resp:
        resp.read()

    return asset_urn


def publish_post(token, author_urn, text, title, image_path=None):
    """Publishes a native LinkedIn feed post (with optional high-res engineering diagram)."""
    if image_path and Path(image_path).exists():
        print(f"[+] Uploading architectural diagram: {image_path} ...")
        asset_urn = upload_image(token, author_urn, image_path)
        print(f"[✓] Image uploaded -> {asset_urn}")
        share_content = {
            "shareCommentary": {"text": text},
            "shareMediaCategory": "IMAGE",
            "media": [
                {
                    "status": "READY",
                    "description": {"text": title},
                    "media": asset_urn,
                    "title": {"text": title},
                }
            ],
        }
    else:
        share_content = {
            "shareCommentary": {"text": text},
            "shareMediaCategory": "NONE",
        }

    body = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {"com.linkedin.ugc.ShareContent": share_content},
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    resp, headers = api_json(token, "POST", "https://api.linkedin.com/v2/ugcPosts", body)
    post_id = resp.get("id") or headers.get("x-restli-id") or headers.get("X-RestLi-Id")
    return post_id


def preview_queue():
    print("=" * 76)
    print("  LINKEDIN WAVE 1 CAMPAIGN QUEUE // 7 FLAGSHIP ENGINEERING POSTS")
    print("=" * 76)
    for idx, item in enumerate(WAVE_1_QUEUE, 1):
        img_ok = Path(item["image"]).exists()
        print(f"\n[{idx}] ID: {item['id']}")
        print(f"    Target URL : https://datacenterfieldguides.com/blog/{item['slug']}")
        print(f"    Diagram PNG: {Path(item['image']).name} ({'READY' if img_ok else 'MISSING'})")
        first_line = item["post_text"].splitlines()[0]
        print(f"    Hook       : {first_line[:85]}...")


def main():
    if "--list" in sys.argv or len(sys.argv) == 1:
        preview_queue()
        cred = load_credentials()
        if not cred or not cred.get("access_token"):
            print("\n[!] Status: Waiting for .linkedin-credentials.json (access_token).")
        else:
            print(f"\n[✓] Status: LinkedIn credentials loaded ({cred.get('profile_name', 'Ready')}).")
        return

    if "--verify" in sys.argv:
        cred = load_credentials()
        if not cred or not cred.get("access_token"):
            print("[!] Missing .linkedin-credentials.json")
            sys.exit(1)
        urn = get_author_urn(cred["access_token"], cred)
        print(f"[✓] LinkedIn API Authenticated! Author URN: {urn} (Name: {cred.get('profile_name')})")
        return

    if "--publish" in sys.argv:
        idx_arg = sys.argv[sys.argv.index("--publish") + 1]
        target = None
        for item in WAVE_1_QUEUE:
            if item["id"] == idx_arg or item["slug"] == idx_arg:
                target = item
                break
        if not target and idx_arg.isdigit():
            i = int(idx_arg) - 1
            if 0 <= i < len(WAVE_1_QUEUE):
                target = WAVE_1_QUEUE[i]
        if not target:
            print(f"[!] Could not find post matching '{idx_arg}'")
            sys.exit(1)

        cred = load_credentials()
        if not cred or not cred.get("access_token"):
            print("[!] Missing .linkedin-credentials.json")
            sys.exit(1)

        token = cred["access_token"]
        urn = get_author_urn(token, cred)
        print(f"[+] Publishing '{target['title']}' as {urn} ...")
        post_id = publish_post(token, urn, target["post_text"], target["title"], target["image"])
        print(f"[✓] Successfully published to LinkedIn! Post URN: {post_id}")
        print(f"    View post: https://www.linkedin.com/feed/update/{post_id}/")


if __name__ == "__main__":
    main()
