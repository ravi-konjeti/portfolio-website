import streamlit as st

st.set_page_config(layout="wide")

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