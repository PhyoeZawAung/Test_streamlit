import streamlit as st
sidebar_selectData  = st.sidebar.selectbox(
"Choose to contact developar",("mail","Phone:","Facebook")
)
sidebar_Slider =st.side.slider("Choose",0.0,100,(25.0,75.0))
