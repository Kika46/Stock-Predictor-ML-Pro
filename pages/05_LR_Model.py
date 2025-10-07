
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import streamlit as st
from datetime import datetime,timedelta
import statsmodels.api as sn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config("Stock Prediction - Linear Regression",layout="wide")
st.title("📈 Linear Regression Stock Prediction")

col1,col2,col3 = st.columns([1,1,1])

with col1:
    ticker = st.text_input('Stock Name','TSLA')

with col2:
    days_to_predict = st.number_input("Days to predict into future",1,365)

with col3:
    n_lags = st.slider("Number of Past Days to Use (lags)",1,60,5)


data = yf.download(ticker, period="2y", interval="1d")
data = data[['Close']].reset_index()

for i in range(1, n_lags + 1):
    data[f'lag_{i}'] = data['Close'].shift(i)


data = data.dropna()

x = data[[f'lag_{i}' for i in range(1, n_lags + 1)]]
y = data['Close']

X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size = 0.2, random_state = 0)

model = LinearRegression()
model.fit(X_train, Y_train)

y_test_pred = model.predict(X_test)

y_train_pred = model.predict(X_train)

r2_score(Y_test,y_test_pred,)

r2_score(Y_train,y_train_pred)

st.write(f"R² on Training Data: {r2_score(Y_train, y_train_pred):.3f}")
st.write(f"R² on Test Data: {r2_score(Y_test, y_test_pred):.3f}")
st.write(f"RMSE on Test Data: {np.sqrt(mean_squared_error(Y_test, y_test_pred)):.2f}")

future_prices = []
last_values = np.array(x.iloc[-1]).flatten()  # ensure 1D

for _ in range(days_to_predict):
    pred = model.predict(last_values.reshape(1, -1))[0]
    future_prices.append(pred)
    last_values = np.append(last_values[1:], pred)



future_dates = [data['Date'].iloc[-1] + timedelta(days=i) for i in range(1, days_to_predict+1)]
future_df = pd.DataFrame({'Date': future_dates, 'Predicted Close': future_prices})

st.subheader("🔮 Future Price Predictions")
st.dataframe(future_df)


plt.figure(figsize=(12,5))
plt.plot(data['Date'], data['Close'], label='Actual', color='blue')
plt.plot(future_dates, future_prices, linestyle='--', label='Predicted', color='red')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(f"{ticker} Price Prediction using {n_lags}-day Lag Model")
plt.legend()
plt.grid(True)
st.pyplot(plt)






































