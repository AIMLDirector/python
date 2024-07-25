import pandas as pd
import numpy as np
import streamlit as st

st.title("This is to view the Graph")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

pdread = st.file_uploader("upload your file", type={"csv", "text"})
pdloaded = pd.read_csv(pdread)
st.line_chart(pdread)

st.write(pdloaded)

