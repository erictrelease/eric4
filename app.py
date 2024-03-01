import streamlit as st
import pandas as pd
import plotly.express


df = pd.read_csv('vehicles_us.csv')

st.header('Compare price distribution between manufacturers')

