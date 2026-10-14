#!/usr/bin/env python3
"""Extractive summaries. See catalog/CONTRACT.md section 3."""
import math
import os
import re
import sqlite3
from collections import Counter

OUT = os.environ.get("SUMMARY_OUT", os.path.join(os.path.dirname(__file__), "content", "summaries"))
ABSTRACT_MAX = 180
SHORT_MAX = 1400
LONG_MAX = 4000
CARD_MAX = 1400
SHORT_BODY = 3000
BINS = 6
STOP = set(
    """
    a an the of and or to for in on with from by as at is are was were be been
    this that these those it its we you they our your their not no yes
    的 了 和 与 及 或 是 在 对 为 以 从 把 被 而 就 也 都 很 更 最 这 那 一个
    我们 你们 他们 可以 进行 通过 以及 其中 如果 但是 因为 所以 没有 不是
    """.split()
)
SKIP_PARTS = ("优才申请资料", "初中报名", "home", "CFD逻辑", "交易记录", "OneDrive备份")
SENSITIVE = ("密码", "证件", "身份证", "通讯录")
TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9_-]{2,}|[\u4e00-\u9fff]{2,}")


def blocked(rel):
    parts = rel.split("/")
    if any(p in SKIP_PARTS for p in parts):
        return True
    return any(tok in parts[-1] for tok in SENSITIVE)


def tokens(text):
    return [t.lower() for t in TOKEN.findall(text) if t.lower() not in STOP]


def informative(text):
    words = tokens(text)
    letters = sum(ch.isalpha() or "\u4e00" <= ch <= "\u9fff" for ch in text)
    digits = sum(ch.isdigit() for ch in text)
    return len(words) >= 3 and letters >= 12 and letters > digits


def sentences_of(text):
    chunks = []
    buf = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            if buf:
                chunks.append(" ".join(buf))
                buf = []
            continue
        buf.append(s)
        if s.endswith(("。", "！", "？", ".", "!", "?")):
            chunks.append(" ".join(buf))
            buf = []
    if buf:
        chunks.append(" ".join(buf))
    out = []
    for chunk in chunks:
        for part in re.split(r"(?<=[。！？.!?])\s+", chunk):
            s = re.sub(r"\s+", " ", part).strip()
            if 12 <= len(s) <= 180 and informative(s):
                out.append(s)
    return out


def headings(text):
    found = []
    for line in text.splitlines():
        raw = line.strip()
        s = raw.lstrip("#").strip()
        if not s or len(s) > 48 or not informative(s):
            continue
        if re.match(r"^(第[0-9一二三四五六七八九十]+[章节部分]|[0-9]+(\.[0-9]+){0,2}\s+\S|[一二三四五六七八九十]+、)", s) or raw.startswith("#"):
            if s not in found:
                found.append(s)
    return found


def luhn_scores(sents):
    df = Counter()
    sent_tokens = [tokens(s) for s in sents]
    for toks in sent_tokens:
        df.update(set(toks))
    n = max(len(sents), 1)
    significant = {t for t, c in df.items() if 1 < c < max(3, int(n * 0.3))}
    scores = []
    for i, toks in enumerate(sent_tokens):
        idx = [j for j, t in enumerate(toks) if t in significant]
        density = 0.0 if len(idx) < 2 else (len(idx) ** 2) / (idx[-1] - idx[0] + 1)
        pos = i / max(n - 1, 1)
        position = 1.3 if pos < 0.12 or pos > 0.88 else 1.0
        scores.append(density * position)
    return scores


def cover(sents, scores):
    if not sents:
        return []
    bins = min(BINS, len(sents))
    width = math.ceil(len(sents) / bins)
    chosen = []
    seen = set()
    for b in range(bins):
        start, end = b * width, min(len(sents), (b + 1) * width)
        if start >= end:
            continue
        best = max(range(start, end), key=lambda i: (scores[i], -i))
        if sents[best] not in seen:
            seen.add(sents[best])
            chosen.append(sents[best])
    return chosen


def clip(text, limit):
    text = text.strip() + "\n"
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…\n"


def card(title, abstract, path, heads, points, limit):
    lines = [f"# {title}", "", abstract, "", f"path: {path}", ""]
    if heads:
        lines.append("## 章节")
        lines.extend(f"- {h}" for h in heads)
        lines.append("")
    if points:
        lines.append("## 覆盖")
        lines.extend(f"- {p}" for p in points)
        lines.append("")
    if not heads and not points:
        lines.append("无可用正文，仅保留路径和文件名。")
        lines.append("")
    return clip("\n".join(lines), limit)


def build_cards(path, body):
    title = os.path.splitext(os.path.basename(path or "未命名"))[0]
    sents = sentences_of(body or "")
    scores = luhn_scores(sents) if sents else []
    heads = headings(body or "")
    if sents:
        opening = sents[: max(1, len(sents) // 3)]
        abstract = max(opening, key=lambda s: scores[sents.index(s)])
    else:
        abstract = f"文件：{title}"
    if len(abstract) > ABSTRACT_MAX:
        abstract = abstract[: ABSTRACT_MAX - 1] + "…"
    points = cover(sents, scores)
    long_doc = len(body or "") >= SHORT_BODY
    if not long_doc or len(heads) <= 12:
        limit = LONG_MAX if long_doc else SHORT_MAX
        return [card(title, abstract, path, heads[:16], points, limit)]
    cards = [card(title, abstract, path, heads, [], CARD_MAX)]
    width = max(1, math.ceil(len(sents) / len(heads))) if heads else len(sents)
    for n, head in enumerate(heads, 1):
        start = min(len(sents), (n - 1) * width)
        end = min(len(sents), n * width)
        chunk = sents[start:end][:4]
        cards.append(card(f"{title} / {head}", head, path, [head], chunk, CARD_MAX))
    return cards


def safe_stem(rel):
    return os.path.splitext(rel.replace("!", "_").replace("\x00", ""))[0]


def write_cards(rel, body):
    written = 0
    for i, text in enumerate(build_cards(rel, body)):
        suffix = ".md" if i == 0 else f".s{i:02d}.md"
        dest = os.path.join(OUT, safe_stem(rel) + suffix)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as handle:
            handle.write(text)
        written += 1
    return written


def from_sqlite(db_path):
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    docs = cards = skipped = 0
    for rel, text, chars in conn.execute("SELECT path, text, chars FROM docs"):
        if blocked(rel):
            skipped += 1
            continue
        cards += write_cards(rel, text or "")
        docs += 1
        if docs % 3000 == 0:
            print(f"sqlite {docs}", flush=True)
    print(f"SQLITE_DOCS {docs} CARDS {cards} SKIPPED {skipped}")


def from_gap(list_path, root):
    docs = cards = skipped = 0
    if not os.path.exists(list_path):
        print("GAP_MISSING")
        return
    # import late so NAS run does not need the extractor
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    from build_content_index import extract
    for line in open(list_path, encoding="utf-8"):
        rel = line.rstrip("\n")
        if not rel or blocked(rel):
            skipped += 1
            continue
        if os.path.exists(os.path.join(OUT, safe_stem(rel) + ".md")):
            continue
        full = os.path.join(root, rel)
        if not os.path.lexists(full):
            skipped += 1
            continue
        flags = getattr(os.lstat(full), "st_flags", 0)
        if flags & 0x40000000:
            skipped += 1
            continue
        text, _method = extract(full)
        cards += write_cards(rel, (text or "")[:120000])
        docs += 1
    print(f"GAP_DOCS {docs} CARDS {cards} SKIPPED {skipped}")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--sqlite")
    parser.add_argument("--gap-list")
    parser.add_argument("--gap-root")
    args = parser.parse_args()
    os.makedirs(OUT, exist_ok=True)
    if args.sqlite:
        from_sqlite(args.sqlite)
    if args.gap_list and args.gap_root:
        from_gap(args.gap_list, args.gap_root)


if __name__ == "__main__":
    main()
