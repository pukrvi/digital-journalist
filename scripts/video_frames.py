#!/usr/bin/env python3
"""Extract frames from a video. Use for citing visual evidence in articles.

Usage:
    video_frames.py movie.mp4                                # every 30s, into ./movie-frames/
    video_frames.py movie.mp4 --every 10                      # every 10 seconds
    video_frames.py movie.mp4 --at 1:23                       # one frame at 1m23s
    video_frames.py movie.mp4 --at 0:30,2:15,5:00             # multiple timestamps
    video_frames.py movie.mp4 -o frames/                      # output dir
    video_frames.py movie.mp4 --fps 0.5                       # 1 frame every 2s (fps form)
"""
import argparse
import os
import shutil
import subprocess
import sys


def to_seconds(ts):
    parts = [int(p) for p in ts.split(":")]
    if len(parts) == 3: h, m, s = parts; return h * 3600 + m * 60 + s
    if len(parts) == 2: m, s = parts; return m * 60 + s
    return parts[0]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("video")
    ap.add_argument("-o", "--out", help="output dir (default: ./<name>-frames/)")
    ap.add_argument("--every", type=int, default=30, help="seconds between frames")
    ap.add_argument("--at", help="timestamps to grab, comma-separated (e.g. '1:23,5:00')")
    ap.add_argument("--fps", type=float, help="frame rate to sample (alternative to --every)")
    ap.add_argument("--width", type=int, default=1280)
    a = ap.parse_args()

    if not shutil.which("ffmpeg"):
        print("ERROR: ffmpeg required.", file=sys.stderr); sys.exit(2)

    base = os.path.splitext(os.path.basename(a.video))[0]
    out = a.out or f"./{base}-frames"
    os.makedirs(out, exist_ok=True)

    if a.at:
        for ts in a.at.split(","):
            ts = ts.strip()
            secs = to_seconds(ts)
            target = os.path.join(out, f"frame_{ts.replace(':','m')}s.jpg")
            cmd = ["ffmpeg", "-y", "-ss", str(secs), "-i", a.video, "-frames:v", "1",
                   "-vf", f"scale={a.width}:-1", "-q:v", "2", target]
            subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(target)
        return

    fps = a.fps if a.fps else (1.0 / a.every)
    pattern = os.path.join(out, "frame_%04d.jpg")
    cmd = ["ffmpeg", "-y", "-i", a.video, "-vf", f"fps={fps},scale={a.width}:-1",
           "-q:v", "2", pattern]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    files = sorted(os.listdir(out))
    print(f"Saved {len(files)} frames to {out}/")


if __name__ == "__main__":
    main()
