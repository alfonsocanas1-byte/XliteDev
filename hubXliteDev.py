import streamlit as st
import pandas as pd
import json
import os
import urllib.parse
import importlib.util

# Configuración de la página
st.set_config_config(
    page_title="XliteDev - Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. Gestión de Datos (JSON)
DB_FILE = "xlite_data.json"

def cargar_datos():
    estructura_objetivo = {
        "config": {"version": "1.2", "branch": "Xlite"},
        "modulos": {
            "Registro": ["Registrarme en Xlite ahora"],
            "Ingenieria": [
                "Meteoro ingeniería (y desarrollo de software)", 
                "Meteoro-repuestos", 
                "Meteoro-combustible", 
                "Meteoro-GPS"
            ],
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
        for modulo, lista in estructura_objetivo["modulos"].items():
            if modulo not in data["modulos"] or data["modulos"][modulo] != lista:
                data["modulos"][modulo] = lista
        return data
    except:
        return estructura_objetivo

data = cargar_datos()

# --- FUNCIÓN PARA CARGAR MÓDULOS EXTERNOS ---
def cargar_archivo_py(nombre_archivo):
    ruta = os.path.join(os.getcwd(), nombre_archivo)
    if os.path.exists(ruta):
        spec = importlib.util.spec_from_file_location("modulo_dinamico", ruta)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        if hasattr(modulo, 'main'):
            modulo.main()
    else:
        st.error(f"No se encontró el archivo: {nombre_archivo}")

# 2. Interfaz de Usuario (Lobby)
st.title("🚀 Xlite: Lobby Principal")
# Aviso más sutil y pequeño
st.caption("Use la barra lateral izquierda para navegar.")
st.markdown("---")

# Sidebar
st.sidebar.header("Módulos Xlite")
opciones_menu = [
    "0. Registro Inicial Xlite",
    "1. Ingeniería, Máquinas y Tecnología. **Aprende a desarrollar software aquí**",
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

def renderizar_submodulos(nombre_modulo, titulo, icono):
    st.header(f"{icono} {titulo}")
    submodulos = data["modulos"].get(nombre_modulo, [])
    if submodulos:
        for i, sub in enumerate(submodulos):
            if st.button(sub, key=f"{nombre_modulo}_{i}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()
    else:
        st.write("Módulo en fase de diseño.")

if 'submodulo_activo' not in st.session_state:
    st.session_state.submodulo_activo = None

if st.session_state.submodulo_activo:
    if st.sidebar.button("⬅️ Volver al Menú Principal"):
        st.session_state.submodulo_activo = None
        st.rerun()

# 3. Lógica de Navegación Dinámica
if st.session_state.submodulo_activo == "Restaurante gourmet":
    cargar_archivo_py("restaurantegourmet.py")
elif st.session_state.submodulo_activo == "Meteoro ingeniería (y desarrollo de software)":
    cargar_archivo_py("meteoroingenieria.py")
elif st.session_state.submodulo_activo == "Meteoro-repuestos":
    cargar_archivo_py("meteororepuestos.py")
elif st.session_state.submodulo_activo in ["Meteoro-combustible", "Meteoro-GPS"]:
    st.info(f"El módulo **{st.session_state.submodulo_activo}** está actualmente en desarrollo.")

else:
    # --- Vista del Lobby por Categoría ---
    if "0." in menu:
        st.header("📝 Registro en Xlite")
        st.write("Regístrate para acceder a todos los beneficios.")
        celular_registro = "3228786322"
        mensaje_reg = urllib.parse.quote("Hola, quiero registrarme en Xlite.")
        url_reg = f"https://wa.me/57{celular_registro}?text={mensaje_reg}"
        st.link_button("Registrarme en Xlite ahora", url_reg, type="primary", use_container_width=True)

    elif "1." in menu:
        st.header("🛠️ Ingeniería y Tecnología")
        nombre_prestador = "Alfonso Cañas"
        celular = "3122204688"
        mensaje_wa = urllib.parse.quote(f"Hola {nombre_prestador}, necesito soporte.")
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
        renderizar_submodulos("Salud_Emocional", "Salud y Bienestar", "🩺")

    elif "4." in menu:
        renderizar_submodulos("Alimentos", "Restaurantes y Alimentos", "🍴")

    elif "5." in menu:
        renderizar_submodulos("Arte", "Arte y Diseño", "🎨")

    elif "6." in menu:
        renderizar_submodulos("Agro_pro", "Agro-pro", "🚜")

    else:
        st.info(f"Módulo {menu} en desarrollo.")

# Pie de página
st.sidebar.markdown("---")
st.sidebar.caption(f"Versión: {data['config']['version']} | Rama: {data['config']['branch']}")
st.sidebar.caption("Universo")