import streamlit as st

messenger_file = st.file_uploader("Enter Your Messenger Dowmloaded file here")
if messenger_file is not None:
  st.write("file uploaded")
  bytes_data = messenger_file.getvalue()
  st.write(bytes_data)
