/* DailyPdfLife service worker: makes the site work offline and open fast
   when it is added to the Home Screen. */
const VERSION = "dpl-0d99165352";
const CORE = ["about", "age-calculator", "app.css", "banner.svg", "blur-image", "construction-calculator", "contact", "cover-letter", "crop-image", "crop-pdf", "cropbox.js", "cv-maker", "excel-to-pdf", "favicon.svg", "fill-pdf-forms", "guide-bangla-pdf-text-copy-broken", "guide-cv-for-gulf-jobs", "guide-documents-for-visa-iqama-applications", "guide-flat-vs-reducing-rate", "guide-heic-photos-not-opening", "guide-passport-photo-size", "guide-reduce-pdf-size", "guide-saudi-vat-15-percent", "guide-scan-documents-phone", "guide-sign-pdf-on-phone", "guide-unlock-bank-statement-pdf", "guide-zakat-on-gold-and-savings", "guides", "heic-to-jpg", "hijri-converter", "image-tools", "image-watermark", "./", "install.js", "invoice-maker", "lang.js", "loan-calculator", "logo.svg", "manifest.webmanifest", "merge-and-jpg", "more-tools", "nav.js", "ocr", "organize-pdf", "passport-photo", "pdf-editor", "pdf-password", "pdf-to-excel", "pdf-to-jpg", "pdf-to-word", "pdf-viewer", "percentage-calculator", "photo-collage", "privacy", "qpdf-run.js", "qr-code", "redact-pdf", "remove-bg", "remove-pages", "result.js", "saudi-vat-calculator", "scan-to-pdf", "split-and-compress", "stamp-pdf", "terms", "text-on-photo", "uae-vat-calculator", "unit-converter", "unlock-pdf", "vat-calculator", "word-to-pdf", "zakat-calculator", "icon-192.png", "apple-touch-icon.png", "logo.png"];
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
      }).catch(() => caches.match(stripQuery(req)).then(r => r || caches.match("./")))
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
/* pages are saved under their clean address (/about, not /about.html) */
function stripQuery(req){ const u = new URL(req.url); u.search = ""; u.hash = ""; u.pathname = u.pathname.replace(/index\.html$/, "").replace(/\.html$/, ""); return u.toString(); }
