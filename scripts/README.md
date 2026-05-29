# scripts/

Reusable Python and shell scripts for the Digital Journalist. These are the heavy lifters — read formats, transcribe video, find patterns, crunch numbers.

For light-weight web search and URL fetching, see [`../tools/`](../tools/) (shell wrappers around `ddgs`, `trafilatura`, `wikipedia-api`, `arxiv`, `feedparser`).

## Quick reference

| Script | Purpose | Example |
|--------|---------|---------|
| **Setup** | | |
| `setup.sh` | Install all deps (Python, ffmpeg, whisper-cpp, whisper model) | `bash scripts/setup.sh` |
| `check_deps.py` | Verify what's installed | `python3 scripts/check_deps.py` |
| `detect_filetype.py` | Identify file via magic bytes | `scripts/detect_filetype.py mystery.bin` |
| **Reading formats** | | |
| `read_pdf.py` | PDF text + tables | `read_pdf.py report.pdf --pages 1-10 --tables` |
| `read_docx.py` | Word docs | `read_docx.py memo.docx --json` |
| `read_xlsx.py` | Excel sheets | `read_xlsx.py data.xlsx --sheet Revenue` |
| `read_csv.py` | CSV/TSV (auto-detects delimiter + encoding) | `read_csv.py data.csv --info` |
| `read_html.py` | Local HTML files → clean markdown | `read_html.py saved.html --links` |
| `read_pptx.py` | PowerPoint + speaker notes | `read_pptx.py deck.pptx --notes-only` |
| `read_epub.py` | Books — TOC, chapter, full text, search | `read_epub.py book.epub --search "algebra"` |
| `clean_text.py` | Normalize whitespace, encoding, strip boilerplate | `cat raw.txt \| clean_text.py --aggressive` |
| **Extracting media** | | |
| `extract_images_pdf.py` | Images embedded in PDFs (for charts/figures) | `extract_images_pdf.py report.pdf --render` |
| `extract_audio.py` | Audio from video (16kHz mono WAV by default) | `extract_audio.py podcast.mp4` |
| `video_frames.py` | Frames from a video at intervals or specific times | `video_frames.py movie.mp4 --at 1:23,5:00` |
| **Video / audio** | | |
| `download_video.py` | Download from YouTube/Vimeo/etc via yt-dlp | `download_video.py <url> --subs` |
| `transcribe.py` | Speech → text via whisper.cpp | `transcribe.py podcast.mp3 --model small.en` |
| **Text analysis** | | |
| `corpus_search.py` | Search across all articles' research files (ripgrep) | `corpus_search.py "algebra tracking"` |
| `find_patterns.py` | Top n-grams, recurring names/orgs, repeated quotes | `find_patterns.py articles/sf-algebra/ --ngram 3` |
| `text_stats.py` | Word count, readability, citation density, source diversity | `text_stats.py article.md` |
| `dedup_sources.py` | Detect duplicate URLs/titles across lenses | `dedup_sources.py articles/sf-algebra/` |
| **Math / data** | | |
| `cagr.py` | Compound Annual Growth Rate (and inverses) | `cagr.py 1000 1500 5` |
| `financial_calc.py` | pct-change, YoY, YTD, NPV, IRR, ROI, Rule of 72 | `financial_calc.py npv --rate 0.10 --cashflows -1000,200,300,400,500` |
| `extrapolate.py` | Linear/exponential/logistic/polynomial forecasting | `extrapolate.py --series 10,15,22,33,49 --model exponential --periods 5` |
| `stats.py` | Mean, median, std, percentiles, outliers, skew/kurtosis | `stats.py --series 12,15,19,22,28,31,45,67,89 --outliers` |
| `correlate.py` | Pearson + Spearman + lag correlations | `correlate.py --file data.csv --columns revenue,headcount --lags 4` |
| **Convert** | | |
| `convert.py` | md ↔ html, html ↔ md, csv ↔ json, md → pdf | `convert.py article.md article.pdf` |

## Conventions

- Every script supports `--help` (argparse).
- Most reading scripts support `--json` for structured output (best for agent consumption).
- Math scripts emit human-readable output by default, `--json` for downstream parsing.
- Scripts that need a file enforce the file exists with a clear error.
- Each script is independently runnable — no shared Python module required.

## Common pipelines

**Cite a podcast quote:**
```bash
scripts/download_video.py "https://youtu.be/..." -o /tmp/pod --audio
scripts/transcribe.py /tmp/pod/*.mp3 --model small.en > /tmp/transcript.txt
scripts/corpus_search.py "the specific phrase" --article sf-algebra
```

**Process a leaked report:**
```bash
scripts/detect_filetype.py mystery.bin
scripts/read_pdf.py report.pdf --tables --json > /tmp/report.json
scripts/extract_images_pdf.py report.pdf -o charts/
```

**Quantify a trend in research:**
```bash
scripts/find_patterns.py articles/sf-algebra/research/ --names --top 30
scripts/text_stats.py articles/sf-algebra/article.md
scripts/dedup_sources.py articles/sf-algebra/
```

**Math for a piece on SaaS spending:**
```bash
scripts/cagr.py --series 100,140,196,274,383
scripts/extrapolate.py --series 100,140,196,274,383 --model exponential --periods 3
scripts/correlate.py --file metrics.csv --columns marketing_spend,revenue --lags 2
```

## Adding a new script

1. Drop a `.py` (or `.sh`) into this folder with a leading docstring.
2. Use `argparse`, default to human-readable output, add `--json` if structured data is useful.
3. Make executable: `chmod +x scripts/your_script.py`.
4. Add a row to the table above.

## Deps

Run `bash scripts/setup.sh` once to install everything, or `python3 scripts/check_deps.py` to see what's missing.

| Python | Purpose |
|--------|---------|
| `pdfplumber`, `pymupdf` (`fitz`), `pypdf` | PDF read + image extract |
| `python-docx` | DOCX |
| `openpyxl`, `pandas` | XLSX, CSV |
| `python-pptx` | PPTX |
| `ebooklib`, `trafilatura` | EPUB, clean HTML |
| `chardet`, `python-magic` | Encoding, MIME detection |
| `markdownify`, `markdown` | HTML ↔ Markdown |
| `numpy`, `scipy` | Math, stats, correlations |
| `pdf2image`, `Pillow` | Image processing |
| `ffmpeg-python`, `yt-dlp` | Video / audio |

| CLI | Purpose |
|-----|---------|
| `ffmpeg` | Audio/video transcode (brew install ffmpeg) |
| `whisper-cli` | whisper.cpp transcription (brew install whisper-cpp) |
| `rg` (ripgrep) | Fast corpus search (brew install ripgrep) |
| `jq` | JSON wrangling |

Whisper models live in `~/.whisper-models/`. Default is `ggml-base.en.bin` (147 MB, fast). For better accuracy:
```bash
curl -L -o ~/.whisper-models/ggml-small.en.bin \
  https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.en.bin
```
