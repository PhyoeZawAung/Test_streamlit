import streamlit as st
import pandas as pd
arr = [1,2,3,4]
arr1 = [5,6,7,8]
df = pd.DataFrame({
    'first column': arr,
    'second column':arr1
    })
df
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
