import streamlit as st
file = st.file_uploader("Chooose a file")

if file is not None:
    st.write("file uploaded")
    # To convert to a string based IO:
    stringio = StringIO(file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)


