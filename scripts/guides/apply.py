"""Insert guide sections, titles and descriptions into tool pages.
Run: python3 scripts/guides/apply.py site"""
import html, json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from g1 import G as A
from g2 import G as B
from g3 import G as C

SITE = sys.argv[1]
G = {**A, **B, **C}
BASE = "https://dailypdflife.com/"

def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))

def section(d):
    out = ['<section class="box seo guide" data-notr>']
    for h, body in d["sections"]:
        out.append(f"  <h2>{h}</h2>\n  {body}")
    out.append("  <h2>Frequently asked questions</h2>")
    out.append("  " + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in d["faq"]))
    out.append("  <p class=\"links\">Related tools: " + " ".join(f'<a href="{h}">{t}</a>' for t, h in d["related"]) + "</p>")
    out.append("</section>")
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in d["faq"]]}
    out.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>")
    return "\n".join(out) + "\n"

words = {}
for name, d in G.items():
    p = os.path.join(SITE, name)
    t = open(p, encoding="utf-8").read()
    t = re.sub(r'\n?<section class="box seo guide" data-notr>.*?</section>\n<script type="application/ld\+json">.*?</script>\n', "\n", t, flags=re.S)
    title = html.escape(d["title"], quote=False)
    desc = html.escape(d["desc"])
    url = BASE + name[:-5]
    t = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", t, count=1, flags=re.S)
    for pat in [r'<meta name="description"[^>]*>\n', r'<link rel="canonical"[^>]*>\n', r'<meta property="og:[^"]*"[^>]*>\n']:
        t = re.sub(pat, "", t)
    head = (f'<meta name="description" content="{desc}">\n<link rel="canonical" href="{url}">\n'
            f'<meta property="og:title" content="{title}">\n<meta property="og:description" content="{desc}">\n'
            f'<meta property="og:url" content="{url}">\n<meta property="og:image" content="https://dailypdflife.com/banner.png">\n')
    t = t.replace(f"<title>{title}</title>\n", f"<title>{title}</title>\n" + head, 1)
    assert '<script src="nav.js"></script>' in t, name
    t = t.replace('<script src="nav.js"></script>', section(d) + '<script src="nav.js"></script>', 1)
    open(p, "w", encoding="utf-8").write(t)
    words[name] = len(strip(" ".join(b for _, b in d["sections"]) + " ".join(q + " " + a for q, a in d["faq"])).split())
for k, v in sorted(words.items(), key=lambda x: x[1]):
    print(v, k)
print(len(G), "pages")
