import streamlit as st
from os inport stringIO
messenger_file = st.file_uploader("Enter Your Messenger Dowmloaded file here",accept_multiple_files=True)
if messenger_file is not None:
  for file in messenger_file:
     bytes_data = file.read()
     st.write("filename:",file.name)
     stringio = StringIO(file.getvalue().decode("utf-8"))
     st.write(stringio)
     
