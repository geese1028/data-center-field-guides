# Data Center Field Guides: Universal Multi-Publisher Publishing Playbook
=============================================================================

> **Document Version**: 2.0.0  
> **Status**: Production Reference & Operational SOP  
> **Author**: Tristan & AI Automation Subsystem  
> **Scope**: English Editions (Vols 1–9) priority sequence (1 book/day). Japanese Editions (Vols 1–9) strictly frozen pending Gemini 4 quota restoration and author audit.

---

## 1. Architecture & Single Source of Truth (SSOT)

All volume metadata, engineering synopses, BISAC category codes, and file assets are strictly centralized:

- **Structured Catalog Database**: [`catalog/kdp_catalog.json`](file:///Users/geese/Downloads/book/catalog/kdp_catalog.json)
  Contains 22 full volume specifications (English, Japanese, Arabic, Indonesian, Korean, Thai).
- **Multi-Publisher Distribution Registry**: [`catalog/publisher_links.json`](file:///Users/geese/Downloads/book/catalog/publisher_links.json)
  Live mapping of all 9 volumes across Amazon, Kobo, Leanpub, Google Books, and Apple Books.
- **Kobo Queue Pipeline**: [`catalog/kobo_queue.json`](file:///Users/geese/Downloads/book/catalog/kobo_queue.json)
  Staging queue for sequential daily batch publishing.
- **Asset Hierarchy**:
  - EPUB Files: `books/<volume-slug>/epub/<lang>/<filename>.epub`
  - High-Res Artwork: `books/<volume-slug>/figures/cover.jpg` (1600x2560px or equivalent 1:1.6 / 3:4 aspect ratio)

---

## 2. Publisher-Specific Operational SOPs

### 2.1 Amazon Kindle Direct Publishing (KDP)

- **Storefront**: Amazon Kindle Store (Worldwide, 70% Royalty Tier).
- **Entry Point**: `https://kdp.amazon.com/title-setup/...`
- **Automation Pipeline**:
  - `scripts/kdp_autofill.user.js` (Tampermonkey / Violentmonkey userscript)
  - `scripts/kdp_companion.html` (Local companion runner for 1-click clipboard paste)
- **Key Fields**:
  - Author: Primary `Tristan` (no last name).
  - Pricing: `$12.99 USD` (KDP 70% royalty requires price between $2.99 and $9.99 for 70%, or $12.99 for 35% standard; set to $9.99 for 70% or $12.99 based on volume thickness).
  - Keywords: 7 specialized engineering keywords (e.g. `Liquid Cooling P&ID`, `NVL72 Commissioning`, `Load Bank Hydraulics`).
  - DRM: Do NOT enable digital rights management (DRM-free technical reference).
- **Post-Publish Step**:
  Once Amazon generates the ASIN (e.g. `B0HMWDV6LT`), update `catalog/publisher_links.json`:
  ```bash
  python3 scripts/sync_publishers.py --publisher amazon --book <vol> --url "https://www.amazon.com/dp/<ASIN>"
  ```

---

### 2.2 Rakuten Kobo Writing Life (KWL)

- **Storefront**: Rakuten Kobo Global Network (OverDrive, Fnac, Booktopia, Indigo, Rakuten Japan).
- **Entry Point**: `https://writinglife.kobo.com/ebook/create`
- **Automation Pipeline**:
  - `scripts/kobo_autopilot.py` (Autonomous end-to-end publisher driving Chrome via macOS System Events).
  - Auto-selects categories: `Computers > Hardware > General` and `Technology & Engineering > Mechanical`.
  - Injects Title, Subtitle, Author (`Tristan`), Publisher (`Data Center Field Guides`), and Synopsis.
  - Native file upload: invokes Chrome file dialog -> sends `Cmd+Shift+G` -> pastes path -> hits Enter.
  - Waits for cloud EPUB conversion and automatically clicks red `Publish` button.
- **Post-Publish Step**:
  Kobo assigns a 13-digit digital ISBN/Query ID (e.g. `1990000032332`). Update the registry:
  ```bash
  python3 scripts/sync_publishers.py --publisher kobo --book <vol> --url "https://www.kobo.com/search?query=<ID>"
  ```

---

### 2.3 Apple Books (CloudWorks & iTunes Connect)

- **Storefront**: Apple Books Store (175 territories, flat 70% royalty regardless of price).
- **Web App**: `https://authors.apple.com/epub-upload/start`
- **Management Portal**: `https://itunesconnect.apple.com/WebObjects/iTunesConnect.woa/da/books`
- **Reverse-Engineered Headless REST API (100% Hands-Off)**:
  Apple Books web frontend uses Apple's internal CloudWorks UI framework. Instead of brittle DOM mouse clicks or file dialogs, use authenticated `fetch` inside Chrome session:
  1. **EPUB Upload**:
     - `POST /epub-upload/uploads/epub`
     - Headers: `X-Csrf-Token: <token>`, `X-Request-Id: <uuid>`
     - Body: `FormData` with `file: <epubBlob>`
     - Returns: `{ "data": { "key": "<epubKey>" } }`
  2. **Cover Upload**:
     - `POST /epub-upload/uploads/cover`
     - Returns: `{ "data": { "key": "<coverKey>" } }`
  3. **EPUB Validation Task**:
     - `POST /epub-upload/api/v1/validate/epub`
     - Body: `{ "epubKey": "<epubKey>", "providerId": "wangyuheng" }`
     - Poll `GET /epub-upload/api/v1/validate/status/<taskId>` until `status: "finished"`, `stage: "complete"`.
  4. **Generate Vendor ID**:
     - `GET /epub-upload/api/v1/metadata/providers/wangyuheng/generate_vendor_id`
  5. **Final Publish Submission**:
     - `POST /epub-upload/api/v1/publish/`
     - Body: Complete `Ps` JSON payload (Vendor ID, Title, Subtitle, Author `Tristan`, Series `Data Center Field Guides` + Vol `1`, BISAC `COM067000`, Language `eng`, assets: full + artwork).
     - Poll `GET /epub-upload/api/v1/publish/status/<publishId>` until `status: "finished"`, `stage: "complete"`.
- **iTunes Connect Rights & Pricing**:
  - Open `My Books` in iTunes Connect.
  - Book appears immediately under Recent Activity with Apple ID (e.g. `6825184697`).
  - In `Rights and Pricing` -> `Add New Countries/Regions`:
    - Base Currency: `USD - US Dollar` (`105`).
    - Release Type: `Digital Only` (`1`).
    - Suggested Apple Books Price: `$12.99`.
    - Countries: Click `Select All` (175 territories).
    - Note: Paid Books Agreement requires 24h bank review before pricing goes live globally.
- **Post-Publish Step**:
  ```bash
  python3 scripts/sync_publishers.py --publisher apple --book <vol> --url "http://books.apple.com/us/book/id<AppleID>"
  ```

---

### 2.4 Leanpub

- **Storefront**: Leanpub (PDF, EPUB, direct digital downloads).
- **Entry Point**: `https://leanpub.com/<slug>`
- **Workflow**: Direct Git-based / Ingest publishing from markdown sources.

---

### 2.5 Google Play Books (Upcoming Expansion)

- **Storefront**: Google Play Store Books (Worldwide).
- **Entry Point**: Google Play Books Partner Center (`play.google.com/books/publish`).
- **Prerequisites**:
  - Partner account registration.
  - Payment profile verification (tax & bank account).
  - Territory rights (Worldwide 100%).
- **Pricing**: $12.99 USD (70% revenue share with Google Play Books).
- **Integration Command**:
  ```bash
  python3 scripts/sync_publishers.py --publisher google --book <vol> --url "https://play.google.com/store/books/details?id=<GoogleID>"
  ```

---

## 3. Universal Site Synchronization & Verification Protocol

Whenever a book is published on ANY platform, the following protocol **MUST** be executed immediately:

### Step 1: Update Publisher Links Registry
Update `catalog/publisher_links.json` via the CLI:
```bash
python3 scripts/sync_publishers.py --publisher <apple|kobo|amazon|google|leanpub> --book <vol_num> --url "<destination_url>"
```

### Step 2: Automatic Site Rebuild & Button Illumination
The sync engine automatically invokes `scripts/build_site.py`:
- Rebuilds all 9 Dedicated Book Volume Pillar Pages (`site/book/volume-0X-...html`).
- Rebuilds Store & Buy Gateway (`site/buy.html`).
- Rebuilds Homepage (`site/index.html`) and Blog Archive.
- Updates the interactive `Order Now` block:
  - If URL is set: renders `<a href="<url>" class="platform-btn is-active <publisher>">` with authentic SVG brand icon and hover states.
  - If URL is empty: renders `<span class="platform-btn is-disabled <publisher>">` (Coming Soon).

### Step 3: Automated DOM & HTTP Verification
Run the built-in verifier:
```bash
python3 scripts/sync_publishers.py --verify
```
The verifier performs:
1. **DOM Inspection**: Ensures the generated static HTML contains active clickable buttons with correct `href` attributes.
2. **HTTP Reachability Check**: Makes standard user-agent requests to verify destination connectivity:
   - `✓ HTTP 200`: Live & instantly purchasable.
   - `⚠ 403 (Bot Guard)`: Protected by Cloudflare / anti-scraping (verified functional in browser).
   - `⏳ 404 (In Review)`: Asset registered in iTunes Connect, awaiting store review / 24h bank clearing.

---

## 4. Current Distribution Matrix (Audited Live)

| Vol | Title (Short) | Amazon | Rakuten Kobo | Leanpub | Google Play | Apple Books |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **V01** | Liquid Load Bank (NVL72) | **✓ LIVE** | **✓ LIVE** | **✓ LIVE** | — | **✓ LIVE (`6825184697`)** |
| **V02** | Read Load Bank Data | **✓ LIVE** | In Queue | **✓ LIVE** | — | Next |
| **V03** | Liquid Cooling Verification | **✓ LIVE** | In Queue | **✓ LIVE** | — | Queued |
| **V04** | Commissioning Hard Hat | **✓ LIVE** | In Queue | — | — | Queued |
| **V05** | NVL72 Thermal Hydraulic | — | In Queue | — | — | Queued |
| **V06** | Rack-Level Flow Balancing | — | In Queue | — | — | Queued |
| **V07** | Facility Water Interfaces | — | In Queue | — | — | Queued |
| **V08** | CDU Hunting & Transient | — | In Queue | — | — | Queued |
| **V09** | Acceptance Sign-Off Binder | — | In Queue | — | — | Queued |
