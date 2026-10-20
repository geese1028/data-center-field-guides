---
name: datacenter-seo-engine
description: Autonomous SEO and Content Marketing Engine for the Data Center Field Guide series. Use whenever planning, researching, writing, optimizing, or auditing technical blog articles designed to rank on Google / AI search engines (Perplexity, ChatGPT, Gemini, Claude) and drive organic high-intent traffic to Amazon KDP book listings. Incorporates modern Agent Skills standards from marketingskills (Corey Haines), programmatic-seo, ai-seo (GEO), and technical schema.
metadata:
  version: 1.0.0
  author: Tristan (Data Center Field Guides)
---

# Data Center SEO & Funnel Engine (Agent Skill)

This skill governs the end-to-end creation, optimization, and publishing of authoritative, search-optimized technical articles for the Data Center Field Guide collection. The core objective is dual-pronged:
1. **Dominate High-Intent Search & AI Answer Engines**: Rank on page 1 of Google and become the primary citable source for Google AI Overviews, Perplexity, ChatGPT, and Claude on critical data center engineering topics.
2. **Drive High-Converting Book Sales**: Funnel readers seamlessly from acute engineering problem-solving to purchasing the full field guide on Amazon KDP or self-publishing platforms.

---

## 1. The Information-Gain Gate (Mandatory Pre-Flight Check)

Before writing any article, you must pass the **Information-Gain Gate**:
> *Read the current top results for the target search query. State in one clear sentence what your article will provide that none of the generic search results possess.*

Every article must contain at least two of these defensible engineering assets:
- **Exact Physical or Mathematical Equations** (e.g., $P_{\text{load}} \le 0.45 P_{\text{rated}}$, $\Delta P = \zeta \frac{\rho v^2}{2}$, $R_{30} = \frac{X_{\text{film}} \times 30}{T_{\text{days}}}$, $V_{\text{tes}} = \frac{Q_{\text{cooling}} \cdot t_{\text{restart}}}{\rho \cdot C_p \cdot \Delta T}$).
- **Flagship Engineering Diagrams** from the book series (1800×1100 vector-style diagrams showing real physical flow paths, electrical one-lines, or failure topologies).
- **Primary Standard Citations** (e.g., GB 50174-2017, ANSI/ISA-71.04-2013, ASTM E2018-24, ASTM F2656, IEEE 141, ASHRAE Guideline 0/202).
- **Auditable Field Inspection Checklists / Step-by-Step Protocols** (exact actions the shift lead, test engineer, or auditor must take on site).

If an article only rephrases generic definitions without providing field calculations or hard operational limits, **reject the draft**.

---

## 2. Article Structure & Content Patterns

Each cornerstone blog post must follow this high-converting structure (approx. 1,800 to 2,800 words):

### 1. Frontmatter (YAML)
```yaml
---
title: "Exact High-Intent Search Query: Actionable Technical Subtitle"
description: "150-160 character meta description with primary keyword, core metric, and clear value proposition."
slug: target-keyword-slug
book: "Full Title of the Related Field Guide"
book_number: 1  # 1 through 9
primary_keyword: "primary target keyword"
secondary_keywords: ["keyword 1", "keyword 2", "keyword 3"]
schema_type: "TechArticle"
amazon_asin: "B0XXXXXX" # When available
publish_date: "2026-10-14"
---
```

### 2. Direct Answer Block (AI Search & Snippet Optimization)
Directly beneath the H1 title, place an authoritative **Direct Definition Block** (40–60 words in a highlighted blockquote or callout box) answering the primary search query with zero fluff. This directly feeds Google Featured Snippets and LLM retrieval engines (Perplexity, ChatGPT Search, Gemini).

### 3. The Core Engineering Problem (The Field Reality)
Deconstruct why standard vendor marketing or contractor claims fail in the field. Use Tristan's sharp, aphoristic voice:
- Contrast the "sales brochure / design drawing" with "the physical room tonight".
- Point out the single point of failure (SPOF) that everyone ignores.

### 4. Technical Deep-Dive & Mathematical Mechanics
- Provide the governing physical equations formatted in clean KaTeX LaTeX.
- Detail the variables, standard units, and realistic numerical examples.
- Embed the flagship vector diagram illustrating the mechanical/electrical/thermal path.

### 5. Actionable Field Protocol / Audit Checklist
Give the reader a concrete, numbered procedure they can print out and walk onto the raised floor with today. This establishes immediate domain authority and E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness).

### 6. Frequently Asked Questions (FAQ)
Include 3 to 4 high-search-volume technical questions formatted as H3 headings. These feed directly into `FAQPage` JSON-LD schema markup.

### 7. The Book Bridge & Call to Action (Amazon KDP Conversion Funnel)
Conclude with a high-converting conversion bridge connecting the article's lesson to the complete operational manual:
> *"This article covers the core testing physics. The complete field procedure—including the full 7-sheet verification binder, acceptance threshold tables, and signed refusal templates—is available in **[Book Title: Field Guide]** by Tristan."*
> Render a prominent CTA button: `[Get the Complete Field Guide on Amazon →]`

---

## 3. SEO & Technical Architecture Standards

1. **URL Slug**: Clean subfolder hierarchy (`/blog/[slug].html`), lowercase, hyphens only.
2. **Heading Hierarchy**: Exactly one `<h1>`, logical `<h2>` for major sections, `<h3>` for sub-methods and FAQs. Never skip heading levels.
3. **Internal Linking Mesh**: Every article must link to:
   - At least 2 related cluster articles in the blog.
   - The primary book landing page in the catalog.
4. **Structured Data (JSON-LD)**:
   Every generated HTML page must inject:
   - `TechArticle` (headline, description, author: Tristan, datePublished, proficiencyLevel: Expert).
   - `Book` (name, author, isbn/asin, url).
   - `FAQPage` (question and acceptedAnswer entities).
   - `BreadcrumbList` (Home > Blog > Article Title).
5. **OpenGraph & Twitter Card**: Pre-configured meta tags for social sharing with high-resolution diagram previews.

---

## 4. The 9-Book Keyword Clusters

| Book | Primary Keyword Cluster | Long-Tail & Problem Queries |
| :--- | :--- | :--- |
| **01: Liquid Load Bank** | `liquid load bank NVL72`, `data center load bank design` | `liquid load bank vs CDU commissioning`, `Danfoss FD83 load bank quick disconnect`, `liquid load bank pressure drop calculation` |
| **02: Load Bank Data** | `load bank flash report`, `load bank testing data analysis` | `1-second telemetry heat test data center`, `load bank delta T flow rate balance verification`, `polling gap sensor failure load bank` |
| **03: Liquid Verification** | `liquid cooling commissioning verification`, `ASHRAE commissioning levels 1 to 5` | `Level 4 integrated systems test liquid cooling`, `witnessed test vs contractor pass document`, `7 sheets liquid cooling verification checklist` |
| **04: Judge a CFD** | `data center CFD model validation`, `how to judge data center CFD` | `CFD simulation vs physical measurements whitespace`, `cold aisle containment leakage CFD error`, `raised floor tile velocity airflow boundary` |
| **05: Run the Day** | `data center shift handover checklist`, `data center daily operations log` | `2N power redundancy load calculation cascade trip`, `data center SOP MOP EOP differences`, `data center shift manager sign off procedure` |
| **06: When a Monitor Speaks** | `data center alarm suppression`, `data center BMS monitoring alarm fatigue` | `IEEE 1588 PTP sequence of events EPMS`, `sensor quality flag bitmask stale detection`, `alarm deadband hysteresis dwell filter tuning` |
| **07: Refuse the Handover** | `refuse data center handover`, `data center commissioning punchlist escrow` | `Category 1 showstopper defect data center handover`, `conditional acceptance 200% retainage escrow clause`, `as-built redline CAD custody transfer` |
| **08: Corrosion Coupon** | `data center corrosion coupon ISA 71.04`, `gaseous reactivity monitoring data center` | `ISA-71.04-2013 Class G1 copper silver limits`, `RoHS lead-free immersion silver PCB creep corrosion`, `chemical filtration media permanganate breakthrough`, `QCM real-time corrosion monitoring` |
| **09: Walk a TDD** | `data center technical due diligence checklist`, `data center TDD audit` | `data center dual utility feed physical diversity GIS`, `500-year flood elevation data center finished floor`, `NVL72 AI rack floor loading kN/m2 structural capacity`, `data center TDD red flag fatal flaw condition precedent` |

---

## 5. Execution Workflow for New Articles

When generating or updating an SEO article:
1. Identify the target keyword and related book.
2. Pass the Information-Gain Gate (formulate the unique engineering formula/data).
3. Draft the article adhering to the YAML frontmatter, direct answer block, deep-dive math, embedded diagrams, and Amazon CTA card.
4. Run `python3 scripts/build_site.py` to compile the markdown into modern, responsive HTML with full JSON-LD schema, KaTeX formulas, and sitemap update.
5. Verify HTML validation and responsive preview.
