"""
Este script carga un conjunto de datos de coches usados y permite al usuario 
crear visualizaciones interactivas utilizando Streamlit y Plotly. Los gráficos incluyen:
- Histograma de la columna 'odometer'
- Gráfico de dispersión de 'odometer' frente a 'price'
"""

import pandas as pd
import plotly.express as px  # Importación correcta para plotly.express
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')


# Botones para seleccionar tipo de gráfico
hist_button = st.button('Construir Histograma')
scat_button = st.button('Construir gráfico de dispersión')

# Si se pulsa el botón para el histograma
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches'
    )
    fig = px.histogram(car_data, x='odometer')  # Crear el histograma
    st.plotly_chart(fig, use_container_width=True)  # Mostrar el histograma

# Si se pulsa el botón para el gráfico de dispersión
if scat_button:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches'
    )
    # Crear gráfico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price')
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)

# Checkbox opcional para construir el histograma
build_histogram = st.checkbox('Construir un histograma adicional')
if build_histogram:
    st.write('Construcción de un histograma adicional para la columna odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
