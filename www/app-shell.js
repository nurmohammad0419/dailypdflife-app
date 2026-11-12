/* DailyPdfLife app shell.
   Loaded only inside the Android app. It connects the web tools to the phone:
   saving files to Download, sharing, printing to PDF, opening PDFs from other
   apps, and Google's document scanner. */
(function () {
  var N = window.DPLNative;
  if (!N) return;                                      /* normal website: do nothing */
  document.documentElement.classList.add("inapp");
  var bn = function () { return window.DPL_LANG === "bn"; };
  var t = function (en, b) { return bn() ? b : en; };

  /* ---------- styles for the app-only bits ---------- */
  var css = document.createElement("style");
  css.textContent = [
    ".dpla-sheet{position:fixed;left:12px;right:12px;bottom:14px;z-index:13000;background:#1b2030;color:#fff;border-radius:16px;",
    "padding:14px 16px;box-shadow:0 14px 40px rgba(0,0,0,.35);font:15px/1.4 system-ui,-apple-system,'Segoe UI',Arial,sans-serif;",
    "transform:translateY(140%);transition:transform .25s ease}",
    ".dpla-sheet.show{transform:none}",
    ".dpla-sheet b{display:block;font-size:15px;margin-bottom:2px}",
    ".dpla-sheet small{display:block;opacity:.75;font-size:12.5px;margin-bottom:10px;word-break:break-all}",
    ".dpla-sheet .r{display:flex;gap:8px}",
    ".dpla-sheet button{flex:1;border:0;border-radius:11px;padding:11px;font-weight:700;font-size:14.5px;background:#fff;color:#1b2030}",
    ".dpla-sheet button.g{background:rgba(255,255,255,.14);color:#fff}",
    ".dpla-busy{position:fixed;inset:0;z-index:13001;background:rgba(16,20,30,.45);display:flex;align-items:center;justify-content:center}",
    ".dpla-busy div{background:#fff;border-radius:14px;padding:18px 22px;font:600 15px system-ui,sans-serif;color:#1b2030}",
    ".dpla-hero{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:0 0 16px}",
    ".dpla-hero a,.dpla-hero button{display:flex;flex-direction:column;gap:6px;align-items:flex-start;text-align:left;border:0;border-radius:18px;",
    "padding:18px 16px;color:#fff;text-decoration:none;font:700 17px system-ui,sans-serif;box-shadow:0 8px 22px rgba(20,25,40,.16)}",
    ".dpla-hero span{font-size:30px;line-height:1}",
    ".dpla-hero small{font-weight:500;font-size:12.5px;opacity:.9}",
    ".dpla-hero .scan{background:linear-gradient(135deg,#2b8a3e,#1f6f31)}",
    ".dpla-hero .view{background:linear-gradient(135deg,#e5322d,#b4231f)}",
    ".dpla-scanbox{background:linear-gradient(135deg,#2b8a3e,#1f6f31);color:#fff;border-radius:18px;padding:20px;margin-bottom:16px}",
    ".dpla-scanbox h3{color:#fff !important;margin:0 0 6px !important;font-size:19px !important;letter-spacing:0 !important;text-transform:none !important}",
    ".dpla-scanbox p{margin:0 0 14px;opacity:.92;font-size:14px}",
    ".dpla-scanbox button{background:#fff !important;color:#1f6f31 !important;border:0 !important;font-weight:800 !important;font-size:16px !important;padding:13px 20px !important;width:100%}",
    "html.inapp .adsbygoogle{display:none !important}"
  ].join("");
  document.head.appendChild(css);

  /* ---------- saving files ---------- */
  var sheet = null, hideT = null;
  function showSheet(title, sub, uri, mime) {
    if (!sheet) { sheet = document.createElement("div"); sheet.className = "dpla-sheet"; document.body.appendChild(sheet); }
    sheet.innerHTML = "<b></b><small></small><div class='r'><button class='o'></button><button class='s'></button><button class='g x'>✕</button></div>";
    sheet.querySelector("b").textContent = title;
    sheet.querySelector("small").textContent = sub;
    sheet.querySelector(".o").textContent = t("Open", "খুলুন");
    sheet.querySelector(".s").textContent = t("Share", "শেয়ার");
    sheet.querySelector(".o").onclick = function () { N.openUri(uri, mime); };
    sheet.querySelector(".s").onclick = function () { N.shareUri(uri, mime); };
    sheet.querySelector(".x").onclick = function () { sheet.classList.remove("show"); };
    requestAnimationFrame(function () { sheet.classList.add("show"); });
    clearTimeout(hideT); hideT = setTimeout(function () { sheet.classList.remove("show"); }, 9000);
  }
  function busy(on, msg) {
    var b = document.getElementById("dplaBusy");
    if (on && !b) { b = document.createElement("div"); b.id = "dplaBusy"; b.className = "dpla-busy"; b.innerHTML = "<div></div>"; document.body.appendChild(b); }
    if (b) { if (on) b.firstChild.textContent = msg; else b.remove(); }
  }
  function b64(blob) {
    return new Promise(function (ok, bad) {
      var r = new FileReader();
      r.onload = function () { var s = r.result; ok(s.slice(s.indexOf(",") + 1)); };
      r.onerror = bad; r.readAsDataURL(blob);
    });
  }
  /* blob → native file in chunks, so big PDFs don't choke the bridge */
  function toNative(blob, name, mime, toDownloads) {
    var id = N.begin(name, mime || blob.type || "application/octet-stream", !!toDownloads);
    var CH = 3 * 1024 * 1024, pos = 0;
    function next() {
      if (pos >= blob.size) return Promise.resolve(JSON.parse(N.finish(id)));
      var part = blob.slice(pos, pos + CH); pos += CH;
      return b64(part).then(function (s) { N.chunk(id, s); return next(); });
    }
    return next();
  }
  var saving = 0;
  function save(blob, name) {
    saving++;
    busy(true, t("Saving…", "সেভ হচ্ছে…"));
    var mime = blob.type || guess(name);
    return toNative(blob, name, mime, true).then(function (r) {
      if (--saving === 0) busy(false);
      if (!r.ok) { alert(t("Could not save the file.", "ফাইল সেভ করা গেল না।")); return; }
      showSheet("✓ " + t("Saved", "সেভ হয়েছে"), r.where + "/" + r.name, r.uri, mime);
    }).catch(function () { if (--saving === 0) busy(false); alert(t("Could not save the file.", "ফাইল সেভ করা গেল না।")); });
  }
  function guess(n) {
    var e = (n.split(".").pop() || "").toLowerCase();
    return {pdf: "application/pdf", jpg: "image/jpeg", jpeg: "image/jpeg", png: "image/png", webp: "image/webp", txt: "text/plain",
            csv: "text/csv", docx: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            xlsx: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", zip: "application/zip"}[e] || "application/octet-stream";
  }
  /* every download link on every page ends up here */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[download]");
    if (!a || !a.href) return;
    e.preventDefault(); e.stopPropagation();
    var name = a.getAttribute("download") || "file";
    fetch(a.href).then(function (r) { return r.blob(); }).then(function (b) { save(b, name); });
  }, true);

  /* "Save as PDF" pages (Word to PDF, CV maker …) use the phone's print-to-PDF */
  window.print = function () { N.print(document.title || "DailyPdfLife"); };

  /* ---------- Android back button ---------- */
  window.DPLApp = {
    save: save,
    back: function () {
      var m = document.querySelector(".dplr-mask");
      if (m) { var x = m.querySelector(".dplr-x"); if (x) x.click(); else m.remove(); return "handled"; }
      if (sheet && sheet.classList.contains("show")) { sheet.classList.remove("show"); return "handled"; }
      var rail = document.querySelector(".rail.open");
      if (rail) { var mb = document.getElementById("dplMenu"); if (mb) mb.click(); return "handled"; }
      return "";
    }
  };

  /* ---------- Google document scanner ---------- */
  function plugin() {
    var C = window.Capacitor;
    if (!C) return null;
    if (C.Plugins && C.Plugins.DocumentScanner) return C.Plugins.DocumentScanner;
    return {
      scanDocument: function (o) { return C.nativePromise("DocumentScanner", "scanDocument", o); },
      isGoogleDocumentScannerModuleAvailable: function () { return C.nativePromise("DocumentScanner", "isGoogleDocumentScannerModuleAvailable", {}); },
      installGoogleDocumentScannerModule: function () { return C.nativePromise("DocumentScanner", "installGoogleDocumentScannerModule", {}); }
    };
  }
  function fileUrl(u) {
    var C = window.Capacitor;
    return C && C.convertFileSrc ? C.convertFileSrc(u) : u;
  }
  function stamp() {
    var d = new Date(), p = function (n) { return (n < 10 ? "0" : "") + n; };
    return d.getFullYear() + "-" + p(d.getMonth() + 1) + "-" + p(d.getDate()) + "_" + p(d.getHours()) + p(d.getMinutes());
  }
  function scan() {
    var P = plugin();
    if (!P) { alert(t("The scanner is not available on this phone.", "এই ফোনে স্ক্যানার পাওয়া যাচ্ছে না।")); return; }
    P.scanDocument({galleryImportAllowed: true, pageLimit: 50, resultFormats: "JPEG_PDF", scannerMode: "FULL"})
      .then(function (r) {
        if (!r || !r.pdf || !r.pdf.uri) return;
        busy(true, t("Preparing your PDF…", "PDF তৈরি হচ্ছে…"));
        return fetch(fileUrl(r.pdf.uri)).then(function (x) { return x.blob(); }).then(function (b) {
          busy(false);
          var blob = new Blob([b], {type: "application/pdf"}), name = "Scan_" + stamp() + ".pdf";
          if (window.DPLResult) DPLResult.file(blob, name); else save(blob, name);
        });
      })
      .catch(function (err) {
        busy(false);
        var m = String(err && (err.message || err) || "");
        if (/cancel/i.test(m)) return;
        alert(t("The scanner could not start. Make sure Google Play services is up to date, or use the other options below.",
                "স্ক্যানার চালু হলো না। Google Play services আপডেট আছে কিনা দেখুন, অথবা নিচের অন্য উপায়গুলো ব্যবহার করুন।"));
      });
  }
  window.DPLApp.scan = scan;

  /* ---------- app-only extras on certain pages ---------- */
  function ready(fn) { if (document.readyState !== "loading") fn(); else document.addEventListener("DOMContentLoaded", fn); }
  ready(function () {
    var page = (location.pathname.split("/").pop() || "index.html").toLowerCase();
    var host = document.querySelector(".shell main, main, .main, body");
    if (page === "index.html" || page === "") {
      var h = document.createElement("div"); h.className = "dpla-hero";
      h.innerHTML = "<button class='scan' id='dplaScan'><span>📷</span>" + t("Scan document", "ডকুমেন্ট স্ক্যান") +
        "<small>" + t("Auto edges, crop &amp; clean", "নিজে থেকে কিনারা খুঁজে কাটে ও পরিষ্কার করে") + "</small></button>" +
        "<a class='view' href='pdf-viewer.html'><span>📖</span>" + t("Open PDF", "PDF খুলুন") +
        "<small>" + t("Read, zoom and search", "পড়ুন, জুম ও সার্চ করুন") + "</small></a>";
      var first = document.querySelector(".hero, .tsec, .chips");
      if (first && first.parentNode) first.parentNode.insertBefore(h, first); else host.insertBefore(h, host.firstChild);
      h.querySelector("#dplaScan").onclick = scan;
    }
    if (page === "scan-to-pdf.html") {
      var s = document.createElement("div"); s.className = "dpla-scanbox";
      s.innerHTML = "<h3>📷 " + t("Smart scan", "স্মার্ট স্ক্যান") + "</h3><p>" +
        t("Point the camera at the paper. The page edges are found for you, the shot is taken by itself, and the page is straightened and cleaned like a real scanner.",
          "কাগজের দিকে ক্যামেরা ধরুন। কিনারা নিজে থেকে খুঁজে ছবি তোলে, তারপর আসল স্ক্যানারের মতো সোজা ও পরিষ্কার করে দেয়।") +
        "</p><button id='dplaScan2'>📷 " + t("Start scanning", "স্ক্যান শুরু করুন") + "</button>";
      var box = document.querySelector(".box");
      if (box && box.parentNode) box.parentNode.insertBefore(s, box); else host.insertBefore(s, host.firstChild);
      s.querySelector("#dplaScan2").onclick = scan;
    }
  });
})();
