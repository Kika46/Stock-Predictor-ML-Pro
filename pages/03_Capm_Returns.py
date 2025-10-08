
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import streamlit as st
import datetime as datetime
import pandas_datareader.data as web
import capm_functions

plt.style.use('dark_background')

st.set_page_config(page_title='Capital Asset Pricing model',layout='wide',page_icon= "chart_with_upwards_icon")
st.title("Capital Asset Pricing model")

#Getting input from a user
col1,col2 = st.columns([2,1])

with col1:
  stocks_list = st.multiselect("Choose 4 stocks",["AAPL","MGM","GOOG","MSFT","GME","AMZN","NVDA","TSLA"],["TSLA","AAPL","AMZN","MSFT"])

with col2:
  year = st.number_input("Number of years",1,10) 

 #Downloading data for S&P 500
try:
    end = datetime.date.today()
    start = datetime.date(datetime.date.today().year - year,
                          datetime.date.today().month,
                          datetime.date.today().day)

    SP5002 = yf.download("^GSPC", start, end)["Close"]

    stocks_df = pd.DataFrame()
    for stock in stocks_list:
        data = yf.download(stock, period=f"{year}y")
        stocks_df[stock] = round(data["Close"], 2)
        stocks_df.dropna(inplace=True)

    stocks_df.reset_index(inplace=True)
    stocks_df["Date"] = stocks_df["Date"].dt.date

    SP5002.reset_index(inplace=True)
    SP5002["Date"] = SP5002["Date"].dt.date

    stocks_df = pd.merge(stocks_df, SP5002, on="Date", how="inner")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("Top 5 heads")
        st.dataframe(stocks_df.head(), use_container_width=True)

    with col2:
        st.markdown("Bottom 5 tails")
        st.dataframe(stocks_df.tail(), use_container_width=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("Price of all the stocks")
        st.plotly_chart(capm_functions.interactive_plot(stocks_df))

    with col2:
        st.markdown("Price of all the stocks (after Normalizing)")
        st.plotly_chart(capm_functions.interactive_plot(
            capm_functions.normalize(stocks_df)))

    stocks_daily_return = capm_functions.daily_return(stocks_df)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### Beta Table")
        st.dataframe(capm_functions.calculate_beta(stocks_daily_return))

    with col2:
        st.markdown("### Expected Return Table (in %)")
        capm_df = capm_functions.calculate_capm_returns(stocks_daily_return)
        st.dataframe(capm_df.style.format({"Expected Return": "{:.2f}%"}))

except Exception as e:
    st.error(f"⚠️ Something went wrong: {e}")








