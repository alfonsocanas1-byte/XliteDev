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

# Gestión de Datos con Cache para mayor velocidad
DB_FILE = "xlite_data.json"

@st.cache_data
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
            "Salud_Emocional": ["Medicina interna", "Reumatología", "Odontología", "Psicología", "Dermatología", "Pediatría"],
            "Alimentos": ["Restaurante gourmet", "Comidas rápidas", "Desayunos sorpresa", "Eventos", "Platos típicos colombianos"],
            "Arte": ["Universo", "Universoia", "Joyería"],
            "Agro_pro": ["Producción Orgánica", "Venta de Huevos", "Gestión de Aves"],
            "Promociones": [], "Atencion": [], "Xpremium": []
        }
    }

    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump(estructura_objetivo, f)
        return estructura_objetivo
    
    try:
        with open(DB_FILE, 'r') as f:
            data = json.load(f)
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
        
        # Nota de registro automático
        st.info("💡 **Nota importante:** Al registrarte, tu número quedará vinculado a nuestra base de datos. Solo necesitarás solicitar los servicios directamente dentro de cada módulo.")
        
        st.write("Completa tus datos para el registro:")
        
        # Formulario de Registro
        with st.container():
            nombre = st.text_input("Nombre y Apellido")
            direccion = st.text_input("Dirección (para domicilios)")
            fecha_nacimiento = st.date_input("Fecha de Nacimiento", min_value=pd.to_datetime("1920-01-01"))
            
            if st.button("Enviar Registro por WhatsApp", type="primary"):
                if nombre and direccion:
                    celular_registro = "3228786322"
                    texto_wa = (
                        f"Hola, quiero registrarme en Xlite.\n\n"
                        f"*Nombre:* {nombre}\n"
                        f"*Dirección:* {direccion}\n"
                        f"*Fecha de Nacimiento:* {fecha_nacimiento}"
                    )
                    url_reg = f"https://wa.me/57{celular_registro}?text={urllib.parse.quote(texto_wa)}"
                    st.markdown(f'<meta http-equiv="refresh" content="0;url={url_reg}">', unsafe_allow_html=True)
                    st.success("Redirigiendo a WhatsApp...")
                else:
                    st.warning("Por favor completa todos los campos.")

    elif "1." in menu:
        st.header("🛠️ Ingeniería y Tecnología")
        nombre_prestador = "Alfonso Cañas"
        celular = "3122204688"
        mensaje_wa = urllib.parse.quote(f"Hola {nombre_prestador}, necesito soporte.")
        url_whatsapp = f"https://wa.me/57{celular}?text={mensaje_wa}"
        st.info(f"**Prestador:** {nombre_prestador} | **Celular:** {celular}")
        st.link_button("Contactar por WhatsApp", url_whatsapp, type="primary")
        st.markdown("---")
        
        # Renderizado de submódulos
        submodulos = data["modulos"].get("Ingenieria", [])
        for i, sub in enumerate(submodulos):
            if st.button(sub, key=f"ing_{i}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

    elif "2." in menu:
        st.header("📦 Logística")
        st.info("**Prestador:** Sebastián Carvajal")
        st.markdown("---")
        submodulos = data["modulos"].get("Logistica", [])
        for i, sub in enumerate(submodulos):
            if st.button(sub, key=f"log_{i}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

    elif "3." in menu:
        st.header("🩺 Salud y Bienestar")
        submodulos = data["modulos"].get("Salud_Emocional", [])
        for i, sub in enumerate(submodulos):
            if st.button(sub, key=f"salud_{i}", use_container_width=True):
                st.session_state.submodulo_activo = sub
                st.rerun()

    else:
        st.info(f"Módulo {menu} en desarrollo.")

# Pie de página
st.sidebar.markdown("---")
st.sidebar.caption(f"Versión: {data['config']['version']} | Rama: {data['config']['branch']}")
st.sidebar.caption("Universo")