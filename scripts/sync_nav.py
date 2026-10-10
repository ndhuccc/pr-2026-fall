# -*- coding: utf-8 -*-
"""Inject a `nav:` block into mkdocs.yml, ordered by schedule.md.

Why: MkDocs sorts pages by file path when no `nav` is given, which puts
`lec02-bayesian-inference.md` before `lec02.md`. The order we want is the order the
materials are listed in `schedule.md` (week, then the order the teacher entered them).

The function is idempotent: it replaces everything from the first `nav:` line to the end of that
block, and leaves the rest of mkdocs.yml untouched.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MK = ROOT / "mkdocs.yml"
NAV_START = "# --- nav(由 build_docs.py 依 schedule.md 產生,請勿手改)---\n"
NAV_END = "# --- nav 結束 ---\n"

# 側邊導覽的固定骨架:標題 -> 檔案或資料夾的 README
FIXED_HEAD = [("首頁 Home", "index.md"), ("課程大綱 Syllabus", "syllabus.md"), ("週次進度表 Schedule", "schedule.md")]
FIXED_TAIL = [
    ("作業 Assignments", "assignments/README.md"),
    ("專題 Projects", "projects/README.md"),
    ("考試與測驗 Exams & Quizzes", "exams/README.md"),
    ("實驗 Labs", "labs/README.md"),
    ("Notebook", "notebooks/README.md"),
    ("投影片下載 Slides", "slides/README.md"),
    ("參考資料 References", "references/README.md"),
    ("自學指引 Study Guide", "study-guide/README.md"),
    ("常見問題 FAQ", "FAQ.md"),
    ("術語表 Glossary", "glossary.md"),
    ("異動紀錄 Changelog", "CHANGELOG.md"),
    ("貢獻指南 Contributing", "CONTRIBUTING.md"),
    ("授權 License", "LICENSE.md"),
]


def lecture_order() -> list[tuple[str, str, str]]:
    """(週次, 標題, 路徑) for every lecture, in the order schedule.md lists them."""
    text = (ROOT / "schedule.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*([0-9/]+)\s*\|([^|]*)\|([^|]*)\|", text, re.M)
    order: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for week, _date, _topic, lec_cell in rows:
        for label, href in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", lec_cell):
            m = re.match(r"^lectures/(lec[0-9A-Za-z._-]*)\.md$", href.strip())
            if not m:
                continue
            slug = m.group(1)
            if slug in seen:
                continue
            seen.add(slug)
            order.append((week, label, f"lectures/{slug}.md"))
    # any lecture not listed in schedule.md is appended, so nothing disappears from the site
    lectures_dir = ROOT / "lectures"
    if lectures_dir.is_dir():
        for p in sorted(lectures_dir.glob("lec*.md")):
            if p.name != "README.md" and p.stem not in seen:
                seen.add(p.stem)
                order.append(("", p.stem, f"lectures/{p.name}"))
    return order


def render_nav() -> str:
    lines = ["nav:", *[f"  - {t}: {p}" for t, p in FIXED_HEAD]]
    lectures = lecture_order()
    if lectures:
        lines.append("  - 講義 Lectures:")
        groups: dict[str, list[tuple[str, str]]] = {}
        for week, t, p in lectures:
            groups.setdefault(week, []).append((t, p))
        for week, items in groups.items():
            lines.append(f"      - 第 {week} 週 Week {week}:" if week else "      - 其他 Others:")
            lines += [f"          - {t}: {p}" for t, p in items]
    lines += [f"  - {t}: {p}" for t, p in FIXED_TAIL]
    return NAV_START + "\n".join(lines) + "\n" + NAV_END


def main() -> int:
    text = MK.read_text(encoding="utf-8")
    block = render_nav()
    if NAV_START in text and NAV_END in text:
        start = text.index(NAV_START)
        end = text.index(NAV_END, start) + len(NAV_END)
        new = text[:start] + block + text[end:]
    else:
        new = text.rstrip("\n") + "\n\n" + block
    if new != text:
        MK.write_text(new, encoding="utf-8")
        print("mkdocs.yml nav updated")
    else:
        print("mkdocs.yml nav already up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
