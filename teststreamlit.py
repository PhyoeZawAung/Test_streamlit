import streamlit as st
import numpy as np
data = np.random.randn(100,100)
st.dataframe(data)
