"""Rewrite internal href="x.html" links in the website to clean addresses (/x). Run after any generator."""
import os, re, sys
S = sys.argv[1] if len(sys.argv) > 1 else "site"
pages = {f[:-5] for f in os.listdir(S) if f.endswith(".html")}
rx = re.compile(r'href=(["\'])([a-z0-9-]+)\.html(#[^"\']*)?\1')
def fix(m):
    q, slug, h = m.group(1), m.group(2), m.group(3) or ""
    if slug not in pages: return m.group(0)
    return f'href={q}{"/" + h if slug == "index" else slug + h}{q}'
n = 0
for f in os.listdir(S):
    if f.endswith(".html"):
        p = os.path.join(S, f); t = open(p, encoding="utf-8").read(); o = rx.sub(fix, t)
        if o != t: open(p, "w", encoding="utf-8").write(o); n += 1
print("clean links in", n, "files")
