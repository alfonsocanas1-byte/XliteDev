import streamlit as st
import pandas as pd
import urllib.parse

# Configuración de la página
st.set_page_config(page_title="Restaurante Sebas Gourmet", page_icon="🍴")

def main():
    st.title("🍴 Restaurante Sebas Gourmet")
    st.markdown("---")

    # 1. Definición de Datos (Menú)
    menu_data = {
        "Producto": [
            "Arroz con pollo", 
            "Sudado con arroz y papa", 
            "Lasagña", 
            "Porción de yuca frita"
        ],
        "Precio": [17000, 20000, 20000, 7000]
    }
    df_menu = pd.DataFrame(menu_data)

    # 2. Interfaz de Selección
    st.subheader("Nuestro Menú")
    
    # Inicializar carrito en la sesión si no existe
    if 'carrito' not in st.session_state:
        st.session_state.carrito = []

    for index, row in df_menu.iterrows():
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.write(f"**{row['Producto']}**")
        with col2:
            st.write(f"${row['Precio']:,}")
        with col3:
            if st.button(f"Añadir", key=f"btn_{index}"):
                st.session_state.carrito.append({"Producto": row['Producto'], "Precio": row['Precio']})
                st.toast(f"Añadido: {row['Producto']}")

    # 3. Resumen del Pedido (Carrito)
    st.markdown("---")
    st.subheader("🛒 Tu Pedido")

    if st.session_state.carrito:
        df_carrito = pd.DataFrame(st.session_state.carrito)
        st.table(df_carrito)
        
        total = df_carrito["Precio"].sum()
        st.write(f"### Total: ${total:,}")

        # Botón para limpiar carrito
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = []
            st.rerun()

        # 4. Configuración de WhatsApp
        st.markdown("---")
        nombre_cliente = st.text_input("Tu nombre para el pedido:")
        
        if st.button("🚀 Enviar Pedido por WhatsApp"):
            if nombre_cliente:
                # Construcción del mensaje
                mensaje_base = f"Hola Sebas Gourmet, mi nombre es {nombre_cliente}. Quisiera pedir:\n"
                detalles = ""
                for item in st.session_state.carrito:
                    detalles += f"- {item['Producto']} (${item['Precio']:,})\n"
                
                mensaje_final = f"{mensaje_base}{detalles}\n*Total: ${total:,}*"
                
                # Formatear URL de WhatsApp
                telefono = "573128942010"
                encoded_msg = urllib.parse.quote(mensaje_final)
                ws_url = f"https://wa.me/{telefono}?text={encoded_msg}"
                
                st.markdown(f'[Confirmar pedido en WhatsApp]({ws_url})')
            else:
                st.warning("Por favor, ingresa tu nombre antes de enviar.")
    else:
        st.info("El carrito está vacío. ¡Antójate de algo!")

if __name__ == "__main__":
    main()