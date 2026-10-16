#!/usr/bin/env python3
"""
Unified Markdown, LaTeX Math, and ASCII-Box-to-Table XHTML Renderer
for Data Center Field Guides (EPUB 3.0 Pipeline).
"""
import html
import re
from pathlib import Path

GREEK_AND_SYMBOLS = {
    r"\Delta": "Δ",
    r"\Omega": "Ω",
    r"\approx": "≈",
    r"\beta": "β",
    r"\cdot": "·",
    r"\equiv": "≡",
    r"\eta": "η",
    r"\forall": "∀",
    r"\ge": "≥",
    r"\geq": "≥",
    r"\implies": "⇒",
    r"\in": "∈",
    r"\int": "∫",
    r"\lambda": "λ",
    r"\le": "≤",
    r"\leq": "≤",
    r"\leftrightarrow": "↔",
    r"\longrightarrow": "⟶",
    r"\to": "→",
    r"\max": "max",
    r"\min": "min",
    r"\mu": "μ",
    r"\nu": "ν",
    r"\pm": "±",
    r"\prec": "≺",
    r"\propto": "∝",
    r"\quad": " &#160;&#160; ",
    r"\qquad": " &#160;&#160;&#160;&#160; ",
    r"\rho": "ρ",
    r"\sigma": "σ",
    r"\sim": "∼",
    r"\sum": "∑",
    r"\tau": "τ",
    r"\times": "×",
    r"\zeta": "ζ",
    r"\alpha": "α",
    r"\gamma": "γ",
    r"\theta": "θ",
    r"\pi": "π",
    r"\infty": "∞",
    r"\neq": "≠",
    r"\ne": "≠",
    r"\partial": "∂",
    r"\lvert": "|",
    r"\rvert": "|",
}


def _extract_braced(s: str, pos: int):
    """Given string s and index pos pointing at '{', return (inner, next_pos)."""
    if pos >= len(s) or s[pos] != "{":
        return None, pos
    depth = 0
    i = pos
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s):
            i += 2
            continue
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return s[pos + 1 : i], i + 1
        i += 1
    return s[pos + 1 :], len(s)


def _render_latex_core(expr: str, is_block: bool = False) -> str:
    s = expr.strip()
    s = re.sub(r"\\begin\{(aligned|cases|array|matrix|pmatrix|bmatrix)\}", "", s)
    s = re.sub(r"\\end\{(aligned|cases|array|matrix|pmatrix|bmatrix)\}", "", s)
    s = s.replace(r"\\", " &#160;;&#160; ")
    s = s.replace("&", " ")
    s = s.replace(r"\_", "_").replace(r"\%", "%")
    s = s.replace(r"\{", "(").replace(r"\}", ")")
    s = s.replace("{,}", ",")
    s = s.replace(r"\,", " ").replace(r"\;", " ").replace(r"\!", "")
    s = s.replace(r"\left\lvert", "|").replace(r"\right\rvert", "|")
    s = s.replace(r"\left\rvert", "|").replace(r"\right\lvert", "|")
    s = re.sub(r"\\left\s*([(\[\|])", r"\1", s)
    s = re.sub(
        r"\\right\s*([)\]\|\.])",
        lambda m: "" if m.group(1) == "." else m.group(1),
        s,
    )
    s = s.replace(r"\left|", "|").replace(r"\right|", "|")

    for k in sorted(GREEK_AND_SYMBOLS.keys(), key=len, reverse=True):
        s = re.sub(re.escape(k) + r"(?![a-zA-Z])", GREEK_AND_SYMBOLS[k], s)

    for _ in range(12):
        changed = False
        for cmd in (r"\text", r"\mathrm", r"\textbf"):
            idx = s.find(cmd + "{")
            while idx != -1:
                inner, nxt = _extract_braced(s, idx + len(cmd))
                if inner is not None:
                    inner_clean = _render_latex_core(inner, is_block=False)
                    if cmd == r"\textbf":
                        inner_clean = f"@@BOPEN@@{inner_clean}@@BCLOSE@@"
                    s = s[:idx] + inner_clean + s[nxt:]
                    changed = True
                    idx = s.find(cmd + "{")
                else:
                    break

        idx = s.find(r"\mathbf{")
        while idx != -1:
            inner, nxt = _extract_braced(s, idx + 7)
            if inner is not None:
                inner_clean = _render_latex_core(inner, is_block=False)
                s = s[:idx] + f"@@BOPEN@@{inner_clean}@@BCLOSE@@" + s[nxt:]
                changed = True
                idx = s.find(r"\mathbf{")
            else:
                break

        for cmd, acc in (
            (r"\dot", "\u0307"),
            (r"\bar", "\u0304"),
            (r"\tilde", "\u0303"),
            (r"\vec", "\u20d7"),
        ):
            idx = s.find(cmd + "{")
            while idx != -1:
                inner, nxt = _extract_braced(s, idx + len(cmd))
                if inner is not None:
                    inner_c = _render_latex_core(inner, is_block=False)
                    s = s[:idx] + inner_c + acc + s[nxt:]
                    changed = True
                    idx = s.find(cmd + "{")
                else:
                    break

        idx = s.find(r"\sqrt{")
        while idx != -1:
            inner, nxt = _extract_braced(s, idx + 5)
            if inner is not None:
                inner_c = _render_latex_core(inner, is_block=False)
                s = s[:idx] + f"√({inner_c})" + s[nxt:]
                changed = True
                idx = s.find(r"\sqrt{")
            else:
                break

        idx = s.find(r"\frac{")
        while idx != -1:
            num, nxt1 = _extract_braced(s, idx + 5)
            if num is not None:
                while nxt1 < len(s) and s[nxt1].isspace():
                    nxt1 += 1
                den, nxt2 = _extract_braced(s, nxt1)
                if den is not None:
                    num_r = _render_latex_core(num, is_block=False)
                    den_r = _render_latex_core(den, is_block=False)
                    if (
                        is_block
                        and "@@FRACOPEN@@" not in num_r
                        and "@@FRACOPEN@@" not in den_r
                    ):
                        repl = (
                            f"@@FRACOPEN@@@@NUMOPEN@@{num_r}@@NUMCLOSE@@"
                            f"@@SLASHOPEN@@/@@SLASHCLOSE@@"
                            f"@@DENOPEN@@{den_r}@@DENCLOSE@@@@FRACCLOSE@@"
                        )
                    else:
                        n_s = f"({num_r})" if ("+" in num_r or " - " in num_r) else num_r
                        d_s = (
                            f"({den_r})"
                            if ("+" in den_r or " - " in den_r or "·" in den_r or "×" in den_r)
                            else den_r
                        )
                        repl = f"{n_s} / {d_s}"
                    s = s[:idx] + repl + s[nxt2:]
                    changed = True
                    idx = s.find(r"\frac{")
                    continue
            break
        if not changed:
            break

    for _ in range(5):
        changed = False
        for sym, tok_o, tok_c in (
            ("_", "@@SUBOPEN@@", "@@SUBCLOSE@@"),
            ("^", "@@SUPOPEN@@", "@@SUPCLOSE@@"),
        ):
            idx = s.find(sym + "{")
            while idx != -1:
                inner, nxt = _extract_braced(s, idx + 1)
                if inner is not None:
                    inner_c = _render_latex_core(inner, is_block=False)
                    s = s[:idx] + f"{tok_o}{inner_c}{tok_c}" + s[nxt:]
                    changed = True
                    idx = s.find(sym + "{")
                else:
                    break
        if not changed:
            break

    s = re.sub(r"_([a-zA-Z0-9])", "@@SUBOPEN@@\\1@@SUBCLOSE@@", s)
    s = re.sub(r"\^([a-zA-Z0-9+-])", "@@SUPOPEN@@\\1@@SUPCLOSE@@", s)
    s = s.replace("{", "").replace("}", "")
    return s


def render_latex_math(expr: str, is_block: bool = False) -> str:
    """Render LaTeX math expression into XML-safe HTML with semantic spans/sub/sup."""
    raw = _render_latex_core(expr, is_block=is_block)
    raw = raw.replace("&#160;", "@@NBSP@@")
    escaped = html.escape(raw)
    tag_map = {
        "@@BOPEN@@": "<strong>",
        "@@BCLOSE@@": "</strong>",
        "@@SUBOPEN@@": "<sub>",
        "@@SUBCLOSE@@": "</sub>",
        "@@SUPOPEN@@": "<sup>",
        "@@SUPCLOSE@@": "</sup>",
        "@@FRACOPEN@@": '<span class="frac">',
        "@@FRACCLOSE@@": "</span>",
        "@@NUMOPEN@@": '<span class="num">',
        "@@NUMCLOSE@@": "</span>",
        "@@SLASHOPEN@@": '<span class="slash">',
        "@@SLASHCLOSE@@": "</span>",
        "@@DENOPEN@@": '<span class="den">',
        "@@DENCLOSE@@": "</span>",
        "@@NBSP@@": "&#160;",
    }
    for k, v in tag_map.items():
        escaped = escaped.replace(k, v)
    return escaped


def inline_format(text: str) -> str:
    """Format inline Markdown and inline LaTeX math into valid XHTML."""
    if not text:
        return ""
    placeholders = []

    def save_ph(html_frag: str) -> str:
        idx = len(placeholders)
        placeholders.append(html_frag)
        return f"@@PH{idx}END@@"

    # 1. Protect inline code `...`
    def repl_code(m):
        code_txt = m.group(1)
        if "\\" in code_txt and ("\\Delta" in code_txt or "\\frac" in code_txt or "\\dot" in code_txt):
            return save_ph(f"<code>{render_latex_math(code_txt.strip('$'), is_block=False)}</code>")
        return save_ph(f"<code>{html.escape(code_txt)}</code>")

    s = re.sub(r"`([^`]+)`", repl_code, text)

    # 2. Protect inline block math $$...$$ inside a paragraph or blockquote
    def repl_disp_math(m):
        return save_ph(f'<span class="math-inline">{render_latex_math(m.group(1), is_block=False)}</span>')

    s = re.sub(r"\$\$(.+?)\$\$", repl_disp_math, s, flags=re.S)

    # 3. Protect inline math $...$
    def repl_inl_math(m):
        inner = m.group(1)
        return save_ph(f'<span class="math-inline">{render_latex_math(inner, is_block=False)}</span>')

    s = re.sub(r"(?<!\$)\$(?!\$)([^\$\n]+?)(?<!\$)\$(?!\$)", repl_inl_math, s)

    # 4. Clean any stray un-delimited LaTeX commands in prose (e.g. \Delta T, \text{K})
    if "\\" in s:
        s = re.sub(r"\\text\{([^{}]+)\}", r"\1", s)
        s = re.sub(r"\\mathrm\{([^{}]+)\}", r"\1", s)
        s = s.replace(r"\,", " ").replace(r"\;", " ")
        for k in sorted(GREEK_AND_SYMBOLS.keys(), key=len, reverse=True):
            s = re.sub(re.escape(k) + r"(?![a-zA-Z])", GREEK_AND_SYMBOLS[k].replace("&#160;", " "), s)
        for cmd, acc in ((r"\dot", "\u0307"), (r"\bar", "\u0304")):
            s = re.sub(re.escape(cmd) + r"\{([^{}]+)\}", lambda m: m.group(1) + acc, s)

    # 5. HTML escape remaining text
    safe = html.escape(s)

    # 6. Format bold, italic, links, and explicit <br/> tags from table parser
    safe = safe.replace("&lt;br/&gt;", "<br/>")
    safe = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", safe)
    safe = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", safe)
    safe = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', safe)

    # 7. Restore placeholders
    for idx, frag in enumerate(placeholders):
        safe = safe.replace(f"@@PH{idx}END@@", frag)

    return safe


def _clean_callout_line(line: str) -> str:
    s = line.strip()
    if s in ("|", "v", "V", "^"):
        return "↓"
    if re.match(r"^\|\s+v$", s):
        return "↓"
    s = re.sub(r"^\+--->\s*", "↳ ", s)
    s = re.sub(r"^\|\s*\+--->\s*", "↳ ", s)
    s = re.sub(r"^\|\s*\+---x\s*", "✕ ", s)
    s = re.sub(r"^\+---x\s*", "✕ ", s)
    s = re.sub(r"^\|\s+", "", s)
    s = s.replace("--->", "→").replace("-->", "→")
    s = re.sub(r"\+[-=\s]{3,}\+?", "", s)
    s = re.sub(r"^\|+|\|+$", "", s)
    return s.strip()


def parse_ascii_block(code: str):
    """
    Detect and parse ASCII box-drawing tables/callouts into structured semantic data:
      - ("grid_table", title, rows)
      - ("dashed_table", title, rows)
      - ("callout_box", title, lines)
    Returns None if `code` is regular source code / JSON / script.
    """
    lines = [l.rstrip() for l in code.strip().splitlines() if l.strip()]
    if not lines or not (
        lines[0].lstrip().startswith("+---") or lines[0].lstrip().startswith("+===")
    ):
        return None

    sep_re = re.compile(r"^\+[-\=+]+\+$")
    seps = [l.strip() for l in lines if sep_re.match(l.strip())]
    max_cols = max((s.count("+") - 1 for s in seps), default=1)

    if max_cols >= 2:
        sections = []
        cur = []
        for l in lines:
            s = l.strip()
            if sep_re.match(s):
                if cur:
                    sections.append(cur)
                    cur = []
            elif s.startswith("|") and s.endswith("|"):
                cur.append([c.strip() for c in s[1:-1].split("|")])
        if cur:
            sections.append(cur)

        title = None
        rows = []
        for sec in sections:
            if len(sec) == 1 and len(sec[0]) == 1 and not title and not rows:
                title = sec[0][0]
                continue
            if len(sec) > 1 and all(len(r) == max_cols for r in sec):
                merged_rows = []
                for r in sec:
                    if not merged_rows:
                        merged_rows.append(list(r))
                    elif r[0] == "" or (
                        len(sec) <= 5
                        and not re.match(r"^(\d+[\.\)]?|[A-Z0-9]{2,4}\b|•)", r[0])
                    ):
                        for idx, val in enumerate(r):
                            if val:
                                sep_str = "<br/>" if val.startswith("•") else " "
                                merged_rows[-1][idx] = (
                                    merged_rows[-1][idx] + sep_str + val
                                ).strip()
                    else:
                        merged_rows.append(list(r))
                rows.extend(merged_rows)
            else:
                merged = [""] * max_cols
                for r in sec:
                    for idx in range(min(len(r), max_cols)):
                        if r[idx]:
                            sep_str = "<br/>" if r[idx].startswith("•") else " "
                            merged[idx] = (merged[idx] + sep_str + r[idx]).strip()
                rows.append(merged)
        return ("grid_table", title, rows)

    # Single-column outer box
    inner = []
    for l in lines:
        s = l.strip()
        if sep_re.match(s):
            continue
        if s.startswith("|") and s.endswith("|"):
            inner.append(s[1:-1])
        else:
            inner.append(s)
    while inner and not inner[0].strip():
        inner.pop(0)
    while inner and not inner[-1].strip():
        inner.pop()
    if not inner:
        return None
    title = inner[0].strip()
    body = inner[1:]
    while body and not body[0].strip():
        body.pop(0)

    # Check for dashed column underline row
    dash_idx = -1
    for idx, b in enumerate(body):
        if re.match(r"^\s*-{3,}(\s+-{3,})+\s*$", b):
            dash_idx = idx
            break
    if dash_idx >= 1:
        dash_line = body[dash_idx]
        spans = [m.span() for m in re.finditer(r"-+", dash_line)]

        def slice_row(r_str):
            cols = []
            for i_s, (st, _en) in enumerate(spans):
                end_pos = spans[i_s + 1][0] if i_s + 1 < len(spans) else len(r_str)
                cols.append(r_str[st:end_pos].strip())
            return cols

        header = slice_row(body[dash_idx - 1])
        data_rows = [slice_row(b) for b in body[dash_idx + 1 :] if b.strip()]
        return ("dashed_table", title, [header] + data_rows)

    cleaned_lines = []
    for b in body:
        if re.match(r"^[\s\=\-]{10,}$", b):
            continue
        c = _clean_callout_line(b)
        if c:
            cleaned_lines.append(c)
    return ("callout_box", title, cleaned_lines)


def render_ascii_table_xhtml(parsed) -> str:
    kind, title, data = parsed
    if kind in ("grid_table", "dashed_table"):
        if not data:
            return ""
        ncols = max((len(r) for r in data), default=1)
        thead_parts = []
        if title:
            thead_parts.append(
                f'<tr><th colspan="{ncols}" class="table-banner">{inline_format(title)}</th></tr>'
            )
        # Check if first row looks like a column header row (when dashed_table or grid_table has >1 rows)
        start_idx = 0
        if kind == "dashed_table" or (len(data) >= 2 and all(len(c) < 45 for c in data[0])):
            th_cells = "".join(f"<th>{inline_format(c)}</th>" for c in data[0])
            thead_parts.append(f"<tr>{th_cells}</tr>")
            start_idx = 1
        thead_html = f"<thead>{''.join(thead_parts)}</thead>" if thead_parts else ""
        tbody_rows = []
        for r in data[start_idx:]:
            padded = list(r) + [""] * (ncols - len(r))
            tds = "".join(f"<td>{inline_format(c)}</td>" for c in padded[:ncols])
            tbody_rows.append(f"<tr>{tds}</tr>")
        return f'<table>{thead_html}<tbody>{"".join(tbody_rows)}</tbody></table>'

    # callout_box -> render as structured 1- or 2-column callout table
    rows_html = []
    for line in data:
        if "→" in line and not line.startswith("↳"):
            left, right = line.split("→", 1)
            rows_html.append(
                f'<tr><td class="callout-key">{inline_format(left.strip())}</td>'
                f"<td>{inline_format(right.strip())}</td></tr>"
            )
        else:
            rows_html.append(f'<tr><td colspan="2">{inline_format(line)}</td></tr>')
    thead = (
        f'<thead><tr><th colspan="2" class="table-banner">{inline_format(title)}</th></tr></thead>'
        if title
        else ""
    )
    return f'<table class="callout-table">{thead}<tbody>{"".join(rows_html)}</tbody></table>'


def md_to_blocks(text: str, base_dir=None):
    if base_dir is None:
        base_dir = Path(".")
    else:
        base_dir = Path(base_dir)

    lines = text.replace("\r\n", "\n").split("\n")
    blocks = []
    buf = []
    list_buf = []
    list_kind = "ul"
    table = []
    code_buf = []
    math_buf = []
    in_code = False
    in_math = False

    def flush_p():
        if buf:
            blocks.append(("p", " ".join(buf).strip()))
            buf.clear()

    def flush_list():
        if list_buf:
            blocks.append((list_kind, list(list_buf)))
            list_buf.clear()

    def flush_table():
        if table:
            rows = []
            for raw in table:
                safe_raw = re.sub(
                    r"\$([^\$]+)\$",
                    lambda m: "$" + m.group(1).replace("|", r"\lvert ") + "$",
                    raw.strip().strip("|"),
                )
                cells = [c.strip() for c in safe_raw.split("|")]
                if cells and not all(set(c) <= set("-: ") for c in cells):
                    rows.append(cells)
            if rows:
                blocks.append(("table", rows))
            table.clear()

    def flush_code():
        if code_buf:
            raw_code = "\n".join(code_buf)
            parsed = parse_ascii_block(raw_code)
            if parsed is not None:
                blocks.append(("ascii_table", parsed))
            else:
                blocks.append(("pre", raw_code))
            code_buf.clear()

    def flush_math():
        if math_buf:
            blocks.append(("math_block", " ".join(math_buf).strip()))
            math_buf.clear()

    img_re = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_p()
            flush_list()
            flush_table()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_buf.append(line)
            continue

        # Multi-line or single-line display math $$...$$
        if stripped.startswith("$$") and (stripped.count("$$") == 1 or (stripped.endswith("$$") and stripped.count("$$") == 2)):
            flush_p()
            flush_list()
            flush_table()
            if in_math:
                inner = stripped[:-2].strip() if stripped.endswith("$$") and len(stripped) > 2 else stripped[2:].strip()
                if inner:
                    math_buf.append(inner)
                flush_math()
                in_math = False
            else:
                if stripped.endswith("$$") and len(stripped) > 4:
                    blocks.append(("math_block", stripped[2:-2].strip()))
                else:
                    in_math = True
                    rem = stripped[2:].strip()
                    if rem:
                        math_buf.append(rem)
            continue

        if in_math:
            if stripped.endswith("$$"):
                rem = stripped[:-2].strip()
                if rem:
                    math_buf.append(rem)
                flush_math()
                in_math = False
            else:
                math_buf.append(stripped)
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_p()
            flush_list()
            table.append(stripped)
            continue
        else:
            flush_table()

        if stripped.startswith("# "):
            flush_p()
            flush_list()
            blocks.append(("h1", stripped[2:].strip()))
        elif stripped.startswith("## "):
            flush_p()
            flush_list()
            blocks.append(("h2", stripped[3:].strip()))
        elif stripped.startswith("### "):
            flush_p()
            flush_list()
            blocks.append(("h3", stripped[4:].strip()))
        elif stripped.startswith("#### "):
            flush_p()
            flush_list()
            blocks.append(("h3", stripped[5:].strip()))
        elif stripped.startswith("> "):
            flush_p()
            flush_list()
            blocks.append(("blockquote", stripped[2:].strip()))
        elif stripped.startswith("- ") or stripped.startswith("* "):
            flush_p()
            if list_buf and list_kind != "ul":
                flush_list()
            list_kind = "ul"
            list_buf.append(stripped[2:].strip())
        elif re.match(r"^\d+\.\s+", stripped):
            flush_p()
            if list_buf and list_kind != "ol":
                flush_list()
            list_kind = "ol"
            list_buf.append(re.sub(r"^\d+\.\s+", "", stripped))
        elif img_re.search(stripped):
            flush_p()
            flush_list()
            m = img_re.search(stripped)
            alt, src = m.group(1), m.group(2)
            path = (base_dir / src).resolve()
            blocks.append(("img", (alt or path.stem, path.name, path)))
        elif stripped == "" or stripped == "---":
            flush_p()
            flush_list()
        else:
            flush_list()
            buf.append(stripped)

    flush_p()
    flush_list()
    flush_table()
    flush_code()
    flush_math()
    return blocks


def fig_html(src: str, caption: str) -> str:
    return (
        f'<figure><img src="images/{html.escape(src)}" alt="{html.escape(caption)}"/>'
        f"<figcaption>{inline_format(caption)}</figcaption></figure>"
    )


def blocks_to_xhtml(blocks, extra_or_figures=None, seen_images=None):
    """
    Convert parsed blocks into XHTML.
    - If `extra_or_figures` is a `dict` (Mode A: Books 01 & 02), injects `extra_or_figures[heading_key]`
      after matching headings and returns `xhtml_str`.
    - Otherwise (Mode B: Books 03-09 & build_lang_epubs.py), `extra_or_figures` is an optional list of
      `(src, caption)` tuples; returns `(xhtml_str, found_images)`.
    """
    mode_a = isinstance(extra_or_figures, dict)
    figures_dict = extra_or_figures if mode_a else {}
    extra_figures = extra_or_figures if (not mode_a and extra_or_figures) else []

    parts = []
    found_images = []
    inserted = set()
    inserted_extra = False
    if seen_images is None:
        seen_images = set()

    for kind, data in blocks:
        check_text = None
        if kind == "h1":
            parts.append(f"<h1>{inline_format(data)}</h1>")
            check_text = data
        elif kind == "h2":
            parts.append(f"<h2>{inline_format(data)}</h2>")
            check_text = data
            if not mode_a and not inserted_extra and extra_figures:
                for src, cap in extra_figures:
                    if src not in seen_images:
                        parts.append(fig_html(src, cap))
                        seen_images.add(src)
                inserted_extra = True
        elif kind == "h3":
            parts.append(f"<h3>{inline_format(data)}</h3>")
            check_text = data
        elif kind == "p":
            parts.append(f"<p>{inline_format(data)}</p>")
        elif kind == "blockquote":
            parts.append(f"<blockquote><p>{inline_format(data)}</p></blockquote>")
        elif kind == "pre":
            parts.append(f"<pre><code>{html.escape(data)}</code></pre>")
        elif kind == "math_block":
            parts.append(f'<div class="math-block">{render_latex_math(data, is_block=True)}</div>')
        elif kind == "ascii_table":
            parts.append(render_ascii_table_xhtml(data))
        elif kind in ("ul", "ol"):
            items = "".join(f"<li>{inline_format(item)}</li>" for item in data)
            parts.append(f"<{kind}>{items}</{kind}>")
        elif kind == "img":
            if len(data) == 3:
                alt, name, path = data
            else:
                alt, path = data
                name = path.name
            if name not in seen_images:
                seen_images.add(name)
                found_images.append((name, path))
                parts.append(fig_html(name, alt))
        elif kind == "table":
            header = data[0]
            rows = data[1:]
            th = "".join(f"<th>{inline_format(c)}</th>" for c in header)
            tr = "".join(
                "<tr>" + "".join(f"<td>{inline_format(c)}</td>" for c in r) + "</tr>"
                for r in rows
            )
            parts.append(f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>")

        if mode_a and check_text:
            for key, fig in figures_dict.items():
                if fig and key in check_text and key not in inserted:
                    parts.append(fig)
                    inserted.add(key)

    if not mode_a and not inserted_extra and extra_figures:
        for src, cap in extra_figures:
            if src not in seen_images:
                parts.append(fig_html(src, cap))
                seen_images.add(src)

    xhtml_out = "\n".join(parts)
    if mode_a:
        return xhtml_out
    return xhtml_out, found_images


SHARED_CSS = """
@font-face { font-family: "DejaVu Sans"; src: url("fonts/DejaVuSans.ttf"); }
@font-face { font-family: "DejaVu Sans"; src: url("fonts/DejaVuSans-Bold.ttf"); font-weight: bold; }
body {
    font-family: "DejaVu Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.55;
    margin: 1.2em 7%;
    color: #0f172a;
    background-color: #ffffff;
}
h1 {
    font-weight: bold;
    font-size: 1.6em;
    line-height: 1.25;
    margin-top: 1.0em;
    margin-bottom: 0.6em;
    color: #0052cc;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 0.25em;
}
h2 {
    font-weight: bold;
    font-size: 1.22em;
    margin-top: 1.5em;
    margin-bottom: 0.45em;
    color: #0f172a;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 0.15em;
}
h3 {
    font-weight: bold;
    font-size: 1.05em;
    margin-top: 1.2em;
    margin-bottom: 0.35em;
    color: #1e3a8a;
}
p {
    margin: 0.7em 0;
}
ul, ol {
    margin: 0.6em 0 0.8em 1.4em;
    padding-left: 0;
}
li {
    margin: 0.35em 0;
}
blockquote {
    border-left: 4px solid #0052cc;
    margin: 1em 0;
    padding: 0.55em 1em;
    background: #f8fafc;
    color: #334155;
}
pre {
    background: #0f172a;
    color: #f8fafc;
    padding: 0.8em 1em;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 0.85em;
    line-height: 1.4;
    margin: 1em 0;
}
code {
    font-family: "Courier New", Courier, monospace;
    font-size: 0.9em;
    background: #f1f5f9;
    padding: 0.1em 0.3em;
    border-radius: 3px;
}
pre code {
    background: transparent;
    padding: 0;
}
.math-block {
    margin: 1.1em 0;
    padding: 0.75em 1em;
    background: #f8fafc;
    border-left: 3px solid #0284c7;
    border-radius: 4px;
    font-family: "DejaVu Sans", sans-serif;
    font-size: 0.96em;
    color: #0f172a;
    overflow-x: auto;
}
.math-inline {
    font-family: "DejaVu Sans", sans-serif;
    white-space: nowrap;
}
.frac {
    display: inline-block;
    vertical-align: middle;
    text-align: center;
}
.frac > .num {
    display: block;
    border-bottom: 1px solid #334155;
    padding: 0 0.3em;
}
.frac > .slash {
    display: none;
}
.frac > .den {
    display: block;
    padding: 0 0.3em;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.2em 0;
    font-size: 0.88em;
    page-break-inside: auto;
}
th, td {
    border: 1px solid #cbd5e1;
    padding: 0.48em 0.65em;
    text-align: left;
    vertical-align: top;
}
th {
    background: #0f172a;
    color: #ffffff;
    font-weight: bold;
}
th.table-banner {
    background: #0052cc;
    color: #ffffff;
    text-align: left;
    font-size: 0.95em;
    letter-spacing: 0.02em;
}
tr:nth-child(even) td {
    background-color: #f8fafc;
}
table.callout-table td.callout-key {
    font-weight: bold;
    width: 34%;
    color: #0f172a;
    background-color: #f1f5f9;
}
figure {
    margin: 1.6em 0;
    page-break-inside: avoid;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 0.65em;
    text-align: center;
}
img {
    width: 100%;
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
}
figcaption {
    font-size: 0.86em;
    line-height: 1.4;
    margin-top: 0.55em;
    color: #0052cc;
    font-weight: bold;
    text-align: left;
}
nav ol {
    line-height: 1.65;
}
"""
