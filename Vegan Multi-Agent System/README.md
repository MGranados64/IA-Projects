# 🌱 Agentic AI: Vegan Recipe Converter & Nutritional Planner

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/CrewAI-F26522?style=for-the-badge&logo=robot&logoColor=white" alt="CrewAI" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Meta%20Llama%203-0467DF?style=for-the-badge&logo=meta&logoColor=white" alt="Llama 3" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=000" alt="Hugging Face" />
</p>

## 🎯 Resumen del Proyecto

Este repositorio contiene una aplicación basada en **Inteligencia Artificial Agéntica (Multi-Agent System)** desarrollada con la librería `CrewAI` y desplegada con `Streamlit`. El sistema está diseñado para transformar cualquier platillo tradicional con carne en una alternativa vegana deliciosa y nutricionalmente balanceada, calculando además las porciones ideales basadas en la biometría del usuario.

El "cerebro" detrás de estos agentes es el modelo **Llama-3.1-8b-instant**, ejecutado a través de la inferencia ultrarrápida de la API de **Groq**.

🚀 **¡Pruébalo en vivo!** Este sistema de agentes está funcionando 24/7 en un espacio interactivo. Solo ingresa tu platillo favorito, tu altura, peso y nivel de actividad física para obtener un plan personalizado:  
👉 **[Live Demo: CrewAgents Vegans en Hugging Face](https://huggingface.co/spaces/MGC1991MF/CREWAGENTS_VEGANS)**

## 🤖 Arquitectura del Sistema Multi-Agente (CrewAI)

El flujo de trabajo es orquestado por un equipo ("Crew") de cuatro agentes especializados, cada uno con un rol y objetivo definido que colaboran en secuencia:

1. 🩺 **Agente Nutricionista:** Analiza el contenido calórico del platillo original y calcula las necesidades calóricas diarias del usuario (por ejemplo, estimando 2,512.50 cal/día para un perfil sedentario específico).
2. 👨‍🍳 **Agente Chef Vegano:** Reemplaza ingredientes de origen animal. Por ejemplo, en una "Lasagna con carne de res", sustituye la carne por tempeh o tofu, y el queso parmesano por levadura nutricional (nutritional yeast).
3. ⚖️ **Especialista en Porciones:** Dimensiona las cantidades exactas basadas en los cálculos del nutricionista para asegurar un balance energético (ej. 30g de carbohidratos, 25g de proteína y 20g de grasas por porción).
4. 📋 **Coordinador del Plan:** Integra la salida de los tres agentes anteriores para redactar un reporte completo, añadiendo beneficios de la dieta vegana (como la reducción del riesgo de enfermedades crónicas) y sugiriendo acompañamientos.

## ⚙️ Características Técnicas

* **Extracción Inteligente de Datos:** Uso avanzado de Expresiones Regulares (`re`) para analizar (parsear) la salida en texto natural de los LLMs y convertirla en métricas estructuradas y tablas.
* **Exportación de Documentos:** Integración con la librería `FPDF` para compilar los resultados de los agentes y generar un reporte PDF descargable formateado profesionalmente.
* **Cloud & Secrets Management:** Configuración segura de variables de entorno para la integración con la API de Groq en la nube de Hugging Face.

## 💻 Cómo ejecutarlo localmente

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/MGranados64/vegan-agentic-ai.git](https://github.com/MGranados64/vegan-agentic-ai.git)
