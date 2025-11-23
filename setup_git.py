#!/usr/bin/env python3
"""
Git Setup Helper - Expert Teaching Tool
Ensures a repo is initialized, remote is configured, and first commit exists.
Designed for devcontainers, ephemeral environments, or new projects.
"""

import subprocess
import sys
from pathlib import Path

def run(cmd, capture_output=False):
    """Run a shell command safely."""
    try:
        result = subprocess.run(
            cmd, shell=True, check=True, capture_output=capture_output, text=True
        )
        return result.stdout.strip() if capture_output else True
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {cmd}")
        if e.stderr:
            print(e.stderr)
        sys.exit(1)

def git_installed():
    """Check if git is installed."""
    try:
        run("git --version", capture_output=True)
        return True
    except SystemExit:
        print("❌ Git is not installed. Please install Git first.")
        return False

def init_repo():
    """Initialize git repo if not exists."""
    if not Path(".git").exists():
        print("🔹 Initializing new Git repository...")
        run("git init")
    else:
        print("⚡ Git repository already exists.")

def ensure_branch(branch="main"):
    """Ensure current branch exists and is set."""
    branches = run("git branch --show-current", capture_output=True)
    if not branches:
        print(f"🔹 Creating initial branch '{branch}'...")
        run(f"git checkout -b {branch}")
    else:
        print(f"⚡ Current branch: {branches}")

def add_remote(remote_url):
    """Add or update remote origin."""
    remotes = run("git remote", capture_output=True).splitlines()
    if "origin" not in remotes:
        print(f"🔹 Adding remote origin: {remote_url}")
        run(f"git remote add origin {remote_url}")
    else:
        current_url = run("git remote get-url origin", capture_output=True)
        if current_url != remote_url:
            print(f"🔹 Updating remote origin URL to: {remote_url}")
            run(f"git remote set-url origin {remote_url}")
        else:
            print("⚡ Remote origin already set correctly.")

def ensure_initial_commit():
    """Create initial commit if no commits exist."""
    try:
        run("git rev-parse HEAD", capture_output=True)
        print("⚡ Initial commit already exists.")
    except SystemExit:
        print("🔹 Creating initial commit...")
        run("git add .")
        run("git commit -m 'Initial commit'")
        print("✅ Initial commit created.")

def test_authentication(remote_url):
    """Check if SSH or HTTPS authentication works."""
    if remote_url.startswith("git@"):
        print("🔹 Testing SSH connection...")
        try:
            run(f"ssh -T {remote_url.split(':')[0]}", capture_output=True)
            print("✅ SSH authentication works.")
        except SystemExit:
            print("⚠️ SSH authentication failed. Consider using HTTPS.")
    else:
        print("ℹ️ Using HTTPS, ensure your token is valid.")

def push_main(remote_url, branch="main"):
    """Push to remote."""
    print(f"🔹 Pushing branch '{branch}' to {remote_url}...")
    run(f"git push -u origin {branch}")

def main():
    if not git_installed():
        sys.exit(1)

    remote_url = input("Enter remote repository URL (SSH or HTTPS): ").strip()

    init_repo()
    ensure_branch()
    add_remote(remote_url)
    ensure_initial_commit()
    test_authentication(remote_url)

    proceed = input("Do you want to push to remote now? [y/N]: ").strip().lower()
    if proceed == "y":
        push_main(remote_url)
    print("✅ Git setup completed.")

if __name__ == "__main__":
    main()
