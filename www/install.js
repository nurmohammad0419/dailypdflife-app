/* DailyPdfLife: install the site as an app.
   iPhone/iPad: shows how to "Add to Home Screen" (Safari has no install button).
   Android/computer: uses the browser's own install prompt, and offers the Android app.
   Also turns on the offline cache (sw.js). Does nothing inside the Android app. */
(function () {
  if (window.DPLNative || (window.Capacitor && window.Capacitor.isNativePlatform && window.Capacitor.isNativePlatform())) return;

  if ("serviceWorker" in navigator && (location.protocol === "https:" || location.hostname === "localhost" || location.hostname === "127.0.0.1")) {
    window.addEventListener("load", function () { navigator.serviceWorker.register("sw.js").catch(function () {}); });
  }

  var T = function (s) { return window.T ? window.T(s) : s; };
  var ua = navigator.userAgent;
  var IOS = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  var ANDROID = /Android/.test(ua);
  var standalone = (window.matchMedia && matchMedia("(display-mode: standalone)").matches) || navigator.standalone === true;
  if (standalone) { document.documentElement.classList.add("standalone"); return; }

  var deferred = null;
  var APK = "https://github.com/nurmohammad0419/dailypdflife-app/releases/latest";
  var KEY = "dpl_install_hide";
  function hiddenRecently() { try { return Date.now() - Number(localStorage.getItem(KEY) || 0) < 14 * 864e5; } catch (e) { return false; } }
  function hideForAWhile() { try { localStorage.setItem(KEY, Date.now()); } catch (e) {} }

  var css = document.createElement("style");
  css.textContent = [
    ".dpli-btn{border:1px solid var(--line,#e3e6ee);background:#fff;color:#1b2030;border-radius:10px;padding:7px 11px;font-size:13px;font-weight:700;cursor:pointer;display:none;align-items:center;gap:6px;font-family:inherit}",
    ".dpli-btn.show{display:inline-flex}",
    "@media(max-width:520px){.dpli-btn b{display:none}}",
    ".dpli-ban{position:fixed;left:12px;right:12px;bottom:14px;z-index:11000;background:#fff;border:1px solid #e3e6ee;border-radius:16px;",
    "box-shadow:0 14px 40px rgba(16,20,30,.22);padding:14px;display:flex;gap:12px;align-items:center;font:14px/1.4 system-ui,-apple-system,'Segoe UI',sans-serif;",
    "max-width:520px;margin:0 auto;animation:dpliup .3s ease}",
    "@keyframes dpliup{from{transform:translateY(120%)}}",
    ".dpli-ban img{width:46px;height:46px;border-radius:11px;flex:none}",
    ".dpli-ban .t{flex:1;min-width:0;color:#2b2f3a}.dpli-ban .t b{display:block;font-size:15px;color:#1b2030}",
    ".dpli-ban .go{background:#e5322d;color:#fff;border:0;border-radius:10px;padding:10px 14px;font-weight:700;font-size:14px;flex:none;font-family:inherit}",
    ".dpli-ban .x{background:none;border:0;color:#8b90a0;font-size:18px;padding:4px;flex:none}",
    ".dpli-mask{position:fixed;inset:0;z-index:12500;background:rgba(16,20,30,.55);display:flex;align-items:flex-end;justify-content:center;",
    "font:15px/1.45 system-ui,-apple-system,'Segoe UI',sans-serif}",
    ".dpli-box{background:#fff;border-radius:20px 20px 0 0;width:100%;max-width:520px;padding:20px 20px 28px;max-height:90vh;overflow:auto}",
    "@media(min-width:600px){.dpli-mask{align-items:center}.dpli-box{border-radius:20px}}",
    ".dpli-box h3{margin:0 0 4px;font-size:19px;color:#1b2030}",
    ".dpli-box p.s{margin:0 0 16px;color:#6b7283;font-size:14px}",
    ".dpli-step{display:flex;gap:12px;align-items:flex-start;padding:12px 0;border-top:1px solid #eef0f4}",
    ".dpli-step i{font-style:normal;flex:none;width:28px;height:28px;border-radius:50%;background:#1b2030;color:#fff;font-weight:800;",
    "display:flex;align-items:center;justify-content:center;font-size:14px}",
    ".dpli-step b{color:#1b2030}",
    ".dpli-ico{display:inline-flex;vertical-align:middle;width:26px;height:26px;border-radius:7px;background:#f2f4f9;align-items:center;justify-content:center;margin:0 3px}",
    ".dpli-ico svg{width:17px;height:17px}",
    ".dpli-box .row{display:flex;gap:10px;margin-top:16px;flex-wrap:wrap}",
    ".dpli-box .row a,.dpli-box .row button{flex:1;text-align:center;border-radius:12px;padding:12px;font-weight:700;font-size:15px;text-decoration:none;border:0;font-family:inherit;cursor:pointer}",
    ".dpli-box .pri{background:#e5322d;color:#fff}.dpli-box .sec{background:#f2f4f9;color:#1b2030}",
    ".dpli-arrow{position:fixed;bottom:6px;left:50%;transform:translateX(-50%);z-index:12600;font-size:34px;animation:dplib 1s infinite alternate;pointer-events:none}",
    "@keyframes dplib{to{transform:translate(-50%,8px)}}"
  ].join("");
  document.head.appendChild(css);

  var SHARE = '<svg viewBox="0 0 24 24" fill="none" stroke="#1971c2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="M8 7l4-4 4 4"/><path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-7"/></svg>';
  var ADD = '<svg viewBox="0 0 24 24" fill="none" stroke="#1b2030" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/></svg>';

  function close(m) { if (m) m.remove(); var a = document.querySelector(".dpli-arrow"); if (a) a.remove(); }
  function sheet(html) {
    var m = document.createElement("div"); m.className = "dpli-mask";
    m.innerHTML = '<div class="dpli-box">' + html + "</div>";
    m.onclick = function (e) { if (e.target === m || (e.target.dataset && e.target.dataset.close)) close(m); };
    document.body.appendChild(m);
    return m;
  }
  function iosGuide() {
    var safari = !/CriOS|FxiOS|EdgiOS/.test(ua);
    var where = safari
      ? (/iPad/.test(ua) || navigator.maxTouchPoints > 1 && !/iPhone/.test(ua) ? T("at the top right of Safari") : T("at the bottom of Safari"))
      : T("in the browser menu");
    sheet(
      "<h3>📲 " + T("Add DailyPdfLife to your Home Screen") + "</h3>" +
      '<p class="s">' + T("It opens full screen like an app, works offline and keeps your files on your phone.") + "</p>" +
      '<div class="dpli-step"><i>1</i><div>' + T("Tap the Share button") + ' <span class="dpli-ico">' + SHARE + "</span> " + where + ".</div></div>" +
      '<div class="dpli-step"><i>2</i><div>' + T("Scroll down and tap") + ' <span class="dpli-ico">' + ADD + "</span> <b>" + T("Add to Home Screen") + "</b>.</div></div>" +
      '<div class="dpli-step"><i>3</i><div>' + "<b>" + T("Tap Add at the top right.") + "</b> " + T("The DailyPdfLife icon appears on your Home Screen.") + "</div></div>" +
      '<div class="row"><button class="sec" data-close="1">' + T("Got it") + "</button></div>"
    );
  }
  function androidChoice() {
    var m = sheet(
      "<h3>📲 " + T("Get DailyPdfLife on your phone") + "</h3>" +
      '<p class="s">' + T("The Android app can open PDFs from WhatsApp and your files, and has a smart document scanner.") + "</p>" +
      '<div class="row"><a class="pri" href="' + APK + '" target="_blank" rel="noopener">⬇ ' + T("Android app") + "</a>" +
      (deferred ? '<button class="sec" id="dpliWeb">' + T("Install web app") + "</button>" : "") + "</div>"
    );
    var w = m.querySelector("#dpliWeb");
    if (w) w.onclick = function () { close(m); promptInstall(); };
  }
  function promptInstall() {
    if (!deferred) return;
    deferred.prompt();
    deferred.userChoice.finally(function () { deferred = null; refresh(); });
  }
  function onClick() {
    if (IOS) iosGuide();
    else if (ANDROID) androidChoice();
    else promptInstall();
  }

  var btn = null;
  function refresh() {
    if (!btn) return;
    btn.classList.toggle("show", IOS || ANDROID || !!deferred);
  }
  window.addEventListener("beforeinstallprompt", function (e) { e.preventDefault(); deferred = e; refresh(); });
  window.addEventListener("appinstalled", function () { deferred = null; if (btn) btn.classList.remove("show"); });

  function mount() {
    var bar = document.querySelector(".appbar");
    if (bar) {
      btn = document.createElement("button");
      btn.className = "dpli-btn"; btn.type = "button";
      btn.innerHTML = "📲 <b>" + T("Install app") + "</b>";
      btn.title = T("Install app");
      btn.onclick = onClick;
      var lang = bar.querySelector(".ptlang");
      bar.insertBefore(btn, lang || null);
      refresh();
    }
    /* a gentle banner on the home page for iPhone users, at most every two weeks */
    var page = (location.pathname.split("/").pop() || "index.html").toLowerCase();
    if (IOS && (page === "index.html" || page === "") && !hiddenRecently()) {
      setTimeout(function () {
        var b = document.createElement("div"); b.className = "dpli-ban";
        b.innerHTML = '<img src="apple-touch-icon.png" alt=""><div class="t"><b>' + T("Use DailyPdfLife like an app") +
          "</b>" + T("Add it to your Home Screen. Free, no App Store needed.") + '</div><button class="go">' + T("How?") +
          '</button><button class="x" aria-label="Close">✕</button>';
        b.querySelector(".go").onclick = function () { b.remove(); hideForAWhile(); iosGuide(); };
        b.querySelector(".x").onclick = function () { b.remove(); hideForAWhile(); };
        document.body.appendChild(b);
      }, 2500);
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { setTimeout(mount, 0); });
  else setTimeout(mount, 0);
})();
