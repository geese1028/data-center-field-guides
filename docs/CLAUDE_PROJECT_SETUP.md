# Anthropic Claude Project & MCP Setup Guide: @Data Center Auditor

> **Goal**: Deploy **@Data Center Auditor** into the Claude ecosystem via both **Claude Desktop (MCP Server)** and **Claude.ai Web/Mobile (Custom Project)**.

---

## Track A: Claude Desktop (MCP Server) — Ready Right Now!

Your local Claude Desktop has **already been automatically configured**!

### Verification:
1. Open or restart the **Claude Desktop** application on your Mac.
2. In the bottom-right corner of any chat window, click the small hammer / plug icon (🛠️ Tools).
3. You will see **`datacenter-auditor`** with 5 tools:
   - `audit_commissioning_script`
   - `verify_hydraulic_boundary`
   - `search_field_protocols`
   - `lookup_defect_code`
   - `classify_corrosion_severity`

### Global Configuration for Other Claude Users:
Other engineers can connect their Claude Desktop to your auditor in 1 step:

Add this to their `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "datacenter-auditor": {
      "command": "npx",
      "args": ["-y", "@dcfg/datacenter-auditor"]
    }
  }
}
```

Or via Smithery CLI:
```bash
npx -y @smithery/cli install @dcfg/datacenter-auditor --client claude
```

---

## Track B: Claude.ai Web & Mobile (Claude Project)

For Claude.ai Pro / Team users on browser or iPhone/Android app:

1. Open [Claude.ai](https://claude.ai) and click **"Projects"** in the sidebar.
2. Click **"Create Project"**.
3. Set Name: `Data Center Auditor`
4. Set Project Instructions: Copy the prompt from `docs/GEMINI_GEM_SETUP.md` (or `SKILL.md`).
5. In Project Knowledge, upload: `/Users/geese/Downloads/book/SKILL.md` or `llms.txt`.
6. Click **"Save"**.
7. In Project Settings, set Sharing to **"Share with link"** or add team members.
