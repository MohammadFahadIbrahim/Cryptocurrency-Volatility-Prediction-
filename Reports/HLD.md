#  High Level Design (HLD)

## 1. Objective
The goal of this project is to predict the **7-day volatility** of cryptocurrencies using historical data such as price, volume, and market capitalization.

---

## 2. System Overview
The system is built as a modular ML pipeline consisting of:

| Stage | Description |
|-------|--------------|
| Data Ingestion | Load daily OHLCV (Open, High, Low, Close, Volume) data. |
| Preprocessing | Handle missing values, clean columns, normalize numeric features. |
| Feature Engineering | Add volatility, moving averages, liquidity ratio. |
| Model Training | Train Random Forest Regressor to predict future volatility. |
| Model Evaluation | Evaluate using MAE, RMSE, and R² score. |
| Deployment | Deploy locally using Streamlit app for testing predictions. |

---

## 3. Architecture Diagram (Conceptual)

---

## 4. Tools and Libraries
- **Python 3**
- **Pandas, NumPy** – data cleaning and manipulation
- **Scikit-learn** – model building and evaluation
- **Matplotlib, Seaborn** – EDA and visualization
- **Streamlit** – interactive deployment

---

## 5. Output
A trained Random Forest model capable of predicting cryptocurrency volatility trends.
