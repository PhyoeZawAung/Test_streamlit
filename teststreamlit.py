import streamlit as st
from zipfile import ZipFile
import json
from io import StringIO
messenger_file = st.file_uploader("Enter Your Messenger Dowmloaded file here")

if messenger_file is not None:
  st.write(messenger_file.name)
  stringio =messenger_file.getvalue()
  st.write(stringio)
  jsonData = json.loads(stringio)
  st.write(jsonData)
  
  
  
 
  #with ZipFile(messenger_file, 'r') as zip:
    #zip.printdir()
    ##st.write('Extracting all the files now...')
    #zip.extractall()
    #st.write('Done!')

  


     
