import sys
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
MODEL_PATH = "model/best_wildlife_model.keras"

model = tf.keras.models.load_model(MODEL_PATH)

# Class names
class_names = [
    "bear",
    "deer",
    "elephant",
    "leopard",
    "wild_boar",
    "wolf"
]

# Check whether an image path was provided
if len(sys.argv) < 2:
    print("Please provide an image path.")
    print("Example:")
    print(r"python .\model\predict.py dataset\split\test\bear\bear_001.jpg")
    sys.exit(1)

# Get image path from command line
image_path = sys.argv[1]

# Load image
image = Image.open(image_path).convert("RGB")

# Resize image
image = image.resize((224, 224))

# Convert image to NumPy array
image_array = np.array(image)

# Add batch dimension
image_array = np.expand_dims(image_array, axis=0)

# Make prediction
predictions = model.predict(image_array, verbose=0)

# Get predicted class
predicted_index = np.argmax(predictions[0])
predicted_class = class_names[predicted_index]
confidence = predictions[0][predicted_index] * 100

print("Predicted animal:", predicted_class)
print(f"Confidence: {confidence:.2f}%")