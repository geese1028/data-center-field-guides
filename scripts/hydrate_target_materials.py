#!/usr/bin/env python3
"""
scripts/hydrate_target_materials.py
精准按需唤醒脚本：将全书《物理智能体现场圣经》所必需的核心高价值原件
从 macOS OneDrive (CloudStorage) 虚拟占位（dataless）状态同步至本地，
坚决避免下载无用的巨型视频或冗余安装包。
"""

import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path("/Users/geese/Library/CloudStorage/OneDrive-Personal")
OUTPUT_MANIFEST = Path("/Users/geese/Downloads/book/catalog/target_hydrated_manifest.json")
SF_DATALESS = 0x40000000
MAX_WORKERS = 4

# 精选核心黄金母文档清单（涵盖全书六大部卷）
TARGET_FILES = [
    # Volume I: 液冷与热力极限
    "假负载采集和控制.pptx",
    "DCIsight/日本AI数据中心/技术方案/假负载测试sow.docx",
    "DCIsight/日本AI数据中心/技术方案/施工验收sow.docx",
    "DCIsight/日本AI数据中心/技术方案/日本液冷机房NRT10项目技术初步审查报告20250810.doc",
    "DCIsight/日本AI数据中心/报告/日本 NRT 10 数据中心 S430 液冷机房 CFD 散热仿真报告（讨论稿）.docx",
    "DCIsight/日本AI数据中心/图纸/评审资料汇总/10.SMCI_1.8MW CDU_Manual_rev1_PBD 20250619.pdf",
    "CDFOM补充文档/扩展讲义及扩展话题/话题1末端气流组织治理/数据中心CFD仿真输入清单.xlsx",
    "CDFOM补充文档/扩展讲义及扩展话题/话题1末端气流组织治理/末端气流组织对比.pptx",
    "公司输出/气流组织治理.docx",

    # Volume II: 现场调试与验收拒签
    "【1】新版体系文件【0410】/AIS-阿里巴巴租用IDC机房验收标准V2.1（终版）.pdf",
    "数据中心技术文档/CDFOM/最佳实践/百度M1机房验证项目报告 Book11.pdf",
    "commission/074 Fundamental Commissioning Steps.pdf",
    "commission/049e Water Cooled CHILLER Pre-Functional Checklist.xlsx",
    "commission/049c Cooling Tower Pre-Functional Checklist.xlsx",
    "吴振杰/东园1.1期验收资料/02设备资料/05各设备产品说明书、维护手册（电气、暖通、弱电、消防）/电气/34、假负载用户手册/AC10.5KV-2000KW使用说明书.doc",

    # Volume III: 电气动力与国家级计量
    "中国计量院/售前资料/售前资料/其他能力/数据中心测试介绍.pptx",
    "中国计量院/售前资料/售前资料/其他能力/智算中心算力测评-NIM V1.0.pptx",
    "中国计量院/售前资料/售前资料/其他能力/金融业数据中心系列认证.pptx",

    # Volume IV: 潜伏杀手：腐蚀与水质
    "中国计量院/售前资料/售前资料/其他能力/腐蚀测试.pptx",
    "CDFOM补充文档/扩展讲义及扩展话题/话题1末端气流组织治理/数据中心末端气流组织及气体腐蚀治理.pptx",
    "commission/049j Flushing and Chemical Cleaning Checklist.xlsx",

    # Volume V: 超大规模云基地运维与 GOC
    "【1】新版体系文件【0410】/NA61-2 GOC报警阈值标准V1.1-发布版【0221 利东】.xlsx",
    "【1】新版体系文件【0410】/AIS-IDC EMS3.1 监控接入指导手册V1.6.docx",
    "【1】新版体系文件【0410】/AIS-文档规范-IDC运营事件管理规范V1.4-20191020.pdf",
    "【1】新版体系文件【0410】/阿里巴巴庙滩二期体系目录.xlsx",
    "【1】新版体系文件【0410】/鹏城实验室项目汇报.pptx",
    "【1】新版体系文件【0410】/ALZJ-04-技术管理/ALZJ-JS-4.3 运维操作手册(SOP)/ALZJ-JS-4.3运维操作手册暖通分册/暖通部分---马利冷塔开机&关机&参数设定操作流程.docx",
    "【1】新版体系文件【0410】/ALZJ-04-技术管理/ALZJ-JS-4.3 运维操作手册(SOP)/ALZJ-JS-4.3运维操作手册暖通分册/暖通部分---反渗透系统参数设置及系统开启操作流程.docx",
    "【1】新版体系文件【0410】/ALZJ-04-技术管理/ALZJ-JS-4.3 运维操作手册(SOP)/ALZJ-JS-4.3运维操作手册暖通分册/暖通部分---定压补水系统开机&关机&参数设定操作流程.docx",
]


def hydrate_file(rel_path: str):
    full_path = ROOT / rel_path
    if not (full_path.exists() or full_path.is_symlink() or os.path.lexists(full_path)):
        return rel_path, "missing", 0

    try:
        flags = getattr(os.lstat(full_path), "st_flags", 0)
        is_dataless = bool(flags & SF_DATALESS)
        size = full_path.stat().st_size if full_path.exists() else 0

        # 如果处于 dataless 状态，读取流以触发 macOS 自动下载
        if is_dataless:
            with open(full_path, "rb") as f:
                while f.read(1024 * 1024):
                    pass
            new_flags = getattr(os.lstat(full_path), "st_flags", 0)
            if new_flags & SF_DATALESS:
                return rel_path, "still_dataless", size
            size = full_path.stat().st_size
            return rel_path, "hydrated_now", size
        else:
            return rel_path, "already_local", size
    except Exception as e:
        return rel_path, f"error:{type(e).__name__}", 0


def main():
    print(f"🚀 开始按需唤醒目标母文档 (总计: {len(TARGET_FILES)} 份)...")
    manifest = []
    counts = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(hydrate_file, rel): rel for rel in TARGET_FILES}
        for fut in as_completed(futures):
            rel, status, size = fut.result()
            counts[status] = counts.get(status, 0) + 1
            print(f"[{status.upper()}] {rel} ({size // 1024} KB)")
            manifest.append({
                "relative_path": rel,
                "status": status,
                "size_bytes": size,
                "size_kb": size // 1024
            })

    OUTPUT_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("\n📊 唤醒统计结果:")
    for status, count in sorted(counts.items()):
        print(f"  - {status}: {count} 份")
    print(f"\n✅ 清单已保存至: {OUTPUT_MANIFEST}")


if __name__ == "__main__":
    main()
