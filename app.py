import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\matth\OneDrive\Desktop\DA\Personal_Projects\Business\cloudservicesfin-eda\CloudServiceFinancials.csv')
st.line_chart(df)
st.write("Data Preview", df.head())
