import streamlit as st
import pandas as pd
import numpy as np
number = np.random.randn(10,20)
st.dataframe(number)
