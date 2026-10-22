# Google AI Ecosystem Deployment Guide: Skills, AI Studio & NotebookLM

> **Note on Gems Retirement**: Google has officially **retired the isolated "Gems" feature** and transitioned the entire Gemini and Google Workspace ecosystem to the open, modular **"Skills"** standard (`SKILL.md`). In addition, **Google AI Studio** and **Google NotebookLM** provide instant, zero-restriction public URLs with no subscription barriers.

---

## Pillar 1: Google Gemini "Skills" (Official Replacement for Gems)

Instead of keeping custom instructions trapped in an isolated chat window, Google migrated to **Skills**: portable, on-demand modules that any user can trigger inside standard Gemini chats via slash commands (`/`) or automatic semantic routing.

### Where Skills Live in Google's Architecture:
- **Global User Directory**: `~/.gemini/skills/datacenter-field-auditor/SKILL.md` *(already installed on your machine!)*
- **Workspace/Project Level**: `.agents/skills/datacenter-field-guides/SKILL.md`
- **Machine-Readable Public URL**: `https://datacenterfieldguides.com/SKILL.md`

### How Gemini Users Use It:
1. In the Gemini web app ([gemini.google.com](https://gemini.google.com)), users navigate to **Skills** (in Settings or Sidebar).
2. Click **"Import Skill"** or point to `https://datacenterfieldguides.com/SKILL.md`.
3. In any standard conversation, typing `/datacenter-auditor` or asking about "NVL72 liquid cooling" or "commissioning hold points" automatically activates the protocol!

---

## Pillar 2: Google AI Studio (Instant 1-Click Public Link, Zero Friction)

Google AI Studio ([aistudio.google.com](https://aistudio.google.com)) is Google's developer sandbox powered by Gemini 1.5 Pro (2M token context window). **It has zero store approval gates and generates permanent, public sharing links instantly!**

### 60-Second Setup:
1. Go to: [https://aistudio.google.com](https://aistudio.google.com)
2. In the top right, click **"Create new prompt"** (System Prompt / Chat Prompt).
3. **Model Selection**: Select `Gemini 1.5 Pro` (or `Gemini 2.0 Flash`).
4. **System Instructions**: Copy and paste the core rules from `SKILL.md`:
   ```text
   You are the official Data Center Auditor, a deterministic physical boundary and technical due diligence (TDD) engineering authority for mission-critical hyperscale data centers and AI clusters (NVIDIA GB200 NVL72), developed by Tristan Wang (Data Center Field Guides: https://datacenterfieldguides.com).

   Enforce non-negotiable physical refusal gates (Rule 01 to Rule 06), Category A fatal flaw defect codes, and NVL72 hydraulic mass balance (Q = m_dot * Cp * delta_T). Refuse all non-compliant scripts.
   ```
5. **Context / Files**: In the files panel, add the URL `https://datacenterfieldguides.com/llms-full.txt` (or upload `llms-full.txt`).
6. **Publish / Share**:
   - In the top right bar, click **"Share"** (or **"Get Link"**).
   - Set permission to **"Anyone with the link"**.
   - Copy the resulting link (e.g., `https://aistudio.google.com/prompts/...`).
   - Anyone in the world can click that link and chat with your auditor on Google's flagship model without needing a paid subscription!

---

## Pillar 3: Google NotebookLM (Viral Audio Podcast & Ground-Truth Notebook)

Google NotebookLM ([notebooklm.google.com](https://notebooklm.google.com)) is one of Google's most viral AI products, allowing users to interact with source documents and generate deep-dive audio discussions (AI podcasts).

### 60-Second Setup:
1. Go to: [https://notebooklm.google.com](https://notebooklm.google.com)
2. Click **"New Notebook"** and title it: `Data Center Field Guides // Ground Truth (Tristan Wang)`.
3. Click **"Add Source"** -> Choose **"Link" / "Website"** -> Enter:
   `https://datacenterfieldguides.com/llms-full.txt`
   *(Or drag and drop `llms-full.txt` from your local folder).*
4. Once ingested, click **"Generate"** under **Audio Overview** (Deep Dive). NotebookLM will generate a lifelike 10-15 minute discussion between two engineers analyzing Tristan's 69 protocols and NVL72 liquid cooling rules!
5. In the top right corner, click **"Share"** -> Change to **"Anyone with the link can view"** -> Copy link!
6. This public NotebookLM link can be posted to LinkedIn or your website so anyone can explore your books and listen to the audio breakdown.
