# DailyPdfLife Android app

The DailyPdfLife website (https://dailypdflife.com) packed as an Android app with:

- **PDF viewer**: PDFs from file managers, WhatsApp, Gmail and downloads open straight in the app.
- **Smart document scanner**: Google's ML Kit scanner finds the page edges, takes the shot by itself,
  straightens and cleans the page, then the pages become one PDF.
- **All 48 tools** of the website, working offline except Remove background and OCR (they download their AI models).
- Finished files are saved to `Download/DailyPdfLife` and can be opened or shared right away.

## How it is built

Every push to `main` builds the app on GitHub Actions (`.github/workflows/build-apk.yml`).
The APK appears under **Releases → latest → DailyPdfLife.apk**.

To update the app after changing the website:

```
python3 scripts/build_www.py <path-to-website-folder>
git add -A && git commit -m "Update app" && git push
```

## Folders

- `www/` – the website, prepared for the app (built by `scripts/build_www.py`)
- `web-extra/` – app-only script (`app-shell.js`) and offline copies of the libraries
- `android/` – the Android project (Capacitor 8). Native code is in `MainActivity.java`.
