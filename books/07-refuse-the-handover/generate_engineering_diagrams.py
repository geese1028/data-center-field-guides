#!/usr/bin/env python3
"""
Generate Flagship Engineering Diagrams for Book 07: Refuse the Handover
Author: Tristan (Data Center Field Guides)
Resolution: 1800 x 1100, publication-grade vector styling.
Palette: Deep slate blue / safety red / steel grey / caution amber / emerald green.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path("/Users/geese/Downloads/book/books/07-refuse-the-handover/figures")
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Theme Palette (Turnover Gate & Commissioning Acceptance)
BG = (15, 23, 42)          # Deep slate blue
PANEL = (30, 41, 59)       # Medium slate
GRID = (51, 65, 85)        # Slate grid
TEXT = (248, 250, 252)     # Crisp white
MUTED = (148, 163, 184)    # Cool grey
RED = (239, 68, 68)        # Refusal / Showstopper / Cat 1
AMBER = (245, 158, 11)     # Conditional / Escrow / Cat 2
GREEN = (34, 197, 94)      # Passed / Accepted / Cat 3
CYAN = (6, 182, 212)       # Verification / Engineering / Level 5
BLUE = (59, 130, 246)      # Data bus / Standards / Test
STEEL = (100, 116, 139)    # As-Built / Drawing / Custody


def get_font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = FONT_DIR / name
    if not path.exists():
        path = Path("/Library/Fonts/Arial Unicode.ttf")
    return ImageFont.truetype(str(path), size)


def new_canvas(w=1800, h=1100):
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, w, 50):
        d.line((x, 0, x, h), fill=GRID, width=1)
    for y in range(0, h, 50):
        d.line((0, y, w, y), fill=GRID, width=1)
    d.rectangle((20, 20, w - 21, h - 21), outline=RED, width=2)
    return im, d


def draw_header(d, num, title, subtitle):
    d.rectangle((40, 35, 1760, 115), fill=PANEL, outline=RED, width=2)
    d.text((60, 48), f"FIGURE 07.{num} :: {title.upper()}", font=get_font(24, True), fill=RED)
    d.text((60, 82), subtitle, font=get_font(16), fill=MUTED)
    d.text((1480, 58), "BOOK 07 // HANDOVER", font=get_font(16, True), fill=AMBER)


def wrap_text(d, text, font, max_width):
    words = str(text).split(" ")
    lines = []
    cur = []
    for w in words:
        test = " ".join(cur + [w])
        if d.textlength(test, font=font) <= max_width:
            cur.append(w)
        else:
            if cur:
                lines.append(" ".join(cur))
                cur = [w]
            else:
                lines.append(w)
                cur = []
    if cur:
        lines.append(" ".join(cur))
    return lines


# -------------------------------------------------------------
# FIG 1: Handover Gatekeeper Architecture
# -------------------------------------------------------------
def fig_01():
    im, d = new_canvas()
    draw_header(d, 1, "The Handover Gatekeeper Architecture",
                "The operations manager is the final firewall between construction optimism and live production risk.")

    # 3 Large Pipeline Stages: Construction -> The Turnover Gate -> Production
    # Stage 1: Project Delivery & Commissioning (Left)
    d.rectangle((60, 150, 520, 1040), fill=PANEL, outline=CYAN, width=2)
    d.text((80, 175), "STAGE 1: PROJECT DELIVERY", font=get_font(18, True), fill=CYAN)
    d.text((80, 205), "Construction, Vendors & Cx Agents", font=get_font(13), fill=MUTED)

    cx_items = [
        ("AS-BUILT DOSSIER", "• Certified Single-Line Diagrams (SLDs)\n• Certified Mechanical P&IDs\n• Cable schedules & torque logs\n• Pressure test & water chem certs", CYAN),
        ("COMMISSIONING PACK", "• Level 1 to Level 5 test scripts\n• Raw high-speed data files (.csv)\n• Integrated System Test (IST) logs\n• Sequence of Events (SOE) record", BLUE),
        ("TRAINING & SPARES", "• Factory O&M manuals\n• 40 hours classroom & hands-on\n• Critical spares cage stocked\n• LOTO master key inventory", STEEL),
    ]

    cy = 245
    for title, body, col in cx_items:
        d.rectangle((80, cy, 500, cy + 235), fill=(20, 28, 45), outline=col, width=1)
        d.text((95, cy + 15), title, font=get_font(15, True), fill=col)
        lines = body.split("\n")
        yy = cy + 50
        for l in lines:
            d.text((95, yy), l, font=get_font(13), fill=TEXT)
            yy += 32
        cy += 260

    # Stage 2: The Turnover Gatekeeper (Center)
    d.rectangle((560, 150, 1240, 1040), fill=(24, 32, 47), outline=RED, width=2)
    d.text((580, 175), "STAGE 2: THE TURNOVER GATEKEEPER", font=get_font(18, True), fill=RED)
    d.text((580, 205), "The Operations Manager's Sole Evaluation Envelope", font=get_font(13), fill=MUTED)

    # 3 Gating Outcomes
    gates = [
        ("OUTCOME A: UNCONDITIONAL ACCEPTANCE", "Zero Category 1 (Critical) defects.\nZero Category 2 (Major) defects.\nAll Level 1-5 tests passed under witnessed load.\nAs-Built redlines 100% reconciled to physical field.\nFull custody transferred; commercial clocks start.", GREEN),
        ("OUTCOME B: CONDITIONAL ACCEPTANCE", "Zero Category 1 defects permitted.\nMinor Category 2 defects open with agreed cure plan.\n200% FINANCIAL ESCROW HOLDBACK legally bound.\nHard 30-day cure window with automatic default remedy.\nOperations holds unilateral right to execute retest.", AMBER),
        ("OUTCOME C: TECHNICAL REFUSAL", "ANY Category 1 defect open (SLA/Safety/Redundancy).\nLevel 5 IST unexecuted or un-witnessed.\nPack contains 'IFC' drawings instead of As-Builts.\nSCADA points uncalibrated or fail forced-failure.\nSIGNATURE REFUSED. Construction maintains site custody.", RED),
    ]

    gy = 245
    for gtitle, gbody, gcol in gates:
        d.rectangle((580, gy, 1220, gy + 175), fill=PANEL, outline=gcol, width=1)
        d.text((600, gy + 15), gtitle, font=get_font(15, True), fill=gcol)
        lines = gbody.split("\n")
        yy = gy + 48
        for l in lines:
            d.text((600, yy), l, font=get_font(12), fill=TEXT)
            yy += 24
        gy += 195

    # Center Bottom: The Cardinal Law
    d.rectangle((580, 840, 1220, 1010), fill=(20, 28, 45), outline=AMBER, width=2)
    d.text((600, 860), "THE CARDINAL TURNOVER LAW", font=get_font(16, True), fill=AMBER)
    d.text((600, 895), "• Applause is not evidence. A heavy binder is not a result.", font=get_font(13, True), fill=TEXT)
    d.text((600, 925), "• Never sign a wide sentence with a narrow footnote.", font=get_font(13, True), fill=RED)
    d.text((600, 955), "• What you sign today, you own at 02:00 tomorrow.", font=get_font(13, True), fill=CYAN)

    # Stage 3: Live Production (Right)
    d.rectangle((1280, 150, 1740, 1040), fill=PANEL, outline=GREEN, width=2)
    d.text((1300, 175), "STAGE 3: PRODUCTION OPERATIONS", font=get_font(18, True), fill=GREEN)
    d.text((1300, 205), "Commercial Service Level Agreement Live", font=get_font(13), fill=MUTED)

    prod_items = [
        ("CUSTODY TRANSFERRED", "• Plant operating under site SOPs\n• Permits to Work (PTW) required\n• Construction access terminated\n• Sole LOTO custody established", GREEN),
        ("SLA CLOCK TICKING", "• 99.999% availability guaranteed\n• 15-minute incident SLA clock live\n• Secondary fluid temp strictly held\n• Revenue power meters recording", AMBER),
        ("REPUTATION & CARE", "• Shift teams walking 6 stations\n• Master Day Sheet signed daily\n• No hidden construction waivers\n• The building runs clean", CYAN),
    ]

    py = 245
    for title, body, col in prod_items:
        d.rectangle((1300, py, 1720, py + 235), fill=(20, 28, 45), outline=col, width=1)
        d.text((1315, py + 15), title, font=get_font(15, True), fill=col)
        lines = body.split("\n")
        yy = py + 50
        for l in lines:
            d.text((1315, yy), l, font=get_font(13), fill=TEXT)
            yy += 32
        py += 260

    # Connecting Arrows
    d.line((500, 520, 580, 520), fill=CYAN, width=3)
    d.line((1220, 332, 1300, 332), fill=GREEN, width=3)

    im.save(OUT_DIR / "fig-01-handover-gatekeeper-architecture.png", "PNG")
    print("Saved: fig-01-handover-gatekeeper-architecture.png")


# -------------------------------------------------------------
# FIG 2: Punchlist Defect Triad Matrix
# -------------------------------------------------------------
def fig_02():
    im, d = new_canvas()
    draw_header(d, 2, "The Punch List Defect Triad Matrix",
                "The three-tier classification governing turnover punch items. Category 1 blocks signature unconditionally.")

    cols = [
        ("CATEGORY 1: CRITICAL SHOWSTOPPER", "ABSOLUTE SIGNATURE REFUSAL", [
            ("Definition", "ANY defect that impairs human life safety, violates statutory building codes, or eliminates system redundancy (N-1 state)."),
            ("Electrical Examples", "• Automatic Transfer Switch (ATS) fails closed-transition under load.\n• Ground fault protective relay curves uncoordinated.\n• Emergency Generator paralleling bus trips on reverse power."),
            ("Mechanical Examples", "• Secondary CDU pump mechanical seal weeping glycol.\n• Quick-disconnect coupling (FD83) dripping at rack header.\n• Plate heat exchanger approach temp > 8.0 K under load."),
            ("SCADA Examples", "• Low loop pressure alarm fails to sound on severed wire.\n• Fire VESDA smoke alert disabled on central console."),
            ("Mandatory Action", "REFUSE SIGNATURE. Construction must remediate, submit revised MOP, and execute full witnessed re-test."),
        ], RED),
        ("CATEGORY 2: MAJOR / CONDITIONAL", "200% ESCROW & 30-DAY CURE", [
            ("Definition", "Defects that impair maintenance ergonomics, secondary sensor accuracy, or spare parts readiness, but plant redundancy remains N+1."),
            ("Electrical Examples", "• Panelboard labeling missing circuit breaker directory.\n• Infrared thermal scan reveals lug delta-T = 6 K (warning).\n• Battery room eyewash station water pressure low."),
            ("Mechanical Examples", "• Manual isolation valve packing gland weeping 1 drop/min.\n• Chilled water pipe insulation dented or jacketing unsealed.\n• Filter differential pressure gauge dial cracked."),
            ("SCADA Examples", "• Non-critical trending point reports STALE quality.\n• Screen graphics show typo on equipment tag name."),
            ("Mandatory Action", "CONDITIONAL ACCEPTANCE ONLY if 200% financial escrow retained and 30-day cure window legally binding."),
        ], AMBER),
        ("CATEGORY 3: MINOR PUNCH ITEMS", "PERMITTED WITH RECORDED RETEST", [
            ("Definition", "Purely cosmetic, architectural, or housekeeping defects with zero impact on electrical, mechanical, or thermal performance."),
            ("Electrical Examples", "• Cable tray nylon zip ties untrimmed or unevenly spaced.\n• Switchgear enclosure touch-up paint scratched.\n• Raised floor grounding pigtail tag faded."),
            ("Mechanical Examples", "• Pump pedestal concrete housekeeping pad chipped.\n• Pipe directional flow arrow sticker peeling.\n• Valve brass identification tag hanging loose."),
            ("SCADA Examples", "• Web dashboard icon alignment offset by 5 pixels.\n• Trend line color on secondary graph preferred blue."),
            ("Mandatory Action", "ACCEPTANCE PERMITTED. Item recorded on Page 2 punch list with named contractor lead and 60-day closeout."),
        ], GREEN),
    ]

    for i, (title, sub, items, col) in enumerate(cols):
        x = 60 + i * 570
        d.rectangle((x, 150, x + 540, 1040), fill=PANEL, outline=col, width=2)
        d.text((x + 20, 175), title, font=get_font(16, True), fill=col)
        d.text((x + 20, 205), sub, font=get_font(13, True), fill=TEXT)
        d.line((x + 20, 230, x + 520, 230), fill=GRID, width=1)

        iy = 245
        for itit, idesc in items:
            d.rectangle((x + 20, iy, x + 520, iy + 145), fill=(20, 28, 45), outline=col, width=1)
            d.text((x + 35, iy + 12), itit.upper(), font=get_font(13, True), fill=col)
            # wrap text
            words = idesc.split()
            cur, l_list = "", []
            for w in words:
                if d.textlength(cur + " " + w, font=get_font(11)) <= 460:
                    cur += (" " if cur else "") + w
                else:
                    l_list.append(cur)
                    cur = w
            if cur:
                l_list.append(cur)
            for k, line in enumerate(l_list):
                d.text((x + 35, iy + 38 + k * 18), line, font=get_font(11), fill=TEXT)
            iy += 155

    im.save(OUT_DIR / "fig-02-punchlist-defect-triad-matrix.png", "PNG")
    print("Saved: fig-02-punchlist-defect-triad-matrix.png")


# -------------------------------------------------------------
# FIG 3: As-Built Redline Custody Audit
# -------------------------------------------------------------
def fig_03():
    im, d = new_canvas()
    draw_header(d, 3, "As-Built vs. Redline Forensic Custody Audit",
                "Never accept a turnover pack where drawings are marked 'Issued for Construction' (IFC). Demand verified As-Builts.")

    # Left: The Four Required As-Built Drawing Sets
    d.rectangle((60, 150, 880, 1040), fill=PANEL, outline=CYAN, width=2)
    d.text((80, 175), "MANDATORY AS-BUILT DRAWING SETS", font=get_font(18, True), fill=CYAN)
    d.text((80, 205), "Must be signed, sealed by Professional Engineer (PE), and field-verified", font=get_font(13), fill=MUTED)

    draw_sets = [
        ("1. ELECTRICAL SINGLE-LINE DIAGRAM (SLD)", "• Full hierarchy: 35kV Utility -> Transformers -> 480V Main -> UPS -> RPP -> Rack ePDUs\n• Overcurrent protective relay curves & trip settings\n• Interlocking logic (Kirk Key / Castell interlocks)\n• Transformer tap positions & grounding grid connections", CYAN),
        ("2. MECHANICAL P&ID (ISA-5.1 COMPLIANT)", "• Chilled water primary (FWS) & secondary (TCS) loops\n• Plate heat exchangers, pumps, bypass valves, flow meters\n• Expansion tank nitrogen pre-charge & makeup skids\n• Exact physical pipe diameters, schedule, and metallurgy", BLUE),
        ("3. CONTROL & INSTRUMENTATION LOOPS", "• Complete terminal-to-terminal wiring schematics\n• Field controller addresses, Modbus register tables, OIDs\n• Analog loop power supply origins (24VDC isolated)\n• Cable conduit routing and pull box locations", AMBER),
        ("4. PHYSICAL VALVE & BREAKER LINEUP SCHEDULES", "• Master valve lineup matrix (Normal / Standby / Fill / Drain)\n• Car-seal list: which valves are sealed open vs sealed closed\n• Breaker directory matching physical panelboard labels\n• Lockout/Tagout (LOTO) energy isolation point registry", GREEN),
    ]

    dy = 245
    for dt, db, dc in draw_sets:
        d.rectangle((80, dy, 860, dy + 180), fill=(20, 28, 45), outline=dc, width=1)
        d.text((95, dy + 15), dt, font=get_font(15, True), fill=dc)
        lines = db.split("\n")
        yy = dy + 45
        for l in lines:
            d.text((95, yy), l, font=get_font(12), fill=TEXT)
            yy += 24
        dy += 195

    # Right: The Field Redline Forensic Audit (Comparison)
    d.rectangle((920, 150, 1740, 1040), fill=(24, 32, 47), outline=RED, width=2)
    d.text((940, 175), "THE REDLINE FORENSIC AUDIT: REASONS TO REFUSE", font=get_font(18, True), fill=RED)
    d.text((940, 205), "The common drawing lies that must halt handover sign-off", font=get_font(13), fill=MUTED)

    refusal_reasons = [
        ("THE 'IFC' STAMP DECEPTION", "The turnover pack contains drawings stamped 'Issued for Construction' (IFC) rather than 'As-Built'. An IFC drawing is a design proposal from two years ago; it does not reflect the field routing changes made when contractors hit structural columns. REFUSE.", RED),
        ("THE UNRECONCILED FIELD REDLINE", "The contractor provides a roll of crumpled physical paper drawings with red-ink scribbles from the job trailer. Scribbles are not As-Builts. The redlines must be drafted into official CAD/BIM revisions, peer-reviewed, and sealed by the engineer of record. REFUSE.", RED),
        ("THE REVERSED VALVE POLARITY", "Physical inspection reveals that 3-way modulating bypass valve TCV-101 is piped in reverse compared to the schematic. Under loss of control signal, the valve fails to closed instead of fail-to-bypass. REFUSE.", AMBER),
        ("THE GHOST CABLE ON THE BUSBAR", "Drawing shows electrical Bus A and Bus B completely isolated. Field walk reveals a temporary 4/0 AWG tie-cable installed during testing still bolted across the buses. Immediate catastrophic single-point failure hazard. REFUSE.", RED),
    ]

    ry = 245
    for rt, rb, rc in refusal_reasons:
        d.rectangle((940, ry, 1720, ry + 180), fill=PANEL, outline=rc, width=1)
        d.text((960, ry + 15), rt, font=get_font(15, True), fill=rc)
        words = rb.split()
        cur, l_list = "", []
        for w in words:
            if d.textlength(cur + " " + w, font=get_font(12)) <= 740:
                cur += (" " if cur else "") + w
            else:
                l_list.append(cur)
                cur = w
        if cur:
            l_list.append(cur)
        for k, line in enumerate(l_list):
            d.text((960, ry + 48 + k * 22), line, font=get_font(12), fill=TEXT)
        ry += 195

    im.save(OUT_DIR / "fig-03-as-built-redline-custody-audit.png", "PNG")
    print("Saved: fig-03-as-built-redline-custody-audit.png")


# -------------------------------------------------------------
# FIG 4: Conditional Acceptance Escrow Ladder
# -------------------------------------------------------------
def fig_04():
    im, d = new_canvas()
    draw_header(d, 4, "The Conditional Acceptance Escrow & Retainage Ladder",
                "How to protect the owner legally and financially when accepting a facility with minor punch items.")

    # 4 Steps of the Escrow Engine
    steps = [
        ("STEP 1: DEFECT ESTIMATION", "Every open Category 2 defect is itemized on the handover punch sheet with an independent engineering cost estimate to remediate.\n• Example: Re-terminate 480V neutral bus = $25,000\n• Example: Replace leaking CDU pump seal = $18,000\n• Total Remediation Estimate = $43,000", CYAN),
        ("STEP 2: THE 200% ESCROW RULE", "Owner withholds exactly TWO HUNDRED PERCENT (200%) of the remediation estimate from the final construction milestone payment in an escrow account:\n• Retainage Amount: 2.0 * $43,000 = $86,000\n• Retainage cannot be released until physical re-test passes.", AMBER),
        ("STEP 3: THE 30-DAY CURE CLOCK", "Contractor is granted a strict, legally binding 30-day cure window:\n• Countdown begins at handover signature.\n• Contractor must submit approved MOP for work.\n• Operations team must witness and sign re-test.\n• No extension permitted without written owner consent.", BLUE),
        ("STEP 4: DEFAULT & THIRD-PARTY REMEDY", "If contractor fails to remediate and pass re-test by Day 30:\n• Owner unilaterally seizes the escrowed retainage.\n• Operations hires an independent third-party contractor.\n• Work is executed and billed directly to the escrow fund.\n• Original contractor forfeits all remaining milestone balances.", RED),
    ]

    for i, (st, sb, sc) in enumerate(steps):
        y = 150 + i * 215
        d.rectangle((60, y, 1740, y + 195), fill=PANEL, outline=sc, width=2)
        d.rectangle((60, y, 320, y + 195), fill=(20, 28, 45), outline=sc, width=1)
        d.text((80, y + 80), f"PHASE {i+1}", font=get_font(28, True), fill=sc)

        d.text((350, y + 25), st, font=get_font(18, True), fill=sc)
        lines = sb.split("\n")
        yy = y + 65
        for l in lines:
            d.text((350, yy), l, font=get_font(13), fill=TEXT)
            yy += 26

    # Bottom Summary Bar
    d.rectangle((60, 1020, 1740, 1075), fill=(20, 28, 45), outline=GREEN, width=1)
    d.text((90, 1038), "FINANCIAL DISCIPLINE LAW: Never sign conditional acceptance on a promise. Retain the cash or refuse the key.", font=get_font(15, True), fill=GREEN)

    im.save(OUT_DIR / "fig-04-conditional-acceptance-escrow-ladder.png", "PNG")
    print("Saved: fig-04-conditional-acceptance-escrow-ladder.png")


# -------------------------------------------------------------
# FIG 5: Commissioning Levels Gating Pyramid
# -------------------------------------------------------------
def fig_05():
    im, d = new_canvas()
    draw_header(d, 5, "Commissioning Levels Gating Pyramid (ASHRAE Guideline 0 / Standard 202)",
                "The 5-level commissioning ladder. A vendor factory test is not a building turnover.")

    # Pyramid Levels (0 to 5)
    levels = [
        ("LEVEL 5: INTEGRATED SYSTEM TESTING (IST) & BLACK-START", "• Full 100% load bank burn-in (heat and power) for 24-48 hours.\n• Pull-the-plug utility failure test; emergency generator auto-transfer.\n• Chiller plant failover under live thermal load; zero IT throttling.\n• Sequence of Events (SOE) microsecond validation.", RED),
        ("LEVEL 4: SYSTEM FUNCTIONAL INTERFACE TESTING", "• Controls and automation interlocking tested across subsystems.\n• BMS, EPMS, and Fire Alarm matrix interlocks verified.\n• Automatic standby pump and chiller lead-lag staging verified.\n• Variable frequency drive (VFD) hunting and PID stability tested.", AMBER),
        ("LEVEL 3: INDIVIDUAL EQUIPMENT START-UP & PRE-FUNCTIONAL", "• Vendor technicians energize and spin individual motors.\n• Direction of rotation, phase balance, and vibration checked.\n• Factory warranty start-up sheets signed.\n• Mechanical piping pressure testing & hydrostatic leak checks.", BLUE),
        ("LEVEL 2: FACTORY WITNESS TESTING (FWT) & PRE-INSTALLATION", "• Equipment inspected at factory prior to shipment (Transformers, Chillers).\n• Witnessed factory load testing on manufacturer test stands.\n• Shipping shock indicator tags audited upon site delivery.", CYAN),
        ("LEVEL 1: DESIGN PROCUREMENT & PRE-CONSTRUCTION", "• Owner's Project Requirements (OPR) & Basis of Design (BOD).\n• Construction drawing review, submittal approvals, and RFI log.", STEEL),
    ]

    for k, (ltitle, ldesc, lcol) in enumerate(levels):
        y = 150 + k * 175
        w_offset = k * 40
        d.rectangle((60 + w_offset, y, 1740 - w_offset, y + 155), fill=PANEL, outline=lcol, width=2)
        d.text((80 + w_offset, y + 15), ltitle, font=get_font(16, True), fill=lcol)
        lines = ldesc.split("\n")
        yy = y + 45
        for l in lines:
            d.text((80 + w_offset, yy), l, font=get_font(12), fill=TEXT)
            yy += 22

    im.save(OUT_DIR / "fig-05-commissioning-levels-gating-pyramid.png", "PNG")
    print("Saved: fig-05-commissioning-levels-gating-pyramid.png")


# -------------------------------------------------------------
# FIG 6: Custody Transfer & LOTO Handover
# -------------------------------------------------------------
def fig_06():
    im, d = new_canvas()
    draw_header(d, 6, "Physical Custody Transfer and Lockout/Tagout (LOTO) Interlocking",
                "A facility cannot have two masters. Handover requires complete physical key transfer and termination of dual custody.")

    # 3 Large Pillars: Construction Custody -> The Key Exchange -> Operations Sole Custody
    pillars = [
        ("1. CONSTRUCTION CUSTODY", "Contractor in Command", [
            ("Contractor Master Padlocks", "All switchgear, valves, and breaker panels secured with contractor red padlocks."),
            ("Jobsite Safety Envelope", "Site governed by General Contractor safety rules and construction permits."),
            ("Temporary Power & Jumpers", "Temporary construction power feeds and bypass hoses may be present."),
            ("Contractor Badge Access", "Construction personnel roam site freely without operational escort."),
        ], RED),
        ("2. THE CUSTODY TRANSFER GATE", "The Physical Boundary", [
            ("Master Key Audit (100%)", "Audit every physical key: switchgear doors, panel locks, Kirk Key interlocks."),
            ("Removal of Construction Locks", "Contractor removes all construction padlocks in presence of Duty Manager."),
            ("Physical Zero-Energy Walk", "Duty Manager inspects every panel: verify zero temporary jumpers remain."),
            ("Access Control Cutover", "Security card readers re-programmed: construction badges revoked."),
        ], AMBER),
        ("3. OPERATIONS SOLE CUSTODY", "Operations in Command", [
            ("Operations LOTO Padlocks", "Duty Manager applies site operational padlocks and yellow danger tags."),
            ("Strict PTW Enforcement", "Any returning contractor must apply for Permit to Work and have site escort."),
            ("Standard Operating State", "All valves car-sealed; breakers locked in designated normal lineup."),
            ("Legal Liability Established", "Operations assumes 100% legal custody of plant safety and SLA delivery."),
        ], GREEN),
    ]

    for i, (title, sub, items, col) in enumerate(pillars):
        x = 60 + i * 570
        d.rectangle((x, 150, x + 540, 1040), fill=PANEL, outline=col, width=2)
        d.text((x + 20, 175), title, font=get_font(17, True), fill=col)
        d.text((x + 20, 205), sub, font=get_font(13), fill=MUTED)
        d.line((x + 20, 230, x + 520, 230), fill=GRID, width=1)

        iy = 250
        for itit, idesc in items:
            d.rectangle((x + 20, iy, x + 520, iy + 165), fill=(20, 28, 45), outline=col, width=1)
            d.text((x + 35, iy + 15), itit, font=get_font(15, True), fill=col)
            words = idesc.split()
            cur, l_list = "", []
            for w in words:
                if d.textlength(cur + " " + w, font=get_font(12)) <= 460:
                    cur += (" " if cur else "") + w
                else:
                    l_list.append(cur)
                    cur = w
            if cur:
                l_list.append(cur)
            for k, line in enumerate(l_list):
                d.text((x + 35, iy + 45 + k * 22), line, font=get_font(12), fill=TEXT)
            iy += 185

    im.save(OUT_DIR / "fig-06-custody-transfer-and-loto-handover.png", "PNG")
    print("Saved: fig-06-custody-transfer-and-loto-handover.png")


# -------------------------------------------------------------
# FIG 7: Master Refusal Sheet & Dissent Ledger
# -------------------------------------------------------------
def fig_07():
    im, d = new_canvas()
    draw_header(d, 7, "The Master Refusal Sheet and Dissent Ledger",
                "The legal and operational instrument of dissent. How to write a legally defensible statement of technical refusal.")

    # Top Box: The Refusal Architecture
    d.rectangle((60, 150, 1740, 280), fill=PANEL, outline=RED, width=2)
    d.text((90, 175), "THE REFUSAL FORMULA: AN AUDITABLE STATEMENT OF OPERATIONAL DISSENT", font=get_font(18, True), fill=RED)
    d.text((90, 205), "When pressured by construction leads or commercial executives to sign an unearned turnover certificate:", font=get_font(13), fill=TEXT)
    d.text((90, 235), "1. Never sign their pre-printed wide sentence. 2. Strike unverified clauses in ink. 3. Attach this Refusal Sheet.", font=get_font(14, True), fill=AMBER)

    # Simulated Master Refusal Sheet Ledger
    d.rectangle((60, 310, 1740, 1040), fill=(20, 28, 45), outline=CYAN, width=2)
    d.text((90, 335), "THE MASTER HANDOVER REFUSAL LEDGER", font=get_font(18, True), fill=CYAN)

    sections = [
        ("SECTION 1: SPECIFIC SCOPE UNDER AUDIT", "Building: DC-02 | Hall: AI Whitespace Pod 3 | Systems: Medium-Voltage Feeder B & Secondary CDUs 01-04\nCommissioning Agent: Apex Commissioning LLC | General Contractor: Turner/StructureTone"),
        ("SECTION 2: WORDS STRUCK FROM THE TURNOVER CERTIFICATE", "Struck: 'The entire electrical and mechanical infrastructure is fully commissioned and accepted without reservation.'\nReason: Stated claim is wider than witnessed evidence. Level 5 Integrated System Test was not run under full thermal load."),
        ("SECTION 3: OPEN CATEGORY 1 SHOWSTOPPER DEFECTS (REASONS FOR REFUSAL)", "1. Item #E-104: Automatic Transfer Switch (ATS-02) failed closed-transition transfer under 100% load test (Relay tripped).\n2. Item #M-088: Secondary CDU-02 Quick-Disconnect manifold connection weeping propylene glycol under 0.60 MPa dwell.\n3. Item #S-014: SCADA communication to Chiller 3 drops to STALE after 60 seconds of broadcast traffic."),
        ("SECTION 4: CONDITIONAL ESCROW DEMAND (IF CONDITIONAL SIGNATURE PERMITTED)", "Total Remediation Estimate: $68,000 USD | 200% Retainage Required: $136,000 USD to be held in third-party escrow.\nCure Window: 30 Calendar Days (Expires 2026-11-14). If un-remediated, Owner retains third-party engineer."),
        ("SECTION 5: THE BINDING SIGNED STATEMENT OF TECHNICAL REFUSAL", "“I certify on my professional engineering license that the designated systems have NOT satisfied the contractual criteria for operational turnover. Full technical handover is REFUSED. Custody remains with the General Contractor until all Category 1 items are remediated and witnessed under live load.”\nSigned: Marcus Vance, PE, Operations Director | Date: 2026-10-14 16:45 UTC"),
    ]

    sy = 375
    for stitle, sbody in sections:
        d.rectangle((90, sy, 1710, sy + 115), fill=PANEL, outline=GRID, width=1)
        d.text((110, sy + 12), stitle, font=get_font(13, True), fill=AMBER if "CATEGORY 1" in stitle or "REFUSAL" in stitle else CYAN)
        lines = sbody.split("\n")
        yy = sy + 38
        for l in lines:
            wrapped = wrap_text(d, l, get_font(12), 1580)
            for wl in wrapped:
                d.text((110, yy), wl, font=get_font(12), fill=TEXT)
                yy += 20
        sy += 130

    im.save(OUT_DIR / "fig-07-master-refusal-sheet-and-dissent-ledger.png", "PNG")
    print("Saved: fig-07-master-refusal-sheet-and-dissent-ledger.png")


def main():
    print("Generating Flagship Engineering Diagrams for Book 07: Refuse the Handover...")
    fig_01()
    fig_02()
    fig_03()
    fig_04()
    fig_05()
    fig_06()
    fig_07()
    print("All 7 Engineering Diagrams successfully generated for Book 07!")


if __name__ == "__main__":
    main()
