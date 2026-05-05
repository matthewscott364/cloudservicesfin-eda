import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Cloud Services Financial EDA", layout="wide")

st.title("Cloud Services Financial EDA")

df = pd.read_csv(r"C:\Users\matth\OneDrive\Desktop\DA\Personal_Projects\Business\cloudservicesfin-eda\CloudServicesFinancials.csv")

st.sidebar.header("Filters")

companies = st.sidebar.multiselect(
    "Select Companies",
    options=df["Company"].unique(),
    default=df["Company"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (int(df["Year"].min()), int(df["Year"].max()))
)

filtered_df = df[
    (df["Company"].isin(companies)) &
    (df["Year"].between(year_range[0], year_range[1]))
]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

col1, col2, col3, = st.columns(3)

col1.metric("Total Net Sales ($MM)", f"{filtered_df['Net Sales ($MM)'].sum():,.0f}")
col2.metric("Total Operating Expenses ($MM)", f"{filtered_df['Operating Expenses ($MM)'].sum():,.0f}")
col3.metric("Total Operating Income ($MM)", f"{filtered_df['Operating Income ($MM)'].sum():,.0f}")

st.subheader("Net Sales by Year")
sales_chart = filtered_df.pivot_table(
    index="Year",
    columns="Company",
    values="Net Sales ($MM)",
    aggfunc="sum"
)

st.line_chart(sales_chart)

st.subheader("Operating Income by Year")
income_chart = filtered_df.pivot_table(
    index="Year",
    columns="Company",
    values="Operating Income ($MM)",
    aggfunc="sum"
)

st.line_chart(income_chart)

st.subheader("Operating Expenses by Year")
expense_chart = filtered_df.pivot_table(
    index="Year",
    columns="Company",
    values="Operating Expenses ($MM)",
    aggfunc="sum"
)

st.bar_chart(expense_chart)