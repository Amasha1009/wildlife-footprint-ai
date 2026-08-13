# AI-Based Wildlife Footprint and Animal Identification System

## Member 1 - Dataset Collection, Analysis and Preprocessing

### 1\. Dataset

Dataset Name: OpenAnimalTracks

Dataset Purpose:
Animal footprint/track recognition.

Dataset Source:
OpenAnimalTracks - Risa Shinoda and Kaede Shiohara, ICIP 2024.

Official Repository:
https://github.com/dahlian00/OpenAnimalTracks

Research Paper:
OpenAnimalTracks: A Dataset for Animal Track Recognition
arXiv:2406.09647

### 2\. Dataset Information

The OpenAnimalTracks dataset contains footprint images from 18 wild animal species.

The exact number of images per species will be recorded after the dataset is received and analyzed.

|Class|Original Images|Valid Images|Corrupted|Final Images|
|-|-:|-:|-:|-:|
|To be analyzed|-|-|-|-|

### 3\. Dataset Cleaning

The dataset will be checked for:

* Missing images
* Corrupted images
* Duplicate images
* Incorrect labels
* Very poor-quality images

### 4\. Image Preprocessing

The selected images will be prepared for MobileNetV3.

Planned preprocessing:

* Convert images to RGB
* Resize images to 224 x 224 pixels
* Apply appropriate normalization
* Apply data augmentation to training images only

### 5\. Dataset Split

The cleaned dataset will be divided into:

* Training set - 70%
* Validation set - 15%
* Test set - 15%

The final number of images in each class will be recorded after the dataset is analyzed.

### 6\. Final Animal Classes

The final 5-8 animal classes will be selected based on:

* Number of available images
* Image quality
* Label quality
* Class balance
* Suitability for footprint classification

The classes will NOT be selected until the actual dataset has been analyzed.

### 7\. Dataset Analysis

A Python script has been created to analyze:

* Number of classes
* Number of images per class
* Total valid images
* Corrupted images

Script:

scripts/analyze\_dataset.py

### 8\. Current Status

Dataset request submitted to the OpenAnimalTracks authors.

Waiting for access to the actual dataset.

No final animal classes have been selected yet because the actual dataset must be examined first.

### 9\. Member 2 Handover

After cleaning and preprocessing, the final dataset will be provided in:

dataset/split/

The structure will be:

dataset/split/
+-- train/
+-- validation/
+-- test/

Member 2 can use these folders to train the MobileNetV3 classification model.

