🔐 Multi-Modal Biometrics for Mobile Authentication

A deep learning-based authentication system that combines Face Recognition and Fingerprint Recognition to improve the accuracy, security, and reliability of mobile user authentication.

📌 Overview

Traditional authentication methods such as passwords and PINs are vulnerable to theft, brute-force attacks, and social engineering. Biometric authentication offers a more secure alternative, but relying on a single biometric trait can still lead to false positives or false negatives.

This project implements a multi-modal biometric authentication system by combining facial and fingerprint features using a Convolutional Neural Network (CNN). The fusion of two independent biometric modalities significantly improves authentication performance compared to single-modal systems.

✨ Features
👤 Face recognition using CNN-based feature extraction
🖐️ Fingerprint recognition with image preprocessing
🔗 Feature-level fusion of facial and fingerprint embeddings
📊 Performance evaluation using Accuracy, FAR, FRR, and EER
📈 Training and validation visualizations
🧠 Deep learning-based classification
📱 Designed for mobile authentication research
🏗️ Project Architecture
Face Dataset
      │
      ▼
Face Preprocessing
      │
      ▼
 CNN Feature Extractor
      │
      ├──────────────┐
      │              │
      ▼              ▼
Fingerprint     Fingerprint
 Dataset       Preprocessing
                     │
                     ▼
            CNN Feature Extractor
                     │
                     ▼
            Feature-Level Fusion
                     │
                     ▼
           Fully Connected Layers
                     │
                     ▼
      Genuine / Impostor Prediction
🛠️ Tech Stack
Python
TensorFlow / Keras
OpenCV
NumPy
Matplotlib
Scikit-learn
Jupyter Notebook / Google Colab
📂 Dataset
Face Dataset

Human Faces Dataset from Kaggle

Images of multiple individuals
Used for learning facial embeddings
Fingerprint Dataset

FVC2000 DB4 Fingerprint Dataset

Multiple fingerprint impressions
Used for fingerprint feature extraction

The datasets are not included in this repository due to size and licensing restrictions.

⚙️ Workflow
Load face and fingerprint datasets
Preprocess images
Resize
Normalize
Noise reduction
Train separate CNN feature extractors
Generate embeddings
Fuse embeddings using feature-level fusion
Train fusion classifier
Evaluate authentication performance
Visualize metrics and results
📊 Evaluation Metrics

The model is evaluated using:

Accuracy
Precision
Recall
F1 Score
False Acceptance Rate (FAR)
False Rejection Rate (FRR)
Equal Error Rate (EER)
📈 Results

The multi-modal approach demonstrates better authentication performance than individual face-only or fingerprint-only models by reducing both false acceptance and false rejection rates.

Example outputs include:

Training Accuracy Curve
Validation Accuracy Curve
Loss Curve
Confusion Matrix
ROC Curve
FAR vs FRR Plot
📁 Project Structure
Multi-Modal-Biometrics/
│
├── data/
│   ├── faces/
│   └── fingerprints/
│
├── models/
│
├── notebooks/
│
├── src/
│   ├── preprocessing.py
│   ├── face_model.py
│   ├── fingerprint_model.py
│   ├── fusion_model.py
│   └── evaluate.py
│
├── results/
│
├── requirements.txt
│
└── README.md
