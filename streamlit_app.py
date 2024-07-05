import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to NagornisGay!
# x!
"""
def click():
    st.balloons()
num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)
size = st.slider("size", 0, 10)
indices = np.linspace(0, size, num_points)
theta = 2 * np.pi * num_turns * indices
radius = np.linspace(0, size, num_points)
chat = st.chat_input()
st.button("press",on_click=click)
with st.sidebar.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')
st.download_button('truth','nagorn is gay','the truth')
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = radius*radius - x*x - y*y
a = st.sidebar.button('Menu')
b = st.sidebar.button('Nagorn loves ut toot')
df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})
st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x"),
        y=alt.Y("y"),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
