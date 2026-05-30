#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 INFINITIGRID TECHNOLOGIES (OPC) PRIVATE LIMITED. Created by Puneet Vishnawat.
#
# install-slash-commands.sh — make /digital-journalist and /onboard available in Codex CLI.
#
# Claude Code loads slash commands automatically from .claude/commands/ when you open the repo.
# Codex CLI looks at ~/.codex/prompts/ (user-level only) — there is no project-level prompts
# directory. This script copies the canonical command files into that location so the same
# slash commands work in both agents.
#
# Re-run any time .claude/commands/ changes (it overwrites the destination files).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_ROOT/.claude/commands"
DEST="${CODEX_HOME:-$HOME/.codex}/prompts"

if [ ! -d "$SRC" ]; then
  echo "error: no .claude/commands/ directory found at $SRC" >&2
  exit 1
fi

shopt -s nullglob
commands=("$SRC"/*.md)
shopt -u nullglob

if [ ${#commands[@]} -eq 0 ]; then
  echo "error: no .md files in $SRC" >&2
  exit 1
fi

mkdir -p "$DEST"

echo "Installing slash commands to $DEST"
for f in "${commands[@]}"; do
  name="$(basename "$f")"
  cp "$f" "$DEST/$name"
  echo "  /$(basename "$name" .md)  ← $name"
done

echo
echo "Done. Restart Codex CLI to pick up the new commands."
echo "Try:  /digital-journalist <your topic>"
