import os

import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf
from PIL import Image


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Wildlife Footprint Identification",
    page_icon="🐾",
    layout="centered"
)


# ---------------------------------------------------------
# Project title
# ---------------------------------------------------------

st.title("🐾 AI-Based Wildlife Footprint and Animal Identification System")

st.write(
    "Upload an animal footprint image and our MobileNetV3 AI model "
    "will predict the animal species and display basic information."
)


# ---------------------------------------------------------
# File paths
# ---------------------------------------------------------

MODEL_PATH = "model/best_wildlife_model.keras"
INFO_PATH = "animal_info/animal_info.csv"
IMAGE_DIR = "animal_info/images"


# ---------------------------------------------------------
# Model classes
# IMPORTANT: These must match Member 2's model exactly
# ---------------------------------------------------------

class_names = [
    "bear",
    "deer",
    "elephant",
    "leopard",
    "wild_boar",
    "wolf"
]


# ---------------------------------------------------------
# Load model
# ---------------------------------------------------------

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


# ---------------------------------------------------------
# Load animal information
# ---------------------------------------------------------

@st.cache_data
def load_animal_info():
    return pd.read_csv(INFO_PATH)


# ---------------------------------------------------------
# Prediction function
# ---------------------------------------------------------

def predict_animal(image, model):
    """
    Predict the animal from an uploaded image.

    Returns:
        predicted_animal: animal class name
        confidence: prediction confidence as a percentage
    """

    image = image.resize((224, 224))

    image_array = np.array(image, dtype=np.float32)

    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(
        image_array,
        verbose=0
    )

    predicted_index = int(np.argmax(predictions[0]))

    predicted_animal = class_names[predicted_index]

    confidence = float(
        predictions[0][predicted_index]
    ) * 100

    return predicted_animal, confidence


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.header("ℹ️ About the Project")

st.sidebar.write(
    "This application uses a MobileNetV3 deep learning model "
    "to identify wildlife animals from footprint images."
)

st.sidebar.write("**AI Model:** MobileNetV3")
st.sidebar.write("**Input Size:** 224 × 224 pixels")

st.sidebar.subheader("Supported Animals")

for animal in class_names:
    st.sidebar.write(
        f"- {animal.replace('_', ' ').title()}"
    )


# ---------------------------------------------------------
# Check required files
# ---------------------------------------------------------

if not os.path.exists(MODEL_PATH):
    st.error(
        f"Model file not found: {MODEL_PATH}"
    )
    st.stop()

if not os.path.exists(INFO_PATH):
    st.error(
        f"Animal information file not found: {INFO_PATH}"
    )
    st.stop()

if not os.path.exists(IMAGE_DIR):
    st.error(
        f"Animal image folder not found: {IMAGE_DIR}"
    )
    st.stop()


# ---------------------------------------------------------
# Load resources
# ---------------------------------------------------------

try:
    model = load_model()
    animal_info = load_animal_info()

except Exception as e:
    st.error(
        f"Could not load the application resources: {e}"
    )
    st.stop()


# ---------------------------------------------------------
# Image upload
# ---------------------------------------------------------

st.subheader("📤 Upload a Footprint Image")

uploaded_file = st.file_uploader(
    "Choose an animal footprint image",
    type=["jpg", "jpeg", "png"]
)


# ---------------------------------------------------------
# Process uploaded image
# ---------------------------------------------------------

if uploaded_file is not None:

    try:
        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Footprint Image",
            width="stretch"
        )

    except Exception:
        st.error(
            "The uploaded file is not a valid image."
        )
        st.stop()

    st.write("")

    if st.button(
        "🔍 Identify Animal",
        type="primary",
        width="stretch"
    ):

        try:
            predicted_animal, confidence = predict_animal(
                image,
                model
            )

            # -------------------------------------------------
            # Prediction result
            # -------------------------------------------------

            st.subheader("🎯 Prediction")

            display_name = (
                predicted_animal
                .replace("_", " ")
                .title()
            )

            st.success(
                f"Animal: {display_name}"
            )

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )


            # -------------------------------------------------
            # Low-confidence warning
            # -------------------------------------------------

            if confidence < 50:
                st.warning(
                    "The prediction confidence is low. "
                    "Please try another clear footprint image."
                )


            # -------------------------------------------------
            # Retrieve animal information
            # -------------------------------------------------

            matching_rows = animal_info[
                animal_info["species_id"] == predicted_animal
            ]

            if matching_rows.empty:

                st.warning(
                    "Animal information is not available "
                    "for this predicted species."
                )

            else:

                animal = matching_rows.iloc[0]

                st.subheader("🐾 Animal Information")


                # -------------------------------------------------
                # Animal photograph
                # -------------------------------------------------

                image_filename = str(
                    animal["image_filename"]
                )

                animal_image_path = os.path.join(
                    IMAGE_DIR,
                    image_filename
                )

                if os.path.exists(animal_image_path):

                    st.image(
                        animal_image_path,
                        caption=animal["common_name"],
                        width="stretch"
                    )

                else:

                    st.warning(
                        "Animal photograph not found."
                    )


                # -------------------------------------------------
                # Animal details
                # -------------------------------------------------

                st.markdown(
                    f"**Common Name:** {animal['common_name']}"
                )

                st.markdown(
                    f"**Scientific Name:** "
                    f"*{animal['scientific_name']}*"
                )

                st.markdown(
                    f"**Habitat:** {animal['habitat']}"
                )

                st.markdown(
                    f"**Diet:** {animal['diet']}"
                )

                st.markdown(
                    f"**Activity:** {animal['activity']}"
                )

                st.markdown(
                    f"**Conservation Status:** "
                    f"{animal['conservation_status']}"
                )

                st.markdown("### About the Animal")

                st.write(
                    animal["introduction"]
                )


        except Exception as e:

            st.error(
                f"An error occurred during prediction: {e}"
            )

else:

    st.info(
        "Please upload a footprint image to begin."
    )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "AI-Based Wildlife Footprint and Animal Identification System "
    "| MobileNetV3 + Streamlit"
)