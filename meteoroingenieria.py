import streamlit as st
import pandas as pd
import urllib.parse

def enviar_whatsapp(servicio, detalle=""):
    telefono = "573122204688"
    msg = f"Hola Meteoro, me interesa el servicio de: {servicio}. {detalle}"
    url = f"https://wa.me/{telefono}?text={urllib.parse.quote(msg)}"
    return url

def main():
    st.title("🛠️ Meteoro: Ingeniería & Software")
    st.markdown("---")

    # --- SECCIÓN 1: ASESORÍA Y CONSULTORÍA ---
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("1. Asesoría y Consultoría")
            st.write("Optimización de procesos de ingeniería en industrias.")
        with col2:
            st.link_button("Solicitar", enviar_whatsapp("Asesoría Industrial"), use_container_width=True)

    st.markdown("---")

    # --- SECCIÓN 2: DESARROLLO DE SOFTWARE CON IA ---
    st.subheader("2. Desarrollo de Software con IA")
    st.write("Herramientas, integración, comunicación con IA y bases de datos.")
    
    servicios_ia = {
        "Nivel": ["Inicial (Setup)", "Proyecto Completo"],
        "Precio": [150000, 400000]
    }
    df_ia = pd.DataFrame(servicios_ia)
    
    # Mostrar tabla de precios
    st.table(df_ia.style.format({"Precio": "${:,.0f}"}))
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Solicitar Inicial ($150k)", use_container_width=True):
            st.markdown(f'<meta http-equiv="refresh" content="0;url={enviar_whatsapp("Software IA", "Plan Inicial $150.000")}">', unsafe_allow_html=True)
    with c2:
        if st.button("Solicitar Completo ($400k)", use_container_width=True):
            st.markdown(f'<meta http-equiv="refresh" content="0;url={enviar_whatsapp("Software IA", "Plan Completo $400.000")}">', unsafe_allow_html=True)

    st.markdown("---")

    # --- SECCIÓN 3: FLUJOGRAMAS Y ESTADÍSTICA ---
    with st.container():
        col3, col4 = st.columns([3, 1])
        with col3:
            st.subheader("3. Flujogramas y Estadística")
            st.write("Modelado de procesos y análisis de datos avanzado.")
        with col4:
            st.link_button("Solicitar", enviar_whatsapp("Flujogramas/Estadística"), use_container_width=True)

    st.sidebar.info("Módulo Meteoro-Ingeniería")
    st.sidebar.caption("Universo")

if __name__ == "__main__":
    main()