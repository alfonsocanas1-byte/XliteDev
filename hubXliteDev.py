import streamlit as st
import pandas as pd
import json
import os
import urllib.parse
import importlib.util
import sys

# 1. Configuración de la página
st.set_page_config(
    page_title="XliteDev - Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CONFIGURACIÓN DE RUTAS ---
USUARIO_GH = "alfonsocanas1-byte"
REPO_GH = "XliteDev"
RAMA_GH = "desarrollo"
BASE_URL_GH = f"https://raw.githubusercontent.com/{USUARIO_GH}/{REPO_GH}/{RAMA_GH}/"

# Gestión de Datos
DB_FILE = "xlite_data.json"

@st.cache_data
def cargar_datos():
    estructura_objetivo = {
        "config": {"version": "2.8", "branch": "Xlite"},
        "modulos": {
            "Registro": ["Registrarme en Xlite ahora"],
            "Ingenieria": ["Meteoro ingeniería (y desarrollo de software)", "Meteoro-repuestos", "Meteoro-combustible", "Meteoro-GPS"],
            "Agro_pro": ["Restaurante gourmet", "Alimentos y productos naturales", "Confecciones"],
            "ACOarte": ["ACOarte - Joyería y Arte"],
            "Salud": ["Asesoría Medicina EPS, Prepagada, Seguros y Pensión"]
        }
    }
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump(estructura_objetivo, f)
        return estructura_objetivo
    try:
        with open(DB_FILE, 'r') as f:
            data = json.load(f)
        data["modulos"] = estructura_objetivo["modulos"]
        return data
    except:
        return estructura_objetivo

data = cargar_datos()

# --- CARGA DINÁMICA ---
def cargar_archivo_py(nombre_archivo):
    ruta = os.path.join(os.getcwd(), nombre_archivo)
    nombre_modulo = nombre_archivo.replace(".py", "")
    if os.path.exists(ruta):
        try:
            if nombre_modulo in sys.modules:
                del sys.modules[nombre_modulo]
            spec = importlib.util.spec_from_file_location(nombre_modulo, ruta)
            modulo = importlib.util.module_from_spec(spec)
            sys.modules[nombre_modulo] = modulo
            spec.loader.exec_module(modulo)
            if hasattr(modulo, 'main'):
                modulo.main()
        except Exception as e:
            st.error(f"Error al ejecutar {nombre_archivo}: {e}")
    else:
        st.error(f"Archivo no encontrado: {nombre_archivo}")

# 2. Interfaz de Usuario
st.title("🚀 Xlite: Lobby Principal")
st.caption("Use la barra lateral izquierda para navegar.")
st.markdown("---")

# Sidebar
opciones_menu = [
    "0. Registro Inicial Xlite", 
    "1. Ingeniería y Tecnología.", 
    "2. Agro-pro", 
    "3. ACOarte",
    "4. Medicina, Salud y Bienestar"
]
menu = st.sidebar.radio("Seleccione un área:", opciones_menu)

if 'submodulo_activo' not in st.session_state:
    st.session_state.submodulo_activo = None

if st.session_state.submodulo_activo:
    if st.sidebar.button("⬅️ Volver al Menú Principal"):
        st.session_state.submodulo_activo = None
        st.rerun()

# 3. Lógica de Navegación
if st.session_state.submodulo_activo:
    mapeo = {
        "Meteoro ingeniería (y desarrollo de software)": "meteoroingenieria.py",
        "Meteoro-repuestos": "meteororepuestos.py",
        "Meteoro-combustible": "meteorocombustible.py",
        "Restaurante gourmet": "restaurantegourmet.py",
        "ACOarte - Joyería y Arte": "acoarte.py"
    }
    archivo = mapeo.get(st.session_state.submodulo_activo)
    if archivo:
        cargar_archivo_py(archivo)
    else:
        st.info("Módulo en desarrollo.")
else:
    # --- Lobby por Categoría ---
    if "0." in menu:
        st.header("📝 Registro en Xlite")
        nombre = st.text_input("Nombre y Apellido")
        if nombre:
            url_reg = f"https://wa.me/573228786322?text=Registro_{nombre}"
            st.link_button("🚀 Enviar por WhatsApp", url_reg, type="primary")

    elif "1." in menu:
        st.header("🛠️ Ingeniería y Tecnología")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(f"{BASE_URL_GH}alfonsocanas1.jpg", width=200)
        with col2:
            st.info("🛠️ **Alfonso Cañas** | 3122204688")
        st.markdown("---")
        for sub in data["modulos"]["Ingenieria"]:
            if st.button(sub, key=f"ing_{sub}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

    elif "2." in menu:
        st.header("🚜 Agro-pro")
        st.image(f"{BASE_URL_GH}alfonsocanas1.jpg", width=150)
        st.warning("🚚 Recorrido: Miércoles 2:00 PM desde Montebello.")
        for sub in data["modulos"]["Agro_pro"]:
            if st.button(sub, key=f"agro_{sub}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

    elif "3." in menu:
        st.header("🎨 ACOarte")
        st.image(f"{BASE_URL_GH}alfonsocanas1.jpg", width=150)
        for sub in data["modulos"]["ACOarte"]:
            if st.button(sub, key=f"aco_{sub}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

    elif "4." in menu:
        st.header("🩺 Medicina, Salud y Bienestar")
        st.write("Seleccione un servicio para ser redirigido:")
        # BOTÓN DIRECTO A LA URL EXTERNA
        st.link_button(
            "🏥 Asesoría Medicina EPS, Prepagada, Seguros y Pensión", 
            "https://julianaasesorasegurosypensiones.streamlit.app/",
            type="primary",
            use_container_width=True
        )

st.sidebar.markdown("---")
st.sidebar.caption(f"Versión: 2.8 | Universo")