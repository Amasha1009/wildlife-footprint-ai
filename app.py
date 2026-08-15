import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.title("Wildlife Footprint & Animal Identification")

class_names = [
    "bear",
    "deer",
    "elephant",
    "leopard",
    "wild_boar",
    "wolf"
]

st.sidebar.header("About the Project")

st.sidebar.write(
    "This application identifies wildlife animals "
    "from uploaded images using a MobileNetV3Small "
    "deep learning model."
)

st.sidebar.write("**Model:** MobileNetV3Small")

st.sidebar.write("**Test Accuracy:** 100%")

st.sidebar.subheader("Supported Animals")

for animal in class_names:
    st.sidebar.write(f"• {animal}")

MODEL_PATH = "model/best_wildlife_model.keras"

model = tf.keras.models.load_model(MODEL_PATH)


uploaded_file = st.file_uploader(
    "Upload a wildlife image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image"
    )

    if st.button("Identify Animal"):

        image = image.resize((224, 224))

    image_array = np.array(image)

    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(
        image_array,
        verbose=0
    )

    predicted_index = np.argmax(predictions[0])

    predicted_animal = class_names[predicted_index]

    confidence = float(
        predictions[0][predicted_index]
    ) * 100

    st.subheader("Prediction")

    st.write(
        f"Animal: **{predicted_animal}**"
    )

    st.write(
        f"Confidence: **{confidence:.2f}%**"
    )