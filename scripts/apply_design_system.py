#!/usr/bin/env python3
"""
Applies the new Stripe Press / Tailwind Catalyst design system across build_site.py.
Eliminates:
- All cyan (#06b6d4, var(--accent-cyan))
- All neon glowing shadows (rgba(6, 182, 212, 0.4))
- Text gradient background clipping
- Emoji clutter in navigation, hero buttons, and kickers
"""

import re
from pathlib import Path

BUILD_SCRIPT = Path("/Users/geese/Downloads/book/site/build_site.py")
code = BUILD_SCRIPT.read_text(encoding="utf-8")

# 1. Global Color & Variable replacements
replacements = [
    # CSS root variables
    (
        '''    :root {
      --bg: #0a0f1d;
      --card-bg: #111827;
      --border: #1f2937;
      --text: #f3f4f6;
      --muted: #9ca3af;
      --accent-cyan: #06b6d4;
      --accent-gold: #f59e0b;
      --accent-blue: #38bdf8;
    }''',
        '''    :root {
      --bg: #090d16;
      --surface: #121826;
      --surface-elevated: #172033;
      --surface-inset: #0c101a;
      --border: #1e283d;
      --border-subtle: rgba(255, 255, 255, 0.07);
      --text-primary: #f8fafc;
      --text-secondary: #cbd5e1;
      --text-muted: #7d8b9e;
      --accent: #2563eb;
      --accent-hover: #3b82f6;
      --accent-subtle: rgba(37, 99, 235, 0.12);
      --amber: #d97706;
      --amber-hover: #f59e0b;
      --amber-subtle: rgba(217, 119, 6, 0.12);
      --green: #10b981;
      --green-subtle: rgba(16, 185, 129, 0.12);
    }'''
    ),
    (
        '''    :root {
      --bg: #0a0f1d;
      --card-bg: #0f172a;
      --border: #1e293b;
      --text: #f3f4f6;
      --muted: #94a3b8;
      --accent-cyan: #06b6d4;
      --accent-gold: #f59e0b;
      --accent-blue: #38bdf8;
    }''',
        '''    :root {
      --bg: #090d16;
      --surface: #121826;
      --surface-elevated: #172033;
      --surface-inset: #0c101a;
      --border: #1e283d;
      --border-subtle: rgba(255, 255, 255, 0.07);
      --text-primary: #f8fafc;
      --text-secondary: #cbd5e1;
      --text-muted: #7d8b9e;
      --accent: #2563eb;
      --accent-hover: #3b82f6;
      --accent-subtle: rgba(37, 99, 235, 0.12);
      --amber: #d97706;
      --amber-hover: #f59e0b;
      --amber-subtle: rgba(217, 119, 6, 0.12);
      --green: #10b981;
      --green-subtle: rgba(16, 185, 129, 0.12);
    }'''
    ),
    (
        '''    :root {
      --bg: #0a0f1d;
      --card-bg: #0f172a;
      --card-hover: #131d31;
      --border: #1e293b;
      --text: #f3f4f6;
      --muted: #94a3b8;
      --accent-cyan: #06b6d4;
      --accent-gold: #f59e0b;
      --accent-blue: #38bdf8;
    }''',
        '''    :root {
      --bg: #090d16;
      --surface: #121826;
      --surface-elevated: #172033;
      --surface-inset: #0c101a;
      --border: #1e283d;
      --border-subtle: rgba(255, 255, 255, 0.07);
      --text-primary: #f8fafc;
      --text-secondary: #cbd5e1;
      --text-muted: #7d8b9e;
      --accent: #2563eb;
      --accent-hover: #3b82f6;
      --accent-subtle: rgba(37, 99, 235, 0.12);
      --amber: #d97706;
      --amber-hover: #f59e0b;
      --amber-subtle: rgba(217, 119, 6, 0.12);
      --green: #10b981;
      --green-subtle: rgba(16, 185, 129, 0.12);
    }'''
    ),
    # Remove text-gradient clipping
    (
        '''    h1 span {
      color: var(--accent-cyan);
      background: linear-gradient(135deg, #06b6d4 0%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }''',
        '''    h1 span {
      color: #93c5fd;
    }'''
    ),
    # Remove hero button neon gradients
    (
        '''    .hero-btn.primary {
      background: linear-gradient(135deg, #06b6d4 0%, #38bdf8 100%);
      color: #000 !important;
      box-shadow: 0 4px 20px rgba(6, 182, 212, 0.4);
    }
    .hero-btn.primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 25px rgba(6, 182, 212, 0.6);
      color: #000 !important;
    }''',
        '''    .hero-btn.primary {
      background: var(--accent);
      color: #ffffff !important;
      border: 1px solid var(--accent);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
    }
    .hero-btn.primary:hover {
      background: var(--accent-hover);
      border-color: var(--accent-hover);
      transform: translateY(-1px);
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
      color: #ffffff !important;
    }'''
    ),
    # Secondary and outline hero buttons
    (
        '''    .hero-btn.secondary {
      background: #151e32;
      color: #f8fafc !important;
      border: 1px solid #334155;
    }
    .hero-btn.secondary:hover {
      background: #1e293b;
      color: #fff !important;
      transform: translateY(-2px);
      border-color: var(--accent-cyan);
    }
    .hero-btn.outline {
      background: rgba(245, 158, 11, 0.1);
      color: var(--accent-gold) !important;
      border: 1px solid rgba(245, 158, 11, 0.4);
    }
    .hero-btn.outline:hover {
      background: rgba(245, 158, 11, 0.2);
      transform: translateY(-2px);
    }''',
        '''    .hero-btn.secondary {
      background: var(--surface);
      color: var(--text-primary) !important;
      border: 1px solid var(--border);
    }
    .hero-btn.secondary:hover {
      background: var(--surface-elevated);
      color: #fff !important;
      transform: translateY(-1px);
      border-color: var(--accent);
    }
    .hero-btn.outline {
      background: var(--amber-subtle);
      color: #fbbf24 !important;
      border: 1px solid rgba(217, 119, 6, 0.35);
    }
    .hero-btn.outline:hover {
      background: rgba(217, 119, 6, 0.2);
      transform: translateY(-1px);
    }'''
    ),
    # Remove emojis from hero action buttons
    (
        '<span>📚 The 9 Engineering Volumes &rarr;</span>',
        '<span>The 9 Engineering Volumes &rarr;</span>'
    ),
    (
        '<span>👤 About Tristan &amp; Credentials</span>',
        '<span>About Tristan &amp; Credentials</span>'
    ),
    (
        '<span>📖 Technical Blog (68)</span>',
        '<span>Field Protocols (68)</span>'
    ),
    (
        '<span>🔍 Search All 68 Protocols</span>',
        '<span>Search All 68 Protocols</span>'
    ),
    (
        'tier_badge = "★ FLAGSHIP DEEP-DIVE GUIDE" if is_deep_dive else "AUDITABLE FIELD PROTOCOL"',
        'tier_badge = "FLAGSHIP GUIDE" if is_deep_dive else "AUDITABLE FIELD PROTOCOL"'
    ),
    (
        '<span class="meta-time">⏱️ {read_mins} MIN READ</span>',
        '<span class="meta-time"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> {read_mins} MIN READ</span>'
    ),
    # Update direct-answer blockquote
    (
        '''    blockquote.direct-answer {
      background: #111e33;
      border-left: 4px solid var(--accent-cyan);
      padding: 1.25rem 1.5rem;
      margin: 1.8rem 0;
      border-radius: 0 8px 8px 0;
      font-size: 1.15rem;
      font-weight: 500;
      color: #e2e8f0;
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }''',
        '''    blockquote.direct-answer {
      background: #111726;
      border: 1px solid var(--border);
      border-left: 3px solid var(--accent);
      padding: 1.25rem 1.6rem;
      margin: 2rem 0;
      border-radius: 0 6px 6px 0;
      font-size: 1.125rem;
      line-height: 1.7;
      color: #e2e8f0;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    }'''
    ),
    # Brand mark update
    (
        '''    .brand {
      font-weight: 800;
      color: #fff;
      text-decoration: none;
      font-size: 1.1rem;
      letter-spacing: 0.05em;
    }
    .brand span { color: var(--accent-cyan); }''',
        '''    .brand {
      font-weight: 800;
      color: #fff;
      text-decoration: none;
      font-size: 1.05rem;
      letter-spacing: 0.04em;
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
    }
    .brand-mark {
      width: 10px;
      height: 10px;
      background: var(--accent);
      border-radius: 2px;
      display: inline-block;
      flex-shrink: 0;
    }
    .brand span { color: #94a3b8; font-weight: 600; font-size: 0.92rem; }'''
    ),
    (
        '''    .brand {
      font-weight: 800;
      color: #fff;
      text-decoration: none;
      font-size: 1.15rem;
      letter-spacing: 0.05em;
    }
    .brand span { color: var(--accent-cyan); }''',
        '''    .brand {
      font-weight: 800;
      color: #fff;
      text-decoration: none;
      font-size: 1.05rem;
      letter-spacing: 0.04em;
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
    }
    .brand-mark {
      width: 10px;
      height: 10px;
      background: var(--accent);
      border-radius: 2px;
      display: inline-block;
      flex-shrink: 0;
    }
    .brand span { color: #94a3b8; font-weight: 600; font-size: 0.92rem; }'''
    ),
    (
        '''<a href="../index.html" class="brand">DATA CENTER <span>FIELD GUIDES</span></a>''',
        '''<a href="../index.html" class="brand"><span class="brand-mark"></span>DATA CENTER <span>FIELD GUIDES</span></a>'''
    ),
    (
        '''<a href="{home_link}" class="brand">DATA CENTER <span>FIELD GUIDES</span></a>''',
        '''<a href="{home_link}" class="brand"><span class="brand-mark"></span>DATA CENTER <span>FIELD GUIDES</span></a>'''
    ),
    (
        '''<a href="index.html" class="brand">DATA CENTER <span>FIELD GUIDES</span></a>''',
        '''<a href="index.html" class="brand"><span class="brand-mark"></span>DATA CENTER <span>FIELD GUIDES</span></a>'''
    )
]

count = 0
for target, repl in replacements:
    # Need to handle double curly braces in python f-string code
    t_escaped = target.replace("{", "{{").replace("}", "}}")
    r_escaped = repl.replace("{", "{{").replace("}", "}}")
    if t_escaped in code:
        code = code.replace(t_escaped, r_escaped)
        count += 1
    elif target in code:
        code = code.replace(target, repl)
        count += 1
    else:
        print(f"Notice: pattern not found, trying raw regex or snippet...")

print(f"Applied {count} design system updates.")
BUILD_SCRIPT.write_text(code, encoding="utf-8")
