import streamlit as st

messenger_file = st.file_uploader("Enter Your Messenger Dowmloaded file here",accept_multiple_files=True)
if messeger_file is not None:
  for file in messenger_file:
     bytes_data = file.read()
     st.write("filename:",file.name)
     st.write(bytes_data)
