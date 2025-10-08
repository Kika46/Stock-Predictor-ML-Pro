import streamlit as st
import datetime
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import capm_functions   

plt.style.use('dark_background')

st.set_page_config(page_title="CAPM Beta", layout="wide")
st.title("📉 Calculate Beta and Return for Individual Stock")

# --- Inputs ---
stock = st.selectbox("Choose a stock", ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"])
years = st.number_input("Number of years", 1, 10, 3)

try:
    # --- Dates ---
    end = datetime.date.today()
    start = datetime.date(end.year - years, end.month, end.day)

    # --- Download Data ---
    stock_data = yf.download(stock, start, end)[["Close"]]
    stock_data.rename(columns={"Close": stock}, inplace=True)

    sp500 = yf.download("^GSPC", start, end)[["Close"]]
    sp500.rename(columns={"Close": "^GSPC"}, inplace=True)

    # Merge into single DataFrame
    df = stock_data.join(sp500, how="inner").dropna()

    # --- Daily Returns ---
    returns = df.pct_change().dropna()

    # --- CAPM Calculations ---
    beta_df = capm_functions.calculate_beta(returns)
    capm_df = capm_functions.calculate_capm_returns(returns)



    # --- Regression Plot ---
    st.subheader(f"Regression Plot: {stock} vs Market (^GSPC)")
    plt.figure(figsize=(8,6))
    sns.regplot(x=returns["^GSPC"], y=returns[stock], line_kws={"color":"red"})
    plt.xlabel("Market Return (^GSPC)")
    plt.ylabel(f"{stock} Return")
    plt.title(f"CAPM Regression for {stock}\nBeta = {beta_df['Beta'][0]:.2f}")
    st.pyplot(plt)

except Exception as e:
    st.error(f"⚠️ {e}")

