
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

#Function to create interactive plotly charts

def interactive_plot(df):
  fig = go.Figure()
  for i in df.columns[1:]:
    fig.add_scatter(x=df['Date'], y=df[i], name=i)
  fig.update_layout(width = 450, margin = dict(l=20,r=20,t=20,b=20),legend = dict(orientation = 'h', yanchor = 'bottom', y = 1.02, xanchor = 'right', x = 1))
  return fig

#funtion to normalise price based on the initial price

def normalize(df_2):
    df_normalize = df_2.copy()
    for i in df_normalize.columns[1:]:
        df_normalize[i] = df_normalize[i] / df_normalize[i].iloc[0]  # fixed typo
    return df_normalize
    

#Calculating Daily returns

def daily_return(df_2):
    df_daily_return = df_2.copy()
    for i in df_daily_return.columns[1:]:
       df_daily_return[i] = df_daily_return[i].pct_change() 
    return df_daily_return.dropna()
    
def calculate_beta(df_daily):
    df_copy = df_daily.copy()         
    beta_list = []

    # Loop through all stock columns except 'Date' and 'GSPC'
    for stock in df_copy.columns[1:]:
        if stock != "^GSPC":           
            X = df_copy["^GSPC"].values.reshape(-1, 1) 
            Y = df_copy[stock].values                
            model = LinearRegression().fit(X, Y)       
            beta = model.coef_[0]                       
            beta_list.append([stock, beta])             

    return pd.DataFrame(beta_list, columns=["Stock", "Beta"])


def calculate_capm_returns(df_daily, rf=0.0418):   
    df_copy = df_daily.copy()
    Rm = df_copy["^GSPC"].mean() * 252   

    capm_list = []   

    for stock in df_copy.columns[1:]:
        if stock != "^GSPC":
            X = df_copy["^GSPC"].values.reshape(-1, 1)
            Y = df_copy[stock].values
            model = LinearRegression().fit(X, Y)
            beta = model.coef_[0]
            capm = rf + beta * (Rm - rf)   # CAPM formula
            capm_list.append([stock, capm])

    capm_df = pd.DataFrame(capm_list, columns=["Stock", "Expected Return"])
    capm_df["Expected Return"] = capm_df["Expected Return"] * 100  # to %
    return capm_df

        


