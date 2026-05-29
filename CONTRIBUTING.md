# Contributing to Digital Journalist

Thanks for your interest. This project is maintained by **INFINITIGRID TECHNOLOGIES (OPC) PRIVATE LIMITED**
and licensed under Apache 2.0.

## Ground rules

- By submitting a contribution you agree it is licensed under [Apache 2.0](LICENSE) (see the Contribution
  clause). Source code remains the copyrighted property of INFINITIGRID TECHNOLOGIES (OPC) PRIVATE LIMITED.
- Keep the journalism principles intact (see [CLAUDE.md](CLAUDE.md)): contrarian lens mandatory, cite-or-skip,
  authoritative-sources-first, adversarial verification. PRs that weaken these will be asked to revise.
- **Never commit secrets.** `tools/api/keys.env`, `keys.fingerprint.json`, and `profile/*.md` are gitignored —
  keep it that way. Run `python3 onboarding/keys_manager.py check` before pushing.

## Dev setup

```bash
bash scripts/setup.sh
python3 scripts/check_deps.py     # all green?
```

## Working on the workflows

The two engines are plain JavaScript executed by the agent's Workflow runtime:

- `digital-journalist.workflow.js` — Stage 1 (research)
- `dj-write.workflow.js` — Stage 2 (write)

Conventions learned the hard way (see `memory/failure-modes.md`):

- **No `Date.now()` / `Math.random()`** in workflow scripts — the runtime forbids them. Pass `timestamp` via args.
- **Parse string args defensively** — the harness sometimes delivers `args` as a JSON string.
- **Heavy file-writing agents should be schema-free** (write the file, return short text). Reserve JSON
  schemas for small control-flow returns. A big "write a document AND return JSON" agent is the fragile one.
- Syntax-check before committing: `node --check digital-journalist.workflow.js && node --check dj-write.workflow.js`.
- Keep `meta.phases` in sync with the `phase()` calls.

## Adding a search provider

1. Add `tools/api/<provider>.py` following the shape of an existing one (e.g. `tavily.py`): a `search(query,
   count, ...)` returning `normalize_result(...)`, plus a small CLI.
2. Register it in `tools/api/limits.json`, in `_common.py` (`KEY_FOR`), and in the `PROVIDERS` maps in
   `search.py` and `ping.py`.
3. Add the key var to `keys.env.example`. Run `python3 tools/api/ping.py` to confirm.
4. Note its best-fit lens in `memory/search-providers.md`.

## Adding a helper script

Drop it in `scripts/`, give it a docstring + `argparse`, default to human output with a `--json` flag,
`chmod +x`, and add a row to `scripts/README.md`.

## Docs & wiki

- Long-form docs live in `wiki/`. To publish to the GitHub Wiki, clone `<repo>.wiki.git` and copy the files,
  or keep them browsable in-repo (the README links to them directly).
- Update `CHANGELOG.md` for user-facing changes.

## Pull requests

Keep PRs focused. Describe what changed and why, and confirm `check_deps.py`, both `node --check`s, and
`keys_manager.py check` pass.
