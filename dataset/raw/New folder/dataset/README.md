# 👩 Member 1: Footprint Dataset Documentation

## Overview
This directory contains the footprint image dataset used for training, validating, and testing our **MobileNetV3** wildlife identification model.

## Supported Classes (6 Species)
1. `leopard`
2. `deer`
3. `elephant`
4. `wild_boar`
5. `bear`
6. `wolf`

## Directory Structure
```
dataset/
├── download_dataset.py       # Script to generate / download local dataset
├── data/                     # Data directory split by class subfolders
│   ├── leopard/
│   ├── deer/
│   ├── elephant/
│   ├── wild_boar/
│   ├── bear/
│   └── wolf/
└── README.md
```

## How to Prepare Dataset
Run the python script to construct the dataset folder:
```bash
python dataset/download_dataset.py
```
This generates 30 synthetic benchmark images per class ($224 \times 224$ pixels) formatted for MobileNetV3 input.
