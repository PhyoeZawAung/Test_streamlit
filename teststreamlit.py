import streamlit as st
x = st.selectbox("Choice the number of x ",(1,2,3,4,5))
st.write(x,"the square is ", x*x)
