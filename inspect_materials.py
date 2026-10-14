#!/usr/bin/env python3
"""
inspect_materials.py - 素材扫描与盘点工具
用于扫描用户导入到当前工作区的历史书籍与项目产出物，统计文档分布与结构。
"""

import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple


IGNORE_DIRS: Set[str] = {
    ".git",
    ".gemini",
    ".idea",
    ".vscode",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
}

DOC_EXTENSIONS: Dict[str, str] = {
    ".md": "Markdown 文档",
    ".markdown": "Markdown 文档",
    ".txt": "纯文本",
    ".docx": "Word 文档",
    ".doc": "Word 文档",
    ".pdf": "PDF 文件",
    ".epub": "电子书 (EPUB)",
    ".mobi": "电子书 (MOBI)",
    ".pptx": "演示文稿",
    ".xlsx": "表格数据",
    ".csv": "表格数据",
    ".html": "网页/HTML",
    ".json": "结构化数据",
    ".py": "代码资产 (Python)",
    ".go": "代码资产 (Go)",
    ".ts": "代码资产 (TypeScript)",
    ".js": "代码资产 (JavaScript)",
}


def format_bytes(size: int) -> str:
    """格式化字节大小为易读字符串。"""
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"


def scan_directory(base_dir: Path) -> Tuple[Dict[str, List[Path]], int]:
    """
    遍历目录，过滤无效隐藏文件夹，按类型分组文件。
    返回: (类型分类字典, 文件总字节数)
    """
    categorized: Dict[str, List[Path]] = defaultdict(list)
    total_bytes = 0

    try:
        for root, dirs, files in os.walk(base_dir):
            # 过滤不需要扫描的目录
            dirs[:] = [d for d in dirs if not d.startswith(".") and d not in IGNORE_DIRS]

            for file_name in files:
                if file_name.startswith("."):
                    continue
                file_path = Path(root) / file_name
                try:
                    file_size = file_path.stat().st_size
                except (OSError, PermissionError):
                    file_size = 0

                total_bytes += file_size
                suffix = file_path.suffix.lower()
                category = DOC_EXTENSIONS.get(suffix, "其他文件")
                categorized[category].append(file_path)
    except Exception as exc:
        sys.stderr.write(f"扫描异常: {exc}\n")

    return categorized, total_bytes


def main() -> None:
    target_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

    if not target_path.exists() or not target_path.is_dir():
        sys.stderr.write(f"错误: 目标路径不存在或非目录: {target_path}\n")
        sys.exit(1)

    print("=" * 60)
    print(f"【素材目录盘点报告】")
    print(f"扫描路径: {target_path.resolve()}")
    print("=" * 60)

    categorized_files, total_size = scan_directory(target_path)
    total_count = sum(len(items) for items in categorized_files.values())

    if total_count == 0:
        print("未在该目录下检测到任何有效文件。")
        print("请将 OneDrive 中的历史书籍/文档同步或复制至当前目录后重试。")
        print("=" * 60)
        return

    print(f"总计文件数: {total_count} 个 | 占用存储: {format_bytes(total_size)}\n")
    print("【分类明细】")
    for category, files in sorted(categorized_files.items(), key=lambda x: len(x[1]), reverse=True):
        cat_size = sum(f.stat().st_size for f in files if f.exists())
        print(f"  - {category:<16}: {len(files):>4} 个文件 ({format_bytes(cat_size)})")

    print("\n【顶级目录与主题概览】")
    top_level_entries = [p for p in target_path.iterdir() if not p.name.startswith(".")]
    for entry in sorted(top_level_entries):
        if entry.is_dir():
            count = sum(1 for _ in entry.rglob("*") if _.is_file())
            print(f"  📁 [目录] {entry.name}/ (含 {count} 个文件)")
        else:
            print(f"  📄 [文件] {entry.name}")

    print("=" * 60)


if __name__ == "__main__":
    main()
