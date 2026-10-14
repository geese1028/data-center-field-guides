# Translation Languages & Publication Registry

Owner order: Multilingual publication across Japanese, Indonesian, Korean, Thai, and Arabic, with Chinese operator verification sheets.

Checked against global AI data center build-out hubs. Localized field editions designed to bridge regional engineering standards with auditable commissioning protocols.

| Language | Code | Market Focus & Engineering Rationale |
| --- | --- | --- |
| Japanese | `ja` | Osaka (KIX15), Tokyo hyperscale expansions. Rigorous technical standards, high-density AI rack commissioning. |
| Indonesian | `id` | Jakarta and Batam mega-clusters. Multilingual engineering crews; field operational language is Bahasa Indonesia. |
| Korean | `ko` | Incheon & Seoul high-density liquid cooling AI clusters. Stringent telemetry and commissioning requirements. |
| Thai | `th` | Bangkok and Eastern Economic Corridor (EEC) hyperscale facilities. Rapid adoption of direct-to-chip liquid cooling. |
| Arabic | `ar` | Gulf Cooperation Council (GCC) high-ambient AI campus builds. Localized operational editions with full RTL layout support. |

## Translated Titles & Scope

All translations derive from the upgraded, rigorous engineering manuscripts. Formulas ($Q = \dot{m} C_p \Delta T$, Darcy-Weisbach $\Delta P$), Danfoss FD83 quick disconnect standards, 1-second telemetry timelines, ASHRAE Guideline 0/202 levels, and 2N power loading limits ($\le 0.45 P_{\text{rated}}$) are preserved intact.

| Book | Slug | Translated Languages | Source Chapters | Key Upgraded Focus |
| --- | --- | --- | --- | --- |
| **01** | `01-liquid-load-bank` | `ja`, `id`, `ko`, `th`, `ar` | 20 chapters | Danfoss FD83 dual-interlock couplings, 50μm bypass flush, Darcy-Weisbach flow balance, Gate 1-5 acceptance sheets. |
| **02** | `02-read-load-bank-data` | `ja`, `id`, `ko`, `th`, `ar` | 17 chapters | 5-line flash report table, 1s telemetry, NTP/PTP timestamps, polling gap criteria (>3s flag, >10s fail), CUSUM change-points. |
| **03** | `03-run-one-test` | `ja`, `id`, `ko`, `th`, `ar` (+ `zh` sheets) | 17 chapters | ASHRAE Levels 1-5, cold pump curve density shifts (PG25 20°C vs 45°C), 7 complete auditable verification sheets. |
| **05** | `05-run-the-day` | `ja`, `id`, `ko`, `th`, `ar` | 13 chapters | Shift lifecycle, SOP/MOP/EOP governance, 6 physical inspection stations, 2N capacity ceiling ($\le 0.45 P_{\text{rated}}$), closeout sheet. |

## Build & Asset Artifacts

Each edition compiles into:
1. Standard EPUB 3.0: `books/<slug>/epub/<lang>/<file>.<lang>.epub`
2. High-resolution Cover (1600×2560): `books/<slug>/figures/covers/<lang>.jpg`
3. KDP Upload Pack: `books/<slug>/publish/<lang>/PACK.md`

All diagrams and plate graphics retain standardized English engineering nomenclature for universal cross-vendor verification.
