import streamlit as st
import pandas as pd
import numpy as np
if st.checkbox("Show data frame"):
  df = pd.DataFrame(
  np.random.randn(2,10),
  columns = ['a','b','c']
  )
