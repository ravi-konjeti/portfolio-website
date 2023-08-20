import streamlit as st
import pandas as pd
#import
st.set_page_config(layout="wide")

# st.columns(2) returns 2 columns and we stored them in col1,col2
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image("images/photo-output Copy.jpg", width=230)

with col2:
    st.title("Ravi Konjeti")
    st.info("Linkedin - https://www.linkedin.com/in/ravi-k-64126523a/")
    content = """
    Hey, Thank you for visiting my web portfolio.
    """
    subheader_content = """I developed various applications using numerous libraries and dependencies in Python."""
    subheader3_cotent = """I am open to work. Feel free to contact me."""
    subheader4_content = """I developed an Excel to Pdf converter, to install it you can use the following command in your code editor"""
    info_content = """pip install pdfinv-generator"""
    st.subheader(content)
    st.subheader(subheader3_cotent)
    st.info(subheader4_content)
    st.subheader(info_content)

