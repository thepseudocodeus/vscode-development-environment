# tools/bootstrap.py
from pathlib import Path
import json
import os

print("DEBUG: CWD =", Path.cwd())
print("DEBUG: Contents =", list(Path.cwd().iterdir()))

def detect_devcontainer():
    return os.path.exists("/workspaces") or os.environ.get("REMOTE_CONTAINERS") == "true"


def verify_container_version():
    config_path = Path(".devcontainer/devcontainer.json")
    if not config_path.exists():
        print("⚠️ No devcontainer.json present.")
        return

    with open(config_path) as f:
        config = json.load(f)
    print(f"🛠 Devcontainer definition found: {config.get('name', '(unnamed)')}")


def main():
    print("\n🚀 Running bootstrap\n")

    if detect_devcontainer():
        print("🐳 Inside a devcontainer")
        verify_container_version()
    else:
        print("💻 Not inside a devcontainer")


if __name__ == "__main__":
    main()
