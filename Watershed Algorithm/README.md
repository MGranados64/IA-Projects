# 🌊 Image Segmentation: Watershed Algorithm

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
</p>

## 🎯 Overview

This repository demonstrates a robust image segmentation pipeline using the **Watershed Algorithm**.
The primary objective is to accurately subdivide an image into its constituent regions and isolate distinct objects from the background. 

This project explores the "topographical" approach of the Watershed transform, where pixel intensities are treated as elevations. By simulating the "flooding" of these basins, we can perfectly delineate complex overlapping objects (like coins in an image).

## 🚀 Key Features & Pipeline

To prevent the common issue of over-segmentation in Watershed applications , this project implements a rigorous pre-processing and marker-identification pipeline:

1. **Pre-processing:**
   * Grayscale conversion and CLAHE (Contrast Limited Adaptive Histogram Equalization) for better detail definition.
   * Application of a **Gaussian Blur (9x9 kernel)** to smooth details and focus only on outer object boundaries.
2. **Otsu's Thresholding:**
   * Automatic and optimal binarization by minimizing intra-class variance and maximizing inter-class variance.
3. **Morphological Gradient (Noise Removal):**
   * Emphasizing object borders by subtracting the erosion of the image from its dilation.
4. **Marker Identification (Distance Transform):**
   * Calculating the distance of white pixels to the nearest black pixel to confidently separate the foreground (sure objects) from the background.
   * Generating unique labels (markers) to guide the final flooding process.
5. **Watershed Transform:**
   * Applying `cv.watershed` to compute the exact boundaries based on the defined markers and drawing the contours over the original image.

## 💡 Use Cases & Conclusions

The results prove that while the algorithm is highly sensitive to noise , combining it with Euclidean distance transforms and morphological operations yields highly accurate boundary detection. 

This approach is highly valuable for domains requiring precise object separation, such as:
* Medical imaging segmentation.
* Biological image processing (e.g., cell counting).
* Spatial/Satellite imagery analysis.

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/MGranados64/watershed-segmentation.git](https://github.com/MGranados64/watershed-segmentation.git)
