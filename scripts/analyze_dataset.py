from pathlib import Path
from PIL import Image

DATASET_PATH = Path("dataset/raw/New folder/dataset/data")

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}


def analyze_dataset():

    if not DATASET_PATH.exists():
        print("ERROR: Dataset folder not found:")
        print(DATASET_PATH)
        return

    print("=" * 60)
    print("       WILDLIFE FOOTPRINT DATASET ANALYSIS")
    print("=" * 60)

    class_counts = {}
    corrupted_images = []
    total_images = 0

    for class_folder in sorted(DATASET_PATH.iterdir()):

        if not class_folder.is_dir():
            continue

        class_name = class_folder.name

        image_files = [
            file for file in class_folder.iterdir()
            if file.is_file()
            and file.suffix.lower() in IMAGE_EXTENSIONS
        ]

        valid_count = 0

        for image_file in image_files:

            try:
                with Image.open(image_file) as img:
                    img.verify()

                valid_count += 1

            except Exception:
                corrupted_images.append(str(image_file))

        class_counts[class_name] = valid_count
        total_images += valid_count

    print("\nImages per class:")
    print("-" * 60)

    for class_name, count in class_counts.items():
        print(f"{class_name:<30} {count:>6}")

    print("-" * 60)

    print(f"Total classes: {len(class_counts)}")
    print(f"Total valid images: {total_images}")
    print(f"Corrupted images: {len(corrupted_images)}")

    if corrupted_images:

        print("\nCorrupted images:")

        for image in corrupted_images:
            print(image)

    print("\nAnalysis completed.")


if __name__ == "__main__":
    analyze_dataset()
