import streamlit as st
left,right = st.columns(2)

with left:
    if st.button("Press me"):
        "Hello do you press me"
        
with right:
    data = st.radio("Choose the data",'mama','koko','mgmg')
    print("You choose {data} love")
