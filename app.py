import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Compare price distribution between manufacturers')

df = pd.read_csv('vehicles_us.csv')
days_price = px.scatter(df, x='days_listed', y='price', title='Days listed vs price of vehicle', labels={'x': 'days listed', 'y': 'Price $'}, opacity=0.7)

# Plot scatter plot for days listed vs price
# Remove outliers
days_price_df = df[df['price']<100000]
days_price_df = days_price_df[days_price_df['days_listed']<200]

days_price = px.scatter(days_price_df, x='days_listed', y='price', title='Days listed vs price of vehicle', labels={'x': 'days listed', 'y': 'Price $'}, opacity=0.7)
days_price.show()

st.write(days_price)


# Plot price vs odometer
# remove rows where odometer is NaN
odo_df = df.dropna(subset=['odometer'])

# Remove outliers for odometer above 400,000
odo_df = odo_df[odo_df['odometer']<400000]

# Remove outliers for price over $100k
odo_df = odo_df[odo_df['price']<60000]

odo_df.info()
odo_plot = px.scatter(odo_df, x='odometer', y='price', title='Odometer vs price of vehicle', labels={'x': 'Odometer', 'y': 'Price $'}, opacity=0.7)
odo_plot.show()

st.write(odo_plot)



