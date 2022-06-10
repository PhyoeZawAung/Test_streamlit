import streamlit as st
from zipfile import ZipFile
messenger_file = st.file_uploader("Enter Your Messenger Dowmloaded file here")

if messenger_file is not None:
  st.write(messenger_file.name)
  with ZipFile(messenger_file, 'r') as zip:
    st.write(zip.is_dir())
    st.write(zip.printdir())

  


     
