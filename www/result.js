/* DailyPdfLife - result panel.
   Nothing downloads on its own: finished files are shown here with a preview
   and a Download button, so the user can review first. */
(function () {
  var css = document.createElement("style");
  css.textContent = [
    ".dplr-mask{position:fixed;inset:0;background:rgba(16,20,30,.55);z-index:12000;display:flex;",
    "align-items:center;justify-content:center;padding:20px;font-family:system-ui,-apple-system,'Segoe UI',Arial,sans-serif}",
    ".dplr{background:#fff;border-radius:18px;max-width:860px;width:100%;max-height:92vh;display:flex;",
    "flex-direction:column;overflow:hidden;box-shadow:0 24px 60px rgba(10,14,24,.35)}",
    ".dplr-top{display:flex;align-items:center;gap:12px;padding:16px 20px;border-bottom:1px solid #eceff5}",
    ".dplr-top h3{margin:0;font-size:17px;flex:1;color:#1f2430;letter-spacing:-.2px}",
    ".dplr-x{border:0;background:#f2f4f9;color:#5a6274;width:34px;height:34px;border-radius:10px;",
    "cursor:pointer;font-size:17px;line-height:1;flex:none;padding:0}",
    ".dplr-x:hover{background:#e6e9f1}",
    ".dplr-body{padding:16px 20px;overflow:auto}",
    ".dplr-prev{background:#f5f6fa;border:1px solid #e6e9f1;border-radius:12px;overflow:hidden;margin-bottom:14px}",
    ".dplr-prev iframe{width:100%;height:60vh;min-height:320px;border:0;display:block;background:#fff}",
    ".dplr-prev img{width:100%;max-height:60vh;object-fit:contain;display:block;background:#fff}",
    ".dplr-pages{max-height:60vh;overflow:auto;padding:12px;display:flex;flex-direction:column;align-items:center;gap:12px}",
    ".dplr-pages canvas{max-width:100%;box-shadow:0 2px 10px rgba(16,20,30,.16);border-radius:4px;background:#fff}",
    ".dplr-more{margin:4px 0 0;font-size:13px;color:#8b90a0}",
    ".dplr-note{margin:26px 0 8px;font-size:14px;color:#6b7283}",
    ".dplr-open{font-size:14px;font-weight:700;color:#e5322d;text-decoration:none;margin-bottom:22px}",
    ".dplr-prev pre{margin:0;padding:14px;max-height:40vh;overflow:auto;white-space:pre-wrap;",
    "font-size:13px;color:#2b2f3a;font-family:ui-monospace,Consolas,monospace}",
    ".dplr-row{display:flex;align-items:center;gap:12px;padding:11px 14px;border:1px solid #e6e9f1;",
    "border-radius:12px;margin-bottom:9px;background:#fff}",
    ".dplr-row .nm{flex:1;min-width:0;font-size:14.5px;color:#1f2430;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}",
    ".dplr-row .sz{font-size:12.5px;color:#8b90a0;flex:none}",
    ".dplr-row.on{border-color:#e5322d;background:#fff6f5}",
    ".dplr-pick{border:0;background:transparent;cursor:pointer;flex:1;display:flex;gap:12px;align-items:center;",
    "text-align:left;padding:0;font-family:inherit;min-width:0}",
    ".dplr-btn{border:0;border-radius:10px;padding:10px 16px;font-size:14px;font-weight:700;cursor:pointer;",
    "font-family:inherit;background:#e5322d;color:#fff;flex:none}",
    ".dplr-btn:hover{filter:brightness(1.07)}",
    ".dplr-btn.ghost{background:#f2f4f9;color:#2b2f3a}",
    ".dplr-foot{display:flex;gap:10px;justify-content:flex-end;padding:14px 20px;border-top:1px solid #eceff5;",
    "background:#fbfcfe;flex-wrap:wrap}",
    "@media(max-width:600px){.dplr-prev iframe{height:46vh}.dplr-foot{justify-content:stretch}.dplr-foot .dplr-btn{flex:1}}"
  ].join("");
  document.head.appendChild(css);

  function kb(n) {
    return n > 1048576 ? (n / 1048576).toFixed(2) + " MB" : Math.max(1, Math.round(n / 1024)) + " KB";
  }

  function saveBlob(blob, name) {
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url; a.download = name;
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 60000);
  }

  /* iPhone / iPad: the share sheet has "Save to Files", which works better than a download,
     especially when the site is added to the Home Screen */
  var IOS = /iPhone|iPad|iPod/.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  function asFile(blob, name) {
    try { return new File([blob], name, { type: blob.type || guess(name) }); } catch (e) { return null; }
  }
  function canShare(files) {
    if (!IOS || window.DPLNative || !navigator.share || !navigator.canShare) return false;
    try { return files.every(Boolean) && navigator.canShare({ files: files }); } catch (e) { return false; }
  }
  function saveSmart(blob, name) {
    var f = asFile(blob, name);
    if (canShare([f])) {
      navigator.share({ files: [f] }).catch(function (e) { if (!e || e.name !== "AbortError") saveBlob(blob, name); });
    } else saveBlob(blob, name);
  }
  var T = function (s) { return window.T ? window.T(s) : s; };

  /* pdf.js is used for the preview so no browser ever treats it as a download */
  var pdfjsPromise = null;
  function ensurePdfJs() {
    if (window.pdfjsLib) return Promise.resolve(window.pdfjsLib);
    if (pdfjsPromise) return pdfjsPromise;
    pdfjsPromise = new Promise(function (ok, bad) {
      var s = document.createElement("script");
      s.src = "vendor/pdf.min.js";
      s.onload = function () {
        try {
          window.pdfjsLib.GlobalWorkerOptions.workerSrc =
            "vendor/pdf.worker.min.js";
        } catch (e) {}
        ok(window.pdfjsLib);
      };
      s.onerror = function () { bad(); };
      document.head.appendChild(s);
    });
    return pdfjsPromise;
  }

  function pdfPreview(blob, box, url) {
    var wrap = document.createElement("div");
    wrap.className = "dplr-pages";
    box.appendChild(wrap);
    ensurePdfJs().then(function (lib) {
      return blob.arrayBuffer().then(function (buf) {
        return lib.getDocument({ data: buf }).promise;
      }).then(function (pdf) {
        var max = Math.min(pdf.numPages, 12), chain = Promise.resolve();
        for (var i = 1; i <= max; i++) {
          (function (n) {
            chain = chain.then(function () {
              return pdf.getPage(n).then(function (page) {
                var w = wrap.clientWidth || 640;
                var v0 = page.getViewport({ scale: 1 });
                var vp = page.getViewport({ scale: Math.min(2, w / v0.width) });
                var c = document.createElement("canvas");
                c.width = vp.width; c.height = vp.height;
                wrap.appendChild(c);
                return page.render({ canvasContext: c.getContext("2d"), viewport: vp }).promise;
              });
            });
          })(i);
        }
        return chain.then(function () {
          if (pdf.numPages > max) {
            var more = document.createElement("p");
            more.className = "dplr-more";
            more.textContent = "+ " + (pdf.numPages - max) + " more pages in the file";
            wrap.appendChild(more);
          }
        });
      });
    }).catch(function () {
      /* no preview possible (e.g. the file is password-protected) */
      wrap.innerHTML = "";
      var note = document.createElement("p");
      note.className = "dplr-note";
      note.textContent = "Preview is not available for this file.";
      var link = document.createElement("a");
      link.href = url; link.target = "_blank"; link.rel = "noopener";
      link.className = "dplr-open"; link.textContent = "Open in a new tab";
      wrap.appendChild(note); wrap.appendChild(link);
    });
  }

  /* items: [{blob, name}] */
  function show(items, title) {
    if (!items || !items.length) return;
    var urls = [];

    var mask = document.createElement("div");
    mask.className = "dplr-mask";
    var box = document.createElement("div");
    box.className = "dplr";
    mask.appendChild(box);

    var top = document.createElement("div");
    top.className = "dplr-top";
    var h = document.createElement("h3");
    h.textContent = title || (items.length > 1 ? "Your files are ready" : "Your file is ready");
    var x = document.createElement("button");
    x.className = "dplr-x"; x.textContent = "✕"; x.title = "Close";
    top.appendChild(h); top.appendChild(x);

    var body = document.createElement("div");
    body.className = "dplr-body";
    var prev = document.createElement("div");
    prev.className = "dplr-prev";
    body.appendChild(prev);

    var rows = [];
    function render(i) {
      var it = items[i];
      rows.forEach(function (r, k) { r.classList.toggle("on", k === i); });
      prev.innerHTML = "";
      if (!urls[i]) urls[i] = URL.createObjectURL(it.blob);
      var type = it.blob.type || "";
      if (/pdf/.test(type) || /\.pdf$/i.test(it.name)) {
        pdfPreview(it.blob, prev, urls[i]);
      } else if (/^image\//.test(type)) {
        var im = document.createElement("img");
        im.src = urls[i];
        prev.appendChild(im);
      } else if (/text|msword|json/.test(type)) {
        var pre = document.createElement("pre");
        it.blob.slice(0, 20000).text().then(function (t) {
          pre.textContent = t.replace(/<[^>]+>/g, " ").replace(/\s+\n/g, "\n").slice(0, 4000);
        }).catch(function () { pre.textContent = ""; });
        prev.appendChild(pre);
      } else {
        prev.style.display = "none";
      }
    }

    items.forEach(function (it, i) {
      var row = document.createElement("div");
      row.className = "dplr-row";
      var pick = document.createElement("button");
      pick.className = "dplr-pick";
      var nm = document.createElement("span");
      nm.className = "nm"; nm.textContent = it.name;
      var sz = document.createElement("span");
      sz.className = "sz"; sz.textContent = kb(it.blob.size);
      pick.appendChild(nm); pick.appendChild(sz);
      pick.onclick = function () { render(i); };
      var dlb = document.createElement("button");
      dlb.className = "dplr-btn"; dlb.textContent = canShare([asFile(it.blob, it.name)]) ? T("Save / Share") : "Download";
      dlb.onclick = function () { saveSmart(it.blob, it.name); };
      row.appendChild(pick); row.appendChild(dlb);
      body.appendChild(row);
      rows.push(row);
    });

    var foot = document.createElement("div");
    foot.className = "dplr-foot";
    if (items.length > 1) {
      var all = document.createElement("button");
      all.className = "dplr-btn";
      var allFiles = items.map(function (it) { return asFile(it.blob, it.name); });
      var shareAll = canShare(allFiles);
      all.textContent = shareAll ? T("Save / Share all") : "Download all";
      all.onclick = function () {
        if (shareAll) {
          navigator.share({ files: allFiles }).catch(function () {});
          return;
        }
        items.forEach(function (it, i) {
          setTimeout(function () { saveBlob(it.blob, it.name); }, i * 450);
        });
      };
      foot.appendChild(all);
    }
    var close = document.createElement("button");
    close.className = "dplr-btn ghost";
    close.textContent = "Close";
    foot.appendChild(close);

    box.appendChild(top); box.appendChild(body); box.appendChild(foot);
    document.body.appendChild(mask);
    render(0);

    function bye() {
      mask.remove();
      urls.forEach(function (u) { if (u) URL.revokeObjectURL(u); });
      document.removeEventListener("keydown", esc);
    }
    function esc(e) { if (e.key === "Escape") bye(); }
    x.onclick = bye; close.onclick = bye;
    mask.onclick = function (e) { if (e.target === mask) bye(); };
    document.addEventListener("keydown", esc);
  }

  window.DPLResult = {
    show: show,
    /* convenience: bytes/blob + name, with an optional mime type */
    file: function (data, name, type) {
      var blob = (data instanceof Blob) ? data : new Blob([data], { type: type || guess(name) });
      show([{ blob: blob, name: name }]);
    },
    files: function (list, title) { show(list, title); },
    save: saveSmart
  };

  function guess(name) {
    if (/\.pdf$/i.test(name)) return "application/pdf";
    if (/\.png$/i.test(name)) return "image/png";
    if (/\.jpe?g$/i.test(name)) return "image/jpeg";
    if (/\.txt$/i.test(name)) return "text/plain;charset=utf-8";
    if (/\.docx?$/i.test(name)) return "application/msword";
    return "application/octet-stream";
  }
})();
