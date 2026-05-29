# Tools & Scripts

Two layers: light **`tools/`** wrappers for search/fetch, and heavy **`scripts/`** lifters for documents,
media, and analysis. Full reference: [`scripts/README.md`](../scripts/README.md), [`tools/README.md`](../tools/README.md),
[`tools/api/README.md`](../tools/api/README.md).

## tools/ — search & fetch (one-liners)

| Tool | Purpose |
|------|---------|
| `tools/search.sh` | DuckDuckGo search (keyless) |
| `tools/fetch.sh` | Clean article-body extraction (trafilatura) |
| `tools/wiki.sh` | Wikipedia summary + URL |
| `tools/arxiv.sh` | Academic papers |
| `tools/feed.sh` | RSS/Atom feed |
| `tools/api/` | The 18-provider aggregator (see [Search Providers](Search-Providers.md)) |

## scripts/ — heavy lifters

| Area | Scripts |
|------|---------|
| **Setup** | `setup.sh`, `check_deps.py`, `detect_filetype.py` |
| **Read formats** | `read_pdf.py`, `read_docx.py`, `read_xlsx.py`, `read_csv.py`, `read_html.py`, `read_pptx.py`, `read_epub.py`, `clean_text.py` |
| **Media** | `extract_audio.py`, `extract_images_pdf.py`, `video_frames.py`, `download_video.py` (yt-dlp), `transcribe.py` (whisper.cpp) |
| **Text/corpus analysis** | `corpus_search.py` (ripgrep), `find_patterns.py` (n-grams, names, quotes), `text_stats.py` (readability, citation density), `dedup_sources.py` |
| **Math / data** | `cagr.py`, `financial_calc.py` (pct-change, YoY, YTD, NPV, IRR, ROI, Rule-of-72), `extrapolate.py`, `stats.py`, `correlate.py` |
| **Convert** | `convert.py` (md ↔ html ↔ csv ↔ json, md → pdf) |

Agents call these via `Bash`, e.g.:

```bash
python3 scripts/read_pdf.py report.pdf --pages 1-10 --tables
python3 scripts/transcribe.py interview.mp4 --model small.en
python3 scripts/cagr.py 1000 1500 5
python3 scripts/correlate.py --file metrics.csv --columns spend,revenue --lags 3
```

## Dependencies

`bash scripts/setup.sh` installs the Python libraries, ffmpeg, whisper.cpp, and ripgrep, then downloads the
default whisper model. `python3 scripts/check_deps.py` verifies everything is wired up.
