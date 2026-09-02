import streamlit as st

# Título
st.title("🚀 Mi primera App con Streamlit")

st.write("Esta aplicación está hecha completamente con Python.")

# Entrada de texto
nombre = st.text_input("¿Cuál es tu nombre?")

# Selector
departamento = st.selectbox(
    "Selecciona tu departamento:",
    ["Ventas", "Finanzas", "Operaciones", "Data Analytics"]
)

# Slider
ventas = st.slider(
    "Venta mensual ($)",
    min_value=0,
    max_value=1000000,
    value=250000,
    step=10000
)

# Botón
if st.button("Calcular"):

    st.success(f"Hola {nombre} 👋")

    st.write("Departamento:", departamento)

    st.metric(
        label="Venta mensual",
        value=f"${ventas:,.0f}"
    )

    venta_anual = ventas * 12

    st.metric(
        label="Venta anual estimada",
        value=f"${venta_anual:,.0f}"
    )

    if ventas >= 500000:
        st.success("🔥 Excelente nivel de ventas")
    else:
        st.warning("Hay oportunidad de crecimiento")