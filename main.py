import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# st.columns(2) returns 2 columns and we stored them in col1,col2
col1 , col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ravi Konjeti")
    content = """
    This is Ravi Konjeti.I am Software engineer by profession.
    """
    st.info(content)


st.write("Below you can find some of the apps i have built in python, Feel free to contact me")

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep = ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
