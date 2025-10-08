
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import streamlit as st
import datetime as datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ta.momentum import RSIIndicator
from ta.trend import MACD
import pandas_datareader.data as web


plt.style.use('dark_background')

st.set_page_config(page_title='Stock Analysis',layout='wide',page_icon= "heavy_dollar_sign")



st.title("Stock Analysis")


col1,col2,col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Stock_ticker","TSLA")

with col2:
    start_date = st.date_input("Choose start Date",datetime.date(today.year -1, today.month,today.day))

with col3:
    End_date = st.date_input("Choose End Date",datetime.date(today.year, today.month,today.day))

st.subheader(ticker)

stock = yf.Ticker(ticker)

st.write(stock.info.get("longBusinessSummary","N/A"))
st.write("**Sector:**",stock.info.get('sector',"NA"))
st.write("**Full Time Exmployees:**",stock.info.get('fullTimeEmployees',"N/A"))
st.write("**Website:**",stock.info.get('website',"N/A"))


col1,col2 = st.columns(2)

with col1:
    info = stock.info
    df = pd.DataFrame({'Metric': ['Market Cap', 'Beta', 'Trailing EPS', 'PE'], 'Value': [info.get('marketCap', 'N/A'),info.get('beta', 'N/A'),info.get('trailingEps', 'N/A'),info.get('trailingPE','N/A')]})
    st.dataframe(df, use_container_width=True, hide_index=True)


with col2:
    df2 = pd.DataFrame({
        'Metric': ['Quick Ratio', 'Revenue per Share', 'Profit Margins', 'Debt to Equity', 'Return on Equity'],
        'Value': [info.get('quickRatio', 'N/A'),info.get('revenuePerShare', 'N/A'),info.get('profitMargins', 'N/A'),info.get('debtToEquity', 'N/A'),info.get('returnOnEquity', 'N/A')]}) 
    st.dataframe(df2, use_container_width=True, hide_index=True)




data = yf.download(ticker,start = start_date,end = End_date)
print(data)

col1,col2,col3 = st.columns(3)

Daily_change = data['Close'].pct_change()*100
Daily_change = Daily_change.dropna()

today_price = round(float(data['Close'].iloc[-1]),2)
today_change = round(float(Daily_change.iloc[-1]),2)

col1.metric("Today's Price", f"${today_price}",f"{today_change}%")

last_10_days_data = data.tail(10).sort_index(ascending=False).round(2)
last_10_days_data.index = last_10_days_data.index.date
st.table(last_10_days_data)







periods = ['5D','1M','3M','6M','YTD','1Y','2Y','5Y','10Y','20Y','MAX']
cols = st.columns(len(periods))
num_period = ''
for i, p in enumerate(periods):
    if cols[i].button(p):
        num_period = p.lower()


if num_period == '':
    num_period = '1y'



col1,col2,col3 = st.columns([1,1,4])
with col1 :
    chart_type = st.selectbox('',['Candle','Line'])

with col2 :
    if chart_type == 'Candle':

        indicator = st.selectbox('', ['RSI','MACD'])

    else :
        indicator = st.selectbox('', ['RSI','MACD','Moving Average'])



data = yf.Ticker(ticker).history(period=num_period)


data['RSI'] = RSIIndicator(data['Close'], window=14).rsi()

macd_indicator = MACD(close=data['Close'], window_slow=26, window_fast=12, window_sign=9)
data['MACD'] = macd_indicator.macd()
data['Signal'] = macd_indicator.macd_signal()
data['MACD_Hist'] = macd_indicator.macd_diff()

data['MA20'] = data['Close'].rolling(20).mean()

show_volume = st.checkbox("Show Volume", value=True)
rows = 2 if show_volume else 1
titles = ["Price + " + indicator]
if show_volume:
    titles.append("Volume")


fig = make_subplots(rows=rows, cols=1, shared_xaxes=True, subplot_titles=titles)


if chart_type == "Candle" and indicator == "RSI":
    fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'],
                                 low=data['Low'], close=data['Close'], name="Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['RSI'], mode="lines", name="RSI", line=dict(color="blue")), row=1, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=1, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=1, col=1)

if chart_type == "Candle" and indicator == "MACD":
    fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'],
                                 low=data['Low'], close=data['Close'], name="Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['MACD'], mode="lines", name="MACD", line=dict(color="purple")), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['Signal'], mode="lines", name="Signal", line=dict(color="pink")), row=1, col=1)

if chart_type == "Line" and indicator == "RSI":
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode="lines", name="Price", line=dict(color="cyan")), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['RSI'], mode="lines", name="RSI", line=dict(color="blue")), row=1, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=1, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=1, col=1)

if chart_type == "Line" and indicator == "MACD":
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode="lines", name="Price", line=dict(color="cyan")), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['MACD'], mode="lines", name="MACD", line=dict(color="purple")), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['Signal'], mode="lines", name="Signal", line=dict(color="pink")), row=1, col=1)

if chart_type == "Line" and indicator == "Moving Average":
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode="lines", name="Price", line=dict(color="cyan")), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], mode="lines", name="20-day MA", line=dict(color="orange")), row=1, col=1)

if show_volume:
    fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name="Volume", marker_color="gray", opacity=0.4), row=rows, col=1)


fig.update_layout(height=600, width=900, template="plotly_dark", hovermode="x unified",
                  title=f"{ticker} - {chart_type} + {indicator}")


st.plotly_chart(fig, use_container_width=True)




