
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import streamlit as st
import datetime as datetime
import plotly.graph_objects as go
import plotly.express as px 
import pandas_datareader.data as web

plt.style.use('dark_background')

st.set_page_config(page_title='Trading App',layout='wide',page_icon= "heavy_dollar_sign")

st.title("Trading Guide App :bar_chart:")

st.header("We provide the Greatest platform for you to collect all information prior to investing in the stocks.")

st.image("app.jpeg", caption="Trading App", width='stretch')

st.markdown("##We provide the following services")

st.markdown("##:one: Stock Information")
st.write("Through this page , you can see all the information about stock.")

st.markdown("##:two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 days based on hsitoricalstock data and advanced forecasting models")

st.markdown("##:three: CAPM Return")
st.write("Discover how the Capital Asset Pricing Model (CAPM) calculates the expected return of different  stock asset based on its rsik and return")

st.markdown("##:four: CAPM Beta")
st.write("Calculates Beta  and  Expected Return for Individual stocks")


























