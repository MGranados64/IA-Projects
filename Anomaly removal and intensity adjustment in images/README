# 🖼️ Image Conditioning: Noise Removal and Intensity Adjustment

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
</p>

## 🎯 Overview

This repository contains a comprehensive laboratory practice focused on the fundamental concepts and basic filtering techniques of digital image processing. The primary goal is to understand how to condition acquired images by dealing with common anomalies (like noise) and poor contrast.

Instead of just applying high-level libraries, this project takes a **comparative approach**, developing mathematical filtering and equalization functions from scratch and comparing their performance against industry-standard tools like **OpenCV**.

## 🚀 Key Features & Methodology

The project is divided into two main analytical sections:

### 1. Noise Injection and Removal
Images were artificially contaminated with specific noise distributions to test filter robustness:
* **Salt & Pepper Noise:** Saturation of pixels to the upper (salt) and lower (pepper) limits.
* **Random Pepper Noise:** Randomly distributed low-intensity saturation.
* **Filtering Approach:** Implementation of a custom **5x5 Median Filter** algorithm to preserve edges while removing noise, directly compared against OpenCV's `cv.medianBlur`.

### 2. Intensity Adjustment (Histogram Equalization)
To fix poorly contrasted images, histogram manipulation techniques were applied:
* **Manual Equalization:** Using a Cumulative Distribution Function (CDF) to uniformly distribute gray-level ranges, enhancing image details mathematically.
* **OpenCV Equalization:** Using `cv.equalizeHist` for baseline comparison.

## 📊 Evaluation Metrics

To objectively evaluate the perceptive image quality and the efficiency of the applied filters, the following metrics were calculated:
* **MSE (Mean Squared Error):** Measures the average squared difference between pixel values.
* **PSNR (Peak Signal-to-Noise Ratio):** Quantifies the amount of noise or distortion present.
* **SSIM (Structural Similarity Index):** Evaluates structural similarity considering luminance, contrast, and structure.

*Result highlight: The custom 5x5 median filter achieved slightly better MSE, PSNR, and SSIM scores compared to the default OpenCV implementation, demonstrating high efficiency in preserving original image features.*

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/MGranados64/image-conditioning.git](https://github.com/MGranados64/image-conditioning.git)
