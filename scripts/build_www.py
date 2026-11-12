#!/usr/bin/env python3
"""Copy the DailyPdfLife website into www/ for the Android app.

  python3 scripts/build_www.py <path-to-website-folder>

- big libraries are served from the app itself (works offline, opens faster)
- website ads are removed (AdSense is not allowed inside apps)
- app-shell.js is added to every page (saving, sharing, printing, scanner)
"""
import os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, "site")
WWW = os.path.join(ROOT, "www")
VENDOR = os.path.join(ROOT, "web-extra", "vendor")

LOCAL = {
    "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js": "vendor/pdf.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js": "vendor/pdf.worker.min.js",
    "https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js": "vendor/pdf-lib.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js": "vendor/qrcode.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js": "vendor/xlsx.full.min.js",
    "https://cdn.jsdelivr.net/npm/mammoth@1.13.0/mammoth.browser.min.js": "vendor/mammoth.browser.min.js",
    "https://cdn.jsdelivr.net/npm/heic2any@0.0.4/dist/heic2any.min.js": "vendor/heic2any.min.js",
    "https://cdn.jsdelivr.net/npm/@neslinesli93/qpdf-wasm@0.3.1/dist/": "vendor/qpdf/",
}
ADS = re.compile(r'\s*<script async src="https://pagead2\.googlesyndication\.com[^>]*>\s*</script>', re.S)
SKIP = {"ads.txt", "ads.js", "robots.txt", "sitemap.xml"}

if os.path.exists(WWW):
    shutil.rmtree(WWW)
os.makedirs(WWW)
for f in os.listdir(SITE):
    src = os.path.join(SITE, f)
    if os.path.isdir(src) or f in SKIP or f.lower().startswith("readme"):
        continue
    shutil.copy2(src, os.path.join(WWW, f))
shutil.copytree(VENDOR, os.path.join(WWW, "vendor"))
shutil.copy2(os.path.join(ROOT, "web-extra", "app-shell.js"), os.path.join(WWW, "app-shell.js"))

pages = 0
for f in os.listdir(WWW):
    if not f.endswith((".html", ".js")):
        continue
    p = os.path.join(WWW, f)
    s = open(p, encoding="utf-8").read()
    o = s
    for k, v in LOCAL.items():
        s = s.replace(k, v)
    if f.endswith(".html"):
        s = ADS.sub("", s)
        if "app-shell.js" not in s:
            s = s.replace('<script src="lang.js"></script>', '<script src="lang.js"></script>\n<script src="app-shell.js"></script>', 1)
        pages += 1
    if s != o:
        open(p, "w", encoding="utf-8").write(s)
left = [f for f in os.listdir(WWW) if f.endswith(".html") and "googlesyndication" in open(os.path.join(WWW, f), encoding="utf-8").read()]
print(f"www ready: {pages} pages, ads left in: {left or 'none'}")
