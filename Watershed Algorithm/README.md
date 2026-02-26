# 🌊 Image Segmentation: Watershed Algorithm

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
</p>

## 🎯 Overview

[cite_start]This repository demonstrates a robust image segmentation pipeline using the **Watershed Algorithm**[cite: 576, 582]. [cite_start]The primary objective is to accurately subdivide an image into its constituent regions and isolate distinct objects from the background[cite: 578, 580]. 

[cite_start]This project explores the "topographical" approach of the Watershed transform, where pixel intensities are treated as elevations[cite: 583]. [cite_start]By simulating the "flooding" of these basins, we can perfectly delineate complex overlapping objects (like coins in an image)[cite: 584, 702, 706].

## 🚀 Key Features & Pipeline

[cite_start]To prevent the common issue of over-segmentation in Watershed applications [cite: 742][cite_start], this project implements a rigorous pre-processing and marker-identification pipeline[cite: 685, 742]:

1. **Pre-processing:**
   * [cite_start]Grayscale conversion and CLAHE (Contrast Limited Adaptive Histogram Equalization) for better detail definition[cite: 586, 606, 607].
   * [cite_start]Application of a **Gaussian Blur (9x9 kernel)** to smooth details and focus only on outer object boundaries[cite: 612].
2. **Otsu's Thresholding:**
   * [cite_start]Automatic and optimal binarization by minimizing intra-class variance and maximizing inter-class variance[cite: 621, 622].
3. **Morphological Gradient (Noise Removal):**
   * [cite_start]Emphasizing object borders by subtracting the erosion of the image from its dilation[cite: 646, 648, 649].
4. **Marker Identification (Distance Transform):**
   * [cite_start]Calculating the distance of white pixels to the nearest black pixel to confidently separate the foreground (sure objects) from the background[cite: 664].
   * [cite_start]Generating unique labels (markers) to guide the final flooding process[cite: 686, 687, 688].
5. **Watershed Transform:**
   * [cite_start]Applying `cv.watershed` to compute the exact boundaries based on the defined markers and drawing the contours over the original image[cite: 709, 723].

## 💡 Use Cases & Conclusions

[cite_start]The results prove that while the algorithm is highly sensitive to noise [cite: 742][cite_start], combining it with Euclidean distance transforms and morphological operations yields highly accurate boundary detection[cite: 742, 744]. 

This approach is highly valuable for domains requiring precise object separation, such as:
* [cite_start]Medical imaging segmentation[cite: 743].
* [cite_start]Biological image processing (e.g., cell counting)[cite: 743].
* [cite_start]Spatial/Satellite imagery analysis[cite: 743].

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/MGranados64/watershed-segmentation.git](https://github.com/MGranados64/watershed-segmentation.git)
