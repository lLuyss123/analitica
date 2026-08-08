import plotly.express as px
import streamlit as st



def grafico_p1(total_genero):

    fig = px.bar(
        total_genero.head(10),
        x="Unique Genres",
        y="Country of Origin",
        text="Unique Genres",
        title="Top 10 Countries by Musical Genre Diversity",
        color_discrete_sequence=["#1DB954"]
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_yaxes(
        autorange="reversed"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )
    
def grafico_p2(relacion):
    fig = px.scatter(
    relacion,
    x="Debut Year",
    y="Total Streams (in millions)",
    title="Relationship Between Debut Year and Total Streams",
    color="Debut Year",
    opacity=0.6,
    trendline="ols"
    )
    st.plotly_chart(
            fig,
            width="stretch"
        )
    
def grafico_p3(relacion):
    fig = px.scatter(
    relacion,
    x="Primary Language",
    y="Total Streams (in millions)",
    title="Relationship Between Primary Language and Total Streams"
    )
    st.plotly_chart(
            fig,
            width="stretch"
        )

def grafico_p4(media):
    fig = px.bar(
        media,
        x="Primary Language",
        y="Total Streams (in millions)",
        title="Median Total Streams by Primary Language"
    )
    st.plotly_chart(
        fig,
        width="stretch"
    )

