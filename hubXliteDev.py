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
    # Estructura maestra del proyecto Xlite
    estructura_objetivo = {
        "config": {"version": "1.0", "branch": "Xlite"},
        "modulos": {
            "Ingenieria": ["Meteoro-ingeniería", "Meteoro-repuestos", "Meteoro-combustible", "Meteoro-GPS"],
            "Logistica": ["Encargo - Domicilio", "Búsqueda de elemento", "Averiguaciones"],
            "Salud_Emocional": ["Medicina interna", "Reumatología", "Odontología", "Psicología"],
            "Alimentos": [
                "Restaurante gourmet", 
                "Comidas rápidas", 
                "Desayunos sorpresa", 
                "Eventos", 
                "Platos típicos colombianos"
            ],
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
    
    # Sincronización automática de nuevos módulos o cambios en la estructura
    actualizado = False
    for modulo, lista in estructura_objetivo["modulos"].items():
        if not data["modulos"].get(modulo) or data["modulos"][modulo] != lista:
            data["modulos"][modulo] = lista
            actualizado = True
            
    if actualizado:
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
    
    submodulos = data["modulos"].get("Ingenieria", [])
    cols = st.columns(len(submodulos))
    for i, sub in enumerate(submodulos):
        with cols[i]:
            if st.button(sub, key=f"eng_{i}", use_container_width=True):
                st.info(f"Cargando {sub}...")
            
elif "2." in menu:
    st.header("📦 Logística")
    st.info("**Prestador de servicio de este módulo:** Sebastián Carvajal")
    st.markdown("---")
    st.subheader("Submódulos Logística")
    
    submodulos_log = data["modulos"].get("Logistica", [])
    cols = st.columns(len(submodulos_log))
    for i, sub in enumerate(submodulos_log):
        with cols[i]:
            if st.button(sub, key=f"log_{i}", use_container_width=True):
                st.info(f"Iniciando {sub}...")

elif "3." in menu:
    st.header("🩺 Médico, Odontológico y Apoyo Emocional")
    st.write("Bienvenido Alfonso. Gestión de salud y bienestar.")
    st.markdown("---")
    st.subheader("Especialidades y Apoyo")
    
    submodulos_salud = data["modulos"].get("Salud_Emocional", [])
    cols = st.columns(len(submodulos_salud))
    for i, sub in enumerate(submodulos_salud):
        with cols[i]:
            if st.button(sub, key=f"med_{i}", use_container_width=True):
                st.info(f"Accediendo a {sub}...")

elif "4." in menu:
    st.header("🍴 Restaurantes y Alimentos")
    st.write("Gestión gastronómica y eventos.")
    st.markdown("---")
    st.subheader("Nuestros Servicios")
    
    submodulos_alimentos = data["modulos"].get("Alimentos", [])
    # Usamos 5 columnas para los nuevos botones
    cols = st.columns(len(submodulos_alimentos))
    for i, sub in enumerate(submodulos_alimentos):
        with cols[i]:
            if st.button(sub, key=f"food_{i}", use_container_width=True):
                st.info(f"Abriendo sección: {sub}...")

elif "5." in menu:
    st.header("🎨 Arte")
    st.write("Módulo ACOarte - Joyería e Ilustración.")

else:
    st.info(f"Módulo {menu} seleccionado. Esperando configuración de lógica.")

# Pie de página técnico
st.sidebar.markdown("---")
st.sidebar.caption(f"Carpeta: `XliteDev` | Repo: `GitHub/XliteDev`")
st.sidebar.caption("Modo: Xlite | Universo")