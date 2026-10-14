#!/usr/bin/env python3
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_content_index import extract

NAS = os.path.join(os.path.dirname(__file__), "content", "nas.sqlite")
CORPUS = os.path.join(os.path.dirname(__file__), "content", "corpus")
GAP = os.path.join(os.path.dirname(__file__), "hydrate_ok.txt")
ONEDRIVE = "/Users/geese/Library/CloudStorage/OneDrive-Personal"
SKIP_PARTS = ("优才申请资料", "初中报名", "home", "CFD逻辑", "交易记录", "OneDrive备份")
SENSITIVE = ("密码", "证件", "身份证", "通讯录")


def blocked(rel):
    parts = rel.split("/")
    if any(p in SKIP_PARTS for p in parts):
        return True
    name = parts[-1]
    return any(tok in name for tok in SENSITIVE)


def out_path(rel):
    return os.path.join(CORPUS, rel + ".md")


def write_md(rel, text, source):
    dest = out_path(rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(f"source: {source}\npath: {rel}\n\n")
        handle.write(text)


def main():
    os.makedirs(CORPUS, exist_ok=True)
    conn = sqlite3.connect(f"file:{NAS}?mode=ro", uri=True)
    written = 0
    skipped = 0
    for rel, text, chars in conn.execute("SELECT path, text, chars FROM docs"):
        if blocked(rel) or not text or chars <= 20:
            skipped += 1
            continue
        write_md(rel, text, "nas")
        written += 1
        if written % 2000 == 0:
            print(f"nas {written}", flush=True)
    gap_new = 0
    gap_skip = 0
    if os.path.exists(GAP):
        for line in open(GAP, encoding="utf-8"):
            rel = line.rstrip("\n")
            if not rel or blocked(rel):
                gap_skip += 1
                continue
            dest = out_path(rel)
            if os.path.exists(dest) and os.path.getsize(dest) > 80:
                continue
            full = os.path.join(ONEDRIVE, rel)
            if not os.path.lexists(full):
                gap_skip += 1
                continue
            flags = getattr(os.lstat(full), "st_flags", 0)
            if flags & 0x40000000:
                gap_skip += 1
                continue
            text, method = extract(full)
            if not text or len(text.strip()) <= 20:
                gap_skip += 1
                continue
            write_md(rel, text[:120000], f"onedrive:{method}")
            gap_new += 1
    print(f"NAS_WRITTEN {written} NAS_SKIPPED {skipped} GAP_NEW {gap_new} GAP_SKIP {gap_skip}")


if __name__ == "__main__":
    main()
