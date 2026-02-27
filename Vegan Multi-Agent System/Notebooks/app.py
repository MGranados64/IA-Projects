# 1. Librerias
import os
import streamlit as st
import re
from crewai import Agent, Task, Crew
from fpdf import FPDF 

# 2. Configuración del LLM en la Nube (Vía st.secrets GROQ) 
os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama-3.1-8b-instant" 
os.environ["OPENAI_API_KEY"] = os.environ.get("API_KEY")

# 3. Definición de Agentes
agente_nutricionista = Agent(
    role='Nutricionista Especializado',
    goal='Analizar el contenido nutricional de platillos y calcular requerimientos calóricos basados en altura y peso.',
    backstory='Eres un nutricionista certificado con expertise en análisis de composición de alimentos y cálculo de necesidades nutricionales personalizadas.',
    verbose=True,
    allow_delegation=False
)

agente_chef = Agent(
    role='Chef Especializado en Cocina Vegana',
    goal='Convertir platillos que contienen carne en alternativas veganas deliciosas y nutricionalmente balanceadas.',
    backstory='Eres un chef reconocido a nivel mundial en gastronomía vegana, experto en sustituir ingredientes de origen animal por alternativas vegetales sin comprometer el sabor.',
    verbose=True,
    allow_delegation=False
)

agente_porciones = Agent(
    role='Especialista en Control de Porciones',
    goal='Calcular tamaños de porción apropiados basados en las necesidades calóricas y características físicas del usuario.',
    backstory='Eres un especialista en nutrición deportiva que calcula porciones ideales para mantener un balance energético óptimo.',
    verbose=True,
    allow_delegation=False
)

agente_coordinador = Agent(
    role='Coordinador de Plan Alimenticio',
    goal='Integrar toda la información y proveer una recomendación completa y personalizada.',
    backstory='Eres un health coach que combina conocimientos de nutrición, gastronomía y planificación de dietas para crear recomendaciones integrales.',
    verbose=True,
    allow_delegation=False
)

# 4. Funciones para Parsear la Salida y Crear PDF
def parse_calorias(text):
    data = {
        "Calorías": "N/A",
        "Proteína": "N/A", 
        "Carbohidratos": "N/A",
        "Grasas": "N/A"
    }
    
    calorias_match = re.search(r"(?:Calorías|Calories):\s*([\d\.,]+)\s*(?:kcal|cal)", text, re.IGNORECASE)
    proteina_match = re.search(r"(?:Proteína|Protein):\s*([\d\.,]+)\s*g", text, re.IGNORECASE)
    carbos_match = re.search(r"(?:Carbohidratos|Carbs):\s*([\d\.,]+)\s*g", text, re.IGNORECASE)
    grasas_match = re.search(r"(?:Grasas|Fat):\s*([\d\.,]+)\s*g", text, re.IGNORECASE)

    if calorias_match: data["Calorías"] = calorias_match.group(1)
    if proteina_match: data["Proteína"] = proteina_match.group(1)
    if carbos_match: data["Carbohidratos"] = carbos_match.group(1)
    if grasas_match: data["Grasas"] = grasas_match.group(1)
        
    return data

def parse_porciones(text):
    porciones_data = []
    lines = text.split('\n')
    
    for line in lines:
        if '|' in line:
            parts = line.split('|')
            if len(parts) >= 3:
                ingrediente = parts[0].strip()
                cantidad = parts[1].strip()
                notas = parts[2].strip()
                if ingrediente and "Ingrediente" not in ingrediente:
                    porciones_data.append({
                        "Ingrediente": ingrediente,
                        "Cantidad": cantidad,
                        "Notas": notas
                    })
    return porciones_data

def parse_sustitutos(text):
    sustitutos_data = []
    lines = text.split('\n')
    
    current_item = ""
    for line in lines:
        if re.match(r'^[•\-]\s*(.+)', line):
            if current_item:
                sustitutos_data.append(current_item.strip())
            current_item = re.match(r'^[•\-]\s*(.+)', line).group(1)
        elif line.strip() and current_item:
            current_item += " " + line.strip()
    
    if current_item:
        sustitutos_data.append(current_item.strip())
        
    return sustitutos_data

# 4.1 FUNCIÓN PARA EXPORTAR EL PDF
def generar_pdf(platillo_nombre, texto_completo):
    pdf = FPDF()
    pdf.add_page()
    
    # 4.1.1 Título Principal
    pdf.set_font("Arial", 'B', 16)
    titulo = f"Reporte Nutricional: {platillo_nombre}".encode('latin-1', 'ignore').decode('latin-1')
    pdf.cell(0, 10, txt=titulo, ln=True, align='C')
    pdf.ln(5)
    
    # 4.1.2 Contenido (limpiamos emojis y caracteres que rompen FPDF)
    pdf.set_font("Arial", size=11)
    texto_limpio = str(texto_completo).encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 8, txt=texto_limpio)
    
    # 4.1.3 Firma al pie
    pdf.ln(10)
    pdf.set_font("Arial", 'I', 9)
    pdf.cell(0, 10, txt="Generado por IA | Ing. Miguel Granados", ln=True, align='R')
    
    return bytes(pdf.output())

# 5. Interfaz de Streamlit
st.set_page_config(page_title="Conversor de Platillos a Vegano", layout="wide")
st.title("🌱 Conversor de Platillos con Carne a Opción Vegana")

# 6. Barra Lateral con Información
with st.sidebar:
    st.header("💡 Información Adicional")
    st.info("""
    Este sistema utiliza IA para:
    - Calcular necesidades calóricas personalizadas
    - Convertir platillos con carne a versiones veganas
    - Proporcionar porciones adecuadas a tu físico
    - Mantener el balance nutricional
    """)
    
    st.header("🔧 Requisitos")
    st.success("""
    Versión para la Nube:
    - Conectado a Llama 3.1 vía API externa
    - Funcionando 24/7 en Hugging Face
    """)
    
    # 6.1 Anuncio LINKEDIN
    st.markdown("---")
    st.markdown(
        """
        <div style='
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin: 10px 0;
        '>
            <h3 style='color: white; margin-bottom: 10px;'>🖤🦇 Hecho por Ing.Miguel Granados Carcaño🦇🖤</h3>
            <p style='margin-bottom: 15px;'>Desarrollador de IA y Machine Learning</p>
            <a href='https://www.linkedin.com/in/miguel-granados-2a77ba199' 
               target='_blank' 
               style='
                   display: inline-block;
                   background-color: #0077b5;
                   color: white;
                   padding: 10px 20px;
                   border-radius: 25px;
                   text-decoration: none;
                   font-weight: bold;
                   transition: all 0.3s ease;
               '
               onmouseover="this.style.backgroundColor='#005582'"
               onmouseout="this.style.backgroundColor='#0077b5'">
               🔗 Conéctame en LinkedIn
            </a>
        </div>
        """, 
        unsafe_allow_html=True
    )

# 7. Contenido Principal
st.header("Información del Usuario")

col1, col2 = st.columns(2)

with col1:
    platillo = st.text_input("🍽️ Platillo con carne que deseas convertir", "Ej: Tacos al pastor")
    altura = st.number_input("📏 Altura (cm)", min_value=100, max_value=220, value=170)

with col2:
    peso = st.number_input("⚖️ Peso (kg)", min_value=30, max_value=200, value=70)
    nivel_actividad = st.selectbox(
        "🏃 Nivel de Actividad",
        ["Sedentario", "Ligero", "Moderado", "Activo", "Muy Activo"]
    )

if st.button("🌱 Convertir a Opción Vegana 🌱"):
    if not platillo or platillo == "Ej: Tacos al pastor":
        st.error("Por favor, ingresa un platillo válido.")
    else:
        with st.spinner(f"Convirtiendo {platillo} a versión vegana... Los agentes están trabajando. Esto puede tomar unos minutos..."):
            try:
                task_nutricion = Task(
                    description=f"Calcula necesidades calóricas diarias para una persona con: Altura: {altura} cm, Peso: {peso} kg, Nivel de actividad: {nivel_actividad}. Analiza el contenido nutricional aproximado del platillo: {platillo}. Calcula el IMC.",
                    agent=agente_nutricionista,
                    expected_output="Informe nutricional detallando: Calorías diarias necesarias, Calorías del platillo original, Proteína (g), Carbohidratos (g), Grasas (g) e IMC calculado."
                )

                task_conversion = Task(
                    description=f"Convierte el platillo '{platillo}' en una versión vegana deliciosa y nutritiva. Proporciona al menos 3-5 sustitutos específicos para los ingredientes de origen animal.",
                    agent=agente_chef,
                    expected_output="Lista de sustitutos en formato: • [Original] → [Sustituto] - [Beneficios/Notas]"
                )

                task_porciones = Task(
                    description=f"Basado en las necesidades calóricas calculadas para {peso}kg, {altura}cm con actividad {nivel_actividad}, determina porciones apropiadas para la versión vegana.",
                    agent=agente_porciones,
                    context=[task_nutricion],
                    expected_output="Tabla de porciones en formato exacto con columnas separadas por '|': Ingrediente | Cantidad | Notas"
                )

                task_final = Task(
                    description=f"Integra toda la información en una recomendación final sobre el platillo {platillo} y su versión vegana, incluyendo acompañamientos sugeridos.",
                    agent=agente_coordinador,
                    context=[task_nutricion, task_conversion, task_porciones],
                    expected_output="Resumen final estructurado con Resumen Nutricional, Versión Vegana, Porciones Recomendadas, Beneficios y Acompañamientos."
                )

                crew = Crew(
                    agents=[agente_nutricionista, agente_chef, agente_porciones, agente_coordinador],
                    tasks=[task_nutricion, task_conversion, task_porciones, task_final],
                    verbose=True
                )
                
                result_final_text = str(crew.kickoff())
                
                nutricion_output = str(task_nutricion.output)
                conversion_output = str(task_conversion.output)
                porciones_output = str(task_porciones.output)

                datos_nutricionales = parse_calorias(nutricion_output)
                sustitutos_veganos = parse_sustitutos(conversion_output)
                tabla_porciones = parse_porciones(porciones_output)

                st.success("✅ Conversión completada exitosamente!")
                
                st.subheader("📊 Información Nutricional")
                if datos_nutricionales["Calorías"] != "N/A":
                    c1, c2, c3, c4 = st.columns(4)
                    c1.metric("Calorías", datos_nutricionales["Calorías"])
                    c2.metric("Proteína", datos_nutricionales["Proteína"])
                    c3.metric("Carbohidratos", datos_nutricionales["Carbohidratos"])
                    c4.metric("Grasas", datos_nutricionales["Grasas"])
                else:
                    st.write(nutricion_output)

                st.subheader("🔄 Sustitutos Veganos")
                if sustitutos_veganos:
                    for sust in sustitutos_veganos:
                        st.write(f"• {sust}")
                else:
                    st.write(conversion_output)

                st.subheader("🍽️ Porciones Recomendadas")
                if tabla_porciones:
                    st.table(tabla_porciones)
                else:
                    st.write(porciones_output)

                st.subheader("📋 Recomendación Completa")
                st.info(result_final_text)

                # 8. NUEVO BOTÓN DE DESCARGA PDF 
                st.divider()
                st.subheader("📥 Exportar Plan")
                
                pdf_bytes = generar_pdf(platillo, result_final_text)
                
                st.download_button(
                    label="📄 Descargar Recomendación en PDF",
                    data=pdf_bytes,
                    file_name=f"Plan_Vegano_{platillo.replace(' ', '_')}.pdf",
                    mime="application/pdf"
                )

            except Exception as e:
                st.error(f"❌ Error durante la conversión: {e}")
                st.info("Revisa la configuración de tus Secrets en Hugging Face y tu API Key.")