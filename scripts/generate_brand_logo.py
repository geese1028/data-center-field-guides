#!/usr/bin/env python3
"""
Generates the official brand identity & logo suite for Data Center Field Guides (DCFG):
1. site/logo.png (800x800 high-DPI anti-aliased PNG for LinkedIn Company Page, App Icon, and Google Organization Schema)
2. site/favicon.png (192x192 PNG for Google SERP favicon & Apple Touch Icon)
3. site/favicon.svg (Crisp vector SVG for browser tabs & site header navbar)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SITE_DIR = Path("/Users/geese/Downloads/book/site")


def generate_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B1120"/>
      <stop offset="55%" stop-color="#090D16"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="frameGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6"/>
      <stop offset="50%" stop-color="#1D4ED8"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="bladeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#172033"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="blueAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#60A5FA"/>
    </linearGradient>
  </defs>

  <!-- Outer Rounded Technical Chassis -->
  <rect x="16" y="16" width="480" height="480" rx="96" fill="url(#bgGrad)" stroke="url(#frameGrad)" stroke-width="12"/>
  
  <!-- Subtle Inner Blueprint Grid Lines -->
  <g stroke="#1E293B" stroke-width="2" opacity="0.55">
    <line x1="96" y1="64" x2="96" y2="448"/>
    <line x1="416" y1="64" x2="416" y2="448"/>
    <line x1="64" y1="120" x2="448" y2="120"/>
    <line x1="64" y1="392" x2="448" y2="392"/>
  </g>

  <!-- Corner Alignment Reticles (Commissioning Target Marks) -->
  <g stroke="#3B82F6" stroke-width="4" fill="none" stroke-linecap="round">
    <path d="M 68 96 L 68 68 L 96 68"/>
    <path d="M 444 96 L 444 68 L 416 68"/>
    <path d="M 68 416 L 68 444 L 96 444"/>
    <path d="M 444 416 L 444 444 L 416 444"/>
  </g>

  <!-- Dual-Feed 2N Redundancy Vertical Busbars (Left: Feed A Blue, Right: Feed B Emerald) -->
  <path d="M 104 132 L 104 348" stroke="#3B82F6" stroke-width="10" stroke-linecap="round"/>
  <path d="M 408 132 L 408 348" stroke="#10B981" stroke-width="10" stroke-linecap="round"/>

  <!-- Rack Module 01 (Top: Power & Grid Verification) -->
  <rect x="132" y="108" width="248" height="68" rx="12" fill="url(#bladeGrad)" stroke="#334155" stroke-width="4"/>
  <line x1="104" y1="142" x2="132" y2="142" stroke="#3B82F6" stroke-width="6"/>
  <line x1="380" y1="142" x2="408" y2="142" stroke="#10B981" stroke-width="6"/>
  <circle cx="164" cy="142" r="10" fill="#3B82F6"/>
  <rect x="192" y="135" width="96" height="14" rx="4" fill="#94A3B8" opacity="0.85"/>
  <rect x="304" y="135" width="48" height="14" rx="4" fill="#3B82F6" opacity="0.45"/>

  <!-- Rack Module 02 (Middle: Liquid Thermal Loop & Load Bank) -->
  <rect x="132" y="206" width="248" height="68" rx="12" fill="url(#bladeGrad)" stroke="#3B82F6" stroke-width="4"/>
  <line x1="104" y1="240" x2="132" y2="240" stroke="#3B82F6" stroke-width="6"/>
  <line x1="380" y1="240" x2="408" y2="240" stroke="#10B981" stroke-width="6"/>
  <circle cx="164" cy="240" r="10" fill="#10B981"/>
  <rect x="192" y="233" width="116" height="14" rx="4" fill="#F8FAFC"/>
  <rect x="322" y="233" width="30" height="14" rx="4" fill="#10B981" opacity="0.65"/>

  <!-- Rack Module 03 (Bottom: Redundancy & Handover Gate) -->
  <rect x="132" y="304" width="248" height="68" rx="12" fill="url(#bladeGrad)" stroke="#334155" stroke-width="4"/>
  <line x1="104" y1="338" x2="132" y2="338" stroke="#3B82F6" stroke-width="6"/>
  <line x1="380" y1="338" x2="408" y2="338" stroke="#10B981" stroke-width="6"/>
  <circle cx="164" cy="338" r="10" fill="#F59E0B"/>
  <rect x="192" y="331" width="80" height="14" rx="4" fill="#94A3B8" opacity="0.85"/>
  <rect x="288" y="331" width="64" height="14" rx="4" fill="#F59E0B" opacity="0.5"/>

  <!-- Bottom Technical Stencil Pill: DCFG -->
  <rect x="148" y="400" width="216" height="44" rx="8" fill="#090D16" stroke="#2563EB" stroke-width="3"/>
  <text x="256" y="430" text-anchor="middle" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="26" font-weight="900" letter-spacing="6">DCFG</text>
</svg>
"""
    svg_path = SITE_DIR / "favicon.svg"
    svg_path.write_text(svg_content, encoding="utf-8")
    print(f"[✓] Generated vector SVG logo: {svg_path}")


def load_font(size, bold=True):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNS.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()


def generate_png():
    # Render at 2400x2400 (3x supersampling) and downsample to 800x800 and 192x192
    S = 2400
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Outer Rounded Chassis
    pad = 60
    draw.rounded_rectangle(
        [pad, pad, S - pad, S - pad],
        radius=420,
        fill=(9, 13, 22, 255),
        outline=(37, 99, 235, 255),
        width=48,
    )

    # Inner dark bevel frame
    in_pad = 108
    draw.rounded_rectangle(
        [in_pad, in_pad, S - in_pad, S - in_pad],
        radius=372,
        fill=(11, 17, 32, 255),
        outline=(30, 41, 59, 255),
        width=12,
    )

    # 2. Blueprint Engineering Grid Lines
    grid_color = (23, 34, 54, 255)
    for gx in [420, 800, 1200, 1600, 1980]:
        draw.line([(gx, 220), (gx, 2180)], fill=grid_color, width=6)
    for gy in [450, 850, 1250, 1650, 1950]:
        draw.line([(220, gy), (2180, gy)], fill=grid_color, width=6)

    # 3. Corner Reticle Target Marks
    ret_color = (59, 130, 246, 255)
    rw = 18
    # Top-left
    draw.line([(300, 420), (300, 300), (420, 300)], fill=ret_color, width=rw)
    # Top-right
    draw.line([(2100, 420), (2100, 300), (1980, 300)], fill=ret_color, width=rw)
    # Bottom-left
    draw.line([(300, 1980), (300, 2100), (420, 2100)], fill=ret_color, width=rw)
    # Bottom-right
    draw.line([(2100, 1980), (2100, 2100), (1980, 2100)], fill=ret_color, width=rw)

    # 4. Dual-Feed 2N Vertical Busbars (Feed A Left: Electric Blue, Feed B Right: Emerald Green)
    bus_left_x = 460
    bus_right_x = 1940
    bus_top_y = 520
    bus_bot_y = 1520

    # Feed A (Left)
    draw.line([(bus_left_x, bus_top_y), (bus_left_x, bus_bot_y)], fill=(59, 130, 246, 255), width=44)
    draw.ellipse([bus_left_x - 36, bus_top_y - 36, bus_left_x + 36, bus_top_y + 36], fill=(59, 130, 246, 255))
    draw.ellipse([bus_left_x - 36, bus_bot_y - 36, bus_left_x + 36, bus_bot_y + 36], fill=(59, 130, 246, 255))

    # Feed B (Right)
    draw.line([(bus_right_x, bus_top_y), (bus_right_x, bus_bot_y)], fill=(16, 185, 129, 255), width=44)
    draw.ellipse([bus_right_x - 36, bus_top_y - 36, bus_right_x + 36, bus_top_y + 36], fill=(16, 185, 129, 255))
    draw.ellipse([bus_right_x - 36, bus_bot_y - 36, bus_right_x + 36, bus_bot_y + 36], fill=(16, 185, 129, 255))

    # 5. Three High-Density Rack Modules (L1 Power, L2 Liquid Cooling, L3 Redundancy Gate)
    modules = [
        {"y": 460, "led": (59, 130, 246, 255), "border": (51, 65, 85, 255), "bar1": 460, "bar2": 220, "tag": "2N"},
        {"y": 880, "led": (16, 185, 129, 255), "border": (59, 130, 246, 255), "bar1": 540, "bar2": 160, "tag": "L5"},
        {"y": 1300, "led": (245, 158, 11, 255), "border": (51, 65, 85, 255), "bar1": 380, "bar2": 280, "tag": "G1"},
    ]

    mod_left = 600
    mod_right = 1800
    mod_h = 300

    for m in modules:
        my = m["y"]
        mid_y = my + mod_h // 2
        # Horizontal feeder taps from Bus A and Bus B
        draw.line([(bus_left_x, mid_y), (mod_left, mid_y)], fill=(59, 130, 246, 255), width=28)
        draw.line([(mod_right, mid_y), (bus_right_x, mid_y)], fill=(16, 185, 129, 255), width=28)

        # Blade enclosure
        draw.rounded_rectangle(
            [mod_left, my, mod_right, my + mod_h],
            radius=54,
            fill=(23, 32, 51, 255),
            outline=m["border"],
            width=18,
        )

        # Status LED with subtle glow ring
        led_x = mod_left + 145
        r_glow = 66
        r_led = 44
        lc = m["led"]
        draw.ellipse([led_x - r_glow, mid_y - r_glow, led_x + r_glow, mid_y + r_glow], fill=(lc[0], lc[1], lc[2], 55))
        draw.ellipse([led_x - r_led, mid_y - r_led, led_x + r_led, mid_y + r_led], fill=lc)

        # Telemetry bar 1 (Primary bus)
        b1_x = mod_left + 270
        draw.rounded_rectangle(
            [b1_x, mid_y - 34, b1_x + m["bar1"], mid_y + 34],
            radius=18,
            fill=(226, 232, 240, 240) if m["y"] == 880 else (148, 163, 184, 210),
        )

        # Telemetry bar 2 (Accent metric)
        b2_x = b1_x + m["bar1"] + 55
        draw.rounded_rectangle(
            [b2_x, mid_y - 34, b2_x + m["bar2"], mid_y + 34],
            radius=18,
            fill=(lc[0], lc[1], lc[2], 165),
        )

    # 6. Bottom Identity Plate: "DCFG" + "FIELD GUIDES"
    plate_top = 1730
    plate_bot = 2070
    draw.rounded_rectangle(
        [520, plate_top, 1880, plate_bot],
        radius=48,
        fill=(9, 13, 22, 255),
        outline=(37, 99, 235, 255),
        width=14,
    )

    font_main = load_font(172, bold=True)
    font_sub = load_font(56, bold=True)

    # Draw centered "DCFG"
    title_str = "D C F G"
    bbox = draw.textbbox((0, 0), title_str, font=font_main)
    tw = bbox[2] - bbox[0]
    draw.text(((S - tw) // 2, plate_top + 34), title_str, font=font_main, fill=(248, 250, 252, 255))

    # Draw subtitle below plate or inside bottom
    sub_str = "DATA CENTER FIELD GUIDES"
    sbbox = draw.textbbox((0, 0), sub_str, font=font_sub)
    stw = sbbox[2] - sbbox[0]
    draw.text(((S - stw) // 2, plate_top + 235), sub_str, font=font_sub, fill=(96, 165, 250, 255))

    # Downsample to 800x800 (LinkedIn & Organization Logo) and 192x192 (Favicon)
    logo_800 = img.resize((800, 800), Image.Resampling.LANCZOS)
    logo_path = SITE_DIR / "logo.png"
    logo_800.save(logo_path, "PNG", optimize=True)
    print(f"[✓] Generated 800x800 high-res logo PNG: {logo_path}")

    fav_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
    fav_path = SITE_DIR / "favicon.png"
    fav_192.save(fav_path, "PNG", optimize=True)
    print(f"[✓] Generated 192x192 favicon PNG: {fav_path}")


if __name__ == "__main__":
    generate_svg()
    generate_png()
