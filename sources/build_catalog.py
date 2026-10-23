#!/usr/bin/env python3
import json
import os
import re
import unicodedata
from collections import defaultdict

ONEDRIVE_ROOT = "/Users/geese/Library/CloudStorage/OneDrive-Personal"
JSONL_PATH = "/Users/geese/Downloads/book/sources/catalog.staging.jsonl"
SUMMARY_PATH = "/Users/geese/Downloads/book/sources/catalog.staging.summary.json"

EXCLUDED_EXACT = {
    "优才申请资料",
    "初中报名",
    "home",
    "CFD逻辑",
    ".Trash",
    "node_modules",
    "__pycache__",
}

SENSITIVE_SUBSTRINGS = ("密码", "证件", "身份证", "通讯录")

INCLUDED_EXTS = {
    ".pdf",
    ".doc",
    ".docx",
    ".ppt",
    ".pptx",
    ".pps",
    ".ppsx",
    ".md",
    ".txt",
    ".rtf",
    ".odt",
    ".epub",
    ".mobi",
    ".azw3",
    ".xls",
    ".xlsx",
    ".xlsm",
    ".csv",
    ".xmind",
    ".emmx",
}

COMPANY_EXTS = {".doc", ".docx", ".md", ".txt", ".pptx"}
EBOOK_EXTS = {".epub", ".mobi", ".azw3"}
DATALESS_FLAG = 0x40000000
REASON_ORDER = [
    "z-library",
    "ebook",
    "standard",
    "third-party-dump",
    "vendor-manual",
    "公司输出",
    "root-note",
    "publication-bucket",
    "courseware",
    "paper",
    "published-book",
    "default",
]
SAMPLE_REASONS = ("publication-bucket", "courseware", "paper")

EXPECTED_TOP = [
    "培训文档",
    "公司输出",
    "个人技能",
    "数据中心技术文档",
    "CDFOM补充文档",
    "CDFOS补充文档",
    "color books",
    "commission",
]


def nfc(text):
    return unicodedata.normalize("NFC", text)


def contains_resume(name):
    return "简历" in name or "简历" in nfc(name)


def is_excluded_dir(name):
    normalized = nfc(name)
    if normalized in EXCLUDED_EXACT:
        return True
    if "交易记录" in normalized:
        return True
    return False


def is_standard_name(name):
    normalized = nfc(name)
    if "规范" in normalized or "标准" in normalized:
        return True
    lowered = normalized.lower()
    if "ashrae" in lowered or "tia-" in lowered or "ieee" in lowered or "nfpa" in lowered:
        return True
    if "gb/t" in lowered:
        return True
    if re.search(r"iso[\s_\-]*\d", lowered):
        return True
    if re.search(r"iec[\s_\-]*\d", lowered):
        return True
    if re.search(r"gb[\s_\-]*\d", lowered):
        return True
    return False


def is_publication_component(part):
    normalized = nfc(part)
    lowered = normalized.lower()
    if "ashrae" in lowered or "cobit" in lowered or "z-library" in lowered:
        return True
    if normalized == "国际标准":
        return True
    return False


def classify(rel_path, name, ext):
    normalized_name = nfc(name)
    lowered_name = normalized_name.lower()
    normalized_path = nfc(rel_path)
    parts = normalized_path.split("/")
    if "z-library" in normalized_path.lower():
        return "reference", "z-library"
    if ext in EBOOK_EXTS:
        return "reference", "ebook"
    if is_standard_name(normalized_name):
        return "reference", "standard"
    if normalized_path.startswith("doc from gao/"):
        return "reference", "third-party-dump"
    if (
        "用户手册" in normalized_name
        or "安装手册" in normalized_name
        or "选型手册" in normalized_name
        or "Handbook" in normalized_name
        or "handbook" in normalized_name
        or "操作手册" in normalized_name
    ):
        return "reference", "vendor-manual"
    if (
        normalized_path.startswith("公司输出/")
        and ext in COMPANY_EXTS
        and "翻译" not in normalized_name
        and "第34章" not in normalized_name
        and "34章" not in normalized_name
    ):
        return "authored", "公司输出"
    if normalized_path == "数据说明.md":
        return "authored", "root-note"
    if (parts and parts[0] == "color books") or any(is_publication_component(part) for part in parts):
        return "reference", "publication-bucket"
    if ext == ".pdf" and (
        normalized_path.startswith("CDFOM补充文档/") or normalized_path.startswith("CDFOS补充文档/")
    ):
        return "reference", "courseware"
    if ext == ".pdf" and "论文集/" in normalized_path:
        return "reference", "paper"
    if ext == ".pdf" and (
        "handbook" in lowered_name or "guidelines" in lowered_name or "edition" in lowered_name
    ):
        return "reference", "published-book"
    if ext == ".pdf" and "10.1109" in normalized_name:
        return "reference", "paper"
    return "working", "default"


def main():
    if not os.path.isdir(ONEDRIVE_ROOT):
        raise SystemExit("OneDrive root is not a directory")

    records = []
    errors = []
    seen_top = set()
    excluded_dir_names = set()
    top_counts = defaultdict(int)
    skipped_sensitive_filename_count = 0
    root_norm = os.path.normpath(ONEDRIVE_ROOT)

    def add_error(message):
        if contains_resume(message):
            message = "redacted"
        if len(errors) < 50:
            errors.append(message)

    def on_walk_error(err):
        add_error(str(err))

    for dirpath, dirnames, filenames in os.walk(
        ONEDRIVE_ROOT,
        topdown=True,
        followlinks=False,
        onerror=on_walk_error,
    ):
        if os.path.normpath(dirpath) == root_norm:
            for dirname in dirnames:
                seen_top.add(nfc(dirname))

        kept = []
        for dirname in dirnames:
            if is_excluded_dir(dirname):
                excluded_dir_names.add(nfc(dirname))
                continue
            kept.append(dirname)
        dirnames[:] = kept

        for filename in filenames:
            normalized_filename = nfc(filename)
            relative = os.path.relpath(os.path.join(dirpath, filename), ONEDRIVE_ROOT)
            parts = relative.split(os.sep)
            sensitive = any(token in normalized_filename for token in SENSITIVE_SUBSTRINGS)
            hidden = filename.startswith(".") or filename.startswith("._")
            if sensitive:
                skipped_sensitive_filename_count += 1
            if sensitive or hidden:
                continue

            ext = os.path.splitext(filename)[1].lower()
            if ext not in INCLUDED_EXTS:
                continue

            full_path = os.path.join(dirpath, filename)
            try:
                stat_result = os.lstat(full_path)
            except OSError as err:
                add_error("lstat failed")
                continue

            relative_path = relative.replace(os.sep, "/")
            file_class, reason = classify(relative_path, filename, ext)
            if "/" in relative_path:
                top_level = nfc(relative_path.split("/", 1)[0])
            else:
                top_level = "(root)"
            top_counts[top_level] += 1
            flags = getattr(stat_result, "st_flags", 0)
            records.append(
                {
                    "path": relative_path,
                    "ext": ext,
                    "bytes": stat_result.st_size,
                    "dataless": bool(flags & DATALESS_FLAG),
                    "class": file_class,
                    "reason": reason,
                }
            )

    records.sort(key=lambda item: item["path"])

    os.makedirs(os.path.dirname(JSONL_PATH), exist_ok=True)
    with open(JSONL_PATH, "w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    class_counts = {"authored": 0, "working": 0, "reference": 0}
    reason_counts = {reason: 0 for reason in REASON_ORDER}
    samples = {"authored": [], "working": [], "reference": []}
    reason_samples = {reason: [] for reason in SAMPLE_REASONS}
    reference_with_text_field = 0
    included_resume_count = 0
    ashrae_count = 0
    cobit_count = 0
    personal_dir_hits = {
        "优才申请资料": 0,
        "初中报名": 0,
        "home": 0,
        "CFD逻辑": 0,
        "交易记录": 0,
    }
    for record in records:
        path = record["path"]
        normalized = nfc(path)
        lowered = normalized.lower()
        parts = normalized.split("/")
        file_class = record["class"]
        reason = record["reason"]
        class_counts[file_class] = class_counts.get(file_class, 0) + 1
        reason_counts[reason] = reason_counts.get(reason, 0) + 1
        if contains_resume(path):
            included_resume_count += 1
        else:
            if file_class in samples and len(samples[file_class]) < 12:
                samples[file_class].append(path)
            if reason in reason_samples and len(reason_samples[reason]) < 8:
                reason_samples[reason].append(path)
        if "ashrae" in lowered:
            ashrae_count += 1
        if "cobit" in lowered:
            cobit_count += 1
        if "优才申请资料" in parts:
            personal_dir_hits["优才申请资料"] += 1
        if "初中报名" in parts:
            personal_dir_hits["初中报名"] += 1
        if "home" in parts:
            personal_dir_hits["home"] += 1
        if "CFD逻辑" in parts:
            personal_dir_hits["CFD逻辑"] += 1
        if any("交易记录" in part for part in parts[:-1]):
            personal_dir_hits["交易记录"] += 1
        if file_class == "reference" and "text" in record:
            reference_with_text_field += 1

    expected_top_missing = [name for name in EXPECTED_TOP if name not in seen_top]
    top_level_with_zero_included = [
        name
        for name in EXPECTED_TOP
        if name in seen_top and top_counts.get(name, 0) == 0
    ]

    summary = {
        "total": len(records),
        "counts_by_class": class_counts,
        "counts_by_reason": reason_counts,
        "counts_by_top_level": {key: top_counts[key] for key in sorted(top_counts)},
        "skipped_personal_dir_hits": sorted(excluded_dir_names),
        "skipped_sensitive_filename_count": skipped_sensitive_filename_count,
        "included_resume_count": included_resume_count,
        "ashrae_count": ashrae_count,
        "cobit_count": cobit_count,
        "personal_dir_hits": personal_dir_hits,
        "reference_with_text_field": reference_with_text_field,
        "errors": errors[:50],
        "samples": samples,
        "samples_by_reason": reason_samples,
        "expected_top_missing": expected_top_missing,
        "top_level_with_zero_included": top_level_with_zero_included,
    }
    with open(SUMMARY_PATH, "w", encoding="utf-8") as handle:
        json.dump(summary, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


if __name__ == "__main__":
    main()
