from pathlib import Path
import subprocess

def repo_root():
    for parent in [Path.cwd()] + list(Path.cwd().parents):
        if (parent / ".git").exists():
            return parent
    raise RuntimeError("No git repo found")

ROOT = repo_root()

def run(*cmd):
    return subprocess.check_output(["git", "-C", str(ROOT), *cmd]).decode()

def current_branch():
    return run("rev-parse", "--abbrev-ref", "HEAD").strip()
