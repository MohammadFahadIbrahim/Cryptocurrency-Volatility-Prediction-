#  Low Level Design (LLD)

## 1. Module Breakdown

| Module | File | Key Functions |
|--------|------|----------------|
| Data Preprocessing | `data_preprocessing.py` | `load_and_clean()` – cleans dataset, fills missing values |
| Feature Engineering | `feature_engineering.py` | `add_features()` – creates new variables like daily_return, ma7, vol_7d |
| Model Training | `model_training.py` | `train_and_save()` – scales features, trains model, saves artifacts |
| Evaluation | integrated in training | calculates MAE, RMSE, and R² |
| Deployment | `streamlit_app.py` | simple UI for real-time prediction |

---

## 2. Data Flow

---

## 3. Implementation Details
- **Input:** Historical OHLCV + market_cap
- **Processing:** StandardScaler normalization
- **Algorithm:** RandomForestRegressor (n_estimators=200)
- **Output:** Predicted 7-day volatility value

---

## 4. Storage
- Models saved as `.pkl` in `models/`
- Dataset stored in `data/`
- Reports in `reports/`

---

## 5. Future Enhancements
- Integrate LSTM models for time-series prediction
- Add live crypto data via API
- Implement automated retraining pipeline
