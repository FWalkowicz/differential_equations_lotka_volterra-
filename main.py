import streamlit as st
import lotka
from pathlib import Path
from PIL import Image

st.set_page_config(layout="wide")

st.markdown(
    "<h1 style='text-align: center'>Równanie różniczkowe Lotki-Volterry</h1>",
    unsafe_allow_html=True,
)

inputs, outputs = st.columns([2, 5])
with inputs:
    alpha = st.slider("Alpha - birth rate of prey", 0.0, 1.0, 0.58, 0.01)
    beta = st.slider(
        "Beta - death rate of prey due to predators", 0.0, 1.0, 0.34, 0.001
    )
    delta = st.slider("Delta - natural death rate of predators", 0.0, 1.0, 0.12, 0.01)
    gamma = st.slider(
        "gamma - factor that describes how many eaten preys give birth to a new predator",
        0.0,
        1.0,
        0.2,
        0.00001,
    )


with outputs:
    st.line_chart(lotka.wykres(alpha, beta, delta, gamma))


with st.container():
    st.markdown(
        "<h1 style='text-align: center'>Równania Lotki-Volterry zwane także układ drapieżnik-ofiara</h1>",
        unsafe_allow_html=True,
    )
    def read_markdown_file(markdown_file):
        return Path(markdown_file).read_text()

    intro_markdown = read_markdown_file("Treść do mówienia.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    image = Image.open('320882178_2164821780369367_5264403790324036163_n.png')
    image2 = Image.open('321084715_3494783160794414_5211654160384390375_n.png')
    st.image(image, width=600)
    st.image(image2, width=600)
