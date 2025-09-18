import argparse
from organizer.categories import FILE_CATEGORIES
from pathlib import Path
import shutil


def move_file(file, target_dir):
    target_dir.mkdir(exist_ok=True)
    target_file = target_dir / file.name

    counter = 1
    while target_file.exists():
        target_file = target_dir / f"{file.stem}_{counter}{file.suffix}"
        counter += 1

    shutil.move(str(file), str(target_file))


def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder '{folder}' does not exist.")

    for file in folder.iterdir():
        if file.is_file():
            moved = False
            ext = file.suffix.lower()

            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    move_file(file, folder / category)
                    moved = True
                    break

            if not moved:
                move_file(file, folder / "Others")


# ✅ CLI Support
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a folder by type.")
    parser.add_argument("path", help="Path to the folder to organize")

    args = parser.parse_args()

    organize_folder(args.path)
    print(f"✅ Done! Organized files in: {args.path}")
