Stock-Predictor-ML-Pro 🧠📈
A comprehensive Streamlit application for advanced Financial Analysis and Stock Price Forecasting.

This tool combines classic financial methods with cutting-edge Machine Learning and Deep Learning, providing powerful, interactive stock market insights.

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
