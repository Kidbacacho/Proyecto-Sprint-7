import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header('Análisis de Datos de Vehículos - Streamlit Dashboard')

# Cargar el dataset
car_data = pd.read_csv('vehicles_us.csv')  # Asegúrate de que el archivo esté en la ruta correcta

# Checkbox para histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión: Precio vs. Kilometraje')
    fig2 = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig2, use_container_width=True)