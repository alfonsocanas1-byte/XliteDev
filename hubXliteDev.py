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

# Gestión de Datos con Cache para optimizar la velocidad de respuesta
DB_FILE = "xlite_data.json"

@st.cache_data
def cargar_datos():
    estructura_objetivo = {
        "config": {"version": "2.4", "branch": "Xlite"},
        "modulos": {
            "Registro": ["Registrarme en Xlite ahora"],
            "Ingenieria": [
                "Meteoro ingeniería (y desarrollo de software)", 
                "Meteoro-repuestos", 
                "Meteoro-combustible", 
                "Meteoro-GPS"
            ],
            "Agro_pro": [
                "Restaurante gourmet", 
                "Alimentos y productos naturales", 
                "Confecciones"
            ],
            "ACOarte": ["ACOarte - Joyería y Arte"]
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

# --- FUNCIÓN DE CARGA OPTIMIZADA ---
def cargar_archivo_py(nombre_archivo):
    ruta = os.path.join(os.getcwd(), nombre_archivo)
    nombre_modulo = nombre_archivo.replace(".py", "")
    
    if os.path.exists(ruta):
        # Limpiar rastro previo para evitar que se quede pegado
        if nombre_modulo in sys.modules:
            del sys.modules[nombre_modulo]
            
        spec = importlib.util.spec_from_file_location(nombre_modulo, ruta)
        modulo = importlib.util.module_from_spec(spec)
        sys.modules[nombre_modulo] = modulo
        spec.loader.exec_module(modulo)
        
        if hasattr(modulo, 'main'):
            modulo.main()
    else:
        st.error(f"Archivo no encontrado: {nombre_archivo}")

# 2. Interfaz de Usuario (Lobby)
st.title("🚀 Xlite: Lobby Principal")
st.caption("Use la barra lateral izquierda para navegar.")
st.markdown("---")

# Sidebar
st.sidebar.header("Módulos Xlite")
opciones_menu = [
    "0. Registro Inicial Xlite",
    "1. Ingeniería y Tecnología. **Aprende a desarrollar software**",
    "2. Agro-pro (Restaurante, Alimentos, Confecciones)",
    "3. ACOarte"
]
menu = st.sidebar.radio("Seleccione un área:", opciones_menu)

if 'submodulo_activo' not in st.session_state:
    st.session_state.submodulo_activo = None

# Botón para volver
if st.session_state.submodulo_activo:
    if st.sidebar.button("⬅️ Volver al Menú Principal"):
        st.session_state.submodulo_activo = None
        st.rerun()

# 3. Lógica de Navegación Dinámica (Enrutador)
if st.session_state.submodulo_activo:
    # Aviso de logística
    if st.session_state.submodulo_activo in data["modulos"]["Agro_pro"]:
        st.warning("🚚 **Logística Agro-pro:** Miércoles 2:00 PM desde Montebello hasta Univ. San Buenaventura.")

    # Mapeo de archivos
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
    elif st.session_state.submodulo_activo in ["Meteoro-GPS", "Alimentos y productos naturales", "Confecciones"]:
        st.info(f"El módulo **{st.session_state.submodulo_activo}** está en desarrollo.")
else:
    # --- Lobby Principal ---
    if "0." in menu:
        st.header("📝 Registro en Xlite")
        st.info("💡 **Nota:** Su número quedará vinculado automáticamente.")
        nombre = st.text_input("Nombre y Apellido")
        direccion = st.text_input("Dirección")
        fecha = st.date_input("Fecha de Nacimiento", min_value=pd.to_datetime("1920-01-01"))
        
        if nombre and direccion:
            texto_wa = f"Hola, quiero registrarme en Xlite.\n*Nombre:* {nombre}\n*Dirección:* {direccion}\n*Fecha:* {fecha}"
            url_reg = f"https://wa.me/573228786322?text={urllib.parse.quote(texto_wa)}"
            st.link_button("🚀 Enviar Registro por WhatsApp", url_reg, type="primary", use_container_width=True)

    elif "1." in menu:
        st.header("🛠️ Ingeniería")
        st.info("Prestador: Alfonso Cañas | 3122204688")
        for sub in data["modulos"]["Ingenieria"]:
            if st.button(sub, key=f"ing_{sub}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

    elif "2." in menu:
        st.header("🚜 Agro-pro")
        st.warning("🚚 Entregas: Miércoles 2:00 PM.")
        for sub in data["modulos"]["Agro_pro"]:
            if st.button(sub, key=f"agro_{sub}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

    elif "3." in menu:
        st.header("🎨 ACOarte")
        for sub in data["modulos"]["ACOarte"]:
            if st.button(sub, key=f"aco_{sub}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.caption("Versión: 2.4 | Universo")