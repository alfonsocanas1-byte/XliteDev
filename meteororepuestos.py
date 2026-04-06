import streamlit as st
import pandas as pd
import urllib.parse

def main():
    st.title("⚙️ Meteoro-Repuestos: Marketplace")
    st.info("💡 Use la barra de la izquierda para navegar entre los diferentes módulos.")
    st.markdown("---")

    # Configuración de URLs de GitHub para imágenes
    # Reemplaza 'TU_USUARIO' y 'TU_REPO' con tus datos de GitHub
    github_base_url = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/"
    
    # 1. Base de Datos de Productos
    productos = [
        {
            "id": 1,
            "nombre": "Aceite 20w50 litro",
            "precio": 40000,
            "imagen": f"{github_base_url}meteororespuestos1.jpg"
        },
        {
            "id": 2,
            "nombre": "Llanta 220",
            "precio": 200000,
            "imagen": f"{github_base_url}meteororespuestos2.jpg"
        }
    ]

    # Inicializar carrito
    if 'carrito_repuestos' not in st.session_state:
        st.session_state.carrito_repuestos = []

    # 2. Visualización de Productos
    st.subheader("Catálogo de Repuestos")
    
    cols = st.columns(2)
    
    for i, prod in enumerate(productos):
        with cols[i]:
            st.image(prod["imagen"], caption=prod["nombre"], use_container_width=True)
            st.write(f"**Precio:** ${prod['precio']:,}")
            if st.button(f"Añadir {prod['nombre']}", key=f"btn_{prod['id']}"):
                st.session_state.carrito_repuestos.append(prod)
                st.toast(f"Añadido: {prod['nombre']}")

    # 3. Resumen y Pedido
    st.markdown("---")
    st.subheader("🛒 Resumen de Compra")

    if st.session_state.carrito_repuestos:
        df_carro = pd.DataFrame(st.session_state.carrito_repuestos)
        st.table(df_carro[["nombre", "precio"]])
        
        total = df_carro["precio"].sum()
        st.write(f"### Total a Pagar: ${total:,}")

        if st.button("Vaciar Carrito"):
            st.session_state.carrito_repuestos = []
            st.rerun()

        # Botón de WhatsApp
        celular_ventas = "3122204688" # Basado en tu contacto de ingeniería
        mensaje_base = "Hola Meteoro-Repuestos, quiero comprar:\n"
        detalles = ""
        for item in st.session_state.carrito_repuestos:
            detalles += f"- {item['nombre']} (${item['precio']:,})\n"
        
        mensaje_final = f"{mensaje_base}{detalles}\n*Total: ${total:,}*"
        url_wa = f"https://wa.me/57{celular_ventas}?text={urllib.parse.quote(mensaje_final)}"
        
        st.link_button("🚀 Finalizar Pedido por WhatsApp", url_wa, type="primary", use_container_width=True)
    else:
        st.write("Tu carrito está esperando por repuestos de calidad.")

    st.sidebar.caption("Universo")

if __name__ == "__main__":
    main()