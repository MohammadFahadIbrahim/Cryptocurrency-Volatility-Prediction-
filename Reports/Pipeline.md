#  Pipeline Architecture

## 1. Overview
The project follows a modular ML pipeline ensuring clarity, reproducibility, and scalability.

---

## 2. Pipeline Flow

---

## 3. Data Handling
- Missing values handled with forward/backward fill.
- Numerical features scaled using `StandardScaler`.
- Features aggregated per `symbol` and `date` for time consistency.

---

## 4. Scalability
This design allows:
- Switching models easily (e.g., XGBoost, LSTM).
- Adding new data sources.
- Integrating automated retraining pipelines.
