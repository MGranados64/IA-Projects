# 📝 NLP: Morphosyntactic Labeling (POS Tagging)

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/NLTK-154f5b?style=for-the-badge&logo=python&logoColor=white" alt="NLTK" />
  <img src="https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white" alt="spaCy" />
</p>

## 🎯 Overview

This repository delves into **Natural Language Processing (NLP)**, specifically focusing on **Morphosyntactic Labeling** (Part-of-Speech or POS tagging). The goal is to accurately assign grammatical categories (such as nouns, verbs, adjectives, etc.) to each token within a text corpus, considering its context and definition.

Morphosyntactic labeling is a critical preprocessing step for advanced NLP tasks, including syntactic parsing, sentiment analysis, machine translation, and Agentic AI interactions.

## 🚀 Key Features & Pipeline

### 1. Text Preprocessing
Handling raw text to make it suitable for algorithmic processing:
* **Tokenization:** Splitting text into meaningful units (words, punctuation).
* **Normalization:** Lowercasing, removing special characters, and handling numerical data.
* **Lemmatization:** Reducing words to their base or dictionary form.

### 2. POS Tagging Methodologies
Exploration and implementation of tagging algorithms to resolve linguistic ambiguities:
* **Rule-Based & Dictionary Approaches:** Using predefined lexicons.
* **Statistical/Probabilistic Models:** (e.g., Hidden Markov Models - HMM, Viterbi Algorithm) to calculate the most likely sequence of tags based on transition and emission probabilities.
* **Modern NLP Libraries:** Utilizing state-of-the-art tools like `NLTK` and `spaCy` to compare custom model performance against industry standards.

### 3. Evaluation Metrics
Evaluating the accuracy of the tagging process using an annotated test corpus:
* Measuring overall **Accuracy**.
* Constructing **Confusion Matrices** for specific grammatical categories to identify common misclassifications (e.g., confusing a noun functioning as an adjective).

## 💡 Conclusions

* **Context is Key:** Simple dictionary lookups fail with ambiguous words (e.g., "book" as a noun vs. "book" as a verb). Statistical and context-aware models are mandatory for high accuracy.
* **Efficiency:** Leveraging optimized libraries like `spaCy` significantly reduces computational time while maintaining high precision for morphosyntactic labeling, providing a solid foundation for more complex Generative AI or LLM pipelines.

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/MGranados64/morphosyntactic-labeling.git](https://github.com/MGranados64/morphosyntactic-labeling.git)
