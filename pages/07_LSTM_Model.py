
import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from datetime import timedelta
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

st.set_page_config("Stock Prediction - Using LSTM", layout="wide")
st.title("📈 LSTM Stock Price Prediction model")

col1,col2,col3 = st.columns([1,1,1])

with col1:
    ticker = st.text_input('Stock Name','TSLA')

with col2:
    days_to_predict = st.number_input("Days to predict into future",1,365)

with col3:
    n_lags = st.slider("Number of Past Days to Use (lags)",1,60,20)

data = yf.download(ticker, period="2y", interval="1d")
data = data[['Close']]
st.write("data:", data.tail())


scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data)

generator = TimeseriesGenerator(scaled_data, scaled_data, length=n_lags, batch_size=32)

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(n_lags, 1)),
    LSTM(50),
    Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(generator, epochs=20, verbose=0)

last_sequence = scaled_data[-n_lags:]

future_prices = []

for _ in range(days_to_predict):
    next_price = model.predict(last_sequence.reshape(1, n_lags, 1))[0,0]
    future_prices.append(next_price)
    last_sequence = np.append(last_sequence[1:], next_price).reshape(-1,1)

future_prices = scaler.inverse_transform(np.array(future_prices).reshape(-1,1))
future_dates = [data.index[-1] + timedelta(days=i) for i in range(1, days_to_predict+1)]
future_df = pd.DataFrame({"Date": future_dates, "Predicted Close": future_prices.flatten()})

st.subheader("🔮 Future Price Predictions")
st.dataframe(future_df)

fig, ax = plt.subplots(figsize=(12,5))
ax.plot(data.index, data['Close'], color='blue', label='Actual Price')
ax.plot(future_df['Date'], future_df['Predicted Close'], color='red', linestyle='--', label='Predicted Price')
ax.set_title(f"{ticker} Stock Price Prediction")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()
ax.grid(True)
fig.tight_layout()
st.pyplot(fig)








































