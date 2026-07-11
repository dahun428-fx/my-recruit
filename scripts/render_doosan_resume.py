"""Render the Doosan Robotics resume PDF from the page-structured HTML.

The résumé is a hand-authored, page-structured document
(``outputs/doosan-robotics-full-resume.html`` + ``.css``) that reuses the
canonical DESIGN.md template — fixed A4 ``.page`` boxes, profile photo,
per-page footers with ``n / 9`` numbers, skill blocks and 경력기술서 project
blocks — matching ``millie-full-resume.html``.

This script does NOT generate the HTML (that would clobber the authored
layout); it only prints the existing HTML to PDF with headless Chrome
``--print-to-pdf``, the renderer DESIGN.md / .claude/agents/designer.md
mandate. Edit the HTML/CSS by hand, then re-run this to refresh the PDF.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_HTML = ROOT / "outputs" / "doosan-robotics-full-resume.html"
OUTPUT_PDF = ROOT / "outputs" / "doosan-robotics-full-resume.pdf"

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_chrome() -> str:
    for path in CHROME_CANDIDATES:
        if Path(path).exists():
            return path
    raise SystemExit("No Chrome/Edge binary found for --print-to-pdf rendering.")


def render_pdf(html_path: Path, pdf_path: Path) -> None:
    chrome = find_chrome()
    with tempfile.TemporaryDirectory(prefix="doosan-chrome-") as user_dir:
        cmd = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-first-run",
            "--disable-extensions",
            f"--user-data-dir={user_dir}",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=10000",
            f"--print-to-pdf={pdf_path.resolve()}",
            html_path.resolve().as_uri(),
        ]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        if not pdf_path.exists():
            sys.stderr.write((result.stdout or "") + "\n" + (result.stderr or "") + "\n")
            raise SystemExit(f"Chrome print-to-pdf failed (exit {result.returncode}).")


def main() -> None:
    if not INPUT_HTML.exists():
        raise SystemExit(f"Missing input HTML: {INPUT_HTML}")
    render_pdf(INPUT_HTML, OUTPUT_PDF)
    size_kb = OUTPUT_PDF.stat().st_size / 1024
    print(f"HTML: {INPUT_HTML}")
    print(f"PDF:  {OUTPUT_PDF} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
