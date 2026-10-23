#!/usr/bin/env python3
"""
scripts/build_publication_dossiers.py
从已唤醒的权威出版物（ASHRAE Datacom系列、BSRIA调试指南、IEEE Color Books）中
提炼权威物理基准与测试标准，并与作者现场项目落地的实战规则（Skill断言）进行深度映射绑定。
"""

from pathlib import Path

OUT_DIR = Path("/Users/geese/Downloads/book/dossiers")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def build_liquid_cooling_and_cfd_dossier():
    content = """# 权威出版物与现场判定映射：液冷温区、流体动力学与 CFD 审查 (Dossier)

> **权威文献源**：
> 1. ASHRAE TC 9.9: *Liquid Cooling Guidelines for Datacom Equipment Centers*
> 2. Jim A. Wingate: *Hydraulics, Pipe Flow, Industrial*
> 3. SPX-APV: *Heat Transfer Handbook* (Plate Heat Exchangers & CDU Core)
> **实战映射源**：
> - `DCIsight/日本AI数据中心/技术方案/假负载测试sow.docx`
> - `10.SMCI_1.8MW CDU_Manual_rev1_PBD 20250619.pdf`
> - `数据中心CFD仿真输入清单.xlsx`

---

## 1. 权威基准：ASHRAE 液冷水温等级分类 (Water Temperature Classes)

| 等级 (Class) | 设施水供水温度 (FWS Supply Temp) | 适用热交换技术 | 冷却设施类型 (Heat Rejection) |
| :--- | :--- | :--- | :--- |
| **W17** | $2^\\circ\\text{C} \\le T_{\\text{supply}} \\le 17^\\circ\\text{C}$ | 冷水机组 (Chiller) 直接供水 | 压缩式冷机、冰蓄冷 |
| **W27** | $17^\\circ\\text{C} < T_{\\text{supply}} \\le 27^\\circ\\text{C}$ | 板换自然冷却 / 冷水机组微调 | 湿式冷却塔、干冷器带喷淋 |
| **W32** | $27^\\circ\\text{C} < T_{\\text{supply}} \\le 32^\\circ\\text{C}$ | 自然冷却优先 (Free Cooling) | 干冷器 (Dry Cooler) |
| **W45** | $32^\\circ\\text{C} < T_{\\text{supply}} \\le 45^\\circ\\text{C}$ | 全年自然冷却 (Year-round Free Cooling) | 纯干冷器、中水回用废热利用 |
| **W+** | $T_{\\text{supply}} > 45^\\circ\\text{C}$ | 极端高热密芯片废热利用 | 区域供暖管网直连 |

---

## 2. 现场实战 Skill 判定规则：CDU 与假负载水力平衡

```mermaid
flowchart TD
    Start["采集二次侧遥测: 流量 Q, 供温 T_s, 回温 T_r, 压差 DP, 功率 P"] --> CheckDP{"DP 是否满足\n阻抗曲线?"}
    CheckDP --"否: 压差异常偏小"--> FlagBypass["【CRITICAL】检出二次侧旁通阀伪平衡开度"]
    CheckDP --"是"--> CalcHeat["计算流体实测热负荷:\nQ_thermal = C_p * rho * Q * (T_r - T_s)"]
    CalcHeat --> ComparePower{"|Q_thermal - P_load| / P_load\n> 5% 容差?"}
    ComparePower --"超标"--> FlagFraud["【FATAL】热负荷虚标或流量计/温敏零点漂移"]
    ComparePower --"合规"--> Pass["测试有效，进入稳态时长核验"]
```

### [Skill 判定断言]
* **断言 1 (假稳态一票否决)**：
  在假负载测试中，若 $\\Delta T = T_{\\text{return}} - T_{\\text{supply}}$ 达标，但一次侧水阀开度持续在 $15\\% \\sim 25\\%$ 高频振荡（Hunting），即便机柜进水温度在允许公差内，判定为控制回路未调谐（PID Tuning Failure），**拒绝签署工况验收**。
* **断言 2 (NVL72 快换接头泄漏阻抗)**：
  二次侧每一回路在额定流量 $Q_{\\text{rated}}$ 下，通过快换接头（QDC）与管路的局部阻抗压降 $\\Delta P$ 若小于设计额定值的 $70\\%$，判定为存在未完全接插或流体短路旁通，**禁止上电施加 100% 满功率阶跃**。
"""
    (OUT_DIR / "vol1_ashrae_liquid_cooling_and_field_rules.md").write_text(content, encoding="utf-8")
    print("Generated vol1_ashrae_liquid_cooling_and_field_rules.md")


def build_corrosion_and_bsria_dossier():
    content = """# 权威出版物与现场判定映射：气体腐蚀、管道预清洗与水化学 (Dossier)

> **权威文献源**：
> 1. ASHRAE TC 9.9: *Particulate and Gaseous Contamination in Datacom Environments (2nd Ed)*
> 2. ANSI/ISA-71.04-2013: *Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*
> 3. BSRIA BG 29/2012: *Pre-Commission Cleaning of Pipework Systems (2nd Edition)*
> 4. APV: *Corrosion Handbook*
> **实战映射源**：
> - `中国计量院/售前资料/售前资料/其他能力/腐蚀测试.pptx`
> - `CDFOM补充文档/扩展讲义及扩展话题/话题1末端气流组织治理/数据中心末端气流组织及气体腐蚀治理.pptx`
> - `commission/049j Flushing and Chemical Cleaning Checklist.xlsx`

---

## 1. 权威基准：ANSI/ISA-71.04 铜/银腐蚀分级与反应性监测

测试周期：**30 天金属反应性暴露试验（Reactivity Monitoring via Metal Coupons）**

| 环境严酷度等级 (Severity Level) | 铜反应率 (Copper Reactivity, Å/month) | 银反应率 (Silver Reactivity, Å/month) | 对数据中心高密 IT / 芯片管脚的影响 |
| :--- | :--- | :--- | :--- |
| **G1 - Mild (温和清洁)** | $< 300$ | $< 200$ | 极其安全，满足机房保修最高标准 |
| **G2 - Moderate (中度污染)** | $300 \\sim 1000$ | $200 \\sim 1000$ | 腐蚀见微，无铅焊料及细间距芯片出现轻微硫化 |
| **G3 - Harsh (严重污染)** | $1000 \\sim 2000$ | $1000 \\sim 2000$ | **高危警告**：板卡微短路概率大幅上升，需强制化学气相过滤 |
| **GX - Severe (极端恶劣)** | $> 2000$ | $> 2000$ | **致命毁灭**：服务器保修失效，2~6个月内发生爬行腐蚀击穿 |

---

## 2. 权威基准：BSRIA BG 29 管道系统清洗与水质冲洗验收

* **冲洗流速法则 (Flushing Velocity Rule)**：
  系统水冲洗时，主干管与支管的最末端实测流速**必须达到系统设计工作流速的 $115\\% \\sim 120\\%$**，且绝对流速不得低于 $1.0\\text{ m/s}$（使管底沉渣、铁锈和焊渣保持悬浮剥离）。
* **水质澄明度标准**：
  冲洗出水浊度（Turbidity）必须 $\\le 5\\text{ NTU}$，且悬浮固体含量（TSS）$< 30\\text{ mg/L}$，方可转入化学钝化预膜程序。

---

## 3. 现场实战 Skill 判定规则：腐蚀与水质一票否决

### [Skill 判定断言]
* **断言 1 (银腐蚀穿透一票否决)**：
  在沿海工业区或临近污水处理厂数据中心，若银测试片暴露 30 天生长厚度超过 $1000\\text{ \\AA/month}$（达到 G3 级别），即便机房温湿度严格处于 ASHRAE A1 推荐区内，**判定环境洁净度验收不合格，叫停服务器进场上电**。
* **断言 2 (冲洗假循环作弊识别)**：
  审核施工方《管路冲洗记录表》时，若其末端连通旁通管管径小于主管径的 $50\\%$，或冲洗泵流量无法提供 $1.15 \\times Q_{\\text{design}}$ 的动力压头，**直接判定冲洗盲区超标，拒绝签字进入打压试运行**。
"""
    (OUT_DIR / "vol4_ashrae_bsria_corrosion_water_rules.md").write_text(content, encoding="utf-8")
    print("Generated vol4_ashrae_bsria_corrosion_water_rules.md")


def build_ieee_electrical_dossier():
    content = """# 权威出版物与现场判定映射：IEEE 电气动力、高精度接地与可靠性核算 (Dossier)

> **权威文献源**：
> 1. IEEE STD 1100 (Emerald Book): *Powering and Grounding Electronic Equipment*
> 2. IEEE STD 493 (Gold Book): *Design of Reliable Industrial and Commercial Power Systems*
> 3. IEEE STD 446 (Orange Book): *Emergency and Standby Power Systems*
> 4. NETA ATS: *Standard for Acceptance Testing Specifications for Electrical Power Equipment*
> **实战映射源**：
> - 10.5kV 2000kW 假负载测试规程及用户手册
> - 智算中心算力测评技术方案与现场实测报告

---

## 1. 权威基准：IEEE 1100 (绿皮书) 信号参考平面 (SRP) 与接地阻抗

* **等电位网格阻抗 (Signal Reference Grid, SRG)**：
  活动地板下 $600\\text{mm} \\times 600\\text{mm}$ 铜带网格，在 $10\\text{MHz}$ 射频干扰频率下，对地阻抗不得大于 $1\\ \\Omega$。
* **零地电压 (Neutral-to-Ground Voltage)**：
  在末端 PDU 满载与空载转换瞬间，IT 关键设备输入端零地电压最大峰值不得超过 $1.5\\text{ V}$（RMS 稳态值不得超过 $1.0\\text{ V}$）。

---

## 2. 现场实战 Skill 判定规则：大功率带载测试与假负载安全

### [Skill 判定断言]
* **断言 1 (中高压柴发突加负载频率跌落)**：
  在 10.5kV 发电机组进行 $0\\% \\to 100\\%$ 满额瞬态突加阶跃测试（Step Load）时，瞬态频率跌落不得超过额定值的 $10\\%$，恢复至稳态带的时间不得大于 $3\\text{ 秒}$；若电压突降超过 $15\\%$，**判定柴发调速器（Governor）及励磁 AVR 响应不合格，拒绝电气完工交接**。
* **断言 2 (接地回路环流短路)**：
  高密液冷机柜与机柜排必须具备独立的双路径接地。若检测到不同机架保护地之间存在大于 $0.5\\text{ A}$ 的工频杂散漏电流，**判定存在二次回路接线中性线混接，立断总闸停机**。
"""
    (OUT_DIR / "vol3_ieee_electrical_grounding_rules.md").write_text(content, encoding="utf-8")
    print("Generated vol3_ieee_electrical_grounding_rules.md")


if __name__ == "__main__":
    build_liquid_cooling_and_cfd_dossier()
    build_corrosion_and_bsria_dossier()
    build_ieee_electrical_dossier()
    print("All publication-to-field dossiers built successfully!")
