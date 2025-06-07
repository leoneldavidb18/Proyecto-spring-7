import streamlit as st
import pandas as pd
import plotly.express as px

car_data= pd.read_csv('vehicles_us.csv')
st.header('Análisis Vehículos')

st.title('Datos de análisis de vehículos')
st.subheader('Tabla de datos original')
st.dataframe(car_data)

hist_button = st.checkbox('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

dis_button = st.button('Crear un gráfico de dispersión')

if dis_button:
       fig = px.scatter(car_data, x="odometer", y="price",
                     title="Relación entre odómetro y precio",
                     labels={"odometer": "Kilometraje", "price": "Precio"})
       st.plotly_chart(fig) # crear gráfico de dispersión

carros_mas_vendidos = car_data.groupby('model')['price'].count().sort_values(ascending=False)
carros_mas_vendidos = carros_mas_vendidos.reset_index()
carros_mas_vendidos.columns= ['Modelo', 'Cantidad de ventas']

st.subheader("Modelo de carros más vendidos")
st.dataframe(carros_mas_vendidos)

car_button = st.button('Gráfico de ventas')

if car_button:
        fig =px.bar(carros_mas_vendidos.head(10), x='Modelo', y='Cantidad de ventas', title= 'Top 10 modelos más vendidos',labels={'Cantidad de ventas': 'Cantidad'})
        st.plotly_chart(fig)