import streamlit as st
import numpy as np
data = np.random.randn(1,10)
st.dataframe(data)
