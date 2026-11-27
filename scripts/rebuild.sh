#!/bin/sh
# Rebuild generated parts of the site in the right order.
set -e
cd "$(dirname "$0")/.."
python3 scripts/newtools/make.py site
python3 scripts/guides/apply.py site > /dev/null
python3 scripts/guides/build_articles.py site > /dev/null
python3 scripts/cleanlinks.py site
