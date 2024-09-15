import pandas as pd
import plotly as px
import streamlit as st

car_data = pd.read_csv(
    '/Users/juanvielmapereyra/NOTEBOOKS/projects/data_project_sprint6/vehicles_us.csv')
hist_button = st.button('Construir Histograma')
scat_button = st.button('Construir gráfico de disperción')

if hist_button:
    st.write(
        'Creacción de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

if scat_button:
    st.write(
        'Creacción de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
