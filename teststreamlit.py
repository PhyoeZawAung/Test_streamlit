import streamlit as st
from zipfile import ZipFile
import json
from io import StringIO
import datetime
from datetime import datetime
allFile = None
messenger_file = st.file_uploader("Enter Your Messenger Dowmloaded file here")

if messenger_file is not None:
  with ZipFile(messenger_file , "r") as archive:
    archive.printdir()
    st.write("Extracting all the file now")
    allFile = archive.extractall()
    st.write("Done")
    st.write("all the extrected file are" , allFile)
path = "messages/inbox/kyawzinphyo_hwfoewmdtq/message_1.json"
if path is not None:
  st.write(path)
  jsonData = json.loads(path.getvalue())
  
  for message in jsonData["messages"]:
                try:
                    date = datetime.fromtimestamp(message["timestamp_ms"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
                    sender = message["sender_name"]
                    content = message["content"]
                    st.write("date     ,sender     ,content")
                    st.write(date,"     " , sender ,"    ", content)

                except KeyError:
                    pass
  
  
  
  
  
 
  #with ZipFile(messenger_file, 'r') as zip:
    #zip.printdir()
    ##st.write('Extracting all the files now...')
    #zip.extractall()
    #st.write('Done!')

  


     
