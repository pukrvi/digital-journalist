# Security

## How your API keys are stored

API keys must stay **usable** to call providers, so they can't be one-way hashed. Instead they're protected
the way mature CLI tools protect them — and we're transparent about exactly how:

- **Local only.** Keys live in `tools/api/keys.env` on your machine. Nothing is sent anywhere except the
  provider you're calling.
- **Gitignored.** `keys.env`, `keys.fingerprint.json`, and `keys.env.enc` are in `.gitignore`. They can't be
  committed by accident.
- **Owner-only permissions.** The file is `chmod 0600` (read/write for you, nobody else).
- **Masked on display.** Any listing shows `tvly…ZVUf (58 chars)` — never the full key.
- **Fingerprinted.** A SHA-256 fingerprint (+ last 4) is recorded in `keys.fingerprint.json` so you can
  confirm *which* key is loaded without ever exposing it.
- **Optional encryption at rest.** `python3 onboarding/keys_manager.py lock` encrypts `keys.env` to
  `keys.env.enc` with a passphrase (PBKDF2-SHA256 → Fernet) and removes the plaintext; `unlock` restores it
  for a working session.

## Commands

```bash
python3 onboarding/keys_manager.py list        # masked status of every provider
python3 onboarding/keys_manager.py set tavily "tvly-..."   # store/replace (value never echoed)
python3 onboarding/keys_manager.py remove tavily
python3 onboarding/keys_manager.py check       # audit perms + gitignore
python3 onboarding/keys_manager.py lock         # encrypt at rest
python3 onboarding/keys_manager.py unlock       # decrypt for a session
```

## Why not hash the keys?

A hash is one-way — you couldn't recover the key to make an API call. Reversible local storage with
restrictive permissions, masking, and optional passphrase encryption is the honest, standard answer. The
**fingerprint** gives you the "hash" benefit (verify identity) without breaking usability.

## Good hygiene

- Run `keys_manager.py check` before pushing.
- Rotate a key by `set`-ting the new value (the fingerprint updates).
- Prefer free-tier keys; enable paid providers (`ALLOW_PAID=1`) deliberately.
- The journalist fetches public web pages — respect each site's terms and each provider's usage policy.
