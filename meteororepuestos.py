import streamlit as st
import pandas as pd
import urllib.parse

def main():
    # Título y Navegación
    st.title("⚙️ Meteoro-Repuestos: Marketplace")
    st.info("💡 Use la barra de la izquierda para navegar entre los diferentes módulos.")
    st.markdown("---")

    # --- CONFIGURACIÓN DE IMÁGENES DESDE GITHUB RAW ---
    # IMPORTANTE: Reemplaza con tus datos reales de GitHub
    usuario = "alfonsocanase"  # Tu usuario de GitHub
    repo = "XliteDev"           # Tu repositorio
    branch = "main"             # Tu rama principal
    
    base_url = f"https://raw.githubusercontent.com/{usuario}/{repo}/{branch}/"

    # 1. Base de Datos de Productos
    productos = [
        {
            "id": 1,
            "nombre": "Aceite 20w50 litro",
            "precio": 40000,
            "imagen": f"{base_url}meteororespuestos1.jpg"
        },
        {
            "id": 2,
            "nombre": "Llanta 220",
            "precio": 200000,
            "imagen": f"{base_url}meteororespuestos2.jpg"
        }
    ]

    # Inicializar carrito en la sesión
    if 'carrito_repuestos' not in st.session_state:
        st.session_state.carrito_repuestos = []

    # 2. Visualización de Productos en Columnas
    st.subheader("Catálogo de Repuestos")
    
    cols = st.columns(2)
    
    for i, prod in enumerate(productos):
        with cols[i]:
            # El parámetro use_container_width ajusta la imagen al ancho de la columna
            st.image(prod["imagen"], caption=prod["nombre"], use_container_width=True)
            st.write(f"**Precio:** ${prod['precio']:,}")
            if st.button(f"Añadir {prod['nombre']}", key=f"btn_{prod['id']}"):
                st.session_state.carrito_repuestos.append(prod)
                st.toast(f"✅ {prod['nombre']} añadido")

    # 3. Carrito y Finalización de Pedido
    st.markdown("---")
    st.subheader("🛒 Resumen de Compra")

    if st.session_state.carrito_repuestos:
        df_carro = pd.DataFrame(st.session_state.carrito_repuestos)
        st.table(df_carro[["nombre", "precio"]])
        
        total = df_carro["precio"].sum()
        st.write(f"### Total a Pagar: ${total:,}")

        col_acc1, col_acc2 = st.columns(2)
        
        with col_acc1:
            if st.button("🗑️ Vaciar Carrito"):
                st.session_state.carrito_repuestos = []
                st.rerun()
        
        with col_acc2:
            # WhatsApp al número de Meteoro
            celular_ventas = "3122204688"
            mensaje_base = "Hola Meteoro-Repuestos, quiero comprar:\n"
            detalles = ""
            for item in st.session_state.carrito_repuestos:
                detalles += f"- {item['nombre']} (${item['precio']:,})\n"
            
            mensaje_final = f"{mensaje_base}{detalles}\n*Total: ${total:,}*"
            url_wa = f"https://wa.me/57{celular_ventas}?text={urllib.parse.quote(mensaje_final)}"
            
            st.link_button("🚀 Pedir por WhatsApp", url_wa, type="primary", use_container_width=True)
    else:
        st.write("Tu carrito está vacío.")

    # Pie de página
    st.sidebar.markdown("---")
    st.sidebar.caption("Universo")

if __name__ == "__main__":
    main()