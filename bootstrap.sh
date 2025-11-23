#!/usr/bin/env bash
set -e

echo "🔹 Starting environment bootstrap..."

# Detect OS
OS=$(uname)
echo "🖥️  Detected OS: $OS"

# Check task-go
if ! command -v task &> /dev/null; then
    echo "❌ Taskfile CLI not found, installing..."
    echo "Should not be possible based on devcontainer setup"
    exit 1
else
  echo "✅ Taskfile CLI found"
  task --init
fi

# Check Python
if ! command -v python3 &> /dev/null; then
  echo "❌ Python3 not found, please install it."
  exit 1
else
  echo "✅ Python3 found"
fi

# Check pip
if ! command -v pip &> /dev/null; then
  echo "❌ pip not found, installing..."
  python3 -m ensurepip --upgrade
fi

# Check uv
if ! command -v uv &> /dev/null; then
  echo "🔹 Installing uv..."
  pip install --upgrade uv
else
  echo "⚡ uv already installed"
fi

# Check npm
if ! command -v npm &> /dev/null; then
  echo "❌ npm not found. Install Node.js/npm first."
  sudo apt-get update -y
  sudo apt-get upgrade -y
  sudo apt-get install -y nodejs npm
else
  echo "✅ npm installed"
fi

# Optional: system linting tools
if ! command -v yamllint &> /dev/null; then
  echo "🔹 Installing yamllint..."
  pip install yamllint
fi

# Optional: npm formatters
npm install -g prettier yamlfmt || true

echo "✅ Environment bootstrap complete!"
