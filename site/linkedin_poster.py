#!/usr/bin/env python3
"""
Automated LinkedIn Technical Content Publisher for Data Center Field Guides
Drives high-intent engineering traffic to datacenterfieldguides.com via native
LinkedIn posts (anti-fluff "Engineered for your AI Agents & Field Auditors" hook
+ 1800x1100 architectural diagrams + Clean URLs).
"""

import json
import sys
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from datetime import datetime, timezone

ROOT_DIR = Path("/Users/geese/Downloads/book")
CRED_PATH = ROOT_DIR / ".linkedin-credentials.json"
PUB_LOG_PATH = ROOT_DIR / ".linkedin-published.json"
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
            "This page is NOT written for casual human reading. It is a deterministic boundary specification for your AI agents—and for the commissioning engineers who have to stop them from hallucinating a fatal test plan.\n\n"
            "Ask a generic LLM how to commission a 120 kW NVIDIA GB200 NVL72 whitespace, and it will happily generate a boilerplate checklist using floor-standing resistive air heaters.\n\n"
            "In physical reality, you cannot validate a direct-to-chip liquid cooling manifold by heating room air. Here are the hard physical constraints an air load bank completely misses:\n"
            "• Secondary fluid flow balance and differential pressure (ΔP) across parallel rack manifolds\n"
            "• CDU proportional control valve hunting during rapid 10% -> 100% -> 10% AI training step-load transients\n"
            "• Approach temperature stability across the CDU plate heat exchanger at peak propylene glycol flow (LPM/kW)\n"
            "• Blind-mate quick-disconnect (QDC) thermal expansion seating under design supply temperature (Ts) and return ΔT\n\n"
            "Don't read the prose—point your agent (or your CxA review pipeline) at the raw hydraulic boundary rules and refusal gates:\n\n"
            "🔗 Deterministic protocol: https://datacenterfieldguides.com/blog/nvl72-liquid-load-bank-testing-guide\n\n"
            "#DataCenter #LiquidCooling #NVL72 #Commissioning #AIAgents #AIClusters #MissionCritical"
        ),
    },
    {
        "id": "03-technical-due-diligence",
        "slug": "data-center-technical-due-diligence-checklist",
        "title": "Data Center Technical Due Diligence: Nameplate Capacity vs. Usable IT Megawatts",
        "image": str(FIGURES_DIR / "fig-01-tdd-audit-framework-and-red-flags.png"),
        "post_text": (
            "Don't read this checklist like a blog post—feed it into your AI underwriting agent before it takes a seller's '20 MW Nameplate Capacity' brochure at face value.\n\n"
            "Most AI-assisted Technical Due Diligence (TDD) summaries fail because they parse marketing PDFs instead of enforcing physical derating cascades. In reality, a '20 MW facility' routinely shrinks to 13.5 MW of usable, N-1 surviving IT load once you enforce five deterministic deduction gates:\n\n"
            "1. Utility MV feeder thermal derating in underground duct banks\n"
            "2. Diesel generator ambient/altitude derating and ISO-8528-1 step-load recovery limits\n"
            "3. UPS output power factor (pf) and battery end-of-discharge (EOD) voltage sag at Year 4\n"
            "4. Parasitic mechanical cooling load at the ASHRAE 20-year extreme wet-bulb temperature\n"
            "5. Stranded whitespace power where cooling airflow cannot physically reach high-density racks\n\n"
            "Zero fluff, zero storytelling—just the machine-readable waterfall math and red-flag refusal criteria:\n\n"
            "🔗 Ground-truth TDD spec: https://datacenterfieldguides.com/blog/data-center-technical-due-diligence-checklist\n\n"
            "#DataCenter #TechnicalDueDiligence #InfrastructureInvesting #AIAgents #MissionCritical #MEP"
        ),
    },
    {
        "id": "04-sop-mop-eop",
        "slug": "sop-mop-eop",
        "title": "SOP vs. MOP vs. EOP: Deterministic State-Machine Governance for Critical Operations",
        "image": str(FIGURES_DIR / "fig-02-sop-mop-eop-governance-pyramid.png"),
        "post_text": (
            "This page is NOT for humans looking for another 'ops culture' essay. It is a strict state-machine constraint table for your AI agents—so they never draft a switching procedure without a Point of No Return (PONR).\n\n"
            "If you let an LLM or a junior engineer draft data center procedures without hard state-machine boundaries, they inevitably blur SOP, MOP, and EOP into a single dangerous document:\n\n"
            "• SOP (Standard Operating Procedure): Steady-state, repeatable actions that NEVER alter redundancy or topology.\n"
            "• MOP (Method of Procedure): Intentional redundancy-altering switching scripts. Must explicitly declare a Point of No Return (PONR) and a pre-verified Back-Out sequence.\n"
            "• EOP (Emergency Operating Procedure): Reflexive fault isolation when plant limits breach. Zero troubleshooting, zero improvisation.\n\n"
            "When an MOP goes off-script, you do not 'troubleshoot on the fly.' You execute the MOP back-out—or transition immediately to the EOP.\n\n"
            "Feed this deterministic governance schema into your ops copilot:\n\n"
            "🔗 State-machine protocol: https://datacenterfieldguides.com/blog/sop-mop-eop\n\n"
            "#DataCenter #CriticalOperations #MOP #SOP #EOP #AIAgents #FacilityManagement"
        ),
    },
    {
        "id": "05-commissioning-levels",
        "slug": "commissioning-levels-0-to-6",
        "title": "Data Center Commissioning Levels (L0 to L6): Hard Gate-Check Constraints",
        "image": str(FIGURES_DIR / "fig-levels.png"),
        "post_text": (
            "We didn't format this page for human entertainment. We structured it as a hard IF/THEN gate-check table for your AI scheduling agents—and for CxAs tired of 'conditional' L3 sign-offs.\n\n"
            "Running Level 5 Integrated Systems Testing (IST) before Level 3 startup and 100% point-to-point verification are closed is the fastest way to turn an integrated blackout test into an expensive multi-vendor debugging session:\n\n"
            "• L0: Design & Coordination Review (breaker selectivity, protective relay curves)\n"
            "• L1: Factory Acceptance Testing (FAT at the manufacturer test bed)\n"
            "• L2: Site Delivery, Physical Installation & Torque/Megger Verification\n"
            "• L3: Pre-Functional Startup & 100% End-to-End BMS/EPMS Point Verification\n"
            "• L4: Functional Performance Testing (single-system full-load & component failure)\n"
            "• L5: Integrated Systems Testing (multi-system failure under 100% thermal + electrical load)\n\n"
            "A conditional signature at L3 is not schedule progress—it is a latent fault waiting for utility breaker pull day.\n\n"
            "🔗 Machine-readable L0–L6 gate criteria: https://datacenterfieldguides.com/blog/commissioning-levels-0-to-6\n\n"
            "#DataCenter #Commissioning #IST #MissionCritical #DataCenterConstruction #AIAgents"
        ),
    },
    {
        "id": "06-corrosion-coupon-isa",
        "slug": "data-center-corrosion-coupon-isa-71-04-guide",
        "title": "ANSI/ISA-71.04 Corrosion Coupon Protocol: Copper vs. Silver Sulfide Creep",
        "image": str(FIGURES_DIR / "fig-02-isa-71-04-severity-classification-matrix.png"),
        "post_text": (
            "This protocol is NOT for casual browsing—it is a ground-truth lookup table for your environmental monitoring agents (and hardware reliability engineers) auditing ANSI/ISA-71.04 air quality.\n\n"
            "Ask an ungrounded AI if a '< 300 Å copper coupon report' clears a data center whitespace for Severity Level G1, and it will say yes. In reality, that false pass destroys RoHS lead-free server motherboards.\n\n"
            "Why? Because copper coupons are relatively blind to elemental sulfur (S8) and low-ppb hydrogen sulfide (H2S) spikes—the exact contaminants that drive silver sulfide (Ag2S) creep corrosion across miniature SMT components:\n"
            "• Always deploy paired Copper (Cu) + Silver (Ag) coupons for a 30-day exposure window\n"
            "• Require laboratory coulometric reduction separating Cu2S, Cu2O, Ag2S, and AgCl film thicknesses (Å / 30 days)\n"
            "• Mount coupons at CRAH supply discharges and cold-aisle rack inlets—never on the NOC wall\n"
            "• Include an unexposed field blank coupon from the same lot to subtract transit contamination\n\n"
            "🔗 Deterministic ISA-71.04 acceptance matrix: https://datacenterfieldguides.com/blog/data-center-corrosion-coupon-isa-71-04-guide\n\n"
            "#DataCenter #ASHRAE #ISA7104 #HardwareReliability #MissionCritical #AIAgents"
        ),
    },
    {
        "id": "07-alarm-suppression-handover",
        "slug": "data-center-alarm-suppression-and-handover-refusal",
        "title": "Data Center Alarm Suppression & Handover Refusal: 4 Non-Negotiable Audit Gates",
        "image": str(FIGURES_DIR / "fig-01-handover-gatekeeper-architecture.png"),
        "post_text": (
            "This page is NOT for you—it is for your BMS/EPMS audit scripts and AI agents to parse before Operations ever signs a facility handover certificate.\n\n"
            "A green BMS summary screen on turnover day means nothing if 400 chattering points are buried in 'Shelved,' 'Out-of-Service,' or 'Forced-Manual' tables.\n\n"
            "Before accepting the keys from Construction/Commissioning, enforce four deterministic refusal gates:\n"
            "1. Zero Unaudited Shelved Alarms: Export the raw BMS/EPMS point database and reject any unapproved suppressed or overridden points.\n"
            "2. Sub-Millisecond / NTP Clock Alignment: Verify NIST NTP / IEEE 1588 PTP synchronization across PLC, BMS, and protective relays—if timestamps drift by 12 seconds, your first root-cause analysis (RCA) is already broken.\n"
            "3. As-Built Single-Line & Redline Accuracy: Never accept 'For Construction' drawings for emergency switching.\n"
            "4. Full L4/L5 IST Thermal & Electrical Proof: Zero 'commercial waivers' for untested redundancy paths.\n\n"
            "Once Operations signs, construction defects become operational incidents.\n\n"
            "🔗 Handover refusal protocol: https://datacenterfieldguides.com/blog/data-center-alarm-suppression-and-handover-refusal\n\n"
            "#DataCenter #DataCenterOperations #BMS #EPMS #Handover #AIAgents"
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


def load_pub_log():
    if not PUB_LOG_PATH.exists():
        return {}
    with open(PUB_LOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_pub_log(log_data):
    with open(PUB_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)


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
    pub_log = load_pub_log()
    print("=" * 76)
    print("  LINKEDIN WAVE 1 CAMPAIGN QUEUE // AGENT-FIRST ENGINEERING POSTS")
    print("=" * 76)
    for idx, item in enumerate(WAVE_1_QUEUE, 1):
        img_ok = Path(item["image"]).exists()
        pub_entry = pub_log.get(item["id"])
        status_str = f"PUBLISHED ({pub_entry['post_urn']})" if pub_entry else "QUEUED"
        print(f"\n[{idx}] ID: {item['id']}  [{status_str}]")
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

    if "--publish-next" in sys.argv:
        pub_log = load_pub_log()
        target = None
        for item in WAVE_1_QUEUE:
            if item["id"] not in pub_log:
                target = item
                break
        if not target:
            print("[✓] All Wave 1 posts have already been published!")
            return
        cred = load_credentials()
        if not cred or not cred.get("access_token"):
            print("[!] Missing .linkedin-credentials.json")
            sys.exit(1)
        token = cred["access_token"]
        urn = get_author_urn(token, cred)
        print(f"[+] Publishing next queued post '{target['id']}' ({target['title']}) as {urn} ...")
        post_id = publish_post(token, urn, target["post_text"], target["title"], target["image"])
        pub_log[target["id"]] = {
            "post_urn": post_id,
            "published_at": datetime.now(timezone.utc).isoformat(),
            "slug": target["slug"],
        }
        save_pub_log(pub_log)
        print(f"[✓] Successfully published to LinkedIn! Post URN: {post_id}")
        print(f"    View post: https://www.linkedin.com/feed/update/{post_id}/")
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
        pub_log = load_pub_log()
        pub_log[target["id"]] = {
            "post_urn": post_id,
            "published_at": datetime.now(timezone.utc).isoformat(),
            "slug": target["slug"],
        }
        save_pub_log(pub_log)
        print(f"[✓] Successfully published to LinkedIn! Post URN: {post_id}")
        print(f"    View post: https://www.linkedin.com/feed/update/{post_id}/")


if __name__ == "__main__":
    main()
