from pathlib import Path

SUBDIRS = {
    "src": ["core", "lib", "utils", "ui", "api", "docs", "logs", "configs", "notes"],
    "tests": ["core_tests", "lib_tests", "utils_tests", "ui_tests", "api_tests"]
}

PYTHON_DIRS = {
    "python": SUBDIRS,
}

def create_dir(path: Path) -> None:
    """Create a directory if it does not exist."""
    if not path.exists():
        print(f"📁 Creating directory: {path}")
        path.mkdir(parents=True, exist_ok=True)
    else:
        print(f"✅ Directory already exists: {path}")


def setup_dirs(dir_dict: dict[str]) -> None:
    """Create project directories if they do not exist."""
    for language, base_dirs in dir_dict.items():
        lang_path = Path(language)
        print(f"Setting up directories for language: {language}")
        create_dir(lang_path)
        for base_dir, subdirs in base_dirs.items():
            base_path = lang_path / base_dir
            print(f"Setting up base directory: {base_path}")
            create_dir(base_path)
            for subdir in subdirs:
                subdir_path = base_path / subdir
                print(f"Setting up directory: {subdir_path}")
                create_dir(subdir_path)


    # for d in dir_list:
    #     path = Path(d)
    #     if not path.exists():
    #         print(f"📁 Creating directory: {d}")
    #         path.mkdir(parents=True, exist_ok=True)
    #     else:
    #         print(f"✅ Directory already exists: {d}")


if __name__ == "__main__":
    setup_dirs(PYTHON_DIRS)
