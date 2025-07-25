import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la app
st.header('📊 Explorador de Datos de Vehículos en Venta')

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Botón 1: Histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para la columna odómetro')
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón 2: Gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para odómetro vs precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="type",
                             title="Relación entre Odómetro y Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)

