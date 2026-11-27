"""Wrap each tool fragment in scripts/newtools/src/<slug>.html into a full site page.
Fragment first line: <!-- libs: pdfjs pdflib jszip adhan -->  (any subset, or none)
Run: python3 scripts/newtools/make.py site"""
import os, re, sys
SRC = os.path.join(os.path.dirname(__file__), "src")
SITE = sys.argv[1]
LIBS = {
  "pdfjs": '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>\n'
           '<script>pdfjsLib.GlobalWorkerOptions.workerSrc="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";</script>',
  "pdflib": '<script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>',
  "jszip": '<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>',
  "adhan": '<script src="https://cdn.jsdelivr.net/npm/adhan@4.4.3/lib/bundles/adhan.umd.min.js"></script>',
}
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#ffffff">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="DailyPdfLife">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<title>{slug}</title>
<link rel="stylesheet" href="app.css">
<script src="lang.js"></script>
<script src="result.js"></script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3528972294042151"
     crossorigin="anonymous"></script>
{libs}
"""
for f in sorted(os.listdir(SRC)):
    if not f.endswith(".html"): continue
    slug = f[:-5]
    t = open(os.path.join(SRC, f), encoding="utf-8").read()
    m = re.match(r"<!--\s*libs:([^>]*)-->\n", t)
    libs = m.group(1).split() if m else []
    if m: t = t[m.end():]
    style = ""
    sm = re.match(r"\s*(<style>.*?</style>)\n", t, re.S)
    if sm: style, t = sm.group(1), t[sm.end():]
    # body = markup up to the first <script>, page script = rest
    i = t.find("<script>")
    body, script = (t[:i], t[i:]) if i >= 0 else (t, "")
    page = (HEAD.format(slug=slug, libs="\n".join(LIBS[l] for l in libs)) + style + "\n</head>\n<body>\n"
            + body.strip() + "\n\n" + script.strip() + "\n"
            + '<script src="nav.js"></script>\n<script src="install.js"></script>\n</body>\n</html>\n')
    # page script must run after nav.js? no: nav.js only wraps markup; keep page script before nav like other pages
    open(os.path.join(SITE, f), "w", encoding="utf-8").write(page)
    print("built", f)
