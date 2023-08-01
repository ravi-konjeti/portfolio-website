import streamlit as st
import pandas as pd
#import
st.set_page_config(layout="wide")

# st.columns(2) returns 2 columns and we stored them in col1,col2
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo-output Copy.JPG")

with col2:
    st.title("Ravi Konjeti")
    st.info("Linkedin - https://www.linkedin.com/in/ravi-k-64126523a/")
    content = """
    Hey, Thank you for visiting my web portfolio.
    """
    subheader_content = """I developed various applications using numerous libraries and dependencies in Python."""
    subheader2_content = """You can find my applications source code in All Projects side bar."""
    subheader3_cotent = """I am open to work. Feel free to contact me."""
    info_content = """pip install pdfinv-generator."""
    st.subheader(content)
    st.subheader(subheader2_content)
    st.subheader(subheader3_cotent)
    st.info(info_content)

