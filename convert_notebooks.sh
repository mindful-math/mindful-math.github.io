#!/usr/bin/env bash
# convert_notebooks.sh
#
# Run from any directory that contains .ipynb files.
# Converts every notebook to HTML and drops a wrapper + raw file
# into your site's notebooks/ folder.
#
# Usage:
#   ./convert_notebooks.sh                     # convert all .ipynb in current dir
#   ./convert_notebooks.sh my_notebook.ipynb   # convert one file
#   ./convert_notebooks.sh --site ~/my-site    # point to a non-default site root
#
# Requirements: Python 3, nbconvert  (pip install nbconvert)

set -euo pipefail

# ── Config (edit these two paths if your layout differs) ────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_ROOT="${SITE_ROOT:-$SCRIPT_DIR}"          # override with --site or $SITE_ROOT
NOTEBOOKS_DIR=""                               # resolved below
# ─────────────────────────────────────────────────────────────────────────────

usage() {
  echo "Usage: $0 [file.ipynb ...] [--site /path/to/site]"
  echo "       Run from a directory containing .ipynb files."
  exit 1
}

# Parse args
TARGETS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --site) SITE_ROOT="$2"; shift 2 ;;
    --help|-h) usage ;;
    *.ipynb) TARGETS+=("$1"); shift ;;
    *) echo "Unknown argument: $1"; usage ;;
  esac
done

# Resolve notebooks output dir
NOTEBOOKS_DIR="$SITE_ROOT/notebooks"

if [[ ! -d "$NOTEBOOKS_DIR" ]]; then
  echo "❌  Cannot find $NOTEBOOKS_DIR"
  echo "    Set --site to the root of your site, or run this script from site/"
  exit 1
fi

# Check nbconvert
if ! command -v jupyter &>/dev/null; then
  echo "❌  jupyter not found. Install with: pip install nbconvert"
  exit 1
fi

# If no specific files given, convert everything in current dir
if [[ ${#TARGETS[@]} -eq 0 ]]; then
  mapfile -t TARGETS < <(find . -maxdepth 1 -name "*.ipynb" | sort)
fi

if [[ ${#TARGETS[@]} -eq 0 ]]; then
  echo "No .ipynb files found in $(pwd)"
  exit 0
fi

echo "Site root : $SITE_ROOT"
echo "Output    : $NOTEBOOKS_DIR"
echo "Notebooks : ${#TARGETS[@]} file(s)"
echo ""

# ── Template for the wrapper page ───────────────────────────────────────────
wrapper_template() {
  local SLUG="$1"
  local TITLE="$2"
  local DATE="$3"
  cat <<HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${TITLE} · experiments · notebook</title>
  <link rel="stylesheet" href="../assets/css/main.css">
  <script>
    window.MathJax = {
      tex: { inlineMath: [['$','\$'],['\\\\(','\\\\)']], displayMath: [['$$','$$'],['\\\\[','\\\\]']] },
      options: { skipHtmlTags: ['script','noscript','style','textarea','pre'] }
    };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
</head>
<body>
<div class="site-wrap">

  <header>
    <nav>
      <a href="../index.html" class="site-title">ikigai</a>
      <a href="../notebooks/index.html">experiments</a>
      <a href="../thoughts/index.html">thoughts</a>
      <a href="../quotes/index.html">quotes</a>
      <a href="../books/index.html">books</a>
      <a href="../photos/index.html">photos</a>
    </nav>
  </header>

  <main>
    <div class="page-header">
      <h1>${TITLE}</h1>
      <p class="meta">${DATE}</p>
    </div>

    <div class="notebook-actions">
      <a class="btn" href="${SLUG}_raw.html" target="_blank">open full page ↗</a>
    </div>

    <iframe
      src="${SLUG}_raw.html"
      class="notebook-embed"
      title="${TITLE}"
      onload="fitIframe(this)"
      style="height: 85vh;">
    </iframe>
  </main>

  <footer>
    <span>built with plain html &amp; css · no framework</span>
    <a href="#">↑ top</a>
  </footer>

</div>
<script src="../assets/js/main.js"></script>
</body>
</html>
HTML
}

# ── Index entry snippet (printed for manual copy-paste) ─────────────────────
index_entry() {
  local SLUG="$1"
  local TITLE="$2"
  local DATE="$3"
  cat <<HTML
      <li>
        <a href="${SLUG}.html" class="entry-link">
          <span class="entry-title">${TITLE}</span>
          <span class="entry-tag">notebook</span>
          <span class="entry-date">${DATE}</span>
        </a>
      </li>
HTML
}

# ── Process each notebook ────────────────────────────────────────────────────
CONVERTED=()
SKIPPED=()

for NB in "${TARGETS[@]}"; do
  NB="${NB#./}"   # strip leading ./
  if [[ ! -f "$NB" ]]; then
    echo "⚠️  Not found: $NB — skipping"
    SKIPPED+=("$NB")
    continue
  fi

  BASENAME="$(basename "$NB" .ipynb)"
  SLUG="${BASENAME// /_}"   # spaces → underscores for safe filenames
  DATE="$(date +%Y-%m-%d)"
  TITLE="${BASENAME//_/ }"  # underscores → spaces for display title

  RAW_OUT="$NOTEBOOKS_DIR/${SLUG}_raw.html"
  WRAPPER_OUT="$NOTEBOOKS_DIR/${SLUG}.html"

  echo "▶  $NB"
  echo "   slug    : $SLUG"
  echo "   raw     : $RAW_OUT"
  echo "   wrapper : $WRAPPER_OUT"

  # Convert notebook → raw HTML
  jupyter nbconvert \
    --to html \
    --output "${SLUG}_raw" \
    --output-dir "$NOTEBOOKS_DIR" \
    "$NB" 2>&1 | sed 's/^/   nbconvert: /'

  # Write wrapper (only if it doesn't already exist — don't overwrite customised titles)
  if [[ -f "$WRAPPER_OUT" ]]; then
    echo "   wrapper exists — skipping (delete it to regenerate)"
  else
    wrapper_template "$SLUG" "$TITLE" "$DATE" > "$WRAPPER_OUT"
    echo "   wrapper written"
  fi

  CONVERTED+=("$SLUG")
  echo ""
done

# ── Summary ──────────────────────────────────────────────────────────────────
echo "════════════════════════════════════════"
echo "Converted : ${#CONVERTED[@]} notebook(s)"
[[ ${#SKIPPED[@]} -gt 0 ]] && echo "Skipped   : ${SKIPPED[*]}"
echo ""
echo "Add these entries to notebooks/index.html and index.html:"
echo ""
for SLUG in "${CONVERTED[@]}"; do
  DATE="$(date +%Y-%m-%d)"
  TITLE="${SLUG//_/ }"
  index_entry "$SLUG" "$TITLE" "$DATE"
done
echo "════════════════════════════════════════"
