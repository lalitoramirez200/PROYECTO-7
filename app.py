import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# encabezado de la aplicación
st.header('Análisis de anuncios de venta de coches')

# botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: odómetro vs precio')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
