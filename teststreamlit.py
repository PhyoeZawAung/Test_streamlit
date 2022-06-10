import streamlit as st
from zipfile import ZipFile
import json
messenger_file = st.file_uploader("Enter Your Messenger Dowmloaded file here")

if messenger_file is not None:
  st.write(messenger_file.name)
  with open(messenger_file,"r") as data:
    mdata = json.load(data)
    st.write(mdata)
  #with ZipFile(messenger_file, 'r') as zip:
    #zip.printdir()
    ##st.write('Extracting all the files now...')
    #zip.extractall()
    #st.write('Done!')

  


     
