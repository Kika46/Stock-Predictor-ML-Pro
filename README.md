Stock-Predictor-ML-Pro 🧠📈
A comprehensive Streamlit application for advanced Financial Analysis and Stock Price Forecasting.
This tool combines classic financial methods with cutting-edge Machine Learning and Deep Learning, providing powerful, interactive stock market insights.

# Stock-Predictor-ML-Pro 🧠📈

A comprehensive **Streamlit** application for advanced **Financial Analysis** and **Stock Price Forecasting**.

This tool combines classic financial methods with cutting-edge Machine Learning and Deep Learning, providing powerful, interactive stock market insights.

## 🔗 View the Live Application!

Click the badge below to access the full multi-page application, hosted for free on Streamlit Community Cloud:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://stock-predictor-pro.streamlit.app/)

## ✨ Key Features & Technology Stack

### Core Functionality
* **Multi-Model Forecasting:** Includes predictions using **Linear Regression**, **ARIMA Time Series**, and **LSTM (Deep Learning)** models, allowing users to compare different predictive methods.
* **CAPM Analysis:** Calculates **Beta** and **Expected Returns** for individual stocks and portfolios, providing a measure of systematic risk.
* **Technical Analysis:** Interactive charts featuring essential indicators like RSI, MACD, and Moving Averages.
* **Customized Page Flow:** The sidebar navigation is organized using numerical prefixes (e.g., `01_`, `02_`, etc.) to guide users through the analysis steps.

### Tech Stack
| Category | Libraries/Tools |
| :--- | :--- |
| **App Framework** | Streamlit |
| **Forecasting** | TensorFlow (LSTM), scikit-learn (Linear Regression), statsmodels (ARIMA) |
| **Data & Finance**| yfinance, pandas, pandas-datareader, ta |
| **Deployment** | GitHub, Streamlit Community Cloud (Free Hosting) |

---

## 💻 Local Setup & Deployment Notes

1.  **Clone Repository:** `git clone https://github.com/kika46/Stock-Predictor-ML-Pro.git`
2.  **Install Dependencies:** `pip install -r requirements.txt`
3.  **Run Locally:** `streamlit run "01_Trading_App.py"`

**Important Deployment Note:** This repository includes the necessary **`.streamlit/config.toml`** file, which forces the deployment environment to use **Python 3.11** for stable compatibility with TensorFlow and scikit-learn.






✨ Key Features & Technology Stack
Core Functionality
Multi-Model Forecasting: Includes predictions using Linear Regression, ARIMA Time Series, and LSTM (Deep Learning) models.

CAPM Analysis: Calculates Beta and Expected Returns for individual stocks and portfolios, providing a measure of systematic risk.

Technical Analysis: Interactive charts featuring essential indicators like RSI, MACD, and Moving Averages.

Customized Page Flow: Uses Streamlit's multi-page feature with numerical prefixes (e.g., 01_, 02_) to ensure a smooth, ordered user experience in the sidebar.

Tech Stack
Category	Libraries/Tools
App Framework	Streamlit
Forecasting	TensorFlow (for LSTM), scikit-learn (for Linear Regression), statsmodels (for ARIMA)
Data & Finance	yfinance, pandas, ta
Deployment	GitHub, Streamlit Community Cloud (Free Hosting)

💻 Setup & Deployment
Clone Repository: git clone https://github.com/your-username/Stock-Predictor-ML-Pro.git

Install Dependencies: pip install -r requirements.txt

Run Locally: streamlit run "01_Home_Page.py"
