import pandas as pd
import streamlit as st
import lotka
import numpy as np

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
    tab1, tab2, tab3 = st.tabs(["📈 Wykres", "📈 Wykres fazowy", "📈 Pole wektorowe"])
    with tab1:
        st.line_chart(lotka.wykres(alpha, beta, delta, gamma))

    with tab2:
        st.image("faze.png")


with st.container():
    st.markdown(
        "<h1 style='text-align: center'>Równanie różniczkowe Lotki-Volterry zwane także układ drapieżnik ofiara</h1>",
        unsafe_allow_html=True,
    )
    st.markdown("In this section we consider more realistic models that take into account the interaction of two species in the same habitat. We will see that these models take theform of a pair of linked differential equations.")
    st.markdown("Examples of prey and predators include ")
    st.markdown("- rabbits and wolves in an isolated forest, ")
    st.markdown("- food-fish and sharks, ")
    st.markdown("- aphids and ladybugs, ")
    st.markdown("- bacteria and amoebas")
    st.markdown("## The Lotka-Volterra Equations")
    st.markdown("![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/79752d662d4760abcc84c6f0bb94d708f17ff442)")
    st.markdown("### Defining the equations\n From the above equation, the parameters can be thought of as the following:\n")
    st.markdown("* $\\frac{dx}{dt}$ = growth rate of rabbit population\n * $\\frac{dy}{dt}$ = growth rate of fox population\n")
    st.markdown("* $x$ = prey population \n * $y$ = predator population\n \n * $\\alpha$ = growth rate of prey\n * $\\beta$ = death rate of prey due to predatation \n * $\\gamma$ = natural death rate of predator\n * $\\delta$ = factor describing how many consumed prey create a new predator\n")
    st.markdown( "### Physical Meaning of the Equations\n")