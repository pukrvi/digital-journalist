#!/usr/bin/env python3
"""Download a video (and optionally subtitles) via yt-dlp. Works for YouTube, Vimeo, and ~1000 other sites.

Usage:
    download_video.py <url>                          # best quality, mp4 if possible
    download_video.py <url> -o videos/               # output dir
    download_video.py <url> --audio                  # audio-only (mp3)
    download_video.py <url> --subs                   # also save subtitles (auto + manual)
    download_video.py <url> --info                   # print metadata, don't download
    download_video.py <url> --transcript             # download subs + print as plain text
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("url")
    ap.add_argument("-o", "--out", default=".", help="output directory")
    ap.add_argument("--audio", action="store_true", help="audio only (mp3)")
    ap.add_argument("--subs", action="store_true", help="also fetch subtitles")
    ap.add_argument("--info", action="store_true", help="metadata only, no download")
    ap.add_argument("--transcript", action="store_true", help="download subs and print as text")
    ap.add_argument("--max-res", default="1080", help="max video height (default 1080)")
    a = ap.parse_args()

    ytdlp = shutil.which("yt-dlp") or os.path.expanduser("~/Library/Python/3.9/bin/yt-dlp")
    os.makedirs(a.out, exist_ok=True)

    if a.info:
        cmd = [ytdlp, "-J", "--no-warnings", a.url]
        out = subprocess.check_output(cmd).decode("utf-8", errors="replace")
        data = json.loads(out)
        keep = {k: data.get(k) for k in ["id", "title", "uploader", "upload_date", "duration", "view_count", "channel", "channel_url", "webpage_url", "description", "tags"]}
        print(json.dumps(keep, indent=2))
        return

    if a.transcript:
        # Download subs to a temp dir, then concatenate
        cmd = [
            ytdlp, "--write-auto-subs", "--write-subs", "--sub-langs", "en.*,en",
            "--skip-download", "--sub-format", "vtt",
            "-o", os.path.join(a.out, "%(id)s.%(ext)s"),
            a.url,
        ]
        subprocess.check_call(cmd)
        for f in os.listdir(a.out):
            if f.endswith(".vtt"):
                with open(os.path.join(a.out, f), encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                clean = re.sub(r"WEBVTT.*?\n\n", "", text, count=1, flags=re.DOTALL)
                clean = re.sub(r"\d{2}:\d{2}:\d{2}\.\d{3} --> .*?\n", "", clean)
                clean = re.sub(r"<[^>]+>", "", clean)
                clean = re.sub(r"\n{2,}", "\n", clean)
                lines, seen = [], set()
                for ln in clean.splitlines():
                    ln = ln.strip()
                    if ln and ln not in seen:
                        seen.add(ln); lines.append(ln)
                print("\n".join(lines))
                return
        print("(no subtitles available)", file=sys.stderr)
        return

    base_cmd = [ytdlp, "-o", os.path.join(a.out, "%(title)s.%(ext)s"), "--no-warnings"]
    if a.audio:
        base_cmd += ["-x", "--audio-format", "mp3", "--audio-quality", "0"]
    else:
        base_cmd += ["-f", f"bv*[height<={a.max_res}]+ba/b[height<={a.max_res}]", "--merge-output-format", "mp4"]
    if a.subs:
        base_cmd += ["--write-subs", "--write-auto-subs", "--sub-langs", "en.*,en", "--embed-subs"]
    base_cmd.append(a.url)
    subprocess.check_call(base_cmd)


if __name__ == "__main__":
    main()
