/* DailyPdfLife — app shell: top bar, left tool rail, page header.
   Works together with app.css. Loaded on every page. */
(function () {
  var GROUPS = [
    ["PDF tools", [
      ["PDF viewer", "pdf-viewer.html", "📖", "#e5322d", "Open and read a PDF: zoom, search and night mode."],
      ["Merge PDF", "merge-and-jpg.html#merge", "⧉", "#e5322d", "Join several PDFs into one file."],
      ["Split PDF", "split-and-compress.html#split", "✂", "#f76707", "Split pages apart or pull out the ones you need."],
      ["Compress PDF", "split-and-compress.html#compress", "⇲", "#7b3fe4", "Make a PDF file smaller."],
      ["Edit PDF", "pdf-editor.html", "✏", "#c2255c", "Add text, shapes, images and signatures to a PDF."],
      ["Rotate PDF", "more-tools.html#rotate", "↻", "#f08c00", "Turn pages right, left or upside down."],
      ["Page numbers", "more-tools.html#numbers", "#", "#1c7ed6", "Put a number on every page."],
      ["Watermark", "more-tools.html#watermark", "💧", "#0ca678", "Stamp a watermark across every page."],
      ["Protect PDF", "pdf-password.html", "🔒", "#c92a2a", "Lock a PDF with strong AES-256 encryption."],
      ["Organize PDF", "organize-pdf.html", "▦", "#1971c2", "Reorder, rotate, remove and combine pages."],
      ["Unlock PDF", "unlock-pdf.html", "🔓", "#0b7285", "Remove the password and restrictions from a PDF you can open."],
      ["Fill PDF forms", "fill-pdf-forms.html", "☑", "#5f3dc4", "Type into the boxes of a fillable PDF form."],
      ["Redact PDF", "redact-pdf.html", "⬛", "#212529", "Black out private text and remove it from the file for good."],
      ["Crop PDF", "crop-pdf.html", "⌗", "#e8590c", "Trim the margins or cut pages to a smaller area."],
      ["Remove pages", "remove-pages.html", "🗑", "#e03131", "Delete the pages you don't need from a PDF."],
      ["Extract pages", "remove-pages.html#extract", "📤", "#1971c2", "Save only the pages you choose as a new PDF."],
      ["Stamp PDF", "stamp-pdf.html", "🔖", "#c92a2a", "Add a PAID or APPROVED stamp, or your company seal."]
    ]],
    ["Convert", [
      ["PDF to Word", "pdf-to-word.html", "W", "#2b579a", "Pull the text out of a PDF into a Word file."],
      ["PDF to JPG", "pdf-to-jpg.html", "🖼", "#f59f00", "Turn every page into a JPG image."],
      ["JPG to PDF", "merge-and-jpg.html#jpg", "📷", "#2e9d4a", "Turn images into a PDF."],
      ["Word to PDF", "word-to-pdf.html", "W", "#1864ab", "Turn a Word (.docx) document into a PDF."],
      ["HEIC to JPG", "heic-to-jpg.html", "📱", "#f59f00", "Convert iPhone photos to JPG or PNG."],
      ["Scan to PDF", "scan-to-pdf.html", "📄", "#2b8a3e", "Photograph paper pages and turn them into a clean PDF."],
      ["Excel to PDF", "excel-to-pdf.html", "X", "#1d6f42", "Turn an Excel or CSV sheet into a neat PDF."],
      ["PDF to Excel", "pdf-to-excel.html", "📊", "#2f9e44", "Pull tables out of a PDF into an Excel sheet."]
    ]],
    ["Image tools", [
      ["Remove background", "remove-bg.html", "🪄", "#7b3fe4", "Cut the background out of a photo with AI."],
      ["Compress image", "image-tools.html#compress", "🗜", "#1c7ed6", "Shrink an image while keeping it sharp."],
      ["Resize image", "image-tools.html#resize", "↔", "#f08c00", "Change an image's size in pixels or percent."],
      ["Convert image", "image-tools.html#convert", "⇄", "#0ca678", "Convert between JPG, PNG and WEBP."],
      ["Passport photo", "passport-photo.html", "🪪", "#1971c2", "Make passport and visa photos ready to print."],
      ["Crop image", "crop-image.html", "✂", "#c2255c", "Cut a photo to any shape, rotate or flip it."],
      ["Photo collage", "photo-collage.html", "🧩", "#d6336c", "Put several photos together in one picture."],
      ["Image watermark", "image-watermark.html", "💧", "#0ca678", "Add your name or logo to photos."],
      ["Blur & hide", "blur-image.html", "🫥", "#5f3dc4", "Blur faces, numbers or private details in a photo."],
      ["Text on photo", "text-on-photo.html", "🅰", "#e8590c", "Write captions, quotes or meme text on a picture."]
    ]],
    ["Document makers", [
      ["CV maker", "cv-maker.html", "📄", "#7b3fe4", "Build a clean CV and download it as a PDF."],
      ["Invoice & quotation", "invoice-maker.html", "🧾", "#0b7285", "Create professional invoices and quotations."],
      ["Cover letter", "cover-letter.html", "✉", "#c2255c", "Write a cover letter for a job application."]
    ]],
    ["Smart tools", [
      ["OCR", "ocr.html", "🔍", "#e8590c", "Pull text out of a photo or a scanned PDF."],
      ["QR code", "qr-code.html", "🔳", "#212529", "Make QR codes for links, WhatsApp and WiFi."],
      ["Hijri date converter", "hijri-converter.html", "☪", "#0ca678", "Convert between Hijri (Umm al-Qura) and Gregorian dates."]
    ]],
    ["Calculators", [
      ["VAT calculator", "vat-calculator.html", "%", "#0b7285", "Add or remove VAT for Saudi Arabia, UAE and more."],
      ["Zakat calculator", "zakat-calculator.html", "☾", "#087f5b", "Work out the zakat due on your savings, gold and silver."],
      ["Loan & EMI", "loan-calculator.html", "🏦", "#1c7ed6", "Monthly payment and total profit for any loan or finance."],
      ["Percentage", "percentage-calculator.html", "٪", "#7048e8", "Percent of, increase, decrease and discount in one place."],
      ["Age calculator", "age-calculator.html", "🎂", "#d6336c", "Exact age in years, months and days, also in Hijri."],
      ["Unit converter", "unit-converter.html", "⇆", "#1971c2", "Length, area, weight, pressure, flow, pipe sizes and more."],
      ["Construction", "construction-calculator.html", "🏗", "#e67700", "Tiles, paint, concrete, blocks, pipes and water tanks."]
    ]]
  ];

  if (!document.querySelector("link[rel~='icon']")) {
    var fav = document.createElement("link");
    fav.rel = "icon"; fav.type = "image/svg+xml"; fav.href = "favicon.svg";
    document.head.appendChild(fav);
  }
  if (!document.querySelector('link[href="app.css"]')) {
    var cs = document.createElement("link");
    cs.rel = "stylesheet"; cs.href = "app.css";
    document.head.appendChild(cs);
  }

  var file = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  var hash = (location.hash || "").toLowerCase();
  var isHome = file === "index.html" || file === "";

  var current = null;
  GROUPS.forEach(function (g) {
    g[1].forEach(function (t) {
      var parts = t[1].toLowerCase().split("#");
      if (parts[0] !== file) return;
      if (!current) current = { t: t, g: g[0] };
      if (hash && parts[1] && ("#" + parts[1]) === hash) current = { t: t, g: g[0] };
    });
  });

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }

  var curLang = window.DPL_LANG || "en";
  var bar = el("div", "appbar");
  bar.innerHTML =
    '<button class="menu" id="dplMenu">☰ <span>Tools</span></button>' +
    '<a class="brand" href="index.html"><img src="logo.svg" alt="DailyPdfLife"></a>' +
    (current ? '<span class="sep"></span><span class="where">' +
      current.g + " · " + current.t[0] + "</span>" : "") +
    '<span class="sp"></span>' +
    '<span class="ptlang">' +
      '<button data-l="en"' + (curLang === "en" ? ' class="on"' : "") + ">EN</button>" +
      '<button data-l="bn"' + (curLang === "bn" ? ' class="on"' : "") + ">বাংলা</button>" +
    "</span>";

  var rail = el("nav", "rail");
  var html = '<a class="home' + (isHome ? " on" : "") + '" href="index.html">' +
             '<span class="ic" style="background:#1b2030">⌂</span>All tools</a>';
  GROUPS.forEach(function (g) {
    html += "<h6>" + g[0] + "</h6>";
    g[1].forEach(function (t) {
      var on = (current && current.t === t) ? "on" : "";
      html += '<a class="' + on + '" href="' + t[1] + '">' +
              '<span class="ic" style="background:' + t[3] + '">' + t[2] + "</span>" + t[0] + "</a>";
    });
  });
  rail.innerHTML = html;

  var mask = el("div", "railmask");
  mask.style.cssText =
    "position:fixed;inset:56px 0 0;background:rgba(18,21,28,.3);z-index:8400;display:none";

  var style = el("style");
  style.textContent = [
    ".ptlang{display:inline-flex;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#fff}",
    ".ptlang button{border:0;background:#fff;color:#5a6274;padding:7px 12px;font-size:13px;font-weight:700;",
    "cursor:pointer;font-family:inherit;border-radius:0}",
    ".ptlang button+button{border-left:1px solid var(--line-2)}",
    ".ptlang button.on{background:#1b2030;color:#fff}",
    ".appbar .menu{border:1px solid var(--line);background:#fff;color:var(--ink);border-radius:10px;",
    "padding:7px 11px;font-size:16px;line-height:1;font-weight:650;cursor:pointer;font-family:inherit;",
    "align-items:center;gap:7px}",
    ".appbar .menu span{font-size:13.5px}",
    "@media(max-width:520px){.appbar .menu span{display:none}}"
  ].join("");
  document.head.appendChild(style);

  function mount() {
    var kids = [].slice.call(document.body.childNodes).filter(function (n) {
      if (n.nodeType === 1 && (n.tagName === "SCRIPT" || n.tagName === "LINK")) return false;
      if (n.nodeType === 8) return false;
      if (n.nodeType === 3 && !n.nodeValue.trim()) return false;
      return true;
    });

    document.body.insertBefore(bar, document.body.firstChild);
    document.body.appendChild(rail);
    document.body.appendChild(mask);

    var shell = el("div", "shell");
    document.body.appendChild(shell);

    /* a page can set its own main heading: <meta name="dpl-h1" content="..."> */
    var h1m = document.querySelector('meta[name="dpl-h1"]');
    var dm = document.querySelector('meta[name="description"]');
    if (!current && h1m) current = { t: [h1m.content, "", "", "", dm ? dm.content : ""], g: "Calculators" };
    if (current) {
      shell.appendChild(el("div", "phead",
        '<div class="crumb">' + current.g + "</div>" +
        "<h1>" + (h1m ? h1m.content : current.t[0]) + "</h1>" +
        "<p>" + current.t[4] + "</p>"));
    }
    kids.forEach(function (k) { shell.appendChild(k); });
    shell.appendChild(el("footer", "sitefoot",
      "<span>\u00a9 2026 DailyPdfLife.com \u00b7 Your files never leave your device.</span>" +
      '<nav><a href="about.html">About</a><a href="contact.html">Contact</a>' +
      '<a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a></nav>'));

    if (current) {
      var want = current.t[0].toLowerCase().replace(/[^a-z0-9]/g, "");
      [].forEach.call(shell.querySelectorAll(".box h1,.panel h1,.panel h2,.form h2"), function (h) {
        var got = h.textContent.toLowerCase().replace(/[^a-z0-9]/g, "");
        if (got && (got === want || want.indexOf(got) === 0 || got.indexOf(want) === 0)) h.style.display = "none";
      });
    }

    document.getElementById("dplMenu").onclick = function () {
      rail.classList.toggle("open");
      mask.style.display = rail.classList.contains("open") ? "block" : "none";
    };
    mask.onclick = function () { rail.classList.remove("open"); mask.style.display = "none"; };
    rail.addEventListener("click", function (e) {
      if (e.target.closest("a")) { rail.classList.remove("open"); mask.style.display = "none"; }
    });
    /* fixed-width previews (CV, invoice, letter) are scaled to fit their column */
    var papers = shell.querySelectorAll("#cv,#doc,#letter");
    [].forEach.call(papers, function (el) {
      var box = document.createElement("div");
      box.className = "paper";
      el.parentNode.insertBefore(box, el);
      box.appendChild(el);
    });
    function fitPaper() {
      [].forEach.call(shell.querySelectorAll(".paper"), function (box) {
        var el = box.firstElementChild; if (!el) return;
        el.style.transform = "none";
        var w = el.offsetWidth, avail = box.clientWidth;
        if (!w || !avail) return;
        var k = Math.min(1, avail / w);
        el.style.transform = k < 1 ? "scale(" + k + ")" : "none";
        box.style.height = (el.offsetHeight * k) + "px";
      });
    }
    window.DPL_fitPaper = fitPaper;
    setTimeout(fitPaper, 60);
    window.addEventListener("resize", fitPaper);
    new MutationObserver(function () { clearTimeout(window.__fp); window.__fp = setTimeout(fitPaper, 120); })
      .observe(shell, { childList: true, subtree: true, characterData: true });

    [].forEach.call(bar.querySelectorAll(".ptlang button"), function (b) {
      b.onclick = function () { if (window.DPL_setLang) window.DPL_setLang(b.dataset.l); };
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount);
  else mount();
})();
