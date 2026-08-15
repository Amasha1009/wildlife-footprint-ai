import tensorflow as tf
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

# Paths
TEST_DIR = "dataset/split/test"
MODEL_PATH = "model/best_wildlife_model.keras"

# Settings
IMG_SIZE = (224, 224)
BATCH_SIZE = 8

# Class names
class_names = [
    "bear",
    "deer",
    "elephant",
    "leopard",
    "wild_boar",
    "wolf"
]

# Load trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Load test dataset
test_dataset = tf.keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# Get true labels and predictions
true_labels = []
predicted_labels = []

for images, labels in test_dataset:
    predictions = model.predict(images, verbose=0)

    predicted_classes = np.argmax(predictions, axis=1)

    true_labels.extend(labels.numpy())
    predicted_labels.extend(predicted_classes)

# Convert to NumPy arrays
true_labels = np.array(true_labels)
predicted_labels = np.array(predicted_labels)

# Confusion matrix
cm = confusion_matrix(
    true_labels,
    predicted_labels
)

print("\nConfusion Matrix:")
print(cm)

# Classification report
print("\nClassification Report:")
print(
    classification_report(
        true_labels,
        predicted_labels,
        target_names=class_names
    )
)