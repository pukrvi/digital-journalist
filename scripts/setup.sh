#!/usr/bin/env bash
# One-shot setup for the Digital Journalist toolkit.
# Installs Python deps, ffmpeg (if missing), and the default whisper.cpp model.
# Idempotent — safe to re-run.
set -euo pipefail

PY_BIN="$HOME/Library/Python/3.9/bin"
WHISPER_MODELS="$HOME/.whisper-models"
DEFAULT_MODEL="ggml-base.en.bin"
MODEL_URL="https://huggingface.co/ggerganov/whisper.cpp/resolve/main/${DEFAULT_MODEL}?download=true"

echo "=== Digital Journalist setup ==="

# 1. Python packages
echo "[1/5] Installing Python packages..."
python3 -m pip install --user --quiet --upgrade \
  ddgs trafilatura wikipedia-api arxiv feedparser \
  pdfplumber pymupdf python-docx openpyxl python-pptx ebooklib \
  chardet python-magic pandas numpy scipy pdf2image Pillow \
  markdownify ffmpeg-python yt-dlp newspaper3k pypdf
echo "    done."

# 2. PATH check
if ! grep -q "Library/Python/3.9/bin" ~/.zshrc 2>/dev/null; then
  printf '\n# Added by Digital Journalist setup\nexport PATH="$HOME/Library/Python/3.9/bin:$PATH"\n' >> ~/.zshrc
  echo "[PATH] Added $PY_BIN to ~/.zshrc — restart your shell or run: export PATH=\"\$HOME/Library/Python/3.9/bin:\$PATH\""
fi

# 3. ffmpeg
echo "[2/5] Checking ffmpeg..."
if ! command -v ffmpeg >/dev/null 2>&1; then
  if command -v brew >/dev/null 2>&1; then
    echo "    installing via brew..."
    brew install ffmpeg
  else
    echo "    WARNING: ffmpeg missing and brew not found. Install ffmpeg manually."
  fi
else
  echo "    found: $(ffmpeg -version | head -1)"
fi

# 4. whisper.cpp
echo "[3/5] Checking whisper.cpp..."
if ! command -v whisper-cli >/dev/null 2>&1 && ! command -v whisper-cpp >/dev/null 2>&1; then
  if command -v brew >/dev/null 2>&1; then
    echo "    installing whisper-cpp via brew..."
    brew install whisper-cpp
  else
    echo "    WARNING: whisper-cpp missing and brew not found. transcribe.py won't work."
  fi
else
  echo "    found."
fi

# 5. ripgrep + jq (used by corpus_search.py and JSON pipelines respectively)
echo "[4/5] Checking ripgrep + jq..."
for tool in rg jq; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    if command -v brew >/dev/null 2>&1; then
      pkg="$tool"; [ "$tool" = "rg" ] && pkg="ripgrep"
      echo "    installing $pkg via brew..."
      brew install "$pkg"
    else
      echo "    WARNING: $tool missing and brew not found. Install it manually."
    fi
  else
    echo "    $tool found: $(command -v "$tool")"
  fi
done

# 6. Whisper model
echo "[5/5] Checking whisper model..."
mkdir -p "$WHISPER_MODELS"
if [[ ! -f "$WHISPER_MODELS/$DEFAULT_MODEL" ]]; then
  echo "    downloading $DEFAULT_MODEL (~147MB)..."
  curl -L --progress-bar -o "$WHISPER_MODELS/$DEFAULT_MODEL" "$MODEL_URL"
else
  echo "    found: $WHISPER_MODELS/$DEFAULT_MODEL ($(du -h "$WHISPER_MODELS/$DEFAULT_MODEL" | cut -f1))"
fi

echo
echo "=== Setup complete ==="
echo "Run 'python3 scripts/check_deps.py' to verify everything is wired up."
echo "For better transcription accuracy: download ggml-small.en.bin (488MB) or ggml-medium.en.bin (1.5GB) into $WHISPER_MODELS/"
