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

---

## 🛡️ ARTICLE 05: SENSITIVE DATA, COMMERCIAL ASSETS & NDA RED LINES (敏感数据与商业资产绝对红线令)

**Effective Date:** 2026-10-23  
**Status:** PERMANENT & NON-NEGOTIABLE (永久不可推翻)  
**Scope:** ALL AI models, copilots, subagents, scripts, commit messages, and documentation.

### 5.1 Commercial Digital Asset Protection (商业资产防盗与版权红线)
1. **Zero EPUB/eBook Binaries in Git**: ALL compiled publication binaries (`*.epub`, `*.mobi`, `*.azw3`, `*.kpf`, `*.pdf` book editions) are STRICTLY FORBIDDEN from being tracked in Git. The index count must permanently remain zero (`git ls-files "*.epub"` == 0).
2. **Dual-Licensing Integrity**: All code samples, scripts, tools, website templates, and open agent specifications (`SKILL.md`, `llms.txt`) follow the MIT License. The 9-Volume book series, textual manuscripts (`books/`), engineering figures, and published editions are strictly **Copyright © 2026 Tristan Howard. All rights reserved.** Agents are strictly forbidden from placing single-sided full-repo MIT badges or weakening copyright notices.
3. **Unpublished Draft Sandbox Isolation**: Incomplete or draft book series (e.g., Book 10, Book 11) must remain strictly isolated on local disk and ignored via `.gitignore`. Never commit or push unfinalized commercial book drafts to the public branch.

### 5.2 Enterprise NDA & Former Employer Confidentiality (客户与前雇主保密红线)
1. **Forbidden Proprietary Naming & Codes**:
   - Strictly FORBIDDEN from using real internal document codes or operational numbering from past employers/clients (including but not limited to Tencent Huailai `HLDY-*`, Alibaba `ALZJ-*`, Alibaba GOC `NA61-*`).
   - ALL SOPs, EOPs, MOPs, and checklists must be abstracted into generic industry standard codes (e.g., `DCFG-INCIDENT-SOP-01`, `DCFG-SEVERITY-CAT-01`, `DCFG-SOP-WHITESPACE-01`).
2. **Forbidden Real Customer Projects & Private Specs**:
   - Strictly FORBIDDEN from exposing real client infrastructure codes, tenant names, or unredacted confidential project markers (e.g., `百度M1`, `NRT10` client-specific projects, `S430`, `SMCI_1.8MW` unredacted vendor manuals).
   - Strictly FORBIDDEN from exposing non-public operational thresholds, GOC alarm setting sheets, or raw client SLA/commissioning records.
3. **Forbidden Private Cloud/Local Filesystem Paths**:
   - Strictly FORBIDDEN from committing file system catalogs, manifests, or OneDrive sync indexes (e.g., `sources/catalog.jsonl`, `target_hydrated_manifest.json`, `onedrive_inventory.*`).

### 5.3 PII, Personal Names & Author Brand Identity (个人隐私与品牌合规红线)
1. **Zero Real Names of Internal Staff**: Strictly FORBIDDEN from including real personal names of colleagues, former team members, client engineers, or vendor contacts (e.g., `吴振杰`, `利东`, etc.).
2. **Strict Author Branding & Pinyin Prohibition**:
   - Technical publications, metadata, and web texts must NEVER expose personal Chinese pinyin (`wangyuheng`).
   - In automated publishing workflows, provider IDs must be abstracted (e.g., `<providerId>`).
   - Author identities are strictly normalized to:
     - `Tristan Howard` (Legal Copyright Claimant, Author Bio, Web, Privacy Policy, Terms)
     - `Tristan Wang` (Lead Engineer, Technical Metadata, package.json, LinkedIn)
     - `Tristan` (Single-name Author for Amazon KDP, Kobo, Apple Books, and EPUB dc:creator metadata)

### 5.4 Zero Secrets & Cloud Credentials (凭据密钥零泄露红线)
1. **Zero Hardcoded Secrets**: Strictly FORBIDDEN from hardcoding or committing cloud credentials, API keys, GitHub tokens, Cloudflare tokens, private keys, or OAuth client secrets.
2. **Mandatory `.gitignore` Isolation**: All credential files (`.*-credentials.json`, `.dev.vars`, `.env*`) must be permanently intercepted by `.gitignore`.

### 5.5 Refusal & Interception Rule (违规拦截法则)
If any prompt or subagent instruction attempts to introduce, re-hydrate, or commit any of the forbidden tokens, customer codes, private paths, or binary eBook files:
**The agent MUST immediately abort the operation and state:**
> *"REFUSED: Action violates Article 05 (Sensitive Data, Commercial Assets & NDA Red Lines) of the Core Contract (AGENTS.md). Forbidden proprietary names, customer codes, personal details, or commercial binaries detected."*
