# WORKSPACE CORE CONTRACT & GOVERNANCE DIRECTIVES
# Data Center Field Guides (datacenterfieldguides.com)

**Effective Date:** 2026-10-22  
**Authority:** Tristan Wang (Owner & Lead Author)  
**Applies To:** All AI Models, Copilots, Autonomous Agents (Antigravity, Claude, Gemini, GPT, Cursor, Windsurf, Subagents)

---

## 🔒 ARTICLE 01: ABSOLUTE WEBSITE DESIGN & UI FREEZE (网站页面绝对封版令)

### 1.1 Status: PERMANENTLY FROZEN (已正式封版)
The design, layout, visual hierarchy, styling, components, and structure of `datacenterfieldguides.com` (including `site/index.html`, `site/blog/`, `scripts/build_site.py` templates, CSS rules, navigation bars, hero layouts, and banners) are **PERMANENTLY FROZEN**.

### 1.2 Strict Universal Prohibition (严格禁止令)
**Starting today (2026-10-22), ALL AI models and autonomous agents are STRICTLY FORBIDDEN from modifying, refactoring, redesigning, adding, deleting, 'optimizing', or tweaking any aspect of the website design, layout, markup structure, or styling WITHOUT EXPLICIT, UNAMBIGUOUS WRITTEN AUTHORIZATION FROM THE USER.**

Any prompt asking to "make it look better", "add a new showcase", "add badges", or "tweak the layout" must be **REFUSED** unless the user provides explicit, direct consent to break this freeze.

---

## ⚡ ARTICLE 02: THE ONLY TWO PERMITTED MUTATIONS (唯一允许的两种例外操作)

The ONLY mutations permitted on the website without breaking the freeze are strictly limited to the following two operations:

### Exception A: Storefront Icon Activation (图书上架点亮图标)
- **Allowed Action**: When a volume in the publishing pipeline (e.g., Apple Books, Rakuten Kobo, Google Play Books) is approved and live with a verified, public consumer purchase URL, the agent may update the catalog metadata to remove `is-disabled` / light up the storefront icon.
- **Strict Limitation**: NO changes to the surrounding HTML structure, banner layouts, or site theme are permitted during this update.

### Exception B: Publishing New Technical Articles & Protocols (新增技术文章)
- **Allowed Action**: Adding new markdown files to the article/dossier folders (e.g. `docs/`) and executing `scripts/build_site.py` to incrementally compile new articles into the existing, frozen design templates.
- **Strict Limitation**: New articles MUST inherit the existing templates and CSS classes without modifying the global templates, global headers, or hero sections.

---

## 🛑 ARTICLE 03: AGENT REFUSAL & SELF-ENFORCEMENT (违规拦截判定)

If any task, subagent, or model instruction attempts to:
1. Modify `generate_hub_index` layout, hero buttons, or promotional banners in `scripts/build_site.py`.
2. Add new visual widgets, sidebars, third-party banners, or experimental badges to `site/index.html`.
3. Introduce unexpected cloud endpoints, serverless functions, or MCP servers to the production website.

**The agent MUST immediately reject the operation and state:**
> *"REFUSED: The website UI is officially frozen per Article 01 of the Core Contract (AGENTS.md). Only Storefront Icon Activation and New Protocol Publishing are permitted. Explicit user confirmation is required for any design modification."*

---

## 📚 ARTICLE 04: CORE PRODUCT FOCUS (聚焦实体核心资产)
The team's resources and agent workflows must remain 100% focused on real-world commercial assets:
1. **Amazon KDP & Multi-Storefront Book Distribution** (Volumes 01–04 live; Volumes 05–09 publishing pipeline).
2. **Deterministic Field Engineering Protocols** (First-principles ASHRAE, ASME, NFPA, ANSI/ISA standards).
3. **LinkedIn & Industry Authority Building** (8 unique engineering diagrams, no duplicates, safe intervals).
