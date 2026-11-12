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

The website itself lives in `site/`. Change files there and push: the app is rebuilt from it
(`scripts/build_www.py` runs during the build). `site/` can also be deployed to Cloudflare Pages
directly (build command: none, output directory: `site`).

## Folders

- `site/` – the DailyPdfLife website (also works as an iPhone web app: manifest, offline service worker)
- `www/` – the website, prepared for the app (built by `scripts/build_www.py`)
- `web-extra/` – app-only script (`app-shell.js`) and offline copies of the libraries
- `android/` – the Android project (Capacitor 8). Native code is in `MainActivity.java`.
