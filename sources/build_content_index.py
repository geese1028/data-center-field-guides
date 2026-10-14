#!/usr/bin/env python3
import argparse
import os
import re
import sqlite3
import subprocess
import zipfile
from multiprocessing import Pool
from xml.etree import ElementTree as ET

EXTS = {
    ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".pps", ".ppsx",
    ".xls", ".xlsx", ".xlsm", ".csv", ".md", ".txt", ".rtf",
}
SKIP_DIRS = {
    "优才申请资料", "初中报名", "home", "CFD逻辑", "OneDrive备份",
    "node_modules", "__pycache__", ".Trash",
}
SENSITIVE = ("密码", "证件", "身份证", "通讯录")
MAX_CHARS = 120000
PDF_TIMEOUT = 90


def local(tag):
    return tag.rsplit("}", 1)[-1]


def xml_text(blob):
    try:
        root = ET.fromstring(blob)
    except ET.ParseError:
        return ""
    parts = []
    for node in root.iter():
        if node.text and node.text.strip():
            parts.append(node.text.strip())
        if node.tail and node.tail.strip():
            parts.append(node.tail.strip())
    return "\n".join(parts)


def zip_members(path, pred):
    chunks = []
    try:
        with zipfile.ZipFile(path) as zf:
            names = [n for n in zf.namelist() if pred(n)]
            names.sort()
            for name in names:
                chunks.append(xml_text(zf.read(name)))
    except (zipfile.BadZipFile, OSError, RuntimeError):
        return "", "badzip"
    return "\n".join(c for c in chunks if c), "zipxml"


def doc_strings(path):
    try:
        data = open(path, "rb").read()
    except OSError as exc:
        return "", f"error:{type(exc).__name__}"
    if data[:8] == b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1":
        text = data.decode("utf-16le", errors="ignore")
        text = re.sub(r"[^\u4e00-\u9fff\u3000-\u303f\w\s.,;:()\[\]%/+\-_=]{1,}", " ", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip(), "ole"
    return data.decode("utf-8", errors="ignore"), "bytes"


def extract(path):
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext == ".pdf":
            proc = subprocess.run(
                ["pdftotext", "-q", "-enc", "UTF-8", path, "-"],
                capture_output=True,
                timeout=PDF_TIMEOUT,
            )
            if proc.returncode != 0:
                err = proc.stderr.decode("utf-8", errors="ignore")[:200]
                return "", f"pdftotext:{err}"
            return proc.stdout.decode("utf-8", errors="ignore"), "pdftotext"
        if ext == ".docx":
            return zip_members(path, lambda n: n.startswith("word/") and n.endswith(".xml"))
        if ext in {".pptx", ".ppsx"}:
            return zip_members(path, lambda n: n.startswith("ppt/slides/slide") and n.endswith(".xml"))
        if ext in {".xlsx", ".xlsm"}:
            return zip_members(path, lambda n: n.startswith("xl/") and n.endswith(".xml"))
        if ext in {".md", ".txt", ".csv", ".rtf"}:
            with open(path, "rb") as handle:
                raw = handle.read(8_000_000)
            return raw.decode("utf-8", errors="ignore"), "text"
        if ext in {".doc", ".ppt", ".xls", ".pps"}:
            return doc_strings(path)
    except subprocess.TimeoutExpired:
        return "", "timeout"
    except Exception as exc:
        return "", f"error:{type(exc).__name__}"
    return "", "skip"


def worker(path):
    text, method = extract(path)
    truncated = 0
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]
        truncated = 1
    try:
        size = os.path.getsize(path)
    except OSError:
        size = -1
    return path, os.path.splitext(path)[1].lower(), size, len(text), truncated, method, text


def skip_dir(name):
    if name in SKIP_DIRS or name.startswith("."):
        return True
    if "交易记录" in name:
        return True
    return False


def skip_file(path):
    name = os.path.basename(path)
    if name.startswith(".") or name.startswith("._"):
        return True
    if any(tok in name for tok in SENSITIVE):
        return True
    if "简历" not in path and any(part in SKIP_DIRS for part in path.split(os.sep)):
        return True
    return False


def collect(root):
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not skip_dir(d)]
        for name in filenames:
            ext = os.path.splitext(name)[1].lower()
            if ext not in EXTS:
                continue
            full = os.path.join(dirpath, name)
            if skip_file(full):
                continue
            found.append(full)
    found.sort()
    return found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--db", required=True)
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.db), exist_ok=True)
    conn = sqlite3.connect(args.db)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute(
        """CREATE TABLE IF NOT EXISTS docs (
            path TEXT PRIMARY KEY,
            ext TEXT,
            bytes INTEGER,
            chars INTEGER,
            truncated INTEGER,
            method TEXT,
            text TEXT
        )"""
    )
    try:
        conn.execute(
            """CREATE VIRTUAL TABLE IF NOT EXISTS docs_fts USING fts5(
                path, text, tokenize='trigram'
            )"""
        )
    except sqlite3.OperationalError:
        conn.execute(
            """CREATE VIRTUAL TABLE IF NOT EXISTS docs_fts USING fts5(
                path, text
            )"""
        )
    have = {row[0] for row in conn.execute("SELECT path FROM docs")}
    files = [p for p in collect(args.root) if p not in have]
    print(f"todo {len(files)} have {len(have)}", flush=True)
    done = 0
    with Pool(args.workers) as pool:
        for row in pool.imap_unordered(worker, files, chunksize=4):
            path, ext, size, chars, truncated, method, text = row
            rel = os.path.relpath(path, args.root)
            conn.execute(
                "INSERT OR REPLACE INTO docs VALUES (?,?,?,?,?,?,?)",
                (rel, ext, size, chars, truncated, method, text),
            )
            conn.execute("INSERT INTO docs_fts(path, text) VALUES (?, ?)", (rel, text))
            done += 1
            if done % 25 == 0:
                conn.commit()
                print(f"done {done}/{len(files)} {rel}", flush=True)
    conn.commit()
    total = conn.execute("SELECT COUNT(*) FROM docs").fetchone()[0]
    nonempty = conn.execute("SELECT COUNT(*) FROM docs WHERE chars > 20").fetchone()[0]
    print(f"TOTAL {total} NONEMPTY {nonempty}", flush=True)


if __name__ == "__main__":
    main()
