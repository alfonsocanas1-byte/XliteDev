import streamlit as st
import pandas as pd
import json

def main():
    # Título y Navegación sutil
    st.title("⛽ Meteoro-Combustible: Precios")
    st.caption("Consulta los precios actualizados de gasolina por estación.")
    st.markdown("---")

    # 1. Definición de Datos con Pandas
    data_gasolina = {
        "Estación de Servicio": [
            "Primax Roosevelt", 
            "Texaco Portada al Mar"
        ],
        "Gasolina Extra": [22000, 21200],
        "Gasolina Corriente": [16000, 15400]
    }
    
    df_precios = pd.DataFrame(data_gasolina)

    # 2. Visualización de Precios
    st.subheader("Costos por Estación (Cali)")
    
    # Formateamos la tabla para que los precios se vean con signo de pesos
    st.table(df_precios.style.format({
        "Gasolina Extra": "${:,.0f}",
        "Gasolina Corriente": "${:,.0f}"
    }))

    # 3. Resumen en formato JSON
    st.markdown("---")
    with st.expander("Ver datos técnicos (JSON)"):
        json_data = df_precios.to_json(orient="records")
        st.json(json.loads(json_data))

    # Pie de página lateral
    st.sidebar.markdown("---")
    st.sidebar.caption("Ecosistema Meteoro")

if __name__ == "__main__":
    main()