# 🩺 Fetal State Classification: Anomaly Detection & Clustering

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/SciPy-8CAAEE?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy" />
</p>

## 🎯 Overview

This repository focuses on applying advanced Machine Learning techniques for anomaly detection and data clustering in the medical field. [cite_start]The project utilizes a Cardiotocography (CTG) dataset to measure fetal heart rate and uterine contractions during pregnancy and labor[cite: 753, 754]. [cite_start]The ultimate goal is to process complex biological data and accurately classify the fetal state[cite: 787].

## 🚀 Key Features & Pipeline

### 1. Exploratory Data Analysis (EDA)
[cite_start]Thorough data preprocessing and visualization to understand variable distributions and handle missing/imbalanced data[cite: 1380, 1459]:
* [cite_start]**Statistical Summaries & Correlation Matrices:** Identifying highly correlated variables[cite: 945, 1038].
* [cite_start]**Boxplots & Histograms:** Visualizing data skewness and preliminary outlier presence across numeric variables[cite: 1041, 1110, 1118].
* [cite_start]**Missing Value Treatment:** Cleaning the dataset systematically to ensure robust model training[cite: 1191].

### 2. Anomaly Detection Models
A comparative approach to identify outliers and anomalous medical readings using four different methodologies:
* [cite_start]**Interquartile Range (IQR):** Statistical baseline for identifying univariate dispersion[cite: 1468].
* [cite_start]**Isolation Forest:** Tree-based algorithm highly efficient for multi-dimensional medical data[cite: 1601, 1604].
* [cite_start]**Local Outlier Factor (LOF):** Density-based detection, excellent for identifying local anomalies in irregular clusters[cite: 1667, 1668, 2080].
* [cite_start]**OneClassSVM:** Boundary-learning model for robust outlier classification[cite: 1711, 1713].

### 3. Feature Selection & Clustering
To ensure optimal grouping of the fetal states, feature importance was evaluated before clustering:
* [cite_start]**Random Forest Permutation Importance:** Used to extract the variables with the highest predictive weight (e.g., `CLASS`, `E`, `DP`)[cite: 1851, 1857, 1884].
* **K-Means Clustering:** Applied to the selected features. [cite_start]The optimal number of clusters (k=3) was determined using the Elbow Method and visualized in a 3D scatter plot[cite: 1890, 1918, 1946].
* [cite_start]**Agglomerative Hierarchical Clustering:** Visualized through a Dendrogram to validate grouping structures without predefined cluster counts[cite: 1987, 2023, 2047].

## 💡 Use Cases & Conclusions

[cite_start]The comparative study yielded crucial insights into model selection for medical datasets[cite: 2051]:
* [cite_start]**Isolation Forest** proved to be the most computationally efficient and robust method for high-dimensional clinical data with complex anomalies[cite: 2065, 2068].
* [cite_start]**LOF** showed high sensitivity for local outliers but was more computationally expensive[cite: 2080, 2087].
* [cite_start]Proper feature selection prior to **K-Means** prevents poor cluster distribution, while **Dendrograms** offer a superior visual understanding of hierarchical clinical relationships[cite: 2089, 2090, 2094].

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/MGranados64/ctg-anomaly-detection.git](https://github.com/MGranados64/ctg-anomaly-detection.git)
