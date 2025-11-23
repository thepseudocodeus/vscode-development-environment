from pathlib import Path

def create_init_files(root_dirs):
    for root in root_dirs:
        for path in Path(root).rglob("*"):
            if path.is_dir():
                init_file = path / "__init__.py"
                init_file.touch(exist_ok=True)
    print("✅ __init__.py files created.")

if __name__ == "__main__":
    create_init_files(["src", "tests"])
