#!/usr/bin/env python3
"""Extract audio from a video as a 16kHz mono WAV (what whisper.cpp expects).

Usage:
    extract_audio.py video.mp4                  # → video.wav
    extract_audio.py video.mp4 -o audio.wav
    extract_audio.py video.mp4 --mp3            # → video.mp3 (better for archiving)
"""
import argparse
import os
import shutil
import subprocess
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("video")
    ap.add_argument("-o", "--out")
    ap.add_argument("--mp3", action="store_true", help="encode as mp3 (default: 16kHz wav)")
    a = ap.parse_args()

    if not shutil.which("ffmpeg"):
        print("ERROR: ffmpeg not found. Install via 'brew install ffmpeg'.", file=sys.stderr)
        sys.exit(2)

    base, _ = os.path.splitext(a.video)
    out = a.out or (base + (".mp3" if a.mp3 else ".wav"))

    if a.mp3:
        cmd = ["ffmpeg", "-y", "-i", a.video, "-vn", "-acodec", "libmp3lame", "-q:a", "2", out]
    else:
        cmd = ["ffmpeg", "-y", "-i", a.video, "-vn", "-ac", "1", "-ar", "16000", "-acodec", "pcm_s16le", out]

    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    print(out)


if __name__ == "__main__":
    main()
