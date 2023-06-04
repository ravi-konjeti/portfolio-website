import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("your message")
    button = st.form_submit_button("Submit")
    print(button)#button is false when it is not presssed and returns true once submit is pressed
    if button:
        message = message + user_email
        print(button)