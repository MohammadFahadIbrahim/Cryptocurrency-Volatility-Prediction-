import streamlit as st
import pandas as pd
import joblib

st.title("Cryptocurrency Volatility Predictor")
model = joblib.load('models/crypto_volatility_model.pkl')
scaler = joblib.load('models/scaler.pkl')

open_ = st.number_input("Open", 0.0)
high = st.number_input("High", 0.0)
low = st.number_input("Low", 0.0)
close = st.number_input("Close", 0.0)
volume = st.number_input("Volume", 0.0)
market_cap = st.number_input("Market Cap", 0.0)

if st.button("Predict"):
    daily_return = (close - open_) / open_ if open_ else 0
    df = pd.DataFrame([[open_, high, low, close, volume, market_cap, daily_return, volume/market_cap if market_cap else 0, close, close]],
                      columns=['open','high','low','close','volume','market_cap','daily_return','liquidity_ratio','ma7','ma30'])
    X_scaled = scaler.transform(df)
    pred = model.predict(X_scaled)
    st.success(f"Predicted 7-day volatility: {pred[0]:.6f}")
