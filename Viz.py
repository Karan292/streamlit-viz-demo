import streamlit as st
import pandas as pd
import numpy as np


st.title("Data Visualization with Streamlit")

data = pd.DataFrame({
    "numbers":[1,2,3,4,5],
    'values':[10,20,30,40,50]
})

st.write("Here is a simple DataFrame:")
st.dataframe(data)

st.write("Line Chart:")
st.line_chart(data["values"])

st.write("Bar Chart:")
st.bar_chart(data["values"])

st.write("Area Chart:")
st.area_chart(data["values"])

