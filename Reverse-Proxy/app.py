import streamlit as st

st.title("Hello from Streamlit on EC2!")

st.write("This is a simple app to test NGINX reverse proxy.")

name = st.text_input("Enter your name:")

if name:
    st.success(f"Welcome, {name}!")
