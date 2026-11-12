/* DailyPdfLife — runs qpdf (compiled to WebAssembly) inside the browser.
   Used by Unlock PDF and Protect PDF. Nothing leaves the device. */
(function () {
  var BASE = "vendor/qpdf/";
  var loading = null;

  function load() {
    if (window.Module && typeof window.Module === "function") return Promise.resolve();
    if (loading) return loading;
    loading = new Promise(function (ok, bad) {
      var s = document.createElement("script");
      s.src = BASE + "qpdf.js";
      s.onload = function () { ok(); };
      s.onerror = function () { loading = null; bad(new Error("qpdf could not be loaded")); };
      document.head.appendChild(s);
    });
    return loading;
  }

  /* args: qpdf command line using /in.pdf and /out.pdf
     returns {code, out (Uint8Array or null), log} */
  async function run(args, input) {
    await load();
    var log = [];
    var q = await window.Module({
      locateFile: function () { return BASE + "qpdf.wasm"; },
      noInitialRun: true,
      print: function (t) { log.push(String(t)); },
      printErr: function (t) { log.push(String(t)); }
    });
    q.FS.writeFile("/in.pdf", input instanceof Uint8Array ? input : new Uint8Array(input));
    var code = 0;
    try { code = q.callMain(args); }
    catch (e) { code = (e && typeof e.status === "number") ? e.status : 2; if (!(e && "status" in e)) log.push(String(e)); }
    var out = null;
    try { out = q.FS.readFile("/out.pdf"); } catch (e) {}
    return { code: code, out: out, log: log.join("\n") };
  }

  window.DPLqpdf = { run: run, load: load };
})();
