# 🩺 Fetal State Classification: Anomaly Detection & Clustering

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/SciPy-8CAAEE?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy" />
</p>

## 🎯 Overview

This repository focuses on applying advanced Machine Learning techniques for anomaly detection and data clustering in the medical field. The project utilizes a Cardiotocography (CTG) dataset to measure fetal heart rate and uterine contractions during pregnancy and labor. The ultimate goal is to process complex biological data and accurately classify the fetal state.

## 🚀 Key Features & Pipeline

### 1. Exploratory Data Analysis (EDA)
Thorough data preprocessing and visualization to understand variable distributions and handle missing/imbalanced data:
* **Statistical Summaries & Correlation Matrices:** Identifying highly correlated variables.
* **Boxplots & Histograms:** Visualizing data skewness and preliminary outlier presence across numeric variables.
* **Missing Value Treatment:** Cleaning the dataset systematically to ensure robust model training.

### 2. Anomaly Detection Models
A comparative approach to identify outliers and anomalous medical readings using four different methodologies:
* **Interquartile Range (IQR):** Statistical baseline for identifying univariate dispersion.
* **Isolation Forest:** Tree-based algorithm highly efficient for multi-dimensional medical data.
* **Local Outlier Factor (LOF):** Density-based detection, excellent for identifying local anomalies in irregular clusters.
* **OneClassSVM:** Boundary-learning model for robust outlier classification.

### 3. Feature Selection & Clustering
To ensure optimal grouping of the fetal states, feature importance was evaluated before clustering:
* **Random Forest Permutation Importance:** Used to extract the variables with the highest predictive weight (e.g., `CLASS`, `E`, `DP`).
* **K-Means Clustering:** Applied to the selected features. The optimal number of clusters (k=3) was determined using the Elbow Method and visualized in a 3D scatter plot.
* **Agglomerative Hierarchical Clustering:** Visualized through a Dendrogram to validate grouping structures without predefined cluster counts.

## 💡 Use Cases & Conclusions

The comparative study yielded crucial insights into model selection for medical datasets:
* **Isolation Forest** proved to be the most computationally efficient and robust method for high-dimensional clinical data with complex anomalies.
* **LOF** showed high sensitivity for local outliers but was more computationally expensive.
* Proper feature selection prior to **K-Means** prevents poor cluster distribution, while **Dendrograms** offer a superior visual understanding of hierarchical clinical relationships.

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/MGranados64/ctg-anomaly-detection.git](https://github.com/MGranados64/ctg-anomaly-detection.git)
