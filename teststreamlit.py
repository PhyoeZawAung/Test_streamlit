import streamlit as st
import numpy as np
data = np.random.randn(10,20)
st.dataframe(data)
