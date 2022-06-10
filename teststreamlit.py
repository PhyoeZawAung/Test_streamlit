import streamlit as st
from zipfile import ZipFile
import json
from io import StringIO
messenger_file = st.file_uploader("Enter Your Messenger Dowmloaded file here")

if messenger_file is not None:
  st.write(messenger_file.name)
  stringio = StringIO(messenger_file.getvalue().decode("utf-8"))
  st.write(stringio)
  with open(messenger_file.name,"r") as data:
    mdata = json.load(data)
    st.write(mdata)
  #with ZipFile(messenger_file, 'r') as zip:
    #zip.printdir()
    ##st.write('Extracting all the files now...')
    #zip.extractall()
    #st.write('Done!')

  


     
