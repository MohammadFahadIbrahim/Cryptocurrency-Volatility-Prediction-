#  Exploratory Data Analysis (EDA) Report

## 1. Dataset Overview
- Source: Provided crypto historical dataset
- Records: ~18,000 daily entries
- Features: `date`, `symbol`, `open`, `high`, `low`, `close`, `volume`, `market_cap`
- Additional engineered columns: `daily_return`, `vol_7d`, `ma7`, `liquidity_ratio`

---

## 2. Data Quality
| Column | Missing Values | Type |
|---------|----------------|------|
| open | 0 | float |
| high | 0 | float |
| low | 0 | float |
| close | 0 | float |
| volume | few | float |
| market_cap | few | float |

---

## 3. Key Insights
- Price columns (`open`, `high`, `low`, `close`) are **highly correlated**.
- **Volume** and **Market Cap** show right-skewed distributions.
- Smaller coins exhibit **higher volatility** than large-cap ones.
- Liquidity ratio (volume/market_cap) inversely relates to volatility.

---

## 4. Visual Summary
- **Line Plot:** Closing Price Trend for sample crypto.
- **Histogram:** Volume and Market Cap distributions are heavy-tailed.
- **Heatmap:** High correlation between price-related features.
- **Boxplot:** Volatility outliers visible in smaller tokens.

---

## 5. Observations
- Missing values filled using forward/backward fill.
- Feature scaling necessary due to large range differences.
- Time-based sorting improves consistency for volatility calculations.
