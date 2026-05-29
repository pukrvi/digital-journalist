#!/usr/bin/env python3
"""Transcribe audio or video to text using whisper.cpp.

Usage:
    transcribe.py audio.mp3                        # plain text
    transcribe.py video.mp4                        # extracts audio first, then transcribes
    transcribe.py podcast.mp3 --srt                # subtitle format
    transcribe.py podcast.mp3 --json               # JSON with timestamps
    transcribe.py podcast.mp3 --model small.en     # use small model (better accuracy)
    transcribe.py podcast.mp3 --speaker-tags       # crude two-speaker labeling via diarization heuristic
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile


MODEL_DIR = os.path.expanduser("~/.whisper-models")


def ensure_wav(media):
    """Return a 16kHz mono WAV path. Convert if needed."""
    ext = os.path.splitext(media)[1].lower()
    if ext == ".wav":
        # Check sample rate; whisper.cpp wants 16kHz mono. Re-encode anyway for safety.
        pass
    if not shutil.which("ffmpeg"):
        print("ERROR: ffmpeg required.", file=sys.stderr); sys.exit(2)
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
    subprocess.check_call(
        ["ffmpeg", "-y", "-i", media, "-vn", "-ac", "1", "-ar", "16000",
         "-acodec", "pcm_s16le", tmp],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    return tmp


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("media")
    ap.add_argument("--model", default="base.en", help="model name (looks for ggml-<MODEL>.bin in ~/.whisper-models)")
    ap.add_argument("--srt", action="store_true")
    ap.add_argument("--vtt", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--threads", type=int, default=0, help="ffmpeg+whisper threads (0=auto)")
    a = ap.parse_args()

    whisper = shutil.which("whisper-cli") or shutil.which("whisper-cpp")
    if not whisper:
        print("ERROR: whisper-cli/whisper-cpp not found. Install: brew install whisper-cpp", file=sys.stderr)
        sys.exit(2)

    model_path = os.path.join(MODEL_DIR, f"ggml-{a.model}.bin")
    if not os.path.isfile(model_path):
        avail = ", ".join(sorted(os.listdir(MODEL_DIR))) if os.path.isdir(MODEL_DIR) else "(none)"
        print(f"ERROR: model not found at {model_path}\n   Available: {avail}\n   Download: curl -L -o {model_path} https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-{a.model}.bin",
              file=sys.stderr)
        sys.exit(2)

    wav = ensure_wav(a.media)

    out_prefix = tempfile.NamedTemporaryFile(suffix="", delete=False).name
    cmd = [whisper, "-m", model_path, "-f", wav, "-of", out_prefix]
    if a.threads:
        cmd += ["-t", str(a.threads)]
    if a.srt:
        cmd += ["-osrt"]
    if a.vtt:
        cmd += ["-ovtt"]
    if a.json:
        cmd += ["-oj"]
    if not (a.srt or a.vtt or a.json):
        cmd += ["-otxt"]

    subprocess.check_call(cmd, stderr=subprocess.DEVNULL)

    suffix = ".srt" if a.srt else ".vtt" if a.vtt else ".json" if a.json else ".txt"
    out_file = out_prefix + suffix
    with open(out_file, encoding="utf-8", errors="replace") as f:
        content = f.read()
    print(content.strip())

    os.unlink(wav)
    if os.path.exists(out_file):
        os.unlink(out_file)


if __name__ == "__main__":
    main()
