# 🧠 Deep Learning: Convolutional Neural Network (CNN) Case Study

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
</p>

## 🎯 Overview

This repository presents a comprehensive case study on designing, training, and evaluating a **Convolutional Neural Network (CNN)** for advanced image classification. 

The primary objective of this project is to demonstrate how deep learning architectures can automatically learn spatial hierarchies of features from input images. By building a custom CNN pipeline, this study tackles the challenges of image feature extraction, overcoming overfitting, and optimizing neural network hyperparameters.

## 🚀 Key Features & Pipeline

### 1. Data Preprocessing & Augmentation
Image datasets require careful preparation to improve model generalization:
* **Rescaling & Normalization:** Scaling pixel values to a standard range (e.g., 0 to 1) for faster convergence.
* **Data Augmentation:** Applying random rotations, flips, and zooms to artificially expand the training dataset and make the model robust against spatial variations.

### 2. CNN Architecture Design
The network was built sequentially to capture both low-level edges and high-level semantic features:
* **Convolutional Layers (Conv2D):** Extracting feature maps using moving filters.
* **Pooling Layers (MaxPooling2D):** Downsampling spatial dimensions to reduce computational load and prevent overfitting.
* **Fully Connected Layers (Dense):** Flattening the 2D matrices into a 1D vector to perform the final classification.
* **Regularization:** Implementing `Dropout` layers to randomly deactivate neurons during training, enforcing robust feature learning.

### 3. Model Training & Optimization
* **Loss Function:** Categorical Cross-Entropy for multi-class classification.
* **Optimizer:** Adam optimizer for adaptive learning rates.
* **Callbacks:** Implementation of `EarlyStopping` to halt training when validation loss stops improving, saving the best model weights.

### 4. Evaluation Metrics
* Tracking **Accuracy** and **Loss** across epochs.
* Generating a **Confusion Matrix** to analyze class-specific predictions and identify misclassifications.

## 💡 Conclusions

* **Feature Extraction:** The CNN successfully learned to identify key visual patterns without manual feature engineering.
* **Generalization:** Data augmentation and Dropout layers were critical in bridging the gap between training accuracy and validation accuracy, effectively mitigating overfitting.
* **Architecture Depth:** Adding deeper convolutional blocks allowed the model to grasp more complex features, though it required careful tuning of the learning rate to ensure stable convergence.

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/MGranados64/cnn-case-study.git](https://github.com/MGranados64/cnn-case-study.git)
