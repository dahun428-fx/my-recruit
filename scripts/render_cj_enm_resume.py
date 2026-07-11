"""DEPRECATED — do not use.

This script renders the résumé by converting Markdown to generic HTML and, when
WeasyPrint is unavailable, falling back to ReportLab. Both paths bypass the
project design system (`DESIGN.md` + the page-structured reference template
`outputs/resume-career-cj-enm.{html,css}`) and produce a flat, inconsistent
document on a different type scale — the exact divergence the resume pipeline is
meant to avoid.

Render résumé/CV artifacts the way `.claude/agents/designer.md` prescribes:
reuse the reference HTML structure + CSS and print to PDF with headless Chrome
(`chrome --headless=new --no-pdf-header-footer --print-to-pdf=<out> <html>`).

This module is kept only for historical reference and is guarded so it cannot
overwrite the corrected artifacts. Remove the guard at your own risk.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_MD = ROOT / "outputs" / "cj-enm-full-resume-draft.md"
OUTPUT_HTML = ROOT / "outputs" / "cj-enm-full-resume-draft.html"
OUTPUT_CSS = ROOT / "outputs" / "cj-enm-full-resume-draft.css"
OUTPUT_PDF = ROOT / "outputs" / "cj-enm-full-resume-draft.pdf"


CSS = r"""@font-face {
  font-family: "Noto Sans KR";
  src: url("file:///C:/Windows/Fonts/NotoSansKR-Regular.ttf") format("truetype");
  font-weight: 400;
}

@font-face {
  font-family: "Noto Sans KR";
  src: url("file:///C:/Windows/Fonts/NotoSansKR-Bold.ttf") format("truetype");
  font-weight: 700 900;
}

:root {
  --background: #ffffff;
  --canvas: #eeeeee;
  --text: #1f1f1f;
  --subtext: #3f4650;
  --muted: #777777;
  --accent: #1f3d55;
  --line: #d7d7d7;
  --line-strong: #1f1f1f;
  --line-soft: #eeeeee;
}

@page {
  size: A4;
  margin: 18mm 19mm 17mm;

  @bottom-left {
    content: "정다훈 이력서 및 경력기술서";
    color: #777777;
    font-family: "Noto Sans KR", "Malgun Gothic", sans-serif;
    font-size: 6.8pt;
    border-top: 1px solid #d7d7d7;
    padding-top: 2.8mm;
    width: 80mm;
    vertical-align: top;
  }

  @bottom-right {
    content: counter(page) " / " counter(pages);
    color: #777777;
    font-family: "Noto Sans KR", "Malgun Gothic", sans-serif;
    font-size: 6.8pt;
    border-top: 1px solid #d7d7d7;
    padding-top: 2.8mm;
    width: 80mm;
    text-align: right;
    vertical-align: top;
  }
}

* {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
}

body {
  background: var(--background);
  color: var(--text);
  font-family: "Noto Sans KR", "Malgun Gothic", sans-serif;
  font-size: 8.6pt;
  line-height: 1.62;
  word-break: keep-all;
}

h1,
h2,
h3,
h4,
p,
ul {
  margin: 0;
}

h1 {
  padding-bottom: 4.8mm;
  border-bottom: 1px solid var(--line-strong);
  font-size: 21pt;
  line-height: 1.24;
  font-weight: 800;
  letter-spacing: 0;
}

.subtitle {
  margin-top: 3.6mm;
  color: var(--accent);
  font-size: 10.6pt;
  line-height: 1.45;
  font-weight: 800;
}

h2 {
  margin-top: 7mm;
  padding-bottom: 2.4mm;
  border-bottom: 1px solid var(--line-soft);
  font-size: 14.5pt;
  line-height: 1.35;
  font-weight: 800;
  letter-spacing: 0;
}

h3 {
  margin-top: 5.8mm;
  color: var(--text);
  font-size: 11.2pt;
  line-height: 1.42;
  font-weight: 800;
}

h4 {
  margin-top: 4.2mm;
  color: var(--accent);
  font-size: 8.9pt;
  line-height: 1.5;
  font-weight: 800;
}

p {
  margin-top: 2.5mm;
  color: var(--subtext);
}

ul {
  margin-top: 2.2mm;
  padding-left: 4.3mm;
}

li {
  margin-top: 0.7mm;
  color: var(--subtext);
}

strong {
  color: var(--text);
  font-weight: 900;
}

hr {
  margin: 6mm 0 0;
  border: 0;
  border-top: 1px solid var(--line);
}

.meta-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.2mm 7mm;
  padding-left: 0;
  list-style: none;
}

.meta-list li {
  margin: 0;
  border-bottom: 1px solid var(--line-soft);
  padding-bottom: 1mm;
  font-size: 8.2pt;
}

.lead-section p {
  font-size: 8.8pt;
  line-height: 1.7;
}

.achievement h3 {
  color: var(--accent);
}

.career-card {
  break-inside: avoid;
}

.project {
  break-inside: avoid;
}

.page-break {
  break-before: page;
}

.avoid-break {
  break-inside: avoid;
}

.tech-line {
  margin-top: 3mm;
  padding-top: 2.6mm;
  border-top: 1px solid var(--line);
  color: var(--subtext);
}

@media screen {
  body {
    max-width: 210mm;
    min-height: 297mm;
    margin: 0 auto;
    padding: 18mm 19mm 17mm;
    background: white;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  }

  html {
    background: var(--canvas);
    padding: 24px 0;
  }
}
"""


def inline_markup(text: str) -> str:
    escaped = html.escape(text)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)


def pdf_markup(text: str) -> str:
    escaped = html.escape(text)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)


def flush_list(out: list[str], items: list[str], class_name: str = "") -> None:
    if not items:
        return
    class_attr = f' class="{class_name}"' if class_name else ""
    out.append(f"<ul{class_attr}>")
    for item in items:
        out.append(f"  <li>{inline_markup(item)}</li>")
    out.append("</ul>")
    items.clear()


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    list_items: list[str] = []
    in_meta = False
    subtitle_pending = False
    section_classes: list[str] = []

    for raw in lines:
        line = raw.rstrip()
        if not line:
            flush_list(out, list_items, "meta-list" if in_meta else "")
            continue

        if line == "---":
            flush_list(out, list_items, "meta-list" if in_meta else "")
            out.append("<hr>")
            continue

        if line.startswith("# "):
            flush_list(out, list_items, "meta-list" if in_meta else "")
            out.append(f"<h1>{inline_markup(line[2:])}</h1>")
            subtitle_pending = True
            continue

        if subtitle_pending and line.startswith("## "):
            flush_list(out, list_items, "meta-list" if in_meta else "")
            out.append(f'<p class="subtitle">{inline_markup(line[3:])}</p>')
            subtitle_pending = False
            continue

        if line.startswith("## "):
            flush_list(out, list_items, "meta-list" if in_meta else "")
            title = line[3:]
            in_meta = title == "인적사항"
            classes = []
            if title in {"기술", "학력 / 교육 / 자격 / 어학", "경력기술서"}:
                classes.append("page-break")
            if title in {"요약"}:
                classes.append("lead-section")
            section_classes = classes
            class_attr = f' class="{" ".join(classes)}"' if classes else ""
            out.append(f"<h2{class_attr}>{inline_markup(title)}</h2>")
            continue

        if line.startswith("### "):
            flush_list(out, list_items, "meta-list" if in_meta else "")
            title = line[4:]
            cls = ""
            if re.match(r"\d+\. ", title):
                cls = ' class="achievement"'
            out.append(f"<h3{cls}>{inline_markup(title)}</h3>")
            continue

        if line.startswith("#### "):
            flush_list(out, list_items, "meta-list" if in_meta else "")
            out.append(f"<h4>{inline_markup(line[5:])}</h4>")
            continue

        if line.startswith("- "):
            list_items.append(line[2:])
            continue

        flush_list(out, list_items, "meta-list" if in_meta else "")

        if line.startswith("**기술:**"):
            out.append(f'<p class="tech-line">{inline_markup(line)}</p>')
        else:
            out.append(f"<p>{inline_markup(line)}</p>")

    flush_list(out, list_items, "meta-list" if in_meta else "")
    body = "\n".join(out)
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>정다훈 이력서 및 경력기술서 - CJ ENM</title>
  <link rel="stylesheet" href="cj-enm-full-resume-draft.css">
</head>
<body>
  <main>
{body}
  </main>
</body>
</html>
"""


def render_pdf_with_reportlab(markdown: str, output_pdf: Path) -> None:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    from reportlab.platypus import HRFlowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer

    regular_font = "NotoSansKR"
    bold_font = "NotoSansKRBold"
    pdfmetrics.registerFont(TTFont(regular_font, r"C:\Windows\Fonts\NotoSansKR-Regular.ttf"))
    pdfmetrics.registerFont(TTFont(bold_font, r"C:\Windows\Fonts\NotoSansKR-Bold.ttf"))

    class NumberedCanvas(canvas.Canvas):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._saved_page_states = []

        def showPage(self):
            self._saved_page_states.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            page_count = len(self._saved_page_states)
            for state in self._saved_page_states:
                self.__dict__.update(state)
                self.draw_footer(page_count)
                super().showPage()
            super().save()

        def draw_footer(self, page_count: int):
            width, _height = A4
            y = 9 * mm
            self.setStrokeColor(colors.HexColor("#d7d7d7"))
            self.setLineWidth(0.4)
            self.line(18 * mm, y + 4.2 * mm, width - 18 * mm, y + 4.2 * mm)
            self.setFillColor(colors.HexColor("#777777"))
            self.setFont(regular_font, 6.8)
            self.drawString(18 * mm, y, "정다훈 이력서 및 경력기술서")
            self.drawRightString(width - 18 * mm, y, f"{self._pageNumber} / {page_count}")

    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=A4,
        leftMargin=19 * mm,
        rightMargin=19 * mm,
        topMargin=18 * mm,
        bottomMargin=17 * mm,
        title="정다훈 이력서 및 경력기술서 - CJ ENM",
        author="정다훈",
    )

    base = getSampleStyleSheet()
    styles = {
        "title": ParagraphStyle(
            "ResumeTitle",
            parent=base["Title"],
            fontName=bold_font,
            fontSize=21,
            leading=26,
            textColor=colors.HexColor("#1f1f1f"),
            spaceAfter=4 * mm,
            alignment=TA_LEFT,
        ),
        "subtitle": ParagraphStyle(
            "ResumeSubtitle",
            parent=base["BodyText"],
            fontName=bold_font,
            fontSize=10.6,
            leading=15,
            textColor=colors.HexColor("#1f3d55"),
            spaceAfter=4 * mm,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName=bold_font,
            fontSize=14.5,
            leading=19,
            textColor=colors.HexColor("#1f1f1f"),
            spaceBefore=5 * mm,
            spaceAfter=2 * mm,
            borderPadding=(0, 0, 2, 0),
            borderColor=colors.HexColor("#eeeeee"),
            borderWidth=0,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "H3",
            parent=base["Heading3"],
            fontName=bold_font,
            fontSize=11.2,
            leading=15.6,
            textColor=colors.HexColor("#1f1f1f"),
            spaceBefore=4 * mm,
            spaceAfter=1.2 * mm,
            keepWithNext=True,
        ),
        "h4": ParagraphStyle(
            "H4",
            parent=base["Heading4"],
            fontName=bold_font,
            fontSize=8.9,
            leading=13,
            textColor=colors.HexColor("#1f3d55"),
            spaceBefore=2.8 * mm,
            spaceAfter=1 * mm,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName=regular_font,
            boldFontName=bold_font,
            fontSize=8.6,
            leading=14.0,
            textColor=colors.HexColor("#3f4650"),
            spaceBefore=1.6 * mm,
            spaceAfter=0,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName=regular_font,
            boldFontName=bold_font,
            fontSize=8.4,
            leading=13.6,
            textColor=colors.HexColor("#3f4650"),
            leftIndent=4 * mm,
            firstLineIndent=-3 * mm,
            spaceBefore=0.8 * mm,
        ),
        "tech": ParagraphStyle(
            "Tech",
            parent=base["BodyText"],
            fontName=regular_font,
            boldFontName=bold_font,
            fontSize=8.2,
            leading=13.2,
            textColor=colors.HexColor("#3f4650"),
            spaceBefore=2.8 * mm,
        ),
    }

    story = []
    subtitle_pending = False

    for raw in markdown.splitlines():
        line = raw.strip()
        if not line:
            continue

        if line == "---":
            story.append(Spacer(1, 2.5 * mm))
            story.append(HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#d7d7d7")))
            continue

        if line.startswith("# "):
            story.append(Paragraph(pdf_markup(line[2:]), styles["title"]))
            story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#1f1f1f")))
            subtitle_pending = True
            continue

        if subtitle_pending and line.startswith("## "):
            story.append(Paragraph(pdf_markup(line[3:]), styles["subtitle"]))
            subtitle_pending = False
            continue

        if line.startswith("## "):
            title = line[3:]
            if title in {"기술", "학력 / 교육 / 자격 / 어학", "경력기술서"}:
                story.append(PageBreak())
            story.append(Paragraph(pdf_markup(title), styles["h2"]))
            story.append(HRFlowable(width="100%", thickness=0.35, color=colors.HexColor("#eeeeee")))
            continue

        if line.startswith("### "):
            story.append(Paragraph(pdf_markup(line[4:]), styles["h3"]))
            continue

        if line.startswith("#### "):
            story.append(Paragraph(pdf_markup(line[5:]), styles["h4"]))
            continue

        if line.startswith("- "):
            story.append(Paragraph("• " + pdf_markup(line[2:]), styles["bullet"]))
            continue

        if line.startswith("**기술:**"):
            story.append(HRFlowable(width="100%", thickness=0.35, color=colors.HexColor("#d7d7d7")))
            story.append(Paragraph(pdf_markup(line), styles["tech"]))
            continue

        story.append(Paragraph(pdf_markup(line), styles["body"]))

    doc.build(story, canvasmaker=NumberedCanvas)


def main() -> None:
    sys.exit(
        "render_cj_enm_resume.py is DEPRECATED and disabled: it would overwrite "
        "the design-system artifacts with a generic Markdown render. Use the "
        "designer process in .claude/agents/designer.md (reuse the reference "
        "template + headless Chrome). To run it anyway, comment out this guard."
    )
    markdown = INPUT_MD.read_text(encoding="utf-8")
    html_text = markdown_to_html(markdown)
    OUTPUT_CSS.write_text(CSS, encoding="utf-8", newline="\n")
    OUTPUT_HTML.write_text(html_text, encoding="utf-8", newline="\n")
    try:
        from weasyprint import HTML

        HTML(filename=str(OUTPUT_HTML)).write_pdf(str(OUTPUT_PDF))
    except Exception as exc:
        print(f"WeasyPrint unavailable, falling back to ReportLab: {type(exc).__name__}: {exc}")
        render_pdf_with_reportlab(markdown, OUTPUT_PDF)
    print(OUTPUT_HTML)
    print(OUTPUT_CSS)
    print(OUTPUT_PDF)


if __name__ == "__main__":
    main()
