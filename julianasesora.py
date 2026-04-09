import streamlit as st
import urllib.parse

# Configuración de página
st.set_page_config(
    page_title="Juliana R - Asesoría Integral",
    page_icon="🛡️",
    layout="centered"
)

# Estilos CSS con forzado de color negro para TODO el texto
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    /* Nombre y subtítulo en NEGRO */
    .main-title {
        color: #000000 !important;
        text-align: center;
        margin-bottom: 0px;
        font-weight: bold;
    }
    .sub-title {
        color: #000000 !important;
        text-align: center;
        margin-bottom: 20px;
        font-weight: 500;
    }
    
    /* Botón de WhatsApp con letras NEGRAS */
    .whatsapp-button {
        display: block;
        width: 100%;
        padding: 15px;
        background-color: #25d366;
        color: #000000 !important;
        text-align: center;
        text-decoration: none !important;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: 0.3s;
        margin-top: 10px;
        border: none;
    }
    .whatsapp-button:visited, .whatsapp-button:active, .whatsapp-button:hover {
        color: #000000 !important;
        text-decoration: none !important;
    }
    .whatsapp-button:hover {
        background-color: #128c7e;
        transform: scale(1.01);
    }

    /* Contenedores de servicio en NEGRO */
    .service-container {
        background: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #000000;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        color: #000000 !important;
    }
    .service-container h3 {
        color: #000000 !important;
        margin-top: 0;
        font-weight: bold;
    }
    
    /* Forzar etiquetas de Streamlit a negro */
    label, .stMarkdown p {
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def link_whatsapp(nombre, servicio):
    phone = "573015492898"
    user_name = nombre if nombre else "un cliente"
    mensaje = f"Hola Juliana, soy {user_name}. Solicito información de: {servicio}"
    encoded_msg = urllib.parse.quote(mensaje)
    return f"https://wa.me/{phone}?text={encoded_msg}"

# --- SECCIÓN SUPERIOR ---
col_img_1, col_img_2, col_img_3 = st.columns([1, 2, 1])
with col_img_2:
    st.image("pelirojita1.jpg.jpeg", use_container_width=True)

st.markdown("<h1 class='main-title'>Juliana R</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='sub-title'>Asesora seguros de vida y medicina prepagada</h4>", unsafe_allow_html=True)
st.divider()

# --- INPUT DE NOMBRE ---
st.markdown("### 👤 Déjanos tu nombre")
nombre_usuario = st.text_input("Escribe tu nombre completo:", placeholder="Ej: Alfonso Pérez")

st.write("") 

# --- BLOQUE DE SERVICIOS ---
services = [
    {"title": "🏥 Medicina Prepagada", "desc": "Afiliación a Colsanitas, Sura y otros.", "svc": "Afiliación a medicina prepagada (Colsanitas, Sura, otros)"},
    {"title": "📋 Seguros y Pensiones", "desc": "Protección integral para tu futuro.", "svc": "Asesoría de seguros y pensiones"},
    {"title": "📑 Certificaciones Z", "desc": "Gestión ágil de certificaciones Z.", "svc": "Certificaciones de la empresa medicina prepagada Z"}
]

for s in services:
    with st.container():
        st.markdown(f"""<div class="service-container">
            <h3>{s['title']}</h3>
            <p>{s['desc']}</p>
        </div>""", unsafe_allow_html=True)
        st.markdown(f'<a href="{link_whatsapp(nombre_usuario, s["svc"])}" target="_blank" class="whatsapp-button">Recibir asesoría</a>', unsafe_allow_html=True)
    st.write("")