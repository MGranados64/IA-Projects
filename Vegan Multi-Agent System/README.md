# 🌱 Agentic AI: Vegan Recipe Converter & Nutritional Planner

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/CrewAI-F26522?style=for-the-badge&logo=robot&logoColor=white" alt="CrewAI" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Meta%20Llama%203-0467DF?style=for-the-badge&logo=meta&logoColor=white" alt="Llama 3" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=000" alt="Hugging Face" />
</p>

## 🎯 Project Overview

This repository contains an **Agentic Artificial Intelligence (Multi-Agent System)** application developed with `CrewAI` and deployed using `Streamlit`. The system is designed to transform any traditional meat-based dish into a delicious, nutritionally balanced vegan alternative, while also calculating the ideal portion sizes based on the user's specific biometrics.

The "brain" powering these agents is the **Llama-3.1-8b-instant** model, executed via the ultra-fast inference of the **Groq API**.

🚀 **Try it live!** This agentic system is running 24/7 in an interactive workspace. Simply input your favorite dish, height, weight, and physical activity level to get a personalized plan:  
👉 **[Live Demo: CrewAgents Vegans on Hugging Face](https://huggingface.co/spaces/MGC1991MF/CREWAGENTS_VEGANS)**

## 🤖 Multi-Agent Architecture (CrewAI)

The workflow is orchestrated by a "Crew" of four specialized agents, each with a specific role and goal, collaborating in sequence:

1. 🩺 **Nutritionist Agent:** Analyzes the caloric content of the original dish and calculates the user's daily caloric needs (e.g., estimating 2,512.50 cal/day for a specific sedentary profile).
2. 👨‍🍳 **Vegan Chef Agent:** Replaces animal-based ingredients with plant-based alternatives. For example, in a "Beef Lasagna", it substitutes the beef with tempeh or tofu, and the parmesan cheese with nutritional yeast.
3. ⚖️ **Portion Specialist:** Determines the exact ingredient quantities based on the nutritionist's calculations to ensure an optimal energy balance (e.g., structuring portions to hit 30g of carbohydrates, 25g of protein, and 20g of fats).
4. 📋 **Plan Coordinator:** Integrates the output from the previous three agents to draft a comprehensive final report, adding the benefits of the vegan diet (such as reducing the risk of chronic diseases) and suggesting appropriate side dishes.

## ⚙️ Technical Features

* **Intelligent Data Extraction:** Advanced use of Regular Expressions (`re`) to parse natural language outputs from the LLMs and convert them into structured metrics and tables.
* **Document Export:** Integration with the `FPDF` library to compile the agents' results and generate a professionally formatted, downloadable PDF report.
* **Cloud & Secrets Management:** Secure configuration of environment variables for seamless integration with the Groq API on the Hugging Face cloud.

## 💻 How to Run Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/MGranados64/vegan-agentic-ai.git](https://github.com/MGranados64/vegan-agentic-ai.git)
