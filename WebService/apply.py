import streamlit as st
import numpy as np
import pandas as pd

st.write(""" 
양승연
""")

#df = pd.read_csv("output.csv")
x = st.slider('x') # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.write("안성현")

# You can access the value at any point with:
st.session_state.name