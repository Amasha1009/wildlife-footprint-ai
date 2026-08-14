from pathlib import Path
from hashlib import md5
from collections import defaultdict

DATASET_PATH = Path("dataset/raw/New folder/dataset/data")

hashes = defaultdict(list)

for image_file in DATASET_PATH.rglob("*"):

    if image_file.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp", ".bmp"}:
        continue

    file_hash = md5(image_file.read_bytes()).hexdigest()
    hashes[file_hash].append(str(image_file))

duplicates = {
    h: files
    for h, files in hashes.items()
    if len(files) > 1
}

print("=" * 60)
print("DUPLICATE IMAGE CHECK")
print("=" * 60)

print(f"Total images checked: {sum(len(v) for v in hashes.values())}")
print(f"Duplicate groups found: {len(duplicates)}")

if duplicates:

    print("\nDuplicate images:")

    for files in duplicates.values():

        print("\nGroup:")

        for file in files:
            print(file)

else:

    print("No exact duplicate images found.")

print("\nDuplicate check completed.")
