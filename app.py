import streamlit as st
import pandas as pd
import numpy as np

def load_data():
    df = pd.read_csv('C:/Users/matth/OneDrive/Desktop/DA/Personal_Projects/Business/cloudservicesfin-eda/CloudServiceFinancials.csv')
    st.write(df)

load_data()