package com.dailypdflife.app;

import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Intent;
import android.database.Cursor;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.print.PrintAttributes;
import android.print.PrintDocumentAdapter;
import android.print.PrintManager;
import android.provider.MediaStore;
import android.provider.OpenableColumns;
import android.util.Base64;
import android.webkit.JavascriptInterface;
import android.webkit.WebView;
import android.widget.Toast;

import androidx.activity.OnBackPressedCallback;
import androidx.core.content.FileProvider;

import com.getcapacitor.BridgeActivity;

import org.json.JSONObject;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Map;

/**
 * DailyPdfLife: the web tools run inside Capacitor's WebView. This activity adds
 *  - opening PDFs that other apps send here (file managers, WhatsApp, Gmail ...)
 *  - saving finished files into Download/DailyPdfLife, opening and sharing them
 *  - "Save as PDF" through Android's print service
 *  - the Android back button
 */
public class MainActivity extends BridgeActivity {

    private final Map<String, File> pending = new HashMap<>();
    private final Map<String, String[]> pendingInfo = new HashMap<>();   // name, mime, toDownloads
    private int nextId = 1;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        WebView wv = bridge.getWebView();
        wv.addJavascriptInterface(new NativeApi(), "DPLNative");

        getOnBackPressedDispatcher().addCallback(this, new OnBackPressedCallback(true) {
            @Override
            public void handleOnBackPressed() {
                WebView w = bridge.getWebView();
                w.evaluateJavascript("(window.DPLApp && DPLApp.back && DPLApp.back()) || ''", value -> {
                    if (value != null && value.contains("handled")) return;
                    if (w.canGoBack()) w.goBack();
                    else finish();
                });
            }
        });

        handleIncoming(getIntent());
    }

    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        setIntent(intent);
        handleIncoming(intent);
    }

    /* ---------- PDFs opened from other apps ---------- */

    private void handleIncoming(Intent intent) {
        if (intent == null) return;
        Uri uri = null;
        String action = intent.getAction();
        if (Intent.ACTION_VIEW.equals(action)) {
            uri = intent.getData();
        } else if (Intent.ACTION_SEND.equals(action)) {
            uri = intent.getParcelableExtra(Intent.EXTRA_STREAM);
        }
        if (uri == null) return;
        final Uri src = uri;
        intent.setAction(Intent.ACTION_MAIN);           // don't open it again on rotation
        new Thread(() -> {
            try {
                String name = displayName(src);
                if (name == null || name.isEmpty()) name = "document.pdf";
                if (!name.toLowerCase().endsWith(".pdf")) name = name + ".pdf";
                File dir = new File(getCacheDir(), "incoming");
                dir.mkdirs();
                File[] old = dir.listFiles();
                if (old != null) for (File f : old) f.delete();
                File out = new File(dir, name.replaceAll("[\\\\/:*?\"<>|]", "_"));
                try (InputStream in = getContentResolver().openInputStream(src);
                     OutputStream os = new FileOutputStream(out)) {
                    if (in == null) throw new Exception("no stream");
                    byte[] buf = new byte[65536];
                    int n;
                    while ((n = in.read(buf)) > 0) os.write(buf, 0, n);
                }
                final String url = bridge.getLocalUrl() + "/pdf-viewer.html?src="
                        + URLEncoder.encode("/_capacitor_file_" + out.getAbsolutePath(), "UTF-8")
                        + "&name=" + URLEncoder.encode(name, "UTF-8");
                runOnUiThread(() -> bridge.getWebView().loadUrl(url));
            } catch (Exception e) {
                runOnUiThread(() -> Toast.makeText(this, "This file could not be opened", Toast.LENGTH_LONG).show());
            }
        }).start();
    }

    private String displayName(Uri uri) {
        if ("file".equals(uri.getScheme())) return new File(uri.getPath()).getName();
        try (Cursor c = getContentResolver().query(uri, new String[]{OpenableColumns.DISPLAY_NAME}, null, null, null)) {
            if (c != null && c.moveToFirst()) return c.getString(0);
        } catch (Exception ignored) { }
        return null;
    }

    /* ---------- bridge for the web pages ---------- */

    private class NativeApi {

        /** start a file; chunks of base64 follow */
        @JavascriptInterface
        public String begin(String name, String mime, boolean toDownloads) {
            try {
                String id = String.valueOf(nextId++);
                File dir = new File(getCacheDir(), "out");
                dir.mkdirs();
                File f = new File(dir, id + "_" + name.replaceAll("[\\\\/:*?\"<>|]", "_"));
                new FileOutputStream(f).close();
                pending.put(id, f);
                pendingInfo.put(id, new String[]{name, mime, toDownloads ? "1" : "0"});
                return id;
            } catch (Exception e) {
                return "";
            }
        }

        @JavascriptInterface
        public void chunk(String id, String b64) {
            File f = pending.get(id);
            if (f == null) return;
            try (OutputStream os = new FileOutputStream(f, true)) {
                os.write(Base64.decode(b64, Base64.DEFAULT));
            } catch (Exception ignored) { }
        }

        /** finish: copy into Download/DailyPdfLife (Android 10+) and return where it went */
        @JavascriptInterface
        public String finish(String id) {
            JSONObject r = new JSONObject();
            File f = pending.remove(id);
            String[] info = pendingInfo.remove(id);
            try {
                if (f == null || info == null) throw new Exception("unknown file");
                String name = info[0], mime = info[1];
                boolean toDownloads = "1".equals(info[2]);
                Uri uri = null;
                String where = "DailyPdfLife";
                if (toDownloads && Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                    ContentValues v = new ContentValues();
                    v.put(MediaStore.MediaColumns.DISPLAY_NAME, name);
                    v.put(MediaStore.MediaColumns.MIME_TYPE, mime);
                    v.put(MediaStore.MediaColumns.RELATIVE_PATH, Environment.DIRECTORY_DOWNLOADS + "/DailyPdfLife");
                    ContentResolver cr = getContentResolver();
                    uri = cr.insert(MediaStore.Downloads.EXTERNAL_CONTENT_URI, v);
                    if (uri != null) {
                        try (InputStream in = new FileInputStream(f); OutputStream os = cr.openOutputStream(uri)) {
                            byte[] buf = new byte[65536];
                            int n;
                            while ((n = in.read(buf)) > 0) os.write(buf, 0, n);
                        }
                        try (Cursor c = cr.query(uri, new String[]{MediaStore.MediaColumns.DISPLAY_NAME}, null, null, null)) {
                            if (c != null && c.moveToFirst()) name = c.getString(0);
                        } catch (Exception ignored) { }
                        where = "Download/DailyPdfLife";
                        f.delete();
                    }
                }
                if (uri == null) {
                    /* older Android, or only sharing: keep the file in the app and share it from there */
                    File keep = new File(new File(getExternalFilesDir(null) != null ? getExternalFilesDir(null) : getFilesDir(), "Saved"), name);
                    keep.getParentFile().mkdirs();
                    if (keep.exists()) keep.delete();
                    if (!f.renameTo(keep)) throw new Exception("could not keep file");
                    uri = FileProvider.getUriForFile(MainActivity.this, getPackageName() + ".fileprovider", keep);
                    where = "DailyPdfLife";
                }
                r.put("ok", true);
                r.put("uri", uri.toString());
                r.put("name", name);
                r.put("where", where);
            } catch (Exception e) {
                try { r.put("ok", false); r.put("error", String.valueOf(e.getMessage())); } catch (Exception ignored) { }
            }
            return r.toString();
        }

        @JavascriptInterface
        public void openUri(String uri, String mime) {
            runOnUiThread(() -> {
                try {
                    Intent i = new Intent(Intent.ACTION_VIEW);
                    i.setDataAndType(Uri.parse(uri), mime);
                    i.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
                    startActivity(Intent.createChooser(i, "Open with"));
                } catch (Exception e) {
                    Toast.makeText(MainActivity.this, "No app can open this file", Toast.LENGTH_LONG).show();
                }
            });
        }

        @JavascriptInterface
        public void shareUri(String uri, String mime) {
            runOnUiThread(() -> {
                try {
                    Intent i = new Intent(Intent.ACTION_SEND);
                    i.setType(mime);
                    i.putExtra(Intent.EXTRA_STREAM, Uri.parse(uri));
                    i.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
                    startActivity(Intent.createChooser(i, "Share"));
                } catch (Exception e) {
                    Toast.makeText(MainActivity.this, "Could not share this file", Toast.LENGTH_LONG).show();
                }
            });
        }

        /** "Save as PDF" pages: Android's print dialog has a Save as PDF printer */
        @JavascriptInterface
        public void print(String title) {
            runOnUiThread(() -> {
                try {
                    PrintManager pm = (PrintManager) getSystemService(PRINT_SERVICE);
                    String name = (title == null || title.isEmpty()) ? "DailyPdfLife" : title;
                    PrintDocumentAdapter a = bridge.getWebView().createPrintDocumentAdapter(name);
                    pm.print(name, a, new PrintAttributes.Builder().setMediaSize(PrintAttributes.MediaSize.ISO_A4).build());
                } catch (Exception e) {
                    Toast.makeText(MainActivity.this, "Printing is not available", Toast.LENGTH_LONG).show();
                }
            });
        }
    }
}
