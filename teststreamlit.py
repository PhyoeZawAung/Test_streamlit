import os
import glob
from pathlib import Path
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
    print("Extracting all file now")
    allFile = archive.extractall()
    print("Done")
    st.write("Done")
    st.write("all the extrected file are" , allFile)
    

obj = os.scandir()

# List all files and directories in the specified path
print("Files and Directories in '% s':")
for entry in obj:
	if entry.is_dir() or entry.is_file():
		print(entry.name)

print("Using glob.glob()")
files = glob.glob('messages/**/*.*', 
                   recursive = True)
for file in files:
    if '.json' in file:
       print(file)
       parent = Path(file).parent
       for entry in parent.iterdir():
        allFile = entry
        if allFile is not None:
         st.write(allFile.name)
         jsonData = json.loads(allFile.getvalue())
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

  


     
