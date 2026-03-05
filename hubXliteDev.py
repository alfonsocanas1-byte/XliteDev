import streamlit as st
import pandas as pd
import json
import os
import urllib.parse

# Configuración de la página
st.set_page_config(
    page_title="XliteDev - Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. Gestión de Datos (JSON)
DB_FILE = "xlite_data.json"

def cargar_datos():
    # Definimos la estructura completa que DEBE tener el archivo
    estructura_objetivo = {
        "config": {"version": "1.0", "branch": "Xlite"},
        "modulos": {
            "Ingenieria": ["Meteoro-ingeniería", "Meteoro-repuestos", "Meteoro-combustible", "Meteoro-GPS"],
            "Logistica": ["Encargo - Domicilio", "Búsqueda de elemento", "Averiguaciones"],
            "Salud_Emocional": [],
            "Alimentos": [],
            "Arte": [],
            "Promociones": [],
            "Atencion": [],
            "Xpremium": []
        }
    }

    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump(estructura_objetivo, f)
        return estructura_objetivo
    
    with open(DB_FILE, 'r') as f:
        data = json.load(f)
    
    # VALIDACIÓN: Si faltan los datos de Logística en el archivo viejo, los inyectamos
    if not data["modulos"].get("Logistica"):
        data["modulos"]["Logistica"] = estructura_objetivo["modulos"]["Logistica"]
        with open(DB_FILE, 'w') as f:
            json.dump(data, f)
            
    return data

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
    nombre_prestador = "Alfonso Cañas"
    celular = "3122204688"
    mensaje_wa = urllib.parse.quote(f"Hola {nombre_prestador}, necesito soporte en el módulo de Ingeniería.")
    url_whatsapp = f"https://wa.me/57{celular}?text={mensaje_wa}"
    
    st.info(f"**Prestador de servicio de este módulo:** {nombre_prestador} | **Celular:** {celular}")
    st.link_button("Contactar por WhatsApp", url_whatsapp, type="primary")
    
    st.markdown("---")
    st.subheader("Submódulos Meteoro")
    
    col1, col2, col3, col4 = st.columns(4)
    submodulos = data["modulos"].get("Ingenieria", [])
    
    # Validación simple para evitar errores de índice
    if len(submodulos) >= 4:
        with col1:
            if st.button(submodulos[0], key="eng1", use_container_width=True):
                st.info(f"Cargando {submodulos[0]}...")
        with col2:
            if st.button(submodulos[1], key="eng2", use_container_width=True):
                st.info(f"Cargando {submodulos[1]}...")
        with col3:
            if st.button(submodulos[2], key="eng3", use_container_width=True):
                st.info(f"Cargando {submodulos[2]}...")
        with col4:
            if st.button(submodulos[3], key="eng4", use_container_width=True):
                st.info(f"Cargando {submodulos[3]}...")
            
elif "2." in menu:
    st.header("📦 Logística")
    st.info("**Prestador de servicio de este módulo:** Sebastián Carvajal")
    st.markdown("---")
    st.subheader("Submódulos Logística")
    
    submodulos_log = data["modulos"].get("Logistica", [])
    
    if len(submodulos_log) >= 3:
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(submodulos_log[0], key="log1", use_container_width=True):
                st.info(f"Iniciando {submodulos_log[0]}...")
        with col2:
            if st.button(submodulos_log[1], key="log2", use_container_width=True):
                st.info(f"Iniciando {submodulos_log[1]}...")
        with col3:
            if st.button(submodulos_log[2], key="log3", use_container_width=True):
                st.info(f"Iniciando {submodulos_log[2]}...")
    else:
        st.error("Error: Datos de logística no encontrados en el archivo JSON.")

elif "3." in menu:
    st.header("❤️ Apoyo Emocional y Salud")
    st.write("Recuerda Alfonso: Eres vulnerable pero indestructible.")
    st.progress(80, text="Progreso del desafío personal (Sin vicios).")

elif "5." in menu:
    st.header("🎨 Arte")
    st.write("Módulo ACOarte - Joyería e Ilustración.")

else:
    st.info(f"Módulo {menu} seleccionado. Esperando configuración de lógica.")

# Pie de página técnico
st.sidebar.markdown("---")
st.sidebar.caption(f"Carpeta: `XliteDev` | Repo: `GitHub/XliteDev`")
st.sidebar.caption("Modo: Xlite | Universo")