import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# encabezado de la aplicación
st.title('Análisis de anuncios de venta de coches')
st.markdown('Esta aplicación permite explorar visualmente los datos de anuncios de venta de coches.')

# botón para histograma
st.subheader('Visualizaciones')
hist = st.checkbox('Mostrar histograma del odómetro')

if hist:
    st.write('Cantidad de coches según el odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# botón para gráfico de dispersión
scatter = st.checkbox('Mostrar gráfico de dispersión')

if scatter:
    st.write('Relación entre el odómetro y el precio')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)