#!/usr/bin/env bash
set -e

echo "🔧 Configuring Git inside devcontainer..."

# Good defaults
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global credential.helper store

# Auto-fix line endings
git config --global core.autocrlf input

# Ensure workspace exists
if [ -d /workspaces ]; then
    cd /workspaces/* || exit 0
else
    cd /workspaces || true
fi

echo "📂 Git setup complete. Current directory: $(pwd)"
