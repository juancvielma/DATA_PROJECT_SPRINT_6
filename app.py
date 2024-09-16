"""
Este script carga un conjunto de datos de coches usados y permite al usuario
crear visualizaciones interactivas utilizando Streamlit y Plotly. Los gráficos incluyen:
- Histograma de la columna 'odometer'
- Gráfico de dispersión de 'odometer' frente a 'price'
- Gráfico de dispersión por modelo seleccionado
"""

import pandas as pd
import plotly.express as px  # Importación correcta para plotly.express
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título del dashboard
st.title("Análisis de Datos de Vehículos Usados")

# Descripción del proyecto
st.write("""
Este proyecto permite visualizar y analizar un conjunto de datos de vehículos usados.
Utiliza Plotly para gráficos interactivos y Streamlit para una interfaz intuitiva.
""")

# Selección de tipo de gráfico
st.header("Visualizaciones Generales")
col1, col2 = st.columns(2)

with col1:
    hist_button = st.button('Construir Histograma')
with col2:
    scat_button = st.button('Construir gráfico de dispersión')

# Mostrar gráfico dependiendo de qué botón se selecciona
if hist_button:
    st.subheader('Histograma de Odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if scat_button:
    st.subheader('Gráfico de Dispersión: Odometer vs Precio')
    fig = px.scatter(car_data, x='odometer', y='price', color='price')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para un histograma adicional
st.subheader("Opciones adicionales")
build_histogram = st.checkbox('Construir un histograma adicional')
if build_histogram:
    st.write('Construcción de un histograma adicional para la columna odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Dropdown de modelos
st.header("Gráfico de Dispersión por Modelo")
modelos = car_data['model'].unique()

# Selección de modelo
modelo_seleccionado = st.selectbox('Selecciona un modelo:', modelos)

# Función para graficar por modelo


def graficar_por_modelo(modelo):
    # Filtrar los datos por el modelo seleccionado
    df_filtrado = car_data[car_data['model'] == modelo]

    # Crear gráfico de dispersión para el modelo seleccionado
    fig = px.scatter(df_filtrado, x='year', y='price',
                     color='fuel', title=f'Precio vs Año para {modelo}')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)


# Llamar a la función para graficar cuando se selecciona un modelo
if modelo_seleccionado:
    graficar_por_modelo(modelo_seleccionado)
