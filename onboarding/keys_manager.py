#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 INFINITIGRID TECHNOLOGIES (OPC) PRIVATE LIMITED. Created by Puneet Vishnawat.
"""Secure local storage for API keys.

Design (honest security posture — API keys must stay reversible to be usable, so they are
NOT one-way hashed; instead they are protected the way real tools protect them):
  - Stored ONLY in tools/api/keys.env, which is gitignored and chmod 0600 (owner read/write only).
  - NEVER printed in full — always masked (first 4 + last 4).
  - A SHA-256 fingerprint (+ last4) is recorded in tools/api/keys.fingerprint.json so you can
    confirm WHICH key is loaded without ever exposing it.
  - Optional encryption-at-rest: `lock` encrypts keys.env -> keys.env.enc with a passphrase
    (PBKDF2-SHA256 -> Fernet); `unlock` restores it for a working session.

Usage:
  keys_manager.py set <PROVIDER|ENV_NAME> <value>     # store/replace a key (value never echoed)
  keys_manager.py list                                # masked status of every known provider
  keys_manager.py remove <PROVIDER|ENV_NAME>
  keys_manager.py check                               # verify file permissions / gitignore
  keys_manager.py lock                                # encrypt keys.env at rest (prompts passphrase)
  keys_manager.py unlock                              # decrypt for this session (prompts passphrase)
"""
from __future__ import annotations

import argparse
import getpass
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API_DIR = ROOT / "tools" / "api"
KEYS_FILE = API_DIR / "keys.env"
FINGERPRINT_FILE = API_DIR / "keys.fingerprint.json"
ENC_FILE = API_DIR / "keys.env.enc"
SALT_FILE = API_DIR / "keys.env.salt"

# Reuse the canonical provider -> env-var map from the aggregator.
sys.path.insert(0, str(API_DIR))
try:
    from _common import KEY_FOR, LIMITS  # type: ignore
except Exception:
    KEY_FOR, LIMITS = {}, {}

# provider short-name -> primary env var (for convenience: `set tavily <key>`)
PROVIDER_ENV = {}
for prov, env in KEY_FOR.items():
    if isinstance(env, str):
        PROVIDER_ENV[prov] = env
    elif isinstance(env, tuple):
        PROVIDER_ENV[prov] = env[0]


def _resolve_env(name: str) -> str:
    """Accept a provider short-name (tavily) or a raw env var (TAVILY_API_KEY)."""
    if name in PROVIDER_ENV:
        return PROVIDER_ENV[name]
    return name.upper()


def mask(value: str) -> str:
    if not value:
        return "(unset)"
    if len(value) <= 10:
        return "*" * len(value)
    return f"{value[:4]}…{value[-4:]} ({len(value)} chars)"


def _fingerprint(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def _read_env() -> dict:
    """Parse keys.env into an ordered dict of KEY=VALUE (comments/blank lines dropped)."""
    out = {}
    if KEYS_FILE.exists():
        for line in KEYS_FILE.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s or s.startswith("#") or "=" not in s:
                continue
            k, _, v = s.partition("=")
            out[k.strip()] = v.strip()
    return out


def _write_env(pairs: dict) -> None:
    API_DIR.mkdir(parents=True, exist_ok=True)
    header = (
        "# Digital Journalist — API key registry (gitignored, chmod 0600).\n"
        "# Managed by onboarding/keys_manager.py. Do not commit. See keys.env.example for signup links.\n\n"
    )
    body = "\n".join(f"{k}={v}" for k, v in pairs.items()) + "\n"
    KEYS_FILE.write_text(header + body, encoding="utf-8")
    os.chmod(KEYS_FILE, 0o600)


def _update_fingerprint(env_name: str, value: str | None) -> None:
    data = {}
    if FINGERPRINT_FILE.exists():
        try:
            data = json.loads(FINGERPRINT_FILE.read_text(encoding="utf-8"))
        except Exception:
            data = {}
    if value is None:
        data.pop(env_name, None)
    else:
        data[env_name] = {
            "fingerprint_sha256_16": _fingerprint(value),
            "last4": value[-4:],
            "length": len(value),
            "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        }
    FINGERPRINT_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    os.chmod(FINGERPRINT_FILE, 0o600)


def set_key(name: str, value: str) -> None:
    env = _resolve_env(name)
    value = value.strip()
    if not value:
        print("ERROR: empty value", file=sys.stderr); sys.exit(2)
    pairs = _read_env()
    pairs[env] = value
    _write_env(pairs)
    _update_fingerprint(env, value)
    print(f"[stored] {env} = {mask(value)}  fingerprint={_fingerprint(value)}  (tools/api/keys.env, 0600)")


def remove_key(name: str) -> None:
    env = _resolve_env(name)
    pairs = _read_env()
    if env in pairs:
        del pairs[env]
        _write_env(pairs)
        _update_fingerprint(env, None)
        print(f"[removed] {env}")
    else:
        print(f"[not set] {env}")


def list_keys() -> None:
    pairs = _read_env()
    fp = {}
    if FINGERPRINT_FILE.exists():
        try:
            fp = json.loads(FINGERPRINT_FILE.read_text(encoding="utf-8"))
        except Exception:
            fp = {}
    print(f"{'PROVIDER':<20} {'ENV VAR':<22} {'STATUS':<8} {'MASKED':<22} TIER")
    print("-" * 92)
    for prov, env in PROVIDER_ENV.items():
        tier = (LIMITS.get(prov) or {}).get("tier", "?")
        if prov in ("duckduckgo",) or (LIMITS.get(prov, {}).get("tier") == "keyless"):
            print(f"{prov:<20} {'(keyless)':<22} {'ready':<8} {'—':<22} {tier}")
            continue
        val = pairs.get(env, "")
        status = "set" if val else "—"
        print(f"{prov:<20} {env:<22} {status:<8} {mask(val):<22} {tier}")
    if ENC_FILE.exists():
        print("\n[locked] An encrypted keys.env.enc exists. Run `unlock` before a session if keys.env is absent.")


def check() -> None:
    ok = True
    if KEYS_FILE.exists():
        mode = oct(os.stat(KEYS_FILE).st_mode & 0o777)
        good = (os.stat(KEYS_FILE).st_mode & 0o077) == 0
        print(f"keys.env permissions: {mode} {'✓ (owner-only)' if good else '✗ — run: chmod 600 ' + str(KEYS_FILE)}")
        ok = ok and good
    else:
        print("keys.env: not present yet (no keys stored).")
    gi = ROOT / ".gitignore"
    ignored = gi.exists() and "keys.env" in gi.read_text(encoding="utf-8")
    print(f".gitignore covers keys.env: {'✓' if ignored else '✗ — add tools/api/keys.env to .gitignore'}")
    ok = ok and ignored
    print("Secrets policy: keys are stored locally only, masked on display, fingerprinted, never committed.")
    sys.exit(0 if ok else 1)


def _derive(passphrase: str, salt: bytes):
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
    import base64
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=390000)
    return base64.urlsafe_b64encode(kdf.derive(passphrase.encode("utf-8")))


def lock() -> None:
    try:
        from cryptography.fernet import Fernet
    except Exception:
        print("ERROR: pip install cryptography", file=sys.stderr); sys.exit(2)
    if not KEYS_FILE.exists():
        print("Nothing to lock (no keys.env).", file=sys.stderr); sys.exit(1)
    p1 = getpass.getpass("New passphrase: "); p2 = getpass.getpass("Confirm: ")
    if p1 != p2 or not p1:
        print("Passphrases don't match.", file=sys.stderr); sys.exit(2)
    salt = os.urandom(16)
    token = Fernet(_derive(p1, salt)).encrypt(KEYS_FILE.read_bytes())
    ENC_FILE.write_bytes(token); os.chmod(ENC_FILE, 0o600)
    SALT_FILE.write_bytes(salt); os.chmod(SALT_FILE, 0o600)
    KEYS_FILE.unlink()
    print(f"[locked] Encrypted -> {ENC_FILE.name}. Plaintext keys.env removed. Run `unlock` before your next session.")


def unlock() -> None:
    try:
        from cryptography.fernet import Fernet
    except Exception:
        print("ERROR: pip install cryptography", file=sys.stderr); sys.exit(2)
    if not ENC_FILE.exists() or not SALT_FILE.exists():
        print("No locked vault found.", file=sys.stderr); sys.exit(1)
    p = getpass.getpass("Passphrase: ")
    try:
        data = Fernet(_derive(p, SALT_FILE.read_bytes())).decrypt(ENC_FILE.read_bytes())
    except Exception:
        print("Wrong passphrase.", file=sys.stderr); sys.exit(2)
    KEYS_FILE.write_bytes(data); os.chmod(KEYS_FILE, 0o600)
    print(f"[unlocked] Restored {KEYS_FILE.name} for this session (0600).")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("set"); s.add_argument("name"); s.add_argument("value")
    r = sub.add_parser("remove"); r.add_argument("name")
    sub.add_parser("list"); sub.add_parser("check"); sub.add_parser("lock"); sub.add_parser("unlock")
    a = ap.parse_args()
    if a.cmd == "set": set_key(a.name, a.value)
    elif a.cmd == "remove": remove_key(a.name)
    elif a.cmd == "list": list_keys()
    elif a.cmd == "check": check()
    elif a.cmd == "lock": lock()
    elif a.cmd == "unlock": unlock()


if __name__ == "__main__":
    main()
