#!/usr/bin/env python3
"""Generate <slug>.html from template.html and add it to index.html.

Usage:
    python make_page.py <slug> <package> "<App name KO>" "<App name EN>" <support-email> [YYYY-MM-DD]
Example:
    python make_page.py wage-calc kr.starmade.wagecalc "알바 시급 계산기" "Wage Calculator" support@example.com 2026-11-13
"""
import datetime
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    if len(sys.argv) not in (6, 7):
        print(__doc__)
        sys.exit(1)
    slug, package, name_ko, name_en, email = sys.argv[1:6]
    date = sys.argv[6] if len(sys.argv) == 7 else datetime.date.today().isoformat()

    html = (HERE / "template.html").read_text(encoding="utf-8")
    for key, value in {
        "[[APP_NAME_KO]]": name_ko,
        "[[APP_NAME_EN]]": name_en,
        "[[PACKAGE]]": package,
        "[[DATE]]": date,
        "[[SUPPORT_EMAIL]]": email,
    }.items():
        html = html.replace(key, value)
    out = HERE / f"{slug}.html"
    out.write_text(html, encoding="utf-8")

    index = HERE / "index.html"
    text = index.read_text(encoding="utf-8")
    entry = f'  <li><a href="{slug}.html">{name_ko} / {name_en}</a> <span class="meta">({package})</span></li>\n'
    if f'href="{slug}.html"' not in text:
        text = re.sub(r"(<ul id=\"apps\">\n)", r"\1" + entry.replace("\\", "\\\\"), text, count=1)
        index.write_text(text, encoding="utf-8")
    print(f"wrote {out.name}; URL: https://dybarogo.github.io/appstore-privacy/{slug}.html")


if __name__ == "__main__":
    main()
