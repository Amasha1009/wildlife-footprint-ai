from pathlib import Path
import random
import shutil

SOURCE = Path("dataset/cleaned")
DEST = Path("dataset/split")

TRAIN_RATIO = 0.70
VAL_RATIO = 0.15

random.seed(42)

for class_folder in sorted(SOURCE.iterdir()):

    if not class_folder.is_dir():
        continue

    images = [
        f for f in class_folder.iterdir()
        if f.is_file()
    ]

    random.shuffle(images)

    total = len(images)

    train_end = int(total * TRAIN_RATIO)
    val_end = train_end + int(total * VAL_RATIO)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    for split_name, split_images in [
        ("train", train_images),
        ("validation", val_images),
        ("test", test_images)
    ]:

        destination = DEST / split_name / class_folder.name
        destination.mkdir(parents=True, exist_ok=True)

        for image in split_images:
            shutil.copy2(image, destination / image.name)

    print(
        f"{class_folder.name}: "
        f"train={len(train_images)}, "
        f"validation={len(val_images)}, "
        f"test={len(test_images)}"
    )

print("\nDataset split completed.")
