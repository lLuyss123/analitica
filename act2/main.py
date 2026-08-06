# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import plotly.express as px
import streamlit as st


# Set the path to the file you'd like to load
file_path = "Most Streamed Artists on Spotify (17_07_2026) V1.1.csv"

# Load the latest version
df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "rishavsvault/most-streamed-artists-on-spotify",
        file_path
    )

""" ANTES DE NORMALIZAR VERIFICAMOS QUE TODO EL CONJUNTO DE DATOS 
NO TENGA REPETIDOS O NULOS O DATOS ERRONEOS PARA CORREGIRLOS Y LUEGO ARREGLARLOS """

""" NORMALIZAMOS LAS TABLAS """
df_artistas = pd.read_excel("artistas.ods", engine="odf")
df_country = pd.read_excel("country.ods", engine="odf")
df_estadisticas = pd.read_excel("estadisticas.ods", engine="odf")
df_genre = pd.read_excel("genre.ods", engine="odf")
df_lenguage = pd.read_excel("lenguage.ods", engine="odf")
df_sexo = pd.read_excel("sexo.ods", engine="odf")
df_type = pd.read_excel("type.ods", engine="odf")

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

fig = px.bar(
            total_genero.head(10),
              x = "Unique Genres",
              y = "Country of Origin",
              text="Unique Genres",
              title="Top 10 Countries by Musical Genre Diversity",
              color_discrete_sequence=["#1DB954"]
              )

fig.update_traces(textposition="outside")
fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig, width="stretch")
st.markdown("""
### Conclusion

The United States has the highest musical genre diversity in the dataset, with 16 unique genres. Germany and the United Kingdom follow with six genres each, indicating a broader musical variety than the remaining countries in the top 10.
""")
