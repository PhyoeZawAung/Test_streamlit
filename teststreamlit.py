import streamlit as st
file = st.file_uploader("Chooose a file")

 if file is not None:
    st.write("file uploaded")

