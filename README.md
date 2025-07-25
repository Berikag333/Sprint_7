# Sprint_7
Construir y desplegar un panel de control de una aplicación web en un servicio en la nube.
# Streamlit App – Análisis Exploratorio de Vehículos Usados

Este proyecto fue desarrollado como parte del Sprint 7 del programa de TripleTen, con el objetivo de construir una aplicación web interactiva que permita visualizar y explorar un conjunto de datos sobre vehículos usados en venta en EE.UU.

## Funcionalidades de la App

La aplicación fue creada con **Streamlit** y permite:

- Visualizar un histograma de la columna `odometer` (kilometraje) con un solo clic.
- Generar un gráfico de dispersión `odometer vs price` filtrado por tipo de vehículo.
- Explorar de forma interactiva los datos a través de un panel gráfico.
- Ejecutar análisis exploratorio directamente desde un archivo Jupyter Notebook (`EDA.ipynb`).

## Tecnologías utilizadas

- Python 3
- pandas
- streamlit
- plotly.express
- Jupyter Notebook

## Estructura del Proyecto
Sprint_7/
├── app.py # Aplicación principal en Streamlit
├── requirements.txt # Librerías necesarias para ejecutar la app
├── vehicles_us.csv # Conjunto de datos utilizado
├── README.md # Documentación del proyecto
└── notebooks/
└── EDA.ipynb # Notebook de análisis exploratorio


