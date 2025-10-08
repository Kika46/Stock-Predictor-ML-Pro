import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import yfinance as yf
import streamlit as st
from datetime import timedelta,datetime
from statsmodels.tsa.arima.model import ARIMA

plt.style.use('dark_background')

st.set_page_config("Stock Prediction - ARIMA", layout="wide")
st.title("📈 ARIMA Stock Prediction")

col1,col2,col3 = st.columns([1,1,1])

with col1:
    ticker = st.text_input('Stock Name', 'TSLA')

with col2:
    days_to_predict = st.number_input("Days to predict into future",1,365)

data = yf.download(ticker, period="2y", interval="1d")
data = data[['Close']].reset_index()

st.subheader("🔮 ARIMA Forecast")


model = ARIMA(data['Close'], order=(5,1,0))  
model_fit = model.fit()                     
forecast = model_fit.forecast(steps=int(days_to_predict))  


last_date = data['Date'].iloc[-1]
future_dates = [last_date + timedelta(days=i) for i in range(1, int(days_to_predict)+1)]

arima_df = pd.DataFrame({'Date': future_dates, 'Predicted Close': forecast})

plt.figure(figsize=(12,5))
plt.plot(data['Date'], data['Close'], label='Actual', color='blue')
plt.plot(arima_df['Date'], arima_df['Predicted Close'], linestyle='--', color='orange', label='ARIMA Forecast')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(f"{ticker} ARIMA Forecast ({days_to_predict} Days)")
plt.legend()
plt.grid(True)
st.pyplot(plt)


col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("🔮 Future Forecast Table")
    st.dataframe(arima_df)

with col2:
    st.subheader("Forecast Chart")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
    x=arima_df['Date'],
    y=arima_df['Predicted Close'],
    mode='lines+markers',
    name='Forecast',
    line=dict(color='orange', dash='dash')))
    st.plotly_chart(fig, use_container_width=True)

    

