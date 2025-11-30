# 🏁 Final Project Report — Cryptocurrency Volatility Prediction

## 1. Objective
To build a machine learning model that predicts **7-day volatility** of cryptocurrencies based on daily trading and market data.

---

## 2. Methodology
1. Data Cleaning and Preprocessing
2. Feature Engineering (volatility, moving averages, liquidity ratio)
3. Model Training using Random Forest
4. Evaluation with MAE, RMSE, and R²
5. Deployment using Streamlit interface

---

## 3. Model Results

| Metric | Description | Value |
|:--------|:-------------|:-------|
| MAE | Mean Absolute Error | 0.035549 |
| RMSE | Root Mean Square Error | 0.142268 |
| R² | Coefficient of Determination | -7.5304 |

---

## 4. Key Findings
- Volatility increases when market cap decreases.
- Liquidity ratio helps stabilize predictions.
- Random Forest gives robust performance on historical data.

---

## 5. Conclusion
The model can effectively predict crypto volatility trends.
Potential improvements include:
- Using LSTM models for temporal patterns
- Integrating real-time APIs for live forecasting

---

## 6. Tools Used
Python • Pandas • NumPy • Matplotlib • Scikit-learn • Streamlit
