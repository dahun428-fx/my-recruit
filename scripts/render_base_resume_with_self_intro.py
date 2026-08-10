"""Render base-resume-with-self-intro.html (이력서 9p + 자기소개서 3p) to PDF
via headless Chrome --print-to-pdf. Edit the HTML/CSS by hand, then re-run to
refresh outputs/base-resume-with-self-intro.pdf.
"""
from __future__ import annotations
import subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_HTML = ROOT / "outputs" / "base-resume-with-self-intro.html"
OUTPUT_PDF = ROOT / "outputs" / "base-resume-with-self-intro.pdf"
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
    raise SystemExit("No Chrome/Edge binary found.")

def render_pdf(html_path: Path, pdf_path: Path) -> None:
    chrome = find_chrome()
    with tempfile.TemporaryDirectory(prefix="base-si-chrome-") as user_dir:
        cmd = [chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
            "--no-first-run", "--disable-extensions", f"--user-data-dir={user_dir}",
            "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=10000", f"--print-to-pdf={pdf_path.resolve()}",
            html_path.resolve().as_uri()]
        result = subprocess.run(cmd, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=120)
        if not pdf_path.exists():
            sys.stderr.write((result.stdout or "") + "\n" + (result.stderr or "") + "\n")
            raise SystemExit(f"Chrome print-to-pdf failed (exit {result.returncode}).")

def main() -> None:
    if not INPUT_HTML.exists():
        raise SystemExit(f"Missing input HTML: {INPUT_HTML}")
    render_pdf(INPUT_HTML, OUTPUT_PDF)
    print(f"PDF: {OUTPUT_PDF} ({OUTPUT_PDF.stat().st_size/1024:.0f} KB)")

if __name__ == "__main__":
    main()
