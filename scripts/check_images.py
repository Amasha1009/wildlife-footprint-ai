from pathlib import Path
from PIL import Image
import csv

DATASET_PATH = Path("dataset/raw/New folder/dataset/data")
OUTPUT = Path("analysis/image_analysis.csv")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

rows = []

for class_folder in sorted(DATASET_PATH.iterdir()):

    if not class_folder.is_dir():
        continue

    for image_file in sorted(class_folder.iterdir()):

        if image_file.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp", ".bmp"}:
            continue

        try:
            with Image.open(image_file) as img:
                rows.append({
                    "class": class_folder.name,
                    "filename": image_file.name,
                    "width": img.width,
                    "height": img.height,
                    "format": img.format,
                    "mode": img.mode,
                    "status": "valid"
                })

        except Exception:
            rows.append({
                "class": class_folder.name,
                "filename": image_file.name,
                "width": "",
                "height": "",
                "format": "",
                "mode": "",
                "status": "corrupted"
            })

with open(OUTPUT, "w", newline="", encoding="utf-8") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=["class", "filename", "width", "height", "format", "mode", "status"]
    )

    writer.writeheader()
    writer.writerows(rows)

print("Image analysis completed.")
print(f"Report saved to: {OUTPUT}")
print(f"Images analyzed: {len(rows)}")
print(f"Valid images: {sum(r['status'] == 'valid' for r in rows)}")
print(f"Corrupted images: {sum(r['status'] == 'corrupted' for r in rows)}")
