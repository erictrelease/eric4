import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Compare price distribution between manufacturers')

df = pd.read_csv('vehicles_us.csv')
days_price = px.scatter(df, x='days_listed', y='price', title='Days listed vs price of vehicle', labels={'x': 'days listed', 'y': 'Price $'}, opacity=0.7)

st.write(days_price)



