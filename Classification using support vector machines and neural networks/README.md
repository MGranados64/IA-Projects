# 🖤 Heart Disease Classification: SVM & Neural Networks

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
</p>

## 🎯 Overview

This repository features a comparative Machine Learning study focused on predicting the presence of heart disease using clinical data. The project comprehensively evaluates and compares the performance of **Support Vector Machines (SVM)** and **Artificial Neural Networks (Multi-Layer Perceptron)**.

By analyzing patient metrics (such as cholesterol, fasting blood sugar, resting ECG, and maximum heart rate), this project demonstrates how to build, tune, and evaluate robust predictive models for healthcare applications.

## 🚀 Key Features & Pipeline

### 1. Exploratory Data Analysis (EDA) & Preprocessing
Clinical datasets are often noisy. To ensure optimal model performance, the data underwent strict preprocessing:
* **Correlation Analysis:** Heatmaps to identify highly correlated clinical features.
* **Outlier Removal:** Using the Interquartile Range (IQR) method to filter out extreme physiological anomalies.
* **Feature Scaling:** Applying `StandardScaler` to normalize features, a crucial step for the convergence of both SVMs and Neural Networks.

### 2. Support Vector Machine (SVM) Classification
Explored how different boundaries separate healthy vs. sick patients:
* Tested multiple kernels (`linear`, `poly`, `rbf`).
* Applied **GridSearchCV** for rigorous hyperparameter tuning (optimizing `C` and `gamma` parameters) to prevent overfitting and maximize recall.

### 3. Artificial Neural Network (ANN / MLP)
Implemented a Multi-Layer Perceptron (`MLPClassifier`) to capture complex, non-linear relationships in the clinical data:
* Experimented with different architectures (number of hidden layers and neurons).
* Tuned activation functions (`relu`, `tanh`) and solvers (`adam`, `sgd`).

### 4. Evaluation Metrics
Models were thoroughly evaluated using:
* **Confusion Matrices:** To explicitly track False Positives and False Negatives (critical in medical diagnoses).
* **Classification Reports:** Comparing Accuracy, Precision, Recall, and F1-Scores across models.

## 💡 Conclusions

* **Data Scaling is Critical:** The Neural Network's performance improved dramatically only after the clinical features were standardized.
* **Model Performance:** Both the tuned SVM (RBF kernel) and the optimized MLP classifier achieved high accuracy. However, proper hyperparameter tuning via GridSearch proved essential to balance precision and recall, ensuring the model reliably identifies true positive heart disease cases without triggering excessive false alarms.

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/MGranados64/heart-disease-classification.git](https://github.com/MGranados64/heart-disease-classification.git)
