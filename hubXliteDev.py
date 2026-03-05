import streamlit as st
import pandas as pd
import json
import os

# Configuración de la página
st.set_page_config(
    page_title="XliteDev - Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. Gestión de Datos (JSON)
DB_FILE = "xlite_data.json"

def cargar_datos():
    if not os.path.exists(DB_FILE):
        # Estructura inicial
        data = {
            "config": {"version": "1.0", "branch": "Xlite"},
            "modulos": {
                "Ingenieria": ["Meteoro-ingeniería", "Meteoro-repuestos", "Meteoro-combustible", "Meteoro-GPS"],
                "Logistica": [],
                "Salud_Emocional": [],
                "Alimentos": [],
                "Arte": [],
                "Promociones": [],
                "Atencion": [],
                "Xpremium": []
            }
        }
        with open(DB_FILE, 'w') as f:
            json.dump(data, f)
    
    with open(DB_FILE, 'r') as f:
        return json.load(f)

data = cargar_datos()

# 2. Interfaz de Usuario (Lobby)
st.title("🚀 Xlite: Lobby Principal")
st.markdown("---")

# Sidebar para navegación
st.sidebar.header("Módulos Xlite")
menu = st.sidebar.radio(
    "Seleccione un área:",
    [
        "1. Ingeniería, Máquinas y Tecnología",
        "2. Logística",
        "3. Médico, Odontológico y Apoyo Emocional",
        "4. Restaurantes y Alimentos",
        "5. Arte",
        "6. Ofertas y Promociones",
        "7. Atención al Usuario",
        "8. Xpremium"
    ]
)

# 3. Lógica de los Módulos
if "1." in menu:
    st.header("🛠️ Ingeniería, Máquinas y Tecnología")
    
    # Usamos Pandas para visualizar las subcategorías de Meteoro
    df_meteoro = pd.DataFrame({
        "Sub-módulos": data["modulos"]["Ingenieria"],
        "Estado": ["Activo", "Desarrollo", "Pendiente", "Activo"]
    })
    
    st.table(df_meteoro)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Acceder a Meteoro-GPS"):
            st.info("Conectando con la señal satelital...")
            
elif "2." in menu:
    st.header("📦 Logística")
    st.write("Gestión de flotas y distribución en progreso.")

elif "3." in menu:
    st.header("❤️ Apoyo Emocional y Salud")
    st.write("Recuerda Alfonso: Mente clara, voluntad indestructible.")
    st.progress(80, text="Progreso del desafío personal")

elif "5." in menu:
    st.header("🎨 Arte")
    st.write("Módulo ACOarte - Joyería e Ilustración.")

else:
    st.info(f"Has seleccionado {menu}. El sistema está listo para recibir la lógica de negocio.")

# Pie de página técnico
st.sidebar.markdown("---")
st.sidebar.caption(f"Carpeta: `XliteDev` | Repo: `GitHub/XliteDev` | Modo: Xlite")