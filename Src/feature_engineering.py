import numpy as np

def add_features(df):
    df['daily_return'] = (df['close'] - df['open']) / df['open']
    df['vol_7d']  = df.groupby('symbol')['daily_return'].rolling(7, min_periods=1).std().reset_index(0,drop=True)
    df['liquidity_ratio'] = df['volume'] / df['market_cap'].replace({0:np.nan})
    df['ma7']  = df.groupby('symbol')['close'].rolling(7, min_periods=1).mean().reset_index(0,drop=True)
    df['ma30'] = df.groupby('symbol')['close'].rolling(30, min_periods=1).mean().reset_index(0,drop=True)
    return df
