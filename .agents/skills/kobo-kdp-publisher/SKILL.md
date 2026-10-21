---
name: multi-publisher-engine
description: Universal multi-platform eBook publishing, headless API ingestion, and storefront synchronization engine for Data Center Field Guides. Supports Amazon KDP, Rakuten Kobo Writing Life (KWL), Apple Books (CloudWorks / iTunes Connect), Leanpub, and Google Play Books. Use whenever publishing, uploading, or syncing book distribution links across platforms and lighting up storefront badges on the website.
metadata:
  version: 2.0.0
  author: Tristan (Data Center Field Guides)
---

# Universal Multi-Publisher Publishing & Site Sync Engine

This skill automates the metadata preparation, formatting, headless asset uploading, validation, and multi-publisher storefront synchronization for the *Data Center Field Guides* across **Amazon KDP**, **Rakuten Kobo Writing Life (KWL)**, **Apple Books**, **Leanpub**, and **Google Play Books**.

---

## 1. Core Metadata Source of Truth (SSOT)

All title, subtitle, author, description, category, and file paths are centralized in:
- `catalog/kdp_catalog.json` (Structured JSON for all 22 book editions across English, Japanese, Korean, Indonesian, Thai, and Arabic).
- `catalog/publisher_links.json` (Multi-publisher live destination URL mapping for all 9 volumes).
- `docs/PUBLISHING_PLAYBOOK.md` (Operational SOP & reverse-engineered technical specifications).

---

## 2. Platform Form & API Mapping

### Apple Books (CloudWorks & iTunes Connect)
- **Ingestion Mode**: Headless authenticated REST API (via active Chrome session).
- **Upload Endpoints**:
  - EPUB: `POST /epub-upload/uploads/epub`
  - Cover: `POST /epub-upload/uploads/cover`
  - Validation: `POST /epub-upload/api/v1/validate/epub`
  - Publish Submission: `POST /epub-upload/api/v1/publish/`
- **iTunes Connect Rights & Pricing**:
  - `My Books` -> Book Details -> `Rights and Pricing` -> `Add New Countries/Regions`.
  - USD $12.99 / Worldwide / Digital Only. Flat 70% royalty on Apple Books.

### Rakuten Kobo Writing Life (KWL)
- **URL**: `https://writinglife.kobo.com/ebook/create`
- **Automation Script**: `scripts/kobo_autopilot.py` (DOM metadata injection + macOS System Events native open-file sheet automation).
- **Categories**: `Computers > Hardware > General` and `Technology & Engineering > Mechanical`.
- **Pricing**: $12.99 USD, 70% royalty, Worldwide rights, Kobo Plus enabled.

### Amazon KDP
- **URL**: `https://kdp.amazon.com/title-setup/...`
- **Automation Pipeline**: `scripts/kdp_autofill.user.js` and `scripts/kdp_companion.html`.

---

## 3. Site Synchronization & Link Verification Workflow

Whenever a book is published on ANY platform:

1. **Update Registry & Rebuild Site**:
   ```bash
   python3 scripts/sync_publishers.py --publisher <apple|kobo|amazon|google|leanpub> --book <vol> --url "<destination_url>"
   ```
2. **Illuminates Icons on Homepage & Buy Gateway**:
   - The sync engine updates `catalog/publisher_links.json` and runs `scripts/build_site.py`.
   - The book's store block lights up from `is-disabled` (Coming Soon) to `is-active <publisher>` with authentic brand colors and SVG logos.
3. **Verify DOM & Test HTTP Resolution**:
   ```bash
   python3 scripts/sync_publishers.py --verify
   ```
   Ensures that every active link exists in the generated HTML and verifies network reachability.
