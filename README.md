# data_project_sprint6
This repository is a project from my Sprint 6 of my bootcamp, where I will showcase everything I have learned so far. It serves to demonstrate the extent of the knowledge I have acquired up to this point.

# Proyecto: Visualización de Datos de Vehículos Usados

Este proyecto utiliza Streamlit para la visualización interactiva de un conjunto de datos de anuncios de venta de vehículos usados. El código permite al usuario construir histogramas y gráficos de dispersión a partir de las métricas de los vehículos, como el odómetro. El conjunto de datos se carga desde un archivo CSV y las visualizaciones se generan usando Plotly.

## Tecnologías utilizadas

- **Pandas**: Para la manipulación y análisis del conjunto de datos.
- **Plotly**: Para la creación de gráficos interactivos (histogramas y gráficos de dispersión).
- **Streamlit**: Para la creación de la interfaz interactiva.

## Estructura del código

### Importaciones

- **pandas**: Se usa para leer y manipular el archivo CSV que contiene los datos de los vehículos.
- **plotly**: Se utiliza para generar gráficos interactivos.
- **streamlit**: Se emplea para crear la interfaz web y permitir la interacción con los botones y checkboxes.

### Carga de datos

El conjunto de datos se carga mediante la función `pd.read_csv()`, apuntando al archivo `vehicles_us.csv` que contiene información de anuncios de vehículos usados.

```python
car_data = pd.read_csv('/Users/juanvielmapereyra/NOTEBOOKS/projects/data_project_sprint6/vehicles_us.csv')
```

### Interfaz interactiva

La aplicación de Streamlit presenta dos botones:

- **Construir Histograma**: Al presionar este botón, se genera un histograma basado en la columna "odometer" del conjunto de datos, que muestra el kilometraje de los vehículos.
  
- **Construir Gráfico de Dispersión**: Similar al histograma, aunque en este caso, parece ser que también genera un histograma basado en la misma columna.

```python
hist_button = st.button('Construir Histograma')
scat_button = st.button('Construir gráfico de disperción')
```

### Gráficos

- **Histograma**: Se genera utilizando `plotly.express.histogram()` para mostrar la distribución de kilometraje de los vehículos en venta.

```python
if hist_button:
    st.write('Creacción de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
```

### Otras características

Hay un checkbox que permite al usuario elegir si desea construir un histograma manualmente para la columna de odómetro.

```python
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
```



## Conjunto de datos

El conjunto de datos utilizado en este proyecto es un archivo CSV que contiene información de anuncios de vehículos usados en los Estados Unidos. Algunos de los campos relevantes son:

- `odometer`: El kilometraje del vehículo.
- Otras columnas que puedes analizar o visualizar.


