# 🎨 Deep Learning: Neural Style Transfer (PyTorch)

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=000" alt="Hugging Face" />
  <img src="https://img.shields.io/badge/Gradio-FF7C00?style=for-the-badge&logo=gradio&logoColor=white" alt="Gradio" />
</p>

## 🎯 Project Overview

This repository contains an advanced implementation of **Neural Style Transfer** using PyTorch. The algorithm takes two images (a "content" base image and an artistic "style" image) and optimizes a blank canvas to blend them together. It preserves the semantic structure of the content image while adopting the textures, brushstrokes, and color palette of the style image.

🚀 **Try it live!** I have deployed this model as an interactive web application built with **Gradio**. You can upload your own images and apply style transfer directly from your browser in my **Hugging Face** Space:  
👉 **[Live Demo: Neural Style Transfer on Hugging Face](https://huggingface.co/spaces/MGC1991MF/NeuralStyleTransfer)**

## ⚙️ Key Features & Architecture

### 1. Dynamic Image Preprocessing
The input pipeline is designed to be robust and automatically adapt to the available hardware:
* **GPU Acceleration:** The code automatically detects CUDA availability (`torch.device("cuda" if torch.cuda.is_available() else "cpu")`) to accelerate tensor processing.
* **Intelligent Scaling:** To prevent Out-Of-Memory (OOM) errors, the model dynamically sets the image size to 1024px if running on a GPU, or scales it down to 512px if running on a CPU.
* **Tensor Normalization:** It converts PIL images to tensors and applies standard ImageNet normalization (Mean: `[0.485, 0.456, 0.406]`, Standard Deviation: `[0.229, 0.224, 0.225]`) required by pretrained `torchvision` models.

### 2. Feature Extraction and Optimization
Instead of training a neural network from scratch, this model leverages Transfer Learning by extracting feature maps from a pretrained Convolutional Neural Network:
* **L-BFGS Optimizer:** Unlike standard Deep Learning classification problems that use Adam or SGD, this project implements the `LBFGS` optimizer (`torch.optim.lbfgs`), which is highly effective for style transfer algorithms due to its precision in minimizing complex loss functions.
* **Image Reconstruction:** The optimizer iteratively adjusts the generated image's pixel values, mathematically clamping the tensor data (e.g., `clamp_(-2.1, 2.6)`) to successfully reconstruct and save a clean final image.

## 💻 How to Run Locally

If you wish to explore the code, experiment with the CNN layers, or run the notebook on your own machine:

1. Clone this repository:
   ```bash
   git clone [https://github.com/MGranados64/neural-style-transfer.git](https://github.com/MGranados64/neural-style-transfer.git)
