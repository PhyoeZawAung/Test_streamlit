import streamlit as st
from io import StringIO
import io
import pandas as pd
messenger_file = st.file_uploader("Enter Your Messenger Dowmloaded file here")

if messenger_file is not None:
  st.write(messenger_file.name)
    

     
