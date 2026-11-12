#!/usr/bin/env node
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Initialize MCP Server
const server = new McpServer({
  name: 'datacenter-auditor',
  version: '1.0.0'
});

// Load Corpus if available
const ROOT_DIR = path.resolve(__dirname, '..');
const LLMS_FULL_PATH = path.join(ROOT_DIR, 'llms-full.txt');
const SKILL_MD_PATH = path.join(ROOT_DIR, 'SKILL.md');

let corpusText = '';
try {
  if (fs.existsSync(LLMS_FULL_PATH)) {
    corpusText = fs.readFileSync(LLMS_FULL_PATH, 'utf-8');
  } else if (fs.existsSync(SKILL_MD_PATH)) {
    corpusText = fs.readFileSync(SKILL_MD_PATH, 'utf-8');
  }
} catch (e) {
  // Silent fallback
}

// -------------------------------------------------------------
// TOOL 1: Audit Commissioning Script (MOP / SOP / EOP / IST)
// -------------------------------------------------------------
server.tool(
  'audit_commissioning_script',
  'Audits a data center commissioning script (MOP, SOP, EOP, or IST Level 1-5) against deterministic physical boundary rules and safety gates.',
  {
    script_text: z.string().describe('The raw text of the MOP, SOP, EOP or commissioning script to audit'),
    commissioning_level: z.enum(['L1', 'L2', 'L3', 'L4', 'L5', 'ALL']).optional().default('ALL').describe('Commissioning level being executed (L1 Factory, L2 Quality/Receipt, L3 Component/PFT, L4 System/FPT, L5 Integrated IST)')
  },
  async ({ script_text, commissioning_level }) => {
    const textLower = script_text.toLowerCase();
    const findings = [];
    let isCategoryA = false;

    // Check 1: Liquid vs Air Thermal Boundary (Rule 01)
    if (
      (textLower.includes('nvl72') || textLower.includes('gb200') || textLower.includes('liquid cooling') || textLower.includes('direct-to-chip')) &&
      (textLower.includes('air heater') || textLower.includes('resistive heater') || textLower.includes('air load bank')) &&
      !textLower.includes('liquid load bank')
    ) {
      isCategoryA = true;
      findings.push({
        code: 'CAT-A-01',
        rule: 'Liquid vs. Air Thermal Boundary Violation (Rule 01)',
        severity: 'CATEGORY A - IMMEDIATE REJECTION',
        finding: 'Script specifies resistive air heaters or air load banks for liquid-cooled NVL72 / GB200 infrastructure without verified liquid load rejection.',
        action: 'Refuse script. Mandate hydraulic liquid load bank with flow balance, delta-T measurement, and CDU step-transient verification at rack manifold.'
      });
    }

    // Check 2: MOP Governance - Point of No Return & Back-out (Rule 04)
    if (textLower.includes('mop') || textLower.includes('method of procedure')) {
      if (!textLower.includes('point of no return') && !textLower.includes('ponr')) {
        isCategoryA = true;
        findings.push({
          code: 'CAT-A-04',
          rule: 'State-Machine Governance Missing PONR (Rule 04)',
          severity: 'CATEGORY A - IMMEDIATE REJECTION',
          finding: 'MOP alters redundancy or performs switching without declaring an explicit Point of No Return (PONR).',
          action: 'Halt approval. Require explicit step identifying the exact physical switching action after which restoration must proceed forward rather than backward.'
        });
      }
      if (!textLower.includes('back-out') && !textLower.includes('backout') && !textLower.includes('abort') && !textLower.includes('rollback')) {
        findings.push({
          code: 'CAT-B-04',
          rule: 'Missing Pre-Verified Back-Out Procedure (Rule 04)',
          severity: 'CATEGORY B - DEFICIENCY',
          finding: 'MOP lacks an explicit step-by-step pre-verified back-out sequence for aborting before the PONR.',
          action: 'Include verified back-out steps with defined safe physical resting states.'
        });
      }
    }

    // Check 3: EOP Troubleshooting Prohibition (Rule 04)
    if (textLower.includes('eop') || textLower.includes('emergency operating procedure')) {
      if (textLower.includes('troubleshoot') || textLower.includes('diagnose root cause') || textLower.includes('inspect circuit board')) {
        isCategoryA = true;
        findings.push({
          code: 'CAT-A-05',
          rule: 'EOP Boundary Violation: In-Band Troubleshooting (Rule 04)',
          severity: 'CATEGORY A - IMMEDIATE REJECTION',
          finding: 'Emergency Operating Procedure contains diagnostic or troubleshooting steps during active fault stabilization.',
          action: 'Purge troubleshooting from EOP. EOP must contain ONLY reflexive stabilization actions. Move diagnostics to post-incident review.'
        });
      }
    }

    // Check 4: Corrosion Verification (Rule 06)
    if (textLower.includes('corrosion') || textLower.includes('isa-71.04') || textLower.includes('coupon')) {
      if (textLower.includes('copper') && !textLower.includes('silver')) {
        findings.push({
          code: 'CAT-B-06',
          rule: 'Single-Metal Coupon Acceptance Defect (Rule 06)',
          severity: 'CATEGORY B - DEFICIENCY',
          finding: 'Corrosion verification relies exclusively on Copper (Cu) coupons. RoHS lead-free hardware requires dual Copper + Silver tracking.',
          action: 'Mandate paired Cu + Ag 30-day reactivity coupons analyzed by coulometric reduction with unexposed field blank.'
        });
      }
    }

    // Check 5: BMS / Alarm Integrity & Clock Synchronization (Rule 05)
    if (commissioning_level === 'L4' || commissioning_level === 'L5' || commissioning_level === 'ALL') {
      if (textLower.includes('handover') || textLower.includes('turnover') || textLower.includes('ist')) {
        if (!textLower.includes('ntp') && !textLower.includes('ptp') && !textLower.includes('clock sync')) {
          findings.push({
            code: 'CAT-C-05',
            rule: 'Sequence-of-Events (SOE) Time Sync Unverified (Rule 05)',
            severity: 'CATEGORY C - OBSERVATION',
            finding: 'Script does not verify IEEE 1588 PTP or NIST NTP millisecond synchronization across protective relays, PLC, and BMS recorders.',
            action: 'Add hold point verifying time sync within +/- 1ms across all event recording devices prior to IST trip tests.'
          });
        }
        if (!textLower.includes('shelved') && !textLower.includes('forced') && !textLower.includes('out-of-service')) {
          findings.push({
            code: 'CAT-B-05',
            rule: 'BMS Alarm Suppression Audit Missing (Rule 05)',
            severity: 'CATEGORY B - DEFICIENCY',
            finding: 'Script accepts overall BMS green status without querying the database for Shelved, Out-of-Service, or Forced-Manual points.',
            action: 'Audit database points; verify zero points are forced manual or shelved before turnover sign-off.'
          });
        }
      }
    }

    const verdict = isCategoryA ? 'REJECTED - CATEGORY A FATAL FLAW DETECTED' : (findings.length > 0 ? 'CONDITIONAL - DEFICIENCIES REQUIRE REVISION' : 'PASSED - DETERMINISTIC CRITERIA MET');

    const report = [
      `=======================================================`,
      `DATA CENTER AUDITOR // COMMISSIONING SCRIPT AUDIT REPORT`,
      `=======================================================`,
      `Commissioning Level : ${commissioning_level}`,
      `Audit Verdict       : ${verdict}`,
      `Total Findings      : ${findings.length}`,
      `Category A Blocker  : ${isCategoryA ? 'YES - STOP WORK MANDATED' : 'NONE'}`,
      `-------------------------------------------------------`,
      ...findings.map((f, i) => `[${i + 1}] ${f.severity}\n    Code   : ${f.code}\n    Rule   : ${f.rule}\n    Finding: ${f.finding}\n    Action : ${f.action}\n`),
      `-------------------------------------------------------`,
      `Reference Standards: ASME B31.3 | NFPA 70E | ASHRAE Guideline 0 | ANSI/ISA-71.04-2013 | ISO-8528-1`,
      `Ground Truth Corpus: https://datacenterfieldguides.com/SKILL.md`
    ].join('\n');

    return {
      content: [{ type: 'text', text: report }]
    };
  }
);

// -------------------------------------------------------------
// TOOL 2: Verify Hydraulic Boundary (NVL72 Liquid Cooling)
// -------------------------------------------------------------
server.tool(
  'verify_hydraulic_boundary',
  'Calculates required coolant flow rate, mass balance, heat removal capacity, and ASHRAE Liquid Cooling Class compliance for AI compute racks (e.g., NVIDIA GB200 NVL72).',
  {
    heat_load_kw: z.number().describe('Total heat load to be rejected via liquid loop in kW (e.g. 132 for NVL72)'),
    delta_t_c: z.number().describe('Coolant temperature rise across compute cold plates in °C (e.g. 10 to 15)'),
    coolant_type: z.enum(['water', 'pg25', 'pg30', 'eg25']).optional().default('pg25').describe('Coolant fluid: water, pg25 (25% Propylene Glycol), pg30, eg25 (25% Ethylene Glycol)'),
    measured_flow_lpm: z.number().optional().describe('Actual measured coolant flow rate in Liters/Minute (optional)'),
    supply_temp_c: z.number().optional().describe('Supply coolant temperature in °C (optional)')
  },
  async ({ heat_load_kw, delta_t_c, coolant_type, measured_flow_lpm, supply_temp_c }) => {
    // Specific heat (kJ / kg*K) & density (kg / m3) approximations at ~35C
    const fluidProps = {
      water: { cp: 4.18, rho: 994, name: 'Deionized / Treated Water' },
      pg25:  { cp: 3.96, rho: 1022, name: '25% Propylene Glycol (PG25)' },
      pg30:  { cp: 3.88, rho: 1028, name: '30% Propylene Glycol (PG30)' },
      eg25:  { cp: 3.85, rho: 1035, name: '25% Ethylene Glycol (EG25)' }
    };

    const prop = fluidProps[coolant_type] || fluidProps.pg25;

    // Heat transfer formula: Q = m_dot * Cp * delta_T
    // m_dot (kg/s) = Q (kW) / (Cp (kJ/kg*K) * delta_T (K))
    const massFlow_kg_s = heat_load_kw / (prop.cp * delta_t_c);
    
    // Volumetric flow rate: V_dot (m3/s) = m_dot / rho
    const volFlow_m3_s = massFlow_kg_s / prop.rho;
    const req_lpm = volFlow_m3_s * 1000 * 60;
    const req_gpm = req_lpm * 0.264172;

    const notes = [];

    // Flow adequacy check
    let flowVerdict = 'THEORETICAL REQUIREMENT CALCULATED';
    if (measured_flow_lpm !== undefined) {
      const flowRatio = measured_flow_lpm / req_lpm;
      if (flowRatio < 0.95) {
        flowVerdict = 'DEFICIENT: MEASURED FLOW BELOW REQUIRED THERMAL REJECTION CAPACITY';
        notes.push(`CRITICAL: Measured flow (${measured_flow_lpm.toFixed(1)} LPM) is ${(100 - flowRatio * 100).toFixed(1)}% below the minimum required flow rate (${req_lpm.toFixed(1)} LPM) for ${heat_load_kw} kW at ΔT=${delta_t_c}°C. Risk of thermal throttling or cold-plate dryout.`);
      } else if (flowRatio > 1.30) {
        flowVerdict = 'EXCESSIVE FLOW: POTENTIAL EROSION & HYDRAULIC INEFFICIENCY';
        notes.push(`WARNING: Measured flow exceeds requirement by ${((flowRatio - 1) * 100).toFixed(1)}%. Check pipe fluid velocity (keep < 1.5 - 2.0 m/s) to prevent copper tube erosion-corrosion.`);
      } else {
        flowVerdict = 'COMPLIANT: FLOW MEETS THERMAL ENVELOPE';
        notes.push(`OPTIMAL: Measured flow matches required thermal envelope within ${(Math.abs(flowRatio - 1) * 100).toFixed(1)}% tolerance.`);
      }
    }

    // ASHRAE Liquid Cooling Class
    let ashraeClass = 'UNSPECIFIED (NO SUPPLY TEMP PROVIDED)';
    if (supply_temp_c !== undefined) {
      if (supply_temp_c <= 17) {
        ashraeClass = 'W1 (Sub-ambient, requires chiller; risk of whitespace condensation)';
      } else if (supply_temp_c <= 27) {
        ashraeClass = 'W1 (17°C - 27°C, typical chiller-assisted)';
      } else if (supply_temp_c <= 32) {
        ashraeClass = 'W2 (27°C - 32°C, dry cooler with chiller trim)';
      } else if (supply_temp_c <= 40) {
        ashraeClass = 'W3 (32°C - 40°C, direct dry-cooler heat rejection)';
      } else if (supply_temp_c <= 45) {
        ashraeClass = 'W4 (40°C - 45°C, warm water / heat reuse class; verify silicon max Tc)';
      } else {
        ashraeClass = 'EXCEEDS ASHRAE W4 (> 45°C) - RISK OF HARDWARE THERMAL TRIP';
        notes.push(`CRITICAL: Supply coolant temperature (${supply_temp_c}°C) exceeds ASHRAE W4 maximum allowable threshold.`);
      }
    }

    const output = [
      `=======================================================`,
      `DATA CENTER AUDITOR // HYDRAULIC & THERMAL VERIFICATION`,
      `=======================================================`,
      `Target Heat Load      : ${heat_load_kw.toFixed(1)} kW`,
      `Design Delta-T (ΔT)   : ${delta_t_c.toFixed(1)} °C`,
      `Fluid Type            : ${prop.name} (Cp = ${prop.cp} kJ/kg·K, ρ = ${prop.rho} kg/m³)`,
      `Required Mass Flow    : ${massFlow_kg_s.toFixed(3)} kg/s`,
      `Required Flow (LPM)   : ${req_lpm.toFixed(1)} LPM`,
      `Required Flow (GPM)   : ${req_gpm.toFixed(1)} GPM`,
      supply_temp_c !== undefined ? `Supply Temperature    : ${supply_temp_c.toFixed(1)} °C (${ashraeClass})` : '',
      measured_flow_lpm !== undefined ? `Measured Flow Rate    : ${measured_flow_lpm.toFixed(1)} LPM` : '',
      `Hydraulic Verdict     : ${flowVerdict}`,
      `-------------------------------------------------------`,
      ...notes.map(n => `- ${n}`),
      `-------------------------------------------------------`,
      `Reference: ASHRAE TC 9.9 Thermal Guidelines for Liquid Cooling | NVIDIA GB200 NVL72 Spec`
    ].filter(Boolean).join('\n');

    return {
      content: [{ type: 'text', text: output }]
    };
  }
);

// -------------------------------------------------------------
// TOOL 3: Search Field Protocols (69-Protocol Ground-Truth)
// -------------------------------------------------------------
server.tool(
  'search_field_protocols',
  'Searches the Data Center Field Guides ground-truth corpus for commissioning procedures, fatal flaw criteria, and engineering formulas.',
  {
    query: z.string().describe('Search terms or protocol topic (e.g. "NVL72 manifold", "corrosion coupon", "MOP switching", "Level 4 commissioning", "substation TDD")')
  },
  async ({ query }) => {
    if (!corpusText) {
      return {
        content: [{ type: 'text', text: `Search offline. Ground truth reference available online at https://datacenterfieldguides.com/llms-full.txt` }]
      };
    }

    const terms = query.toLowerCase().split(/\s+/).filter(t => t.length > 2);
    const paragraphs = corpusText.split(/\n\n+/);
    
    const matches = [];
    for (const para of paragraphs) {
      const lower = para.toLowerCase();
      let matchCount = 0;
      for (const t of terms) {
        if (lower.includes(t)) matchCount++;
      }
      if (matchCount > 0) {
        matches.push({ score: matchCount, text: para.trim() });
      }
    }

    matches.sort((a, b) => b.score - a.score);
    const topMatches = matches.slice(0, 3);

    if (topMatches.length === 0) {
      return {
        content: [{ type: 'text', text: `No direct matches found for "${query}" in the 69-protocol corpus.\nBrowse the full index at: https://datacenterfieldguides.com/llms.txt` }]
      };
    }

    const result = [
      `Found ${matches.length} matches for "${query}" in Data Center Field Guides Ground Truth:`,
      `=======================================================`,
      ...topMatches.map((m, i) => `[MATCH ${i + 1} // RELEVANCE SCORE: ${m.score}]\n${m.text}\n`),
      `=======================================================`,
      `Full unredacted protocol access: https://datacenterfieldguides.com/llms-full.txt`
    ].join('\n');

    return {
      content: [{ type: 'text', text: result }]
    };
  }
);

// -------------------------------------------------------------
// TOOL 4: Lookup Defect Code
// -------------------------------------------------------------
server.tool(
  'lookup_defect_code',
  'Looks up standard mission-critical data center defect codes (Category A: Stop-Work, Category B: Pre-Handover Deficiency, Category C: Punchlist Observation).',
  {
    defect_code: z.string().describe('Defect code such as "CAT-A-01", "A-01", "CAT-B-04", "ISA-71.04", "PUE-01"')
  },
  async ({ defect_code }) => {
    const code = defect_code.toUpperCase().trim();
    
    const defectDatabase = {
      'A-01': {
        title: 'Air Load Bank Used on Liquid Manifold Boundary',
        severity: 'CATEGORY A - IMMEDIATE REJECTION (FATAL FLAW)',
        trigger: 'Attempting to accept liquid-cooled compute whitespace (NVL72) using 100% air-side load banks.',
        consequence: 'Zero verification of CDU primary/secondary ΔP, blind spots in bypass valve transitions, manifold seal cavitation.',
        mandate: 'Immediate Stop-Work. Replace with calibrated hydraulic liquid load bank instrumented with 1-sec flow and ΔT telemetry.',
        standards: 'ASHRAE Guideline 0-2019, Section 6.2 | NVIDIA GB200 Infrastructure Guidelines'
      },
      'A-02': {
        title: 'Non-Binding Feasibility Letter Accepted as Firm Power',
        severity: 'CATEGORY A - IMMEDIATE REJECTION (FATAL FLAW)',
        trigger: 'Site selection or acquisition approved on non-binding utility letter without executed Large Load Interconnection Agreement (LGIA).',
        consequence: 'Stranded capital asset, multi-year interconnect queue delays, unexpected $50M+ substation upgrade assessments.',
        mandate: 'Refuse site approval. Require signed LGIA, completed System Impact Study, and verified transmission substation capacity.',
        standards: 'FERC Order 2023 | IEEE 1547 | Volume 09: Walk a TDD'
      },
      'A-04': {
        title: 'Redundancy-Altering MOP Missing Point of No Return (PONR)',
        severity: 'CATEGORY A - IMMEDIATE REJECTION (FATAL FLAW)',
        trigger: 'MOP executed for electrical or mechanical switching without an explicit, irreversible physical hold-point declared.',
        consequence: 'Operator confusion during unexpected trip, simultaneous dual-path de-energization, total whitespace outage.',
        mandate: 'Immediate MOP freeze. Require clear PONR step and pre-verified back-out procedure for all preceding steps.',
        standards: 'NFPA 70E Section 120 | Volume 05: Run the Data Center Day'
      },
      'A-05': {
        title: 'In-Band Diagnostic Troubleshooting During Active EOP',
        severity: 'CATEGORY A - IMMEDIATE REJECTION (FATAL FLAW)',
        trigger: 'Technician opens cabinets, analyzes waveform captures, or resets circuit breakers during emergency stabilization.',
        consequence: 'Arc flash hazard, escalation from partial trip to cascading total blackout.',
        mandate: 'Purge all diagnostic steps from EOP. EOP scope is strictly reflexive fault isolation to return facility to known stable state.',
        standards: 'IEEE 3006.7 | NFPA 70B | Volume 05: Run the Data Center Day'
      },
      'B-04': {
        title: 'Missing Pre-Verified Back-Out Procedure in MOP',
        severity: 'CATEGORY B - PRE-HANDOVER DEFICIENCY',
        trigger: 'MOP defines switching steps but fails to articulate rollback actions if a step fails prior to the PONR.',
        consequence: 'Prolonged degraded redundancy while operations team invents improvised recovery steps under alarm stress.',
        mandate: 'Update MOP to include exact inverse switching sequence and safe rest positions.',
        standards: 'Volume 05: Run the Data Center Day'
      },
      'B-06': {
        title: 'Single-Metal (Copper-Only) Corrosion Reactivity Monitoring',
        severity: 'CATEGORY B - PRE-HANDOVER DEFICIENCY',
        trigger: 'Whitespace environmental certification relies solely on copper corrosion coupons.',
        consequence: 'Failure to detect sulfur-bearing gas corrosion (Ag2S) which attacks lead-free RoHS solder and silver terminations.',
        mandate: 'Deploy paired Copper + Silver 30-day reactivity coupons analyzed by coulometric reduction per ANSI/ISA-71.04-2013.',
        standards: 'ANSI/ISA-71.04-2013 Severity Level G1'
      }
    };

    const cleanCode = code.replace(/^CAT-/, '');
    const found = defectDatabase[cleanCode] || defectDatabase[code];

    if (!found) {
      return {
        content: [{
          type: 'text',
          text: `Defect code "${defect_code}" not found in quick table. Refer to the complete defect taxonomy in Volume 07: Refuse the Handover and SKILL.md: https://datacenterfieldguides.com/SKILL.md`
        }]
      };
    }

    const report = [
      `=======================================================`,
      `DEFECT CODE AUDIT SHEET: ${defect_code}`,
      `=======================================================`,
      `Title       : ${found.title}`,
      `Severity    : ${found.severity}`,
      `Trigger     : ${found.trigger}`,
      `Consequence : ${found.consequence}`,
      `Mandate     : ${found.mandate}`,
      `Standards   : ${found.standards}`,
      `=======================================================`
    ].join('\n');

    return {
      content: [{ type: 'text', text: report }]
    };
  }
);

// -------------------------------------------------------------
// TOOL 5: ANSI/ISA-71.04 Corrosion Reactivity Classifier
// -------------------------------------------------------------
server.tool(
  'classify_corrosion_severity',
  'Classifies data center whitespace atmospheric corrosion severity according to ANSI/ISA-71.04-2013 for Copper and Silver reactivity.',
  {
    copper_angstroms_30d: z.number().describe('Copper reactivity rate in Angstroms per 30 days (Å/30 days)'),
    silver_angstroms_30d: z.number().describe('Silver reactivity rate in Angstroms per 30 days (Å/30 days)')
  },
  async ({ copper_angstroms_30d, silver_angstroms_30d }) => {
    // ANSI/ISA-71.04-2013 Table 1 Reactivity Levels:
    // Level G1 (Mild): Cu < 300 Å/30 days, Ag < 200 Å/30 days
    // Level G2 (Moderate): Cu 300 - 1000 Å, Ag 200 - 1000 Å
    // Level G3 (Harsh): Cu 1000 - 2000 Å, Ag 1000 - 2000 Å
    // Level GX (Severe): Cu >= 2000 Å, Ag >= 2000 Å

    let cuLevel = 'G1';
    if (copper_angstroms_30d >= 2000) cuLevel = 'GX';
    else if (copper_angstroms_30d >= 1000) cuLevel = 'G3';
    else if (copper_angstroms_30d >= 300) cuLevel = 'G2';

    let agLevel = 'G1';
    if (silver_angstroms_30d >= 2000) agLevel = 'GX';
    else if (silver_angstroms_30d >= 1000) agLevel = 'G3';
    else if (silver_angstroms_30d >= 200) agLevel = 'G2';

    // The overall severity is governed by the worst of the two
    const rank = { G1: 1, G2: 2, G3: 3, GX: 4 };
    const overallLevel = rank[cuLevel] >= rank[agLevel] ? cuLevel : agLevel;

    const levelDescriptions = {
      G1: 'G1 (Mild) - Well-controlled environment. Electronic equipment reliability is not compromised. Mandatory for RoHS lead-free solder.',
      G2: 'G2 (Moderate) - Corrosion is measurable. Solder creep corrosion risk on fine-pitch components (DIMM, PCIe sockets).',
      G3: 'G3 (Harsh) - High probability of electronic failure due to silver sulfide (Ag2S) or copper sulfide growth.',
      GX: 'GX (Severe) - Extreme environmental degradation. Rapid failure of electronics; requires immediate chemical gas-phase filtration.'
    };

    const isWarrantySafe = overallLevel === 'G1';

    const output = [
      `=======================================================`,
      `ANSI/ISA-71.04-2013 CORROSION REACTIVITY AUDIT REPORT`,
      `=======================================================`,
      `Copper (Cu) Rate     : ${copper_angstroms_30d} Å / 30 days (Classification: Level ${cuLevel})`,
      `Silver (Ag) Rate     : ${silver_angstroms_30d} Å / 30 days (Classification: Level ${agLevel})`,
      `Overall Environment  : Level ${overallLevel}`,
      `Description          : ${levelDescriptions[overallLevel]}`,
      `RoHS Compliance      : ${isWarrantySafe ? 'COMPLIANT (Meets OEM Warranty Requirements)' : 'NON-COMPLIANT (Hardware Warranty at Risk)'}`,
      `-------------------------------------------------------`,
      isWarrantySafe 
        ? 'RECOMMENDATION: Maintain positive pressurization and replace chemical filters per regular schedule.'
        : 'MANDATORY ACTION: Deploy chemical gas-phase filtration (deep-bed carbon/permanganate) immediately to bring environment under G1 (< 300 Å Cu, < 200 Å Ag). Audit outdoor air intake damper seals.',
      `-------------------------------------------------------`,
      `Reference: ANSI/ISA-71.04-2013 | Volume 08: Judge a Corrosion Coupon`
    ].join('\n');

    return {
      content: [{ type: 'text', text: output }]
    };
  }
);

// Start server on stdio
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch((err) => {
  console.error('Fatal MCP Server error:', err);
  process.exit(1);
});
