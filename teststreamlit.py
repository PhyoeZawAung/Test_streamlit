import streamlit as st
import jina as jn
st.set_page_config(page_title="Jina Text Search",)

endpoint = "http://0.0.0.0:45678/api/search" # This is Jina's default endpoint. If your Flow uses something different, switch it out

st.title("Jina Text Search")

jn.text_search(endpoint=endpoint)
