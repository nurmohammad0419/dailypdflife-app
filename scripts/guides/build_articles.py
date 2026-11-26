"""Build guide article pages and guides.html into the site folder.
Run: python3 scripts/guides/build_articles.py site"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from articles import ARTICLES

SITE = sys.argv[1]
BASE = "https://dailypdflife.com/"
AD = ('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3528972294042151"\n'
      '     crossorigin="anonymous"></script>')

def page(slug, title, h1, desc, body, ld):
    url = BASE + ("guides" if slug == "guides" else slug)
    t, d = html.escape(title, quote=False), html.escape(desc)
    return f"""<!DOCTYPE html>
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
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://dailypdflife.com/banner.png">
<meta name="dpl-h1" content="{html.escape(h1)}">
<meta name="dpl-crumb" content="Guides">
<link rel="stylesheet" href="app.css">
<script src="lang.js"></script>
{AD}
</head>
<body>
{body}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script src="nav.js"></script>
<script src="install.js"></script>
</body>
</html>
"""

cards = []
for a in ARTICLES:
    tools = " ".join(f'<a href="{h}">{l}</a>' for l, h in a["tools"])
    others = " ".join(f'<a href="{b["slug"]}.html">{html.escape(b["h1"])}</a>' for b in ARTICLES if b is not a)
    body = (f'<article class="box seo guide art" data-notr>\n<p class="meta">DailyPdfLife guides · Updated {a["date"]}</p>\n'
            f'{a["body"].strip()}\n<p class="links">Tools used in this guide: {tools}</p>\n</article>\n'
            f'<section class="box seo more" data-notr><h2>More guides</h2><p class="links stack">{others}</p></section>')
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["h1"], "description": a["desc"],
          "datePublished": a["date"], "dateModified": a["date"], "mainEntityOfPage": BASE + a["slug"],
          "image": "https://dailypdflife.com/banner.png",
          "author": {"@type": "Organization", "name": "DailyPdfLife"},
          "publisher": {"@type": "Organization", "name": "DailyPdfLife", "logo": {"@type": "ImageObject", "url": "https://dailypdflife.com/logo.png"}}}
    open(os.path.join(SITE, a["slug"] + ".html"), "w", encoding="utf-8").write(page(a["slug"], a["title"], a["h1"], a["desc"], body, ld))
    cards.append(f'<a class="gcard" href="{a["slug"]}.html"><b>{html.escape(a["h1"])}</b><span>{html.escape(a["desc"])}</span></a>')
    n = len(re.sub(r"<[^>]+>", " ", a["body"]).split())
    print(n, a["slug"])

idx = ('<section class="box seo" data-notr><p>Short, practical guides for everyday document jobs: unlocking bank statements, '
       'making passport photos, shrinking PDFs for online portals, scanning with your phone, VAT and loan maths. '
       'Each guide links to the free DailyPdfLife tool that does the job in your browser.</p></section>\n'
       '<div class="glist" data-notr>\n' + "\n".join(cards) + "\n</div>")
ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "DailyPdfLife guides", "url": BASE + "guides"}
open(os.path.join(SITE, "guides.html"), "w", encoding="utf-8").write(
    page("guides", "Guides – PDF, Photo & Document How-tos | DailyPdfLife", "Guides",
         "Practical how-to guides for PDFs, passport photos, scanning, VAT and loans, with free tools that work in your browser.", idx, ld))
print("guides.html")
