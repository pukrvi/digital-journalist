#!/usr/bin/env python3
"""Verify every script's dependencies are installed and wired up. Prints a status table."""
import importlib
import shutil
import sys
import os

PY_MODULES = [
    ("ddgs", "DuckDuckGo search"),
    ("trafilatura", "Clean article extraction"),
    ("wikipediaapi", "Wikipedia"),
    ("arxiv", "Arxiv papers"),
    ("feedparser", "RSS/Atom feeds"),
    ("pdfplumber", "PDF text + tables"),
    ("fitz", "PDF + images (pymupdf)"),
    ("docx", "DOCX (python-docx)"),
    ("openpyxl", "XLSX"),
    ("pptx", "PPTX (python-pptx)"),
    ("ebooklib", "EPUB"),
    ("chardet", "Encoding detection"),
    ("magic", "File type (python-magic)"),
    ("pandas", "Data frames"),
    ("numpy", "Array math"),
    ("scipy", "Statistics"),
    ("PIL", "Pillow images"),
    ("pdf2image", "PDF page rendering"),
    ("markdownify", "HTML to Markdown"),
    ("ffmpeg", "ffmpeg-python wrapper"),
    ("yt_dlp", "Video download"),
    ("newspaper", "newspaper3k"),
    ("pypdf", "PDF basic"),
]

CLI_TOOLS = [
    ("ffmpeg", "Audio/video processing"),
    ("whisper-cli", "Transcription (whisper.cpp)"),
    ("ddgs", "DuckDuckGo CLI"),
    ("trafilatura", "Article extraction CLI"),
    ("yt-dlp", "Video download CLI"),
    ("rg", "ripgrep (corpus_search)"),
    ("jq", "JSON processing"),
]

WHISPER_MODELS = [
    "ggml-tiny.en.bin",
    "ggml-base.en.bin",
    "ggml-small.en.bin",
    "ggml-medium.en.bin",
    "ggml-large-v3.bin",
]


def status(ok):
    return "[OK]   " if ok else "[MISS] "


PY_USER_BIN = os.path.expanduser("~/Library/Python/3.9/bin")


def which(tool):
    """shutil.which, but also check the Python user-bin since the parent shell may not have it on PATH yet."""
    p = shutil.which(tool)
    if p:
        return p
    fallback = os.path.join(PY_USER_BIN, tool)
    return fallback if os.path.isfile(fallback) and os.access(fallback, os.X_OK) else None


def main():
    print("=" * 60)
    print("Python modules:")
    print("=" * 60)
    missing_py = []
    for mod, desc in PY_MODULES:
        try:
            importlib.import_module(mod)
            print(f"{status(True)}{mod:<18} {desc}")
        except ImportError:
            missing_py.append(mod)
            print(f"{status(False)}{mod:<18} {desc}")
        except Exception as e:
            missing_py.append(f"{mod} (broken: {type(e).__name__})")
            print(f"{status(False)}{mod:<18} {desc}  -- import error: {type(e).__name__}: {e}")

    print("\n" + "=" * 60)
    print("CLI tools:")
    print("=" * 60)
    missing_cli = []
    for tool, desc in CLI_TOOLS:
        path = which(tool)
        if path:
            print(f"{status(True)}{tool:<18} {desc} ({path})")
        else:
            missing_cli.append(tool)
            print(f"{status(False)}{tool:<18} {desc}")

    print("\n" + "=" * 60)
    print("Whisper models:")
    print("=" * 60)
    models_dir = os.path.expanduser("~/.whisper-models")
    if not os.path.isdir(models_dir):
        print(f"{status(False)}~/.whisper-models/ does not exist")
    else:
        any_model = False
        for m in WHISPER_MODELS:
            p = os.path.join(models_dir, m)
            if os.path.isfile(p):
                size_mb = os.path.getsize(p) / 1024 / 1024
                print(f"{status(True)}{m:<24} ({size_mb:.0f} MB)")
                any_model = True
        if not any_model:
            print(f"{status(False)}No models found. Run scripts/setup.sh to download base.en.")

    print("\n" + "=" * 60)
    if missing_py:
        print(f"Missing Python: {', '.join(missing_py)}")
        print(f"  Install: python3 -m pip install --user {' '.join(missing_py)}")
    if missing_cli:
        print(f"Missing CLI: {', '.join(missing_cli)}")
    if not missing_py and not missing_cli:
        print("All required tools are installed.")
    print("=" * 60)
    sys.exit(0 if not (missing_py or missing_cli) else 1)


if __name__ == "__main__":
    main()
