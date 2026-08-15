import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.title("🐾 Wildlife Footprint & Animal Identification")

class_names = [
    "🐻bear",
    "🦌deer",
    "🐘elephant",
    "🐆leopard",
    "🐗wild_boar",
    "🐺wolf"
]

# Sidebar
st.sidebar.header("ℹ️ About the Project")

st.sidebar.write(
    "This application identifies wildlife animals "
    "from uploaded images using a MobileNetV3Small "
    "deep learning model."
)

st.sidebar.write("**Model:** MobileNetV3Small")
st.sidebar.write("**Test Accuracy:** 70%")

st.sidebar.subheader("Supported Animals")

for animal in class_names:
    st.sidebar.write(f"- {animal}")

# Load model
MODEL_PATH = "model/best_wildlife_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Upload image
uploaded_file = st.file_uploader(
    "Upload a wildlife image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="📁Uploaded Image"
    )

    # Button
    if st.button("Identify Animal"):

        # Resize image
        resized_image = image.resize((224, 224))

        # Convert image to NumPy array
        image_array = np.array(resized_image)

        # Add batch dimension
        image_array = np.expand_dims(
            image_array,
            axis=0
        )

        # Make prediction
        predictions = model.predict(
            image_array,
            verbose=0
        )

        # Get predicted class
        predicted_index = np.argmax(predictions[0])

        predicted_animal = class_names[predicted_index]

        # Get confidence
        confidence = float(
            predictions[0][predicted_index]
        ) * 100

        # Display result
        st.subheader("🎯Prediction")

        st.write(
            f"🐾Animal: **{predicted_animal.replace('_', ' ').title()}**"
        )

        st.write(
            f"📊Confidence: **{confidence:.2f}%**"
        )