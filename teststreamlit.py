import streamlit as st
sidebar_selectData  = st.sidebar.selectbox(
"Choose to contact developar",("mail","Phone:","Facebook")
)
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
