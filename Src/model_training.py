import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
from data_preprocessing import load_and_clean
from feature_engineering import add_features

def train_and_save():
    df = load_and_clean('crypto_volatility_project/data/dataset.csv')
    df = add_features(df)
    features = ['open','high','low','close','volume','market_cap','daily_return','liquidity_ratio','ma7','ma30']
    df = df.dropna(subset=features + ['vol_7d'])
    X, y = df[features], df['vol_7d']
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)
    split = int(0.8*len(Xs))
    X_train, X_test = Xs[:split], Xs[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    print(f"MAE={mae:.6f}, RMSE={rmse:.6f}, R²={r2:.4f}")
    joblib.dump(model,'crypto_volatility_project/models/crypto_volatility_model.pkl')
    joblib.dump(scaler,'crypto_volatility_project/models/scaler.pkl')

if __name__ == "__main__":
    train_and_save()
