/* DailyPdfLife — a draggable, resizable crop rectangle.
   new DPLCrop(host, {ratio, onchange}) — host must be position:relative and
   exactly cover the picture. Values are fractions (0..1) of the host size. */
(function () {
  var css = document.createElement("style");
  css.textContent = [
    ".dplcrop{position:absolute;border:2px solid #fff;box-shadow:0 0 0 9999px rgba(15,18,28,.52);",
    "cursor:move;touch-action:none;box-sizing:border-box}",
    ".dplcrop i{position:absolute;width:16px;height:16px;background:#fff;border-radius:4px;",
    "box-shadow:0 1px 4px rgba(0,0,0,.4)}",
    ".dplcrop i.nw{left:-9px;top:-9px;cursor:nwse-resize}",
    ".dplcrop i.ne{right:-9px;top:-9px;cursor:nesw-resize}",
    ".dplcrop i.sw{left:-9px;bottom:-9px;cursor:nesw-resize}",
    ".dplcrop i.se{right:-9px;bottom:-9px;cursor:nwse-resize}",
    ".dplcrop b{position:absolute;background:rgba(255,255,255,.45);pointer-events:none}",
    ".dplcrop b.v1{left:33.3%;top:0;bottom:0;width:1px}.dplcrop b.v2{left:66.6%;top:0;bottom:0;width:1px}",
    ".dplcrop b.h1{top:33.3%;left:0;right:0;height:1px}.dplcrop b.h2{top:66.6%;left:0;right:0;height:1px}"
  ].join("");
  document.head.appendChild(css);

  window.DPLCrop = function (host, opts) {
    opts = opts || {};
    var ratio = opts.ratio || 0;                 /* width / height in pixels, 0 = free */
    var r = { x: 0.06, y: 0.06, w: 0.88, h: 0.88 };
    var box = document.createElement("div");
    box.className = "dplcrop";
    box.innerHTML = '<i class="nw"></i><i class="ne"></i><i class="sw"></i><i class="se"></i>' +
                    '<b class="v1"></b><b class="v2"></b><b class="h1"></b><b class="h2"></b>';
    host.appendChild(box);

    function W() { return host.clientWidth || 1; }
    function H() { return host.clientHeight || 1; }
    function clamp() {
      var min = 0.03;
      r.w = Math.max(min, Math.min(1, r.w)); r.h = Math.max(min, Math.min(1, r.h));
      r.x = Math.max(0, Math.min(1 - r.w, r.x)); r.y = Math.max(0, Math.min(1 - r.h, r.y));
    }
    function draw(silent) {
      box.style.left = r.x * W() + "px"; box.style.top = r.y * H() + "px";
      box.style.width = r.w * W() + "px"; box.style.height = r.h * H() + "px";
      if (!silent && opts.onchange) opts.onchange(api.get());
    }
    function applyRatio(center) {
      if (!ratio) return;
      var cx = r.x + r.w / 2, cy = r.y + r.h / 2;
      var hFromW = r.w * W() / ratio / H();
      if (hFromW <= 1) { r.h = hFromW; }
      else { r.h = 1; r.w = ratio * H() / W(); }
      if (r.w > 1) { r.w = 1; r.h = W() / ratio / H(); }
      if (center) { r.x = cx - r.w / 2; r.y = cy - r.h / 2; }
      clamp();
    }

    box.addEventListener("pointerdown", function (ev) {
      ev.preventDefault();
      var handle = ev.target.tagName === "I" ? ev.target.className : "";
      var o = { x: r.x, y: r.y, w: r.w, h: r.h }, sx = ev.clientX, sy = ev.clientY;
      box.setPointerCapture(ev.pointerId);
      function move(e) {
        var dx = (e.clientX - sx) / W(), dy = (e.clientY - sy) / H();
        if (!handle) { r.x = o.x + dx; r.y = o.y + dy; clamp(); draw(); return; }
        var L = o.x, T = o.y, R = o.x + o.w, B = o.y + o.h;
        if (/w/.test(handle)) L = Math.min(R - 0.03, Math.max(0, o.x + dx));
        if (/e/.test(handle)) R = Math.max(L + 0.03, Math.min(1, R + dx));
        if (/n/.test(handle)) T = Math.min(B - 0.03, Math.max(0, o.y + dy));
        if (/s/.test(handle)) B = Math.max(T + 0.03, Math.min(1, B + dy));
        r.x = L; r.y = T; r.w = R - L; r.h = B - T;
        if (ratio) {
          var h2 = r.w * W() / ratio / H();
          if (/n/.test(handle)) r.y = B - h2;
          r.h = h2;
          if (r.y < 0 || r.y + r.h > 1) {          /* too tall: shrink width instead */
            var maxH = /n/.test(handle) ? B : 1 - T;
            r.h = maxH; r.w = r.h * H() * ratio / W();
            if (/w/.test(handle)) r.x = R - r.w;
            r.y = /n/.test(handle) ? B - r.h : T;
          }
        }
        clamp(); draw();
      }
      function up() {
        box.removeEventListener("pointermove", move);
        box.removeEventListener("pointerup", up);
        box.removeEventListener("pointercancel", up);
      }
      box.addEventListener("pointermove", move);
      box.addEventListener("pointerup", up);
      box.addEventListener("pointercancel", up);
    });

    var api = {
      get: function () { return { x: r.x, y: r.y, w: r.w, h: r.h }; },
      set: function (f) { r = { x: f.x, y: f.y, w: f.w, h: f.h }; clamp(); applyRatio(true); draw(); },
      setRatio: function (k) { ratio = k || 0; applyRatio(true); draw(); },
      reset: function () { r = { x: 0.06, y: 0.06, w: 0.88, h: 0.88 }; applyRatio(true); draw(); },
      redraw: function () { draw(true); },
      destroy: function () { box.remove(); }
    };
    applyRatio(true); draw(true);
    window.addEventListener("resize", function () { draw(true); });
    return api;
  };
})();
