import streamlit as st
import pandas as pd
import json
import os

# Configuración de la página
st.set_config = st.set_page_config(
    page_title="XliteDev - Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. Gestión de Datos (JSON)
DB_FILE = "xlite_data.json"

def cargar_datos():
    if not os.path.exists(DB_FILE):
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
    st.subheader("Submódulos Meteoro")
    
    # Creamos una cuadrícula de botones para los submódulos
    col1, col2, col3, col4 = st.columns(4)
    
    submodulos = data["modulos"]["Ingenieria"]
    
    with col1:
        if st.button(submodulos[0], use_container_width=True):
            st.info(f"Cargando {submodulos[0]}...")
            # Aquí irá el enlace al .py correspondiente
            
    with col2:
        if st.button(submodulos[1], use_container_width=True):
            st.info(f"Cargando {submodulos[1]}...")
            
    with col3:
        if st.button(submodulos[2], use_container_width=True):
            st.info(f"Cargando {submodulos[2]}...")
            
    with col4:
        if st.button(submodulos[3], use_container_width=True):
            st.info(f"Cargando {submodulos[3]}...")

    st.markdown("---")
    # Tabla informativa de estados
    df_meteoro = pd.DataFrame({
        "Módulo": submodulos,
        "Estado": ["Activo", "Desarrollo", "Pendiente", "Activo"]
    })
    st.write("### Estado del Sistema")
    st.table(df_meteoro)
            
elif "2." in menu:
    st.header("📦 Logística")
    st.write("Módulo en fase de diseño.")

elif "3." in menu:
    st.header("❤️ Apoyo Emocional y Salud")
    st.write("Recuerda Alfonso: Eres vulnerable pero indestructible.")
    st.progress(80, text="Progreso del desafío personal (Sin vicios desde el 27 de febrero).")

elif "5." in menu:
    st.header("🎨 Arte")
    st.write("Módulo ACOarte - Joyería e Ilustración.")

else:
    st.info(f"Módulo {menu} seleccionado. Esperando configuración de lógica.")

# Pie de página técnico
st.sidebar.markdown("---")
st.sidebar.caption(f"Carpeta: `XliteDev` | Repo: `GitHub/XliteDev`")
st.sidebar.caption("Modo: Xlite | Universo")