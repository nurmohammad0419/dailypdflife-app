"""Add the new tools to nav.js, the home page and the tool counts."""
import re, sys
S = sys.argv[1]
NEW = {
 "PDF tools": [
  ["Sign PDF", "sign-pdf.html", "✍", "#1a3fb0", "Draw, type or upload your signature and place it on a PDF.", "sign signature e-sign"],
  ["Compare PDF", "compare-pdf.html", "⇆", "#1c7ed6", "See what changed between two versions of a PDF.", "compare difference diff changes versions"],
  ["Flatten PDF", "flatten-pdf.html", "▤", "#5f3dc4", "Lock form fields and comments so they can't be changed.", "flatten lock form annotations"],
  ["Grayscale PDF", "grayscale-pdf.html", "◐", "#495057", "Turn a colour PDF into grayscale or black and white.", "grayscale black white monochrome print"]],
 "Convert": [
  ["PDF to PNG", "pdf-to-png.html", "🖼", "#f08c00", "Turn PDF pages into sharp PNG or WEBP images.", "png webp image picture"],
  ["PowerPoint to PDF", "ppt-to-pdf.html", "P", "#c43e1c", "Turn a .pptx presentation into a PDF.", "ppt pptx powerpoint slides presentation"],
  ["PDF to text", "pdf-to-text.html", "📝", "#495057", "Pull all the text out of a PDF into a .txt file.", "text txt extract copy"],
  ["HTML to PDF", "html-to-pdf.html", "‹›", "#e8590c", "Turn an HTML file or pasted content into a PDF.", "html web page code"],
  ["ZIP files", "zip-files.html", "🗜", "#5f3dc4", "Make a ZIP from many files, or open a ZIP.", "zip unzip extract archive compress"]],
 "Image tools": [
  ["Resize image to KB", "image-to-kb.html", "KB", "#1c7ed6", "Make a photo exactly 20 KB, 50 KB, 100 KB or any size.", "kb size reduce photo form 20kb 50kb 100kb"],
  ["Signature maker", "signature-maker.html", "✒", "#1a3fb0", "Draw or type a signature and save it as a transparent PNG.", "signature sign png transparent"],
  ["Photo enhancer", "photo-enhancer.html", "✨", "#7b3fe4", "Brighten, sharpen and fix the colours of a photo.", "enhance brighten sharpen fix colour quality"],
  ["Meme maker", "meme-maker.html", "😂", "#f59f00", "Make a meme with top and bottom text or a caption.", "meme funny caption"]],
 "Document makers": [
  ["ID card maker", "id-card-maker.html", "🪪", "#1c4fa1", "Design employee, student and event ID cards, front and back.", "id card identity badge employee student pass"],
  ["Calendar maker", "calendar-maker.html", "📆", "#e5322d", "Make a printable calendar with your photos, holidays and Hijri or Bangla dates.", "calendar planner year month print photo hijri bangla"]],
 "Smart tools": [
  ["Emergency numbers", "emergency-numbers.html", "🆘", "#e03131", "Police, ambulance and fire numbers for your country and city.", "emergency police ambulance fire hospital helpline 999 911"],
  ["Prayer times", "prayer-times.html", "🕌", "#0b7285", "Today's salah times for your city, with a countdown.", "prayer salah namaz times azan fajr maghrib"]],
 "Calculators": [
  ["End of service (gratuity)", "gratuity-calculator.html", "💼", "#087f5b", "Saudi and UAE end-of-service benefit for your years of work.", "gratuity end of service eosb benefit saudi uae"],
  ["Currency converter", "currency-converter.html", "💱", "#1c7ed6", "SAR, BDT, AED, USD and more at today's rates.", "currency exchange rate riyal taka dirham dollar"],
  ["BMI calculator", "bmi-calculator.html", "⚖", "#2b8a3e", "Body mass index and the healthy weight for your height.", "bmi weight height health"],
  ["Date calculator", "date-calculator.html", "📅", "#e8590c", "Days between two dates, or add days to a date.", "date days between difference add working days"]],
}
nav = open(f"{S}/nav.js", encoding="utf-8").read()
idx = open(f"{S}/index.html", encoding="utf-8").read()
for g, tools in NEW.items():
    # nav: append to the group's list
    m = re.search(r'\["' + re.escape(g) + r'", \[\n(.*?)\n    \]\]', nav, re.S)
    body = m.group(1)
    add = "".join(f',\n      ["{t[0]}", "{t[1]}", "{t[2]}", "{t[3]}", "{t[4]}"]' for t in tools if t[1] not in body)
    nav = nav[:m.end(1)] + add + nav[m.end(1):]
    # home: append cards to the section
    sm = re.search(r'(<section class="tsec" data-c="' + re.escape(g) + r'">.*?)(\n        </div>\n      </section>)', idx, re.S)
    cards = ""
    for t in tools:
        href = t[1][:-5]
        if f'href="{href}"' in sm.group(1): continue
        key = (t[0] + " " + t[4] + " " + t[5]).lower().replace('"', "")
        cards += (f'\n        <a class="tcard" href="{href}" style="--c:{t[3]}" data-k="{key}">\n'
                  f'          <span class="ic">{t[2]}</span>\n'
                  f'          <span class="tx"><b>{t[0]}</b><i>{t[4]}</i></span>\n        </a>')
    idx = idx[:sm.end(1)] + cards + idx[sm.end(1):]
open(f"{S}/nav.js", "w", encoding="utf-8").write(nav)
# section counts and total
total = 0
def recount(m):
    global total
    n = m.group(2).count('class="tcard"'); total += n
    return re.sub(r"<span>\d+</span>", f"<span>{n}</span>", m.group(1), count=1) + m.group(2)
idx = re.sub(r'(<section class="tsec" data-c="[^"]+">\s*<h2>[^<]*<span>\d+</span></h2>)(.*?</section>)', recount, idx, flags=re.S)
idx = re.sub(r"\b\d\d free tools", f"{total} free tools", idx)
idx = re.sub(r"<div><b>\d\d</b>tools</div>", f"<div><b>{total}</b>tools</div>", idx)
open(f"{S}/index.html", "w", encoding="utf-8").write(idx)
print("total tools on home:", total)
