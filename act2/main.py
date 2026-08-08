# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import plotly.express as px
import streamlit as st

from graficos import *

# Set the path to the file you'd like to load
file_path = "Most Streamed Artists on Spotify (17_07_2026) V1.1.csv"

# Load the latest version
df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "rishavsvault/most-streamed-artists-on-spotify",
        file_path
    )

#ANTES DE NORMALIZAR VERIFICAMOS QUE TODO EL CONJUNTO DE DATOS 
#NO TENGA REPETIDOS O NULOS O DATOS ERRONEOS PARA CORREGIRLOS Y LUEGO ARREGLARLOS 

#NORMALIZAMOS LAS TABLAS
df_artistas = pd.read_excel("artistas.ods", engine="odf")
df_country = pd.read_excel("country.ods", engine="odf")
df_estadisticas = pd.read_excel("estadisticas.ods", engine="odf")
df_genre = pd.read_excel("genre.ods", engine="odf")
df_lenguage = pd.read_excel("lenguage.ods", engine="odf")
df_sexo = pd.read_excel("sexo.ods", engine="odf")
df_type = pd.read_excel("type.ods", engine="odf")


#¿Qué países muestran mayor diversidad de géneros musicales? 
grupo_paises = df.groupby(["Country of Origin"])
total_genero=grupo_paises["Primary Genre"].nunique().sort_values(ascending=False)
total_genero= total_genero.reset_index()
total_genero= total_genero.rename(columns={
    "Primary Genre":"Unique Genres"
}) 
print(total_genero)
st.set_page_config(
    page_title="Spotify Analytics",
    layout="wide"
)
grafico_p1(total_genero)

#¿Existe relación entre el año de debut y el número de streams? 

relacion = df[["Debut Year", "Total Streams (in millions)"]].sort_values(
    by="Debut Year",
    ascending=True
)

grafico_p2(relacion)

# ¿El idioma influye realmente en el alcance global de un artista o existen excepciones importantes?

relacion2 = df[["Primary Language", "Total Streams (in millions)"]]
grafico_p3(relacion2)

media=df.groupby("Primary Language")["Total Streams (in millions)"].median().reset_index()
print(media)
grafico_p4(media)