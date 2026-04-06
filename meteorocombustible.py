import streamlit as st
import pandas as pd
import json
import os
import urllib.parse
import importlib.util

# 1. Configuración de la página
st.set_page_config(
    page_title="XliteDev - Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Gestión de Datos con Cache
DB_FILE = "xlite_data.json"

@st.cache_data
def cargar_datos():
    estructura_objetivo = {
        "config": {"version": "2.3", "branch": "Xlite"},
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

if st.session_state.submodulo_activo:
    if st.sidebar.button("⬅️ Volver al Menú Principal"):
        st.session_state.submodulo_activo = None
        st.rerun()

# 3. Lógica de Navegación Dinámica (Enrutador)
if st.session_state.submodulo_activo:
    if st.session_state.submodulo_activo in data["modulos"]["Agro_pro"]:
        st.warning("🚚 **Logística Agro-pro:** Los miércoles a las 2:00 PM inicia recorrido desde Montebello hasta la Univ. San Buenaventura entregando pedidos.")

    if st.session_state.submodulo_activo == "Meteoro ingeniería (y desarrollo de software)":
        cargar_archivo_py("meteoroingenieria.py")
    elif st.session_state.submodulo_activo == "Meteoro-repuestos":
        cargar_archivo_py("meteororepuestos.py")
    elif st.session_state.submodulo_activo == "Meteoro-combustible": # ACTUALIZADO
        cargar_archivo_py("meteorocombustible.py")
    elif st.session_state.submodulo_activo == "Restaurante gourmet":
        cargar_archivo_py("restaurantegourmet.py")
    elif st.session_state.submodulo_activo == "ACOarte - Joyería y Arte":
        cargar_archivo_py("acoarte.py")
    elif st.session_state.submodulo_activo in ["Meteoro-GPS", "Alimentos y productos naturales", "Confecciones"]:
        st.info(f"El módulo **{st.session_state.submodulo_activo}** está actualmente en desarrollo.")

else:
    if "0." in menu:
        st.header("📝 Registro en Xlite")
        st.info("💡 **Nota importante:** Al registrarte, tu número quedará vinculado. Solo solicita los servicios dentro de cada módulo.")
        with st.container():
            nombre = st.text_input("Nombre y Apellido")
            direccion = st.text_input("Dirección (para domicilios)")
            fecha_nacimiento = st.date_input("Fecha de Nacimiento", min_value=pd.to_datetime("1920-01-01"))
            if nombre and direccion:
                celular_registro = "3228786322"
                texto_wa = f"Hola, quiero registrarme en Xlite.\n\n*Nombre:* {nombre}\n*Dirección:* {direccion}\n*Fecha:* {fecha_nacimiento}"
                url_reg = f"https://wa.me/57{celular_registro}?text={urllib.parse.quote(texto_wa)}"
                st.link_button("🚀 Enviar Registro por WhatsApp", url_reg, type="primary", use_container_width=True)
            else:
                st.warning("Complete Nombre y Dirección para habilitar el registro.")

    elif "1." in menu:
        st.header("🛠️ Ingeniería y Tecnología")
        st.info("**Prestador:** Alfonso Cañas | **Celular:** 3122204688")
        st.markdown("---")
        submodulos = data["modulos"].get("Ingenieria", [])
        for i, sub in enumerate(submodulos):
            if st.button(sub, key=f"ing_{i}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

    elif "2." in menu:
        st.header("🚜 Agro-pro")
        st.warning("🚚 **Recorrido de entregas:** Los miércoles a las 2:00 PM desde Montebello hasta la Univ. San Buenaventura.")
        st.write("Servicios de alimentación, productos naturales y confecciones.")
        st.markdown("---")
        submodulos = data["modulos"].get("Agro_pro", [])
        for i, sub in enumerate(submodulos):
            if st.button(sub, key=f"agro_{i}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

    elif "3." in menu:
        st.header("🎨 ACOarte")
        st.write("Expresión artística y joyería exclusiva.")
        st.markdown("---")
        submodulos = data["modulos"].get("ACOarte", [])
        for i, sub in enumerate(submodulos):
            if st.button(sub, key=f"aco_{i}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

# Pie de página
st.sidebar.markdown("---")
st.sidebar.caption(f"Versión: {data['config']['version']} | Rama: {data['config']['branch']}")
st.sidebar.caption("Universo")