/* DailyPdfLife service worker: makes the site work offline and open fast
   when it is added to the Home Screen. */
const VERSION = "dpl-824a088352";
const CORE = ["about.html", "age-calculator.html", "app.css", "banner.svg", "blur-image.html", "construction-calculator.html", "contact.html", "cover-letter.html", "crop-image.html", "crop-pdf.html", "cropbox.js", "cv-maker.html", "excel-to-pdf.html", "favicon.svg", "fill-pdf-forms.html", "heic-to-jpg.html", "hijri-converter.html", "image-tools.html", "image-watermark.html", "index.html", "install.js", "invoice-maker.html", "lang.js", "loan-calculator.html", "logo.svg", "manifest.webmanifest", "merge-and-jpg.html", "more-tools.html", "nav.js", "ocr.html", "organize-pdf.html", "passport-photo.html", "pdf-editor.html", "pdf-password.html", "pdf-to-excel.html", "pdf-to-jpg.html", "pdf-to-word.html", "pdf-viewer.html", "percentage-calculator.html", "photo-collage.html", "privacy.html", "qpdf-run.js", "qr-code.html", "redact-pdf.html", "remove-bg.html", "remove-pages.html", "result.js", "scan-to-pdf.html", "split-and-compress.html", "stamp-pdf.html", "terms.html", "text-on-photo.html", "unit-converter.html", "unlock-pdf.html", "vat-calculator.html", "word-to-pdf.html", "zakat-calculator.html", "icon-192.png", "apple-touch-icon.png", "logo.png"];
/* libraries from these hosts never change for the same address, so keep them */
const LIB_HOSTS = ["cdnjs.cloudflare.com", "unpkg.com", "cdn.jsdelivr.net"];
/* big AI models (background removal, OCR languages) are not stored: too large for a phone */
const SKIP = [/@imgly\//, /tesseract/i, /tessdata/i, /googlesyndication|doubleclick|google-analytics|adservice/];

/* the main libraries, saved ahead so the tools also work offline the first time */
const LIBS = [
  "vendor/pdf.min.js",
  "vendor/pdf.worker.min.js",
  "vendor/pdf-lib.min.js",
  "vendor/qrcode.min.js",
  "vendor/xlsx.full.min.js",
  "vendor/mammoth.browser.min.js",
  "vendor/heic2any.min.js",
  "vendor/qpdf/qpdf.js",
  "vendor/qpdf/qpdf.wasm"
];
self.addEventListener("install", e => {
  const libs = caches.open("dpl-libs").then(c => Promise.all(LIBS.map(u =>
    c.match(u).then(hit => hit || fetch(u, {mode: "cors"}).then(r => { if (r.ok) return c.put(u, r); }).catch(() => {}))
  ))).catch(() => {});
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(CORE.map(u => new Request(u, {cache: "reload"}))))
    .then(() => libs).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith("dpl-") && k !== VERSION && k !== "dpl-libs").map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (SKIP.some(r => r.test(req.url))) return;

  /* pages: try the network first so updates show up, fall back to the saved copy offline */
  if (req.mode === "navigate") {
    e.respondWith(
      fetch(req).then(res => {
        if (res.ok && url.origin === location.origin) { const copy = res.clone(); caches.open(VERSION).then(c => c.put(stripQuery(req), copy)); }
        return res;
      }).catch(() => caches.match(stripQuery(req)).then(r => r || caches.match("index.html")))
    );
    return;
  }
  /* libraries: saved copy first */
  if (LIB_HOSTS.includes(url.hostname)) {
    e.respondWith(caches.open("dpl-libs").then(c => c.match(req).then(hit => hit || fetch(req).then(res => {
      if (res.ok || res.type === "opaque") c.put(req, res.clone());
      return res;
    }))));
    return;
  }
  /* our own files: saved copy right away, refresh it in the background */
  if (url.origin === location.origin) {
    e.respondWith(caches.open(VERSION).then(c => c.match(req, {ignoreSearch: true}).then(hit => {
      const net = fetch(req).then(res => { if (res.ok) c.put(req, res.clone()); return res; }).catch(() => hit);
      return hit || net;
    })));
  }
});
function stripQuery(req){ const u = new URL(req.url); u.search = ""; u.hash = ""; if (u.pathname.endsWith("/")) u.pathname += "index.html"; return u.toString(); }
