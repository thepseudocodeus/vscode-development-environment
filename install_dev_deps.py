from pathlib import Path

DEV_REQ_FILE = "dev-requirements.txt"

def install_from_file(f: str | None = None) -> None:
    """Install development dependencies from a requirements file."""
    import subprocess
    if f is None:
        f = DEV_REQ_FILE
    print(f"🔍 Checking for development requirements file at {f}...")

    with open(Path(f), "r") as file:
        print(f"📦 Installing development dependencies from {f}...")
        for line in file:
            pkg = f"{line.strip()}"
            print(f"Installing: {pkg}...")
            subprocess.run(["uv", "add", pkg], check=True)
            print(f"{pkg} installed")
    print("✅ Development dependencies installed.")

if __name__ == "__main__":
    dev_file = input("Enter the path to the development requirements file (or press Enter to use default): ").strip()
    input_file = dev_file if dev_file else None
    install_from_file(input_file)
