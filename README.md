# Data Center Field Guides (DCFG) // AI Agent Specification & MCP Server

[![smithery badge](https://smithery.ai/badge/datacenter-field-auditor)](https://smithery.ai/server/datacenter-field-auditor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Website](https://img.shields.io/badge/Website-datacenterfieldguides.com-0284c7.svg)](https://datacenterfieldguides.com)

Deterministic physical boundary and Technical Due Diligence (TDD) commissioning Model Context Protocol (MCP) server for mission-critical data centers and NVIDIA GB200 NVL72 liquid cooling.

This repository hosts the official companion tools, agent skill specifications ([`SKILL.md`](SKILL.md)), ground-truth context ([`llms.txt`](llms.txt)), and MCP server for the **Data Center Field Guides** engineering series by Tristan.

---

## Ecosystem Links

- 🌐 **Official Website & Field Protocols**: [datacenterfieldguides.com](https://datacenterfieldguides.com)
- 📚 **Bookstore & Published Volumes**: Available on [Amazon Kindle](https://www.amazon.com/author/tristanhoward), Apple Books, and Google Play Books.
- 🤖 **Agent Specification**: [`SKILL.md`](SKILL.md) and [`llms.txt`](llms.txt).

---

## Quick Start: MCP Server

The Data Center Auditor MCP server provides AI models (Claude, Cursor, Antigravity, Windsurf) with deterministic physical calculation tools, P&ID hydraulic validation, and standards checking across ASHRAE, ASME, NFPA, and ANSI/ISA frameworks.

### Installing via Smithery

To install Data Center Auditor for Claude Desktop automatically via [Smithery](https://smithery.ai/server/datacenter-field-auditor):

```bash
npx -y @smithery/cli install datacenter-field-auditor --client claude
```

### Manual Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "datacenter-auditor": {
      "command": "npx",
      "args": ["-y", "datacenter-auditor"]
    }
  }
}
```

Or run directly from source:

```bash
cd mcp-server
npm install
node index.js
```

---

## Agent Capabilities & Tools

1. **`calculate_liquid_cooling_hydraulics`**: Evaluates primary and secondary CDU loops, calculating mass flow rates, Darcy-Weisbach pressure drops, and enthalpy closure balances across high-density AI clusters (e.g., 120 kW–132 kW NVL72 racks).
2. **`verify_electrical_capacity`**: Audits 2N switchgear continuous bus loading, enforcing symmetric thresholds (≤ 45% for 100%-rated switchgear; ≤ 40% for standard 80%-rated UL 489 breakers).
3. **`audit_alarm_suppression_matrix`**: Validates telemetry quality propagation (OPC UA IEC 62541-4 StatusCodes vs legacy OPC DA), requiring parent-child alarm suppression, analog deadbands, and IEEE 1588v2 PTP (≤ 1 µs) / NTP (≤ 10 ms) clock alignment.
4. **`validate_cfd_model`**: Enforces physical empirical validation gates on computational fluid dynamics (CFD) models, requiring multi-point vertical inlet sensor arrays and MAE thresholds (≤ 1.5 K).

---

## License

This project is licensed under the terms of the [MIT License](LICENSE).

The accompanying 10-volume book series, textual manuscripts, and published editions are strictly **Copyright © 2026 Tristan Howard. All rights reserved.**
