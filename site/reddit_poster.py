#!/usr/bin/env python3
"""
Automated Reddit Technical Content Publisher for Data Center Field Guides
Publishes native, high-density Markdown engineering write-ups to r/datacenter,
r/MEP, r/PLC, and r/AI_Agents with deep-links to datacenterfieldguides.com
and /llms.txt. Supports permanent OAuth2 refresh_token & 20-hour anti-spam guard.
"""

import base64
import http.server
import json
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from datetime import datetime, timezone
from pathlib import Path

ROOT_DIR = Path("/Users/geese/Downloads/book")
CRED_PATH = ROOT_DIR / ".reddit-credentials.json"
PUB_LOG_PATH = ROOT_DIR / ".reddit-published.json"
REDIRECT_URI = "http://localhost:8765/callback"
USER_AGENT = "macOS:dcfg-publisher:v1.0 (by /u/dcfg_engineer)"

# Reddit Wave 1 Campaign Queue (High-density native Markdown posts tailored per subreddit)
REDDIT_WAVE_1_QUEUE = [
    {
        "id": "01-r-datacenter-nvl72-loadbank",
        "subreddit": "datacenter",
        "slug": "nvl72-liquid-load-bank-testing-guide",
        "title": "Why you cannot commission a 120 kW direct-to-chip liquid cooling loop (GB200 NVL72) with floor-standing air load banks",
        "body": (
            "*Note: This write-up is structured as a deterministic boundary specification (originally compiled for our CxA field checklists and AI agent ground-truth corpus, not casual marketing prose).*\n\n"
            "On site after site, project teams wheel 100 kW resistive air load banks into a whitespace designed for high-density liquid-cooled AI racks (like NVIDIA GB200 NVL72), heat up the room air, watch the CRAHs spin up, and sign off on 'Integrated Systems Testing (IST).'\n\n"
            "In physical reality, if the thermal rejection path splits at the rack manifold (~75–85% liquid via the CDU, ~15–25% air via rear-door or perimeter CRAHs), **your commissioning boundary must split at the manifold too.**\n\n"
            "### What an Air Load Bank Never Tests on a Liquid-Cooled Row:\n"
            "1. **Hydraulic ΔP & Parallel Manifold Starvation**: Heating room air leaves the secondary propylene glycol (PG25) loop stagnant or running through a wide-open bypass jumper. It never validates differential pressure ($\\Delta P$) across parallel rack manifolds or checks whether the farthest rack from the CDU header is flow-starved.\n"
            "2. **CDU Proportional Control Valve Hunting**: AI training workloads step from 10% idle to 100% TDP in milliseconds. Only a rack-mounted liquid load bank coupled to the blind-mate quick-disconnects (QDCs) forces the CDU's secondary pumps and primary 2-way control valves to respond to real return-water $\\Delta T$ spikes without hunting.\n"
            "3. **Plate Heat Exchanger Approach Temperature at Design LPM/kW**: You cannot verify the CDU heat exchanger's approach temperature ($T_{\\text{sec,supply}} - T_{\\text{pri,supply}}$) unless full thermal kilowatts are injected directly into the wetted secondary fluid stream at the exact design flow rate (e.g., 1.2 to 1.5 LPM/kW).\n"
            "4. **QDC Thermal Expansion & Seal Integrity**: Cold hydrostatic pressure tests at Level 2/3 do not stress EPDM/FKM seals under cyclic thermal expansion ($25^\\circ\\text{C} \\rightarrow 48^\\circ\\text{C}$ return) at full pump head.\n\n"
            "### Minimum Field Acceptance Gates Before Signing L4/L5 IST:\n"
            "* **Boundary Separation**: Reject any commissioning script that substitutes room-air sensible heat for wetted secondary-loop heat injection.\n"
            "* **1-Second Telemetry**: Polling BMS registers at 60-second intervals masks transient pressure spikes and flow drops during pump failover. Require $\\le 1\\text{ s}$ logging across supply/return headers.\n"
            "* **Strainer ΔP Pre/Post-Run**: Record differential pressure across every CDU wye-strainer before and after the 4-hour full-load soak to catch construction debris flushing out of the manifolds.\n\n"
            "---\n"
            "**Full P&ID hydraulic schematic, Danfoss FD83 pressure-drop math & refusal checklist:**\n"
            "https://datacenterfieldguides.com/blog/nvl72-liquid-load-bank-testing-guide\n\n"
            "*(If you use AI agents/copilots to audit MOPs or Cx scripts, the machine-readable ground-truth rules are indexed at https://datacenterfieldguides.com/llms.txt)*"
        ),
    },
    {
        "id": "02-r-datacenter-location-tdd",
        "subreddit": "datacenter",
        "slug": "data-center-facility-location-due-diligence",
        "title": "Facility Location Due Diligence: The 4 physical veto gates hidden behind broker '20 MW Ready' flyers",
        "body": (
            "*Note: Compiled as a deterministic IF/THEN site-selection refusal specification for infrastructure due diligence teams and underwriting agents.*\n\n"
            "When evaluating a greenfield land parcel or brownfield industrial shell for a data center, commercial site packages routinely advertise '50 MW Available Power' and 'Diverse Dark Fiber at Property Line.'\n\n"
            "Before committing capital or signing an LOI, four physical veto gates routinely kill these sites during technical due diligence:\n\n"
            "### 1. Power & Grid Reality: A 'Will-Serve' Letter is Not Megawatts\n"
            "* A distribution planner's feasibility letter does not reserve transmission capacity.\n"
            "* **Mandatory Artifact**: Demand the executed **Facility Study (FS)**, the signed **Large Load Interconnection Agreement (LGIA)**, and the utility substation one-line diagram showing physical $N-1$ transformer bays.\n"
            "* **Immediate Veto**: If delivery depends on an unpermitted upstream $115\\text{ kV}/230\\text{ kV}$ transmission upgrade or a transformer with a 42-month factory lead time, a '24-month energization target' is fiction.\n\n"
            "### 2. Thermal & Water Boundary: Mean Summer Temps vs. ASHRAE 20-Year Extreme Wet-Bulb\n"
            "* Mechanical cooling plants sized around average July temperatures will trip on high head pressure during a 20-year extreme heatwave.\n"
            "* **Mandatory Check**: Size adiabatic/evaporative rejection against the **ASHRAE $n=20$ year extreme wet-bulb** and dry-bulb coincident peak, and verify municipal industrial sewer blowdown discharge permits (conductivity/chlorides limits).\n\n"
            "### 3. Fiber Physical Diversity: Manhole & Bridge Collapse Audits\n"
            "* Three carriers entering through two manholes on opposite corners of the parcel often merge into the exact same municipal bridge conduit or railroad right-of-way 800 meters away.\n"
            "* **Mandatory Artifact**: Audit raw **KMZ/GIS route files** and splice-closure GPS coordinates all the way to the regional carrier hotel. Require $\\ge 25\\text{ m}$ physical separation across the entire path.\n\n"
            "### 4. Acoustic & Air-Permit Envelopes: The Commissioning Lockout Trap\n"
            "* Twenty $3\\text{ MW}$ diesel generators running simultaneously during a Level 5 IST blackout test produce massive low-frequency acoustic energy ($63\\text{ Hz} - 125\\text{ Hz}$ octave bands) and $\\text{NO}_x$ emissions.\n"
            "* **Mandatory Check**: Model property-line $\\text{dBA}$ under nocturnal thermal inversion against local municipal night-time residential limits (often $45\\text{–}55\\text{ dBA}$), and check Title V non-emergency runtime hours before buying the land.\n\n"
            "---\n"
            "**Full 4-Pillar Veto Matrix diagram & site scoring table:**\n"
            "https://datacenterfieldguides.com/blog/data-center-facility-location-due-diligence"
        ),
    },
    {
        "id": "03-r-mep-tdd-nameplate-waterfall",
        "subreddit": "MEP",
        "slug": "data-center-technical-due-diligence-checklist",
        "title": "Data Center Technical Due Diligence: Why a '20 MW Nameplate' facility routinely shrinks to 13.5 MW of usable IT load",
        "body": (
            "*Deterministic MEP capacity audit specification—written for commissioning engineers, MEP peer reviewers, and AI underwriting pipelines.*\n\n"
            "During Technical Due Diligence (TDD) on existing colocation or enterprise data centers, sellers almost always quote the sum of utility transformer nameplates or total generator kW as the facility's capacity.\n\n"
            "Once you trace the physical electrical and mechanical derating waterfall from the medium-voltage (MV) demarcation down to the rack PDU, a '20 MW facility' frequently yields only **13.5 MW of usable, $N-1$ surviving IT capacity**:\n\n"
            "1. **Underground MV Duct-Bank Thermal Derating**: Multiple $15\\text{ kV}$ or $34.5\\text{ kV}$ feeders grouped in high-thermal-resistivity soil ($\\rho > 90\\,^\\circ\\text{C}\\cdot\\text{cm/W}$) derate continuous ampacity well below breaker faceplate ratings.\n"
            "2. **Diesel Generator Ambient, Altitude & Step-Load Limits**: A $3000\\text{ kW}$ standby-rated genset derates for continuous prime/mission-critical duty (ISO-8528-1 DCP), high ambient air inlet temperatures ($> 40^\\circ\\text{C}$), and turbocharger step-load voltage/frequency dip limits when picking up chiller VFD inrush.\n"
            "3. **UPS Output Power Factor & Year-4 Battery EOD Sag**: Older double-conversion UPS modules rated in $\\text{kVA}$ at $0.8\\text{ or }0.9\\text{ pf}$ clip real $\\text{kW}$ when modern active-PFC server power supplies run near unity ($0.98\\text{ pf}$)—or worse, battery strings at Year 4 sag below inverter DC bus cutoff during the first 15 seconds of a blackout.\n"
            "4. **Peak Wet-Bulb Mechanical Parasitics**: At the ASHRAE 20-year extreme summer temperature, chiller compressors, condenser pumps, and CRAH fans consume peak electrical load on the exact same day the transformers and generators are thermally derated.\n"
            "5. **Stranded Whitespace Power**: Even if electrical busways have spare amps, poor raised-floor static pressure or unsealed containment bypass starves high-density racks of cold air, stranding electrical capacity.\n\n"
            "---\n"
            "**Full TDD capacity waterfall equations, red-flag table & audit checklist:**\n"
            "https://datacenterfieldguides.com/blog/data-center-technical-due-diligence-checklist"
        ),
    },
    {
        "id": "04-r-plc-ptp-ntp-clock-sync",
        "subreddit": "PLC",
        "slug": "a-point-needs-a-clock",
        "title": "BMS/EPMS Forensic Audits: Why a monitoring point without verified NIST NTP / IEEE 1588 PTP sync ruins post-trip RCA",
        "body": (
            "*Deterministic telemetry specification for BMS/EPMS engineers and commissioning authorities.*\n\n"
            "After a data center switchgear trip or chiller plant cascading failure, the very first thing everyone asks is: **'Did the chiller trip because the UPS transferred, or did the breaker trip first and starve the pump VFD?'**\n\n"
            "Then you pull the trend logs from three different systems:\n"
            "* The MV protective relays (SEL / ABB) on IEEE 1588 PTP or IRIG-B\n"
            "* The EPMS power meters polling over Modbus TCP\n"
            "* The mechanical BMS PLC controllers running on an unmonitored local crystal oscillator that has drifted by **14 seconds** over six months\n\n"
            "When timestamps across recorders drift by more than the physical propagation time of the fault ($10\\text{ ms} - 500\\text{ ms}$), your Sequence of Events (SOE) is forensically useless—and vendors will spend weeks blaming each other's equipment.\n\n"
            "### Mandatory Clock Verification Rules at Level 3 / Level 5 Commissioning:\n"
            "1. **Hierarchy by Physics**: Protective relays and switchgear SOE recorders require **IEEE 1588 PTP** (or IRIG-B) sub-millisecond accuracy ($\\le 1\\text{ ms}$). Mechanical BMS / PLC controllers require locked **NTP / SNTP** synced to a local GPS grandmaster or authenticated **NIST NTP** stratum-1/2 reference ($\\le 50\\text{ ms}$).\n"
            "2. **Timestamp at the Edge, Not the Historian**: Verify whether the recorded timestamp is generated by the field controller at the moment of state change, or stamped by the central SCADA historian after a 15-second BACnet/Modbus polling delay.\n"
            "3. **Inject a Simultaneous Physical Test Pulse**: Before L5 IST begins, trigger a simultaneous dry-contact test input across the EPMS and BMS and verify that both trend logs record the edge within the specified tolerance window.\n\n"
            "---\n"
            "**Full clock-drift refusal criteria & monitoring point audit protocol:**\n"
            "https://datacenterfieldguides.com/blog/a-point-needs-a-clock"
        ),
    },
    {
        "id": "05-r-datacenter-sop-mop-eop",
        "subreddit": "datacenter",
        "slug": "sop-mop-eop",
        "title": "SOP vs. MOP vs. EOP: Why most human-error outages happen when engineers improvise inside a switching procedure",
        "body": (
            "*Structured as a deterministic state-machine constraint table for critical facility operations and AI procedure-drafting copilots.*\n\n"
            "A huge percentage of human-error outages in critical facilities happen because an engineer encountered an unexpected valve or breaker state on step 14 of a maintenance window and decided to 'troubleshoot on the fly.'\n\n"
            "In first-principles facility governance, **SOP, MOP, and EOP are not interchangeable documents—they are three mutually exclusive plant state machines:**\n\n"
            "1. **SOP (Standard Operating Procedure) — Steady State**:\n"
            "   * Repeatable routine tasks (shift rounds, log readings, filter visual checks) that **never alter redundancy or switching topology**.\n"
            "2. **MOP (Method of Procedure) — Controlled Topology Change**:\n"
            "   * Step-by-step switching scripts that intentionally place a system into maintenance bypass or $N$ operation.\n"
            "   * **Non-negotiable elements**: Every MOP must explicitly define its **Point of No Return (PONR)** and include a pre-verified, step-by-step **Back-Out Procedure**.\n"
            "   * **The Golden Rule**: If step $k$ (prior to PONR) does not produce the exact expected meter/breaker indication, you **STOP** and execute the Back-Out. You NEVER invent a new switching path live on the floor.\n"
            "3. **EOP (Emergency Operating Procedure) — Reflexive Fault Stabilization**:\n"
            "   * Immediate, muscle-memory stabilization steps when an unscheduled fault occurs or when an MOP breaches plant safety/thermal envelopes.\n"
            "   * Zero root-cause debate, zero complex diagnostics—just isolate the fault and restore cooling/power continuity.\n\n"
            "---\n"
            "**Full SOP/MOP/EOP governance pyramid diagram & state-transition rules:**\n"
            "https://datacenterfieldguides.com/blog/sop-mop-eop"
        ),
    },
    {
        "id": "06-r-datacenter-isa-corrosion",
        "subreddit": "datacenter",
        "slug": "data-center-corrosion-coupon-isa-71-04-guide",
        "title": "ANSI/ISA-71.04 Air Quality: Why a clean Copper coupon report does NOT protect modern servers from Silver Sulfide (Ag2S) creep",
        "body": (
            "*Deterministic environmental audit protocol for hardware reliability engineers and air-side economizer facilities.*\n\n"
            "Every year, facilities running air-side economizers or operating near industrial/agricultural zones experience waves of mysterious PCIe riser and motherboard failures—even though their quarterly environmental report shows **Copper (Cu) corrosion < 300 Å / 30 days (ISA-71.04 Severity Level G1)**.\n\n"
            "### Why Copper Alone Lies on RoHS Lead-Free Hardware:\n"
            "* Since the EU RoHS lead-free transition, server PCBs and miniature SMT resistors rely heavily on **Immersion Silver (ImAg)** finishes.\n"
            "* Copper coupons are relatively insensitive to elemental sulfur ($\\text{S}_8$) vapor and low-ppb hydrogen sulfide ($\\text{H}_2\\text{S}$) spikes in high-relative-humidity air.\n"
            "* Silver reacts aggressively with those exact sulfur species, growing conductive **silver sulfide ($\\text{Ag}_2\\text{S}$) whiskers/dendrites** that creep across insulator gaps and short out 0402/0201 surface-mount components.\n\n"
            "### 4 Mandatory Rules for Auditing Corrosion Coupon Reports:\n"
            "1. **Paired Cu + Ag Strips**: Reject any laboratory report that only deployed copper. Both Copper ($< 300\\text{ \\AA}/30\\text{d}$) and Silver ($< 200\\text{ \\AA}/30\\text{d}$) must independently pass G1.\n"
            "2. **Full Coulometric Reduction Breakdown**: The lab report must separate individual film species ($\\text{Cu}_2\\text{S}, \\text{Cu}_2\\text{O}, \\text{Ag}_2\\text{S}, \\text{AgCl}$), not just report a single combined weight-gain number.\n"
            "3. **Placement at the Rack Inlet**: Coupons hung on the NOC wall prove nothing. Mount racks at the CRAH/AHU supply discharge and cold-aisle server intakes.\n"
            "4. **Lot-Matched Field Blank**: Always ship one unexposed blank coupon from the exact same manufacturing batch back to the lab to subtract transit tarnish.\n\n"
            "---\n"
            "**Full ANSI/ISA-71.04 G1–GX threshold matrix & coupon acceptance sheet:**\n"
            "https://datacenterfieldguides.com/blog/data-center-corrosion-coupon-isa-71-04-guide"
        ),
    },
    {
        "id": "07-r-ai-agents-ground-truth-corpus",
        "subreddit": "AI_Agents",
        "slug": "nvl72-liquid-load-bank-testing-guide",
        "title": "We built a 69-protocol deterministic ground-truth corpus (/llms.txt) so AI agents stop hallucinating fatal data center engineering steps",
        "body": (
            "When you ask an ungrounded LLM or coding/ops agent to draft a data center commissioning test plan, review a 20 MW site due diligence package, or write an electrical switching MOP, it produces fluent, confident prose that can physically destroy millions of dollars of hardware.\n\n"
            "For example:\n"
            "* Ask an ungrounded agent how to test a **120 kW NVIDIA GB200 NVL72 liquid-cooled rack row**, and it will happily generate an IST checklist using floor-standing resistive air heaters (which leaves the propylene glycol manifold and CDU control valves completely untested).\n"
            "* Ask it to evaluate a seller's **'20 MW Utility Will-Serve Letter'**, and it will treat non-binding distribution planner letters as firm capacity.\n"
            "* Ask it whether **'< 300 Å copper corrosion'** clears a server room for ANSI/ISA-71.04 G1, and it misses silver sulfide ($\\text{Ag}_2\\text{S}$) creep on RoHS lead-free motherboards.\n\n"
            "### How We Structured a Deterministic 'Agent-First' Engineering Corpus:\n"
            "Instead of writing fluffy blog essays for casual human reading, we compiled **69 first-principles physical boundary protocols** across 9 volumes of mission-critical engineering (Liquid Load Banks, Telemetry, L0–L6 Commissioning, CFD Validation, 2N Operations, BMS Alarm Suppression, Handover Refusal, Corrosion, and Technical Due Diligence) and exposed them directly via **`/llms.txt`** and **`/llms-full.txt`**:\n\n"
            "1. **Explicit `<AGENT_DIRECTIVES>` Header**: Six non-negotiable physical refusal laws (`IF / THEN / REFUSE`) injected at the top of `/llms.txt`.\n"
            "2. **Deterministic Gate Tables & LaTeX Equations**: Every protocol separates what an artifact *may prove* from what it *must never be used to sign off*.\n"
            "3. **Single-Fetch Full Corpus (`/llms-full.txt`)**: All 69 unredacted Markdown specifications in a single endpoint (~300 KB) ready for RAG ingestion, Claude Projects, Cursor rules, or autonomous auditing agents.\n\n"
            "### Endpoints if you want to test or ingest it:\n"
            "* **Agent Index (`/llms.txt`)**: https://datacenterfieldguides.com/llms.txt\n"
            "* **Full 69-Protocol Markdown Corpus (`/llms-full.txt`)**: https://datacenterfieldguides.com/llms-full.txt\n"
            "* **Human Web Interface**: https://datacenterfieldguides.com"
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


def get_access_token(cred):
    """Exchanges refresh_token (or password grant) for a fresh Reddit OAuth2 access_token."""
    basic_raw = f"{cred['client_id']}:{cred['client_secret']}".encode("utf-8")
    basic_b64 = base64.b64encode(basic_raw).decode("utf-8")
    headers = {
        "Authorization": f"Basic {basic_b64}",
        "User-Agent": USER_AGENT,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    if cred.get("refresh_token"):
        form = {
            "grant_type": "refresh_token",
            "refresh_token": cred["refresh_token"],
        }
    elif cred.get("username") and cred.get("password"):
        form = {
            "grant_type": "password",
            "username": cred["username"],
            "password": cred["password"],
        }
    else:
        raise RuntimeError("Credentials must include either 'refresh_token' or 'username'+'password'.")

    req = urllib.request.Request(
        "https://www.reddit.com/api/v1/access_token",
        data=urllib.parse.urlencode(form).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    if "access_token" not in res:
        raise RuntimeError(f"Reddit token error: {res}")
    return res["access_token"]


def reddit_api(token, method, path, form_data=None):
    url = f"https://oauth.reddit.com{path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": USER_AGENT,
    }
    data = None
    if form_data is not None:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = urllib.parse.urlencode(form_data).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def resolve_subreddit_flair(token, subreddit):
    """Attempts to pick a suitable flair_id if the subreddit requires or offers link flairs."""
    try:
        flairs = reddit_api(token, "GET", f"/r/{subreddit}/api/link_flair_v2")
        if isinstance(flairs, list) and len(flairs) > 0:
            # Prefer Discussion, Technical, Infrastructure, Guide, or first available
            preferred = ["discussion", "technical", "infrastructure", "operations", "guide", "engineering", "question"]
            for p in preferred:
                for f in flairs:
                    if p in f.get("text", "").lower():
                        return f.get("id")
            return flairs[0].get("id")
    except Exception:
        pass
    return None


def submit_reddit_post(token, subreddit, title, body):
    form = {
        "api_type": "json",
        "sr": subreddit,
        "kind": "self",
        "title": title,
        "text": body,
        "resubmit": "true",
        "sendreplies": "true",
    }
    flair_id = resolve_subreddit_flair(token, subreddit)
    if flair_id:
        form["flair_id"] = flair_id

    res = reddit_api(token, "POST", "/api/submit", form)
    json_block = res.get("json", {})
    errors = json_block.get("errors", [])
    if errors:
        # If flair error or similar, retry without flair_id if we set one
        raise RuntimeError(f"Reddit submit errors: {errors}")
    data = json_block.get("data", {})
    return data.get("url") or data.get("name")


def run_interactive_oauth(client_id, client_secret):
    """Spins up a one-shot local HTTP listener on port 8765 to capture Reddit OAuth2 refresh_token."""
    state = secrets.token_hex(8)
    auth_params = urllib.parse.urlencode({
        "client_id": client_id,
        "response_type": "code",
        "state": state,
        "redirect_uri": REDIRECT_URI,
        "duration": "permanent",
        "scope": "identity submit read flair",
    })
    auth_url = f"https://www.reddit.com/api/v1/authorize?{auth_params}"
    print("\n" + "=" * 76)
    print("  REDDIT OAUTH2 PERMANENT AUTHORIZATION")
    print("=" * 76)
    print(f"Open this URL in your browser and click 'Allow':\n\n  {auth_url}\n")
    try:
        webbrowser.open(auth_url)
    except Exception:
        pass

    captured = {}

    class CallbackHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            qs = urllib.parse.parse_qs(parsed.query)
            if "code" in qs:
                captured["code"] = qs["code"][0]
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(b"<h2>Reddit API Authorized! You can close this tab and return to Antigravity.</h2>")
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Authorization failed or cancelled.")

        def log_message(self, format, *args):
            pass

    server = http.server.HTTPServer(("127.0.0.1", 8765), CallbackHandler)
    print("[*] Waiting for browser callback on http://localhost:8765/callback ...")
    server.handle_request()
    server.server_close()

    code = captured.get("code")
    if not code:
        raise RuntimeError("Did not receive authorization code from callback.")

    basic_raw = f"{client_id}:{client_secret}".encode("utf-8")
    basic_b64 = base64.b64encode(basic_raw).decode("utf-8")
    form = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    req = urllib.request.Request(
        "https://www.reddit.com/api/v1/access_token",
        data=urllib.parse.urlencode(form).encode("utf-8"),
        headers={
            "Authorization": f"Basic {basic_b64}",
            "User-Agent": USER_AGENT,
            "Content-Type": "application/x-www-form-urlencoded",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        tok_data = json.loads(resp.read().decode("utf-8"))

    access_token = tok_data["access_token"]
    refresh_token = tok_data.get("refresh_token")
    me = reddit_api(access_token, "GET", "/api/v1/me")
    username = me.get("name", "unknown")

    cred = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "username": username,
    }
    save_credentials(cred)
    print(f"[✓] Successfully authenticated Reddit account: u/{username}!")


def preview_queue():
    pub_log = load_pub_log()
    print("=" * 76)
    print("  REDDIT WAVE 1 CAMPAIGN QUEUE // 7 HIGH-DENSITY ENGINEERING WRITE-UPS")
    print("=" * 76)
    for idx, item in enumerate(REDDIT_WAVE_1_QUEUE, 1):
        pub_entry = pub_log.get(item["id"])
        status_str = f"PUBLISHED ({pub_entry['url']})" if pub_entry else "QUEUED"
        q = urllib.parse.urlencode({
            "selftext": "true",
            "title": item["title"],
            "text": item["body"],
        })
        prefill_url = f"https://old.reddit.com/r/{item['subreddit']}/submit?{q}"
        print(f"\n[{idx}] ID: {item['id']}  [{status_str}]")
        print(f"    Subreddit   : r/{item['subreddit']}")
        print(f"    Title       : {item['title']}")
        print(f"    Target URL  : https://datacenterfieldguides.com/blog/{item['slug']}")
        print(f"    1-Click Post: {prefill_url[:90]}...")



def main():
    if "--list" in sys.argv or len(sys.argv) == 1:
        preview_queue()
        cred = load_credentials()
        if not cred:
            print("\n[!] Status: Waiting for .reddit-credentials.json.")
        else:
            print(f"\n[✓] Status: Reddit credentials loaded (u/{cred.get('username', 'Ready')}).")
        return

    if "--auth" in sys.argv:
        idx = sys.argv.index("--auth")
        client_id = sys.argv[idx + 1]
        client_secret = sys.argv[idx + 2]
        run_interactive_oauth(client_id, client_secret)
        return

    if "--verify" in sys.argv:
        cred = load_credentials()
        if not cred:
            print("[!] Missing .reddit-credentials.json")
            sys.exit(1)
        token = get_access_token(cred)
        me = reddit_api(token, "GET", "/api/v1/me")
        print(f"[✓] Reddit API Authenticated! Account: u/{me.get('name')} | Link Karma: {me.get('link_karma')} | Comment Karma: {me.get('comment_karma')}")
        return

    if "--publish-next" in sys.argv:
        pub_log = load_pub_log()
        now_utc = datetime.now(timezone.utc)
        for entry in pub_log.values():
            pub_ts = entry.get("published_at")
            if pub_ts:
                try:
                    dt = datetime.fromisoformat(pub_ts.replace("Z", "+00:00"))
                    hours_since = (now_utc - dt).total_seconds() / 3600.0
                    if hours_since < 20.0 and "--force" not in sys.argv:
                        print(f"[i] A Reddit post was already published {hours_since:.1f}h ago ({entry.get('url')}). Skipping to protect account reputation.")
                        return
                except Exception:
                    pass
        target = None
        for item in REDDIT_WAVE_1_QUEUE:
            if item["id"] not in pub_log:
                target = item
                break
        if not target:
            print("[✓] All Wave 1 Reddit posts have already been published!")
            return
        cred = load_credentials()
        if not cred:
            print("[!] Missing .reddit-credentials.json")
            sys.exit(1)
        token = get_access_token(cred)
        print(f"[+] Submitting '{target['id']}' to r/{target['subreddit']} ...")
        url = submit_reddit_post(token, target["subreddit"], target["title"], target["body"])
        pub_log[target["id"]] = {
            "url": url,
            "subreddit": target["subreddit"],
            "published_at": now_utc.isoformat(),
        }
        save_pub_log(pub_log)
        print(f"[✓] Successfully published to r/{target['subreddit']}!")
        print(f"    Live URL: {url}")


if __name__ == "__main__":
    main()
