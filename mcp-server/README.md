# @dcfg/datacenter-auditor (Model Context Protocol Server)

> **Deterministic physical boundary and TDD commissioning engine for mission-critical AI hyperscale data centers, NVIDIA GB200 NVL72 liquid cooling loops, and Level 1-5 commissioning.**

Official MCP Server from [Data Center Field Guides](https://datacenterfieldguides.com).

## Tools Provided to Claude / Cursor / Zed

1. `audit_commissioning_script`: Deterministic audit of SOP, MOP, EOP, and Level 1-5 commissioning scripts against physical boundaries, refusal gates (Rule 01 to Rule 06), and Category A/B/C defect codes.
2. `verify_hydraulic_boundary`: Exact heat removal, mass flow ($\dot{m}$), required LPM/GPM, and ASHRAE Liquid Cooling Class (W1-W4) calculations for high-density AI clusters (NVL72 / GB200).
3. `search_field_protocols`: Semantic and keyword search across the 69 unredacted field commissioning protocols.
4. `lookup_defect_code`: Stop-work classification, root causes, and safety mandates for Category A, B, and C defects.
5. `classify_corrosion_severity`: ANSI/ISA-71.04-2013 Severity Level (G1-GX) classification for paired Copper & Silver 30-day reactivity coupons.

## Installation in Claude Desktop

Add this block to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "datacenter-auditor": {
      "command": "node",
      "args": ["/absolute/path/to/datacenterfieldguides/mcp-server/index.js"]
    }
  }
}
```

Or install via Smithery:

```bash
npx -y @smithery/cli install @dcfg/datacenter-auditor --client claude
```

## License

MIT © Tristan Wang (Data Center Field Guides)
