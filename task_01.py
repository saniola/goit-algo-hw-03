import argparse
from pathlib import Path
import shutil


def parse_args():
    parser = argparse.ArgumentParser(
        description="Рекурсивно копіює файли та сортує їх за розширенням"
    )
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Шлях до вихідної директорії"
    )
    parser.add_argument(
        "-d",
        "--destination",
        type=Path,
        default=Path("dist"),
        help="Шлях до директорії призначення (за замовчуванням: 'dist')",
    )
    return parser.parse_args()


def recursive_copy_and_sort(source: Path, destination: Path):
    for item in source.iterdir():
        if item.is_dir():
            recursive_copy_and_sort(item, destination)
        else:
            file_extension = item.suffix.lower()
            folder_path = destination / file_extension[1:]
            folder_path.mkdir(exist_ok=True, parents=True)
            shutil.copy(item, folder_path)


def main():
    args = parse_args()
    recursive_copy_and_sort(args.source, args.destination)
    print(f"Файли успішно скопійовано та сортовано в {args.destination}")


if __name__ == "__main__":
    main()
