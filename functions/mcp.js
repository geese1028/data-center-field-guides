// Cloudflare Pages Function: Remote MCP HTTP Endpoint for Data Center Field Auditor
// Compliant with Model Context Protocol (2024-11-05) over HTTP

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization, x-api-key',
  'Content-Type': 'application/json'
};

const TOOLS = [
  {
    name: 'audit_commissioning_script',
    description: 'Audits a data center commissioning script (MOP, SOP, EOP, or IST Level 1-5) against deterministic physical boundary rules, refusal gates, and Category A/B/C defect codes.',
    inputSchema: {
      type: 'object',
      properties: {
        script_text: {
          type: 'string',
          description: 'The raw text of the MOP, SOP, EOP or commissioning script to audit'
        },
        commissioning_level: {
          type: 'string',
          enum: ['L1', 'L2', 'L3', 'L4', 'L5', 'ALL'],
          default: 'ALL',
          description: 'Commissioning level being executed'
        }
      },
      required: ['script_text']
    }
  },
  {
    name: 'verify_hydraulic_boundary',
    description: 'Calculates required coolant flow rate (LPM/GPM), mass balance, heat removal capacity, and ASHRAE Liquid Cooling Class compliance for high-density AI clusters (e.g. NVIDIA GB200 NVL72).',
    inputSchema: {
      type: 'object',
      properties: {
        heat_load_kw: {
          type: 'number',
          description: 'Total heat load in kW (e.g. 132 for NVL72)'
        },
        delta_t_c: {
          type: 'number',
          description: 'Coolant temperature rise across compute cold plates in °C'
        },
        coolant_type: {
          type: 'string',
          enum: ['water', 'pg25', 'pg30', 'eg25'],
          default: 'pg25',
          description: 'Coolant fluid type'
        },
        measured_flow_lpm: {
          type: 'number',
          description: 'Actual measured coolant flow rate in Liters/Minute (optional)'
        },
        supply_temp_c: {
          type: 'number',
          description: 'Supply coolant temperature in °C (optional)'
        }
      },
      required: ['heat_load_kw', 'delta_t_c']
    }
  },
  {
    name: 'search_field_protocols',
    description: 'Searches the 69-protocol ground-truth engineering corpus from Data Center Field Guides for commissioning procedures and safety standards.',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Search topic (e.g. "NVL72 manifold", "corrosion coupon", "MOP switching")'
        }
      },
      required: ['query']
    }
  },
  {
    name: 'lookup_defect_code',
    description: 'Looks up standard mission-critical data center defect codes (Category A: Stop-Work, Category B: Deficiency, Category C: Observation).',
    inputSchema: {
      type: 'object',
      properties: {
        defect_code: {
          type: 'string',
          description: 'Defect code such as "CAT-A-01", "A-01", "CAT-B-04", "ISA-71.04"'
        }
      },
      required: ['defect_code']
    }
  },
  {
    name: 'classify_corrosion_severity',
    description: 'Classifies data center whitespace atmospheric corrosion severity according to ANSI/ISA-71.04-2013 for Copper and Silver reactivity.',
    inputSchema: {
      type: 'object',
      properties: {
        copper_angstroms_30d: {
          type: 'number',
          description: 'Copper reactivity rate in Angstroms per 30 days (Å/30 days)'
        },
        silver_angstroms_30d: {
          type: 'number',
          description: 'Silver reactivity rate in Angstroms per 30 days (Å/30 days)'
        }
      },
      required: ['copper_angstroms_30d', 'silver_angstroms_30d']
    }
  }
];

// Tool Execution Helpers
function handleAuditScript(args) {
  const scriptText = (args.script_text || '').toLowerCase();
  const level = args.commissioning_level || 'ALL';
  const findings = [];
  let isCatA = false;

  if (
    (scriptText.includes('nvl72') || scriptText.includes('gb200') || scriptText.includes('liquid cooling')) &&
    (scriptText.includes('air heater') || scriptText.includes('resistive heater') || scriptText.includes('air load bank')) &&
    !scriptText.includes('liquid load bank')
  ) {
    isCatA = true;
    findings.push({
      code: 'CAT-A-01',
      rule: 'Liquid vs. Air Thermal Boundary Violation (Rule 01)',
      severity: 'CATEGORY A - IMMEDIATE REJECTION',
      finding: 'Script specifies resistive air heaters for liquid-cooled NVL72 / GB200 racks.',
      action: 'Refuse script. Mandate hydraulic liquid load bank with flow balance and delta-T measurement at rack manifold.'
    });
  }

  if (scriptText.includes('mop') || scriptText.includes('method of procedure')) {
    if (!scriptText.includes('point of no return') && !scriptText.includes('ponr')) {
      isCatA = true;
      findings.push({
        code: 'CAT-A-04',
        rule: 'State-Machine Governance Missing PONR (Rule 04)',
        severity: 'CATEGORY A - IMMEDIATE REJECTION',
        finding: 'MOP alters redundancy without declaring an explicit Point of No Return (PONR).',
        action: 'Halt approval. Require explicit step declaring the physical point of no return.'
      });
    }
    if (!scriptText.includes('back-out') && !scriptText.includes('backout') && !scriptText.includes('abort') && !scriptText.includes('rollback')) {
      findings.push({
        code: 'CAT-B-04',
        rule: 'Missing Pre-Verified Back-Out Procedure (Rule 04)',
        severity: 'CATEGORY B - DEFICIENCY',
        finding: 'MOP lacks an explicit pre-verified back-out sequence.',
        action: 'Add verified step-by-step rollback procedure.'
      });
    }
  }

  if (scriptText.includes('eop') || scriptText.includes('emergency operating procedure')) {
    if (scriptText.includes('troubleshoot') || scriptText.includes('diagnose root cause')) {
      isCatA = true;
      findings.push({
        code: 'CAT-A-05',
        rule: 'EOP Boundary Violation: In-Band Troubleshooting (Rule 04)',
        severity: 'CATEGORY A - IMMEDIATE REJECTION',
        finding: 'EOP contains diagnostic troubleshooting during active fault stabilization.',
        action: 'Purge troubleshooting from EOP. Restrict scope strictly to reflexive stabilization.'
      });
    }
  }

  if (scriptText.includes('corrosion') || scriptText.includes('coupon')) {
    if (scriptText.includes('copper') && !scriptText.includes('silver')) {
      findings.push({
        code: 'CAT-B-06',
        rule: 'Single-Metal Coupon Defect (Rule 06)',
        severity: 'CATEGORY B - DEFICIENCY',
        finding: 'Whitespace relies solely on copper coupons without silver tracking for RoHS hardware.',
        action: 'Mandate paired Cu + Ag 30-day reactivity coupons analyzed by coulometric reduction.'
      });
    }
  }

  const verdict = isCatA ? 'REJECTED - CATEGORY A FATAL FLAW DETECTED' : (findings.length > 0 ? 'CONDITIONAL - DEFICIENCIES REQUIRE REVISION' : 'PASSED - DETERMINISTIC CRITERIA MET');

  const report = [
    `=======================================================`,
    `DATA CENTER AUDITOR // COMMISSIONING SCRIPT AUDIT REPORT`,
    `=======================================================`,
    `Commissioning Level : ${level}`,
    `Audit Verdict       : ${verdict}`,
    `Total Findings      : ${findings.length}`,
    `Category A Blocker  : ${isCatA ? 'YES - STOP WORK MANDATED' : 'NONE'}`,
    `-------------------------------------------------------`,
    ...findings.map((f, i) => `[${i + 1}] ${f.severity}\n    Code   : ${f.code}\n    Rule   : ${f.rule}\n    Finding: ${f.finding}\n    Action : ${f.action}\n`),
    `-------------------------------------------------------`,
    `Reference Standards: ASME B31.3 | NFPA 70E | ASHRAE Guideline 0 | ANSI/ISA-71.04-2013`,
    `Ground Truth Corpus: https://datacenterfieldguides.com/SKILL.md`
  ].join('\n');

  return report;
}

function handleHydraulics(args) {
  const heatKw = Number(args.heat_load_kw) || 132;
  const deltaT = Number(args.delta_t_c) || 12;
  const cType = args.coolant_type || 'pg25';
  const measuredFlow = args.measured_flow_lpm !== undefined ? Number(args.measured_flow_lpm) : undefined;
  const supplyTemp = args.supply_temp_c !== undefined ? Number(args.supply_temp_c) : undefined;

  const props = {
    water: { cp: 4.18, rho: 994, name: 'Treated Water' },
    pg25:  { cp: 3.96, rho: 1022, name: '25% Propylene Glycol (PG25)' },
    pg30:  { cp: 3.88, rho: 1028, name: '30% Propylene Glycol (PG30)' },
    eg25:  { cp: 3.85, rho: 1035, name: '25% Ethylene Glycol (EG25)' }
  }[cType] || { cp: 3.96, rho: 1022, name: '25% PG' };

  const massFlow = heatKw / (props.cp * deltaT);
  const volFlow_m3_s = massFlow / props.rho;
  const reqLpm = volFlow_m3_s * 1000 * 60;
  const reqGpm = reqLpm * 0.264172;

  const notes = [];
  let flowVerdict = 'THEORETICAL REQUIREMENT CALCULATED';
  if (measuredFlow !== undefined) {
    const ratio = measuredFlow / reqLpm;
    if (ratio < 0.95) {
      flowVerdict = 'DEFICIENT: FLOW BELOW THERMAL CAPACITY';
      notes.push(`CRITICAL: Measured flow (${measuredFlow.toFixed(1)} LPM) is ${(100 - ratio * 100).toFixed(1)}% below required ${reqLpm.toFixed(1)} LPM.`);
    } else if (ratio > 1.30) {
      flowVerdict = 'EXCESSIVE: EROSION RISK';
      notes.push(`WARNING: Measured flow exceeds requirement by ${((ratio - 1) * 100).toFixed(1)}%. Check fluid velocity < 1.5 - 2.0 m/s.`);
    } else {
      flowVerdict = 'COMPLIANT: MEETS ENVELOPE';
      notes.push(`OPTIMAL: Measured flow matches requirement within ${(Math.abs(ratio - 1) * 100).toFixed(1)}% tolerance.`);
    }
  }

  let ashraeClass = 'UNSPECIFIED';
  if (supplyTemp !== undefined) {
    if (supplyTemp <= 27) ashraeClass = 'W1 (17°C - 27°C)';
    else if (supplyTemp <= 32) ashraeClass = 'W2 (27°C - 32°C)';
    else if (supplyTemp <= 40) ashraeClass = 'W3 (32°C - 40°C)';
    else if (supplyTemp <= 45) ashraeClass = 'W4 (40°C - 45°C)';
    else {
      ashraeClass = 'EXCEEDS W4 (> 45°C)';
      notes.push('CRITICAL: Supply temp exceeds ASHRAE W4 limit.');
    }
  }

  return [
    `=======================================================`,
    `DATA CENTER AUDITOR // HYDRAULIC & THERMAL VERIFICATION`,
    `=======================================================`,
    `Target Heat Load      : ${heatKw.toFixed(1)} kW`,
    `Design Delta-T (ΔT)   : ${deltaT.toFixed(1)} °C`,
    `Fluid Type            : ${props.name} (Cp = ${props.cp} kJ/kg·K, ρ = ${props.rho} kg/m³)`,
    `Required Mass Flow    : ${massFlow.toFixed(3)} kg/s`,
    `Required Flow (LPM)   : ${reqLpm.toFixed(1)} LPM`,
    `Required Flow (GPM)   : ${reqGpm.toFixed(1)} GPM`,
    supplyTemp !== undefined ? `Supply Temperature    : ${supplyTemp.toFixed(1)} °C (${ashraeClass})` : '',
    measuredFlow !== undefined ? `Measured Flow Rate    : ${measuredFlow.toFixed(1)} LPM` : '',
    `Hydraulic Verdict     : ${flowVerdict}`,
    `-------------------------------------------------------`,
    ...notes.map(n => `- ${n}`),
    `-------------------------------------------------------`,
    `Reference: ASHRAE TC 9.9 | NVIDIA GB200 NVL72 Spec`
  ].filter(Boolean).join('\n');
}

function handleDefectLookup(code) {
  const c = (code || '').toUpperCase().trim().replace(/^CAT-/, '');
  const db = {
    'A-01': {
      title: 'Air Load Bank Used on Liquid Manifold Boundary',
      severity: 'CATEGORY A - IMMEDIATE REJECTION',
      mandate: 'Immediate Stop-Work. Replace with calibrated hydraulic liquid load bank instrumented with 1-sec flow and delta-T telemetry.'
    },
    'A-02': {
      title: 'Non-Binding Feasibility Letter Accepted as Firm Power',
      severity: 'CATEGORY A - IMMEDIATE REJECTION',
      mandate: 'Refuse site approval. Require signed Large Load Interconnection Agreement (LGIA).'
    },
    'A-04': {
      title: 'Redundancy-Altering MOP Missing Point of No Return (PONR)',
      severity: 'CATEGORY A - IMMEDIATE REJECTION',
      mandate: 'Freeze MOP. Declare explicit PONR and pre-verified back-out sequence.'
    },
    'A-05': {
      title: 'In-Band Diagnostic Troubleshooting During Active EOP',
      severity: 'CATEGORY A - IMMEDIATE REJECTION',
      mandate: 'Purge troubleshooting from EOP. EOP scope is strictly reflexive fault isolation.'
    },
    'B-06': {
      title: 'Single-Metal (Copper-Only) Corrosion Reactivity Monitoring',
      severity: 'CATEGORY B - PRE-HANDOVER DEFICIENCY',
      mandate: 'Deploy paired Copper + Silver 30-day reactivity coupons analyzed by coulometric reduction.'
    }
  };

  const item = db[c];
  if (!item) {
    return `Defect code "${code}" details available in SKILL.md: https://datacenterfieldguides.com/SKILL.md`;
  }

  return [
    `DEFECT CODE: ${code}`,
    `Title   : ${item.title}`,
    `Severity: ${item.severity}`,
    `Mandate : ${item.mandate}`,
    `Full Taxonomy: https://datacenterfieldguides.com/SKILL.md`
  ].join('\n');
}

function handleCorrosion(cu, ag) {
  let cuLevel = cu >= 2000 ? 'GX' : cu >= 1000 ? 'G3' : cu >= 300 ? 'G2' : 'G1';
  let agLevel = ag >= 2000 ? 'GX' : ag >= 1000 ? 'G3' : ag >= 200 ? 'G2' : 'G1';
  const rank = { G1: 1, G2: 2, G3: 3, GX: 4 };
  const overall = rank[cuLevel] >= rank[agLevel] ? cuLevel : agLevel;

  return [
    `=======================================================`,
    `ANSI/ISA-71.04-2013 CORROSION REACTIVITY REPORT`,
    `=======================================================`,
    `Copper Rate : ${cu} Å/30d (Level ${cuLevel})`,
    `Silver Rate : ${ag} Å/30d (Level ${agLevel})`,
    `Overall     : Level ${overall}`,
    `RoHS Safe   : ${overall === 'G1' ? 'YES (Warranty Compliant)' : 'NO (Hardware Warranty at Risk)'}`,
    `Reference   : ANSI/ISA-71.04-2013 | Volume 08: Judge a Corrosion Coupon`
  ].join('\n');
}

export async function onRequest(context) {
  const { request } = context;
  const method = request.method;

  if (method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: CORS_HEADERS });
  }

  if (method === 'GET') {
    return new Response(JSON.stringify({
      name: 'datacenter-field-auditor',
      version: '1.0.0',
      description: 'Deterministic physical boundary and TDD commissioning MCP server for mission-critical data centers and NVIDIA GB200 NVL72 liquid cooling.',
      transport: 'HTTP/JSON-RPC 2.0 (Streamable HTTP)',
      endpoint: 'https://datacenterfieldguides.com/mcp',
      documentation: 'https://datacenterfieldguides.com/SKILL.md',
      tools: TOOLS.map(t => ({ name: t.name, description: t.description }))
    }, null, 2), { status: 200, headers: CORS_HEADERS });
  }

  if (method === 'POST') {
    try {
      const body = await request.json();
      const { id, method: rpcMethod, params } = body;

      if (rpcMethod === 'initialize') {
        return new Response(JSON.stringify({
          jsonrpc: '2.0',
          id: id || 1,
          result: {
            protocolVersion: '2024-11-05',
            capabilities: { tools: { listChanged: false } },
            serverInfo: {
              name: 'datacenter-field-auditor',
              version: '1.0.0'
            }
          }
        }), { status: 200, headers: CORS_HEADERS });
      }

      if (rpcMethod === 'notifications/initialized') {
        return new Response(JSON.stringify({ jsonrpc: '2.0', id: id || null, result: {} }), { status: 200, headers: CORS_HEADERS });
      }

      if (rpcMethod === 'ping') {
        return new Response(JSON.stringify({ jsonrpc: '2.0', id: id || 1, result: {} }), { status: 200, headers: CORS_HEADERS });
      }

      if (rpcMethod === 'tools/list') {
        return new Response(JSON.stringify({
          jsonrpc: '2.0',
          id: id || 1,
          result: { tools: TOOLS }
        }), { status: 200, headers: CORS_HEADERS });
      }

      if (rpcMethod === 'tools/call') {
        const toolName = params?.name;
        const toolArgs = params?.arguments || {};
        let resultText = '';

        if (toolName === 'audit_commissioning_script') {
          resultText = handleAuditScript(toolArgs);
        } else if (toolName === 'verify_hydraulic_boundary') {
          resultText = handleHydraulics(toolArgs);
        } else if (toolName === 'lookup_defect_code') {
          resultText = handleDefectLookup(toolArgs.defect_code);
        } else if (toolName === 'classify_corrosion_severity') {
          resultText = handleCorrosion(Number(toolArgs.copper_angstroms_30d) || 0, Number(toolArgs.silver_angstroms_30d) || 0);
        } else if (toolName === 'search_field_protocols') {
          resultText = `Full 69-protocol unredacted engineering corpus query available at: https://datacenterfieldguides.com/llms-full.txt\nTopic: ${toolArgs.query}`;
        } else {
          return new Response(JSON.stringify({
            jsonrpc: '2.0',
            id: id || 1,
            error: { code: -32601, message: `Tool "${toolName}" not found.` }
          }), { status: 404, headers: CORS_HEADERS });
        }

        return new Response(JSON.stringify({
          jsonrpc: '2.0',
          id: id || 1,
          result: {
            content: [{ type: 'text', text: resultText }]
          }
        }), { status: 200, headers: CORS_HEADERS });
      }

      return new Response(JSON.stringify({
        jsonrpc: '2.0',
        id: id || null,
        error: { code: -32601, message: `Method "${rpcMethod}" not supported.` }
      }), { status: 400, headers: CORS_HEADERS });

    } catch (err) {
      return new Response(JSON.stringify({
        jsonrpc: '2.0',
        id: null,
        error: { code: -32700, message: 'Parse error: ' + err.message }
      }), { status: 400, headers: CORS_HEADERS });
    }
  }

  return new Response('Method Not Allowed', { status: 405, headers: CORS_HEADERS });
}
