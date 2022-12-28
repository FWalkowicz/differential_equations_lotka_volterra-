import streamlit as st
import lotka
import numpy as np

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center'>Równanie różniczkowe Lotki-Volterry</h1>", unsafe_allow_html=True)

inputs, outputs = st.columns([1, 3])
with inputs:
    alpha = st.slider('Alpha', 0, 10, 1)
    beta = st.slider('beta', 0, 10, 1)
    delta = st.slider('delta', 0, 10, 1)
    gamma = st.slider('gamma', 0, 10, 1)

with outputs:
    tab1, tab2, tab3 = st.tabs(["📈 Wykres", "📈 Wykres fazowy", "📈 Pole wektorowe"])
    with tab1:
        st.image('diagram.png')

    with tab2:
        st.image('faze.png')


with st.container():
    st.markdown("<h1 style='text-align: center'>Równanie różniczkowe Lotki-Volterry zwane także układ drapieżnik ofiara</h1>", unsafe_allow_html=True)
    st.markdown("Rownania tego typu rozważają sytuację interakcji dwóch gatunków w tym samym środowisk. Modele te przyjmują postać pary sprzężonych równań różniczkowych.")
    st.markdown("Przykładami układu drapieżnik-ofiara mogą być:")
    st.markdown("- wilk i zając")
    st.markdown("- rekiny i ryby")
    st.markdown("- biedronki i mszyce")
    st.markdown("- ameby i bakterie")
    st.markdown("Przez Z(t) oznaczymy liczbę ofiar, a W(t) będzie liczbą drapieżników w chwili t.")
    st.markdown("Przy braku drapieżnika wystarczające zasoby pożywienia prowadziłyby do wykładniczego wzrostu populacji ofiar, to znaczy: ")
    st.latex(r'''\frac{dZ}{dt} = kZ, gdzie k jest dodatnią stałą''')
    st.markdown("Przy braku ofiary zakładamy, że populacja drapieżnika zmniejszyłaby się wskutek śmiertelności proporcjonalnej do wielkości populacji, to znaczy: ")
    st.latex(r'''\frac{dW}{dt} = -rW, gdzie r jest dodatnią stałą''')
    st.markdown("Gdy oba te gatunki żyją w tym samym środowisku, zakładamy że główną przyczyną śmierci ofiar jest bycie zjedzonym przez drapieżnika. "
                "Liczba drapieżników będzie wyznaczana dzięki dostępnemu pożywieniu czyli liczby ofiar. Zakładamy również że oba gatunki nartafiają na siebie z częstotliwością"
                "proporcjonalną do wielkości obu populacji. Te dwa założenia pozwolą nam wyznaczyć układ równań różniczkowych: ")
    st.latex(r'''\left{\frac{dZ}{dt}}''')

