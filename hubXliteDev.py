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
    # Estructura maestra actualizada con las nuevas especialidades médicas
    estructura_objetivo = {
        "config": {"version": "1.2", "branch": "Xlite"},
        "modulos": {
            "Ingenieria": ["Meteoro-ingeniería", "Meteoro-repuestos", "Meteoro-combustible", "Meteoro-GPS"],
            "Logistica": ["Encargo - Domicilio", "Búsqueda de elemento", "Averiguaciones"],
            "Salud_Emocional": [
                "Medicina interna", 
                "Reumatología", 
                "Odontología", 
                "Psicología",
                "Dermatología",
                "Pediatría"
            ],
            "Alimentos": ["Restaurante gourmet", "Comidas rápidas", "Desayunos sorpresa", "Eventos", "Platos típicos colombianos"],
            "Arte": ["Universo", "Universoia", "Joyería"],
            "Agro_pro": ["Producción Orgánica", "Venta de Huevos", "Gestión de Aves"],
            "Promociones": [],
            "Atencion": [],
            "Xpremium": []
        }
    }

    if not os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, 'w') as f:
                json.dump(estructura_objetivo, f)
        except:
            pass
        return estructura_objetivo
    
    try:
        with open(DB_FILE, 'r') as f:
            data = json.load(f)
        
        # Sincronización de seguridad para actualizar submódulos nuevos
        for modulo, lista in estructura_objetivo["modulos"].items():
            if modulo not in data["modulos"] or data["modulos"][modulo] != lista:
                data["modulos"][modulo] = lista
        
        return data
    except:
        return estructura_objetivo

data = cargar_datos()

# 2. Interfaz de Usuario (Lobby)
st.title("🚀 Xlite: Lobby Principal")
st.markdown("---")

# Sidebar
st.sidebar.header("Módulos Xlite")
opciones_menu = [
    "1. Ingeniería, Máquinas y Tecnología",
    "2. Logística",
    "3. Médico, Odontológico y Apoyo Emocional",
    "4. Restaurantes y Alimentos",
    "5. Arte",
    "6. Agro-pro",
    "7. Ofertas y Promociones",
    "8. Atención al Usuario",
    "9. Xpremium"
]
menu = st.sidebar.radio("Seleccione un área:", opciones_menu)

# Función genérica para renderizar botones de forma dinámica
def renderizar_submodulos(nombre_modulo, titulo, icono):
    st.header(f"{icono} {titulo}")
    submodulos = data["modulos"].get(nombre_modulo, [])
    if submodulos:
        # Crea automáticamente las columnas necesarias según la cantidad de submódulos
        cols = st.columns(len(submodulos))
        for i, sub in enumerate(submodulos):
            with cols[i]:
                if st.button(sub, key=f"{nombre_modulo}_{i}", use_container_width=True):
                    st.info(f"Accediendo a: {sub}")
    else:
        st.write("Módulo en fase de diseño.")

# 3. Lógica de los Módulos
if "1." in menu:
    st.header("🛠️ Ingeniería, Máquinas y Tecnología")
    nombre_prestador = "Alfonso Cañas"
    celular = "3122204688"
    mensaje_wa = urllib.parse.quote(f"Hola {nombre_prestador}, necesito soporte en Ingeniería.")
    url_whatsapp = f"https://wa.me/57{celular}?text={mensaje_wa}"
    st.info(f"**Prestador:** {nombre_prestador} | **Celular:** {celular}")
    st.link_button("Contactar por WhatsApp", url_whatsapp, type="primary")
    st.markdown("---")
    renderizar_submodulos("Ingenieria", "Submódulos Meteoro", "")

elif "2." in menu:
    st.header("📦 Logística")
    st.info("**Prestador:** Sebastián Carvajal")
    st.markdown("---")
    renderizar_submodulos("Logistica", "Servicios de Logística", "")

elif "3." in menu:
    renderizar_submodulos("Salud_Emocional", "Médico, Odontológico y Apoyo Emocional", "🩺")

elif "4." in menu:
    renderizar_submodulos("Alimentos", "Restaurantes y Alimentos", "🍴")

elif "5." in menu:
    renderizar_submodulos("Arte", "Arte y Diseño", "🎨")

elif "6." in menu:
    renderizar_submodulos("Agro_pro", "Agro-pro: Campo y Tecnología", "🚜")

else:
    st.info(f"Módulo {menu} seleccionado. Esperando configuración de lógica.")

# Pie de página
st.sidebar.markdown("---")
st.sidebar.caption(f"Versión: {data['config']['version']} | Modo: Xlite")
st.sidebar.caption("Universo")