# 🐾 AI-Based Wildlife Footprint and Animal Identification System

An end-to-end AI-based web application that identifies wildlife animals from uploaded footprint images using a **MobileNetV3** deep learning model and displays detailed animal information from a local database.

The system combines dataset preparation, deep learning classification, animal information retrieval, and a Streamlit web interface into one complete application.

---

## 🎯 Project Overview

The **AI-Based Wildlife Footprint and Animal Identification System** is designed to assist users in identifying wildlife animals from footprint images.

The application follows this workflow:

```text
                         USER
                           │
                           ▼
                Upload Footprint Image
                           │
                           ▼
                 Image Preprocessing
                      224 × 224
                           │
                           ▼
                    MobileNetV3
                    Deep Learning
                           │
                           ▼
                  Animal Prediction
                           │
                    ┌──────┴──────┐
                    ▼             ▼
              Animal Class    Confidence
                    │
                    ▼
              Animal Database
                    │
          ┌─────────┼──────────┐
          ▼         ▼          ▼
       Photo    Information  Introduction
                    │
                    ▼
              Streamlit Result
```

---

## 🏗️ System Architecture

The project consists of four major components:

### Member 1 — Dataset and Preprocessing

Responsible for preparing the wildlife footprint dataset and preprocessing images for model training.

### Member 2 — MobileNetV3 Model

Responsible for developing, training, evaluating, and providing the trained MobileNetV3 model used for animal prediction.

### Member 3 — Animal Information Database

Responsible for creating the animal information database and collecting reference photographs for the supported animals.

### Member 4 — Streamlit Application

Responsible for integrating all components into one user-friendly application.

The Streamlit application:

1. Accepts an uploaded footprint image.
2. Validates the uploaded image.
3. Preprocesses the image to `224 × 224`.
4. Sends the image to the trained MobileNetV3 model.
5. Obtains the predicted animal class.
6. Calculates the prediction confidence.
7. Retrieves information from `animal_info.csv`.
8. Displays the corresponding animal photograph.
9. Displays scientific name, habitat, diet, activity, conservation status, and introduction.
10. Handles missing files, invalid images, missing database information, and low-confidence predictions.

---

# 👥 Team Work Division

| Member       | Name                           | Branch                 | Main Responsibility                                    |
| ------------ | ------------------------------ | ---------------------- | ------------------------------------------------------ |
| **Member 1** | G.D.H. Devindee                | `member-1-dataset`     | Dataset preparation and preprocessing                  |
| **Member 2** | Bimalsha Kavishan Aththanayaka | `member-2-model`       | MobileNetV3 model development, training and evaluation |
| **Member 3** | P.D.H. Mohotti                 | `member-3-animal-info` | Animal information database and reference photographs  |
| **Member 4** | E.M.H.A.K. Ekanayaka           | `member-4-streamlit`   | Streamlit UI and complete system integration           |

---

# 📁 Repository Structure

```text
wildlife-footprint-ai-git/
│
├── analysis/
│
├── animal_info/
│   ├── animal_info.csv
│   ├── image_sources.csv
│   └── images/
│       ├── bear.jpg
│       ├── deer.jpg
│       ├── elephant.jpg
│       ├── leopard.jpg
│       ├── wild_boar.jpg
│       └── wolf.jpg
│
├── dataset/
│   ├── README.md
│   └── ...
│
├── documentation/
│
├── model/
│   ├── best_wildlife_model.keras
│   ├── wildlife_model.keras
│   ├── train.py
│   ├── predict.py
│   └── evaluate.py
│
├── scripts/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🌿 Supported Animals

The current system supports six wildlife classes:

| Class       | Common Name           | Scientific Name        |
| ----------- | --------------------- | ---------------------- |
| `leopard`   | Leopard               | *Panthera pardus*      |
| `deer`      | Spotted Deer (Chital) | *Axis axis*            |
| `elephant`  | Asian Elephant        | *Elephas maximus*      |
| `wild_boar` | Wild Boar             | *Sus scrofa*           |
| `bear`      | Sloth Bear            | *Melursus ursinus*     |
| `wolf`      | Indian Wolf           | *Canis lupus pallipes* |

The class names used by the application are kept consistent with the trained model:

```text
bear
deer
elephant
leopard
wild_boar
wolf
```

---

# 🧠 Machine Learning Model

The project uses **MobileNetV3** with TensorFlow/Keras for wildlife classification.

The trained model is stored in:

```text
model/best_wildlife_model.keras
```

The application does **not** create another AI model.

The Streamlit application directly loads the trained model provided by Member 2.

---

# 🖼️ Image Processing

Uploaded images are:

1. Loaded using Pillow.
2. Converted to RGB.
3. Resized to:

```text
224 × 224 pixels
```

4. Converted into a NumPy array.
5. A batch dimension is added.
6. The processed image is passed to the trained model.

Example:

```text
Uploaded Image
      ↓
RGB Conversion
      ↓
Resize 224 × 224
      ↓
NumPy Array
      ↓
MobileNetV3
      ↓
Prediction
```

---

# 🌐 Streamlit Application

The main application is:

```text
app.py
```

Run the application using:

```bash
streamlit run app.py
```

The application provides:

### Upload Section

Users can upload:

* `.jpg`
* `.jpeg`
* `.png`

### Prediction Section

The application displays:

```text
Predicted Animal: Leopard

Confidence: 94.20%
```

### Animal Information Section

After prediction, the application retrieves the corresponding record from:

```text
animal_info/animal_info.csv
```

It can display:

* Common name
* Scientific name
* Habitat
* Diet
* Activity
* Conservation status
* Introduction
* Animal photograph

---

# 📊 Animal Information Database

The animal information database is stored at:

```text
animal_info/animal_info.csv
```

The CSV contains:

```text
species_id
common_name
scientific_name
habitat
diet
activity
conservation_status
introduction
image_filename
```

The corresponding photographs are stored in:

```text
animal_info/images/
```

For example:

```text
leopard → leopard.jpg
deer → deer.jpg
elephant → elephant.jpg
wild_boar → wild_boar.jpg
bear → bear.jpg
wolf → wolf.jpg
```

The application automatically matches the predicted `species_id` with the corresponding database record.

---

# ⚠️ Error Handling

The Streamlit application handles common problems including:

### No Image Uploaded

The user is prompted to upload an image before prediction.

### Invalid Image

Invalid or unreadable image files are handled without crashing the application.

### Unsupported File Format

The uploader accepts only:

```text
JPG
JPEG
PNG
```

### Low Confidence

If the model produces a low-confidence prediction, the application can warn the user that the result may be uncertain.

### Missing Animal Information

If the predicted animal does not exist in the animal database, the application displays an appropriate warning instead of crashing.

### Missing Animal Photograph

If an animal photograph cannot be found, the animal information can still be displayed.

### Missing Model

The application checks that the trained model exists before attempting prediction.

---

# 🚀 Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Amasha1009/wildlife-footprint-ai.git
```

Move into the project directory:

```bash
cd wildlife-footprint-ai-git
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

From the project root directory:

```text
C:\Users\User\Desktop\wildlife-footprint-ai-git
```

activate the virtual environment:

```bash
venv\Scripts\activate
```

Then run:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, normally similar to:

```text
http://localhost:8501
```

Open the URL in a web browser.

---

# 🧪 Testing

The application was tested locally before integration.

## Python Syntax Test

```bash
python -m py_compile .\app.py
```

Result:

```text
No errors
```

This confirms that `app.py` contains valid Python syntax.

---

## Animal CSV Test

```bash
python -c "import pandas as pd; df=pd.read_csv('./animal_info/animal_info.csv'); print('CSV OK'); print(df[['species_id','common_name']].to_string(index=False))"
```

Expected result:

```text
CSV OK

species_id    common_name
leopard       Leopard
deer          Spotted Deer (Chital)
elephant      Asian Elephant
wild_boar     Wild Boar
bear          Sloth Bear
wolf          Indian Wolf
```

---

## Model File Test

```powershell
Test-Path .\model\best_wildlife_model.keras
```

Expected result:

```text
True
```

---

## Animal Image Test

```powershell
Test-Path .\animal_info\images\leopard.jpg
```

Expected result:

```text
True
```

---

## Streamlit Test

The application was successfully launched using:

```bash
streamlit run app.py
```

The Streamlit page was displayed successfully.

---

# 🔍 Model Prediction Test

The trained model can also be tested directly using:

```bash
python .\model\predict.py .\animal_info\images\leopard.jpg
```

The model returns a predicted class and confidence score.

> Note: The reference animal photographs in `animal_info/images/` are not necessarily footprint images. Therefore, predictions on these photographs should not be considered an evaluation of footprint classification accuracy. Proper footprint test images should be used for final model testing.

---

# 🔄 Complete Application Workflow

The complete system works as follows:

```text
1. User opens Streamlit application
              ↓
2. User uploads footprint image
              ↓
3. Application validates image
              ↓
4. Image converted to RGB
              ↓
5. Image resized to 224 × 224
              ↓
6. MobileNetV3 model processes image
              ↓
7. Model produces class probabilities
              ↓
8. Highest probability class selected
              ↓
9. Confidence score calculated
              ↓
10. species_id used to search animal_info.csv
              ↓
11. Animal information retrieved
              ↓
12. Corresponding photograph loaded
              ↓
13. Final prediction and animal information displayed
```

---

# 🖥️ Expected User Interface

The application provides an interface similar to:

```text
==================================================
 AI-Based Wildlife Footprint and Animal
 Identification System
==================================================

Upload a footprint image:

[ Choose an image ]

             Uploaded Footprint
             ┌───────────────┐
             │               │
             │    IMAGE      │
             │               │
             └───────────────┘

             [ Identify Animal ]

--------------------------------------------------

Prediction

Animal: Leopard
Confidence: 94.20%

--------------------------------------------------

Animal Information

             [ Leopard Photo ]

Common Name:
Leopard

Scientific Name:
Panthera pardus

Habitat:
Dense forests, grasslands, rocky hills

Diet:
Carnivorous

Activity:
Nocturnal / Crepuscular

Conservation Status:
Vulnerable

About the Animal:
Short animal introduction...
```

---

# 🌳 Git Branching Strategy

Each team member works on a separate branch.

Current project branches:

```text
main
member-2-model
member-3-animal-info
member-4-streamlit
```

Member 4's active branch:

```text
member-4-streamlit
```

---

# 🤝 Git Workflow

## Check Current Branch

```bash
git branch
```

Switch to Member 4's branch:

```bash
git checkout member-4-streamlit
```

---

## Check Changes

```bash
git status
```

---

## Add Changes

```bash
git add app.py
git add animal_info/animal_info.csv
git add README.md
```

Or:

```bash
git add .
```

---

## Commit Changes

```bash
git commit -m "Complete Streamlit wildlife identification application"
```

---

## Push to GitHub

```bash
git push origin member-4-streamlit
```

---

# 🔀 Pull Request

After pushing the Member 4 branch:

1. Open the GitHub repository.
2. Select the `member-4-streamlit` branch.
3. Create a Pull Request.
4. Set the destination branch to `main`.
5. Review the changes.
6. Merge the Pull Request after the team confirms that the application works correctly.

The final `main` branch should contain the integrated work of all four members.

---

# 📌 Important Development Rules

* Do not create another AI model in the Streamlit branch.
* Do not unnecessarily modify Member 2's trained model.
* Keep the six model class names unchanged.
* Use the existing MobileNetV3 model.
* Use the existing animal information database.
* Keep the animal photograph filenames consistent with `animal_info.csv`.
* Test the application before creating the Pull Request.
* Keep sensitive credentials and API keys out of the repository.

---

# 🛠️ Technologies Used

| Technology  | Purpose                                    |
| ----------- | ------------------------------------------ |
| Python      | Application programming language           |
| TensorFlow  | Deep learning framework                    |
| Keras       | Model loading and inference                |
| MobileNetV3 | Wildlife image classification              |
| NumPy       | Image array processing                     |
| Pillow      | Image loading and conversion               |
| Pandas      | Animal information CSV processing          |
| Streamlit   | Web application interface                  |
| Git         | Version control                            |
| GitHub      | Team collaboration and source code hosting |

---

# 👨‍💻 Team Contributions

### Member 1 — G.D.H. Devindee

Responsible for:

* Wildlife footprint dataset
* Dataset organization
* Image preprocessing
* Dataset documentation

### Member 2 — Bimalsha Kavishan Aththanayaka

Responsible for:

* MobileNetV3 model
* Model training
* Model evaluation
* Prediction functionality
* Model files

### Member 3 — P.D.H. Mohotti

Responsible for:

* Animal information database
* Animal descriptions
* Animal photographs
* Image source documentation

### Member 4 — E.M.H.A.K. Ekanayaka

Responsible for:

* Streamlit web interface
* Image upload functionality
* Model integration
* Prediction display
* Confidence display
* Animal database integration
* Animal photograph display
* Error handling
* End-to-end application testing

---

# 📈 Future Improvements

Possible future improvements include:

* Increasing the number of footprint images per species.
* Adding more wildlife species.
* Improving model accuracy with a larger real-world dataset.
* Adding image preprocessing and augmentation improvements.
* Adding prediction history.
* Improving the visual design of the Streamlit interface.
* Deploying the application online using Streamlit Community Cloud.
* Adding more detailed wildlife conservation information.

---

# 📄 Project Status

**Current Status:** Integrated Streamlit application

The project currently includes:

* ✅ Wildlife dataset structure
* ✅ MobileNetV3 trained model
* ✅ Animal information CSV
* ✅ Animal reference photographs
* ✅ Streamlit interface
* ✅ Image upload
* ✅ Image preprocessing
* ✅ Model prediction
* ✅ Confidence calculation
* ✅ Animal information retrieval
* ✅ Animal photograph retrieval
* ✅ Error handling
* ✅ Local Streamlit testing

---

# 🐾 Final System

The final system combines all four team members' contributions:

```text
Member 1
Dataset & Preprocessing
        │
        ▼
Member 2
MobileNetV3 Model
        │
        ▼
Member 4
Streamlit Integration
        │
        ├──────────────► Member 3
        │                Animal Information
        │
        ▼
Complete Wildlife Identification System
```

The final objective is:

```text
UPLOAD FOOTPRINT
       ↓
PREPROCESS IMAGE
       ↓
MOBILENETV3 PREDICTION
       ↓
ANIMAL + CONFIDENCE
       ↓
ANIMAL DATABASE
       ↓
PHOTO + INFORMATION
       ↓
USER
```
#GitHub Repository Link
https://github.com/Amasha1009/wildlife-footprint-ai.git

#Live Demo Link 
https://wildlife-footprint-ai-jre8xwhbz4r7hwudbcxueh.streamlit.app/

**AI-Based Wildlife Footprint and Animal Identification System**
*An integrated machine learning application for wildlife footprint identification.*
